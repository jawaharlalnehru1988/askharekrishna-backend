from rest_framework import serializers
from .models import PoojaVidhi, PoojaVidhiTranslation, PoojaVidhiTopic, PoojaVidhiQuestion, PoojaVidhiQuestionOption


class PoojaVidhiTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoojaVidhiTranslation
        fields = ['id', 'language_code', 'mainTopic', 'subTopic', 'article', 'audioPath']


class PoojaVidhiQuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoojaVidhiQuestionOption
        fields = ['id', 'order', 'option_text', 'is_correct']


class PoojaVidhiQuestionSerializer(serializers.ModelSerializer):
    options = PoojaVidhiQuestionOptionSerializer(many=True, read_only=True)

    class Meta:
        model = PoojaVidhiQuestion
        fields = ['id', 'order', 'question_text', 'is_active', 'options']


class PoojaVidhiSerializer(serializers.ModelSerializer):
    translations = PoojaVidhiTranslationSerializer(many=True, read_only=True)
    questions = serializers.SerializerMethodField()
    mainTopic = serializers.SerializerMethodField()
    subTopic = serializers.SerializerMethodField()
    article = serializers.SerializerMethodField()
    audioPath = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    imageUrl = serializers.SerializerMethodField()
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
            return PoojaVidhiQuestionSerializer(questions, many=True, context=self.context).data
        return []

    def get_imageUrl(self, obj):
        image = obj.effective_image()
        return image.url if image else None

    def get_articleImage(self, obj):
        image = obj.effective_image()
        if image:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(image.url)
            return image.url
        return None

    class Meta:
        model = PoojaVidhi
        fields = [
            'id',
            'mainTopic',
            'subTopic',
            'article',
            'slug',
            'order',
            'language',
            'audioPath',
            'articleImage',
            'imageUrl',
            'translations',
            'questions',
            'created_at',
            'updated_at',
        ]


class PoojaVidhiListItemSerializer(PoojaVidhiSerializer):
    pass


class PoojaVidhiTopicGroupedSerializer(serializers.ModelSerializer):
    description = serializers.CharField(default='', read_only=True)
    image = serializers.SerializerMethodField()
    articleList = serializers.SerializerMethodField()

    class Meta:
        model = PoojaVidhiTopic
        fields = ['name', 'description', 'image', 'articleList']

    def get_image(self, obj):
        return None

    def get_articleList(self, obj):
        grouped_articles = self.context.get('grouped_articles', {})
        queryset = grouped_articles.get(obj.name, PoojaVidhi.objects.none())
        return PoojaVidhiListItemSerializer(
            queryset,
            many=True,
            context=self.context,
        ).data
