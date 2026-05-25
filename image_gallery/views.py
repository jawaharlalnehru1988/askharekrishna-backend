from django.db.models import Count
from rest_framework import viewsets
from rest_framework.response import Response
from askharekrishna_backend.permissions import IsAdminOrReadOnly
from .models import ImageGallery, ImageGalleryCategory
from .serializers import ImageGallerySerializer, ImageGalleryCategorySerializer


class ImageGalleryViewSet(viewsets.ModelViewSet):
    queryset = ImageGallery.objects.all()
    serializer_class = ImageGallerySerializer
    permission_classes = [IsAdminOrReadOnly]


class ImageGalleryCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ImageGalleryCategorySerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = ImageGalleryCategory.objects.all().order_by('category_name')

        if self.action == 'list':
            mapped_only = str(self.request.query_params.get('mappedOnly', '')).lower() in ('true', '1', 'yes')
            if mapped_only:
                mapped_category_names = ImageGallery.objects.exclude(category='').values_list('category', flat=True).distinct()
                queryset = queryset.filter(category_name__in=mapped_category_names)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        mapped_counts = {
            row['category']: row['count']
            for row in ImageGallery.objects.exclude(category='').values('category').order_by().annotate(count=Count('id'))
        }

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = serializer.data
            for item in data:
                item['mappedImageCount'] = mapped_counts.get(item.get('categoryName'), 0)
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        for item in data:
            item['mappedImageCount'] = mapped_counts.get(item.get('categoryName'), 0)
        return Response(data)
