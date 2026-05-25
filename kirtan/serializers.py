from rest_framework import serializers
from .models import Kirtan, KirtanCategory, KirtanTranslation, KirtanCategoryTranslation


class KirtanCategoryTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = KirtanCategoryTranslation
        fields = [
            'language_code',
            'name',
        ]


class KirtanCategorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    translations = KirtanCategoryTranslationSerializer(many=True, read_only=True)

    def get_name(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang') if request else None

        if lang:
            trans = obj.translations.filter(language_code=lang).first()
            if trans:
                return trans.name

        trans = obj.translations.filter(language_code='en').first()
        if trans:
            return trans.name

        trans = obj.translations.first()
        if trans:
            return trans.name

        return obj.name

    class Meta:
        model = KirtanCategory
        fields = [
            'id',
            'name',
            'translations',
            'categoryImage',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class KirtanTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = KirtanTranslation
        fields = [
            'id',
            'language_code',
            'title',
            'authorName',
            'description',
            'lyrics'
        ]


class KirtanSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    categoryId = serializers.PrimaryKeyRelatedField(
        source='category',
        queryset=KirtanCategory.objects.all(),
        write_only=True,
        allow_null=True,
        required=False,
    )
    translations = KirtanTranslationSerializer(many=True, read_only=True)

    def get_category(self, obj):
        return obj.category.name if obj.category else ''

    class Meta:
        model = Kirtan
        fields = [
            'id',
            'category',
            'categoryId',
            'audioPath',
            'imagePath',
            'videoPath',
            'order',
            'translations',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'translations']
