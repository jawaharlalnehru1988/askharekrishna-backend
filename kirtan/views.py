from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from askharekrishna_backend.permissions import IsAdminOrReadOnly
from .models import Kirtan, KirtanCategory
from .serializers import KirtanSerializer, KirtanCategorySerializer


class KirtanCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = KirtanCategory.objects.prefetch_related('translations').all()
    serializer_class = KirtanCategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'translations__name']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']


class KirtanViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Kirtan CRUD operations.
    
    Supports:
    - List all kirtans
    - Create new kirtan
    - Retrieve specific kirtan
    - Update kirtan
    - Delete kirtan
    - Filter by category
    - Search by title, description, authorName, lyrics
    """
    queryset = Kirtan.objects.prefetch_related('translations').all()
    serializer_class = KirtanSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'category__name']
    # Updated to search on translation fields
    search_fields = ['translations__title', 'translations__description', 'translations__authorName', 'translations__lyrics', 'category__name']
    ordering_fields = ['created_at', 'order', 'translations__title']
    ordering = ['order', '-created_at']
