from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os


class BookLibrary(models.Model):
    """Model for managing spiritual books and literature"""
    
    CATEGORY_CHOICES = [
        ('vedic_scriptures', 'Vedic Scriptures'),
        ('prabhupada_books', 'Prabhupada Books'),
        ('puranas', 'Puranas'),
        ('other_sampradaya_scriptures', 'Other Sampradaya scriptures'),
        ('articles', 'Articles'),
        ('research_documentations', 'Research Documentations'),
        ('tutorials', 'Tutorials'),
        ('stories', 'Stories'),
        ('miscellaneous', 'Miscellaneous'),
    ]
    
    BOOK_FORMAT_CHOICES = [
        ('pdf', 'PDF'),
        ('epub', 'EPUB'),
        ('doc', 'DOC'),
        ('docx', 'DOCX'),
        ('xls', 'XLS'),
        ('xlsx', 'XLSX'),
        ('txt', 'TXT'),
        ('mobi', 'MOBI'),
        ('azw', 'AZW'),
    ]

    LANGUAGE_CHOICES = [
        ('tamil', 'Tamil'),
        ('english', 'English'),
        ('hindi', 'Hindi'),
        ('sanskrit', 'Sanskrit'),
        ('kannada', 'Kannada'),
        ('telugu', 'Telugu'),
        ('bengali', 'Bengali'),
        ('malayalam', 'Malayalam'),
        ('marathi', 'Marathi'),
    ]
    
    # Required fields
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=300)
    description = models.CharField(max_length=150)
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    book_format = models.CharField(max_length=10, choices=BOOK_FORMAT_CHOICES)
    book_url = models.FileField(upload_to='books/', max_length=500)
    
    # Optional fields
    pages = models.PositiveIntegerField(
        blank=True, 
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(100000)]
    )
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    downloads = models.PositiveIntegerField(default=0)
    
    class Meta:
        db_table = 'book_library'
        ordering = ['-created_at']
        verbose_name = 'DocumentLibrary'
        verbose_name_plural = 'DocumentLibrary'
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def increment_downloads(self):
        """Increment download counter"""
        self.downloads += 1
        self.save(update_fields=['downloads'])


@receiver(post_delete, sender=BookLibrary)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    for field_name in ['book_url', 'cover_image']:
        field_file = getattr(instance, field_name)
        if field_file:
            if not BookLibrary.objects.filter(**{field_name: field_file.name}).exclude(pk=instance.pk).exists():
                if field_file.storage.exists(field_file.name):
                    field_file.storage.delete(field_file.name)


@receiver(pre_save, sender=BookLibrary)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_instance = BookLibrary.objects.get(pk=instance.pk)
    except BookLibrary.DoesNotExist:
        return False

    for field_name in ['book_url', 'cover_image']:
        old_file = getattr(old_instance, field_name)
        new_file = getattr(instance, field_name)

        if old_file and old_file != new_file:
            if not BookLibrary.objects.filter(**{field_name: old_file.name}).exclude(pk=instance.pk).exists():
                if old_file.storage.exists(old_file.name):
                    old_file.storage.delete(old_file.name)

