from rest_framework import serializers
from .models import BrahmhacaryaArticle, BrahmhacaryaRegistration


class BrahmhacaryaArticleSerializer(serializers.ModelSerializer):
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
