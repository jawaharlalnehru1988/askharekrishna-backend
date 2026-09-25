import logging
from django.core.management.base import BaseCommand
from stories.models import Story
from vaishnava_calendar.models import CalendarObservance, CalendarObservanceTranslation

logger = logging.getLogger(__name__)

# Direct, authoritative mapping from CalendarDay.ekadashi_name to Story ID
EKADASHI_NAME_TO_STORY_ID = {
    'sat-tila': 148,        # Sattila Ekadashi
    'bhaimi': 147,          # Jaya Ekadashi
    'vijaya': 146,          # Vijaya Ekadashi
    'amalaki': 144,         # Amalaki Ekadashi
    'papamocani': 143,      # Papamocani Ekadashi
    'kamada': 128,          # Kamada Ekadashi
    'varuthini': 110,       # Varuthini Ekadashi
    'mohini': 142,          # Mohini Ekadashi
    'apara': 114,           # Aparaa Ekadasi
    'padmini': 127,         # Padmini Ekadashi
    'parama': 177,          # Parama Ekadasi
    'pandava nirjala': 140, # Nirjala Ekadashi
    'nirjala': 140,         # Nirjala Ekadashi
    'yogini': 139,          # Yogini Ekadashi
    'sayana': 138,          # Devashayani Ekadashi
    'kamika': 137,          # Kamika Ekadashi
    'pavitraropana': 136,   # Putrada Ekadashi
    'pavitropana': 136,     # Putrada Ekadashi
    'annada': 135,          # Aja Ekadashi
    'parsva': 134,          # Padma Ekadashi (Parsva / Parivartini)
    'indira': 133,          # Indira Ekadashi
    'pasankusa': 131,       # Papankusha Ekadashi
    'rama': 130,            # Rama Ekadashi
    'utthana': 129,         # Prabodhini Ekadashi
    'utpanna': 109,         # The History of How Ekadashi Came to Be
    'moksada': 145,         # Mokshada Ekadashi
}

LANGUAGES = ['en', 'ta', 'hi', 'kn', 'te']


def get_story_for_observance(obs, stories_by_id):
    name = (obs.day.ekadashi_name or '').lower()
    for key, story_id in EKADASHI_NAME_TO_STORY_ID.items():
        if key in name:
            return stories_by_id.get(story_id)

    # Fallback to checking existing translation title if day.ekadashi_name is empty
    en_t = obs.translations.filter(language_code='en').first()
    title = (en_t.title if en_t else '').lower()
    for key, story_id in EKADASHI_NAME_TO_STORY_ID.items():
        if key in title:
            return stories_by_id.get(story_id)

    return None


def get_formatted_title(base_title, is_fasting, lang_code):
    base_clean = base_title.strip()
    if not is_fasting:
        return base_clean

    if lang_code == 'en':
        if not base_clean.lower().startswith('fasting'):
            return f"Fasting for {base_clean}"
        return base_clean
    elif lang_code == 'ta':
        if not base_clean.endswith('விரதம்'):
            return f"{base_clean} விரதம்"
        return base_clean
    elif lang_code == 'hi':
        if not base_clean.endswith('व्रत'):
            return f"{base_clean} व्रत"
        return base_clean
    elif lang_code == 'kn':
        if not base_clean.endswith('ವ್ರತ'):
            return f"{base_clean} ವ್ರತ"
        return base_clean
    elif lang_code == 'te':
        if not base_clean.endswith('వ్రతం'):
            return f"{base_clean} వ్రతం"
        return base_clean
    return base_clean


def populate_all_ekadasi_languages():
    stories_by_id = {s.id: s for s in Story.objects.filter(topic_id=11).prefetch_related('translations')}
    ek_observances = CalendarObservance.objects.filter(category='Ekadashi').select_related('day').order_by('day__event_date')

    stats = {lang: 0 for lang in LANGUAGES}
    images_updated = 0

    for obs in ek_observances:
        story = get_story_for_observance(obs, stories_by_id)
        if not story:
            continue

        is_fasting = (obs.order > 0)

        # Update observance image from story
        if story.imagePath and (not obs.image or 'rituals_for_lord_krishna' in str(obs.image)):
            obs.image = story.imagePath
            obs.save(update_fields=['image'])
            images_updated += 1

        for lang in LANGUAGES:
            trans = story.get_translation(lang)
            if not trans or not trans.article:
                continue

            title = get_formatted_title(trans.subTopic, is_fasting, lang)

            obs_trans, _ = CalendarObservanceTranslation.objects.get_or_create(
                observance=obs,
                language_code=lang,
                defaults={
                    'title': title,
                    'description': trans.article,
                }
            )
            obs_trans.title = title
            obs_trans.description = trans.article
            if trans.audioPath and not obs_trans.audio_file:
                obs_trans.audio_file = trans.audioPath
            obs_trans.save()
            stats[lang] += 1

    return stats, images_updated


class Command(BaseCommand):
    help = 'Populate Ekadasi descriptions and titles in Vaishnava Calendar for all 5 languages (en, ta, hi, kn, te) using stories database.'

    def handle(self, *args, **options):
        stats, images_updated = populate_all_ekadasi_languages()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully updated Ekadasi observances for all languages:\n"
                f" - English: {stats['en']}\n"
                f" - Tamil: {stats['ta']}\n"
                f" - Hindi: {stats['hi']}\n"
                f" - Kannada: {stats['kn']}\n"
                f" - Telugu: {stats['te']}\n"
                f" - Images updated: {images_updated}"
            )
        )
