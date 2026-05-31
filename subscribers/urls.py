from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import SubscriberDashboardView, SubscriberViewSet, SubscriberQuizAttemptViewSet


router = DefaultRouter()
router.register(r'subscribers', SubscriberViewSet, basename='subscriber')
router.register(r'subscriber-quiz-attempts', SubscriberQuizAttemptViewSet, basename='subscriber-quiz-attempt')

urlpatterns = router.urls
urlpatterns += [
	path('subscriber-dashboard/', SubscriberDashboardView.as_view(), name='subscriber-dashboard'),
]
