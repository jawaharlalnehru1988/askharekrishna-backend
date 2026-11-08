from django import forms
from django.contrib import admin
from django.utils.html import format_html
from .models import CookingArticle, CookingArticleTranslation, CookingMainTopic


class CookingArticleTranslationInlineForm(forms.ModelForm):
    mainTopic = forms.ChoiceField(required=True)

    class Meta:
        model = CookingArticleTranslation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        topic_names = list(
            CookingMainTopic.objects.filter(is_active=True).order_by('order', 'name').values_list('name', flat=True)
        )
        choices = [('', '---------')] + [(name, name) for name in topic_names]

        current_value = getattr(self.instance, 'mainTopic', '') if self.instance else ''
        if current_value and current_value not in topic_names:
            choices.append((current_value, current_value))

        self.fields['mainTopic'].choices = choices


class CookingArticleTranslationInline(admin.StackedInline):
    model = CookingArticleTranslation
    form = CookingArticleTranslationInlineForm
    extra = 1
    fields = ('language_code', 'mainTopic', 'subTopic', 'article', 'audioPath')


@admin.register(CookingMainTopic)
class CookingMainTopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active', 'articles_count', 'image')
    search_fields = ('name', 'description')
    list_filter = ('is_active',)
    ordering = ('order', 'name')
    fields = ('name', 'order', 'is_active', 'description', 'description_translations', 'image', 'name_translations')

    def articles_count(self, obj):
        return obj.articles.count()

    articles_count.short_description = 'Articles Count'


@admin.register(CookingArticle)
class CookingArticleAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'get_main_topic', 'id', 'order', 'image_preview', 'translations_list')
    list_display_links = ('get_title',)
    search_fields = ('topic__name', 'translations__mainTopic', 'translations__subTopic', 'translations__article')
    list_filter = ('topic', 'translations__language_code')
    fields = ('id', 'topic', 'slug', 'order', 'imagePath', 'image_preview')
    readonly_fields = ('id', 'slug', 'image_preview')
    ordering = ('order', 'id')
    save_as = True
    inlines = [CookingArticleTranslationInline]

    def get_title(self, obj):
        trans = obj.get_translation('en') or obj.translations.first()
        if trans:
            return f"{trans.subTopic} [{trans.language_code.upper()}]"
        return f"Cooking Article {obj.id}"

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
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 90px; border-radius: 4px; border: 1px solid #ccc; object-fit: cover;" />',
                image.url,
            )
        return '-'

    image_preview.short_description = 'Image Preview'


@admin.register(CookingArticleTranslation)
class CookingArticleTranslationAdmin(admin.ModelAdmin):
    list_display = ('subTopic', 'mainTopic', 'language_code', 'article_parent', 'audioPath', 'id')
    list_filter = ('language_code', 'mainTopic')
    search_fields = ('mainTopic', 'subTopic', 'article')
    ordering = ('article_parent_id', 'language_code')

    def has_module_permission(self, request):
        return False
