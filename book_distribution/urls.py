from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookDistributionViewSet

router = DefaultRouter()
router.register(r'articles', BookDistributionViewSet, basename='book-distribution-article')

urlpatterns = [
    path('v1/book_distribution/', include(router.urls)),
]
