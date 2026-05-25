from django.contrib import admin
from .models import Audio

@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('id','title','language','duration','audioListId','isPlaying','created_at')
    search_fields = ('title','description','language')
    list_filter = ('language','isPlaying')
