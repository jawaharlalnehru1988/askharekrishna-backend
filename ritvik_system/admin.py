from django.contrib import admin
from django.utils.html import format_html
from .models import (
    RitvikSection,
    RitvikSectionTranslation,
    RitvikQA,
    RitvikQATranslation,
)


class RitvikSectionTranslationInline(admin.StackedInline):
    model = RitvikSectionTranslation
    extra = 1
    fields = ('language', 'title', 'description')


@admin.register(RitvikSection)
class RitvikSectionAdmin(admin.ModelAdmin):
    list_display = ('section_number', 'get_title', 'slug', 'order', 'image', 'has_en', 'has_ta')
    list_display_links = ('section_number', 'get_title')
    search_fields = ('section_number', 'translations__title')
    fields = ('section_number', 'slug', 'order', 'image')
    ordering = ('order', 'section_number')
    inlines = [RitvikSectionTranslationInline]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('translations')

    def get_title(self, obj):
        trans = next((t for t in obj.translations.all() if t.language == 'en'), None)
        if not trans and obj.translations.exists():
            trans = obj.translations.first()
        return trans.title if trans else f"Section {obj.section_number}"
    get_title.short_description = 'Title'

    def has_en(self, obj):
        return any(t.language == 'en' for t in obj.translations.all())
    has_en.boolean = True
    has_en.short_description = 'En'

    def has_ta(self, obj):
        return any(t.language == 'ta' for t in obj.translations.all())
    has_ta.boolean = True
    has_ta.short_description = 'Ta'


class RitvikQATranslationInline(admin.StackedInline):
    model = RitvikQATranslation
    extra = 1
    fields = ('language', 'question', 'summary', 'answer', 'audioPath')


@admin.register(RitvikQA)
class RitvikQAAdmin(admin.ModelAdmin):
    list_display = (
        'question_code',
        'get_question_short',
        'section',
        'order',
        'image',
        'is_published',
        'has_en',
        'has_ta',
        'has_hi',
    )
    list_display_links = ('question_code', 'get_question_short')
    list_filter = ('section', 'is_published')
    search_fields = ('question_code', 'translations__question', 'translations__answer')
    fields = ('section', 'question_code', 'slug', 'order', 'image', 'is_published')
    ordering = ('section__section_number', 'order', 'id')
    inlines = [RitvikQATranslationInline]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('translations', 'section')

    def get_question_short(self, obj):
        trans = next((t for t in obj.translations.all() if t.language == 'en'), None)
        if not trans and obj.translations.exists():
            trans = obj.translations.first()
        if trans and trans.question:
            return trans.question[:80] + ('...' if len(trans.question) > 80 else '')
        return '-'
    get_question_short.short_description = 'Question'

    def has_en(self, obj):
        return any(t.language == 'en' and bool(t.question) for t in obj.translations.all())
    has_en.boolean = True
    has_en.short_description = 'En'

    def has_ta(self, obj):
        return any(t.language == 'ta' and bool(t.question) for t in obj.translations.all())
    has_ta.boolean = True
    has_ta.short_description = 'Ta'

    def has_hi(self, obj):
        return any(t.language == 'hi' and bool(t.question) for t in obj.translations.all())
    has_hi.boolean = True
    has_hi.short_description = 'Hi'
