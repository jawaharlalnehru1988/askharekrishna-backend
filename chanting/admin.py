from django import forms
from django.contrib import admin
from django.utils.html import format_html
from .models import ChantingArticle, MainTopicTranslation

@admin.register(MainTopicTranslation)
class MainTopicTranslationAdmin(admin.ModelAdmin):
    list_display = ('english_topic', 'language', 'translated_topic')
    list_filter = ('language',)
    search_fields = ('english_topic', 'translated_topic')



CHANTING_LANGUAGE_NAMES = {
    "en": "English",
    "ta": "Tamil",
    "hi": "Hindi",
    "te": "Telugu",
    "kn": "Kannada",
    "ml": "Malayalam",
    "bn": "Bengali",
}

CHANTING_LANGUAGE_CHOICES = tuple((code, f"{name} ({code})") for code, name in CHANTING_LANGUAGE_NAMES.items())

class ChantingArticleTranslationInline(admin.StackedInline):
    model = ChantingArticle
    fk_name = 'parent'
    extra = 1
    fields = ('language', 'mainTopic', 'subTopic', 'article', 'slug', 'audioPath')
    prepopulated_fields = {'slug': ('mainTopic', 'subTopic')}

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        parent_language = obj.language if obj else 'en'
        
        class CustomInlineForm(formset.form):
            def __init__(self, *args, **kwargs_form):
                super().__init__(*args, **kwargs_form)
                choices = [(code, name) for code, name in CHANTING_LANGUAGE_CHOICES if code != parent_language]
                self.fields['language'].widget = forms.Select(choices=choices)
                
        formset.form = CustomInlineForm
        return formset


@admin.register(ChantingArticle)
class ChantingArticleAdmin(admin.ModelAdmin):
    inlines = [ChantingArticleTranslationInline]

    class Media:
        js = ('chanting/js/admin_translations.js?v=2',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(parent__isnull=True)

    list_display = ('subTopic', 'slug', 'mainTopic', 'language', 'order', 'audio_player')
    
    def audio_player(self, obj):
        if obj.audioPath:
            return format_html(
                '<audio controls style="width: 200px; height: 35px;"><source src="{}" type="audio/mpeg">Your browser does not support the audio element.</audio>',
                obj.audioPath.url
            )
        return '-'
    audio_player.short_description = 'Audio'

    list_filter = ('language', 'mainTopic', 'subTopic')
    search_fields = ('mainTopic', 'subTopic', 'article')
    fields = ('language', 'mainTopic', 'subTopic', 'article', 'slug', 'order', 'audioPath')
    prepopulated_fields = {'slug': ('mainTopic', 'subTopic')}
    ordering = ('order', 'mainTopic', 'subTopic')

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'language':
            kwargs['widget'] = forms.Select(choices=CHANTING_LANGUAGE_CHOICES)
        return super().formfield_for_dbfield(db_field, request, **kwargs)
