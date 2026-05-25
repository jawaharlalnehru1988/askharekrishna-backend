from django.contrib import admin
from .models import OurOtherSite


@admin.register(OurOtherSite)
class OurOtherSiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'web_url', 'created_at', 'updated_at')
    search_fields = ('web_url', 'purpose', 'features_available')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
