from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, pagination, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import DebateArticle, DebateCategory
from .serializers import (
    DebateArticleSerializer,
    DebateCategoryNestedSerializer,
    DebateArticleListItemSerializer,
    DebateCategoryArticleListSerializer,
)


class DebateArticlePagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100


class DebateArticleViewSet(viewsets.ModelViewSet):
    queryset = DebateArticle.objects.all().order_by('order', 'topic', 'subTopic', 'id')
    serializer_class = DebateArticleSerializer
    pagination_class = DebateArticlePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'id': ['exact'],
        'topic': ['exact', 'icontains'],
        'debateCategory': ['exact'],
        'debateCategory__name': ['exact', 'icontains'],
        'subTopic': ['exact', 'icontains'],
        'slug': ['exact'],
        'language': ['exact'],
    }
    search_fields = ['topic', 'subTopic', 'article', 'debateCategory__name']
    ordering_fields = ['id', 'order', 'created_at', 'topic', 'subTopic']
    ordering = ['order', 'topic', 'subTopic', 'id']

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
        topic = self.request.query_params.get('topic')
        query = self.request.query_params.get('query')

        if category:
            queryset = queryset.filter(debateCategory__name__icontains=category)

        if topic:
            queryset = queryset.filter(topic__icontains=topic)

        if query:
            queryset = queryset.filter(
                Q(topic__icontains=query)
                | Q(subTopic__icontains=query)
                | Q(debateCategory__name__icontains=query)
                | Q(article__icontains=query)
            )

        return queryset.distinct().order_by('order', 'topic', 'subTopic', 'id')

    @action(detail=False, methods=['get'], url_path='categories')
    def categories(self, request):
        categories = list(
            DebateArticle.objects.exclude(topic__exact='')
            .values_list('topic', flat=True)
            .distinct()
            .order_by('topic')
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
    search_fields = ['name', 'description', 'articles__topic', 'articles__subTopic']
    ordering_fields = ['id', 'name']
    ordering = ['name']
