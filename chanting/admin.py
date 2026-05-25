from django.contrib import admin
from .models import ChantingArticle

@admin.register(ChantingArticle)
class ChantingArticleAdmin(admin.ModelAdmin):
    list_display = ('mainTopic', 'subTopic', 'language', 'order', 'slug', 'audioPath', 'created_at')
    list_filter = ('language', 'mainTopic', 'subTopic')
    search_fields = ('mainTopic', 'subTopic', 'article')
    fields = ('language', 'mainTopic', 'subTopic', 'article', 'slug', 'order', 'audioPath')
    prepopulated_fields = {'slug': ('mainTopic', 'subTopic')}
    ordering = ('order', 'mainTopic', 'subTopic')
