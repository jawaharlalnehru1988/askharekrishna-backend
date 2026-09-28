import logging
import re
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.text import slugify

from stories.models import Story, StoryMainTopic, StoryTranslation
from vaishnava_calendar.models import CalendarObservance, CalendarObservanceTranslation

logger = logging.getLogger(__name__)


def clean_name_by_language(raw_title: str, lang_code: str) -> str:
    """Extract clean Acharya / Devotee name from calendar observance title."""
    t = raw_title.strip()

    if lang_code == 'en':
        if ': Appearance of ' in t:
            t = t.split(': Appearance of ')[-1].strip()
        t = re.sub(r'\s*[-—–]+\s*(Appearance|Disappearance).*$', '', t, flags=re.IGNORECASE).strip()
    elif lang_code == 'ta':
        t = re.sub(
            r'\s*[-—–]+\s*(தோற்றத் திருநாள்|மறைவுத் திருநாள்|தோற்றம்|மறைவு).*$',
            '',
            t,
            flags=re.IGNORECASE,
        ).strip()
    elif lang_code == 'hi':
        t = re.sub(
            r'\s*[-—–]+\s*(आविर्भाव तिथि|तिरोभाव तिथि|आविर्भाव|तिरोभाव).*$',
            '',
            t,
            flags=re.IGNORECASE,
        ).strip()
    elif lang_code == 'kn':
        t = re.sub(
            r'\s*[-—–]+\s*(ಆವಿರ್ಭಾವ ತಿಥಿ|ತಿರೋಭಾವ ತಿಥಿ|ಆವಿರ್ಭಾವ|ತಿರೋಭಾವ).*$',
            '',
            t,
            flags=re.IGNORECASE,
        ).strip()
    elif lang_code == 'te':
        t = re.sub(
            r'\s*[-—–]+\s*(ఆవిర్భావ తిథి|తిరోభావ తిథి|ఆవిర్భావ|తిరోభావ).*$',
            '',
            t,
            flags=re.IGNORECASE,
        ).strip()
    else:
        t = re.sub(r'\s*[-—–]+.*$', '', t).strip()

    return t


