from rest_framework import serializers
from .models import ImageGallery, ImageGalleryCategory


class ImageGallerySerializer(serializers.ModelSerializer):
    Image = serializers.ImageField(source='image')
    cdnUrl = serializers.URLField(source='cdn_url', read_only=True)

    class Meta:
        model = ImageGallery
        fields = ['id', 'Image', 'cdnUrl', 'category', 'note']


class ImageGalleryCategorySerializer(serializers.ModelSerializer):
    categoryName = serializers.CharField(source='category_name')
    categoryImage = serializers.ImageField(source='category_image')
    categoryDescription = serializers.CharField(source='category_description', allow_blank=True, required=False)
    routerPath = serializers.CharField(source='router_path', allow_blank=True, required=False)
    mappedImageCount = serializers.IntegerField(read_only=True)

    class Meta:
        model = ImageGalleryCategory
        fields = [
            'id',
            'categoryName',
            'categoryImage',
            'categoryDescription',
            'routerPath',
            'mappedImageCount',
        ]
