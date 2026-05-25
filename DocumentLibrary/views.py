from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import BookLibrary
from .serializers import BookLibrarySerializer, BookLibraryListSerializer


class BookLibraryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Book Library API
    
    Endpoints:
    - GET /api/books/ - List all books
    - GET /api/books/{id}/ - Get specific book
    - GET /api/books/category/{category}/ - Filter by category
    - GET /api/books/search/?search=query - Search books
    - POST /api/books/ - Create new book (admin only)
    - PUT /api/books/{id}/ - Update book (admin only)
    - DELETE /api/books/{id}/ - Delete book (admin only)
    - POST /api/books/{id}/download/ - Increment download counter
    """
    
    queryset = BookLibrary.objects.all()
    serializer_class = BookLibrarySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'language', 'book_format', 'author']
    search_fields = ['title', 'author', 'description']
    ordering_fields = ['created_at', 'title', 'downloads', 'author']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        """Use simplified serializer for list view"""
        if self.action == 'list':
            return BookLibraryListSerializer
        return BookLibrarySerializer
    
    @action(detail=False, methods=['get'], url_path='category/(?P<category>[^/.]+)')
    def by_category(self, request, category=None):
        """Get books by category"""
        books = self.queryset.filter(category=category)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def download(self, request, pk=None):
        """Increment download counter when book is downloaded"""
        book = self.get_object()
        book.increment_downloads()
        return Response({
            'message': 'Download recorded',
            'downloads': book.downloads
        })
    
    @action(detail=False, methods=['get'])
    def popular(self, request):
        """Get most downloaded books"""
        books = self.queryset.order_by('-downloads')[:10]
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def recent(self, request):
        """Get recently added books"""
        books = self.queryset.order_by('-created_at')[:10]
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
