from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from askharekrishna_backend.permissions import IsAdminOrReadOnly
from .models import Video
from .serializers import VideoSerializer


class VideoPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100


class VideoViewSet(viewsets.ModelViewSet):
    """
    CRUD endpoints for scripture Videos.

    Supports filtering by: book_name, chapter_number, sloka_number
    Supports searching by: chapter_name
    Supports ordering by: chapter_number, sloka_number
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = VideoPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['book_name', 'chapter_number', 'sloka_number', 'sloka_start', 'language']
    search_fields = []
    ordering_fields = ['chapter_number', 'sloka_start', 'language']
