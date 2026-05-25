from django.db import models
from django.utils.text import slugify

class VaishnavaEtiquette(models.Model):
    mainTopic = models.CharField(max_length=255)
    subTopic = models.CharField(max_length=255)
    article = models.TextField()
    slug = models.SlugField(max_length=280, unique=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    language = models.CharField(max_length=10, default='en')
    audioPath = models.FileField(upload_to='vaishnava_etiquettes/audio/', max_length=500, blank=True, null=True)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'mainTopic', 'subTopic']
        verbose_name = 'Vaishnava Etiquette'
        verbose_name_plural = 'Vaishnava Etiquettes'

    def __str__(self):
        return f"[{self.language.upper()}] {self.mainTopic} - {self.subTopic}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.mainTopic} {self.subTopic}")[:280]
        super().save(*args, **kwargs)
