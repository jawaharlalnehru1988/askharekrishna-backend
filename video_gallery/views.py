from rest_framework import viewsets
from askharekrishna_backend.permissions import IsAdminOrReadOnly
from .models import VideoGallery
from .serializers import VideoGallerySerializer


class VideoGalleryViewSet(viewsets.ModelViewSet):
    queryset = VideoGallery.objects.all()
    serializer_class = VideoGallerySerializer
    permission_classes = [IsAdminOrReadOnly]
