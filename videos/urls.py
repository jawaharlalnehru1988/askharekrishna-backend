from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoViewSet


router = DefaultRouter()
router.register(r'videos', VideoViewSet, basename='videos')

urlpatterns = [
    path('v1/', include(router.urls)),
]
