from django.contrib import admin
from django.utils.html import format_html
from .models import CalendarDay, CalendarObservance, CalendarObservanceTranslation


class CalendarObservanceTranslationInline(admin.StackedInline):
    model = CalendarObservanceTranslation
    extra = 1
    fields = ('language_code', 'title', 'description', 'audio_file')


class CalendarObservanceInline(admin.TabularInline):
    model = CalendarObservance
    extra = 1
    fields = ('order', 'category', 'image')
    ordering = ('order', 'id')


@admin.register(CalendarDay)
class CalendarDayAdmin(admin.ModelAdmin):
    list_display = (
        'event_date',
        'day_of_week',
        'is_ekadashi_badge',
        'ekadashi_name',
        'is_fast_day_badge',
        'break_fast_window_display',
        'observances_count',
    )
    list_filter = ('is_ekadashi', 'is_fast_day', 'event_date')
    search_fields = ('event_date', 'ekadashi_name', 'observances__translations__title', 'fast_details')
    date_hierarchy = 'event_date'
    ordering = ('event_date',)
    inlines = [CalendarObservanceInline]

    fieldsets = (
        ('General Date Information', {
            'fields': ('event_date', 'day_of_week')
        }),
        ('Ekadashi & Fasting Details', {
            'fields': (
                'is_ekadashi',
                'ekadashi_name',
                'is_fast_day',
                'fast_details',
            )
        }),
        ('Parana (Break-Fast Window)', {
            'fields': ('break_fast_start', 'break_fast_end')
        }),
    )

    @admin.display(description='Ekadashi', boolean=True)
    def is_ekadashi_badge(self, obj):
        return obj.is_ekadashi

    @admin.display(description='Fast Day', boolean=True)
    def is_fast_day_badge(self, obj):
        return obj.is_fast_day

    @admin.display(description='Break Fast Window')
    def break_fast_window_display(self, obj):
        if obj.break_fast_start and obj.break_fast_end:
            return f"{obj.break_fast_start.strftime('%H:%M')} - {obj.break_fast_end.strftime('%H:%M')}"
        return "-"

    @admin.display(description='Observances')
    def observances_count(self, obj):
        count = obj.observances.count()
        return f"{count} item(s)"


@admin.register(CalendarObservance)
class CalendarObservanceAdmin(admin.ModelAdmin):
    list_display = ('title_display', 'category', 'day', 'order', 'has_image')
    list_filter = ('category', 'day__event_date')
    search_fields = ('translations__title', 'translations__description', 'day__event_date')
    ordering = ('day__event_date', 'order')
    inlines = [CalendarObservanceTranslationInline]

    @admin.display(description='Title (English)')
    def title_display(self, obj):
        return obj.title

    @admin.display(description='Image', boolean=True)
    def has_image(self, obj):
        return bool(obj.image)


@admin.register(CalendarObservanceTranslation)
class CalendarObservanceTranslationAdmin(admin.ModelAdmin):
    list_display = ('title', 'language_code', 'observance', 'has_audio')
    list_filter = ('language_code', 'observance__category')
    search_fields = ('title', 'description', 'observance__day__event_date')

    @admin.display(description='Audio File', boolean=True)
    def has_audio(self, obj):
        return bool(obj.audio_file)
