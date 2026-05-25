from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KirtanTutorialViewSet

router = DefaultRouter()
router.register(r'articles', KirtanTutorialViewSet, basename='kirtan-tutorial-article')

urlpatterns = [
    path('v1/kirtan_tutorials/', include(router.urls)),
]
