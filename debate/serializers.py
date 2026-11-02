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
    previousArticle = serializers.SerializerMethodField()
    nextArticle = serializers.SerializerMethodField()

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
            'previousArticle',
            'nextArticle',
        ]

    def _get_translation(self, obj):
        if hasattr(obj, 'cached_trans') and obj.cached_trans:
            return obj.cached_trans[0]
        request = self.context.get('request')
        lang = request.query_params.get('language', 'en') if request else 'en'
        return obj.translations.filter(language=lang).first() or obj.translations.first()

    def get_subTopic(self, obj):
        t = self._get_translation(obj)
        return t.subTopic if t else ''

    def get_mainTopic(self, obj):
        t = self._get_translation(obj)
        if not t or not t.debateCategory_id:
            return ''
        cat_names = self.context.get('category_names')
        if cat_names and t.debateCategory_id in cat_names:
            return cat_names[t.debateCategory_id]
        cat = t.debateCategory
        if hasattr(cat, 'cached_cat_trans') and cat.cached_cat_trans:
            cat_t = cat.cached_cat_trans[0]
            return cat_t.translated_name if cat_t.translated_name else cat.name
        request = self.context.get('request')
        lang = request.query_params.get('language', 'en') if request else 'en'
        cat_t = cat.translations.filter(language=lang).first()
        return cat_t.translated_name if cat_t else cat.name

    def get_article(self, obj):
        request = self.context.get('request')
        # If slug or id is passed or include_content is true, provide the full markdown body.
        # Otherwise for catalog lists, omit to keep payload 97% lighter and ultra-fast.
        if request and (request.query_params.get('slug') or request.query_params.get('id') or request.query_params.get('include_content') == 'true'):
            t = self._get_translation(obj)
            return t.article if t else ''
        return ''

    def get_language(self, obj):
        t = self._get_translation(obj)
        return t.language if t else 'en'

    def get_audioPath(self, obj):
        t = self._get_translation(obj)
        return t.audioPath.url if t and t.audioPath else None

    def get_previousArticle(self, obj):
        request = self.context.get('request')
        if not request or not (request.query_params.get('slug') or request.query_params.get('id')):
            return None
        prev_art = DebateArticle.objects.filter(order__lt=obj.order).order_by('-order').first()
        if not prev_art:
            return None
        lang = request.query_params.get('language', 'en')
        t = prev_art.translations.filter(language=lang).first() or prev_art.translations.first()
        return {
            'id': prev_art.id,
            'slug': str(prev_art.id),
            'fullSlug': prev_art.slug,
            'subTopic': t.subTopic if t else '',
            'order': prev_art.order,
        }

    def get_nextArticle(self, obj):
        request = self.context.get('request')
        if not request or not (request.query_params.get('slug') or request.query_params.get('id')):
            return None
        next_art = DebateArticle.objects.filter(order__gt=obj.order).order_by('order').first()
        if not next_art:
            return None
        lang = request.query_params.get('language', 'en')
        t = next_art.translations.filter(language=lang).first() or next_art.translations.first()
        return {
            'id': next_art.id,
            'slug': str(next_art.id),
            'fullSlug': next_art.slug,
            'subTopic': t.subTopic if t else '',
            'order': next_art.order,
        }


class DebateCategoryArticleListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    articleList = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    translations = serializers.SerializerMethodField()
    all_names = serializers.SerializerMethodField()

    class Meta:
        model = DebateCategory
        fields = ['id', 'name', 'description', 'image', 'articleList', 'translations', 'all_names']

    def get_image(self, obj):
        if not obj.image:
            return None
        url = obj.image.url
        request = self.context.get('request')
        if request:
            uri = request.build_absolute_uri(url)
            if '127.0.0.1' in uri or 'localhost' in uri:
                return f"https://api.askharekrishna.com{url}"
            return uri
        return f"https://api.askharekrishna.com{url}"

    def _get_translation(self, obj):
        if hasattr(obj, 'cached_cat_trans') and obj.cached_cat_trans:
            return obj.cached_cat_trans[0]
        request = self.context.get('request')
        lang = request.query_params.get('language', 'en') if request else 'en'
        return obj.translations.filter(language=lang).first()

    def get_name(self, obj):
        t = self._get_translation(obj)
        return t.translated_name if t else obj.name

    def get_description(self, obj):
        t = self._get_translation(obj)
        return t.description if t and t.description else obj.description

    def get_translations(self, obj):
        result = {'en': obj.name}
        trans_list = getattr(obj, 'all_cat_translations', None)
        if trans_list is None:
            trans_list = obj.translations.all()
        for trans in trans_list:
            if trans.translated_name:
                result[trans.language] = trans.translated_name
        return result

    def get_all_names(self, obj):
        names = set()
        result = []
        if obj.name:
            names.add(obj.name.strip().lower())
            result.append(obj.name)
        trans_list = getattr(obj, 'all_cat_translations', None)
        if trans_list is None:
            trans_list = obj.translations.all()
        for trans in trans_list:
            t_name = trans.translated_name.strip() if trans.translated_name else ''
            if t_name and t_name.lower() not in names:
                names.add(t_name.lower())
                result.append(t_name)
        return result

    def get_articleList(self, obj):
        grouped_articles = self.context.get('grouped_articles', {})
        queryset = grouped_articles.get(obj.id, [])
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
