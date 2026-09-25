from django.apps import AppConfig


class VaishnavaCalendarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vaishnava_calendar'
    verbose_name = 'Vaishnava Calendar'

    def ready(self):
        import vaishnava_calendar.signals
