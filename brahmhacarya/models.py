from django.db import models
from django.db.models import Q
from django.utils.text import slugify


class BrahmhacaryaArticle(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280, unique=True, blank=True)
    language = models.CharField(max_length=20, default='en', db_index=True)
    category = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)
    excerpt = models.CharField(max_length=500, blank=True)
    content = models.TextField()
    audioUrl = models.FileField(upload_to='brahmhacarya/audio/', max_length=500, blank=True, null=True)
    featured_image = models.ImageField(upload_to='brahmhacarya/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['language', 'order', '-published_at', '-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['language', 'category', 'order'],
                condition=~Q(category=''),
                name='unique_order_per_brahmhacarya_language_category',
            )
        ]
        verbose_name = 'Brahmhacarya Article'
        verbose_name_plural = 'Brahmhacarya Articles'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class BrahmhacaryaRegistration(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30, default='')
    whatsapp_number = models.CharField(max_length=30, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Brahmhacarya Registration'
        verbose_name_plural = 'Brahmhacarya Registrations'

    def __str__(self):
        return f"{self.full_name} ({self.email})"
