from rest_framework import viewsets, filters, status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from askharekrishna_backend.permissions import IsAdminOrReadOnly
from .models import Story, StoryMainTopic
from .serializers import StorySerializer, StoryListItemSerializer, StoryMainTopicGroupedSerializer


class StoryPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.select_related('mainTopic').prefetch_related(
        'questions__options'
    ).all().order_by('order', 'mainTopic__name', 'subTopic', 'id')
    serializer_class = StorySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = StoryPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'mainTopic': ['exact'],
        'mainTopic__name': ['exact', 'icontains'],
        'subTopic': ['exact'],
        'slug': ['exact'],
        'language': ['exact'],
    }
    search_fields = ['mainTopic__name', 'subTopic', 'article']
    ordering_fields = ['order', 'created_at']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        grouped_articles = {}
        for story in queryset:
            if story.mainTopic_id is None:
                continue
            grouped_articles.setdefault(story.mainTopic_id, []).append(story)

        topics = StoryMainTopic.objects.filter(id__in=grouped_articles.keys()).order_by('name')
        grouped_data = StoryMainTopicGroupedSerializer(
            topics,
            many=True,
            context={
                'request': request,
                'grouped_articles': grouped_articles,
            },
        ).data

        return Response(grouped_data)


class StoryDetailByIDView(APIView):
    """Get a single story by its ID. Supports optional language filter."""
    
    def get(self, request, story_id):
        try:
            story = Story.objects.get(id=story_id)
            serializer = StorySerializer(story)
            return Response(serializer.data)
        except Story.DoesNotExist:
            return Response(
                {'error': f'Story with id {story_id} not found'},
                status=status.HTTP_404_NOT_FOUND
            )


class StoryListByFiltersView(APIView):
    """Get stories by topic ID and story ID. Supports language filtering."""
    
    def get(self, request, topic_id, story_id):
        try:
            story = Story.objects.get(
                id=story_id,
                mainTopic_id=topic_id
            )
            serializer = StorySerializer(story)
            return Response(serializer.data)
        except Story.DoesNotExist:
            return Response(
                {'error': f'Story not found with these IDs: topic={topic_id}, story={story_id}'},
                status=status.HTTP_404_NOT_FOUND
            )
