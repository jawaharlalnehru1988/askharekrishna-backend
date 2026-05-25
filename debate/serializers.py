from rest_framework import serializers
from .models import DebateArticle, DebateCategory


class DebateArticleSerializer(serializers.ModelSerializer):
    debateCategoryName = serializers.CharField(source='debateCategory.name', read_only=True)
    debateCategoryDescription = serializers.CharField(source='debateCategory.description', read_only=True)
    debateCategoryImage = serializers.ImageField(source='debateCategory.image', read_only=True)

    class Meta:
        model = DebateArticle
        fields = '__all__'


class DebateArticleListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebateArticle
        fields = [
            'topic',
            'subTopic',
            'article',
            'slug',
            'order',
            'language',
            'audioPath',
            'debateCategory',
        ]


class DebateCategoryArticleListSerializer(serializers.ModelSerializer):
    articleList = serializers.SerializerMethodField()

    class Meta:
        model = DebateCategory
        fields = ['name', 'description', 'image', 'articleList']

    def get_articleList(self, obj):
        grouped_articles = self.context.get('grouped_articles', {})
        queryset = grouped_articles.get(obj.id, DebateArticle.objects.none())
        return DebateArticleListItemSerializer(
            queryset,
            many=True,
            context=self.context,
        ).data


class DebateArticleChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebateArticle
        fields = [
            'id',
            'topic',
            'subTopic',
            'article',
            'slug',
            'order',
            'language',
            'audioPath',
            'created_at',
            'updated_at',
            'debateCategory',
        ]


class DebateCategoryNestedSerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()

    class Meta:
        model = DebateCategory
        fields = ['id', 'name', 'description', 'image', 'articles']

    def get_articles(self, obj):
        queryset = obj.articles.all().order_by('order', 'topic', 'subTopic', 'id')
        request = self.context.get('request')

        if request:
            language = request.query_params.get('language')
            if language:
                queryset = queryset.filter(language=language)

        return DebateArticleChildSerializer(queryset, many=True, context=self.context).data
