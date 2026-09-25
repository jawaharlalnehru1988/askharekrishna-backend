from django.contrib import admin
# KirtanTutorial is no longer needed in Django admin
# from .models import KirtanTutorial
#
# @admin.register(KirtanTutorial)
# class KirtanTutorialAdmin(admin.ModelAdmin):
#     list_display = ('mainTopic', 'subTopic', 'language', 'order', 'slug', 'audioPath', 'created_at')
#     list_filter = ('language', 'mainTopic', 'subTopic')
#     search_fields = ('mainTopic', 'subTopic', 'article')
#     fields = ('language', 'mainTopic', 'subTopic', 'article', 'slug', 'order', 'audioPath')
#     prepopulated_fields = {'slug': ('mainTopic', 'subTopic')}
#     ordering = ('order', 'mainTopic', 'subTopic')
