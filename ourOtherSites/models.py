from django.db import models


class OurOtherSite(models.Model):
    web_url = models.URLField(max_length=500)
    purpose = models.TextField()
    features_available = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Our Other Site'
        verbose_name_plural = 'Our Other Sites'

    def __str__(self):
        return self.web_url
