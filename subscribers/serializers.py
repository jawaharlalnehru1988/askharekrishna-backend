from rest_framework import serializers
from .models import Subscriber, SubscriberQuizAttempt


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
        extra_kwargs = {
            'phone_number': {'validators': [], 'required': False, 'allow_blank': True, 'allow_null': True},
            'email': {'validators': [], 'required': False, 'allow_blank': True, 'allow_null': True},
        }


class SubscriberQuizAttemptSerializer(serializers.ModelSerializer):
    subscriber_phone_number = serializers.CharField(source='subscriber.phone_number', read_only=True)
    subscriber_email = serializers.CharField(source='subscriber.email', read_only=True)
    subscriber_name = serializers.CharField(source='subscriber.name', read_only=True)
    subscriber_picture = serializers.CharField(source='subscriber.picture', read_only=True)

    class Meta:
        model = SubscriberQuizAttempt
        fields = [
            'id',
            'subscriber',
            'subscriber_name',
            'subscriber_email',
            'subscriber_phone_number',
            'subscriber_picture',
            'article_id',
            'article_title',
            'quiz_type',
            'score',
            'total_questions',
            'attempt_number',
            'created_at',
        ]
        read_only_fields = ('id', 'subscriber', 'subscriber_email', 'subscriber_phone_number', 'subscriber_name', 'subscriber_picture', 'attempt_number', 'created_at')


class SubscriberQuizAttemptCreateSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=254, required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    identifier = serializers.CharField(max_length=254, required=False, allow_blank=True)
    article_id = serializers.IntegerField(min_value=1)
    article_title = serializers.CharField(max_length=255)
    quiz_type = serializers.ChoiceField(choices=['pooja_vidhi', 'story'])
    score = serializers.IntegerField(min_value=0)
    total_questions = serializers.IntegerField(min_value=1)

    def validate(self, attrs):
        if attrs['score'] > attrs['total_questions']:
            raise serializers.ValidationError({'score': 'Score cannot be greater than total_questions.'})
        if not attrs.get('phone_number') and not attrs.get('email') and not attrs.get('identifier'):
            raise serializers.ValidationError({'identifier': 'Either email or phone_number is required.'})
        return attrs


class GoogleAuthSerializer(serializers.Serializer):
    credential = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    name = serializers.CharField(max_length=150, required=False, allow_blank=True)
    picture = serializers.CharField(max_length=500, required=False, allow_blank=True)
    google_id = serializers.CharField(max_length=255, required=False, allow_blank=True)
    language = serializers.CharField(max_length=80, required=False, default='en')