class Command(BaseCommand):
    help = (
        'Import unique Acharya and Devotee pastimes from CalendarObservance '
        'into Story (under Devotee Pastimes, topic_id=1).'
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--topic-id',
            type=int,
            default=1,
            help='StoryMainTopic ID to import into (default: 1 for Devotee Pastimes)',
        )
        parser.add_argument(
            '--category',
            type=str,
            default='Appearance',
            help='CalendarObservance category to filter by (default: Appearance)',
        )
        parser.add_argument(
            '--update-existing',
            action='store_true',
            help='Update article and image if the story already exists for this Acharya',
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Simulate the import process without writing changes to the database',
        )

    def handle(self, *args, **options):
        topic_id = options['topic_id']
        category = options['category']
        update_existing = options['update_existing']
        dry_run = options['dry_run']

        try:
            topic = StoryMainTopic.objects.get(pk=topic_id)
        except StoryMainTopic.DoesNotExist:
            self.stderr.write(self.style.ERROR(f'StoryMainTopic with id={topic_id} not found.'))
            return

        self.stdout.write(
            self.style.NOTICE(
                f"Starting import into Topic: '{topic.name}' (ID: {topic.id}) | Category: '{category}'"
            )
        )
        if dry_run:
            self.stdout.write(self.style.WARNING("Running in DRY-RUN mode. No changes will be saved."))

        # 1. Fetch all observances of the category with preloaded translations
        observances = (
            CalendarObservance.objects.filter(category=category)
            .select_related('day')
            .prefetch_related('translations')
        )

        # 2. Group observances by canonical English name
        grouped = {}
        for obs in observances:
            en_trans = obs.translations.filter(language_code='en').first()
            if not en_trans or not en_trans.description or not en_trans.description.strip():
                continue

            clean_name = clean_name_by_language(en_trans.title, 'en')
            if not clean_name:
                continue

            if clean_name not in grouped:
                grouped[clean_name] = []
            grouped[clean_name].append(obs)

        total_unique = len(grouped)
        self.stdout.write(f"Found {total_unique} distinct Acharyas/Devotees with articles in category '{category}'.")

        # 3. Find current max order in this topic
        last_story = Story.objects.filter(topic=topic).order_by('-order').first()
        current_order = (last_story.order if last_story else 0) + 1

        # 4. Cache existing stories under this topic for quick duplicate detection
        existing_stories = Story.objects.filter(topic=topic).prefetch_related('translations')
        existing_by_name = {}
        for s in existing_stories:
            for t in s.translations.all():
                if t.language_code == 'en':
                    existing_by_name[t.subTopic.strip().lower()] = s

        created_count = 0
        updated_count = 0
        skipped_count = 0

        for clean_name in sorted(grouped.keys()):
            obs_list = grouped[clean_name]

            # Pick the best observance (one with longest English description)
            best_obs = max(
                obs_list,
                key=lambda o: len(
                    (o.translations.filter(language_code='en').first().description or '')
                ),
            )

            # Check if any observance in this group has an image
            image_obs = next((o for o in obs_list if o.image), None)
            best_image = image_obs.image.name if image_obs else None

            # Collect translations across all observances for this group (longest description per language)
            lang_translations = {}
            for o in obs_list:
                for t in o.translations.all():
                    lang = t.language_code
                    desc = (t.description or '').strip()
                    if not desc:
                        continue
                    if lang not in lang_translations or len(desc) > len(lang_translations[lang]['desc']):
                        lang_translations[lang] = {
                            'title': t.title,
                            'desc': desc,
                        }

            clean_name_key = clean_name.lower()
            existing_story = existing_by_name.get(clean_name_key)

            if existing_story and not update_existing:
                skipped_count += 1
                self.stdout.write(f"  [SKIP] '{clean_name}' already exists (Story ID: {existing_story.id}).")
                continue

            if dry_run:
                action = 'UPDATE' if existing_story else 'CREATE'
                langs_preview = list(lang_translations.keys())
                self.stdout.write(
                    f"  [{action}] '{clean_name}' (Langs: {langs_preview}, Image: {bool(best_image)})"
                )
                if existing_story:
                    updated_count += 1
                else:
                    created_count += 1
                continue

            # Execute database changes
            with transaction.atomic():
                if existing_story:
                    story = existing_story
                    if best_image and not story.imagePath:
                        story.imagePath = best_image
                        story.save()
                    action_name = 'Updated'
                    updated_count += 1
                else:
                    story = Story(
                        topic=topic,
                        order=current_order,
                        imagePath=best_image if best_image else '',
                    )
                    current_order += 1
                    story.save()
                    action_name = 'Created'
                    created_count += 1

                # Save translations
                for lang_code, t_data in lang_translations.items():
                    localized_main = topic.get_localized_name(lang_code)
                    localized_sub = clean_name_by_language(t_data['title'], lang_code)
                    if not localized_sub:
                        localized_sub = clean_name

                    trans_obj, _ = StoryTranslation.objects.get_or_create(
                        story=story,
                        language_code=lang_code,
                        defaults={
                            'mainTopic': localized_main,
                            'subTopic': localized_sub,
                            'article': t_data['desc'],
                        },
                    )
                    if not _:
                        # Update translation if exists
                        trans_obj.mainTopic = localized_main
                        trans_obj.subTopic = localized_sub
                        trans_obj.article = t_data['desc']
                        trans_obj.save()

                # Re-save story to generate proper slug based on English translation
                base_slug = slugify(f"{topic.name} {clean_name}", allow_unicode=True)
                story.slug = story._build_unique_slug(base_slug)
                story.save()

                self.stdout.write(
                    self.style.SUCCESS(
                        f"  [{action_name}] '{clean_name}' -> Story ID: {story.id} (Slug: {story.slug}, Langs: {list(lang_translations.keys())})"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"\n=== Summary ===\n"
                f"Total Acharyas Found: {total_unique}\n"
                f"Created: {created_count}\n"
                f"Updated: {updated_count}\n"
                f"Skipped (already exist): {skipped_count}\n"
            )
        )
