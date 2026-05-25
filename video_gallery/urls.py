from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import VideoGalleryViewSet


router = DefaultRouter()
router.register(r'video-gallery', VideoGalleryViewSet, basename='video-gallery')

urlpatterns = [
    path('v1/', include(router.urls)),
]
