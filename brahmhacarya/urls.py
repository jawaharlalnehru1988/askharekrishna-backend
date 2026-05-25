from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BrahmhacaryaArticleViewSet, BrahmhacaryaRegistrationCreateAPIView


router = DefaultRouter()
router.register(r'brahmhacarya', BrahmhacaryaArticleViewSet, basename='brahmhacarya')

urlpatterns = [
    path('v1/brahmhacarya/registration/', BrahmhacaryaRegistrationCreateAPIView.as_view(), name='brahmhacarya-registration'),
    path('v1/', include(router.urls)),
]
