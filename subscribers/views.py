from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from .models import Subscriber, SubscriberQuizAttempt
from .serializers import (
    SubscriberSerializer,
    SubscriberQuizAttemptSerializer,
    SubscriberQuizAttemptCreateSerializer,
)


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

        try:
            subscriber = Subscriber.objects.get(phone_number=validated['phone_number'])
        except Subscriber.DoesNotExist:
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
