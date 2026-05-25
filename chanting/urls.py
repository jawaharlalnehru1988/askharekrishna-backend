from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChantingArticleViewSet

router = DefaultRouter()
router.register(r'articles', ChantingArticleViewSet, basename='chanting-article')

urlpatterns = [
    path('v1/chanting/', include(router.urls)),
]
