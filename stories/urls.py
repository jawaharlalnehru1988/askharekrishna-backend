from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StoryViewSet, StoryDetailByIDView, StoryListByFiltersView

router = DefaultRouter()
router.register(r'articles', StoryViewSet, basename='story-article')

urlpatterns = [
    path('v1/stories/', include(router.urls)),
    # Short URL patterns using IDs
    path('v1/stories/id/<int:story_id>/', StoryDetailByIDView.as_view(), name='story-by-id'),
    path('v1/stories/filter/<int:topic_id>/<int:story_id>/', StoryListByFiltersView.as_view(), name='story-by-ids'),
]
