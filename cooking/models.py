from django.db import models
from django.utils.text import slugify
from pooja_vidhis.models import LANGUAGE_CHOICES

COOKING_LANGUAGE_CHOICES = LANGUAGE_CHOICES


class CookingMainTopic(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    name_translations = models.JSONField(
        default=dict,
        blank=True,
        help_text="Localized names: {'ta': '...', 'hi': '...', 'kn': '...', 'te': '...', ...}",
    )
    description = models.CharField(max_length=500, blank=True, default='')
    description_translations = models.JSONField(
        default=dict,
        blank=True,
        help_text="Localized descriptions: {'ta': '...', 'hi': '...', 'kn': '...', 'te': '...', ...}",
    )
    image = models.ImageField(upload_to='cooking/category/', max_length=500, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Cooking Main Topic'
        verbose_name_plural = 'Cooking Main Topics'

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

    def get_localized_description(self, lang_code='en'):
        if not lang_code or lang_code == 'en':
            return self.description
        if isinstance(self.description_translations, dict):
            localized = self.description_translations.get(lang_code.lower())
            if localized:
                return localized
        return self.description


class CookingArticle(models.Model):
    topic = models.ForeignKey(
        CookingMainTopic,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles',
    )
    slug = models.SlugField(max_length=280, unique=True, blank=True, allow_unicode=True)
    order = models.PositiveIntegerField(default=0)
    imagePath = models.ImageField(upload_to='cooking/images/', max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Cooking Article'
        verbose_name_plural = 'Cooking Articles'

    def __str__(self):
        trans = self.get_translation('en') or (self.translations.first() if self.pk else None)
        if trans:
            return f"[{trans.language_code.upper()}] {trans.mainTopic} - {trans.subTopic}"
        return f"Cooking Article {self.id or 'new'}"

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

        while CookingArticle.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
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
                base_slug = f"cooking-article-{self.pk or 'new'}"
            if not base_slug:
                base_slug = "cooking-article"
            self.slug = self._build_unique_slug(base_slug)
        super().save(*args, **kwargs)


class CookingArticleTranslation(models.Model):
    article_parent = models.ForeignKey(
        CookingArticle,
        on_delete=models.CASCADE,
        related_name='translations',
    )
    language_code = models.CharField(
        max_length=10,
        choices=COOKING_LANGUAGE_CHOICES,
        default='en',
    )
    mainTopic = models.CharField(max_length=255)
    subTopic = models.CharField(max_length=255)
    article = models.TextField()
    audioPath = models.FileField(upload_to='cooking/audio/', max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['article_parent_id', 'language_code']
        constraints = [
            models.UniqueConstraint(
                fields=['article_parent', 'language_code'],
                name='uq_cooking_translation_language',
            ),
        ]
        verbose_name = 'Cooking Article Translation'
        verbose_name_plural = 'Cooking Article Translations'

    def __str__(self):
        return f"[{self.language_code.upper()}] {self.mainTopic} - {self.subTopic}"
