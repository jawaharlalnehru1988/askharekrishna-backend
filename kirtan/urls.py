from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KirtanViewSet, KirtanCategoryViewSet

router = DefaultRouter()
router.register(r'kirtans', KirtanViewSet, basename='kirtan')
router.register(r'kirtan-categories', KirtanCategoryViewSet, basename='kirtan-category')

urlpatterns = [
    path('v1/', include(router.urls)),
]
