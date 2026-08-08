from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils.html import format_html
from django.conf import settings
from .models import Kirtan, KirtanCategory, KirtanTranslation, KirtanCategoryTranslation


# ---------------------------------------------------------------------------
# Custom widget – shows an HTML5 <audio> player beneath the file-upload input
# ---------------------------------------------------------------------------

class AudioPlayerWidget(forms.ClearableFileInput):
    """
    Extends Django's ClearableFileInput so that, when the field already has a
    value, an <audio> player is rendered directly in the admin change-form –
    no page navigation required.
    """

    def render(self, name, value, attrs=None, renderer=None):
        # Render the standard file-input first (includes "Currently: …" link
        # and the "Clear" checkbox that Django adds automatically).
        output = super().render(name, value, attrs=attrs, renderer=renderer)

        # If there is a current file, append a styled audio player.
        if value and hasattr(value, 'url'):
            audio_url = value.url
            # Prepend the public base URL when the stored URL is relative
            if audio_url.startswith('/media/'):
                public_base = getattr(
                    settings, 'PUBLIC_MEDIA_BASE_URL', ''
                ).rstrip('/')
                audio_url = f"{public_base}{audio_url}"

            output += format_html(
                '''
                <div style="
                    margin-top: 14px;
                    padding: 14px 18px;
                    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
                    border-radius: 12px;
                    border: 1px solid rgba(255,165,0,0.40);
                    box-shadow: 0 4px 20px rgba(0,0,0,0.45);
                    display: inline-flex;
                    align-items: center;
                    gap: 12px;
                    min-width: 360px;
                    max-width: 580px;
                ">
                    <span style="font-size:22px;filter:drop-shadow(0 0 6px rgba(255,165,0,0.8));">&#127925;</span>
                    <div style="flex:1;">
                        <p style="margin:0 0 6px;font-size:11px;color:#ff9800;font-weight:600;letter-spacing:0.5px;text-transform:uppercase;">
                            Audio Preview
                        </p>
                        <audio controls preload="none"
                               style="width:100%;height:36px;border-radius:8px;accent-color:#ff9800;">
                            <source src="{}" type="audio/mpeg">
                            <source src="{}" type="audio/ogg">
                            <source src="{}" type="audio/wav">
                            Your browser does not support the audio element.
                        </audio>
                    </div>
                </div>
                ''',
                audio_url, audio_url, audio_url,
            )

        return output


# ---------------------------------------------------------------------------
# Admin form that wires up the custom widget for audioPath
# ---------------------------------------------------------------------------

class KirtanAdminForm(forms.ModelForm):
    class Meta:
        model = Kirtan
        fields = '__all__'
        widgets = {
            'audioPath': AudioPlayerWidget,
        }


# ---------------------------------------------------------------------------
# Inline forms
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# ModelAdmin registrations
# ---------------------------------------------------------------------------

@admin.register(KirtanCategory)
class KirtanCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'categoryImage', 'created_at', 'updated_at')
    search_fields = ('name',)
    inlines = [KirtanCategoryTranslationInline]
    readonly_fields = ('created_at', 'updated_at')
    fields = ('name', 'categoryImage', 'created_at', 'updated_at')
    ordering = ('name',)


class KirtanLanguageFilter(admin.SimpleListFilter):
    title = 'Language'
    parameter_name = 'language'

    def lookups(self, request, queryset):
        from .models import LANGUAGE_CHOICES
        return LANGUAGE_CHOICES

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(translations__language_code=self.value()).distinct()
        return queryset


@admin.register(Kirtan)
class KirtanAdmin(admin.ModelAdmin):
    form = KirtanAdminForm
    list_display = (
        'get_title',
        'category',
        'id',
        'order',
    )
    list_filter = ('category', KirtanLanguageFilter, 'created_at')
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

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        self._current_request = request
        return qs

    def get_title(self, obj):
        request = getattr(self, '_current_request', None)
        selected_lang = request.GET.get('language') if request else None

        if selected_lang:
            trans = obj.translations.filter(language_code=selected_lang).first()
            if trans and trans.title:
                return trans.title

        trans = obj.translations.filter(language_code='en').first()
        if not trans:
            trans = obj.translations.first()
        return trans.title if trans else f"Kirtan {obj.id}"
    get_title.short_description = 'Title'
    get_title.admin_order_field = 'translations__title'

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
