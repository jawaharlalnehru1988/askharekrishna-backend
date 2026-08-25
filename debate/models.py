from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models import Q

DEBATE_LANGUAGE_NAMES = {
    "en": "English",
    "ta": "Tamil",
    "hi": "Hindi",
    "te": "Telugu",
    "kn": "Kannada",
    "ml": "Malayalam",
    "bn": "Bengali",
}

DEBATE_LANGUAGE_CHOICES = tuple((code, f"{name} ({code})") for code, name in DEBATE_LANGUAGE_NAMES.items())



class DebateCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.CharField(max_length=200, blank=True, default='')
    image = models.ImageField(upload_to='debate/category/', max_length=500, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Debate Category'
        verbose_name_plural = 'Debate Categories'

    def __str__(self):
        return self.name


class DebateCategoryTranslation(models.Model):
    category = models.ForeignKey(DebateCategory, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(max_length=10, choices=DEBATE_LANGUAGE_CHOICES, default='en')
    translated_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'language']
        constraints = [
            models.UniqueConstraint(fields=['category', 'language'], name='uq_debate_category_translation_language'),
        ]
        verbose_name = 'Debate Category Translation'
        verbose_name_plural = 'Debate Category Translations'

    def __str__(self):
        return f"[{self.language.upper()}] {self.translated_name}"


class DebateArticle(models.Model):
    # Removed debateCategory as it is now in translation model
    slug = models.SlugField(max_length=255, unique=True, blank=True, allow_unicode=True)
    order = models.PositiveIntegerField(default=0)
    articleImage = models.ImageField(upload_to='debate/article/', max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'slug']
        verbose_name = 'Debate Article'
        verbose_name_plural = 'Debate Articles'

    def __str__(self):
        return f"Debate Article - {self.slug}"

    def _build_unique_slug(self, base_slug):
        candidate = base_slug[:280]
        counter = 2

        while DebateArticle.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
            suffix = f"-{counter}"
            candidate = f"{base_slug[:280 - len(suffix)]}{suffix}"
            counter += 1

        return candidate

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = "debate-article"
            self.slug = self._build_unique_slug(base_slug)
        super().save(*args, **kwargs)


class DebateArticleTranslation(models.Model):
    article_parent = models.ForeignKey(DebateArticle, on_delete=models.CASCADE, related_name='translations')
    language = models.CharField(max_length=10, choices=DEBATE_LANGUAGE_CHOICES, default='en')
    debateCategory = models.ForeignKey(
        DebateCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='article_translations',
    )
    subTopic = models.CharField(max_length=255)
    article = models.TextField()
    audioPath = models.FileField(upload_to='debate/audio/', max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['article_parent', 'language']
        constraints = [
            models.UniqueConstraint(fields=['article_parent', 'language'], name='uq_debate_translation_language'),
        ]
        verbose_name = 'Debate Article Translation'
        verbose_name_plural = 'Debate Article Translations'

    def __str__(self):
        return f"[{self.language.upper()}] {self.subTopic}"


class DebateQuestion(models.Model):
    debate_article = models.ForeignKey(DebateArticle, on_delete=models.CASCADE, related_name='questions')
    language = models.CharField(max_length=10, choices=DEBATE_LANGUAGE_CHOICES, default='en')
    question_text = models.TextField()
    order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['debate_article_id', 'language', 'order', 'id']
        constraints = [
            models.UniqueConstraint(fields=['debate_article', 'language', 'order'], name='uq_debate_question_order'),
        ]
        verbose_name = 'Debate MCQ Question'
        verbose_name_plural = 'Debate MCQ Questions'

    def __str__(self):
        return f"{self.debate_article_id} - Q{self.order}"

    def clean(self):
        super().clean()
        existing_count = self.debate_article.questions.filter(language=self.language).exclude(pk=self.pk).count() if self.debate_article_id else 0
        if existing_count >= 10:
            raise ValidationError(f'A debate article can have a maximum of 10 MCQ questions per language (language: {self.language}).')


class DebateQuestionOption(models.Model):
    question = models.ForeignKey(DebateQuestion, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=500)
    order = models.PositiveSmallIntegerField(default=1)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['question_id', 'order', 'id']
        constraints = [
            models.UniqueConstraint(fields=['question', 'order'], name='uq_debate_option_order'),
        ]
        verbose_name = 'Debate MCQ Option'
        verbose_name_plural = 'Debate MCQ Options'

    def __str__(self):
        return f"Q{self.question.order} - Option {self.order}"

    def clean(self):
        super().clean()
        existing_count = self.question.options.exclude(pk=self.pk).count() if self.question_id else 0
        if existing_count >= 4:
            raise ValidationError('A question can have a maximum of 4 options.')
