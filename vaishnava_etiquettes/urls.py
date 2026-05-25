from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VaishnavaEtiquetteViewSet

router = DefaultRouter()
router.register(r'articles', VaishnavaEtiquetteViewSet, basename='vaishnava-etiquette-article')

urlpatterns = [
    path('v1/vaishnava_etiquettes/', include(router.urls)),
]
