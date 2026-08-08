from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify


LANGUAGE_CHOICES = [
    ('en', 'English'),
    ('ta', 'Tamil'),
    ('kn', 'Kannada'),
    ('te', 'Telugu'),
    ('hi', 'Hindi'),
    ('ml', 'Malayalam'),
    ('bn', 'Bengali'),
]


class PoojaVidhiTopic(models.Model):
    name = models.CharField(max_length=255, unique=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Pooja Vidhi Topic'
        verbose_name_plural = 'Pooja Vidhi Topics'

    def __str__(self):
        return self.name


class Language(models.Model):
    code = models.CharField(max_length=10, unique=True, primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return f"{self.name} ({self.code})"


class PoojaVidhi(models.Model):
    slug = models.SlugField(max_length=280, unique=True, blank=True, allow_unicode=True)
    order = models.PositiveIntegerField(default=0)
    articleImage = models.ImageField(upload_to='pooja_vidhis/images/', max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Pooja Vidhi'
        verbose_name_plural = 'Pooja Vidhis'

    def __str__(self):
        trans = self.get_translation('en') or self.translations.first()
        if trans:
            return f"[{trans.language_code.upper()}] {trans.mainTopic} - {trans.subTopic}"
        return f"Pooja Vidhi {self.id}"

    def effective_image(self):
        return self.articleImage

    def get_translation(self, lang_code='en'):
        trans = self.translations.filter(language_code=lang_code).first()
        if not trans:
            trans = self.translations.filter(language_code='en').first()
        if not trans:
            trans = self.translations.first()
        return trans

    def _build_unique_slug(self, base_slug):
        candidate = base_slug[:280]
        counter = 2

        while PoojaVidhi.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
            suffix = f"-{counter}"
            candidate = f"{base_slug[:280 - len(suffix)]}{suffix}"
            counter += 1

        return candidate

    def save(self, *args, **kwargs):
        if not self.slug:
            trans = self.get_translation('en') or self.translations.first()
            if trans:
                base_slug = slugify(f"{trans.mainTopic} {trans.subTopic}", allow_unicode=True)
            else:
                base_slug = f"pooja-vidhi-{self.pk or 'new'}"
            if not base_slug:
                base_slug = "pooja-vidhi"
            self.slug = self._build_unique_slug(base_slug)
        super().save(*args, **kwargs)


class PoojaVidhiTranslation(models.Model):
    pooja_vidhi = models.ForeignKey(
        PoojaVidhi,
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
    audioPath = models.FileField(upload_to='pooja_vidhis/audio/', max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['language_code']
        verbose_name = 'Pooja Vidhi Translation'
        verbose_name_plural = 'Pooja Vidhi Translations'
        unique_together = ('pooja_vidhi', 'language_code')

    def __str__(self):
        return f"[{self.language_code.upper()}] {self.mainTopic} - {self.subTopic}"


class PoojaVidhiQuestion(models.Model):
    translation = models.ForeignKey(
        PoojaVidhiTranslation,
        on_delete=models.CASCADE,
        related_name='questions',
    )
    question_text = models.TextField()
    order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['translation_id', 'order', 'id']
        constraints = [
            models.UniqueConstraint(fields=['translation', 'order'], name='uq_pooja_vidhi_translation_question_order'),
        ]
        verbose_name = 'Pooja Vidhi MCQ Question'
        verbose_name_plural = 'Pooja Vidhi MCQ Questions'

    def __str__(self):
        return f"{self.translation.subTopic} ({self.translation.language_code}) - Q{self.order}"

    def clean(self):
        super().clean()
        if self.translation_id:
            existing_count = self.translation.questions.exclude(pk=self.pk).count()
            if existing_count >= 10:
                raise ValidationError('A Pooja Vidhi translation can have a maximum of 10 MCQ questions.')


class PoojaVidhiQuestionOption(models.Model):
    question = models.ForeignKey(PoojaVidhiQuestion, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=500)
    order = models.PositiveSmallIntegerField(default=1)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['question_id', 'order', 'id']
        constraints = [
            models.UniqueConstraint(fields=['question', 'order'], name='uq_pooja_vidhi_option_order'),
        ]
        verbose_name = 'Pooja Vidhi MCQ Option'
        verbose_name_plural = 'Pooja Vidhi MCQ Options'

    def __str__(self):
        return f"Q{self.question.order} - Option {self.order}"

    def clean(self):
        super().clean()
        existing_count = self.question.options.exclude(pk=self.pk).count() if self.question_id else 0
        if existing_count >= 4:
            raise ValidationError('A question can have a maximum of 4 options.')
