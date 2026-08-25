from django import forms
from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from django.utils.html import format_html, format_html_join
from .models import (
    DebateArticle,
    DebateArticleTranslation,
    DebateCategory,
    DebateCategoryTranslation,
    DebateQuestion,
    DebateQuestionOption,
)

class DebateCategoryTranslationInline(admin.StackedInline):
    model = DebateCategoryTranslation
    extra = 1
    fields = ('language', 'translated_name', 'description')

@admin.register(DebateCategory)
class DebateCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'order')
    search_fields = ('name', 'description')
    ordering = ('order', 'name')
    inlines = [DebateCategoryTranslationInline]


class DebateArticleTranslationInline(admin.StackedInline):
    model = DebateArticleTranslation
    extra = 7
    max_num = 7
    fields = ('language', 'debateCategory', 'subTopic', 'article', 'audioPath', 'generate_mcq_action')
    readonly_fields = ('generate_mcq_action',)

    def generate_mcq_action(self, obj):
        if obj and obj.pk:
            url = reverse('admin:debate_debatearticle_generate_mcqs', args=[obj.article_parent_id, obj.language])
            return format_html(
                '<a href="{}" class="button" style="background:#417690;color:#fff;padding:6px 12px;border-radius:4px;text-decoration:none;" onclick="return confirm(\'This will REPLACE all existing MCQs for {}. Continue?\');">&#129302; Generate MCQs ({})</a>',
                url, obj.language.upper(), obj.language.upper()
            )
        return 'Save this translation first to generate MCQs.'
    generate_mcq_action.short_description = 'AI Actions'


class DebateQuestionInline(admin.StackedInline):
    model = DebateQuestion
    extra = 0
    max_num = 70
    fields = ('language', 'order', 'question_text', 'options_preview', 'is_active')
    readonly_fields = ('options_preview',)
    ordering = ('language', 'order', 'id')

    def options_preview(self, obj):
        if not obj or not obj.pk:
            return '-'

        options = obj.options.all().order_by('order')
        if not options:
            return '-'

        return format_html(
            '<ol style="margin:0;padding-left:18px;">{}</ol>',
            format_html_join(
                '',
                '<li>{} {}</li>',
                (
                    (
                        opt.option_text,
                        format_html('<strong style="color:#4caf50;">{}</strong>', '(Correct)')
                        if opt.is_correct else '',
                    )
                    for opt in options
                ),
            ),
        )

    options_preview.short_description = 'Options'


