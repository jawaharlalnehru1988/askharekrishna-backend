from django import forms
from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from django.utils.html import format_html, format_html_join
from .models import (
    DebateArticle,
    DebateCategory,
    DebateQuestion,
    DebateQuestionOption,
)


DEBATE_LANGUAGE_NAMES = {
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

DEBATE_LANGUAGE_CHOICES = tuple((code, f"{name} ({code})") for code, name in DEBATE_LANGUAGE_NAMES.items())


@admin.register(DebateCategory)
class DebateCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name', 'description')


class DebateArticleAdminForm(forms.ModelForm):
    class Meta:
        model = DebateArticle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        language_choices = list(DEBATE_LANGUAGE_CHOICES)
        current_language = (getattr(self.instance, 'language', '') or '').strip()
        if current_language and current_language not in {code for code, _ in language_choices}:
            language_choices.append((current_language, current_language))

        self.fields['language'].widget = forms.Select(choices=language_choices)
        if not self.instance or not self.instance.pk:
            self.fields['language'].initial = 'en'


class DebateQuestionInline(admin.StackedInline):
    model = DebateQuestion
    extra = 0
    max_num = 10
    fields = ('order', 'question_text', 'options_preview', 'is_active')
    readonly_fields = ('options_preview',)
    ordering = ('order', 'id')

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
    change_form_template = 'admin/debate/debatearticle/change_form.html'
    translation_language_choices = DEBATE_LANGUAGE_CHOICES
    form = DebateArticleAdminForm
    list_display = (
        'subTopic',
        'mcq_exists',
        'mainTopic',
        'debateCategory',
        'language',
        'articleImage',
        'audioPath',
        'created_at',
    )
    list_filter = ('language', 'debateCategory', 'mainTopic', 'subTopic')
    search_fields = ('mainTopic', 'subTopic', 'debateCategory__name', 'article')
    fields = (
        'language',
        'source_article',
        'debateCategory',
        'mainTopic',
        'subTopic',
        'article',
        'slug',
        'order',
        'articleImage',
        'audioPath',
    )
    readonly_fields = ('source_article',)
    ordering = ('order', 'mainTopic', 'subTopic')
    inlines = [DebateQuestionInline]

    def mcq_exists(self, obj):
        return obj.questions.exists()

    mcq_exists.boolean = True
    mcq_exists.short_description = 'MCQ Exists'

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                '<int:pk>/translate-article/',
                self.admin_site.admin_view(self.translate_article_view),
                name='debate_debatearticle_translate_article',
            ),
            path(
                '<int:pk>/generate-mcqs/',
                self.admin_site.admin_view(self.generate_mcqs_view),
                name='debate_debatearticle_generate_mcqs',
            ),
        ]
        return custom + urls

    def _resolve_source_article(self, article: DebateArticle) -> DebateArticle:
        return article.source_article or article

    def translate_article_view(self, request, pk):
        article = self.get_object(request, pk)
        if article is None:
            messages.error(request, 'Debate article not found.')
            return HttpResponseRedirect('../../')

        if request.method != 'POST':
            return HttpResponseRedirect(f'../../{pk}/change/')

        source_language = (article.language or '').strip().lower()
        if source_language not in DEBATE_LANGUAGE_NAMES:
            messages.error(request, 'Translation is supported only for configured source languages.')
            return HttpResponseRedirect(f'../../{pk}/change/')

        target_language = (request.POST.get('target_language') or '').strip().lower()
        allowed_codes = {code for code, _ in self.translation_language_choices}
        if target_language not in allowed_codes:
            messages.error(request, 'Please select a valid target language.')
            return HttpResponseRedirect(f'../../{pk}/change/')

        if target_language == source_language:
            messages.error(request, 'Source and target languages must be different.')
            return HttpResponseRedirect(f'../../{pk}/change/')

        if not article.article or not article.article.strip():
            messages.error(request, 'Source article has no text to translate.')
            return HttpResponseRedirect(f'../../{pk}/change/')

        replace_existing = (request.POST.get('_replace_existing_translation') or '').strip() in {'1', 'true', 'yes'}

        try:
            from .translation_generator import translate_debate_content

            translated = translate_debate_content(
                main_topic=article.mainTopic,
                sub_topic=article.subTopic,
                article_text=article.article,
                source_language=source_language,
                target_language=target_language,
            )

            translated_main_topic = (translated.get('mainTopic') or '').strip()
            translated_sub_topic = (translated.get('subTopic') or '').strip()
            translated_article = (translated.get('article') or '').strip()

            if not translated_main_topic or not translated_sub_topic or not translated_article:
                raise ValueError('AI translation returned empty required fields.')

            source_article = self._resolve_source_article(article)
            existing_article = DebateArticle.objects.filter(
                source_article=source_article,
                language=target_language,
            ).order_by('id').first()

            if existing_article and not replace_existing:
                language_name = dict(self.translation_language_choices).get(target_language, target_language)
                messages.warning(
                    request,
                    (
                        f'A {language_name} translation already exists '
                        f'(Article ID: {existing_article.pk}). Click Translate again and confirm to replace it.'
                    ),
                )
                return HttpResponseRedirect(
                    f'../../{pk}/change/?replace_lang={target_language}&replace_article_id={existing_article.pk}'
                )

            if existing_article and replace_existing:
                existing_article.source_article = source_article
                existing_article.debateCategory = article.debateCategory
                existing_article.mainTopic = translated_main_topic
                existing_article.subTopic = translated_sub_topic
                existing_article.article = translated_article
                existing_article.order = source_article.order
                if article.articleImage:
                    existing_article.articleImage = article.articleImage
                if article.audioPath:
                    existing_article.audioPath = article.audioPath
                existing_article.save()

                messages.success(
                    request,
                    (
                        f'Existing {target_language} translation was replaced successfully. '
                        'Review and edit it if needed.'
                    ),
                )
                return HttpResponseRedirect(reverse('admin:debate_debatearticle_change', args=[existing_article.pk]))

            translated_article_obj = DebateArticle(
                language=target_language,
                source_article=source_article,
                debateCategory=article.debateCategory,
                mainTopic=translated_main_topic,
                subTopic=translated_sub_topic,
                article=translated_article,
                order=source_article.order,
            )
            if article.articleImage:
                translated_article_obj.articleImage = article.articleImage
            if article.audioPath:
                translated_article_obj.audioPath = article.audioPath
            translated_article_obj.save()

            messages.success(
                request,
                'Translated article created successfully. Review and edit it if needed.',
            )
            return HttpResponseRedirect(reverse('admin:debate_debatearticle_change', args=[translated_article_obj.pk]))
        except ValueError as exc:
            messages.error(request, f'Article translation failed: {exc}')
        except Exception as exc:
            messages.error(request, f'Unexpected error during translation: {exc}')

        return HttpResponseRedirect(f'../../{pk}/change/')

    def generate_mcqs_view(self, request, pk):
        from .mcq_generator import generate_mcqs, save_mcqs

        article = self.get_object(request, pk)
        if article is None:
            messages.error(request, 'Debate article not found.')
            return HttpResponseRedirect('../../')

        if not article.article or not article.article.strip():
            messages.error(request, 'This article has no text to generate MCQs from.')
            return HttpResponseRedirect(f'../../{pk}/change/')

        try:
            questions = generate_mcqs(article.article, language=article.language or 'en')
            count = save_mcqs(article, questions)
            messages.success(
                request,
                f'Successfully generated and saved {count} MCQ questions for "{article.subTopic}".',
            )
        except ValueError as exc:
            messages.error(request, f'MCQ generation failed: {exc}')
        except Exception as exc:
            messages.error(request, f'Unexpected error while generating MCQs: {exc}')

        return HttpResponseRedirect(f'../../{pk}/change/')

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        if request.method == 'POST' and request.POST.get('_translate_article'):
            return self.translate_article_view(request, object_id)
        return super().changeform_view(request, object_id, form_url, extra_context)

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context['translation_language_choices'] = self.translation_language_choices
        source_obj = obj or context.get('original')
        source_language_code = ''
        if source_obj and getattr(source_obj, 'language', None):
            source_language_code = (source_obj.language or '').strip().lower()

        context['translation_source_language_code'] = source_language_code
        context['translation_source_language_name'] = DEBATE_LANGUAGE_NAMES.get(
            source_language_code,
            source_language_code,
        )
        context['translation_source_supported'] = source_language_code in DEBATE_LANGUAGE_NAMES
        replace_lang = (request.GET.get('replace_lang') or '').strip().lower()
        replace_article_id = (request.GET.get('replace_article_id') or '').strip()
        if replace_lang:
            context['replace_translation_language'] = replace_lang
            context['replace_translation_language_name'] = dict(self.translation_language_choices).get(replace_lang, replace_lang)
        if replace_article_id.isdigit():
            context['replace_translation_article_id'] = replace_article_id
            context['replace_translation_article_change_url'] = reverse(
                'admin:debate_debatearticle_change',
                args=[int(replace_article_id)],
            )
        return super().render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)


class DebateQuestionOptionInline(admin.TabularInline):
    model = DebateQuestionOption
    extra = 4
    max_num = 4
    fields = ('order', 'option_text', 'is_correct')
    ordering = ('order', 'id')


@admin.register(DebateQuestion)
class DebateQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'debate_article', 'order', 'short_question', 'is_active', 'options_count')
    list_filter = ('is_active', 'debate_article__language', 'debate_article__mainTopic')
    search_fields = ('debate_article__subTopic', 'debate_article__slug', 'question_text')
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
    list_filter = ('is_correct', 'question__debate_article__language')
    search_fields = ('question__question_text', 'option_text', 'question__debate_article__subTopic')
    ordering = ('question_id', 'order', 'id')
