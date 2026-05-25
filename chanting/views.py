from rest_framework import viewsets
from .models import ChantingArticle
from .serializers import ChantingArticleSerializer

class ChantingArticleViewSet(viewsets.ModelViewSet):
    queryset = ChantingArticle.objects.all()
    serializer_class = ChantingArticleSerializer
    filterset_fields = ['mainTopic', 'subTopic', 'slug']
    search_fields = ['mainTopic', 'subTopic', 'article']
    ordering_fields = ['order', 'created_at']