@admin.register(DebateArticle)
class DebateArticleAdmin(admin.ModelAdmin):
    list_display = (
        'get_subtopic',
        'articleImage',
        'order',
        'has_en',
        'has_en_mcq',
        'has_ta',
        'has_ta_mcq',
        'has_hi',
        'has_hi_mcq',
        'has_kn',
        'has_kn_mcq',
        'has_te',
        'has_te_mcq',
        'has_ml',
        'has_ml_mcq',
    )
    list_filter = ('translations__debateCategory',)
    search_fields = ('translations__debateCategory__name',)
    fields = (
        'slug',
        'order',
        'articleImage',
    )
    ordering = ('order', 'slug')
    inlines = [DebateArticleTranslationInline, DebateQuestionInline]
    change_form_template = 'admin/debate/debatearticle/change_form.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<path:object_id>/generate-mcqs/<str:language>/', self.admin_site.admin_view(self.generate_mcqs_view), name='debate_debatearticle_generate_mcqs'),
        ]
        return custom_urls + urls

    def generate_mcqs_view(self, request, object_id, language):
        article = self.get_object(request, object_id)
        if not article:
            return HttpResponseRedirect("..")

        translation = article.translations.filter(language=language).first()
        if not translation:
            self.message_user(request, f"No translation found for {language}. Cannot generate MCQs.", level=messages.ERROR)
            return HttpResponseRedirect("..")

        try:
            from .mcq_generator import generate_mcqs, save_mcqs
            questions_data = generate_mcqs(translation.article, language=language)
            count = save_mcqs(article, questions_data, language=language)
            self.message_user(request, f"Successfully generated {count} MCQs for {language}.", level=messages.SUCCESS)
        except Exception as e:
            self.message_user(request, f"Error generating MCQs: {e}", level=messages.ERROR)

        return HttpResponseRedirect("..")

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        if object_id:
            article = self.get_object(request, object_id)
            if article:
                extra_context['available_languages'] = [t.language for t in article.translations.all()]
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('translations', 'questions')

    def get_subtopic(self, obj):
        translations = list(obj.translations.all())
        t = next((t for t in translations if t.language == 'en'), None)
        if not t and translations:
            t = translations[0]
        return t.subTopic if t else '-'
    get_subtopic.short_description = 'Subtopic'

    def has_en(self, obj):
        return any(t.language == 'en' for t in obj.translations.all())
    has_en.boolean = True
    has_en.short_description = 'En'

    def has_en_mcq(self, obj):
        return any(q.language == 'en' for q in obj.questions.all())
    has_en_mcq.boolean = True
    has_en_mcq.short_description = 'En-MCQ'

    def has_ta(self, obj):
        return any(t.language == 'ta' for t in obj.translations.all())
    has_ta.boolean = True
    has_ta.short_description = 'Ta'

    def has_ta_mcq(self, obj):
        return any(q.language == 'ta' for q in obj.questions.all())
    has_ta_mcq.boolean = True
    has_ta_mcq.short_description = 'Ta-MCQ'

    def has_hi(self, obj):
        return any(t.language == 'hi' for t in obj.translations.all())
    has_hi.boolean = True
    has_hi.short_description = 'Hi'

    def has_hi_mcq(self, obj):
        return any(q.language == 'hi' for q in obj.questions.all())
    has_hi_mcq.boolean = True
    has_hi_mcq.short_description = 'Hi-MCQ'

    def has_kn(self, obj):
        return any(t.language == 'kn' for t in obj.translations.all())
    has_kn.boolean = True
    has_kn.short_description = 'Ka'

    def has_kn_mcq(self, obj):
        return any(q.language == 'kn' for q in obj.questions.all())
    has_kn_mcq.boolean = True
    has_kn_mcq.short_description = 'Ka-MCQ'

    def has_te(self, obj):
        return any(t.language == 'te' for t in obj.translations.all())
    has_te.boolean = True
    has_te.short_description = 'Tl'

    def has_te_mcq(self, obj):
        return any(q.language == 'te' for q in obj.questions.all())
    has_te_mcq.boolean = True
    has_te_mcq.short_description = 'Tl-MCQ'

    def has_ml(self, obj):
        return any(t.language == 'ml' for t in obj.translations.all())
    has_ml.boolean = True
    has_ml.short_description = 'Ml'

    def has_ml_mcq(self, obj):
        return any(q.language == 'ml' for q in obj.questions.all())
    has_ml_mcq.boolean = True
    has_ml_mcq.short_description = 'Ml-MCQ'




class DebateQuestionOptionInline(admin.TabularInline):
    model = DebateQuestionOption
    extra = 4
    max_num = 4
    fields = ('order', 'option_text', 'is_correct')
    ordering = ('order', 'id')


@admin.register(DebateQuestion)
class DebateQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'debate_article', 'order', 'short_question', 'is_active', 'options_count')
    list_filter = ('is_active', 'debate_article__translations__debateCategory__name')
    search_fields = ('debate_article__slug', 'question_text', 'debate_article__translations__debateCategory__name')
    ordering = ('debate_article_id', 'order', 'id')
    inlines = [DebateQuestionOptionInline]

    def short_question(self, obj):
        text = (obj.question_text or '').strip()
        return text[:80] + ('...' if len(text) > 80 else '')

    short_question.short_description = 'Question'

    def options_count(self, obj):
        return obj.options.count()

    options_count.short_description = 'Options'


@admin.register(DebateQuestionOption)
class DebateQuestionOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'order', 'option_text', 'is_correct')
    list_filter = ('is_correct',)
    search_fields = ('question__question_text', 'option_text')
    ordering = ('question_id', 'order', 'id')
