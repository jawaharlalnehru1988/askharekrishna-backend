from django import forms
from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from django.utils.html import format_html, format_html_join
from django.utils.safestring import mark_safe
from .models import (
    PoojaVidhi,
    PoojaVidhiTranslation,
    PoojaVidhiTopic,
    PoojaVidhiQuestion,
    PoojaVidhiQuestionOption,
    Language,
    LANGUAGE_CHOICES,
)

POOJA_VIDHI_LANGUAGE_NAMES = dict(LANGUAGE_CHOICES)
POOJA_VIDHI_LANGUAGE_CHOICES = LANGUAGE_CHOICES


class PoojaVidhiTranslationInlineForm(forms.ModelForm):
    mainTopic = forms.ChoiceField(required=True)

    class Meta:
        model = PoojaVidhiTranslation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        topic_names = list(
            PoojaVidhiTopic.objects.filter(is_active=True).order_by('order', 'name').values_list('name', flat=True)
        )
        choices = [('', '---------')] + [(name, name) for name in topic_names]

        current_value = getattr(self.instance, 'mainTopic', '') if self.instance else ''
        if current_value and current_value not in topic_names:
            choices.append((current_value, current_value))

        self.fields['mainTopic'].choices = choices


class PoojaVidhiTranslationInline(admin.StackedInline):
    model = PoojaVidhiTranslation
    form = PoojaVidhiTranslationInlineForm
    extra = 1
    readonly_fields = ('manage_mcqs_info',)

    def manage_mcqs_info(self, obj):
        if not obj or not getattr(obj, 'pk', None):
            return mark_safe('<em style="color:#888;">Save this translation first to manage MCQs.</em>')

        try:
            q_count = obj.questions.count()
            edit_url = reverse('admin:pooja_vidhis_poojavidhitranslation_change', args=[obj.pk])
            gen_url = reverse('admin:pooja_vidhis_poojavidhitranslation_generate_mcqs', args=[obj.pk])

            status_color = '#16a34a' if q_count > 0 else '#dc2626'
            status_text = f"{q_count} MCQ Questions attached" if q_count > 0 else "No MCQs attached"

            return format_html(
                '<div style="display:flex;align-items:center;gap:12px;padding:8px 12px;background:#f8fafc;border:1px solid #cbd5e1;border-radius:6px;margin-top:6px;">'
                '<strong style="color:{}; font-size:13px;">📝 {}</strong> &nbsp;|&nbsp; '
                '<a href="{}" class="button" style="background:#2563eb;color:#fff;padding:6px 14px;border-radius:4px;text-decoration:none;font-weight:600;font-size:12px;">'
                '✏️ View / Edit MCQs for [{}]'
                '</a> '
                '<a href="{}" class="button" style="background:#7c3aed;color:#fff;padding:6px 14px;border-radius:4px;text-decoration:none;font-weight:600;font-size:12px;" onclick="return confirm(\'Generate / Regenerate MCQs via OpenAI for this translation?\');">'
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


class PoojaVidhiQuestionInline(admin.StackedInline):
    model = PoojaVidhiQuestion
    extra = 0
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


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    ordering = ('name',)


@admin.register(PoojaVidhi)
class PoojaVidhiAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'id', 'order', 'image_preview')
    list_display_links = ('get_title',)
    search_fields = ('translations__mainTopic', 'translations__subTopic', 'translations__article')
    fields = ('id', 'slug', 'order', 'articleImage', 'image_preview')
    readonly_fields = ('id', 'slug', 'image_preview')
    ordering = ('order', 'id')
    save_as = True
    inlines = [PoojaVidhiTranslationInline]

    def get_title(self, obj):
        trans = obj.get_translation('en')
        if trans:
            return f"[{trans.language_code.upper()}] {trans.mainTopic} - {trans.subTopic}"
        return f"Pooja Vidhi {obj.id}"
    get_title.short_description = 'Title'

    def image_preview(self, obj):
        image = obj.effective_image()
        if image:
            return format_html('<img src="{}" style="max-height: 80px; max-width: 150px; border-radius: 4px; border: 1px solid #ccc;" />', image.url)
        return '-'
    image_preview.short_description = 'Image Preview'


@admin.register(PoojaVidhiTranslation)
class PoojaVidhiTranslationAdmin(admin.ModelAdmin):
    list_display = ('subTopic', 'mainTopic', 'language_code', 'pooja_vidhi', 'audioPath', 'mcq_count', 'id')
    list_filter = ('language_code', 'mainTopic')
    search_fields = ('mainTopic', 'subTopic', 'article')
    inlines = [PoojaVidhiQuestionInline]
    ordering = ('pooja_vidhi_id', 'language_code')

    def mcq_count(self, obj):
        return obj.questions.count()
    mcq_count.short_description = 'MCQ Questions'

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                '<int:pk>/generate-mcqs/',
                self.admin_site.admin_view(self.generate_mcqs_view),
                name='pooja_vidhis_poojavidhitranslation_generate_mcqs',
            ),
        ]
        return custom + urls

    def generate_mcqs_view(self, request, pk):
        from .mcq_generator import generate_mcqs, save_mcqs

        trans = self.get_object(request, pk)
        if trans is None:
            messages.error(request, 'Pooja Vidhi translation not found.')
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


@admin.register(PoojaVidhiTopic)
class PoojaVidhiTopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_active',)
    ordering = ('order', 'name')


class PoojaVidhiQuestionOptionInline(admin.TabularInline):
    model = PoojaVidhiQuestionOption
    extra = 4
    max_num = 4
    fields = ('order', 'option_text', 'is_correct')
    ordering = ('order', 'id')


@admin.register(PoojaVidhiQuestion)
class PoojaVidhiQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'translation', 'order', 'short_question', 'is_active', 'options_count')
    list_filter = ('is_active', 'translation__language_code')
    search_fields = ('question_text', 'translation__subTopic')
    ordering = ('translation_id', 'order', 'id')
    inlines = [PoojaVidhiQuestionOptionInline]

    def short_question(self, obj):
        text = (obj.question_text or '').strip()
        return text[:80] + ('...' if len(text) > 80 else '')

    short_question.short_description = 'Question'

    def options_count(self, obj):
        return obj.options.count()

    options_count.short_description = 'Options'


@admin.register(PoojaVidhiQuestionOption)
class PoojaVidhiQuestionOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'order', 'option_text', 'is_correct')
    list_filter = ('is_correct',)
    search_fields = ('question__question_text', 'option_text')
    ordering = ('question_id', 'order', 'id')
