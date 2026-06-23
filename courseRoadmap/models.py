from django.db import models

class Roadmap(models.Model):
    mainTopic = models.CharField(max_length=255)
    routerLink = models.CharField(max_length=255, unique=True)
    intro = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mainTopic

class RoadmapChapter(models.Model):
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE, related_name='chapters')
    chapterName = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.chapterName

class RoadmapSubtopic(models.Model):
    chapter = models.ForeignKey(RoadmapChapter, on_delete=models.CASCADE, related_name='subtopics')
    subtopicName = models.CharField(max_length=1000)
    explanation = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subtopicName

class RoadmapSubtopicQuestion(models.Model):
    subtopic = models.ForeignKey(RoadmapSubtopic, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=1000)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RoadmapSubtopicOption(models.Model):
    question = models.ForeignKey(RoadmapSubtopicQuestion, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=1000)
    order = models.PositiveIntegerField(default=0)
    is_correct = models.BooleanField(default=False)
