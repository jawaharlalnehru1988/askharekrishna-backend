from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models import Q
from django.db import transaction


class StoryMainTopic(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    description = models.CharField(max_length=200, blank=True, default='')
    image = models.ImageField(upload_to='stories/main-topic/', max_length=500, blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Story Main Topic'
        verbose_name_plural = 'Story Main Topics'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        old_image_name = None
        if self.pk:
            old_image_name = StoryMainTopic.objects.filter(pk=self.pk).values_list('image', flat=True).first()

        super().save(*args, **kwargs)

        new_image_name = self.image.name if self.image else None
        if old_image_name and new_image_name and old_image_name != new_image_name:
            storage = StoryMainTopic._meta.get_field('image').storage
            if storage.exists(old_image_name):
                storage.delete(old_image_name)


class Story(models.Model):
    mainTopic = models.ForeignKey(
        StoryMainTopic,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='stories',
    )
    subTopic = models.CharField(max_length=255)
    article = models.TextField()
    slug = models.SlugField(max_length=280, unique=True, blank=True, allow_unicode=True)
    order = models.PositiveIntegerField(default=0)
    language = models.CharField(max_length=10, default='en', db_index=True)
    source_story = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='translations',
    )
    audioPath = models.FileField(upload_to='stories/audio/', max_length=500, blank=True, null=True)
    imagePath = models.ImageField(upload_to='stories/images/', max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'mainTopic__name', 'subTopic']
        indexes = [
            models.Index(fields=['mainTopic', 'language', 'order'], name='story_topic_lang_ord_idx'),
            models.Index(fields=['mainTopic', 'id'], name='story_topic_id_idx'),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['source_story', 'language'],
                condition=Q(source_story__isnull=False),
                name='uq_story_source_language',
            ),
        ]
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'

    def __str__(self):
        return f"[{self.language.upper()}] {self.mainTopic} - {self.subTopic}"

    def effective_image_path(self):
        if self.imagePath:
            return self.imagePath
        if self.source_story and self.source_story.imagePath:
            return self.source_story.imagePath
        return None

    @staticmethod
    def _resolve_root_story_id(source_story_id, story_id=None):
        root_id = source_story_id or story_id
        while root_id:
            parent_id = Story.objects.filter(pk=root_id).values_list('source_story_id', flat=True).first()
            if not parent_id:
                break
            root_id = parent_id
        return root_id

    @staticmethod
    def _collect_family_ids(root_id):
        if not root_id:
            return set()

        family_ids = {root_id}
        frontier = {root_id}

        while frontier:
            child_ids = set(
                Story.objects.filter(source_story_id__in=frontier).values_list('id', flat=True)
            )
            child_ids -= family_ids
            if not child_ids:
                break
            family_ids |= child_ids
            frontier = child_ids

        return family_ids

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.mainTopic} {self.subTopic}", allow_unicode=True)[:280] or "story"
            slug = base_slug
            counter = 1

            while Story.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                suffix = f"-{counter}"
                slug = f"{base_slug[:280 - len(suffix)]}{suffix}"
                counter += 1

            self.slug = slug

        root_id_before_save = self._resolve_root_story_id(self.source_story_id, self.pk)
        family_ids_before_save = self._collect_family_ids(root_id_before_save)
        old_image_names = set()
        if family_ids_before_save:
            old_image_names = {
                name
                for name in Story.objects.filter(pk__in=family_ids_before_save).values_list('imagePath', flat=True)
                if name
            }

        with transaction.atomic():
            super().save(*args, **kwargs)

            new_image_name = self.imagePath.name if self.imagePath else None
            if not new_image_name:
                return

            root_id_after_save = self._resolve_root_story_id(self.source_story_id, self.pk)
            family_ids_after_save = self._collect_family_ids(root_id_after_save)
            if not family_ids_after_save:
                return

            Story.objects.filter(pk__in=family_ids_after_save).exclude(pk=self.pk).update(imagePath=new_image_name)

        storage = Story._meta.get_field('imagePath').storage
        deletable_image_names = {
            name for name in old_image_names if name and name != new_image_name
        }
        for old_name in deletable_image_names:
            if Story.objects.filter(imagePath=old_name).exists():
                continue
            if storage.exists(old_name):
                storage.delete(old_name)


class StoryQuestion(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['story_id', 'order', 'id']
        constraints = [
            models.UniqueConstraint(fields=['story', 'order'], name='uq_story_question_order'),
        ]
        verbose_name = 'Story MCQ Question'
        verbose_name_plural = 'Story MCQ Questions'

    def __str__(self):
        return f"{self.story_id} - Q{self.order}"

    def clean(self):
        super().clean()
        existing_count = self.story.questions.exclude(pk=self.pk).count() if self.story_id else 0
        if existing_count >= 10:
            raise ValidationError('A story can have a maximum of 10 MCQ questions.')


class StoryQuestionOption(models.Model):
    question = models.ForeignKey(StoryQuestion, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=500)
    order = models.PositiveSmallIntegerField(default=1)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['question_id', 'order', 'id']
        constraints = [
            models.UniqueConstraint(fields=['question', 'order'], name='uq_story_option_order'),
        ]
        verbose_name = 'Story MCQ Option'
        verbose_name_plural = 'Story MCQ Options'

    def __str__(self):
        return f"Q{self.question.order} - Option {self.order}"

    def clean(self):
        super().clean()
        existing_count = self.question.options.exclude(pk=self.pk).count() if self.question_id else 0
        if existing_count >= 4:
            raise ValidationError('A question can have a maximum of 4 options.')
