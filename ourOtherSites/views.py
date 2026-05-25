from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from askharekrishna_backend.permissions import IsAdminOrReadOnly
from .models import OurOtherSite
from .serializers import OurOtherSiteSerializer


class OurOtherSiteViewSet(viewsets.ModelViewSet):
    queryset = OurOtherSite.objects.all()
    serializer_class = OurOtherSiteSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['web_url', 'purpose', 'features_available']
    ordering_fields = ['created_at', 'updated_at', 'web_url']
    ordering = ['-created_at']
