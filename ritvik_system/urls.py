from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import RitvikSectionViewSet, RitvikQAViewSet

router = DefaultRouter()
router.register(r'sections', RitvikSectionViewSet, basename='ritvik-section')
router.register(r'questions', RitvikQAViewSet, basename='ritvik-qa')

urlpatterns = [
    path('v1/ritvik/', include(router.urls)),
]
