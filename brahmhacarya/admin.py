from django.contrib import admin
from .models import BrahmhacaryaArticle, BrahmhacaryaRegistration


@admin.register(BrahmhacaryaArticle)
class BrahmhacaryaArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'order', 'title', 'category', 'slug', 'is_published', 'published_at', 'created_at')
    list_editable = ('order',)
    list_filter = ('language', 'category', 'is_published', 'created_at', 'published_at')
    search_fields = ('title', 'slug', 'language', 'category', 'excerpt', 'content', 'audioUrl')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Article', {
            'fields': ('language', 'order', 'title', 'category', 'slug', 'excerpt', 'content', 'audioUrl', 'featured_image')
        }),
        ('Publishing', {
            'fields': ('is_published', 'published_at')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    ordering = ('language', 'category', 'order', '-published_at', '-created_at')


@admin.register(BrahmhacaryaRegistration)
class BrahmhacaryaRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phone_number', 'whatsapp_number', 'created_at')
    search_fields = ('full_name', 'email', 'phone_number', 'whatsapp_number')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
