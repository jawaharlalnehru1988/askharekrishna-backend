from django.contrib import admin
from django.utils.html import format_html
from .models import (
	Category,
	CarnaticQuestion,
	CarnaticSyllabus,
	CarnaticSyllabusVideoSample,
	CarnaticKacheri,
	CarnaticClassAudio,
	CarnaticLessonPractice,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'order', 'name', 'colorCode', 'created_at')
	search_fields = ('name',)
	readonly_fields = ('created_at', 'updated_at')
	fields = ('order', 'name', 'colorCode', 'created_at', 'updated_at')


@admin.register(CarnaticQuestion)
class CarnaticQuestionAdmin(admin.ModelAdmin):
	list_display = ('id', 'question', 'category', 'created_at')
	list_filter = ('category',)
	search_fields = ('question', 'answer', 'category__name')
	readonly_fields = ('created_at', 'updated_at')
	fields = ('category', 'question', 'answer', 'audio', 'created_at', 'updated_at')


class CarnaticSyllabusVideoSampleInline(admin.TabularInline):
	model = CarnaticSyllabusVideoSample
	extra = 1
	fields = ('url',)


@admin.register(CarnaticSyllabus)
class CarnaticSyllabusAdmin(admin.ModelAdmin):
	list_display = ('id', 'topic')
	list_filter = ('category',)
	search_fields = ('category__name', 'topic', 'lesson')
	readonly_fields = ('created_at', 'updated_at')
	fields = ('category', 'topic', 'lesson', 'audioPath', 'created_at', 'updated_at')
	inlines = [CarnaticSyllabusVideoSampleInline]


@admin.register(CarnaticKacheri)
class CarnaticKacheriAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'singer', 'ragam', 'created_at')
	search_fields = ('title', 'singer', 'ragam', 'description')
	readonly_fields = ('created_at', 'updated_at')
	fields = ('title', 'singer', 'ragam', 'videoUrl', 'description', 'created_at', 'updated_at')


@admin.register(CarnaticClassAudio)
class CarnaticClassAudioAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'created_at')
	search_fields = ('title',)
	readonly_fields = ('audio_preview', 'created_at', 'updated_at')
	fields = ('title', 'audioPath', 'audio_preview', 'created_at', 'updated_at')

	def audio_preview(self, obj):
		if obj and obj.audioPath:
			return format_html(
				'<audio controls preload="none" style="max-width: 420px;"><source src="{}">Your browser does not support the audio element.</audio>',
				obj.audioPath.url,
			)
		return 'No audio uploaded yet.'

	audio_preview.short_description = 'Audio Preview'


@admin.register(CarnaticLessonPractice)
class CarnaticLessonPracticeAdmin(admin.ModelAdmin):
	list_display = ('id', 'PracticeCategory', 'lessonName', 'created_at')
	search_fields = ('PracticeCategory', 'lessonName')
	readonly_fields = ('audio_preview', 'created_at', 'updated_at')
	fields = ('PracticeCategory', 'lessonName', 'audioPath', 'audio_preview', 'created_at', 'updated_at')

	def audio_preview(self, obj):
		if obj and obj.audioPath:
			return format_html(
				'<audio controls preload="none" style="max-width: 420px;"><source src="{}">Your browser does not support the audio element.</audio>',
				obj.audioPath.url,
			)
		return 'No audio uploaded yet.'

	audio_preview.short_description = 'Audio Preview'
