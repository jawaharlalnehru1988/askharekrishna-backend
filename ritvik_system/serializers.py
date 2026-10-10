from rest_framework import serializers
from .models import (
    RitvikSection,
    RitvikSectionTranslation,
    RitvikQA,
    RitvikQATranslation,
)


class RitvikSectionTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RitvikSectionTranslation
        fields = ['language', 'title', 'description']


class RitvikQATranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RitvikQATranslation
        fields = ['language', 'question', 'summary', 'answer', 'audioPath']


class RitvikSectionSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    questionsCount = serializers.SerializerMethodField()
    translations = RitvikSectionTranslationSerializer(many=True, read_only=True)

    class Meta:
        model = RitvikSection
        fields = [
            'id',
            'section_number',
            'slug',
            'order',
            'image',
            'title',
            'description',
            'questionsCount',
            'translations',
        ]

    def _get_translation(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('language', 'en') if request else 'en'
        return obj.translations.filter(language=lang).first() or obj.translations.filter(language='en').first() or obj.translations.first()

    def get_title(self, obj):
        t = self._get_translation(obj)
        return t.title if t else f"Section {obj.section_number}"

    def get_description(self, obj):
        t = self._get_translation(obj)
        return t.description if t else ""

    def get_questionsCount(self, obj):
        return obj.questions.filter(is_published=True).count()


class RitvikQAListSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    summary = serializers.SerializerMethodField()
    section_number = serializers.IntegerField(source='section.section_number', read_only=True)
    section_title = serializers.SerializerMethodField()

    class Meta:
        model = RitvikQA
        fields = [
            'id',
            'question_code',
            'slug',
            'order',
            'image',
            'section_number',
            'section_title',
            'question',
            'summary',
        ]

    def _get_translation(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('language', 'en') if request else 'en'
        return obj.translations.filter(language=lang).first() or obj.translations.filter(language='en').first() or obj.translations.first()

    def get_question(self, obj):
        t = self._get_translation(obj)
        return t.question if t else ""

    def get_summary(self, obj):
        t = self._get_translation(obj)
        return t.summary if t else ""

    def get_section_title(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('language', 'en') if request else 'en'
        st = obj.section.translations.filter(language=lang).first() or obj.section.translations.first()
        return st.title if st else f"Section {obj.section.section_number}"


class RitvikQADetailSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()
    summary = serializers.SerializerMethodField()
    audioPath = serializers.SerializerMethodField()
    section = RitvikSectionSerializer(read_only=True)
    translations = RitvikQATranslationSerializer(many=True, read_only=True)

    class Meta:
        model = RitvikQA
        fields = [
            'id',
            'question_code',
            'slug',
            'order',
            'image',
            'is_published',
            'section',
            'question',
            'answer',
            'summary',
            'audioPath',
            'translations',
            'created_at',
            'updated_at',
        ]

    def _get_translation(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('language', 'en') if request else 'en'
        return obj.translations.filter(language=lang).first() or obj.translations.filter(language='en').first() or obj.translations.first()

    def get_question(self, obj):
        t = self._get_translation(obj)
        return t.question if t else ""

    def get_answer(self, obj):
        t = self._get_translation(obj)
        return t.answer if t else ""

    def get_summary(self, obj):
        t = self._get_translation(obj)
        return t.summary if t else ""

    def get_audioPath(self, obj):
        t = self._get_translation(obj)
        if t and t.audioPath:
            request = self.context.get('request')
            return request.build_absolute_uri(t.audioPath.url) if request else t.audioPath.url
        return None
