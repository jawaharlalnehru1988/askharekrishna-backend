from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os


class Audio(models.Model):
    audioListId = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    language = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    audioUrl = models.FileField(upload_to='audios/', max_length=500)
    isPlaying = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'audio-bg'
        verbose_name_plural = 'audio-bg'

    def __str__(self):
        return f"{self.title} ({self.language})"


@receiver(post_delete, sender=Audio)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.audioUrl:
        if not Audio.objects.filter(audioUrl=instance.audioUrl.name).exclude(pk=instance.pk).exists():
            if instance.audioUrl.storage.exists(instance.audioUrl.name):
                instance.audioUrl.storage.delete(instance.audioUrl.name)


@receiver(pre_save, sender=Audio)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_instance = Audio.objects.get(pk=instance.pk)
    except Audio.DoesNotExist:
        return False

    old_file = old_instance.audioUrl
    new_file = instance.audioUrl

    if old_file and old_file != new_file:
        if not Audio.objects.filter(audioUrl=old_file.name).exclude(pk=instance.pk).exists():
            if old_file.storage.exists(old_file.name):
                old_file.storage.delete(old_file.name)

