from django import forms
from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from django.utils.html import format_html, format_html_join
from django.utils.text import slugify
from .models import (
    BrahmhacaryaArticle,
    BrahmhacaryaRegistration,
    BrahmhacaryaQuestion,
    BrahmhacaryaQuestionOption,
)


BRAHMHACARYA_LANGUAGE_NAMES = {
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

BRAHMHACARYA_LANGUAGE_CHOICES = tuple(
    (code, f"{name} ({code})") for code, name in BRAHMHACARYA_LANGUAGE_NAMES.items()
)


class BrahmhacaryaQuestionInline(admin.StackedInline):
    model = BrahmhacaryaQuestion
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


@admin.register(BrahmhacaryaArticle)
class BrahmhacaryaArticleAdmin(admin.ModelAdmin):
    change_form_template = 'admin/brahmhacarya/brahmhacaryaarticle/change_form.html'
    list_display = ('title', 'category', 'language', 'mcq_exists', 'id', 'audio_path', 'image_preview')
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
    inlines = [BrahmhacaryaQuestionInline]

    def _build_transliterated_slug(self, title: str, target_language: str) -> str:
        base_slug = slugify(title, allow_unicode=True)[:280] or 'brahmhacarya-article'
        base_slug = f'{base_slug}-{target_language}'
        base_slug = base_slug[:280]
        slug = base_slug
        counter = 1

        while BrahmhacaryaArticle.objects.filter(slug=slug).exists():
            suffix = f'-{counter}'
            slug = f'{base_slug[:280 - len(suffix)]}{suffix}'
            counter += 1

        return slug

    def mcq_exists(self, obj):
        return obj.questions.exists()

    mcq_exists.boolean = True
    mcq_exists.short_description = 'Is MCQ exists?'

    def audio_path(self, obj):
        if obj.audioUrl:
            return format_html('<a href="{}" target="_blank" rel="noopener noreferrer">{}</a>', obj.audioUrl.url, obj.audioUrl.name.split('/')[-1])
        return '-'

    audio_path.short_description = 'audioPath'

    def image_preview(self, obj):
        if obj.featured_image:
            return format_html(
                '<img src="{}" style="max-height:60px;max-width:90px;border-radius:4px;object-fit:cover;" />',
                obj.featured_image.url,
            )
        return '-'

    image_preview.short_description = 'Image preview'

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'language':
            kwargs['widget'] = forms.Select(choices=BRAHMHACARYA_LANGUAGE_CHOICES)
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                '<int:pk>/translate-article/',
                self.admin_site.admin_view(self.translate_article_view),
                name='brahmhacarya_brahmhacaryaarticle_translate_article',
            ),
            path(
                '<int:pk>/generate-mcqs/',
                self.admin_site.admin_view(self.generate_mcqs_view),
                name='brahmhacarya_brahmhacaryaarticle_generate_mcqs',
            ),
        ]
        return custom + urls

    def translate_article_view(self, request, pk):
        article = self.get_object(request, pk)
        if article is None:
            messages.error(request, 'Brahmhacarya article not found.')
            return HttpResponseRedirect('../../')

        if request.method != 'POST':
            return HttpResponseRedirect(f'../../{pk}/change/')

        if (article.language or '').lower() != 'en':
            messages.error(request, 'Translation is allowed only from English source articles.')
            return HttpResponseRedirect(f'../../{pk}/change/')

        target_language = (request.POST.get('target_language') or '').strip().lower()
        allowed_codes = {code for code, _ in BRAHMHACARYA_LANGUAGE_CHOICES}
        if target_language not in allowed_codes:
            messages.error(request, 'Please select a valid target language.')
            return HttpResponseRedirect(f'../../{pk}/change/')

        if target_language == 'en':
            messages.error(request, 'Target language cannot be English.')
            return HttpResponseRedirect(f'../../{pk}/change/')

        if not article.content or not article.content.strip():
            messages.error(request, 'Source article has no content text to translate.')
            return HttpResponseRedirect(f'../../{pk}/change/')

        replace_existing = (request.POST.get('_replace_existing_translation') or '').strip() in {'1', 'true', 'yes'}

        try:
            from .translation_generator import translate_brahmhacarya_article

            translated = translate_brahmhacarya_article(
                title=article.title,
                excerpt=article.excerpt or '',
                content=article.content,
                target_language=target_language,
            )

            translated_title = (translated.get('title') or '').strip()
            translated_excerpt = (translated.get('excerpt') or '').strip()
            translated_content = (translated.get('content') or '').strip()

            if not translated_title or not translated_content:
                raise ValueError('AI translation returned empty required fields.')

            generated_slug = self._build_transliterated_slug(translated_title, target_language)

            existing_article = BrahmhacaryaArticle.objects.filter(
                language=target_language,
                category=article.category,
                order=article.order,
            ).order_by('id').first()

            if existing_article and not replace_existing:
                messages.warning(
                    request,
                    (
                        f'A {target_language} translation already exists (Article ID: {existing_article.pk}). '
                        'Click Translate again and confirm to replace it.'
                    ),
                )
                return HttpResponseRedirect(
                    f'../../{pk}/change/?replace_lang={target_language}&replace_article_id={existing_article.pk}'
                )

            if existing_article and replace_existing:
                existing_article.title = translated_title
                existing_article.excerpt = translated_excerpt
                existing_article.content = translated_content
                existing_article.slug = generated_slug
                existing_article.order = article.order
                existing_article.language = target_language
                existing_article.category = article.category
                existing_article.is_published = article.is_published
                existing_article.published_at = article.published_at
                if article.audioUrl:
                    existing_article.audioUrl = article.audioUrl
                if article.featured_image:
                    existing_article.featured_image = article.featured_image
                existing_article.save()

                messages.success(
                    request,
                    (
                        f'Existing {target_language} translation was replaced successfully. '
                        'Review and edit it if needed.'
                    ),
                )
                return HttpResponseRedirect(reverse('admin:brahmhacarya_brahmhacaryaarticle_change', args=[existing_article.pk]))

            translated_article = BrahmhacaryaArticle(
                title=translated_title,
                excerpt=translated_excerpt,
                content=translated_content,
                slug=generated_slug,
                order=article.order,
                language=target_language,
                category=article.category,
                is_published=article.is_published,
                published_at=article.published_at,
            )
            if article.audioUrl:
                translated_article.audioUrl = article.audioUrl
            if article.featured_image:
                translated_article.featured_image = article.featured_image
            translated_article.save()

            messages.success(
                request,
                'Translated article created successfully. Review and edit it if needed.',
            )
            return HttpResponseRedirect(reverse('admin:brahmhacarya_brahmhacaryaarticle_change', args=[translated_article.pk]))
        except ValueError as exc:
            messages.error(request, f'Article translation failed: {exc}')
        except Exception as exc:
            messages.error(request, f'Unexpected error during translation: {exc}')

        return HttpResponseRedirect(f'../../{pk}/change/')

    def generate_mcqs_view(self, request, pk):
        from .mcq_generator import generate_mcqs, save_mcqs

        article = self.get_object(request, pk)
        if article is None:
            messages.error(request, 'Brahmhacarya article not found.')
            return HttpResponseRedirect('../../')

        if not article.content or not article.content.strip():
            messages.error(request, 'This article has no content to generate MCQs from.')
            return HttpResponseRedirect(f'../../{pk}/change/')

        try:
            questions = generate_mcqs(article.content, language=article.language or 'en')
            count = save_mcqs(article, questions)
            messages.success(
                request,
                f'Successfully generated and saved {count} MCQ questions for "{article.title}".',
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
        replace_lang = (request.GET.get('replace_lang') or '').strip().lower()
        replace_article_id = (request.GET.get('replace_article_id') or '').strip()
        context['translation_language_choices'] = BRAHMHACARYA_LANGUAGE_CHOICES
        if replace_lang:
            context['replace_translation_language'] = replace_lang
            context['replace_translation_language_name'] = dict(BRAHMHACARYA_LANGUAGE_CHOICES).get(replace_lang, replace_lang)
        if replace_article_id.isdigit():
            context['replace_translation_article_id'] = replace_article_id
        return super().render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)


