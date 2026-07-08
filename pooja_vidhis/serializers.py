from rest_framework import serializers
from .models import PoojaVidhi, PoojaVidhiTopic, PoojaVidhiQuestion, PoojaVidhiQuestionOption


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
    questions = PoojaVidhiQuestionSerializer(many=True, read_only=True)
    imageUrl = serializers.SerializerMethodField()
    articleImage = serializers.SerializerMethodField()

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
        fields = '__all__'


class PoojaVidhiListItemSerializer(serializers.ModelSerializer):
    questions = PoojaVidhiQuestionSerializer(many=True, read_only=True)
    imageUrl = serializers.SerializerMethodField()
    articleImage = serializers.SerializerMethodField()

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
            'translated_from',
            'source_vidhi',
            'audioPath',
            'articleImage',
            'imageUrl',
            'questions',
        ]


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
