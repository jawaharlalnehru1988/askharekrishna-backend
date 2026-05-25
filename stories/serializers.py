from rest_framework import serializers
from .models import Story, StoryMainTopic, StoryQuestion, StoryQuestionOption


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
    mainTopicName = serializers.CharField(source='mainTopic.name', read_only=True)
    mainTopicDescription = serializers.CharField(source='mainTopic.description', read_only=True)
    mainTopicImage = serializers.ImageField(source='mainTopic.image', read_only=True)
    imageUrl = serializers.ImageField(source='imagePath', read_only=True)
    questions = StoryQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Story
        fields = '__all__'


class StoryListItemSerializer(serializers.ModelSerializer):
    questions = StoryQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Story
        fields = [
            'id',
            'mainTopic',
            'subTopic',
            'article',
            'slug',
            'order',
            'language',
            'audioPath',
            'imagePath',
            'questions',
            'created_at',
            'updated_at',
        ]


class StoryMainTopicGroupedSerializer(serializers.ModelSerializer):
    articleList = serializers.SerializerMethodField()

    class Meta:
        model = StoryMainTopic
        fields = ['name', 'description', 'image', 'articleList']

    def get_articleList(self, obj):
        grouped_articles = self.context.get('grouped_articles', {})
        queryset = grouped_articles.get(obj.id, Story.objects.none())
        return StoryListItemSerializer(queryset, many=True, context=self.context).data
