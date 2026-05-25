from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


class Category(models.Model):
    order = models.PositiveIntegerField(default=0, db_index=True)
    name = models.CharField(max_length=255, unique=True)
    colorCode = models.CharField(max_length=7, default='#000000')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class CarnaticQuestion(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='questions', blank=True, null=True)
    question = models.TextField()
    answer = models.TextField()
    audio = models.FileField(upload_to='carnatic_questions/audio/', max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Carnatic Question'
        verbose_name_plural = 'Carnatic Questions'

    def __str__(self):
        return self.question[:60]


class CarnaticSyllabus(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='syllabus_items', blank=True, null=True)
    topic = models.CharField(max_length=255)
    lesson = models.TextField()
    audioPath = models.FileField(upload_to='carnatic_syllabus/audio/', max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category__name', 'topic', 'lesson']
        verbose_name = 'Carnatic Syllabus'
        verbose_name_plural = 'Carnatic Syllabus'

    def __str__(self):
        return self.topic


class CarnaticSyllabusVideoSample(models.Model):
    syllabus = models.ForeignKey(CarnaticSyllabus, on_delete=models.CASCADE, related_name='video_samples')
    url = models.URLField(max_length=500)
    sort_order = models.PositiveIntegerField(default=0, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Carnatic Syllabus Video Sample'
        verbose_name_plural = 'Carnatic Syllabus Video Samples'

    def __str__(self):
        return f"Video sample for {self.syllabus.topic}"


class CarnaticKacheri(models.Model):
    title = models.CharField(max_length=255)
    singer = models.CharField(max_length=255)
    ragam = models.CharField(max_length=255)
    videoUrl = models.URLField(max_length=500)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title', 'singer', 'ragam', '-created_at']
        verbose_name = 'Carnatic Kacheri'
        verbose_name_plural = 'Carnatic Kacheri'

    def __str__(self):
        return self.title


class CarnaticClassAudio(models.Model):
    title = models.CharField(max_length=255)
    audioPath = models.FileField(upload_to='carnatic_class_audios/', max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', 'title']
        verbose_name = 'Carnatic Class Audio'
        verbose_name_plural = 'Carnatic Class Audios'

    def __str__(self):
        return self.title


class CarnaticLessonPractice(models.Model):
    PRACTICE_CATEGORY_CHOICES = [
        ("Sarali Varisaigal", "Sarali Varisaigal"),
        ("Jantai Varisaigal", "Jantai Varisaigal"),
        ("Dhattu Varisaigal", "Dhattu Varisaigal"),
        ("Mel Sthayi Varisaigal", "Mel Sthayi Varisaigal"),
        ("Keezh Sthayi Varisaigal", "Keezh Sthayi Varisaigal"),
        ("Alankaarams", "Alankaarams"),
        ("Gitam Lessons", "Gitam Lessons"),
    ]
    PracticeCategory = models.CharField(
        max_length=50,
        choices=PRACTICE_CATEGORY_CHOICES,
        default="Sarali Varisaigal",
    )
    lessonName = models.CharField(max_length=255)
    audioPath = models.FileField(upload_to='carnatic_lesson_practice/', max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', 'PracticeCategory', 'lessonName']
        verbose_name = 'Carnatic Lesson Practice'
        verbose_name_plural = 'Carnatic Lesson Practices'

    def __str__(self):
        return f"{self.PracticeCategory} - {self.lessonName}"


@receiver(post_delete, sender=CarnaticQuestion)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.audio:
        if not CarnaticQuestion.objects.filter(audio=instance.audio.name).exclude(pk=instance.pk).exists():
            if instance.audio.storage.exists(instance.audio.name):
                instance.audio.storage.delete(instance.audio.name)


@receiver(pre_save, sender=CarnaticQuestion)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_instance = CarnaticQuestion.objects.get(pk=instance.pk)
    except CarnaticQuestion.DoesNotExist:
        return False

    old_file = old_instance.audio
    new_file = instance.audio

    if old_file and old_file != new_file:
        if not CarnaticQuestion.objects.filter(audio=old_file.name).exclude(pk=instance.pk).exists():
            if old_file.storage.exists(old_file.name):
                old_file.storage.delete(old_file.name)


@receiver(post_delete, sender=CarnaticSyllabus)
def auto_delete_syllabus_file_on_delete(sender, instance, **kwargs):
    if instance.audioPath:
        if not CarnaticSyllabus.objects.filter(audioPath=instance.audioPath.name).exclude(pk=instance.pk).exists():
            if instance.audioPath.storage.exists(instance.audioPath.name):
                instance.audioPath.storage.delete(instance.audioPath.name)


@receiver(pre_save, sender=CarnaticSyllabus)
def auto_delete_syllabus_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_instance = CarnaticSyllabus.objects.get(pk=instance.pk)
    except CarnaticSyllabus.DoesNotExist:
        return False

    old_audio = old_instance.audioPath
    new_audio = instance.audioPath

    if old_audio and old_audio != new_audio:
        if not CarnaticSyllabus.objects.filter(audioPath=old_audio.name).exclude(pk=instance.pk).exists():
            if old_audio.storage.exists(old_audio.name):
                old_audio.storage.delete(old_audio.name)


