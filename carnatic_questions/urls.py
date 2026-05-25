from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CarnaticKacheriViewSet, CarnaticQuestionViewSet, CarnaticSyllabusViewSet, CategoryViewSet, CarnaticLessonPracticeViewSet


router = DefaultRouter()
router.register(r'carnatic-categories', CategoryViewSet, basename='carnatic-categories')
router.register(r'carnatic-kacheri', CarnaticKacheriViewSet, basename='carnatic-kacheri')
router.register(r'carnatic-questions', CarnaticQuestionViewSet, basename='carnatic-questions')
router.register(r'carnatic-syllabus', CarnaticSyllabusViewSet, basename='carnatic-syllabus')
router.register(r'carnatic-lesson-practice', CarnaticLessonPracticeViewSet, basename='carnatic-lesson-practice')

urlpatterns = [
    path('v1/', include(router.urls)),
]
