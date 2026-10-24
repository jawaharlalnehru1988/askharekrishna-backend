from django import forms
from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from django.utils.html import format_html, format_html_join
from django.utils.safestring import mark_safe
from pooja_vidhis.models import LANGUAGE_CHOICES
from .models import (
    Story,
    StoryTranslation,
    StoryMainTopic,
    StoryQuestion,
    StoryQuestionOption,
)


class StoryTranslationInlineForm(forms.ModelForm):
    mainTopic = forms.ChoiceField(required=True)

    class Meta:
        model = StoryTranslation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        topic_names = list(
            StoryMainTopic.objects.filter(is_active=True).order_by('order', 'name').values_list('name', flat=True)
        )
        choices = [('', '---------')] + [(name, name) for name in topic_names]

        current_value = getattr(self.instance, 'mainTopic', '') if self.instance else ''
        if current_value and current_value not in topic_names:
            choices.append((current_value, current_value))

        self.fields['mainTopic'].choices = choices


class StoryTranslationInline(admin.StackedInline):
    model = StoryTranslation
    form = StoryTranslationInlineForm
    extra = 1
    readonly_fields = ('manage_mcqs_info',)

    def manage_mcqs_info(self, obj):
        if not obj or not getattr(obj, 'pk', None):
            return mark_safe('<em style="color:#888;">Save this translation first to manage MCQs.</em>')

        try:
            q_count = obj.questions.count()
            edit_url = reverse('admin:stories_storytranslation_change', args=[obj.pk])
            gen_url = reverse('admin:stories_storytranslation_generate_mcqs', args=[obj.pk])

            status_color = '#16a34a' if q_count > 0 else '#dc2626'
            status_text = f"{q_count} MCQ Questions attached" if q_count > 0 else "No MCQs attached"

            return format_html(
                '<div style="display:flex;align-items:center;gap:12px;padding:8px 12px;background:#f8fafc;border:1px solid #cbd5e1;border-radius:6px;margin-top:6px;">'
                '<strong style="color:{}; font-size:13px;">📝 {}</strong> &nbsp;|&nbsp; '
                '<a href="{}" class="button" style="background:#2563eb;color:#fff;padding:6px 14px;border-radius:4px;text-decoration:none;font-weight:600;font-size:12px;">'
                '✏️ View / Edit MCQs for [{}]'
                '</a> '
                '<a href="{}" class="button" style="background:#7c3aed;color:#fff;padding:6px 14px;border-radius:4px;text-decoration:none;font-weight:600;font-size:12px;" onclick="return confirm(\'Generate / Regenerate MCQs via AI for this translation?\');">'
                '🤖 Generate AI MCQs'
                '</a>'
                '</div>',
                status_color,
                status_text,
                edit_url,
                obj.language_code.upper() if obj.language_code else 'EN',
                gen_url,
            )
        except Exception:
            return mark_safe('<em style="color:#888;">Save translation to activate MCQ links.</em>')

    manage_mcqs_info.short_description = 'Language MCQs'


class StoryQuestionInline(admin.StackedInline):
    model = StoryQuestion
    extra = 0
    fields = ('order', 'question_text', 'options_preview', 'edit_question_link', 'is_active')
    readonly_fields = ('options_preview', 'edit_question_link')
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

    def edit_question_link(self, obj):
        if not obj or not obj.pk:
            return mark_safe('<em style="color:#888;">Save translation first to edit options.</em>')
        url = reverse('admin:stories_storyquestion_change', args=[obj.pk])
        return format_html(
            '<a href="{}" class="button" style="background:#0284c7;color:#fff;padding:4px 12px;border-radius:4px;text-decoration:none;font-size:12px;font-weight:600;">'
            '✏️ Edit Question & Options'
            '</a>',
            url,
        )

    edit_question_link.short_description = 'Edit Question & Options'


@admin.register(StoryMainTopic)
class StoryMainTopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active', 'stories_count', 'image')
    search_fields = ('name', 'description')
    list_filter = ('is_active',)
    ordering = ('order', 'name')
    fields = ('name', 'order', 'is_active', 'description', 'description_translations', 'image', 'name_translations')

    def stories_count(self, obj):
        return obj.stories.count()

    stories_count.short_description = 'Stories Count'


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'get_main_topic', 'id', 'order', 'image_preview', 'translations_list')
    list_display_links = ('get_title',)
    search_fields = ('topic__name', 'translations__mainTopic', 'translations__subTopic', 'translations__article')
    list_filter = ('topic', 'translations__language_code')
    fields = ('id', 'topic', 'slug', 'order', 'imagePath', 'image_preview')
    readonly_fields = ('id', 'slug', 'image_preview')
    ordering = ('order', 'id')
    save_as = True
    inlines = [StoryTranslationInline]

    def get_title(self, obj):
        trans = obj.get_translation('en') or obj.translations.first()
        if trans:
            return f"{trans.subTopic} [{trans.language_code.upper()}]"
        return f"Story {obj.id}"

    get_title.short_description = 'Title'

    def get_main_topic(self, obj):
        if obj.topic:
            return obj.topic.name
        trans = obj.get_translation('en') or obj.translations.first()
        return trans.mainTopic if trans else '-'

    get_main_topic.short_description = 'Main Topic'

    def translations_list(self, obj):
        langs = [t.language_code.upper() for t in obj.translations.all()]
        return ', '.join(langs) if langs else '-'

    translations_list.short_description = 'Languages'

    def image_preview(self, obj):
        image = obj.effective_image_path()
        if image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 90px; border-radius: 4px; border: 1px solid #ccc; object-fit: cover;" />', image.url)
        return '-'

    image_preview.short_description = 'Image Preview'


