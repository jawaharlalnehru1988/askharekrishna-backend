from rest_framework.routers import DefaultRouter
from .views import SubscriberViewSet, SubscriberQuizAttemptViewSet


router = DefaultRouter()
router.register(r'subscribers', SubscriberViewSet, basename='subscriber')
router.register(r'subscriber-quiz-attempts', SubscriberQuizAttemptViewSet, basename='subscriber-quiz-attempt')

urlpatterns = router.urls
