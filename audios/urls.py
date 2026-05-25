from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AudioViewSet, audio_bg_seed

router = DefaultRouter()
router.register(r'audio-bg', AudioViewSet, basename='audio-bg')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('audio-bg', audio_bg_seed, name='audio-bg'),
]
