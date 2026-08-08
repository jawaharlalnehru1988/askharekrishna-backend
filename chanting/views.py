from rest_framework import viewsets
from .models import ChantingArticle
from .serializers import ChantingArticleSerializer

class ChantingArticleViewSet(viewsets.ModelViewSet):
    queryset = ChantingArticle.objects.all()
    serializer_class = ChantingArticleSerializer
    filterset_fields = ['mainTopic', 'subTopic', 'slug', 'language']
    search_fields = ['mainTopic', 'subTopic', 'article']
    ordering_fields = ['order', 'created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        lang = self.request.query_params.get('lang') or self.request.query_params.get('language')
        if lang:
            queryset = queryset.filter(language=lang)
        return queryset

from django.http import JsonResponse
from .models import MainTopicTranslation

def get_topic_translations(request):
    topic = request.GET.get('topic')
    lang = request.GET.get('lang')
    if topic and lang:
        try:
            translation = MainTopicTranslation.objects.get(english_topic=topic, language=lang)
            return JsonResponse({'translated_topic': translation.translated_topic})
        except MainTopicTranslation.DoesNotExist:
            return JsonResponse({'translated_topic': ''}, status=404)
    return JsonResponse({'error': 'Missing topic or lang'}, status=400)
