from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.core.validators import MaxLengthValidator


LANGUAGE_CHOICES = [
    ('en', 'English'),
    ('ta', 'Tamil'),
    ('kn', 'Kannada'),
    ('te', 'Telugu'),
    ('hi', 'Hindi'),
]


class KirtanCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    categoryImage = models.ImageField(upload_to='kirtans/categories/', max_length=500, blank=True, null=True)
    language_code = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        default='en'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Kirtan Category'
        verbose_name_plural = 'Kirtan Categories'

    def __str__(self):
        trans = self.translations.filter(language_code='en').first()
        if not trans:
            trans = self.translations.first()
        return trans.name if trans else self.name


class KirtanCategoryTranslation(models.Model):
    category = models.ForeignKey(
        KirtanCategory,
        on_delete=models.CASCADE,
        related_name='translations'
    )
    language_code = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        default='en'
    )
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Kirtan Category Translation'
        verbose_name_plural = 'Kirtan Category Translations'
        unique_together = ('category', 'language_code')

    def __str__(self):
        return f"{self.name} ({self.language_code})"


class Kirtan(models.Model):
    category = models.ForeignKey(
        KirtanCategory,
        on_delete=models.SET_NULL,
        related_name='kirtans',
        blank=True,
        null=True,
    )
    audioPath = models.FileField(upload_to='kirtans/audio/', max_length=500, blank=True, null=True)
    imagePath = models.ImageField(upload_to='kirtans/images/', max_length=500, blank=True, null=True)
    videoPath = models.URLField(max_length=500, blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Order for frontend sorting")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Kirtan'
        verbose_name_plural = 'Kirtans'

    def __str__(self):
        trans = self.translations.filter(language_code='en').first()
        if not trans:
            trans = self.translations.first()
        return trans.title if trans else f"Kirtan {self.id}"


class KirtanTranslation(models.Model):
    kirtan = models.ForeignKey(
        Kirtan,
        on_delete=models.CASCADE,
        related_name='translations'
    )
    language_code = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        default='en'
    )
    title = models.CharField(max_length=255)
    authorName = models.CharField(max_length=255, default='', blank=True)
    description = models.TextField(blank=True, validators=[MaxLengthValidator(300)])
    lyrics = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Kirtan Translation'
        verbose_name_plural = 'Kirtan Translations'
        unique_together = ('kirtan', 'language_code')

    def __str__(self):
        return f"{self.title} ({self.language_code})"


@receiver(post_delete, sender=Kirtan)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    for field_name in ['audioPath', 'imagePath']:
        field_file = getattr(instance, field_name)
        if field_file:
            if not Kirtan.objects.filter(**{field_name: field_file.name}).exclude(pk=instance.pk).exists():
                if field_file.storage.exists(field_file.name):
                    field_file.storage.delete(field_file.name)


@receiver(pre_save, sender=Kirtan)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_instance = Kirtan.objects.get(pk=instance.pk)
    except Kirtan.DoesNotExist:
        return False

    for field_name in ['audioPath', 'imagePath']:
        old_file = getattr(old_instance, field_name)
        new_file = getattr(instance, field_name)

        if old_file and old_file != new_file:
            if not Kirtan.objects.filter(**{field_name: old_file.name}).exclude(pk=instance.pk).exists():
                if old_file.storage.exists(old_file.name):
                    old_file.storage.delete(old_file.name)

