from rest_framework import serializers
from .models import Audio


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ['id', 'audioListId', 'title', 'description', 'language', 'duration', 'audioUrl', 'isPlaying', 'created_at', 'updated_at']
