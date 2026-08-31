from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    CarnaticKacheriViewSet,
    CarnaticSyllabusViewSet,
    CategoryViewSet,
    CarnaticLessonPracticeViewSet,
    RagamLessonViewSet,
    MridangaLessonViewSet,
)


router = DefaultRouter()
router.register(r'carnatic-categories', CategoryViewSet, basename='carnatic-categories')
router.register(r'carnatic-kacheri', CarnaticKacheriViewSet, basename='carnatic-kacheri')
router.register(r'carnatic-syllabus', CarnaticSyllabusViewSet, basename='carnatic-syllabus')
router.register(r'carnatic-lesson-practice', CarnaticLessonPracticeViewSet, basename='carnatic-lesson-practice')
router.register(r'carnatic-ragam-lessons', RagamLessonViewSet, basename='carnatic-ragam-lessons')
router.register(r'carnatic-mridanga-lessons', MridangaLessonViewSet, basename='carnatic-mridanga-lessons')

urlpatterns = [
    path('v1/', include(router.urls)),
]

