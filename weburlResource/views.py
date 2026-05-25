from rest_framework import viewsets
from .models import WebUrlResource
from .serializers import WebUrlResourceSerializer

class WebUrlResourceViewSet(viewsets.ModelViewSet):
    queryset = WebUrlResource.objects.all().order_by('-created_at')
    serializer_class = WebUrlResourceSerializer
