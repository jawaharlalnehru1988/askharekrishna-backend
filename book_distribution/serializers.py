from rest_framework import serializers
from .models import BookDistribution

class BookDistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDistribution
        fields = '__all__'
