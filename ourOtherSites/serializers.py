from rest_framework import serializers
from .models import OurOtherSite


class OurOtherSiteSerializer(serializers.ModelSerializer):
    webUrl = serializers.URLField(source='web_url')
    featuresAvailable = serializers.CharField(source='features_available')

    class Meta:
        model = OurOtherSite
        fields = ['id', 'webUrl', 'purpose', 'featuresAvailable', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
