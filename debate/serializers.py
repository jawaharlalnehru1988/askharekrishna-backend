from rest_framework import serializers
from .models import DebateArticle, DebateCategory, DebateQuestion, DebateQuestionOption


class DebateQuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebateQuestionOption
        fields = ['order', 'option_text', 'is_correct']


class DebateQuestionSerializer(serializers.ModelSerializer):
    options = DebateQuestionOptionSerializer(many=True, read_only=True)

    class Meta:
        model = DebateQuestion
        fields = ['order', 'question_text', 'is_active', 'options']


class DebateArticleTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import DebateArticleTranslation
        model = DebateArticleTranslation
        fields = ['language', 'subTopic', 'article', 'audioPath']

class DebateArticleSerializer(serializers.ModelSerializer):
    debateCategoryName = serializers.SerializerMethodField()
    debateCategoryDescription = serializers.SerializerMethodField()
    debateCategoryImage = serializers.ImageField(source='debateCategory.image', read_only=True)
    mainTopic = serializers.SerializerMethodField()
    questions = serializers.SerializerMethodField()
    translations = DebateArticleTranslationSerializer(many=True, read_only=True)

    class Meta:
        model = DebateArticle
        fields = '__all__'

    def _get_category_translation(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('language', 'en') if request else 'en'
        t = obj.translations.filter(language=lang).first()
        if t and t.debateCategory:
            return t.debateCategory.translations.filter(language=lang).first() or t.debateCategory
        return None

    def get_debateCategoryName(self, obj):
        cat_t = self._get_category_translation(obj)
        if hasattr(cat_t, 'translated_name'):
            return cat_t.translated_name
        return cat_t.name if cat_t else None

    def get_debateCategoryDescription(self, obj):
        cat_t = self._get_category_translation(obj)
        return getattr(cat_t, 'description', None)

    def get_mainTopic(self, obj):
        return self.get_debateCategoryName(obj)
    translations = DebateArticleTranslationSerializer(many=True, read_only=True)

    class Meta:
        model = DebateArticle
        fields = '__all__'

    def get_questions(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('language', 'en') if request else 'en'
        qs = obj.questions.filter(language=lang)
        return DebateQuestionSerializer(qs, many=True).data


class DebateArticleListItemSerializer(serializers.ModelSerializer):
    mainTopic = serializers.SerializerMethodField()
    subTopic = serializers.SerializerMethodField()
    article = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    audioPath = serializers.SerializerMethodField()

    class Meta:
        model = DebateArticle
        fields = [
            'mainTopic',
            'subTopic',
            'article',
            'slug',
            'order',
            'language',
            'articleImage',
            'articleImage',
            'audioPath',
            # 'debateCategory' removed
        ]

    def _get_translation(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('language', 'en') if request else 'en'
        return obj.translations.filter(language=lang).first() or obj.translations.first()

    def get_subTopic(self, obj):
        t = self._get_translation(obj)
        return t.subTopic if t else ''

    def get_mainTopic(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('language', 'en') if request else 'en'
        t = obj.translations.filter(language=lang).first()
        if not t or not t.debateCategory:
            return ''
        cat_t = t.debateCategory.translations.filter(language=lang).first()
        return cat_t.translated_name if cat_t else t.debateCategory.name

    def get_article(self, obj):
        t = self._get_translation(obj)
        return t.article if t else ''

    def get_language(self, obj):
        t = self._get_translation(obj)
        return t.language if t else 'en'

    def get_audioPath(self, obj):
        t = self._get_translation(obj)
        return t.audioPath.url if t and t.audioPath else None


class DebateCategoryArticleListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    articleList = serializers.SerializerMethodField()

    class Meta:
        model = DebateCategory
        fields = ['name', 'description', 'image', 'articleList']

    def _get_translation(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('language', 'en') if request else 'en'
        return obj.translations.filter(language=lang).first()

    def get_name(self, obj):
        t = self._get_translation(obj)
        return t.translated_name if t else obj.name

    def get_description(self, obj):
        t = self._get_translation(obj)
        return t.description if t and t.description else obj.description

    def get_articleList(self, obj):
        grouped_articles = self.context.get('grouped_articles', {})
        queryset = grouped_articles.get(obj.id, DebateArticle.objects.none())
        return DebateArticleListItemSerializer(
            queryset,
            many=True,
            context=self.context,
        ).data


class DebateArticleChildSerializer(serializers.ModelSerializer):
    mainTopic = serializers.SerializerMethodField()
    subTopic = serializers.SerializerMethodField()
    article = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    audioPath = serializers.SerializerMethodField()

    class Meta:
        model = DebateArticle
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
            'created_at',
            'updated_at',
            # 'debateCategory' removed
        ]

    def _get_translation(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('language', 'en') if request else 'en'
        return obj.translations.filter(language=lang).first() or obj.translations.first()

    def get_subTopic(self, obj):
        t = self._get_translation(obj)
        return t.subTopic if t else ''

    def get_mainTopic(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('language', 'en') if request else 'en'
        t = obj.translations.filter(language=lang).first()
        if not t or not t.debateCategory:
            return ''
        cat_t = t.debateCategory.translations.filter(language=lang).first()
        return cat_t.translated_name if cat_t else t.debateCategory.name

    def get_article(self, obj):
        t = self._get_translation(obj)
        return t.article if t else ''

    def get_language(self, obj):
        t = self._get_translation(obj)
        return t.language if t else 'en'

    def get_audioPath(self, obj):
        t = self._get_translation(obj)
        return t.audioPath.url if t and t.audioPath else None


class DebateCategoryNestedSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    articles = serializers.SerializerMethodField()

    class Meta:
        model = DebateCategory
        fields = ['id', 'name', 'description', 'image', 'articles']

    def _get_translation(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('language', 'en') if request else 'en'
        return obj.translations.filter(language=lang).first()

    def get_name(self, obj):
        t = self._get_translation(obj)
        return t.translated_name if t else obj.name

    def get_description(self, obj):
        t = self._get_translation(obj)
        return t.description if t and t.description else obj.description

    def get_articles(self, obj):
        # We need to get translations where debateCategory is obj
        # But we return DebateArticleChildSerializer which expects DebateArticle
        # So we fetch articles that have a translation pointing to this category
        queryset = DebateArticle.objects.filter(translations__debateCategory=obj).distinct().order_by('order', 'id')
        request = self.context.get('request')

        if request:
            language = request.query_params.get('language')
            if language:
                queryset = queryset.filter(translations__language=language).distinct()

        return DebateArticleChildSerializer(queryset, many=True, context=self.context).data

class DebateArticleTranslationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import DebateArticleTranslation
        model = DebateArticleTranslation
        fields = '__all__'
        read_only_fields = ['id', 'article_parent', 'language']
