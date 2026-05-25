from django.contrib import admin
from .models import WebUrlResource

@admin.register(WebUrlResource)
class WebUrlResourceAdmin(admin.ModelAdmin):
    list_display = ('link', 'description', 'resources', 'created_at', 'updated_at')
    search_fields = ('link', 'description', 'resources')
