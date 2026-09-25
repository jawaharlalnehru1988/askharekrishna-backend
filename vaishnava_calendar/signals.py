import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CalendarObservance, CalendarObservanceTranslation

logger = logging.getLogger(__name__)

# Thread-local recursion guard
_is_syncing = False


@receiver(post_save, sender=CalendarObservanceTranslation)
def sync_observance_translation_across_years(sender, instance, **kwargs):
    """
    When a translation is added or updated for an observance (e.g. in 2026),
    automatically propagate this translation (title, description, audio_file)
    to all matching observances across other calendar years (2027, 2028, etc.).
    """
    global _is_syncing
    if _is_syncing:
        return

    source_obs = instance.observance
    if not source_obs:
        return

    # Determine the canonical English title of this observance
    if instance.language_code == 'en':
        en_title = instance.title.strip()
    else:
        en_trans = source_obs.translations.filter(language_code='en').first()
        en_title = en_trans.title.strip() if en_trans else None

    if not en_title:
        return

    # Find all other observances across any year with the same English title and category
    matching_observances = CalendarObservance.objects.filter(
        translations__language_code='en',
        translations__title=en_title,
        category=source_obs.category
    ).exclude(id=source_obs.id).distinct()

    if not matching_observances.exists():
        return

    _is_syncing = True
    try:
        for target_obs in matching_observances:
            target_trans, created = CalendarObservanceTranslation.objects.get_or_create(
                observance=target_obs,
                language_code=instance.language_code,
                defaults={
                    'title': instance.title,
                    'description': instance.description,
                    'audio_file': instance.audio_file,
                }
            )
            if not created:
                needs_save = False
                if target_trans.title != instance.title:
                    target_trans.title = instance.title
                    needs_save = True
                if target_trans.description != instance.description:
                    target_trans.description = instance.description
                    needs_save = True
                if instance.audio_file and target_trans.audio_file != instance.audio_file:
                    target_trans.audio_file = instance.audio_file
                    needs_save = True
                if needs_save:
                    target_trans.save()
    except Exception as e:
        logger.error(f"Error syncing translation across years for '{en_title}': {e}")
    finally:
        _is_syncing = False


@receiver(post_save, sender=CalendarObservance)
def sync_observance_image_across_years(sender, instance, **kwargs):
    """
    When an image is added or updated on an observance,
    automatically copy it to all other occurrences in other years.
    """
    global _is_syncing
    if _is_syncing or not instance.image:
        return

    en_trans = instance.translations.filter(language_code='en').first()
    if not en_trans:
        return
    en_title = en_trans.title.strip()

    matching_observances = CalendarObservance.objects.filter(
        translations__language_code='en',
        translations__title=en_title,
        category=instance.category,
        image__isnull=True
    ).exclude(id=instance.id).distinct()

    _is_syncing = True
    try:
        for target_obs in matching_observances:
            target_obs.image = instance.image
            target_obs.save(update_fields=['image'])
    except Exception as e:
        logger.error(f"Error syncing image across years for '{en_title}': {e}")
    finally:
        _is_syncing = False
