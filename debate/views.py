from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, pagination, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import DebateArticle, DebateCategory, DebateQuestion, DebateQuestionOption, DebateArticleTranslation
from .serializers import (
    DebateArticleSerializer,
    DebateCategoryNestedSerializer,
    DebateArticleListItemSerializer,
    DebateCategoryArticleListSerializer,
    DebateQuestionSerializer,
    DebateQuestionOptionSerializer,
    DebateArticleTranslationUpdateSerializer,
)


class DebateArticlePagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100


class DebateArticleViewSet(viewsets.ModelViewSet):
    queryset = DebateArticle.objects.prefetch_related('questions__options', 'translations').all().order_by('order', 'id')
    serializer_class = DebateArticleSerializer
    pagination_class = DebateArticlePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'id': ['exact'],
        'translations__debateCategory': ['exact'],
        'translations__debateCategory__name': ['exact', 'icontains'],
        'translations__subTopic': ['exact', 'icontains'],
        'slug': ['exact'],
        'translations__language': ['exact'],
    }
    search_fields = ['translations__debateCategory__name', 'translations__subTopic', 'translations__article']
    ordering_fields = ['id', 'order', 'created_at']
    ordering = ['order', 'id']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        grouped_articles = {}
        uncategorized = []

        # Group by the translation's category for the requested language
        req_lang = request.query_params.get('language', 'en')
        
        for article in queryset:
            t = article.translations.filter(language=req_lang).first()
            if not t or t.debateCategory_id is None:
                uncategorized.append(article)
                continue
            grouped_articles.setdefault(t.debateCategory_id, []).append(article)

        categories = DebateCategory.objects.filter(id__in=grouped_articles.keys()).order_by('order', 'name')
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
        lang = self.request.query_params.get('language', 'en')

        if category:
            queryset = queryset.filter(translations__language=lang, translations__debateCategory__name__icontains=category)

        if main_topic:
            # We don't have mainTopic directly anymore, we filter by category name
            queryset = queryset.filter(translations__language=lang, translations__debateCategory__name__icontains=main_topic)

        if query:
            queryset = queryset.filter(
                Q(translations__debateCategory__name__icontains=query)
                | Q(translations__subTopic__icontains=query)
                | Q(translations__article__icontains=query)
            )

        return queryset.distinct().order_by('order', 'id')

    @action(detail=False, methods=['get'], url_path='categories')
    def categories(self, request):
        lang = request.query_params.get('language', 'en')
        categories = list(
            DebateArticle.objects.filter(translations__language=lang).exclude(translations__debateCategory__isnull=True)
            .values_list('translations__debateCategory__name', flat=True)
            .distinct()
        )
        return Response({'categories': categories})


class DebateCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DebateCategory.objects.all().prefetch_related('articles').order_by('order', 'name')
    serializer_class = DebateCategoryNestedSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'id': ['exact'],
        'name': ['exact', 'icontains'],
    }
    search_fields = ['name', 'description', 'articles__debateCategory__name', 'articles__translations__subTopic']
    ordering_fields = ['id', 'order', 'name']
    ordering = ['order', 'name']


class DebateQuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DebateQuestion.objects.prefetch_related('options').all().order_by('debate_article_id', 'order', 'id')
    serializer_class = DebateQuestionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'id': ['exact'],
        'debate_article': ['exact'],
        'debate_article__slug': ['exact'],
        'debate_article__translations__language': ['exact'],
        'is_active': ['exact'],
    }
    search_fields = ['question_text', 'debate_article__translations__debateCategory__name', 'debate_article__translations__subTopic']
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


class DebateArticleTranslationViewSet(viewsets.ModelViewSet):
    queryset = DebateArticleTranslation.objects.all()
    serializer_class = DebateArticleTranslationUpdateSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'id': ['exact'],
        'article_parent': ['exact'],
        'language': ['exact'],
    }
