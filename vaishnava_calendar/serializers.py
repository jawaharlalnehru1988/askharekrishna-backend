from rest_framework import serializers
from .models import CalendarDay, CalendarObservance, CalendarObservanceTranslation


class CalendarObservanceTranslationSerializer(serializers.ModelSerializer):
    audioUrl = serializers.SerializerMethodField()

    class Meta:
        model = CalendarObservanceTranslation
        fields = ['id', 'language_code', 'title', 'description', 'audio_file', 'audioUrl']

    def get_audioUrl(self, obj):
        if obj.audio_file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.audio_file.url)
            return obj.audio_file.url
        return None


class CalendarObservanceSerializer(serializers.ModelSerializer):
    translations = CalendarObservanceTranslationSerializer(many=True, read_only=True)
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    audioUrl = serializers.SerializerMethodField()
    imageUrl = serializers.SerializerMethodField()

    day_id = serializers.IntegerField(source='day.id', read_only=True)
    event_date = serializers.CharField(source='day.event_date', read_only=True)
    day_of_week = serializers.CharField(source='day.day_of_week', read_only=True)
    is_ekadashi = serializers.BooleanField(source='day.is_ekadashi', read_only=True)
    ekadashi_name = serializers.CharField(source='day.ekadashi_name', read_only=True)
    is_fast_day = serializers.BooleanField(source='day.is_fast_day', read_only=True)
    fast_details = serializers.CharField(source='day.fast_details', read_only=True)
    
    break_fast_date = serializers.SerializerMethodField()
    break_fast_day_of_week = serializers.SerializerMethodField()
    break_fast_window = serializers.SerializerMethodField()

    class Meta:
        model = CalendarObservance
        fields = [
            'id',
            'day_id',
            'event_date',
            'day_of_week',
            'is_ekadashi',
            'ekadashi_name',
            'is_fast_day',
            'fast_details',
            'break_fast_date',
            'break_fast_day_of_week',
            'break_fast_window',
            'category',
            'order',
            'image',
            'imageUrl',
            'title',
            'description',
            'audioUrl',
            'translations',
        ]

    def _get_break_fast_info(self, obj):
        day = getattr(obj, 'day', obj)
        if day.is_ekadashi:
            from datetime import timedelta
            next_day = CalendarDay.objects.filter(event_date=day.event_date + timedelta(days=1)).first()
            if next_day and next_day.break_fast_window_display:
                return {
                    'date': str(next_day.event_date),
                    'day_of_week': next_day.day_of_week,
                    'window': next_day.break_fast_window_display
                }
        if day.break_fast_window_display:
            return {
                'date': str(day.event_date),
                'day_of_week': day.day_of_week,
                'window': day.break_fast_window_display
            }
        return None

    def get_break_fast_date(self, obj):
        info = self._get_break_fast_info(obj)
        return info['date'] if info else None

    def get_break_fast_day_of_week(self, obj):
        info = self._get_break_fast_info(obj)
        return info['day_of_week'] if info else None

    def get_break_fast_window(self, obj):
        info = self._get_break_fast_info(obj)
        return info['window'] if info else None

    def _get_requested_lang(self):
        request = self.context.get('request')
        if request:
            query_params = getattr(request, 'query_params', None)
            if query_params is None:
                query_params = getattr(request, 'GET', {})
            lang = query_params.get('language') or query_params.get('lang')
            if lang:
                return lang.strip().lower()
        return 'en'

    def get_title(self, obj):
        trans = obj.get_translation(self._get_requested_lang())
        return trans.title if trans else ''

    def get_description(self, obj):
        trans = obj.get_translation(self._get_requested_lang())
        return trans.description if trans else ''

    def get_audioUrl(self, obj):
        trans = obj.get_translation(self._get_requested_lang())
        if trans and trans.audio_file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(trans.audio_file.url)
            return trans.audio_file.url
        return None

    def get_imageUrl(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class CalendarDaySerializer(serializers.ModelSerializer):
    observances = CalendarObservanceSerializer(many=True, read_only=True)
    break_fast_date = serializers.SerializerMethodField()
    break_fast_day_of_week = serializers.SerializerMethodField()
    break_fast_window = serializers.SerializerMethodField()

    class Meta:
        model = CalendarDay
        fields = [
            'id',
            'event_date',
            'day_of_week',
            'is_ekadashi',
            'ekadashi_name',
            'is_fast_day',
            'fast_details',
            'break_fast_start',
            'break_fast_end',
            'break_fast_date',
            'break_fast_day_of_week',
            'break_fast_window',
            'observances',
            'created_at',
            'updated_at',
        ]

    def _get_break_fast_info(self, obj):
        if obj.is_ekadashi:
            from datetime import timedelta
            next_day = CalendarDay.objects.filter(event_date=obj.event_date + timedelta(days=1)).first()
            if next_day and next_day.break_fast_window_display:
                return {
                    'date': str(next_day.event_date),
                    'day_of_week': next_day.day_of_week,
                    'window': next_day.break_fast_window_display
                }
        if obj.break_fast_window_display:
            return {
                'date': str(obj.event_date),
                'day_of_week': obj.day_of_week,
                'window': obj.break_fast_window_display
            }
        return None

    def get_break_fast_date(self, obj):
        info = self._get_break_fast_info(obj)
        return info['date'] if info else None

    def get_break_fast_day_of_week(self, obj):
        info = self._get_break_fast_info(obj)
        return info['day_of_week'] if info else None

    def get_break_fast_window(self, obj):
        info = self._get_break_fast_info(obj)
        return info['window'] if info else None
