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

    class Meta:
        model = PoojaVidhi
        fields = '__all__'


class PoojaVidhiListItemSerializer(serializers.ModelSerializer):
    questions = PoojaVidhiQuestionSerializer(many=True, read_only=True)

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
