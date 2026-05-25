from rest_framework import viewsets
from .models import BookDistribution
from .serializers import BookDistributionSerializer

class BookDistributionViewSet(viewsets.ModelViewSet):
    queryset = BookDistribution.objects.all()
    serializer_class = BookDistributionSerializer
    filterset_fields = ['mainTopic', 'subTopic', 'slug', 'language']
    search_fields = ['mainTopic', 'subTopic', 'article']
    ordering_fields = ['order', 'created_at']
