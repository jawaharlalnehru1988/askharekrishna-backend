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
    orderNumber = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Order Number")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='lesson_practices',
        blank=True,
        null=True,
        verbose_name="Practice Category",
    )
    lessonName = models.CharField(max_length=255)
    swarams = models.TextField(blank=True, default='', verbose_name="Swarams")
    audioPath = models.FileField(upload_to='carnatic_lesson_practice/', max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['orderNumber', 'id']
        verbose_name = 'Carnatic Lesson Practice'
        verbose_name_plural = 'Carnatic Lesson Practices'

    @property
    def PracticeCategory(self):
        return self.category.name if self.category else ""

    def __str__(self):
        cat_name = self.category.name if self.category else "No Category"
        return f"{cat_name} - {self.lessonName}"


class CarnaticLessonPracticeAudio(models.Model):
    lesson_practice = models.ForeignKey(
        CarnaticLessonPractice,
        on_delete=models.CASCADE,
        related_name='audios',
        verbose_name='Lesson Practice',
    )
    audioPathName = models.CharField(max_length=255, blank=True, verbose_name='Audio Path Name')
    audioPath = models.FileField(
        upload_to='carnatic_lesson_practice/audio/',
        max_length=500,
        verbose_name='Audio Path',
    )
    sort_order = models.PositiveIntegerField(default=0, db_index=True, verbose_name='Sort Order')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Carnatic Lesson Practice Audio'
        verbose_name_plural = 'Carnatic Lesson Practice Audios'

    def __str__(self):
        return f"{self.audioPathName or 'Audio'} ({self.lesson_practice})"


class CarnaticLessonPracticeVideo(models.Model):
    lesson_practice = models.ForeignKey(
        CarnaticLessonPractice,
        on_delete=models.CASCADE,
        related_name='videos',
        verbose_name='Lesson Practice',
    )
    youtubevideoUrl = models.URLField(max_length=500, verbose_name='YouTube Video URL')
    sort_order = models.PositiveIntegerField(default=0, db_index=True, verbose_name='Sort Order')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Carnatic Lesson Practice Video'
        verbose_name_plural = 'Carnatic Lesson Practice Videos'

    def __str__(self):
        return f"Video for {self.lesson_practice}"


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


@receiver(post_delete, sender=CarnaticLessonPracticeAudio)
def auto_delete_lesson_practice_audio_on_delete(sender, instance, **kwargs):
    if instance.audioPath:
        if not CarnaticLessonPracticeAudio.objects.filter(audioPath=instance.audioPath.name).exclude(pk=instance.pk).exists():
            if instance.audioPath.storage.exists(instance.audioPath.name):
                instance.audioPath.storage.delete(instance.audioPath.name)


@receiver(pre_save, sender=CarnaticLessonPracticeAudio)
def auto_delete_lesson_practice_audio_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_instance = CarnaticLessonPracticeAudio.objects.get(pk=instance.pk)
    except CarnaticLessonPracticeAudio.DoesNotExist:
        return False

    old_audio = old_instance.audioPath
    new_audio = instance.audioPath

    if old_audio and old_audio != new_audio:
        if not CarnaticLessonPracticeAudio.objects.filter(audioPath=old_audio.name).exclude(pk=instance.pk).exists():
            if old_audio.storage.exists(old_audio.name):
                old_audio.storage.delete(old_audio.name)


class RagamLesson(models.Model):
    raga_name = models.CharField(max_length=255, verbose_name="Raga Name")
    swarasthanas = models.TextField(blank=True, verbose_name="Swarasthanas")
    arohanam_avarohanam = models.TextField(blank=True, verbose_name="Arohanam & Avarohanam")
    description = models.TextField(blank=True, verbose_name="Description (Raga Lakshanas)")
    famousCompositions = models.TextField(blank=True, verbose_name="Famous Compositions")
    melakarthaNumber = models.PositiveIntegerField(null=True, blank=True, verbose_name="Melakarta Number")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['melakarthaNumber', 'raga_name']
        verbose_name = 'Ragam Lesson'
        verbose_name_plural = 'Ragam Lessons'

    def __str__(self):
        if self.melakarthaNumber:
            return f"Mela {self.melakarthaNumber}: {self.raga_name}"
        return self.raga_name


class RagamLessonAudio(models.Model):
    ragam_lesson = models.ForeignKey(
        RagamLesson,
        on_delete=models.CASCADE,
        related_name='audios',
        verbose_name='Ragam Lesson',
    )
    songName = models.CharField(max_length=255, verbose_name="Song Name")
    audioPath = models.FileField(
        upload_to='carnatic_ragam_lessons/audio/',
        max_length=500,
        verbose_name="Audio File",
    )
    sort_order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Sort Order")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Ragam Lesson Audio'
        verbose_name_plural = 'Ragam Lesson Audios'

    def __str__(self):
        return f"{self.songName} ({self.ragam_lesson.raga_name})"


class RagamLessonVideo(models.Model):
    ragam_lesson = models.ForeignKey(
        RagamLesson,
        on_delete=models.CASCADE,
        related_name='videos',
        verbose_name='Ragam Lesson',
    )
    title = models.CharField(max_length=255, blank=True, default='', verbose_name="Song / Video Title")
    youtubevideoUrl = models.URLField(max_length=500, verbose_name="YouTube Video URL")
    sort_order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Sort Order")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Ragam Lesson Video'
        verbose_name_plural = 'Ragam Lesson Videos'

    def __str__(self):
        if self.title:
            return f"{self.title} ({self.ragam_lesson.raga_name})"
        return f"Video for {self.ragam_lesson.raga_name}"


@receiver(post_delete, sender=RagamLessonAudio)
def auto_delete_ragam_audio_on_delete(sender, instance, **kwargs):
    if instance.audioPath:
        if not RagamLessonAudio.objects.filter(audioPath=instance.audioPath.name).exclude(pk=instance.pk).exists():
            if instance.audioPath.storage.exists(instance.audioPath.name):
                instance.audioPath.storage.delete(instance.audioPath.name)


@receiver(pre_save, sender=RagamLessonAudio)
def auto_delete_ragam_audio_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_instance = RagamLessonAudio.objects.get(pk=instance.pk)
    except RagamLessonAudio.DoesNotExist:
        return False

    old_audio = old_instance.audioPath
    new_audio = instance.audioPath

    if old_audio and old_audio != new_audio:
        if not RagamLessonAudio.objects.filter(audioPath=old_audio.name).exclude(pk=instance.pk).exists():
            if old_audio.storage.exists(old_audio.name):
                old_audio.storage.delete(old_audio.name)


class MridangaLesson(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('medium', 'Medium'),
        ('advanced', 'Advanced'),
    ]

    TALA_CATEGORY_CHOICES = [
        ('daspahira', 'Daspahira'),
        ('kaharba', 'Kaharba'),
        ('dadra', 'Dadra'),
        ('lofa', 'Lofa'),
        ('rupak', 'Rupak'),
        ('jhap', 'Jhap'),
        ('teen', 'Teen'),
        ('matan', 'Matan'),
        ('rela', 'Rela'),
        ('duggi', 'Duggi Style'),
    ]

    tala_name = models.CharField(max_length=255, verbose_name="Tala Name")
    tala_category = models.CharField(
        max_length=50,
        choices=TALA_CATEGORY_CHOICES,
        default='daspahira',
        db_index=True,
        verbose_name="Tala Category",
    )
    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default='beginner',
        db_index=True,
        verbose_name="Level",
    )
    matras = models.PositiveIntegerField(null=True, blank=True, verbose_name="Matras (Beats)")
    mantras_and_notes = models.TextField(blank=True, verbose_name="Mantras and Notes")
    description = models.TextField(blank=True, verbose_name="Description")
    sort_order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Sort Order")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', 'tala_category', 'level', 'matras', 'tala_name']
        verbose_name = 'Mridanga Lesson'
        verbose_name_plural = 'Mridanga Lessons'

    def __str__(self):
        if self.matras:
            return f"{self.tala_name} ({self.matras} Matras)"
        return self.tala_name


