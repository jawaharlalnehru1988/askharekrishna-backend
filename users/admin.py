from django.contrib import admin
from .models import UserProfile, UserModuleSubscription

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')
    search_fields = ('user__username', 'phone_number', 'user__email')

@admin.register(UserModuleSubscription)
class UserModuleSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'module_name', 'role', 'joined_at')
    list_filter = ('module_name', 'role', 'joined_at')
    search_fields = ('user__username', 'module_name')
