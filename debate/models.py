from django.db import models
from django.utils.text import slugify


class DebateCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.CharField(max_length=200, blank=True, default='')
    image = models.ImageField(upload_to='debate/category/', max_length=500, blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Debate Category'
        verbose_name_plural = 'Debate Categories'

    def __str__(self):
        return self.name


class DebateArticle(models.Model):
    topic = models.CharField(max_length=255, blank=True, default='')
    subTopic = models.CharField(max_length=255)
    debateCategory = models.ForeignKey(
        DebateCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles',
    )
    article = models.TextField()
    slug = models.SlugField(max_length=280, unique=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    language = models.CharField(max_length=10, default='en')
    audioPath = models.FileField(upload_to='debate/audio/', max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'topic', 'subTopic']
        verbose_name = 'Debate Article'
        verbose_name_plural = 'Debate Articles'

    def __str__(self):
        return f"[{self.language.upper()}] {self.topic or '-'} - {self.subTopic}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.topic} {self.subTopic}")[:280]
        super().save(*args, **kwargs)
