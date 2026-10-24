from rest_framework import serializers
from .models import (
    VaishnavaEtiquetteArticle,
    VaishnavaEtiquetteTranslation,
    EtiquetteCategory,
    EtiquetteCategoryTranslation,
    EtiquetteQuestion,
    EtiquetteQuestionOption,
)


class EtiquetteQuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtiquetteQuestionOption
        fields = ['order', 'option_text', 'is_correct']


class EtiquetteQuestionSerializer(serializers.ModelSerializer):
    options = EtiquetteQuestionOptionSerializer(many=True, read_only=True)

    class Meta:
        model = EtiquetteQuestion
        fields = ['order', 'question_text', 'is_active', 'options']


class VaishnavaEtiquetteTranslationSerializer(serializers.ModelSerializer):
    categoryName = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = VaishnavaEtiquetteTranslation
        fields = ['language', 'category', 'categoryName', 'subTopic', 'article', 'audioPath']


class VaishnavaEtiquetteArticleSerializer(serializers.ModelSerializer):
    categoryName = serializers.SerializerMethodField()
    categoryDescription = serializers.SerializerMethodField()
    categoryImage = serializers.SerializerMethodField()
    mainTopic = serializers.SerializerMethodField()
    subTopic = serializers.SerializerMethodField()
    article = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    audioPath = serializers.SerializerMethodField()
    questions = serializers.SerializerMethodField()
    translations = VaishnavaEtiquetteTranslationSerializer(many=True, read_only=True)

    class Meta:
        model = VaishnavaEtiquetteArticle
        fields = '__all__'

    def _get_translation(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('language', request.query_params.get('lang', 'en')) if request else 'en'
        t = obj.translations.filter(language=lang).first()
        if not t:
            t = obj.translations.filter(language='en').first() or obj.translations.first()
        return t

    def _get_category_translation(self, obj):
        t = self._get_translation(obj)
        request = self.context.get('request')
        lang = request.query_params.get('language', request.query_params.get('lang', 'en')) if request else 'en'
        if t and t.category:
            return t.category.translations.filter(language=lang).first() or t.category
        return None

    def get_categoryName(self, obj):
        cat_t = self._get_category_translation(obj)
        if hasattr(cat_t, 'translated_name'):
            return cat_t.translated_name
        return cat_t.name if cat_t else None

    def get_categoryDescription(self, obj):
        cat_t = self._get_category_translation(obj)
        return getattr(cat_t, 'description', None)

    def get_categoryImage(self, obj):
        t = self._get_translation(obj)
        if t and t.category and t.category.image:
            return t.category.image.url
        return 'https://api.askharekrishna.com/media/debate/article/harekrishnaPreaching.jpg'

    def get_mainTopic(self, obj):
        return self.get_categoryName(obj)

    def get_subTopic(self, obj):
        t = self._get_translation(obj)
        return t.subTopic if t else None

    def get_article(self, obj):
        t = self._get_translation(obj)
        return t.article if t else None

    def get_language(self, obj):
        t = self._get_translation(obj)
        return t.language if t else None

    def get_audioPath(self, obj):
        t = self._get_translation(obj)
        if t and t.audioPath:
            return t.audioPath.url
        return None

    def get_questions(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('language', request.query_params.get('lang', 'en')) if request else 'en'
        qs = obj.questions.filter(language=lang)
        return EtiquetteQuestionSerializer(qs, many=True).data


class VaishnavaEtiquetteArticleListItemSerializer(serializers.ModelSerializer):
    mainTopic = serializers.SerializerMethodField()
    subTopic = serializers.SerializerMethodField()
    article = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    audioPath = serializers.SerializerMethodField()
    articleImage = serializers.SerializerMethodField()
    previousArticle = serializers.SerializerMethodField()
    nextArticle = serializers.SerializerMethodField()

    class Meta:
        model = VaishnavaEtiquetteArticle
        fields = [
            'id',
            'mainTopic',
            'subTopic',
            'article',
            'slug',
            'order',
            'language',
            'articleImage',
            'audioPath',
            'previousArticle',
            'nextArticle',
        ]

    def _get_translation(self, obj):
        if hasattr(obj, 'cached_trans') and obj.cached_trans:
            return obj.cached_trans[0]
        request = self.context.get('request')
        lang = request.query_params.get('language', request.query_params.get('lang', 'en')) if request else 'en'
        return obj.translations.filter(language=lang).first() or obj.translations.filter(language='en').first() or obj.translations.first()

    def get_mainTopic(self, obj):
        t = self._get_translation(obj)
        if not t or not t.category_id:
            return 'General Etiquette'
        cat_names = self.context.get('category_names', {})
        if t.category_id in cat_names:
            return cat_names[t.category_id]
        return t.category.name if t.category else 'General Etiquette'

    def get_subTopic(self, obj):
        t = self._get_translation(obj)
        return t.subTopic if t else ''

    def get_article(self, obj):
        t = self._get_translation(obj)
        return t.article if t else ''

    def get_language(self, obj):
        t = self._get_translation(obj)
        return t.language if t else 'en'

    def get_audioPath(self, obj):
        t = self._get_translation(obj)
        return t.audioPath.url if t and t.audioPath else None

    def get_articleImage(self, obj):
        if obj.articleImage:
            url = obj.articleImage.url
            if url.startswith('http://') or url.startsWith('https://'):
                return url
            return f"https://api.askharekrishna.com{url}"
        return 'https://api.askharekrishna.com/media/debate/article/harekrishnaPreaching.jpg'

    def get_previousArticle(self, obj):
        request = self.context.get('request')
        if not request or not (request.query_params.get('slug') or request.query_params.get('id')):
            return None
        prev_art = VaishnavaEtiquetteArticle.objects.filter(order__lt=obj.order).order_by('-order').first()
        if not prev_art:
            # Wrap around or none
            return None
        lang = request.query_params.get('language', request.query_params.get('lang', 'en'))
        t = prev_art.translations.filter(language=lang).first() or prev_art.translations.filter(language='en').first() or prev_art.translations.first()
        return {
            'id': prev_art.id,
            'slug': prev_art.slug,
            'fullSlug': prev_art.slug,
            'subTopic': t.subTopic if t else '',
            'order': prev_art.order,
        }

    def get_nextArticle(self, obj):
        request = self.context.get('request')
        if not request or not (request.query_params.get('slug') or request.query_params.get('id')):
            return None
        next_art = VaishnavaEtiquetteArticle.objects.filter(order__gt=obj.order).order_by('order').first()
        if not next_art:
            return None
        lang = request.query_params.get('language', request.query_params.get('lang', 'en'))
        t = next_art.translations.filter(language=lang).first() or next_art.translations.filter(language='en').first() or next_art.translations.first()
        return {
            'id': next_art.id,
            'slug': next_art.slug,
            'fullSlug': next_art.slug,
            'subTopic': t.subTopic if t else '',
            'order': next_art.order,
        }


class EtiquetteCategoryArticleListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    articleList = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = EtiquetteCategory
        fields = ['id', 'name', 'description', 'image', 'articleList']

    def get_image(self, obj):
        if not obj.image:
            return 'https://api.askharekrishna.com/media/debate/article/harekrishnaPreaching.jpg'
        url = obj.image.url
        return f"https://api.askharekrishna.com{url}"

    def _get_translation(self, obj):
        if hasattr(obj, 'cached_cat_trans') and obj.cached_cat_trans:
            return obj.cached_cat_trans[0]
        request = self.context.get('request')
        lang = request.query_params.get('language', request.query_params.get('lang', 'en')) if request else 'en'
        return obj.translations.filter(language=lang).first()

    def get_name(self, obj):
        t = self._get_translation(obj)
        return t.translated_name if t else obj.name

    def get_description(self, obj):
        t = self._get_translation(obj)
        return t.description if t and t.description else obj.description

    def get_articleList(self, obj):
        grouped_articles = self.context.get('grouped_articles', {})
        queryset = grouped_articles.get(obj.id, [])
        return VaishnavaEtiquetteArticleListItemSerializer(
            queryset,
            many=True,
            context=self.context,
        ).data
