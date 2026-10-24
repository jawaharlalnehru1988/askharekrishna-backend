import calendar
import datetime
import logging
import re
import zoneinfo
import gaurabda as gcal

from django.db import transaction
from django.utils import timezone
from vaishnava_calendar.models import (
    CalendarDay,
    CalendarObservance,
    CalendarObservanceTranslation,
)

logger = logging.getLogger(__name__)

# Default location matching Vrindavan, India
DEFAULT_LOCATION = {
    'latitude': 27.583,
    'longitude': 77.73,
    'tzname': '+5:30 Asia/Calcutta',
    'name': 'Vrindavan, India',
}

FESTIVAL_KEYWORDS = [
    'Puja', 'Utsava', 'Yatra', 'Abhiseka', 'Pancami', 'Purnima', 'Amavasya',
    'Sankranti', 'Navami', 'Janmastami', 'Rasa', 'Holi', 'Divali', 'Dipavali',
    'Jhulan', 'Govardhana', 'Gaura Purnima', 'Rama Navami', 'Radhastami',
    'Kunda', 'Snana', 'Ratha', 'Gundica', 'Cida Dahi', 'Damanaka', 'Candana',
]


def classify_category(title: str) -> str:
    clean = title.strip()
    if clean.startswith('Break fast'):
        return 'Parana'
    if 'Appearance' in clean or 'Disappearance' in clean:
        return 'Appearance'
    if 'Ekadasi' in clean or 'Ekadashi' in clean:
        return 'Ekadashi'
    if clean.startswith('(Fast') or clean.startswith('(Fasting'):
        return 'Fasting'
    if any(kw.lower() in clean.lower() for kw in FESTIVAL_KEYWORDS):
        return 'Festival'
    return 'Observance'


def attach_stories_and_translations():
    """
    Invokes all existing story population commands so that newly generated days
    are enriched with multi-language titles, descriptions, and story images.
    """
    summary = {}
    try:
        from vaishnava_calendar.management.commands.populate_ekadasi_stories import (
            populate_all_ekadasi_languages,
        )
        stats, img_count = populate_all_ekadasi_languages()
        summary['ekadasi'] = {'stats': stats, 'images': img_count}
    except Exception as e:
        logger.error(f"Error populating ekadasi stories: {e}")

    try:
        from vaishnava_calendar.management.commands.populate_festival_stories import (
            populate_festival_descriptions,
        )
        summary['festivals'] = populate_festival_descriptions()
    except Exception as e:
        logger.error(f"Error populating festival stories: {e}")

    try:
        from vaishnava_calendar.management.commands.populate_acharya_stories import (
            populate_acharya_descriptions,
        )
        summary['acharyas'] = populate_acharya_descriptions()
    except Exception as e:
        logger.error(f"Error populating acharya stories: {e}")

    try:
        from vaishnava_calendar.management.commands.populate_acharyas_stories import (
            populate_acharyas_descriptions,
        )
        summary['acharyas_more'] = populate_acharyas_descriptions()
    except Exception as e:
        logger.error(f"Error populating additional acharyas stories: {e}")

    try:
        from vaishnava_calendar.management.commands.populate_avatar_stories import (
            populate_avatar_descriptions,
        )
        summary['avatars'] = populate_avatar_descriptions()
    except Exception as e:
        logger.error(f"Error populating avatar stories: {e}")

    try:
        from vaishnava_calendar.management.commands.populate_gosvami_stories import (
            populate_gosvami_descriptions,
        )
        summary['gosvamis'] = populate_gosvami_descriptions()
    except Exception as e:
        logger.error(f"Error populating gosvami stories: {e}")

    try:
        from vaishnava_calendar.management.commands.populate_panchatattva_stories import (
            populate_panchatattva_descriptions,
        )
        summary['panchatattva'] = populate_panchatattva_descriptions()
    except Exception as e:
        logger.error(f"Error populating panchatattva stories: {e}")

    try:
        from vaishnava_calendar.management.commands.populate_navadvipa_parsadas_stories import (
            populate_navadvipa_parsadas_descriptions,
        )
        summary['navadvipa_parsadas'] = populate_navadvipa_parsadas_descriptions()
    except Exception as e:
        logger.error(f"Error populating navadvipa parsadas stories: {e}")

    try:
        from vaishnava_calendar.management.commands.populate_ramacandra_vijayotsava import (
            populate_ramacandra_vijayotsava_stories,
        )
        summary['ramacandra_vijayotsava'] = populate_ramacandra_vijayotsava_stories()
    except Exception as e:
        logger.error(f"Error populating ramacandra vijayotsava stories: {e}")

    return summary



