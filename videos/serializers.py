from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    book_name_display = serializers.CharField(source='get_book_name_display', read_only=True)
    language_display = serializers.CharField(source='get_language_display', read_only=True)

    class Meta:
        model = Video
        fields = [
            'id',
            'video_file',
            'language',
            'language_display',
            'chapter_number',
            'sloka_number',
            'book_name',
            'book_name_display',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'book_name_display', 'language_display', 'created_at', 'updated_at']