class MridangaLessonAudio(models.Model):
    mridanga_lesson = models.ForeignKey(
        MridangaLesson,
        on_delete=models.CASCADE,
        related_name='audios',
        verbose_name='Mridanga Lesson',
    )
    songName = models.CharField(max_length=255, verbose_name="Audio Title / Song Name")
    audioPath = models.FileField(
        upload_to='carnatic_mridanga_lessons/audio/',
        max_length=500,
        verbose_name="Audio File",
    )
    mantras_and_notes = models.TextField(blank=True, default='', verbose_name="Mantras and Notes")
    sort_order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Sort Order")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Mridanga Lesson Audio'
        verbose_name_plural = 'Mridanga Lesson Audios'

    def __str__(self):
        return f"{self.songName} ({self.mridanga_lesson.tala_name})"


class MridangaLessonVideo(models.Model):
    mridanga_lesson = models.ForeignKey(
        MridangaLesson,
        on_delete=models.CASCADE,
        related_name='videos',
        verbose_name='Mridanga Lesson',
    )
    title = models.CharField(max_length=255, blank=True, default='', verbose_name="Video Title")
    youtubevideoUrl = models.URLField(max_length=500, verbose_name="YouTube Video URL")
    mantras_and_notes = models.TextField(blank=True, default='', verbose_name="Mantras and Notes")
    sort_order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Sort Order")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Mridanga Lesson Video'
        verbose_name_plural = 'Mridanga Lesson Videos'

    def __str__(self):
        if self.title:
            return f"{self.title} ({self.mridanga_lesson.tala_name})"
        return f"Video for {self.mridanga_lesson.tala_name}"


