from rest_framework import serializers
from .models import Subscriber, SubscriberQuizAttempt


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
        extra_kwargs = {
            'phone_number': {'validators': []},
        }


class SubscriberQuizAttemptSerializer(serializers.ModelSerializer):
    subscriber_phone_number = serializers.CharField(source='subscriber.phone_number', read_only=True)
    subscriber_name = serializers.CharField(source='subscriber.name', read_only=True)

    class Meta:
        model = SubscriberQuizAttempt
        fields = [
            'id',
            'subscriber',
            'subscriber_name',
            'subscriber_phone_number',
            'article_id',
            'article_title',
            'quiz_type',
            'score',
            'total_questions',
            'attempt_number',
            'created_at',
        ]
        read_only_fields = ('id', 'subscriber', 'subscriber_phone_number', 'attempt_number', 'created_at')


class SubscriberQuizAttemptCreateSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=20)
    article_id = serializers.IntegerField(min_value=1)
    article_title = serializers.CharField(max_length=255)
    quiz_type = serializers.ChoiceField(choices=['pooja_vidhi', 'story'])
    score = serializers.IntegerField(min_value=0)
    total_questions = serializers.IntegerField(min_value=1)

    def validate(self, attrs):
        if attrs['score'] > attrs['total_questions']:
            raise serializers.ValidationError({'score': 'Score cannot be greater than total_questions.'})
        return attrs
