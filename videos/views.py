from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from askharekrishna_backend.permissions import IsAdminOrReadOnly
from .models import Video
from .serializers import VideoSerializer


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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['book_name', 'chapter_number', 'sloka_number', 'language']
    search_fields = []
    ordering_fields = ['chapter_number', 'sloka_number', 'language']
