from django.contrib import admin
from django import forms
from django.urls import path
from django.http import HttpResponseRedirect
from django.utils.html import format_html, format_html_join
from django.utils.text import slugify
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from .models import Story, StoryMainTopic, StoryQuestion, StoryQuestionOption


STORY_LANGUAGE_NAMES = {
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

STORY_LANGUAGE_CHOICES = tuple((code, f"{name} ({code})") for code, name in STORY_LANGUAGE_NAMES.items())


@admin.register(StoryMainTopic)
class StoryMainTopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name', 'description')


class StoryQuestionInline(admin.StackedInline):
    model = StoryQuestion
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
                        format_html(
                            '<strong style="color:#4caf50;">{}</strong>',
                            '(Correct)',
                        ) if opt.is_correct else '',
                    )
                    for opt in options
                ),
            ),
        )

    options_preview.short_description = 'Options'

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    change_form_template = 'admin/stories/story/change_form.html'
    translation_language_choices = (
        ('ta', 'Tamil'),
        ('te', 'Telugu'),
        ('kn', 'Kannada'),
        ('hi', 'Hindi'),
        ('ml', 'Malayalam'),
    )

    list_display = (
        'subTopic',
        'mcq_exists',
        'mainTopic',
        'language',
        'audioPath',
        'imagePath',
        'image_preview',
        'created_at',
    )
    list_filter = ('language', 'mainTopic', 'subTopic')
    search_fields = ('mainTopic__name', 'subTopic', 'article')
    fields = (
        'language',
        'mainTopic',
        'subTopic',
        'article',
        'slug',
        'order',
        'audioPath',
        'imagePath',
        'image_preview',
    )
    readonly_fields = ('image_preview',)
    ordering = ('order', 'mainTopic__name', 'subTopic')
    inlines = [StoryQuestionInline]

    def mcq_exists(self, obj):
        return obj.questions.exists()

    mcq_exists.boolean = True
    mcq_exists.short_description = 'MCQ Exists'

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                '<int:pk>/generate-mcqs/',
                self.admin_site.admin_view(self.generate_mcqs_view),
                name='stories_story_generate_mcqs',
            ),
            path(
                '<int:pk>/translate-story/',
                self.admin_site.admin_view(self.translate_story_view),
                name='stories_story_translate_story',
            ),
        ]
        return custom + urls

    def _build_transliterated_slug(self, main_topic_name: str, sub_topic: str, target_language: str) -> str:
        base_slug = slugify(f"{main_topic_name} {sub_topic}", allow_unicode=False) or "story"
        base_slug = f"{base_slug}-{target_language}"
        base_slug = base_slug[:280]
        slug = base_slug
        counter = 1

        while Story.objects.filter(slug=slug).exists():
            suffix = f"-{counter}"
            slug = f"{base_slug[:280 - len(suffix)]}{suffix}"
            counter += 1

        return slug

    def translate_story_view(self, request, pk):
        story = self.get_object(request, pk)
        if story is None:
            messages.error(request, "Story not found.")
            return HttpResponseRedirect("../../")

        if request.method != 'POST':
            return HttpResponseRedirect(f"../../{pk}/change/")

        if (story.language or '').lower() != 'en':
            messages.error(request, "Translation is allowed only from English source stories.")
            return HttpResponseRedirect(f"../../{pk}/change/")

        target_language = (request.POST.get('target_language') or '').strip().lower()
        allowed_codes = {code for code, _ in self.translation_language_choices}
        if target_language not in allowed_codes:
            messages.error(request, "Please select a valid target language.")
            return HttpResponseRedirect(f"../../{pk}/change/")

        if target_language == 'en':
            messages.error(request, "Target language cannot be English.")
            return HttpResponseRedirect(f"../../{pk}/change/")

        if not story.article or not story.article.strip():
            messages.error(request, "Source story has no article text to translate.")
            return HttpResponseRedirect(f"../../{pk}/change/")

        replace_existing = (request.POST.get('_replace_existing_translation') or '').strip() in {'1', 'true', 'yes'}

        try:
            from .translation_generator import translate_story_content

            translated = translate_story_content(
                main_topic=story.mainTopic.name if story.mainTopic else '',
                sub_topic=story.subTopic,
                article_text=story.article,
                target_language=target_language,
            )

            translated_main_topic = (translated.get('mainTopic') or '').strip()
            translated_sub_topic = (translated.get('subTopic') or '').strip()
            translated_article = (translated.get('article') or '').strip()

            if not translated_main_topic or not translated_sub_topic or not translated_article:
                raise ValueError("AI translation returned empty required fields.")

            translated_topic, _ = StoryMainTopic.objects.get_or_create(name=translated_main_topic)
            generated_slug = self._build_transliterated_slug(
                main_topic_name=translated_topic.name,
                sub_topic=translated_sub_topic,
                target_language=target_language,
            )

            existing_story = Story.objects.filter(language=target_language).filter(
                Q(mainTopic=translated_topic, subTopic__iexact=translated_sub_topic) |
                Q(slug=generated_slug)
            ).order_by('id').first()

            if existing_story and not replace_existing:
                language_name = dict(self.translation_language_choices).get(target_language, target_language)
                messages.warning(
                    request,
                    (
                        f"A {language_name} translation already exists "
                        f"(Story ID: {existing_story.pk}). Click Translate again and confirm to replace it."
                    ),
                )
                return HttpResponseRedirect(
                    f"../../{pk}/change/?replace_lang={target_language}&replace_story_id={existing_story.pk}"
                )

            if existing_story and replace_existing:
                existing_story.mainTopic = translated_topic
                existing_story.subTopic = translated_sub_topic
                existing_story.article = translated_article
                existing_story.order = story.order
                if story.imagePath:
                    existing_story.imagePath = story.imagePath
                existing_story.save()

                messages.success(
                    request,
                    (
                        f"Existing {target_language} translation was replaced successfully. "
                        "Review and edit it if needed."
                    ),
                )
                return HttpResponseRedirect(
                    reverse('admin:stories_story_change', args=[existing_story.pk])
                )

            translated_story = Story(
                language=target_language,
                mainTopic=translated_topic,
                subTopic=translated_sub_topic,
                article=translated_article,
                slug=generated_slug,
                order=story.order,
            )
            if story.imagePath:
                translated_story.imagePath = story.imagePath
            translated_story.save()

            messages.success(
                request,
                "Translated story created successfully. Review and edit it if needed.",
            )
            return HttpResponseRedirect(
                reverse('admin:stories_story_change', args=[translated_story.pk])
            )
        except ValueError as exc:
            messages.error(request, f"Story translation failed: {exc}")
        except Exception as exc:
            messages.error(request, f"Unexpected error during translation: {exc}")

        return HttpResponseRedirect(f"../../{pk}/change/")

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        if request.method == 'POST' and request.POST.get('_translate_story'):
            return self.translate_story_view(request, object_id)
        return super().changeform_view(request, object_id, form_url, extra_context)

    def generate_mcqs_view(self, request, pk):
        from .mcq_generator import generate_mcqs, save_mcqs
        story = self.get_object(request, pk)
        if story is None:
            messages.error(request, "Story not found.")
            return HttpResponseRedirect("../../")

        if not story.article or not story.article.strip():
            messages.error(request, "This story has no article text to generate MCQs from.")
            return HttpResponseRedirect(f"../../{pk}/change/")

        try:
            questions = generate_mcqs(story.article, language=story.language or "en")
            count = save_mcqs(story, questions)
            messages.success(
                request,
                f"Successfully generated and saved {count} MCQ questions for \"{story.subTopic}\"."
            )
        except ValueError as exc:
            messages.error(request, f"MCQ generation failed: {exc}")
        except Exception as exc:
            messages.error(request, f"Unexpected error while generating MCQs: {exc}")

        return HttpResponseRedirect(f"../../{pk}/change/")

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'language':
            kwargs['widget'] = forms.Select(choices=STORY_LANGUAGE_CHOICES)

        if db_field.name == 'article':
            kwargs['widget'] = forms.Textarea(
                attrs={
                    'rows': 20,
                    'cols': 200,
                    'class': 'vLargeTextField article-editor-fullwidth',
                    'style': 'width:calc(100vw - 560px);max-width:100%;min-width:780px;box-sizing:border-box;',
                }
            )
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context['translation_language_choices'] = self.translation_language_choices
        context['copy_image_from_story_id'] = request.GET.get('_copy_image_from_story_id', '')
        replace_lang = (request.GET.get('replace_lang') or '').strip().lower()
        replace_story_id = (request.GET.get('replace_story_id') or '').strip()
        if replace_lang:
            context['replace_translation_language'] = replace_lang
            context['replace_translation_language_name'] = dict(self.translation_language_choices).get(replace_lang, replace_lang)
        if replace_story_id.isdigit():
            context['replace_translation_story_id'] = replace_story_id
        return super().render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)

    def save_model(self, request, obj, form, change):
        if not change and not obj.imagePath:
            source_story_id = (request.POST.get('_copy_image_from_story_id') or '').strip()
            if source_story_id.isdigit():
                source_story = Story.objects.filter(pk=int(source_story_id), language='en').first()
                if source_story and source_story.imagePath:
                    obj.imagePath = source_story.imagePath
        super().save_model(request, obj, form, change)

    def image_preview(self, obj):
        if obj.imagePath:
            return format_html(
                '<img src="{}" style="max-height:80px;max-width:120px;border-radius:4px;" />',
                obj.imagePath.url,
            )
        return '-'

    image_preview.short_description = 'Image Preview'


class StoryQuestionOptionInline(admin.TabularInline):
    model = StoryQuestionOption
    extra = 4
    max_num = 4
    fields = ('order', 'option_text', 'is_correct')
    ordering = ('order', 'id')


@admin.register(StoryQuestion)
class StoryQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'story', 'order', 'short_question', 'is_active', 'options_count')
    list_filter = ('is_active', 'story__language', 'story__mainTopic')
    search_fields = ('story__subTopic', 'story__slug', 'question_text')
    ordering = ('story_id', 'order', 'id')
    inlines = [StoryQuestionOptionInline]

    def short_question(self, obj):
        text = (obj.question_text or '').strip()
        return text[:80] + ('...' if len(text) > 80 else '')

    short_question.short_description = 'Question'

    def options_count(self, obj):
        return obj.options.count()

    options_count.short_description = 'Options'


@admin.register(StoryQuestionOption)
class StoryQuestionOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'order', 'option_text', 'is_correct')
    list_filter = ('is_correct', 'question__story__language')
    search_fields = ('question__question_text', 'option_text', 'question__story__subTopic')
    ordering = ('question_id', 'order', 'id')
