from django.contrib import admin
from .models import VideoGallery


@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'video', 'note', 'created_at')
    search_fields = ('note', 'description')
    readonly_fields = ('created_at', 'updated_at')
