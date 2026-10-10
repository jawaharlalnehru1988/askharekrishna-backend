from django.db import models
from django.utils.text import slugify

RITVIK_LANGUAGE_NAMES = {
    "en": "English",
    "ta": "Tamil",
    "hi": "Hindi",
    "te": "Telugu",
    "kn": "Kannada",
    "ml": "Malayalam",
    "bn": "Bengali",
}

RITVIK_LANGUAGE_CHOICES = tuple((code, f"{name} ({code})") for code, name in RITVIK_LANGUAGE_NAMES.items())


class RitvikSection(models.Model):
    section_number = models.PositiveIntegerField(unique=True, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to='ritvik/sections/', max_length=500, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'section_number']
        verbose_name = 'Ritvik Section'
        verbose_name_plural = 'Ritvik Sections'

    def __str__(self):
        trans = self.translations.filter(language='en').first() or self.translations.first()
        title = trans.title if trans else f"Section {self.section_number}"
        return f"Section {self.section_number}: {title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"section-{self.section_number}"
        if not self.order:
            self.order = self.section_number
        super().save(*args, **kwargs)


class RitvikSectionTranslation(models.Model):
    section = models.ForeignKey(RitvikSection, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(max_length=10, choices=RITVIK_LANGUAGE_CHOICES, default='en')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['section', 'language']
        constraints = [
            models.UniqueConstraint(fields=['section', 'language'], name='uq_ritvik_section_translation_language'),
        ]
        verbose_name = 'Ritvik Section Translation'
        verbose_name_plural = 'Ritvik Section Translations'

    def __str__(self):
        return f"[{self.language.upper()}] Section {self.section.section_number} - {self.title}"


class RitvikQA(models.Model):
    section = models.ForeignKey(RitvikSection, on_delete=models.CASCADE, related_name='questions')
    question_code = models.CharField(max_length=20, db_index=True)  # e.g., "Q1.1"
    slug = models.SlugField(max_length=255, unique=True, blank=True, allow_unicode=True)
    image = models.ImageField(upload_to='ritvik/questions/', max_length=500, blank=True, null=True)  # common image
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['section__section_number', 'order', 'id']
        verbose_name = 'Ritvik Q&A'
        verbose_name_plural = 'Ritvik Q&As'

    def __str__(self):
        return f"{self.question_code} ({self.slug})"

    def save(self, *args, **kwargs):
        if not self.slug and self.question_code:
            self.slug = slugify(self.question_code.lower())
        super().save(*args, **kwargs)


class RitvikQATranslation(models.Model):
    qa_parent = models.ForeignKey(RitvikQA, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(max_length=10, choices=RITVIK_LANGUAGE_CHOICES, default='en')
    question = models.TextField()
    answer = models.TextField()
    summary = models.TextField(blank=True, default='')
    audioPath = models.FileField(upload_to='ritvik/audio/', max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['qa_parent', 'language']
        constraints = [
            models.UniqueConstraint(fields=['qa_parent', 'language'], name='uq_ritvik_qa_translation_language'),
        ]
        verbose_name = 'Ritvik Q&A Translation'
        verbose_name_plural = 'Ritvik Q&A Translations'

    def __str__(self):
        return f"[{self.language.upper()}] {self.qa_parent.question_code}: {self.question[:60]}"
