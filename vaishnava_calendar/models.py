from django.db import models
from django.utils import timezone


LANGUAGE_CHOICES = [
    ('en', 'English'),
    ('ta', 'Tamil'),
    ('kn', 'Kannada'),
    ('te', 'Telugu'),
    ('hi', 'Hindi'),
    ('ml', 'Malayalam'),
    ('bn', 'Bengali'),
]


class CalendarDay(models.Model):
    event_date = models.DateField(unique=True, db_index=True, help_text="Date of the calendar day (YYYY-MM-DD)")
    day_of_week = models.CharField(max_length=20, help_text="Day of the week (e.g., Thursday)")
    is_ekadashi = models.BooleanField(default=False, help_text="Whether this day is an Ekadashi")
    ekadashi_name = models.CharField(max_length=150, blank=True, null=True, help_text="Name of Ekadashi if applicable")
    is_fast_day = models.BooleanField(default=False, help_text="Whether fasting is required on this day")
    fast_details = models.TextField(blank=True, null=True, help_text="Specific fasting details or instructions")
    break_fast_start = models.DateTimeField(blank=True, null=True, help_text="Break fast (Parana) start datetime")
    break_fast_end = models.DateTimeField(blank=True, null=True, help_text="Break fast (Parana) end datetime")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['event_date']
        verbose_name = 'Calendar Day'
        verbose_name_plural = 'Calendar Days'

    def __str__(self):
        title = self.ekadashi_name if self.is_ekadashi and self.ekadashi_name else f"{self.event_date} ({self.day_of_week})"
        return f"{self.event_date} - {title}"

    @property
    def break_fast_window_display(self):
        if self.break_fast_start and self.break_fast_end:
            import zoneinfo
            tz = zoneinfo.ZoneInfo("Asia/Kolkata")
            start_str = self.break_fast_start.astimezone(tz).strftime("%H:%M")
            end_str = self.break_fast_end.astimezone(tz).strftime("%H:%M")
            return f"{start_str} - {end_str}"
        return None


class CalendarObservance(models.Model):
    CATEGORY_CHOICES = [
        ('Ekadashi', 'Ekadashi'),
        ('Parana', 'Parana'),
        ('Appearance', 'Appearance / Disappearance'),
        ('Festival', 'Festival'),
        ('Fasting', 'Fasting Note'),
        ('Observance', 'General Observance'),
    ]

    day = models.ForeignKey(CalendarDay, on_delete=models.CASCADE, related_name='observances')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Observance')
    image = models.ImageField(upload_to='vaishnava_calendar/images/', max_length=500, blank=True, null=True, help_text="Common image for all languages")
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Calendar Observance'
        verbose_name_plural = 'Calendar Observances'

    def get_translation(self, lang_code='en'):
        trans = self.translations.filter(language_code=lang_code).first()
        if not trans:
            trans = self.translations.filter(language_code='en').first()
        if not trans:
            trans = self.translations.first()
        return trans

    @property
    def title(self):
        trans = self.get_translation('en')
        return trans.title if trans else f"Observance {self.id}"

    def __str__(self):
        return f"{self.title} ({self.category})"


class CalendarObservanceTranslation(models.Model):
    observance = models.ForeignKey(
        CalendarObservance,
        on_delete=models.CASCADE,
        related_name='translations',
    )
    language_code = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        default='en',
        help_text="Language of this translation"
    )
    title = models.CharField(max_length=255, help_text="Title in specific language")
    description = models.TextField(blank=True, null=True, help_text="Optional description or details")
    audio_file = models.FileField(upload_to='vaishnava_calendar/audios/', max_length=500, blank=True, null=True, help_text="Language-specific audio file")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['language_code', 'id']
        unique_together = ('observance', 'language_code')
        verbose_name = 'Observance Translation'
        verbose_name_plural = 'Observance Translations'

    def __str__(self):
        return f"[{self.language_code.upper()}] {self.title}"
