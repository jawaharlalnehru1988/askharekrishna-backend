from django.contrib import admin
from .models import Subscriber, SubscriberQuizAttempt


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'language', 'place', 'is_active', 'created_at')
    list_filter = ('is_active', 'language', 'place')
    search_fields = ('name', 'phone_number', 'language', 'place')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(SubscriberQuizAttempt)
class SubscriberQuizAttemptAdmin(admin.ModelAdmin):
    list_display = (
        'subscriber',
        'quiz_type',
        'article_id',
        'article_title',
        'score',
        'total_questions',
        'attempt_number',
        'created_at',
    )
    list_filter = ('quiz_type', 'created_at')
    search_fields = ('subscriber__phone_number', 'subscriber__name', 'article_title')
    readonly_fields = ('created_at',)
