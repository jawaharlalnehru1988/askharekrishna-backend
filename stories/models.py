from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models import Q
from pooja_vidhis.models import LANGUAGE_CHOICES, Language


from django.utils import timezone

class StoryMainTopic(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    name_translations = models.JSONField(default=dict, blank=True, help_text="Localized names: {'ta': '...', 'hi': '...', 'kn': '...', 'te': '...'}")
    description = models.CharField(max_length=200, blank=True, default='')
    image = models.ImageField(upload_to='stories/main-topic/', max_length=500, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Story Main Topic'
        verbose_name_plural = 'Story Main Topics'

    def __str__(self):
        return self.name

    def get_localized_name(self, lang_code='en'):
        if not lang_code or lang_code == 'en':
            return self.name
        if isinstance(self.name_translations, dict):
            localized = self.name_translations.get(lang_code.lower())
            if localized:
                return localized
        return self.name

    def save(self, *args, **kwargs):
        old_image_name = None
        if self.pk:
            old_image_name = StoryMainTopic.objects.filter(pk=self.pk).values_list('image', flat=True).first()

        super().save(*args, **kwargs)

        new_image_name = self.image.name if self.image else None
        if old_image_name and new_image_name and old_image_name != new_image_name:
            storage = StoryMainTopic._meta.get_field('image').storage
            if storage.exists(old_image_name):
                storage.delete(old_image_name)


class Story(models.Model):
    topic = models.ForeignKey(
        StoryMainTopic,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='stories',
    )
    slug = models.SlugField(max_length=280, unique=True, blank=True, allow_unicode=True)
    order = models.PositiveIntegerField(default=0)
    imagePath = models.ImageField(upload_to='stories/images/', max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'

    def __str__(self):
        trans = self.get_translation('en') or (self.translations.first() if self.pk else None)
        if trans:
            return f"[{trans.language_code.upper()}] {trans.mainTopic} - {trans.subTopic}"
        return f"Story {self.id or 'new'}"

    def effective_image_path(self):
        return self.imagePath

    def get_translation(self, lang_code='en'):
        if not self.pk:
            return None
        if hasattr(self, '_prefetched_objects_cache') and 'translations' in self._prefetched_objects_cache:
            translations = self._prefetched_objects_cache['translations']
            trans = next((t for t in translations if t.language_code == lang_code), None)
            if not trans:
                trans = next((t for t in translations if t.language_code == 'en'), None)
            if not trans and translations:
                trans = translations[0]
            return trans

        trans = self.translations.filter(language_code=lang_code).first()
        if not trans:
            trans = self.translations.filter(language_code='en').first()
        if not trans:
            trans = self.translations.first()
        return trans

    def _build_unique_slug(self, base_slug):
        candidate = base_slug[:280]
        counter = 2

        while Story.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
            suffix = f"-{counter}"
            candidate = f"{base_slug[:280 - len(suffix)]}{suffix}"
            counter += 1

        return candidate

    def save(self, *args, **kwargs):
        if not self.slug:
            trans = self.get_translation('en') or (self.translations.first() if self.pk else None)
            if trans:
                base_slug = slugify(f"{trans.mainTopic} {trans.subTopic}", allow_unicode=True)
            else:
                base_slug = f"story-{self.pk or 'new'}"
            if not base_slug:
                base_slug = "story"
            self.slug = self._build_unique_slug(base_slug)
        super().save(*args, **kwargs)


class StoryTranslation(models.Model):
    story = models.ForeignKey(
        Story,
        on_delete=models.CASCADE,
        related_name='translations',
    )
    language_code = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        default='en',
    )
    mainTopic = models.CharField(max_length=255)
    subTopic = models.CharField(max_length=255)
    article = models.TextField()
    audioPath = models.FileField(upload_to='stories/audio/', max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['story_id', 'language_code']
        constraints = [
            models.UniqueConstraint(
                fields=['story', 'language_code'],
                name='uq_story_translation_language',
            ),
        ]
        verbose_name = 'Story Translation'
        verbose_name_plural = 'Story Translations'

    def __str__(self):
        return f"[{self.language_code.upper()}] {self.mainTopic} - {self.subTopic}"


class StoryQuestion(models.Model):
    translation = models.ForeignKey(
        StoryTranslation,
        on_delete=models.CASCADE,
        related_name='questions',
        null=True,
        blank=True,
    )
    question_text = models.TextField()
    order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['translation_id', 'order', 'id']
        constraints = [
            models.UniqueConstraint(
                fields=['translation', 'order'],
                name='uq_story_translation_question_order',
            ),
        ]
        verbose_name = 'Story MCQ Question'
        verbose_name_plural = 'Story MCQ Questions'

    def __str__(self):
        return f"{self.translation_id} - Q{self.order}"

    def clean(self):
        super().clean()
        existing_count = self.translation.questions.exclude(pk=self.pk).count() if self.translation_id else 0
        if existing_count >= 10:
            raise ValidationError('A story translation can have a maximum of 10 MCQ questions.')


class StoryQuestionOption(models.Model):
    question = models.ForeignKey(
        StoryQuestion,
        on_delete=models.CASCADE,
        related_name='options',
    )
    option_text = models.CharField(max_length=500)
    order = models.PositiveSmallIntegerField(default=1)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['question_id', 'order', 'id']
        constraints = [
            models.UniqueConstraint(
                fields=['question', 'order'],
                name='uq_story_translation_option_order',
            ),
        ]
        verbose_name = 'Story MCQ Option'
        verbose_name_plural = 'Story MCQ Options'

    def __str__(self):
        return f"Q{self.question.order} - Option {self.order}"

    def clean(self):
        super().clean()
        existing_count = self.question.options.exclude(pk=self.pk).count() if self.question_id else 0
        if existing_count >= 4:
            raise ValidationError('A question can have a maximum of 4 options.')
