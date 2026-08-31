import json

from rest_framework import serializers
from .models import (
    Category,
    CarnaticKacheri,
    CarnaticLessonPractice,
    CarnaticLessonPracticeAudio,
    CarnaticLessonPracticeVideo,
    CarnaticSyllabus,
    CarnaticSyllabusVideoSample,
    RagamLesson,
    RagamLessonAudio,
    RagamLessonVideo,
    MridangaLesson,
    MridangaLessonAudio,
    MridangaLessonVideo,
    MridangaLessonKirtanDemo,
)


class CarnaticLessonPracticeAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarnaticLessonPracticeAudio
        fields = ['id', 'audioPathName', 'audioPath', 'sort_order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class CarnaticLessonPracticeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarnaticLessonPracticeVideo
        fields = ['id', 'youtubevideoUrl', 'sort_order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class CarnaticLessonPracticeSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField(read_only=True)
    category_colorCode = serializers.SerializerMethodField(read_only=True)
    PracticeCategory = serializers.SerializerMethodField(read_only=True)
    audios = CarnaticLessonPracticeAudioSerializer(many=True, read_only=True)
    videos = CarnaticLessonPracticeVideoSerializer(many=True, read_only=True)
    audioPath = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CarnaticLessonPractice
        fields = [
            'id',
            'orderNumber',
            'category',
            'category_name',
            'category_colorCode',
            'PracticeCategory',
            'lessonName',
            'swarams',
            'audioPath',
            'audios',
            'videos',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'category': {'required': False, 'allow_null': True}
        }

    def get_PracticeCategory(self, obj):
        return obj.category.name if obj.category else ""

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None

    def get_category_colorCode(self, obj):
        return obj.category.colorCode if obj.category else None

    def get_audioPath(self, obj):
        first_audio = obj.audios.order_by('sort_order', 'id').first()
        if first_audio and first_audio.audioPath:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(first_audio.audioPath.url)
            return first_audio.audioPath.url
        if obj.audioPath:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.audioPath.url)
            return obj.audioPath.url
        return None



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'order', 'name', 'colorCode', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class CarnaticKacheriSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarnaticKacheri
        fields = ['id', 'title', 'singer', 'ragam', 'videoUrl', 'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class CarnaticSyllabusVideoSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarnaticSyllabusVideoSample
        fields = ['id', 'url', 'sort_order']
        read_only_fields = ['id']


class CarnaticSyllabusSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField(read_only=True)
    category_order = serializers.SerializerMethodField(read_only=True)
    category_colorCode = serializers.SerializerMethodField(read_only=True)
    videoPath = serializers.SerializerMethodField(read_only=True)
    videoSamples = CarnaticSyllabusVideoSampleSerializer(many=True, required=False, source='video_samples')

    class Meta:
        model = CarnaticSyllabus
        fields = [
            'id',
            'category',
            'category_name',
            'category_order',
            'category_colorCode',
            'topic',
            'lesson',
            'audioPath',
            'videoPath',
            'videoSamples',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'category': {'required': False, 'allow_null': True},
            'audioPath': {'required': False, 'allow_null': True},
        }

    def get_videoPath(self, obj):
        first_sample = obj.video_samples.order_by('sort_order', 'id').first()
        return first_sample.url if first_sample else None

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None

    def get_category_order(self, obj):
        return obj.category.order if obj.category else None

    def get_category_colorCode(self, obj):
        return obj.category.colorCode if obj.category else None

    def _extract_video_samples(self):
        request = self.context.get('request')
        initial_video_path = self.initial_data.get('videoPath')
        video_samples = self.initial_data.get('videoSamples')

        if video_samples is None and request is not None:
            video_samples = request.data.get('videoSamples')

        if isinstance(video_samples, str):
            try:
                video_samples = json.loads(video_samples)
            except json.JSONDecodeError:
                video_samples = None

        normalized_samples = []
        if isinstance(video_samples, list):
            for sample in video_samples:
                if isinstance(sample, dict):
                    url = (sample.get('url') or '').strip()
                    sort_order = sample.get('sort_order', sample.get('sortOrder'))
                else:
                    url = str(sample).strip()
                    sort_order = None
                if url:
                    normalized_samples.append({'url': url, 'sort_order': sort_order})

        if initial_video_path and not normalized_samples:
            normalized_samples.append({'url': str(initial_video_path).strip(), 'sort_order': 0})

        for index, sample in enumerate(normalized_samples):
            sample['sort_order'] = index if sample['sort_order'] in (None, '') else int(sample['sort_order'])

        return normalized_samples

    def _normalize_validated_video_samples(self, video_samples):
        if video_samples is None:
            return None

        normalized_samples = []
        for index, sample in enumerate(video_samples):
            url = (sample.get('url') or '').strip()
            if not url:
                continue

            sort_order = sample.get('sort_order', index)
            normalized_samples.append({'url': url, 'sort_order': int(sort_order)})

        return normalized_samples

    def _save_video_samples(self, syllabus, video_samples):
        if video_samples is None:
            return

        syllabus.video_samples.all().delete()
        for sample in video_samples:
            CarnaticSyllabusVideoSample.objects.create(
                syllabus=syllabus,
                url=sample['url'],
                sort_order=sample['sort_order'],
            )

    def create(self, validated_data):
        video_samples = validated_data.pop('video_samples', None)
        syllabus = super().create(validated_data)
        extracted_samples = self._normalize_validated_video_samples(video_samples)
        if extracted_samples is None:
            extracted_samples = self._extract_video_samples()
        self._save_video_samples(syllabus, extracted_samples)
        return syllabus

    def update(self, instance, validated_data):
        video_samples = validated_data.pop('video_samples', None)
        syllabus = super().update(instance, validated_data)

        extracted_samples = self._normalize_validated_video_samples(video_samples)
        if 'videoSamples' in self.initial_data or 'videoPath' in self.initial_data:
            extracted_samples = self._extract_video_samples()

        self._save_video_samples(syllabus, extracted_samples)
        return syllabus


class RagamLessonAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RagamLessonAudio
        fields = ['id', 'songName', 'audioPath', 'sort_order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class RagamLessonVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RagamLessonVideo
        fields = ['id', 'title', 'youtubevideoUrl', 'sort_order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class RagamLessonSerializer(serializers.ModelSerializer):
    audios = RagamLessonAudioSerializer(many=True, read_only=True)
    videos = RagamLessonVideoSerializer(many=True, read_only=True)

    class Meta:
        model = RagamLesson
        fields = [
            'id',
            'raga_name',
            'swarasthanas',
            'arohanam_avarohanam',
            'description',
            'famousCompositions',
            'melakarthaNumber',
            'audios',
            'videos',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class MridangaLessonAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MridangaLessonAudio
        fields = ['id', 'songName', 'audioPath', 'mantras_and_notes', 'sort_order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class MridangaLessonVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MridangaLessonVideo
        fields = ['id', 'title', 'youtubevideoUrl', 'mantras_and_notes', 'sort_order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class MridangaLessonKirtanDemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MridangaLessonKirtanDemo
        fields = ['id', 'title', 'youtubevideoUrl', 'mantras_and_notes', 'sort_order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class MridangaLessonSerializer(serializers.ModelSerializer):
    audios = MridangaLessonAudioSerializer(many=True, read_only=True)
    videos = MridangaLessonVideoSerializer(many=True, read_only=True)
    kirtan_demos = MridangaLessonKirtanDemoSerializer(many=True, read_only=True)

    class Meta:
        model = MridangaLesson
        fields = [
            'id',
            'tala_name',
            'tala_category',
            'level',
            'matras',
            'mantras_and_notes',
            'description',
            'sort_order',
            'audios',
            'videos',
            'kirtan_demos',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


