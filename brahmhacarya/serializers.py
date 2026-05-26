from rest_framework import serializers
from .models import (
    BrahmhacaryaArticle,
    BrahmhacaryaRegistration,
    BrahmhacaryaQuestion,
    BrahmhacaryaQuestionOption,
)


class BrahmhacaryaQuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrahmhacaryaQuestionOption
        fields = ['id', 'order', 'option_text', 'is_correct']


class BrahmhacaryaQuestionSerializer(serializers.ModelSerializer):
    options = BrahmhacaryaQuestionOptionSerializer(many=True, read_only=True)

    class Meta:
        model = BrahmhacaryaQuestion
        fields = ['id', 'order', 'question_text', 'is_active', 'options']


class BrahmhacaryaArticleSerializer(serializers.ModelSerializer):
    questions = BrahmhacaryaQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = BrahmhacaryaArticle
        fields = [
            'id',
            'order',
            'title',
            'slug',
            'language',
            'category',
            'excerpt',
            'content',
            'audioUrl',
            'featured_image',
            'is_published',
            'questions',
            'published_at',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class BrahmhacaryaRegistrationSerializer(serializers.ModelSerializer):
    phoneNumber = serializers.CharField(source='phone_number')
    whatsappNumber = serializers.CharField(source='whatsapp_number')

    class Meta:
        model = BrahmhacaryaRegistration
        fields = ['id', 'full_name', 'email', 'phoneNumber', 'whatsappNumber', 'created_at']
        read_only_fields = ['id', 'created_at']
