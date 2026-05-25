from rest_framework import serializers
from .models import CookingArticle

class CookingArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookingArticle
        fields = '__all__'
