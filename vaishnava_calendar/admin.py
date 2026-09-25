import datetime
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from .models import CalendarDay, CalendarObservance, CalendarObservanceTranslation


class UpcomingObservancePeriodFilter(admin.SimpleListFilter):
    title = 'Date Period'
    parameter_name = 'period'

    def lookups(self, request, model_admin):
        return (
            ('upcoming', 'Upcoming (From Today)'),
            ('today', 'Today'),
            ('this_week', 'Next 7 Days'),
            ('this_month', 'This Month'),
            ('past', 'Past Events'),
            ('all', 'All Dates (Full Archive)'),
        )

    def choices(self, changelist):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup or (self.value() is None and lookup == 'upcoming'),
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        today = timezone.localdate()
        val = self.value()

        # If user searches or uses date hierarchy, don't restrict unless explicitly chosen
        if 'q' in request.GET or any(k.startswith('day__event_date') for k in request.GET):
            if val == 'upcoming':
                return queryset.filter(day__event_date__gte=today)
            elif val == 'past':
                return queryset.filter(day__event_date__lt=today)
            return queryset

        if val == 'upcoming' or val is None:
            return queryset.filter(day__event_date__gte=today)
        elif val == 'today':
            return queryset.filter(day__event_date=today)
        elif val == 'this_week':
            return queryset.filter(day__event_date__gte=today, day__event_date__lte=today + datetime.timedelta(days=7))
        elif val == 'this_month':
            return queryset.filter(day__event_date__year=today.year, day__event_date__month=today.month)
        elif val == 'past':
            return queryset.filter(day__event_date__lt=today)
        elif val == 'all':
            return queryset
        return queryset


class UpcomingDayPeriodFilter(admin.SimpleListFilter):
    title = 'Date Period'
    parameter_name = 'period'

    def lookups(self, request, model_admin):
        return (
            ('upcoming', 'Upcoming (From Today)'),
            ('today', 'Today'),
            ('this_week', 'Next 7 Days'),
            ('this_month', 'This Month'),
            ('past', 'Past Days'),
            ('all', 'All Days (Full Archive)'),
        )

    def choices(self, changelist):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup or (self.value() is None and lookup == 'upcoming'),
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        today = timezone.localdate()
        val = self.value()

        if 'q' in request.GET or any(k.startswith('event_date') for k in request.GET):
            if val == 'upcoming':
                return queryset.filter(event_date__gte=today)
            elif val == 'past':
                return queryset.filter(event_date__lt=today)
            return queryset

        if val == 'upcoming' or val is None:
            return queryset.filter(event_date__gte=today)
        elif val == 'today':
            return queryset.filter(event_date=today)
        elif val == 'this_week':
            return queryset.filter(event_date__gte=today, event_date__lte=today + datetime.timedelta(days=7))
        elif val == 'this_month':
            return queryset.filter(event_date__year=today.year, event_date__month=today.month)
        elif val == 'past':
            return queryset.filter(event_date__lt=today)
        elif val == 'all':
            return queryset
        return queryset


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
    list_filter = (UpcomingDayPeriodFilter, 'is_ekadashi', 'is_fast_day')
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
    list_display = ('title_display', 'category', 'day', 'languages_list', 'order', 'has_image')
    list_filter = (UpcomingObservancePeriodFilter, 'category', 'translations__language_code')
    search_fields = ('translations__title', 'translations__description', 'day__event_date')
    date_hierarchy = 'day__event_date'
    ordering = ('day__event_date', 'order')
    inlines = [CalendarObservanceTranslationInline]

    @admin.display(description='Title (English)')
    def title_display(self, obj):
        return obj.title

    @admin.display(description='Languages')
    def languages_list(self, obj):
        langs = [t.language_code.upper() for t in obj.translations.all().order_by('language_code')]
        return ', '.join(langs) if langs else '-'

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
