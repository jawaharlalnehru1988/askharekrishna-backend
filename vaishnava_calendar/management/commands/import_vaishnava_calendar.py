import json
import os
from datetime import datetime
from django.core.management.base import BaseCommand
from django.utils import timezone
import zoneinfo

from vaishnava_calendar.models import CalendarDay, CalendarObservance, CalendarObservanceTranslation

from vaishnava_calendar.management.commands.populate_ekadasi_stories import populate_stories

DEFAULT_JSON_PATH = '/var/www/askharekrishna-platform/frontends/articlesFrontend/src/app/pooja-vidhis/vaishnava_calendar_2026.json'


class Command(BaseCommand):
    help = 'Import Vaishnava Calendar data from JSON into PostgreSQL database and attach Ekadasi stories'

    def add_arguments(self, parser):
        parser.add_argument(
            '--json_file',
            type=str,
            default=DEFAULT_JSON_PATH,
            help='Path to the Vaishnava calendar JSON file'
        )

    def handle(self, *args, **options):
        json_path = options['json_file']

        if not os.path.exists(json_path):
            self.stderr.write(self.style.ERROR(f"JSON file not found at: {json_path}"))
            return

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        tz = zoneinfo.ZoneInfo("Asia/Kolkata")
        days_imported = 0
        observances_imported = 0

        months = data.get('months', [])
        for month in months:
            for day_data in month.get('days', []):
                date_str = day_data.get('date')
                day_of_week = day_data.get('dayOfWeek', '')
                is_ekadashi = day_data.get('isEkadashi', False)
                ekadashi_name = day_data.get('ekadashiName')
                is_fast_day = day_data.get('isFastDay', False)
                fast_details = day_data.get('fastDetails')

                # Parse break fast window if present
                break_fast_window = day_data.get('breakFastWindow')
                break_fast_start = None
                break_fast_end = None

                if break_fast_window and break_fast_window.get('startTime') and break_fast_window.get('endTime'):
                    try:
                        start_time_str = break_fast_window['startTime']
                        end_time_str = break_fast_window['endTime']

                        dt_start = datetime.strptime(f"{date_str} {start_time_str}", "%Y-%m-%d %H:%M")
                        dt_end = datetime.strptime(f"{date_str} {end_time_str}", "%Y-%m-%d %H:%M")

                        break_fast_start = dt_start.replace(tzinfo=tz)
                        break_fast_end = dt_end.replace(tzinfo=tz)
                    except Exception as e:
                        self.stderr.write(self.style.WARNING(f"Failed to parse breakFastWindow for {date_str}: {e}"))

                # Create or update CalendarDay
                calendar_day, created = CalendarDay.objects.update_or_create(
                    event_date=date_str,
                    defaults={
                        'day_of_week': day_of_week,
                        'is_ekadashi': is_ekadashi,
                        'ekadashi_name': ekadashi_name,
                        'is_fast_day': is_fast_day,
                        'fast_details': fast_details,
                        'break_fast_start': break_fast_start,
                        'break_fast_end': break_fast_end,
                    }
                )
                days_imported += 1

                # Clear old observances for re-import
                calendar_day.observances.all().delete()

                # Add observances
                observances_list = day_data.get('observances', [])
                for idx, obs_data in enumerate(observances_list):
                    title = obs_data.get('title', '')
                    category = obs_data.get('category', 'Observance')

                    obs = CalendarObservance.objects.create(
                        day=calendar_day,
                        category=category,
                        order=idx
                    )
                    CalendarObservanceTranslation.objects.create(
                        observance=obs,
                        language_code='en',
                        title=title,
                    )
                    observances_imported += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully imported {days_imported} calendar days and {observances_imported} observances with English translations."
            )
        )

        en_count, ta_count = populate_stories()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully attached Ekadasi stories to {en_count} English and {ta_count} Tamil observances."
            )
        )

        # Clean up duplicate Ekadashi label observances on break fast days
        from datetime import timedelta
        ek_days = list(CalendarDay.objects.filter(is_ekadashi=True).order_by('event_date'))
        for day in ek_days:
            prev_day = CalendarDay.objects.filter(event_date=day.event_date - timedelta(days=1)).first()
            if prev_day and (prev_day.is_ekadashi or (prev_day.ekadashi_name and day.ekadashi_name and prev_day.ekadashi_name in day.ekadashi_name)):
                obs_to_del = list(day.observances.filter(category='Ekadashi'))
                for o in obs_to_del:
                    o.delete()
                day.is_ekadashi = False
                day.ekadashi_name = None
                day.save()

