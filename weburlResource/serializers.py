from rest_framework import serializers
from .models import WebUrlResource

class WebUrlResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebUrlResource
        fields = '__all__'
