from rest_framework import serializers
from .models import BookLibrary


class BookLibrarySerializer(serializers.ModelSerializer):
    """Serializer for Book Library API"""
    
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    book_format_display = serializers.CharField(source='get_book_format_display', read_only=True)
    
    class Meta:
        model = BookLibrary
        fields = [
            'id',
            'title',
            'author',
            'description',
            'language',
            'category',
            'category_display',
            'book_format',
            'book_format_display',
            'book_url',
            'pages',
            'cover_image',
            'downloads',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'downloads', 'created_at', 'updated_at']


class BookLibraryListSerializer(serializers.ModelSerializer):
    """Simplified serializer for list view"""
    
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    book_format_display = serializers.CharField(source='get_book_format_display', read_only=True)
    
    class Meta:
        model = BookLibrary
        fields = [
            'id',
            'title',
            'author',
            'description',
            'language',
            'category',
            'category_display',
            'book_format',
            'book_format_display',
            'cover_image',
            'downloads',
            'created_at',
        ]
