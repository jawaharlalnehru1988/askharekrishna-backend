from django import forms
from django.contrib import admin
from .models import ChantingArticle


CHANTING_LANGUAGE_NAMES = {
    "en": "English",
    "ta": "Tamil",
    "hi": "Hindi",
    "te": "Telugu",
    "kn": "Kannada",
    "ml": "Malayalam",
    "mr": "Marathi",
    "bn": "Bengali",
    "gu": "Gujarati",
    "pa": "Punjabi",
    "or": "Odia",
    "sa": "Sanskrit",
}

CHANTING_LANGUAGE_CHOICES = tuple((code, f"{name} ({code})") for code, name in CHANTING_LANGUAGE_NAMES.items())

@admin.register(ChantingArticle)
class ChantingArticleAdmin(admin.ModelAdmin):
    list_display = ('mainTopic', 'subTopic', 'language', 'order', 'slug', 'audioPath', 'created_at')
    list_filter = ('language', 'mainTopic', 'subTopic')
    search_fields = ('mainTopic', 'subTopic', 'article')
    fields = ('language', 'mainTopic', 'subTopic', 'article', 'slug', 'order', 'audioPath')
    prepopulated_fields = {'slug': ('mainTopic', 'subTopic')}
    ordering = ('order', 'mainTopic', 'subTopic')

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'language':
            kwargs['widget'] = forms.Select(choices=CHANTING_LANGUAGE_CHOICES)
        return super().formfield_for_dbfield(db_field, request, **kwargs)
