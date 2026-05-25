from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import DebateArticleViewSet, DebateCategoryViewSet

router = DefaultRouter()
router.register(r'articles', DebateArticleViewSet, basename='debate-article')
router.register(r'categories', DebateCategoryViewSet, basename='debate-category')

urlpatterns = [
    path('v1/debate/', include(router.urls)),
]
