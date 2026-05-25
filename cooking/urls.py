from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CookingArticleViewSet

router = DefaultRouter()
router.register(r'articles', CookingArticleViewSet, basename='cooking-article')

urlpatterns = [
    path('v1/cooking/', include(router.urls)),
]
