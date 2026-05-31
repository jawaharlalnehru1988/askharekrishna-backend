from rest_framework import permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Subscriber, SubscriberQuizAttempt
from .serializers import (
    SubscriberSerializer,
    SubscriberQuizAttemptSerializer,
    SubscriberQuizAttemptCreateSerializer,
)


def _phone_candidates(raw_phone: str) -> list[str]:
    trimmed = (raw_phone or '').strip()
    if not trimmed:
        return []

    digits = ''.join(ch for ch in trimmed if ch.isdigit())
    candidates = [trimmed]

    if digits and digits not in candidates:
        candidates.append(digits)

    if len(digits) == 10:
        prefixed = f"+91{digits}"
        if prefixed not in candidates:
            candidates.append(prefixed)
        prefixed_plain = f"91{digits}"
        if prefixed_plain not in candidates:
            candidates.append(prefixed_plain)

    return candidates


def _find_subscriber_by_phone(raw_phone: str):
    for candidate in _phone_candidates(raw_phone):
        subscriber = Subscriber.objects.filter(phone_number=candidate).first()
        if subscriber:
            return subscriber
    return None


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all().order_by('-created_at')
    serializer_class = SubscriberSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated = serializer.validated_data

        subscriber, created = Subscriber.objects.update_or_create(
            phone_number=validated['phone_number'],
            defaults={
                'name': validated['name'],
                'language': validated['language'],
                'place': validated['place'],
                'is_active': validated.get('is_active', True),
            },
        )

        output = self.get_serializer(subscriber)
        return Response(
            output.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )


class SubscriberQuizAttemptViewSet(viewsets.ModelViewSet):
    queryset = SubscriberQuizAttempt.objects.select_related('subscriber').all().order_by('-created_at')
    serializer_class = SubscriberQuizAttemptSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def create(self, request, *args, **kwargs):
        input_serializer = SubscriberQuizAttemptCreateSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        validated = input_serializer.validated_data

        subscriber = _find_subscriber_by_phone(validated['phone_number'])
        if not subscriber:
            return Response(
                {'phone_number': 'Subscriber not found. Please subscribe first.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        previous_attempt_count = SubscriberQuizAttempt.objects.filter(
            subscriber=subscriber,
            quiz_type=validated['quiz_type'],
            article_id=validated['article_id'],
        ).count()

        attempt = SubscriberQuizAttempt.objects.create(
            subscriber=subscriber,
            article_id=validated['article_id'],
            article_title=validated['article_title'],
            quiz_type=validated['quiz_type'],
            score=validated['score'],
            total_questions=validated['total_questions'],
            attempt_number=previous_attempt_count + 1,
        )

        output = SubscriberQuizAttemptSerializer(attempt)
        return Response(output.data, status=status.HTTP_201_CREATED)


class SubscriberDashboardView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        phone_number = (request.query_params.get('phone_number') or '').strip()
        if not phone_number:
            return Response(
                {'phone_number': 'phone_number query parameter is required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        subscriber = _find_subscriber_by_phone(phone_number)
        if not subscriber:
            return Response(
                {'detail': 'Subscriber not found. Please subscribe first.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        attempts = SubscriberQuizAttempt.objects.filter(subscriber=subscriber).order_by('-created_at')

        return Response(
            {
                'subscriber': SubscriberSerializer(subscriber).data,
                'attempts': SubscriberQuizAttemptSerializer(attempts, many=True).data,
            },
            status=status.HTTP_200_OK,
        )
