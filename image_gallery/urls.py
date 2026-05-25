from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ImageGalleryViewSet, ImageGalleryCategoryViewSet


router = DefaultRouter()
router.register(r'image-gallery', ImageGalleryViewSet, basename='image-gallery')
router.register(r'imageGalleryCategories', ImageGalleryCategoryViewSet, basename='imageGalleryCategories')

urlpatterns = [
    path('v1/', include(router.urls)),
]
