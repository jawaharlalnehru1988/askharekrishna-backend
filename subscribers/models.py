from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, unique=True)
    language = models.CharField(max_length=80)
    place = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['phone_number'], name='subscriber_phone_idx'),
            models.Index(fields=['language'], name='subscriber_language_idx'),
        ]
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return f"{self.name} ({self.phone_number})"


class SubscriberQuizAttempt(models.Model):
    QUIZ_TYPE_CHOICES = [
        ('pooja_vidhi', 'Pooja Vidhi'),
        ('story', 'Story'),
    ]

    subscriber = models.ForeignKey(
        Subscriber,
        on_delete=models.CASCADE,
        related_name='quiz_attempts',
    )
    article_id = models.PositiveIntegerField()
    article_title = models.CharField(max_length=255)
    quiz_type = models.CharField(max_length=32, choices=QUIZ_TYPE_CHOICES, default='pooja_vidhi')
    score = models.PositiveIntegerField()
    total_questions = models.PositiveIntegerField()
    attempt_number = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['subscriber', 'quiz_type', 'article_id'], name='quiz_attempt_lookup_idx'),
            models.Index(fields=['created_at'], name='quiz_attempt_created_idx'),
        ]
        verbose_name = 'Subscriber Quiz Attempt'
        verbose_name_plural = 'Subscriber Quiz Attempts'

    def __str__(self):
        return f"{self.subscriber.phone_number} | {self.quiz_type} | {self.article_title} | {self.score}/{self.total_questions}"
