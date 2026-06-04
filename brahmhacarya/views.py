from django.db import transaction
from rest_framework import viewsets, filters, generics, status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from askharekrishna_backend.permissions import IsAdminOrReadOnly
from .models import BrahmhacaryaArticle, BrahmhacaryaRegistration
from .serializers import BrahmhacaryaArticleSerializer, BrahmhacaryaRegistrationSerializer


class BrahmhacaryaArticleViewSet(viewsets.ModelViewSet):
    queryset = BrahmhacaryaArticle.objects.prefetch_related('questions__options').all()
    serializer_class = BrahmhacaryaArticleSerializer
    lookup_field = 'slug'
    lookup_value_regex = r'(?!bulk$)[^/.]+'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['language', 'category', 'is_published']
    search_fields = ['title', 'language', 'category', 'excerpt', 'content']
    ordering_fields = ['order', 'created_at', 'updated_at', 'published_at', 'title']
    ordering = ['order', '-published_at', '-created_at']


class BrahmhacaryaRegistrationCreateAPIView(generics.CreateAPIView):
    queryset = BrahmhacaryaRegistration.objects.all()
    serializer_class = BrahmhacaryaRegistrationSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminOrReadOnly]


class BrahmhacaryaBulkAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def post(self, request):
        if not isinstance(request.data, list):
            return Response(
                {'detail': 'Expected a list of article objects.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = BrahmhacaryaArticleSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            articles = serializer.save()

        response_serializer = BrahmhacaryaArticleSerializer(articles, many=True)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        if not isinstance(request.data, list):
            return Response(
                {'detail': 'Expected a list of article objects.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        updated_articles = []

        with transaction.atomic():
            for item in request.data:
                slug = item.get('slug')
                if not slug:
                    return Response(
                        {'detail': 'Each bulk update item must include slug.'},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                try:
                    article = BrahmhacaryaArticle.objects.prefetch_related('questions__options').get(slug=slug)
                except BrahmhacaryaArticle.DoesNotExist:
                    return Response(
                        {'detail': f'Article not found for slug: {slug}'},
                        status=status.HTTP_404_NOT_FOUND,
                    )

                serializer = BrahmhacaryaArticleSerializer(article, data=item, partial=True)
                serializer.is_valid(raise_exception=True)
                updated_articles.append(serializer.save())

        response_serializer = BrahmhacaryaArticleSerializer(updated_articles, many=True)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
