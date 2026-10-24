from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models import Q

ETIQUETTE_LANGUAGE_NAMES = {
    "en": "English",
    "ta": "Tamil",
    "hi": "Hindi",
    "te": "Telugu",
    "kn": "Kannada",
    "ml": "Malayalam",
    "bn": "Bengali",
}

ETIQUETTE_LANGUAGE_CHOICES = tuple((code, f"{name} ({code})") for code, name in ETIQUETTE_LANGUAGE_NAMES.items())


class EtiquetteCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.CharField(max_length=200, blank=True, default='')
    image = models.ImageField(upload_to='vaishnava_etiquettes/category/', max_length=500, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Etiquette Category'
        verbose_name_plural = 'Etiquette Categories'

    def __str__(self):
        return self.name


class EtiquetteCategoryTranslation(models.Model):
    category = models.ForeignKey(EtiquetteCategory, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(max_length=10, choices=ETIQUETTE_LANGUAGE_CHOICES, default='en')
    translated_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'language']
        constraints = [
            models.UniqueConstraint(fields=['category', 'language'], name='uq_etiquette_category_translation_language'),
        ]
        verbose_name = 'Etiquette Category Translation'
        verbose_name_plural = 'Etiquette Category Translations'

    def __str__(self):
        return f"[{self.language.upper()}] {self.translated_name}"


class VaishnavaEtiquetteArticle(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True, allow_unicode=True)
    order = models.PositiveIntegerField(default=0)
    articleImage = models.ImageField(upload_to='vaishnava_etiquettes/article/', max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'slug']
        verbose_name = 'Vaishnava Etiquette Article'
        verbose_name_plural = 'Vaishnava Etiquette Articles'

    def __str__(self):
        return f"Etiquette Article - {self.slug}"

    def _build_unique_slug(self, base_slug):
        candidate = base_slug[:280]
        counter = 2

        while VaishnavaEtiquetteArticle.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
            suffix = f"-{counter}"
            candidate = f"{base_slug[:280 - len(suffix)]}{suffix}"
            counter += 1

        return candidate

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = "vaishnava-etiquette"
            self.slug = self._build_unique_slug(base_slug)
        super().save(*args, **kwargs)


# Alias for backward compatibility
VaishnavaEtiquette = VaishnavaEtiquetteArticle


class VaishnavaEtiquetteTranslation(models.Model):
    article_parent = models.ForeignKey(VaishnavaEtiquetteArticle, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(max_length=10, choices=ETIQUETTE_LANGUAGE_CHOICES, default='en')
    category = models.ForeignKey(
        EtiquetteCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='article_translations',
    )
    subTopic = models.CharField(max_length=255)
    article = models.TextField()
    audioPath = models.FileField(upload_to='vaishnava_etiquettes/audio/', max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['article_parent', 'language']
        constraints = [
            models.UniqueConstraint(fields=['article_parent', 'language'], name='uq_etiquette_translation_language'),
        ]
        verbose_name = 'Vaishnava Etiquette Translation'
        verbose_name_plural = 'Vaishnava Etiquette Translations'

    def __str__(self):
        return f"[{self.language.upper()}] {self.subTopic}"


class EtiquetteQuestion(models.Model):
    etiquette_article = models.ForeignKey(VaishnavaEtiquetteArticle, on_delete=models.CASCADE, related_name='questions')
    language = models.CharField(max_length=10, choices=ETIQUETTE_LANGUAGE_CHOICES, default='en')
    question_text = models.TextField()
    order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['etiquette_article_id', 'language', 'order', 'id']
        constraints = [
            models.UniqueConstraint(fields=['etiquette_article', 'language', 'order'], name='uq_etiquette_question_order'),
        ]
        verbose_name = 'Etiquette MCQ Question'
        verbose_name_plural = 'Etiquette MCQ Questions'

    def __str__(self):
        return f"{self.etiquette_article_id} - Q{self.order}"

    def clean(self):
        super().clean()
        existing_count = (
            self.etiquette_article.questions.filter(language=self.language).exclude(pk=self.pk).count()
            if self.etiquette_article_id
            else 0
        )
        if existing_count >= 10:
            raise ValidationError(
                f'An etiquette article can have a maximum of 10 MCQ questions per language (language: {self.language}).'
            )


class EtiquetteQuestionOption(models.Model):
    question = models.ForeignKey(EtiquetteQuestion, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=500)
    order = models.PositiveSmallIntegerField(default=1)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['question_id', 'order', 'id']
        constraints = [
            models.UniqueConstraint(fields=['question', 'order'], name='uq_etiquette_option_order'),
        ]
        verbose_name = 'Etiquette MCQ Option'
        verbose_name_plural = 'Etiquette MCQ Options'

    def __str__(self):
        return f"Q{self.question.order} - Option {self.order}"

    def clean(self):
        super().clean()
        existing_count = self.question.options.exclude(pk=self.pk).count() if self.question_id else 0
        if existing_count >= 4:
            raise ValidationError('A question can have a maximum of 4 options.')


from django.db.models.signals import post_save, post_delete
from django.core.cache import cache

def invalidate_etiquette_cache(sender, **kwargs):
    cache_keys = [f"etiquette_catalog_v2_{lang}" for lang in ETIQUETTE_LANGUAGE_NAMES.keys()]
    cache.delete_many(cache_keys)

for _model in [EtiquetteCategory, EtiquetteCategoryTranslation, VaishnavaEtiquetteArticle, VaishnavaEtiquetteTranslation]:
    post_save.connect(invalidate_etiquette_cache, sender=_model)
    post_delete.connect(invalidate_etiquette_cache, sender=_model)
