from django import forms
from django.contrib import admin
from .models import ImageGallery, ImageGalleryCategory


class ImageGalleryAdminForm(forms.ModelForm):
    category = forms.ChoiceField(required=False)

    class Meta:
        model = ImageGallery
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        category_names = list(
            ImageGalleryCategory.objects.order_by('category_name').values_list('category_name', flat=True)
        )
        choices = [('', '---------')] + [(name, name) for name in category_names]

        current_value = getattr(self.instance, 'category', '') if self.instance else ''
        if current_value and current_value not in category_names:
            choices.append((current_value, current_value))

        self.fields['category'].choices = choices


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    form = ImageGalleryAdminForm
    list_display = ('id', 'image', 'cdn_url', 'category', 'note', 'created_at')
    search_fields = ('category', 'note')
    list_filter = ('category', 'created_at')
    readonly_fields = ('cdn_url', 'created_at', 'updated_at')


@admin.register(ImageGalleryCategory)
class ImageGalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'router_path', 'created_at')
    search_fields = ('category_name', 'category_description', 'router_path')
    readonly_fields = ('created_at', 'updated_at')
