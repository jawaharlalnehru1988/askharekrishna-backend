from rest_framework import routers
from .views import WebUrlResourceViewSet

router = routers.DefaultRouter()
router.register(r'weburl-resources', WebUrlResourceViewSet)

urlpatterns = router.urls
