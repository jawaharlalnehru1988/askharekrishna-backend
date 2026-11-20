from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, pagination, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CookingArticle, CookingMainTopic
from .serializers import CookingArticleSerializer, CookingMainTopicSerializer


class CookingArticlePagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 200


class CookingArticleViewSet(viewsets.ModelViewSet):
    queryset = CookingArticle.objects.select_related('topic').prefetch_related('translations').all().order_by('order', 'id')
    serializer_class = CookingArticleSerializer
    pagination_class = CookingArticlePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'slug']
    search_fields = ['translations__mainTopic', 'translations__subTopic', 'translations__article', 'topic__name']
    ordering_fields = ['id', 'order', 'created_at']
    ordering = ['order', 'id']

    def get_queryset(self):
        queryset = super().get_queryset()

        category = (
            self.request.query_params.get('cat')
            or self.request.query_params.get('category')
            or self.request.query_params.get('mainTopic')
        )
        major = self.request.query_params.get('major') or self.request.query_params.get('majorCategory')
        query = self.request.query_params.get('query')
        lang = self.request.query_params.get('language') or self.request.query_params.get('lang')

        if major:
            major_clean = str(major).strip().lower()
            if major_clean in ('1', 'modern'):
                queryset = queryset.filter(topic__name__in=[
                    'Breads / Rotis', 'Sambar Items', 'Rasam Items', 'Variety Rice Items',
                    'Sabji / Vegetable Preparations', 'Chutneys', 'Snack Items', 'Sweet Items',
                    'Hot Drinks', 'Hot Drinks (No Coffee / Tea)', 'Preservative Foods'
                ])
            elif major_clean in ('2', 'ayurvedic'):
                queryset = queryset.filter(
                    Q(topic__name='Ayurvedic Shastra Recipes') | Q(topic__name__startswith='Diet:')
                )
            elif major_clean in ('3', 'philosophy'):
                queryset = queryset.filter(topic__name__in=[
                    'Krishna Conscious Principles for Cooking',
                    'Why No Onion & Garlic',
                    'Why Veg?',
                    'Health Care of Devotees',
                ])

        if category:
            cat_str = str(category).strip()
            if cat_str.isdigit():
                queryset = queryset.filter(topic__id=int(cat_str))
            else:
                queryset = queryset.filter(
                    Q(topic__name__icontains=cat_str)
                    | Q(translations__mainTopic__icontains=cat_str)
                )

        if query:
            queryset = queryset.filter(
                Q(translations__mainTopic__icontains=query)
                | Q(translations__subTopic__icontains=query)
                | Q(translations__article__icontains=query)
                | Q(topic__name__icontains=query)
            )

        if lang:
            queryset = queryset.filter(translations__language_code=lang.strip().lower())

        return queryset.distinct().order_by('order', 'id')

    @action(detail=False, methods=['get'], url_path='categories')
    def categories(self, request):
        lang = request.query_params.get('language') or request.query_params.get('lang') or 'en'
        topics = CookingMainTopic.objects.filter(is_active=True).order_by('order', 'name')
        category_names = []
        category_details = []
        
        # Category icon map for visual flair
        icon_map = {
            'Sambar Items': '🍲',
            'Rasam Items': '🥣',
            'Variety Rice Items': '🍚',
            'Sabji / Vegetable Preparations': '🥗',
            'Breads / Rotis': '🫓',
            'Chutneys': '🫙',
            'Snack Items': '🥟',
            'Sweet Items': '🍯',
            'Hot Drinks': '☕',
            'Hot Drinks (No Coffee / Tea)': '🍵',
            'Preservative Foods': '🥒',
            'Ayurvedic Shastra Recipes': '🌿',
            'Health Care of Devotees': '🧘',
            'Krishna Conscious Principles for Cooking': '🪷',
            'Why No Onion & Garlic': '🧅',
            'Why Veg?': '🌾',
        }
        
        for t in topics:
            loc_name = t.get_localized_name(lang)
            count = CookingArticle.objects.filter(topic=t).count()
            category_names.append(loc_name)
            icon = icon_map.get(t.name, '🩺' if t.name.startswith('Diet:') else '🥘')
            
            if t.name == 'Ayurvedic Shastra Recipes' or t.name.startswith('Diet:'):
                major_group = 'ayurvedic'
            elif t.name in [
                'Krishna Conscious Principles for Cooking',
                'Why No Onion & Garlic',
                'Why Veg?',
                'Health Care of Devotees',
            ]:
                major_group = 'philosophy'
            else:
                major_group = 'modern'
                
            category_details.append({
                'id': t.id,
                'canonicalName': t.name,
                'name': loc_name,
                'count': count,
                'icon': icon,
                'majorGroup': major_group,
                'isDiet': t.name.startswith('Diet:'),
                'isPhilosophy': major_group == 'philosophy',
            })
            
        return Response({
            'categories': category_names,
            'details': category_details
        })
