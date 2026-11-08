from rest_framework import serializers
from .models import CookingArticle, CookingArticleTranslation, CookingMainTopic


class CookingArticleTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookingArticleTranslation
        fields = ['id', 'language_code', 'mainTopic', 'subTopic', 'article', 'audioPath']


class CookingArticleSerializer(serializers.ModelSerializer):
    translations = CookingArticleTranslationSerializer(many=True, read_only=True)
    mainTopic = serializers.SerializerMethodField()
    subTopic = serializers.SerializerMethodField()
    article = serializers.SerializerMethodField()
    audioPath = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    imageUrl = serializers.SerializerMethodField()
    imagePath = serializers.SerializerMethodField()
    articleImage = serializers.SerializerMethodField()

    def _get_requested_lang(self):
        request = self.context.get('request')
        if request:
            query_params = getattr(request, 'query_params', None)
            if query_params is None:
                query_params = getattr(request, 'GET', {})
            lang = query_params.get('language') or query_params.get('lang')
            if lang:
                return lang.strip().lower()
        return 'en'

    def get_mainTopic(self, obj):
        trans = obj.get_translation(self._get_requested_lang())
        if trans and trans.mainTopic:
            return trans.mainTopic
        if obj.topic:
            return obj.topic.get_localized_name(self._get_requested_lang())
        return ''

    def get_subTopic(self, obj):
        trans = obj.get_translation(self._get_requested_lang())
        return trans.subTopic if trans else ''

    def get_article(self, obj):
        trans = obj.get_translation(self._get_requested_lang())
        return trans.article if trans else ''

    def get_audioPath(self, obj):
        trans = obj.get_translation(self._get_requested_lang())
        if trans and trans.audioPath:
            return trans.audioPath.url
        return None

    def get_language(self, obj):
        trans = obj.get_translation(self._get_requested_lang())
        return trans.language_code if trans else 'en'

    def get_imageUrl(self, obj):
        image = obj.effective_image_path()
        return image.url if image else None

    def get_imagePath(self, obj):
        image = obj.effective_image_path()
        return image.url if image else None

    def get_articleImage(self, obj):
        image = obj.effective_image_path()
        if image:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(image.url)
            return image.url
        return None

    class Meta:
        model = CookingArticle
        fields = [
            'id',
            'topic_id',
            'mainTopic',
            'subTopic',
            'article',
            'slug',
            'order',
            'language',
            'audioPath',
            'imagePath',
            'imageUrl',
            'articleImage',
            'translations',
            'created_at',
            'updated_at',
        ]


class CookingMainTopicSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = CookingMainTopic
        fields = ['id', 'name', 'description', 'image', 'order', 'name_translations', 'description_translations']

    def _get_lang(self):
        request = self.context.get('request')
        if request:
            query_params = getattr(request, 'query_params', None)
            if query_params is None:
                query_params = getattr(request, 'GET', {})
            lang = query_params.get('language') or query_params.get('lang')
            if lang:
                return lang.strip().lower()
        return 'en'

    def get_name(self, obj):
        return obj.get_localized_name(self._get_lang())

    def get_description(self, obj):
        return obj.get_localized_description(self._get_lang())
