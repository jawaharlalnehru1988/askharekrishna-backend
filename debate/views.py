from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, pagination, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import DebateArticle, DebateCategory, DebateQuestion, DebateQuestionOption
from .serializers import (
    DebateArticleSerializer,
    DebateCategoryNestedSerializer,
    DebateArticleListItemSerializer,
    DebateCategoryArticleListSerializer,
    DebateQuestionSerializer,
    DebateQuestionOptionSerializer,
)


class DebateArticlePagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100


class DebateArticleViewSet(viewsets.ModelViewSet):
    queryset = DebateArticle.objects.prefetch_related('questions__options').all().order_by('order', 'mainTopic', 'subTopic', 'id')
    serializer_class = DebateArticleSerializer
    pagination_class = DebateArticlePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'id': ['exact'],
        'mainTopic': ['exact', 'icontains'],
        'debateCategory': ['exact'],
        'debateCategory__name': ['exact', 'icontains'],
        'subTopic': ['exact', 'icontains'],
        'slug': ['exact'],
        'language': ['exact'],
    }
    search_fields = ['mainTopic', 'subTopic', 'article', 'debateCategory__name']
    ordering_fields = ['id', 'order', 'created_at', 'mainTopic', 'subTopic']
    ordering = ['order', 'mainTopic', 'subTopic', 'id']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        grouped_articles = {}
        uncategorized = []

        for article in queryset:
            if article.debateCategory_id is None:
                uncategorized.append(article)
                continue
            grouped_articles.setdefault(article.debateCategory_id, []).append(article)

        categories = DebateCategory.objects.filter(id__in=grouped_articles.keys()).order_by('name')
        category_data = DebateCategoryArticleListSerializer(
            categories,
            many=True,
            context={
                'request': request,
                'grouped_articles': grouped_articles,
            },
        ).data

        if uncategorized:
            uncategorized_data = DebateArticleListItemSerializer(
                uncategorized,
                many=True,
                context={'request': request},
            ).data
            category_data.append(
                {
                    'name': '',
                    'description': '',
                    'image': None,
                    'articleList': uncategorized_data,
                }
            )

        return Response(category_data)

    def get_queryset(self):
        queryset = super().get_queryset()

        category = self.request.query_params.get('category')
        main_topic = self.request.query_params.get('mainTopic') or self.request.query_params.get('topic')
        query = self.request.query_params.get('query')

        if category:
            queryset = queryset.filter(debateCategory__name__icontains=category)

        if main_topic:
            queryset = queryset.filter(mainTopic__icontains=main_topic)

        if query:
            queryset = queryset.filter(
                Q(mainTopic__icontains=query)
                | Q(subTopic__icontains=query)
                | Q(debateCategory__name__icontains=query)
                | Q(article__icontains=query)
            )

        return queryset.distinct().order_by('order', 'mainTopic', 'subTopic', 'id')

    @action(detail=False, methods=['get'], url_path='categories')
    def categories(self, request):
        categories = list(
            DebateArticle.objects.exclude(mainTopic__exact='')
            .values_list('mainTopic', flat=True)
            .distinct()
            .order_by('mainTopic')
        )
        return Response({'categories': categories})


class DebateCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DebateCategory.objects.all().prefetch_related('articles').order_by('name')
    serializer_class = DebateCategoryNestedSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'id': ['exact'],
        'name': ['exact', 'icontains'],
    }
    search_fields = ['name', 'description', 'articles__mainTopic', 'articles__subTopic']
    ordering_fields = ['id', 'name']
    ordering = ['name']


class DebateQuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DebateQuestion.objects.prefetch_related('options').all().order_by('debate_article_id', 'order', 'id')
    serializer_class = DebateQuestionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'id': ['exact'],
        'debate_article': ['exact'],
        'debate_article__slug': ['exact'],
        'debate_article__language': ['exact'],
        'is_active': ['exact'],
    }
    search_fields = ['question_text', 'debate_article__mainTopic', 'debate_article__subTopic']
    ordering_fields = ['id', 'order', 'debate_article_id']
    ordering = ['debate_article_id', 'order', 'id']


class DebateQuestionOptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DebateQuestionOption.objects.select_related('question', 'question__debate_article').all().order_by(
        'question_id',
        'order',
        'id',
    )
    serializer_class = DebateQuestionOptionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'id': ['exact'],
        'question': ['exact'],
        'question__debate_article': ['exact'],
        'question__debate_article__slug': ['exact'],
        'is_correct': ['exact'],
    }
    search_fields = ['option_text', 'question__question_text']
    ordering_fields = ['id', 'order', 'question_id']
    ordering = ['question_id', 'order', 'id']