class MridangaLessonKirtanDemo(models.Model):
    mridanga_lesson = models.ForeignKey(
        MridangaLesson,
        on_delete=models.CASCADE,
        related_name='kirtan_demos',
        verbose_name='Mridanga Lesson',
    )
    title = models.CharField(max_length=255, blank=True, default='', verbose_name="Kirtan Demo Title")
    youtubevideoUrl = models.URLField(max_length=500, verbose_name="YouTube Video URL")
    mantras_and_notes = models.TextField(blank=True, default='', verbose_name="Mantras and Notes")
    sort_order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Sort Order")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Mridanga Lesson Kirtan Demo'
        verbose_name_plural = 'Mridanga Lesson Kirtan Demos'

    def __str__(self):
        if self.title:
            return f"{self.title} ({self.mridanga_lesson.tala_name})"
        return f"Kirtan Demo for {self.mridanga_lesson.tala_name}"


@receiver(post_delete, sender=MridangaLessonAudio)
def auto_delete_mridanga_audio_on_delete(sender, instance, **kwargs):
    if instance.audioPath:
        if not MridangaLessonAudio.objects.filter(audioPath=instance.audioPath.name).exclude(pk=instance.pk).exists():
            if instance.audioPath.storage.exists(instance.audioPath.name):
                instance.audioPath.storage.delete(instance.audioPath.name)


@receiver(pre_save, sender=MridangaLessonAudio)
def auto_delete_mridanga_audio_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_instance = MridangaLessonAudio.objects.get(pk=instance.pk)
    except MridangaLessonAudio.DoesNotExist:
        return False

    old_audio = old_instance.audioPath
    new_audio = instance.audioPath

    if old_audio and old_audio != new_audio:
        if not MridangaLessonAudio.objects.filter(audioPath=old_audio.name).exclude(pk=instance.pk).exists():
            if old_audio.storage.exists(old_audio.name):
                old_audio.storage.delete(old_audio.name)





