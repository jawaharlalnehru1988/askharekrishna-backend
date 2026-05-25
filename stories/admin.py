from django.contrib import admin
from django import forms
from django.urls import path
from django.http import HttpResponseRedirect
from django.utils.html import format_html, format_html_join
from django.contrib import messages
from .models import Story, StoryMainTopic, StoryQuestion, StoryQuestionOption


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
        ]
        return custom + urls

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
