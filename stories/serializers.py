from rest_framework import serializers
from .models import (
    Story,
    StoryTranslation,
    StoryMainTopic,
    StoryQuestion,
    StoryQuestionOption,
)


class StoryTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryTranslation
        fields = ['id', 'language_code', 'mainTopic', 'subTopic', 'article', 'audioPath']


class StoryQuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryQuestionOption
        fields = [
            'id',
            'order',
            'option_text',
            'is_correct',
        ]


class StoryQuestionSerializer(serializers.ModelSerializer):
    options = StoryQuestionOptionSerializer(many=True, read_only=True)

    class Meta:
        model = StoryQuestion
        fields = [
            'id',
            'order',
            'question_text',
            'is_active',
            'options',
        ]


class StorySerializer(serializers.ModelSerializer):
    translations = StoryTranslationSerializer(many=True, read_only=True)
    questions = serializers.SerializerMethodField()
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
        return trans.mainTopic if trans else ''

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

    def get_questions(self, obj):
        lang = self._get_requested_lang()
        trans = obj.get_translation(lang)
        if trans:
            questions = trans.questions.filter(is_active=True).order_by('order', 'id')
            return StoryQuestionSerializer(questions, many=True, context=self.context).data
        return []

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
        model = Story
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
            'questions',
            'created_at',
            'updated_at',
        ]


class StoryListItemSerializer(serializers.ModelSerializer):
    mainTopic = serializers.SerializerMethodField()
    subTopic = serializers.SerializerMethodField()
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
        return trans.mainTopic if trans else ''

    def get_subTopic(self, obj):
        trans = obj.get_translation(self._get_requested_lang())
        return trans.subTopic if trans else ''

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
        model = Story
        fields = [
            'id',
            'topic_id',
            'mainTopic',
            'subTopic',
            'slug',
            'order',
            'language',
            'audioPath',
            'imagePath',
            'imageUrl',
            'articleImage',
            'created_at',
            'updated_at',
        ]


class StoryMainTopicGroupedSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    articleList = serializers.SerializerMethodField()

    class Meta:
        model = StoryMainTopic
        fields = ['id', 'name', 'description', 'image', 'articleList']

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

    def get_articleList(self, obj):
        grouped_articles = self.context.get('grouped_articles', {})
        story_list = grouped_articles.get(obj.id, [])
        return StoryListItemSerializer(
            story_list,
            many=True,
            context=self.context,
        ).data