def generate_calendar_for_year(year: int, location_data=None, force: bool = False):
    """
    Calculates the complete Vaishnava calendar for the given year using the GCal engine.
    Stores CalendarDay and CalendarObservance records in PostgreSQL and links all stories.
    """
    year = int(year)
    existing_count = CalendarDay.objects.filter(event_date__year=year).count()
    if not force and existing_count >= 365:
        logger.info(f"Vaishnava Calendar for {year} already exists ({existing_count} days).")
        return {
            'year': year,
            'days_count': existing_count,
            'observances_count': 0,
            'status': 'already_exists',
        }

    logger.info(f"Calculating Vaishnava Calendar for year {year} using GCal...")
    total_days = 366 if calendar.isleap(year) else 365
    loc = gcal.GCLocation(data=location_data or DEFAULT_LOCATION)
    start_date = gcal.GCGregorianDate(text=f'1 jan {year}')
    cal = gcal.TCalendar()
    cal.CalculateCalendar(loc, start_date, total_days)
    calendar_data = cal.get_json_object()

    tz = zoneinfo.ZoneInfo("Asia/Kolkata")
    days_imported = 0
    observances_imported = 0

    with transaction.atomic():
        for day_obj in calendar_data.get('days', []):
            d_info = day_obj.get('date', {})
            y, m, d = d_info['year'], d_info['month'], d_info['day']
            event_date = datetime.date(y, m, d)
            date_str = event_date.strftime('%Y-%m-%d')
            day_of_week = event_date.strftime('%A')

            events = day_obj.get('events', [])
            raw_ek_name = day_obj.get('ekadashiName') or ''
            raw_fast = day_obj.get('fast', 0)

            is_ekadashi = False
            ekadashi_name = None
            is_fast_day = False
            fast_details = None
            break_fast_start = None
            break_fast_end = None

            # Check if this day is marked as Ekadashi
            if raw_ek_name and raw_fast != 0:
                is_ekadashi = True
                ekadashi_name = raw_ek_name

            # Check events for fasting, Ekadashi, and Parana
            for ev in events:
                text = ev.get('text', '').strip()
                if not is_ekadashi and ('Fasting for ' in text and 'Ekadasi' in text):
                    is_ekadashi = True
                    ekadashi_name = text.replace('Fasting for ', '').strip()

                if text.startswith('(Fast') or text.startswith('(Fasting'):
                    fast_details = text
                    is_fast_day = True

                if text.startswith('Break fast'):
                    match = re.search(r'Break fast\s+(\d{2}:\d{2})\s*-\s*(\d{2}:\d{2})', text)
                    if match:
                        start_time_str, end_time_str = match.group(1), match.group(2)
                        try:
                            dt_start = datetime.datetime.strptime(f"{date_str} {start_time_str}", "%Y-%m-%d %H:%M").replace(tzinfo=tz)
                            dt_end = datetime.datetime.strptime(f"{date_str} {end_time_str}", "%Y-%m-%d %H:%M").replace(tzinfo=tz)
                            break_fast_start = dt_start
                            break_fast_end = dt_end
                            is_fast_day = True
                        except Exception as e:
                            logger.warning(f"Error parsing break-fast time for {date_str}: {e}")

            if is_ekadashi:
                is_fast_day = True

            # Create or update CalendarDay
            calendar_day, _ = CalendarDay.objects.update_or_create(
                event_date=event_date,
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

            # Rebuild observances for the day
            calendar_day.observances.all().delete()

            order_idx = 0
            # If Ekadashi, add primary Ekadashi title at order 0 if not present
            if is_ekadashi and ekadashi_name:
                obs = CalendarObservance.objects.create(
                    day=calendar_day,
                    category='Ekadashi',
                    order=order_idx,
                )
                CalendarObservanceTranslation.objects.create(
                    observance=obs,
                    language_code='en',
                    title=ekadashi_name,
                )
                order_idx += 1
                observances_imported += 1

            for ev in events:
                text = ev.get('text', '').strip()
                if 'durga puja' in text.lower():
                    continue

                category = classify_category(text)

                # Skip duplicate Ekadashi fasting event because primary Ekadashi is already created at order 0
                if is_ekadashi and ('fasting for' in text.lower() or text.lower().startswith('fasting')):
                    continue

                obs_image = None
                if category == 'Parana' or text.startswith('Break fast'):
                    obs_image = 'vaishnava_calendar/images/parana_break_fast.jpg'

                obs = CalendarObservance.objects.create(
                    day=calendar_day,
                    category=category,
                    image=obs_image,
                    order=order_idx,
                )
                CalendarObservanceTranslation.objects.create(
                    observance=obs,
                    language_code='en',
                    title=text,
                )
                order_idx += 1
                observances_imported += 1

        # Post-cleanup: Fix consecutive duplicate Ekadashi flags on break-fast days
        ek_days = list(CalendarDay.objects.filter(event_date__year=year, is_ekadashi=True).order_by('event_date'))
        for day in ek_days:
            prev_day = CalendarDay.objects.filter(event_date=day.event_date - datetime.timedelta(days=1)).first()
            if prev_day and (prev_day.is_ekadashi or (prev_day.ekadashi_name and day.ekadashi_name and prev_day.ekadashi_name in day.ekadashi_name)):
                obs_to_del = list(day.observances.filter(category='Ekadashi'))
                for o in obs_to_del:
                    o.delete()
                day.is_ekadashi = False
                day.ekadashi_name = None
                day.save()

    # Enrich observances with multilingual translations and stories
    story_summary = attach_stories_and_translations()

    return {
        'year': year,
        'days_count': days_imported,
        'observances_count': observances_imported,
        'story_summary': story_summary,
        'status': 'generated',
    }
