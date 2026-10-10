from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    RitvikSection,
    RitvikQA,
    RitvikSectionTranslation,
    RitvikQATranslation,
)
from .serializers import (
    RitvikSectionSerializer,
    RitvikQAListSerializer,
    RitvikQADetailSerializer,
)


class RitvikSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RitvikSection.objects.all().prefetch_related('translations', 'questions')
    serializer_class = RitvikSectionSerializer
    lookup_field = 'section_number'
    ordering = ['order', 'section_number']


class RitvikQAViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RitvikQA.objects.filter(is_published=True).select_related('section').prefetch_related('translations', 'section__translations')
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['question_code', 'translations__question', 'translations__answer', 'translations__summary']
    ordering_fields = ['order', 'section__section_number', 'question_code']
    ordering = ['section__section_number', 'order', 'id']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RitvikQADetailSerializer
        return RitvikQAListSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        section_num = self.request.query_params.get('section')
        if section_num:
            qs = qs.filter(section__section_number=section_num)
        return qs
