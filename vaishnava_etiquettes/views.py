from rest_framework import viewsets
from .models import VaishnavaEtiquette
from .serializers import VaishnavaEtiquetteSerializer

class VaishnavaEtiquetteViewSet(viewsets.ModelViewSet):
    queryset = VaishnavaEtiquette.objects.all()
    serializer_class = VaishnavaEtiquetteSerializer
    filterset_fields = ['mainTopic', 'subTopic', 'slug', 'language']
    search_fields = ['mainTopic', 'subTopic', 'article']
    ordering_fields = ['order', 'created_at']
