from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model
from .models import UserProfile, UserModuleSubscription

User = get_user_model()

class CustomUserCreateSerializer(UserCreateSerializer):
    phone_number = serializers.CharField(required=False, allow_blank=True)
    module_name = serializers.CharField(write_only=True, required=False, allow_blank=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name', 'phone_number', 'module_name')

    def create(self, validated_data):
        phone_number = validated_data.pop('phone_number', '')
        module_name = validated_data.pop('module_name', '')
        
        # If username is not provided, use email
        if 'username' not in validated_data or not validated_data['username']:
            validated_data['username'] = validated_data.get('email')

        user = super().create(validated_data)
        
        UserProfile.objects.create(user=user, phone_number=phone_number)
        
        if module_name:
            UserModuleSubscription.objects.create(user=user, module_name=module_name)
            
        return user


class UserModuleSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModuleSubscription
        fields = ('module_name', 'role', 'joined_at')


class CustomUserSerializer(UserSerializer):
    phone_number = serializers.CharField(source='profile.phone_number', read_only=True)
    subscriptions = UserModuleSubscriptionSerializer(many=True, read_only=True)

    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'phone_number', 'subscriptions')
