from django.db import models


class WebUrlResource(models.Model):
    link = models.URLField(max_length=500)
    description = models.TextField(blank=True)
    resources = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Web URL Resource'
        verbose_name_plural = 'Web URL Resources'

    def __str__(self):
        return self.link
