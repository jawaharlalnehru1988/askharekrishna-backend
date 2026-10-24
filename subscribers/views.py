import json
import base64
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Subscriber, SubscriberQuizAttempt
from .serializers import (
    SubscriberSerializer,
    SubscriberQuizAttemptSerializer,
    SubscriberQuizAttemptCreateSerializer,
    GoogleAuthSerializer,
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


def _find_subscriber(raw_identifier: str):
    trimmed = (raw_identifier or '').strip()
    if not trimmed:
        return None

    if '@' in trimmed:
        subscriber = Subscriber.objects.filter(email__iexact=trimmed).first()
        if subscriber:
            return subscriber

    subscriber = Subscriber.objects.filter(google_id=trimmed).first()
    if subscriber:
        return subscriber

    for candidate in _phone_candidates(trimmed):
        subscriber = Subscriber.objects.filter(phone_number=candidate).first()
        if subscriber:
            return subscriber

    return Subscriber.objects.filter(email__iexact=trimmed).first()


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all().order_by('-created_at')
    serializer_class = SubscriberSerializer

    def get_permissions(self):
        if self.action in ['create', 'google_auth']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated = serializer.validated_data

        phone = validated.get('phone_number')
        email = validated.get('email')

        if not phone and not email:
            return Response(
                {'detail': 'Either phone_number or email is required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        subscriber = None
        if email:
            subscriber = Subscriber.objects.filter(email__iexact=email).first()
        if not subscriber and phone:
            subscriber = _find_subscriber(phone)

        created = False
        if subscriber:
            subscriber.name = validated.get('name') or subscriber.name
            subscriber.language = validated.get('language') or subscriber.language
            subscriber.place = validated.get('place') or subscriber.place
            if phone:
                existing_phone_sub = Subscriber.objects.filter(phone_number=phone).exclude(id=subscriber.id).first()
                if existing_phone_sub:
                    if not existing_phone_sub.email and not existing_phone_sub.google_id:
                        existing_phone_sub.delete()
                        subscriber.phone_number = phone
                    else:
                        # Keep existing phone as is or allow update
                        subscriber.phone_number = phone
                else:
                    subscriber.phone_number = phone
            if email:
                subscriber.email = email
            subscriber.save()
        else:
            subscriber = Subscriber.objects.create(
                name=validated.get('name', 'Devotee'),
                phone_number=phone or None,
                email=email or None,
                language=validated.get('language', 'en'),
                place=validated.get('place', ''),
                is_active=validated.get('is_active', True),
            )
            created = True

        output = self.get_serializer(subscriber)
        return Response(
            output.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )

    @action(detail=False, methods=['post'], url_path='google-auth', permission_classes=[permissions.AllowAny])
    def google_auth(self, request):
        serializer = GoogleAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        email = (data.get('email') or '').strip().lower()
        name = (data.get('name') or '').strip()
        picture = (data.get('picture') or '').strip()
        google_id = (data.get('google_id') or '').strip()
        language = (data.get('language') or 'en').strip()

        # If credential JWT string is passed directly, decode it
        credential = data.get('credential')
        if credential and not email:
            try:
                parts = credential.split('.')
                if len(parts) >= 2:
                    padding = '=' * (4 - len(parts[1]) % 4)
                    payload_json = base64.urlsafe_b64decode(parts[1] + padding).decode('utf-8')
                    payload = json.loads(payload_json)
                    email = (payload.get('email') or email).lower()
                    name = name or payload.get('name', '')
                    picture = picture or payload.get('picture', '')
                    google_id = google_id or payload.get('sub', '')
            except Exception:
                pass

        if not email and not google_id:
            return Response({'detail': 'Email or Google ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        subscriber = None
        if google_id:
            subscriber = Subscriber.objects.filter(google_id=google_id).first()
        if not subscriber and email:
            subscriber = Subscriber.objects.filter(email__iexact=email).first()

        created = False
        if subscriber:
            if name:
                subscriber.name = name
            if picture:
                subscriber.picture = picture
            if google_id:
                subscriber.google_id = google_id
            if email and not subscriber.email:
                subscriber.email = email
            if language:
                subscriber.language = language
            subscriber.save()
        else:
            subscriber = Subscriber.objects.create(
                email=email or None,
                name=name or (email.split('@')[0] if email else 'Devotee'),
                picture=picture,
                google_id=google_id or None,
                language=language or 'en',
                is_active=True,
            )
            created = True

        output = self.get_serializer(subscriber)
        return Response(output.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)


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

        identifier = (
            validated.get('identifier')
            or validated.get('email')
            or validated.get('phone_number')
            or ''
        )
        subscriber = _find_subscriber(identifier)
        if not subscriber:
            return Response(
                {'identifier': 'Subscriber not found. Please sign in first.'},
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
        identifier = (
            request.query_params.get('email')
            or request.query_params.get('phone_number')
            or request.query_params.get('identifier')
            or ''
        ).strip()
        if not identifier:
            return Response(
                {'identifier': 'email, phone_number, or identifier query parameter is required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        subscriber = _find_subscriber(identifier)
        if not subscriber:
            return Response(
                {'detail': 'Subscriber not found. Please sign in first.'},
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

