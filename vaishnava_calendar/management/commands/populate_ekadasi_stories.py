import logging
from django.core.management.base import BaseCommand
from stories.models import Story
from vaishnava_calendar.models import CalendarObservance, CalendarObservanceTranslation

logger = logging.getLogger(__name__)

EXACT_NAME_MAP = {
    'sat-tila': 'Sattila Ekadashi',
    'bhaimi': 'Jaya Ekadashi',
    'vijaya': 'Vijaya Ekadashi',
    'amalaki': 'Amalaki Ekadashi',
    'papamocani': 'Papamocani Ekadashi',
    'kamada': 'Kamada Ekadashi',
    'varuthini': 'Varuthini Ekadashi',
    'mohini': 'Mohini Ekadashi',
    'apara': 'Aparaa Ekadasi',
    'padmini': 'Padmini Ekadashi',
    'parama': 'Parama Ekadasi',
    'pandava nirjala': 'Nirjala Ekadashi',
    'nirjala': 'Nirjala Ekadashi',
    'yogini': 'Yogini Ekadashi',
    'sayana': 'Devashayani Ekadashi',
    'kamika': 'Kamika Ekadashi',
    'pavitraropana': 'Putrada Ekadashi',
    'annada': 'Aja Ekadashi',
    'parsva': 'Padma Ekadashi',
    'indira': 'Indira Ekadashi',
    'pasankusa': 'Papankusha Ekadashi',
    'rama': 'Rama Ekadashi',
    'utthana': 'Prabodhini Ekadashi',
    'utpanna': 'The History of How Ekadashi Came to Be',
    'moksada': 'Mokshada Ekadashi',
}

TA_NAME_MAP = {
    'sat-tila': 'சத்தில',
    'bhaimi': 'ஜெயா',
    'vijaya': 'விஜயா',
    'amalaki': 'அமலகி',
    'papamocani': 'பாபமோசனி',
    'kamada': 'காமதா',
    'varuthini': 'வருத்தினி',
    'mohini': 'மோஹினி',
    'apara': 'அபரா',
    'padmini': 'பத்மினி',
    'parama': 'பரம',
    'pandava nirjala': 'நிர்ஜல',
    'nirjala': 'நிர்ஜல',
    'yogini': 'யோகினி',
    'sayana': 'தேவஷயனி',
    'kamika': 'காமிகா',
    'pavitraropana': 'புத்ரதா',
    'annada': 'அஜா',
    'parsva': 'பத்ம',
    'indira': 'இந்திர',
    'pasankusa': 'பாபாங்குஷ',
    'rama': 'ரமா',
    'utthana': 'ப்ரபோதினி',
    'utpanna': 'ஏகாதசி உருவான வரலாறு',
    'moksada': 'மோக்ஷதா',
}


def get_story_for_observance(title_or_name, lang_code='en'):
    clean = title_or_name.replace('Fasting for', '').replace('vrata', '').replace('Ekadasi', '').replace('Ekadashi', '').strip().lower()
    
    if lang_code == 'en':
        target_subtopic = None
        for k in sorted(EXACT_NAME_MAP.keys(), key=len, reverse=True):
            if k in clean:
                target_subtopic = EXACT_NAME_MAP[k]
                break
        if not target_subtopic:
            target_subtopic = clean
        return Story.objects.filter(language__code='en', subTopic__iexact=target_subtopic).first() or \
               Story.objects.filter(language__code='en', subTopic__icontains=target_subtopic).first()
    elif lang_code == 'ta':
        target_ta = None
        for k in sorted(TA_NAME_MAP.keys(), key=len, reverse=True):
            if k in clean:
                target_ta = TA_NAME_MAP[k]
                break
        if target_ta:
            story = Story.objects.filter(language__code='ta', subTopic__icontains=target_ta).first()
            if story:
                return story
        # Fallback to translation of en story
        en_story = get_story_for_observance(title_or_name, 'en')
        if en_story:
            return en_story.translations.filter(language__code='ta').first() or \
                   (en_story.source_story if en_story.source_story and en_story.source_story.language.code == 'ta' else None)
    return None


def populate_stories():
    updated_en_count = 0
    updated_ta_count = 0

    ek_observances = CalendarObservance.objects.filter(category='Ekadashi')

    for obs in ek_observances:
        en_trans = obs.translations.filter(language_code='en').first()
        title = en_trans.title if en_trans else obs.day.ekadashi_name or ''

        if title.startswith('Ksaya'):
            continue

        # English story
        en_story = get_story_for_observance(title, 'en')
        if en_story:
            if not en_trans:
                en_trans = CalendarObservanceTranslation.objects.create(
                    observance=obs,
                    language_code='en',
                    title=title,
                    description=en_story.article
                )
            else:
                en_trans.description = en_story.article
                en_trans.save()
            updated_en_count += 1

            # Attach story image to observance if missing
            eff_image = en_story.effective_image_path()
            if eff_image and not obs.image:
                obs.image = eff_image
                obs.save()

        # Tamil story
        ta_story = get_story_for_observance(title, 'ta')
        if ta_story:
            ta_trans, created = CalendarObservanceTranslation.objects.get_or_create(
                observance=obs,
                language_code='ta',
                defaults={
                    'title': ta_story.subTopic,
                    'description': ta_story.article,
                }
            )
            if not created:
                ta_trans.description = ta_story.article
                if not ta_trans.title or ta_trans.title == title:
                    ta_trans.title = ta_story.subTopic
                ta_trans.save()
            updated_ta_count += 1

    return updated_en_count, updated_ta_count


class Command(BaseCommand):
    help = 'Populate Ekadasi descriptions in Vaishnava Calendar observances using stories database.'

    def handle(self, *args, **options):
        en_count, ta_count = populate_stories()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully updated Ekadasi story descriptions for {en_count} English and {ta_count} Tamil observances."
            )
        )
