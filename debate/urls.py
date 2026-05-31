from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    DebateArticleViewSet,
    DebateCategoryViewSet,
    DebateQuestionViewSet,
    DebateQuestionOptionViewSet,
)

router = DefaultRouter()
router.register(r'articles', DebateArticleViewSet, basename='debate-article')
router.register(r'categories', DebateCategoryViewSet, basename='debate-category')
router.register(r'questions', DebateQuestionViewSet, basename='debate-question')
router.register(r'question-options', DebateQuestionOptionViewSet, basename='debate-question-option')

urlpatterns = [
    path('v1/debate/', include(router.urls)),
]