@admin.register(BrahmhacaryaRegistration)
class BrahmhacaryaRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phone_number', 'whatsapp_number', 'created_at')
    search_fields = ('full_name', 'email', 'phone_number', 'whatsapp_number')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)


class BrahmhacaryaQuestionOptionInline(admin.TabularInline):
    model = BrahmhacaryaQuestionOption
    extra = 4
    max_num = 4
    fields = ('order', 'option_text', 'is_correct')
    ordering = ('order', 'id')


@admin.register(BrahmhacaryaQuestion)
class BrahmhacaryaQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'order', 'short_question', 'is_active', 'options_count')
    list_filter = ('is_active', 'article__language', 'article__category')
    search_fields = ('article__title', 'article__slug', 'question_text')
    ordering = ('article_id', 'order', 'id')
    inlines = [BrahmhacaryaQuestionOptionInline]

    def short_question(self, obj):
        text = (obj.question_text or '').strip()
        return text[:80] + ('...' if len(text) > 80 else '')

    short_question.short_description = 'Question'

    def options_count(self, obj):
        return obj.options.count()

    options_count.short_description = 'Options'


@admin.register(BrahmhacaryaQuestionOption)
class BrahmhacaryaQuestionOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'order', 'option_text', 'is_correct')
    list_filter = ('is_correct', 'question__article__language')
    search_fields = ('question__question_text', 'option_text', 'question__article__title')
    ordering = ('question_id', 'order', 'id')
