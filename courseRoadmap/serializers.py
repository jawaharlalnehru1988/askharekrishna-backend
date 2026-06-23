from rest_framework import serializers
from .models import Roadmap, RoadmapChapter, RoadmapSubtopic, RoadmapSubtopicQuestion, RoadmapSubtopicOption

class RoadmapSubtopicOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadmapSubtopicOption
        fields = ['id', 'option_text', 'order', 'is_correct']

class RoadmapSubtopicQuestionSerializer(serializers.ModelSerializer):
    options = RoadmapSubtopicOptionSerializer(many=True)

    class Meta:
        model = RoadmapSubtopicQuestion
        fields = ['id', 'question_text', 'order', 'options']

class RoadmapSubtopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadmapSubtopic
        fields = ['id', 'subtopicName', 'explanation']

class RoadmapChapterSerializer(serializers.ModelSerializer):
    subtopics = RoadmapSubtopicSerializer(many=True)

    class Meta:
        model = RoadmapChapter
        fields = ['chapterName', 'subtopics']

class RoadmapListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roadmap
        fields = ['id', 'mainTopic', 'routerLink', 'intro', 'created_at']

class RoadmapSerializer(serializers.ModelSerializer):
    chapters = RoadmapChapterSerializer(many=True)

    class Meta:
        model = Roadmap
        fields = ['mainTopic', 'routerLink', 'intro', 'chapters']

    def create(self, validated_data):
        chapters_data = validated_data.pop('chapters', [])
        
        routerLink = validated_data.get('routerLink')
        roadmap, created = Roadmap.objects.update_or_create(
            routerLink=routerLink,
            defaults=validated_data
        )

        if not created:
            roadmap.chapters.all().delete()

        for chapter_data in chapters_data:
            subtopics_data = chapter_data.pop('subtopics', [])
            chapter = RoadmapChapter.objects.create(roadmap=roadmap, **chapter_data)
            for subtopic_data in subtopics_data:
                RoadmapSubtopic.objects.create(chapter=chapter, **subtopic_data)
        
        return roadmap
