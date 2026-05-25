from rest_framework import serializers
from .models import KirtanTutorial

class KirtanTutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = KirtanTutorial
        fields = '__all__'
