from django.contrib import admin
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'book_name',
        'chapter_number',
        'sloka_number',
        'language',
        'video_file',
        'created_at',
    )
    list_filter = ('book_name', 'chapter_number', 'language')
    search_fields = ('video_file',)
    ordering = ('book_name', 'chapter_number', 'sloka_number', 'language')
    readonly_fields = ('created_at', 'updated_at')
