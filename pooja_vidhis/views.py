from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.response import Response
from .models import PoojaVidhi, PoojaVidhiTopic
from .serializers import (
    PoojaVidhiSerializer,
    PoojaVidhiTopicGroupedSerializer,
)


class PoojaVidhiViewSet(viewsets.ModelViewSet):
    queryset = PoojaVidhi.objects.prefetch_related('translations__questions__options').all().order_by('order', 'id')
    serializer_class = PoojaVidhiSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['slug']
    search_fields = ['translations__mainTopic', 'translations__subTopic', 'translations__article']
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
        lang = request.query_params.get('language') or request.query_params.get('lang') or 'en'
        lang = lang.strip().lower()

        grouped_articles = {}
        for article in queryset:
            trans = article.get_translation(lang)
            main_topic = trans.mainTopic if trans else ''
            if main_topic:
                grouped_articles.setdefault(main_topic, []).append(article)

        existing_topic_names = set(
            PoojaVidhiTopic.objects.filter(name__in=grouped_articles.keys()).values_list('name', flat=True)
        )

        topics = list(PoojaVidhiTopic.objects.filter(name__in=grouped_articles.keys()).order_by('order', 'name'))

        missing_topic_names = sorted(name for name in grouped_articles.keys() if name not in existing_topic_names)
        for name in missing_topic_names:
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
