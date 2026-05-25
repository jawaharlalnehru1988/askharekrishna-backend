from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.db import transaction
from .models import Kirtan, KirtanCategory, KirtanTranslation, KirtanCategoryTranslation


class KirtanTranslationInlineForm(forms.ModelForm):
    class Meta:
        model = KirtanTranslation
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'maxlength': 300}),
        }

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        if len(description) > 300:
            raise ValidationError('Description must be at most 300 characters.')
        return description


class KirtanTranslationInline(admin.TabularInline):
    model = KirtanTranslation
    form = KirtanTranslationInlineForm
    extra = 1


class KirtanCategoryTranslationInline(admin.TabularInline):
    model = KirtanCategoryTranslation
    extra = 1


@admin.register(KirtanCategory)
class KirtanCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'categoryImage', 'created_at', 'updated_at')
    search_fields = ('name',)
    inlines = [KirtanCategoryTranslationInline]
    readonly_fields = ('created_at', 'updated_at')
    fields = ('name', 'categoryImage', 'created_at', 'updated_at')
    ordering = ('name',)


@admin.register(Kirtan)
class KirtanAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_title',
        'category',
        'order',
        'created_at',
        'updated_at'
    )
    list_filter = ('category', 'created_at')
    search_fields = ('translations__title', 'translations__authorName', 'category__name')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [KirtanTranslationInline]
    actions = ['duplicate_selected_kirtans']
    save_as = True
    fieldsets = (
        ('Basic Information', {
            'fields': ('category', 'order')
        }),
        ('Media', {
            'fields': ('audioPath', 'imagePath', 'videoPath')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    ordering = ['order', '-created_at']

    def get_title(self, obj):
        trans = obj.translations.filter(language_code='en').first()
        if not trans:
            trans = obj.translations.first()
        return trans.title if trans else f"Kirtan {obj.id}"
    get_title.short_description = 'Title'

    @admin.action(description='Duplicate selected kirtans')
    def duplicate_selected_kirtans(self, request, queryset):
        duplicated_count = 0

        for kirtan in queryset.prefetch_related('translations'):
            with transaction.atomic():
                duplicated = Kirtan.objects.create(
                    category=kirtan.category,
                    audioPath=kirtan.audioPath,
                    imagePath=kirtan.imagePath,
                    videoPath=kirtan.videoPath,
                    order=kirtan.order,
                )

                KirtanTranslation.objects.bulk_create([
                    KirtanTranslation(
                        kirtan=duplicated,
                        language_code=translation.language_code,
                        title=translation.title,
                        authorName=translation.authorName,
                        description=translation.description,
                        lyrics=translation.lyrics,
                    )
                    for translation in kirtan.translations.all()
                ])

            duplicated_count += 1

        self.message_user(request, f'{duplicated_count} kirtan(s) duplicated successfully.')
