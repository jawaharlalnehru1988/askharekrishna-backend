from django import forms
from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import path
from django.utils.html import format_html, format_html_join
from .models import (
    PoojaVidhi,
    PoojaVidhiTopic,
    PoojaVidhiQuestion,
    PoojaVidhiQuestionOption,
)


class PoojaVidhiAdminForm(forms.ModelForm):
    mainTopic = forms.ChoiceField(required=True)

    class Meta:
        model = PoojaVidhi
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

class PoojaVidhiQuestionInline(admin.StackedInline):
    model = PoojaVidhiQuestion
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


@admin.register(PoojaVidhi)
class PoojaVidhiAdmin(admin.ModelAdmin):
    change_form_template = 'admin/pooja_vidhis/poojavidhi/change_form.html'
    form = PoojaVidhiAdminForm
    list_display = ('subTopic', 'mainTopic', 'language', 'mcq_exists', 'audioPath', 'articleImage', 'created_at')
    list_filter = ('language', 'mainTopic', 'subTopic')
    search_fields = ('mainTopic', 'subTopic', 'article')
    fields = ('language', 'mainTopic', 'subTopic', 'article', 'slug', 'order', 'audioPath', 'articleImage')
    readonly_fields = ('slug',)
    ordering = ('order', 'mainTopic', 'subTopic')
    save_as = True
    inlines = [PoojaVidhiQuestionInline]

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
                name='pooja_vidhis_poojavidhi_generate_mcqs',
            ),
        ]
        return custom + urls

    def generate_mcqs_view(self, request, pk):
        from .mcq_generator import generate_mcqs, save_mcqs

        pooja_vidhi = self.get_object(request, pk)
        if pooja_vidhi is None:
            messages.error(request, 'Pooja Vidhi article not found.')
            return HttpResponseRedirect('../../')

        if not pooja_vidhi.article or not pooja_vidhi.article.strip():
            messages.error(request, 'This article has no text to generate MCQs from.')
            return HttpResponseRedirect(f'../../{pk}/change/')

        try:
            questions = generate_mcqs(pooja_vidhi.article, language=pooja_vidhi.language or 'en')
            count = save_mcqs(pooja_vidhi, questions)
            messages.success(
                request,
                f'Successfully generated and saved {count} MCQ questions for "{pooja_vidhi.subTopic}".',
            )
        except ValueError as exc:
            messages.error(request, f'MCQ generation failed: {exc}')
        except Exception as exc:
            messages.error(request, f'Unexpected error while generating MCQs: {exc}')

        return HttpResponseRedirect(f'../../{pk}/change/')

    def save_model(self, request, obj, form, change):
        if '_saveasnew' in request.POST and not obj.articleImage:
            if request.resolver_match and hasattr(request.resolver_match, 'kwargs'):
                original_id = request.resolver_match.kwargs.get('object_id')
                if original_id:
                    try:
                        original = PoojaVidhi.objects.get(pk=original_id)
                        obj.articleImage = original.articleImage
                    except PoojaVidhi.DoesNotExist:
                        pass

        super().save_model(request, obj, form, change)


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
    list_display = ('id', 'pooja_vidhi', 'order', 'short_question', 'is_active', 'options_count')
    list_filter = ('is_active', 'pooja_vidhi__language', 'pooja_vidhi__mainTopic')
    search_fields = ('pooja_vidhi__subTopic', 'pooja_vidhi__slug', 'question_text')
    ordering = ('pooja_vidhi_id', 'order', 'id')
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
    list_filter = ('is_correct', 'question__pooja_vidhi__language')
    search_fields = ('question__question_text', 'option_text', 'question__pooja_vidhi__subTopic')
    ordering = ('question_id', 'order', 'id')
