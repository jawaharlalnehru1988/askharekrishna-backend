from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.conf import settings
from urllib.parse import urljoin


class ImageGallery(models.Model):
    image = models.ImageField(upload_to='image_gallery/', max_length=500)
    cdn_url = models.URLField(max_length=1000, blank=True, default='')
    category = models.CharField(max_length=100, blank=True, default='')
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Image Gallery Item'
        verbose_name_plural = 'Image Gallery'

    def __str__(self):
        return f"Image #{self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            public_base = getattr(settings, 'PUBLIC_MEDIA_BASE_URL', '').strip()
            generated_cdn_url = urljoin(public_base, self.image.url) if public_base else self.image.url
        else:
            generated_cdn_url = ''

        if self.cdn_url != generated_cdn_url:
            self.cdn_url = generated_cdn_url
            type(self).objects.filter(pk=self.pk).update(cdn_url=generated_cdn_url)


class ImageGalleryCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    category_image = models.ImageField(upload_to='image_gallery/categories/', max_length=500)
    category_description = models.TextField(blank=True)
    router_path = models.CharField(max_length=255, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category_name']
        verbose_name = 'Image Gallery Category'
        verbose_name_plural = 'Image Gallery Categories'

    def __str__(self):
        return self.category_name


@receiver(post_delete, sender=ImageGallery)
def auto_delete_image_gallery_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if not ImageGallery.objects.filter(image=instance.image.name).exclude(pk=instance.pk).exists():
            if instance.image.storage.exists(instance.image.name):
                instance.image.storage.delete(instance.image.name)


@receiver(pre_save, sender=ImageGallery)
def auto_delete_image_gallery_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_instance = ImageGallery.objects.get(pk=instance.pk)
    except ImageGallery.DoesNotExist:
        return False

    old_file = old_instance.image
    new_file = instance.image

    if old_file and old_file != new_file:
        if not ImageGallery.objects.filter(image=old_file.name).exclude(pk=instance.pk).exists():
            if old_file.storage.exists(old_file.name):
                old_file.storage.delete(old_file.name)


@receiver(post_delete, sender=ImageGalleryCategory)
def auto_delete_category_file_on_delete(sender, instance, **kwargs):
    if instance.category_image:
        if not ImageGalleryCategory.objects.filter(category_image=instance.category_image.name).exclude(pk=instance.pk).exists():
            if instance.category_image.storage.exists(instance.category_image.name):
                instance.category_image.storage.delete(instance.category_image.name)


@receiver(pre_save, sender=ImageGalleryCategory)
def auto_delete_category_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_instance = ImageGalleryCategory.objects.get(pk=instance.pk)
    except ImageGalleryCategory.DoesNotExist:
        return False

    old_file = old_instance.category_image
    new_file = instance.category_image

    if old_file and old_file != new_file:
        if not ImageGalleryCategory.objects.filter(category_image=old_file.name).exclude(pk=instance.pk).exists():
            if old_file.storage.exists(old_file.name):
                old_file.storage.delete(old_file.name)

