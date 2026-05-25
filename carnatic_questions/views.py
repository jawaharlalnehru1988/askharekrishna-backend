from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from askharekrishna_backend.permissions import IsAdminOrReadOnly
from .models import CarnaticKacheri, CarnaticLessonPractice, CarnaticQuestion, CarnaticSyllabus, Category
from .serializers import (
    CarnaticLessonPracticeSerializer,
    CategorySerializer,
    CarnaticKacheriSerializer,
    CarnaticQuestionSerializer,
    CarnaticSyllabusSerializer,
)


def filter_by_category(queryset, category_value):
    if not category_value:
        return queryset

    if category_value.isdigit():
        return queryset.filter(category_id=category_value)

    return queryset.filter(category__name__icontains=category_value)


class CarnaticSyllabusPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class CarnaticLessonPracticeViewSet(viewsets.ModelViewSet):
    queryset = CarnaticLessonPractice.objects.all()
    serializer_class = CarnaticLessonPracticeSerializer
    permission_classes = [IsAdminOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('query')

        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset


class CarnaticQuestionViewSet(viewsets.ModelViewSet):
    queryset = CarnaticQuestion.objects.select_related('category').all()
    serializer_class = CarnaticQuestionSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()

        category = self.request.query_params.get('category') or self.request.query_params.get('division')
        query = self.request.query_params.get('query')

        queryset = filter_by_category(queryset, category)

        if query:
            queryset = queryset.filter(
                Q(question__icontains=query)
                | Q(answer__icontains=query)
                | Q(category__name__icontains=query)
            )

        return queryset


class CarnaticKacheriViewSet(viewsets.ModelViewSet):
    queryset = CarnaticKacheri.objects.all()
    serializer_class = CarnaticKacheriSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = CarnaticSyllabusPagination

    def get_queryset(self):
        queryset = super().get_queryset()

        singer = self.request.query_params.get('singer')
        ragam = self.request.query_params.get('ragam')
        title = self.request.query_params.get('title')
        query = self.request.query_params.get('query')

        if title:
            queryset = queryset.filter(title__icontains=title)

        if singer:
            queryset = queryset.filter(singer__icontains=singer)

        if ragam:
            queryset = queryset.filter(ragam__icontains=ragam)

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
                | Q(singer__icontains=query)
                | Q(ragam__icontains=query)
                | Q(description__icontains=query)
            )

        return queryset


class CarnaticSyllabusViewSet(viewsets.ModelViewSet):
    queryset = CarnaticSyllabus.objects.select_related('category').prefetch_related('video_samples').all()
    serializer_class = CarnaticSyllabusSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = CarnaticSyllabusPagination

    def get_queryset(self):
        queryset = super().get_queryset()

        category = self.request.query_params.get('category') or self.request.query_params.get('division')
        query = self.request.query_params.get('query')

        queryset = filter_by_category(queryset, category)

        if query:
            queryset = queryset.filter(
                Q(topic__icontains=query)
                | Q(lesson__icontains=query)
                | Q(category__name__icontains=query)
            )

        return queryset

    @action(detail=False, methods=['get'], url_path='categories')
    def categories(self, request):
        categories = Category.objects.all()
        category_options = CategorySerializer(categories, many=True).data
        return Response({
            'categories': [category['name'] for category in category_options],
            'category_options': category_options,
        })
