from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CalendarDayViewSet, CalendarObservanceViewSet

router = DefaultRouter()
router.register(r'calendar-days', CalendarDayViewSet, basename='calendar-day')
router.register(r'observances', CalendarObservanceViewSet, basename='calendar-observance')

urlpatterns = [
    path('', include(router.urls)),
]
