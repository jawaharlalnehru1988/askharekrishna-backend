from rest_framework import serializers
from .models import VideoGallery


class VideoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGallery
        fields = ['id', 'video', 'note', 'description']
