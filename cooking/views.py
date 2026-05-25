from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, pagination, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CookingArticle
from .serializers import CookingArticleSerializer


class CookingArticlePagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100


class CookingArticleViewSet(viewsets.ModelViewSet):
    queryset = CookingArticle.objects.all().order_by('order', 'mainTopic', 'subTopic', 'id')
    serializer_class = CookingArticleSerializer
    pagination_class = CookingArticlePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'mainTopic', 'subTopic', 'slug', 'language']
    search_fields = ['mainTopic', 'subTopic', 'article']
    ordering_fields = ['id', 'order', 'created_at', 'mainTopic', 'subTopic']
    ordering = ['order', 'mainTopic', 'subTopic', 'id']

    def get_queryset(self):
        queryset = super().get_queryset()

        category = self.request.query_params.get('category') or self.request.query_params.get('mainTopic')
        query = self.request.query_params.get('query')

        if category:
            queryset = queryset.filter(mainTopic__icontains=category)

        if query:
            queryset = queryset.filter(
                Q(mainTopic__icontains=query)
                | Q(subTopic__icontains=query)
                | Q(article__icontains=query)
            )

        return queryset.distinct().order_by('order', 'mainTopic', 'subTopic', 'id')

    @action(detail=False, methods=['get'], url_path='categories')
    def categories(self, request):
        categories = list(
            CookingArticle.objects.exclude(mainTopic__isnull=True)
            .exclude(mainTopic__exact='')
            .values_list('mainTopic', flat=True)
            .distinct()
            .order_by('mainTopic')
        )
        return Response({'categories': categories})
