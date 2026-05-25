from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookLibraryViewSet

router = DefaultRouter()
router.register(r'document-library', BookLibraryViewSet, basename='document-library')

urlpatterns = [
    path('', include(router.urls)),
]
