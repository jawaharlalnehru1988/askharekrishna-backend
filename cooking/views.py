from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, pagination, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CookingArticle, CookingMainTopic
from .serializers import CookingArticleSerializer, CookingMainTopicSerializer


class CookingArticlePagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 200


class CookingArticleViewSet(viewsets.ModelViewSet):
    queryset = CookingArticle.objects.select_related('topic').prefetch_related('translations').all().order_by('order', 'id')
    serializer_class = CookingArticleSerializer
    pagination_class = CookingArticlePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'slug']
    search_fields = ['translations__mainTopic', 'translations__subTopic', 'translations__article', 'topic__name']
    ordering_fields = ['id', 'order', 'created_at']
    ordering = ['order', 'id']

    def get_queryset(self):
        queryset = super().get_queryset()

        category = self.request.query_params.get('category') or self.request.query_params.get('mainTopic')
        query = self.request.query_params.get('query')
        lang = self.request.query_params.get('language') or self.request.query_params.get('lang')

        if category:
            queryset = queryset.filter(
                Q(topic__name__icontains=category)
                | Q(translations__mainTopic__icontains=category)
            )

        if query:
            queryset = queryset.filter(
                Q(translations__mainTopic__icontains=query)
                | Q(translations__subTopic__icontains=query)
                | Q(translations__article__icontains=query)
                | Q(topic__name__icontains=query)
            )

        if lang:
            queryset = queryset.filter(translations__language_code=lang.strip().lower())

        return queryset.distinct().order_by('order', 'id')

    @action(detail=False, methods=['get'], url_path='categories')
    def categories(self, request):
        lang = request.query_params.get('language') or request.query_params.get('lang') or 'en'
        topics = CookingMainTopic.objects.filter(is_active=True).order_by('order', 'name')
        if topics.exists():
            category_names = [t.get_localized_name(lang) for t in topics]
        else:
            category_names = list(
                CookingArticle.objects.filter(topic__isnull=False)
                .values_list('topic__name', flat=True)
                .distinct()
                .order_by('topic__name')
            )
        return Response({'categories': category_names})
