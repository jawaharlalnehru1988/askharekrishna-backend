from rest_framework import serializers
from .models import VaishnavaEtiquette

class VaishnavaEtiquetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaishnavaEtiquette
        fields = '__all__'
