from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import OurOtherSiteViewSet

router = DefaultRouter()
router.register(r'ourOtherSites', OurOtherSiteViewSet, basename='our-other-sites')

urlpatterns = [
    path('', include(router.urls)),
]
