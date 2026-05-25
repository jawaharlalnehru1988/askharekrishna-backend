from rest_framework import serializers
from .models import ChantingArticle

class ChantingArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChantingArticle
        fields = '__all__'
