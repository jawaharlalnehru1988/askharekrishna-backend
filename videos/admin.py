from django.contrib import admin
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'book_name',
        'chapter_number',
        'sloka_number',
        'sloka_start',
        'language',
        'video_file',
        'created_at',
    )
    list_filter = ('book_name', 'chapter_number', 'language')
    search_fields = ('video_file', 'sloka_number')
    ordering = ('book_name', 'chapter_number', 'sloka_start', 'language')
    readonly_fields = ('sloka_start', 'created_at', 'updated_at')
