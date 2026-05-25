from django.contrib import admin
from django.utils.html import format_html
from .models import BookLibrary


@admin.register(BookLibrary)
class BookLibraryAdmin(admin.ModelAdmin):
    """Admin interface for DocumentLibrary."""
    
    list_display = [
        'title', 
        'author', 
        'category', 
        'language', 
        'book_format', 
        'pages',
        'downloads',
        'created_at'
    ]
    
    list_filter = [
        'category', 
        'language', 
        'book_format',
        'created_at'
    ]
    
    search_fields = [
        'title', 
        'author', 
        'description'
    ]
    
    readonly_fields = [
        'downloads',
        'created_at', 
        'updated_at',
        'cover_image_preview',
    ]
    
    fieldsets = (
        ('Document Information', {
            'fields': ('title', 'author', 'description')
        }),
        ('Classification', {
            'fields': ('category', 'language', 'book_format', 'pages')
        }),
        ('Files', {
            'fields': ('book_url', 'cover_image', 'cover_image_preview')
        }),
        ('Statistics', {
            'fields': ('downloads', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    list_per_page = 50
    
    def get_queryset(self, request):
        """Optimize query"""
        return super().get_queryset(request).select_related()

    def cover_image_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" alt="Cover Image" style="max-height: 180px; border-radius: 6px;" />',
                obj.cover_image.url,
            )
        return "No cover image"

    cover_image_preview.short_description = 'Cover image preview'
