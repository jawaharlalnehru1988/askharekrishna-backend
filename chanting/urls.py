from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChantingArticleViewSet, get_topic_translations

router = DefaultRouter()
router.register(r'articles', ChantingArticleViewSet, basename='chanting-article')

urlpatterns = [
    path('v1/chanting/admin/topic-translations/', get_topic_translations, name='topic-translations'),
    path('v1/chanting/', include(router.urls)),
]
