from datetime import date
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CalendarDay, CalendarObservance
from .serializers import CalendarDaySerializer, CalendarObservanceSerializer


class CalendarDayViewSet(viewsets.ModelViewSet):
    queryset = CalendarDay.objects.prefetch_related('observances').all().order_by('event_date')
    serializer_class = CalendarDaySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_ekadashi', 'is_fast_day', 'event_date']
    search_fields = ['ekadashi_name', 'observances__title', 'fast_details']
    ordering_fields = ['event_date', 'id']
    ordering = ['event_date']

    def get_queryset(self):
        qs = super().get_queryset()
        params = self.request.query_params

        # Filter by start_date and end_date
        start_date = params.get('start_date')
        end_date = params.get('end_date')
        if start_date:
            qs = qs.filter(event_date__gte=start_date)
        if end_date:
            qs = qs.filter(event_date__lte=end_date)

        # Filter by year and month
        year = params.get('year')
        month = params.get('month')
        if year:
            qs = qs.filter(event_date__year=year)
        if month:
            qs = qs.filter(event_date__month=month)

        return qs

    @action(detail=False, methods=['get'], url_path='upcoming')
    def upcoming(self, request):
        """
        Returns upcoming calendar days from today onwards.
        Query param 'limit' can specify max records (default 10).
        """
        today = date.today()
        limit = int(request.query_params.get('limit', 10))
        queryset = self.get_queryset().filter(event_date__gte=today)[:limit]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CalendarObservanceViewSet(viewsets.ModelViewSet):
    queryset = CalendarObservance.objects.select_related('day').prefetch_related('translations').all().order_by('day__event_date', 'order')
    serializer_class = CalendarObservanceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['day', 'category', 'day__is_ekadashi', 'day__is_fast_day', 'day__event_date']
    search_fields = ['translations__title', 'translations__description']

