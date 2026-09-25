from rest_framework import viewsets, filters, status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from askharekrishna_backend.permissions import IsAdminOrReadOnly
from .models import Story, StoryMainTopic, StoryTranslation
from .serializers import StorySerializer, StoryListItemSerializer, StoryMainTopicGroupedSerializer


class StoryPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.select_related('topic').prefetch_related('translations__questions__options').all().order_by('order', 'id')
    serializer_class = StorySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = StoryPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['slug']
    search_fields = ['translations__mainTopic', 'translations__subTopic', 'translations__article', 'topic__name']
    ordering_fields = ['order', 'created_at', 'id']
    ordering = ['order', 'id']

    def get_queryset(self):
        qs = super().get_queryset()
        if self.action == 'list':
            language = self.request.query_params.get('language') or self.request.query_params.get('lang')
            if language:
                qs = qs.filter(translations__language_code=language.strip().lower()).distinct()
        return qs

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        grouped_articles = {}
        for story in queryset:
            if story.topic_id:
                grouped_articles.setdefault(story.topic_id, []).append(story)

        # Retrieve active topics ordered by 'order', 'name'
        topics = list(StoryMainTopic.objects.filter(is_active=True).order_by('order', 'name'))
        topics_with_stories = [t for t in topics if t.id in grouped_articles]

        grouped_data = StoryMainTopicGroupedSerializer(
            topics_with_stories,
            many=True,
            context={
                'request': request,
                'grouped_articles': grouped_articles,
            },
        ).data

        return Response(grouped_data)


class StoryDetailByIDView(APIView):
    """Get a single story by its ID. Supports optional language query parameter."""
    
    def get(self, request, story_id):
        try:
            story = Story.objects.select_related('topic').prefetch_related('translations__questions__options').get(id=story_id)
            serializer = StorySerializer(story, context={'request': request})
            return Response(serializer.data)
        except Story.DoesNotExist:
            return Response(
                {'error': f'Story with id {story_id} not found'},
                status=status.HTTP_404_NOT_FOUND
            )


class StoryListByFiltersView(APIView):
    """Get story by story ID. Supports language filtering."""
    
    def get(self, request, topic_id, story_id):
        try:
            story = Story.objects.select_related('topic').prefetch_related('translations__questions__options').get(id=story_id)
            serializer = StorySerializer(story, context={'request': request})
            return Response(serializer.data)
        except Story.DoesNotExist:
            return Response(
                {'error': f'Story not found with ID: {story_id}'},
                status=status.HTTP_404_NOT_FOUND
            )

