from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os


class VideoGallery(models.Model):
    video = models.FileField(upload_to='video_gallery/', max_length=500)
    note = models.TextField(blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Video Gallery Item'
        verbose_name_plural = 'Video Gallery'

    def __str__(self):
        return f"Video #{self.id}"


@receiver(post_delete, sender=VideoGallery)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `VideoGallery` object is deleted.
    """
    if instance.video:
        # Check if any other VideoGallery instance uses the same video file
        if not VideoGallery.objects.filter(video=instance.video.name).exclude(pk=instance.pk).exists():
            if instance.video.storage.exists(instance.video.name):
                instance.video.storage.delete(instance.video.name)


@receiver(pre_save, sender=VideoGallery)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `VideoGallery` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_instance = VideoGallery.objects.get(pk=instance.pk)
    except VideoGallery.DoesNotExist:
        return False

    old_file = old_instance.video
    new_file = instance.video

    if old_file and old_file != new_file:
        # Check if any other VideoGallery instance uses the same old video file
        if not VideoGallery.objects.filter(video=old_file.name).exclude(pk=instance.pk).exists():
            if old_file.storage.exists(old_file.name):
                old_file.storage.delete(old_file.name)

