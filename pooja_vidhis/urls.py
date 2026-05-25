from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PoojaVidhiViewSet

router = DefaultRouter()
router.register(r'articles', PoojaVidhiViewSet, basename='pooja-vidhi-article')

urlpatterns = [
    path('v1/pooja_vidhis/', include(router.urls)),
]
