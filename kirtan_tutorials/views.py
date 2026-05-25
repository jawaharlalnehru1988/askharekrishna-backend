from rest_framework import viewsets
from .models import KirtanTutorial
from .serializers import KirtanTutorialSerializer

class KirtanTutorialViewSet(viewsets.ModelViewSet):
    queryset = KirtanTutorial.objects.all()
    serializer_class = KirtanTutorialSerializer
    filterset_fields = ['mainTopic', 'subTopic', 'slug', 'language']
    search_fields = ['mainTopic', 'subTopic', 'article']
    ordering_fields = ['order', 'created_at']
