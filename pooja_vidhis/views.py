from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.response import Response
from .models import PoojaVidhi, PoojaVidhiTopic
from .serializers import (
    PoojaVidhiSerializer,
    PoojaVidhiTopicGroupedSerializer,
)

class PoojaVidhiViewSet(viewsets.ModelViewSet):
    queryset = PoojaVidhi.objects.prefetch_related('questions__options').all().order_by(
        'order', 'mainTopic', 'subTopic', 'id'
    )
    serializer_class = PoojaVidhiSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['mainTopic', 'subTopic', 'slug', 'language']
    search_fields = ['mainTopic', 'subTopic', 'article']
    ordering_fields = ['order', 'created_at', 'mainTopic', 'subTopic']
    ordering = ['order', 'mainTopic', 'subTopic', 'id']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        grouped_articles = {}
        for article in queryset:
            grouped_articles.setdefault(article.mainTopic, []).append(article)

        existing_topic_names = set(
            PoojaVidhiTopic.objects.filter(name__in=grouped_articles.keys()).values_list('name', flat=True)
        )

        topics = list(PoojaVidhiTopic.objects.filter(name__in=grouped_articles.keys()).order_by('order', 'name'))

        missing_topic_names = sorted(name for name in grouped_articles.keys() if name not in existing_topic_names)
        for name in missing_topic_names:
            # Build lightweight topic-like objects for mainTopic values without a PoojaVidhiTopic row.
            topic = PoojaVidhiTopic(name=name, is_active=True)
            topic.pk = None
            topics.append(topic)

        grouped_data = PoojaVidhiTopicGroupedSerializer(
            topics,
            many=True,
            context={
                'request': request,
                'grouped_articles': grouped_articles,
            },
        ).data

        return Response(grouped_data)
