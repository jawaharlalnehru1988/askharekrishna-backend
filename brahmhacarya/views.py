from rest_framework import viewsets, filters, generics
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from askharekrishna_backend.permissions import IsAdminOrReadOnly
from .models import BrahmhacaryaArticle, BrahmhacaryaRegistration
from .serializers import BrahmhacaryaArticleSerializer, BrahmhacaryaRegistrationSerializer


class BrahmhacaryaArticleViewSet(viewsets.ModelViewSet):
    queryset = BrahmhacaryaArticle.objects.all()
    serializer_class = BrahmhacaryaArticleSerializer
    lookup_field = 'slug'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['language', 'category', 'is_published']
    search_fields = ['title', 'language', 'category', 'excerpt', 'content']
    ordering_fields = ['order', 'created_at', 'updated_at', 'published_at', 'title']
    ordering = ['order', '-published_at', '-created_at']


class BrahmhacaryaRegistrationCreateAPIView(generics.CreateAPIView):
    queryset = BrahmhacaryaRegistration.objects.all()
    serializer_class = BrahmhacaryaRegistrationSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminOrReadOnly]
