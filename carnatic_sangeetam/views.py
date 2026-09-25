import re
from urllib.parse import quote
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from askharekrishna_backend.permissions import IsAdminOrReadOnly
from .models import (
    CarnaticKacheri,
    CarnaticLessonPractice,
    CarnaticSyllabus,
    Category,
    RagamLesson,
    MridangaLesson,
)
from .serializers import (
    CarnaticLessonPracticeSerializer,
    CategorySerializer,
    CarnaticKacheriSerializer,
    CarnaticSyllabusSerializer,
    RagamLessonSerializer,
    MridangaLessonSerializer,
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
    queryset = CarnaticLessonPractice.objects.select_related('category').prefetch_related('audios', 'videos').all()
    serializer_class = CarnaticLessonPracticeSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category') or self.request.query_params.get('division')
        query = self.request.query_params.get('query')

        queryset = filter_by_category(queryset, category)

        if query:
            queryset = queryset.filter(
                Q(lessonName__icontains=query)
                | Q(category__name__icontains=query)
            )

        return queryset


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
    queryset = CarnaticSyllabus.objects.prefetch_related('video_samples').all()
    serializer_class = CarnaticSyllabusSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = CarnaticSyllabusPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('query')

        if query:
            queryset = queryset.filter(
                Q(topic__icontains=query)
                | Q(lesson__icontains=query)
            )

        return queryset


class RagamLessonViewSet(viewsets.ModelViewSet):
    queryset = RagamLesson.objects.prefetch_related('audios', 'videos', 'famous_compositions__videos').all()
    serializer_class = RagamLessonSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = CarnaticSyllabusPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        melakartha = self.request.query_params.get('melakartha')
        query = self.request.query_params.get('query')

        if melakartha:
            queryset = queryset.filter(melakarthaNumber=melakartha)

        if query:
            queryset = queryset.filter(
                Q(raga_name__icontains=query)
                | Q(swarasthanas__icontains=query)
                | Q(arohanam_avarohanam__icontains=query)
                | Q(description__icontains=query)
                | Q(famousCompositions__icontains=query)
            )

        return queryset


class MridangaLessonViewSet(viewsets.ModelViewSet):
    queryset = MridangaLesson.objects.prefetch_related('audios', 'videos', 'kirtan_demos').all()
    serializer_class = MridangaLessonSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = CarnaticSyllabusPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        tala_category = self.request.query_params.get('tala_category')
        level = self.request.query_params.get('level')
        matras = self.request.query_params.get('matras')
        query = self.request.query_params.get('query')

        if tala_category:
            queryset = queryset.filter(tala_category__iexact=tala_category)

        if level:
            queryset = queryset.filter(level__iexact=level)

        if matras:
            queryset = queryset.filter(matras=matras)

        if query:
            queryset = queryset.filter(
                Q(tala_name__icontains=query)
                | Q(tala_category__icontains=query)
                | Q(mantras_and_notes__icontains=query)
                | Q(description__icontains=query)
            )

        return queryset


def slugify_name(name):
    return re.sub(r'[^a-z0-9]+', '-', (name or '').lower().strip()).strip('-')


class CarnaticSearchIndexView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        items = []

        # 1. Categories (only those with practice lessons)
        for cat in Category.objects.filter(lesson_practices__isnull=False).distinct().values('id', 'name', 'colorCode'):
            encoded_cat = quote(cat['name'])
            items.append({
                'id': f"cat-{cat['id']}",
                'type': 'category',
                'title': cat['name'],
                'subtitle': 'Practice Category',
                'category': 'Category',
                'url': f"/practice?category={encoded_cat}",
                'color': cat['colorCode'] if cat['colorCode'] and cat['colorCode'] != '#000000' else '#f59e0b',
                'icon': 'category',
                'badge': 'Category',
            })

        # 2. Carnatic Theory
        for syl in CarnaticSyllabus.objects.all().values('id', 'topic'):
            items.append({
                'id': f"theory-{syl['id']}",
                'type': 'theory',
                'title': syl['topic'],
                'subtitle': 'Carnatic Theory',
                'category': 'Theory',
                'url': f"/theory/{syl['id']}",
                'color': '#06b6d4',
                'icon': 'auto_stories',
                'badge': 'Theory',
            })

        # 3. Practice Lessons
        for prac in CarnaticLessonPractice.objects.select_related('category').all().values('id', 'lessonName', 'category__name'):
            cat_name = prac['category__name'] or 'Practice'
            items.append({
                'id': f"prac-{prac['id']}",
                'type': 'practice',
                'title': prac['lessonName'],
                'subtitle': f"Practice • {cat_name}",
                'category': cat_name,
                'url': f"/practice/{prac['id']}",
                'color': '#10b981',
                'icon': 'queue_music',
                'badge': 'Practice',
            })

        # 4. Ragam Lessons
        for rag in RagamLesson.objects.all().values('id', 'raga_name', 'melakarthaNumber', 'arohanam_avarohanam'):
            mela_str = f"Mela {rag['melakarthaNumber']}" if rag['melakarthaNumber'] else 'Raga Lakshana'
            swaras_preview = (rag['arohanam_avarohanam'] or '')[:50]
            sub = f"{mela_str} • {swaras_preview}" if swaras_preview else mela_str
            items.append({
                'id': f"rag-{rag['id']}",
                'type': 'ragam',
                'title': rag['raga_name'],
                'subtitle': sub,
                'category': 'Ragam',
                'url': f"/ragams/{rag['id']}",
                'color': '#ec4899',
                'icon': 'music_note',
                'badge': 'Ragam',
            })

        # 5. Mridanga Lessons
        for mri in MridangaLesson.objects.all().values('id', 'tala_name', 'tala_category', 'level', 'matras'):
            meta_parts = []
            if mri['tala_category']:
                meta_parts.append(mri['tala_category'].capitalize())
            if mri['level']:
                meta_parts.append(mri['level'].capitalize())
            if mri['matras']:
                meta_parts.append(f"{mri['matras']} Matras")
            sub = ' • '.join(meta_parts) if meta_parts else 'Mridanga Lesson'
            items.append({
                'id': f"mri-{mri['id']}",
                'type': 'mridanga',
                'title': mri['tala_name'],
                'subtitle': sub,
                'category': 'Mridanga',
                'url': f"/mridanga/{mri['id']}",
                'color': '#8b5cf6',
                'icon': 'graphic_eq',
                'badge': 'Mridanga',
            })

        return Response(items)



