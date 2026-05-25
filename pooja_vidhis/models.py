from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify


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


class LanguageChoices(models.TextChoices):
    EN = 'en', 'en'
    TA = 'ta', 'ta'


class PoojaVidhi(models.Model):
    mainTopic = models.CharField(max_length=255)
    subTopic = models.CharField(max_length=255)
    article = models.TextField()
    slug = models.SlugField(max_length=280, unique=True, blank=True, allow_unicode=True)
    order = models.PositiveIntegerField(default=0)
    language = models.CharField(max_length=10, choices=LanguageChoices.choices, default='en')
    audioPath = models.FileField(upload_to='pooja_vidhis/audio/', max_length=500, blank=True, null=True)
    articleImage = models.ImageField(upload_to='pooja_vidhis/images/', max_length=500, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'mainTopic', 'subTopic']
        verbose_name = 'Pooja Vidhi'
        verbose_name_plural = 'Pooja Vidhis'

    def __str__(self):
        return f"[{self.language.upper()}] {self.mainTopic} - {self.subTopic}"

    def _build_unique_slug(self, base_slug):
        candidate = base_slug[:280]
        counter = 2

        while PoojaVidhi.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
            suffix = f"-{counter}"
            candidate = f"{base_slug[:280 - len(suffix)]}{suffix}"
            counter += 1

        return candidate

    def save(self, *args, **kwargs):
        base_slug = slugify(f"{self.mainTopic} {self.subTopic}", allow_unicode=True)
        if not base_slug:
            base_slug = "pooja-vidhi"

        self.slug = self._build_unique_slug(base_slug)
        super().save(*args, **kwargs)


class PoojaVidhiQuestion(models.Model):
    pooja_vidhi = models.ForeignKey(PoojaVidhi, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['pooja_vidhi_id', 'order', 'id']
        constraints = [
            models.UniqueConstraint(fields=['pooja_vidhi', 'order'], name='uq_pooja_vidhi_question_order'),
        ]
        verbose_name = 'Pooja Vidhi MCQ Question'
        verbose_name_plural = 'Pooja Vidhi MCQ Questions'

    def __str__(self):
        return f"{self.pooja_vidhi_id} - Q{self.order}"

    def clean(self):
        super().clean()
        existing_count = self.pooja_vidhi.questions.exclude(pk=self.pk).count() if self.pooja_vidhi_id else 0
        if existing_count >= 10:
            raise ValidationError('A Pooja Vidhi article can have a maximum of 10 MCQ questions.')


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
