from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os


BOOK_CHOICES = [
    ('bhagavad_gita', 'Bhagavad Gita'),
]

LANGUAGE_CHOICES = [
    ('tamil', 'Tamil'),
    ('english', 'English'),
    ('kannada', 'Kannada'),
    ('hindi', 'Hindi'),
    ('telugu', 'Telugu'),
    ('malayalam', 'Malayalam'),
]


class Video(models.Model):
    """
    Represents a scripture video entry.
    `video_upload_path` is a filesystem path (not a URL) to the video file.
    """
    video_file = models.FileField(
        upload_to='videos/',
        max_length=1000,
        help_text="Upload the video file here."
    )
    language = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES,
        default='tamil',
    )
    chapter_number = models.PositiveIntegerField()
    sloka_number = models.PositiveIntegerField()
    book_name = models.CharField(
        max_length=100,
        choices=BOOK_CHOICES,
        default='bhagavad_gita',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['book_name', 'chapter_number', 'sloka_number', 'language']
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        unique_together = ('book_name', 'chapter_number', 'sloka_number', 'language')

    def __str__(self):
        return (
            f"{self.get_book_name_display()} | "
            f"Chapter {self.chapter_number} | "
            f"Sloka {self.sloka_number} | "
            f"{self.get_language_display()}"
        )


@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Video` object is deleted.
    """
    if instance.video_file:
        if instance.video_file.storage.exists(instance.video_file.name):
            instance.video_file.storage.delete(instance.video_file.name)


@receiver(pre_save, sender=Video)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Video` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_instance = Video.objects.get(pk=instance.pk)
    except Video.DoesNotExist:
        return False

    old_file = old_instance.video_file
    new_file = instance.video_file

    if old_file and old_file != new_file:
        if old_file.storage.exists(old_file.name):
            old_file.storage.delete(old_file.name)
