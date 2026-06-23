from django.urls import path
from .views import PushRoadmapAPIView, RoadmapListView, RoadmapDetailView, ExplainSubtopicAPIView, SubtopicQuizAPIView

urlpatterns = [
    path('import-syllabus/push-roadmap', PushRoadmapAPIView.as_view(), name='push-roadmap'),
    path('roadmaps/', RoadmapListView.as_view(), name='roadmap-list'),
    path('roadmaps/<str:routerLink>/', RoadmapDetailView.as_view(), name='roadmap-detail'),
    path('explain-subtopic/', ExplainSubtopicAPIView.as_view(), name='explain-subtopic'),
    path('subtopic-quiz/', SubtopicQuizAPIView.as_view(), name='subtopic-quiz'),
]
