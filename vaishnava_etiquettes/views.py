from django.db.models import Prefetch, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, pagination, viewsets
from rest_framework.response import Response

from .models import (
    VaishnavaEtiquetteArticle,
    VaishnavaEtiquetteTranslation,
    EtiquetteCategory,
    EtiquetteCategoryTranslation,
)
from .serializers import (
    VaishnavaEtiquetteArticleSerializer,
    VaishnavaEtiquetteArticleListItemSerializer,
    EtiquetteCategoryArticleListSerializer,
)


class VaishnavaEtiquettePagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100


class VaishnavaEtiquetteViewSet(viewsets.ModelViewSet):
    queryset = VaishnavaEtiquetteArticle.objects.prefetch_related('translations__category', 'questions__options').all().order_by('order', 'id')
    serializer_class = VaishnavaEtiquetteArticleSerializer
    pagination_class = VaishnavaEtiquettePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'id': ['exact'],
        'translations__category': ['exact'],
        'translations__category__name': ['exact', 'icontains'],
        'translations__subTopic': ['exact', 'icontains'],
        'slug': ['exact'],
        'translations__language': ['exact'],
    }
    search_fields = ['translations__category__name', 'translations__subTopic', 'translations__article']
    ordering_fields = ['id', 'order', 'created_at']
    ordering = ['order', 'id']

    def list(self, request, *args, **kwargs):
        if request.query_params.get('format') == 'flat':
            return super().list(request, *args, **kwargs)

        req_lang = request.query_params.get('language', request.query_params.get('lang', 'en'))
        slug = request.query_params.get('slug')

        # If slug is numeric, treat it as ID in query parameters
        if slug and slug.isdigit():
            request.GET._mutable = True
            request.GET.pop('slug', None)
            request.GET['id'] = slug
            request.GET._mutable = False
            slug = None

        # Build translation prefetch
        # Try requested language first; if missing in DB, include 'en' as fallback
        art_trans_qs = (
            VaishnavaEtiquetteTranslation.objects.filter(
                Q(language=req_lang) | Q(language='en')
            )
            .exclude(article__isnull=True)
            .exclude(article__exact="")
            .select_related('category')
        )

        queryset = self.filter_queryset(self.get_queryset()).prefetch_related(
            Prefetch('translations', queryset=art_trans_qs, to_attr='cached_trans')
        )

        grouped_articles = {}
        uncategorized = []

        for article in queryset:
            translations = getattr(article, 'cached_trans', [])
            # Prefer matching req_lang, then fallback to 'en', then first
            t = next((tr for tr in translations if tr.language == req_lang), None)
            if not t:
                t = next((tr for tr in translations if tr.language == 'en'), None)
            if not t and translations:
                t = translations[0]

            if not t or not (t.article and t.article.strip()):
                continue

            article.cached_trans = [t]  # Pin the matched translation for serializer

            if t.category_id is None:
                uncategorized.append(article)
                continue
            grouped_articles.setdefault(t.category_id, []).append(article)

        cat_trans_qs = EtiquetteCategoryTranslation.objects.filter(language=req_lang)
        categories = list(
            EtiquetteCategory.objects.filter(id__in=grouped_articles.keys())
            .prefetch_related(Prefetch('translations', queryset=cat_trans_qs, to_attr='cached_cat_trans'))
            .order_by('order', 'name')
        )
        cat_names = {}
        for c in categories:
            trans = c.cached_cat_trans[0] if (hasattr(c, 'cached_cat_trans') and c.cached_cat_trans) else None
            cat_names[c.id] = (trans.translated_name if (trans and trans.translated_name) else c.name)

        category_data = EtiquetteCategoryArticleListSerializer(
            categories,
            many=True,
            context={
                'request': request,
                'grouped_articles': grouped_articles,
                'category_names': cat_names,
            },
        ).data

        if uncategorized:
            uncategorized_data = VaishnavaEtiquetteArticleListItemSerializer(
                uncategorized,
                many=True,
                context={
                    'request': request,
                    'category_names': cat_names,
                },
            ).data
            category_data.append({
                'id': 0,
                'name': 'Other Etiquettes',
                'description': 'Miscellaneous articles',
                'image': None,
                'articleList': uncategorized_data,
            })

        return Response(category_data)