@admin.register(StoryTranslation)
class StoryTranslationAdmin(admin.ModelAdmin):
    list_display = ('subTopic', 'mainTopic', 'language_code', 'story', 'audioPath', 'mcq_count', 'id')
    list_filter = ('language_code', 'mainTopic')
    search_fields = ('mainTopic', 'subTopic', 'article')
    readonly_fields = ('parent_story_link',)
    fields = ('parent_story_link', 'story', 'language_code', 'mainTopic', 'subTopic', 'article', 'audioPath')
    inlines = [StoryQuestionInline]
    ordering = ('story_id', 'language_code')

    def has_module_permission(self, request):
        return False

    def response_change(self, request, obj):
        if "_continue" not in request.POST and "_addanother" not in request.POST:
            if obj.story_id:
                return HttpResponseRedirect(reverse('admin:stories_story_change', args=[obj.story_id]))
        return super().response_change(request, obj)

    def parent_story_link(self, obj):
        if obj and obj.story_id:
            url = reverse('admin:stories_story_change', args=[obj.story_id])
            return format_html(
                '<a href="{}" class="button" style="background:#475569;color:#fff;padding:6px 14px;border-radius:4px;text-decoration:none;font-weight:600;font-size:12px;">'
                '⬅️ Back to Parent Story (ID: {})'
                '</a>',
                url,
                obj.story_id,
            )
        return '-'

    parent_story_link.short_description = 'Parent Story'

    def mcq_count(self, obj):
        return obj.questions.count()

    mcq_count.short_description = 'MCQ Questions'

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                '<int:pk>/generate-mcqs/',
                self.admin_site.admin_view(self.generate_mcqs_view),
                name='stories_storytranslation_generate_mcqs',
            ),
        ]
        return custom + urls

    def generate_mcqs_view(self, request, pk):
        from .mcq_generator import generate_mcqs, save_mcqs

        trans = self.get_object(request, pk)
        if trans is None:
            messages.error(request, 'Story translation not found.')
            return HttpResponseRedirect('../../')

        if not trans.article or not trans.article.strip():
            messages.error(request, 'This translation has no text to generate MCQs from.')
            return HttpResponseRedirect(f'../../{pk}/change/')

        try:
            questions = generate_mcqs(trans.article, language=trans.language_code)
            count = save_mcqs(trans, questions)
            messages.success(
                request,
                f'Successfully generated and saved {count} MCQ questions for "{trans.subTopic}" ({trans.language_code.upper()}).',
            )
        except ValueError as exc:
            messages.error(request, f'MCQ generation failed: {exc}')
        except Exception as exc:
            messages.error(request, f'Unexpected error while generating MCQs: {exc}')

        return HttpResponseRedirect(f'../../{pk}/change/')


class StoryQuestionOptionInline(admin.TabularInline):
    model = StoryQuestionOption
    extra = 4
    max_num = 4
    fields = ('order', 'option_text', 'is_correct')
    ordering = ('order', 'id')


@admin.register(StoryQuestion)
class StoryQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'translation', 'order', 'short_question', 'is_active', 'options_count')
    list_filter = ('is_active', 'translation__language_code')
    search_fields = ('question_text', 'translation__subTopic')
    readonly_fields = ('parent_translation_link',)
    fields = ('parent_translation_link', 'translation', 'order', 'question_text', 'is_active')
    ordering = ('translation_id', 'order', 'id')
    inlines = [StoryQuestionOptionInline]

    def has_module_permission(self, request):
        return False

    def response_change(self, request, obj):
        if "_continue" not in request.POST and "_addanother" not in request.POST:
            if obj.translation_id:
                return HttpResponseRedirect(reverse('admin:stories_storytranslation_change', args=[obj.translation_id]))
        return super().response_change(request, obj)

    def parent_translation_link(self, obj):
        if obj and obj.translation_id:
            url = reverse('admin:stories_storytranslation_change', args=[obj.translation_id])
            return format_html(
                '<a href="{}" class="button" style="background:#475569;color:#fff;padding:6px 14px;border-radius:4px;text-decoration:none;font-weight:600;font-size:12px;">'
                '⬅️ Back to Translation (ID: {})'
                '</a>',
                url,
                obj.translation_id,
            )
        return '-'

    parent_translation_link.short_description = 'Parent Translation'

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
    list_filter = ('is_correct',)
    search_fields = ('question__question_text', 'option_text')
    ordering = ('question_id', 'order', 'id')

    def has_module_permission(self, request):
        return False

    def response_change(self, request, obj):
        if "_continue" not in request.POST and "_addanother" not in request.POST:
            if obj.question_id:
                return HttpResponseRedirect(reverse('admin:stories_storyquestion_change', args=[obj.question_id]))
        return super().response_change(request, obj)
