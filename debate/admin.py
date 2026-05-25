from django.contrib import admin
from .models import DebateArticle, DebateCategory


@admin.register(DebateCategory)
class DebateCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name', 'description')


@admin.register(DebateArticle)
class DebateArticleAdmin(admin.ModelAdmin):
    list_display = ('debateCategory', 'topic', 'subTopic', 'language', 'order', 'slug', 'audioPath', 'created_at')
    list_filter = ('language', 'debateCategory', 'topic', 'subTopic')
    search_fields = ('topic', 'subTopic', 'debateCategory__name', 'article')
    fields = ('language', 'debateCategory', 'topic', 'subTopic', 'article', 'slug', 'order', 'audioPath')
    ordering = ('order', 'topic', 'subTopic')
