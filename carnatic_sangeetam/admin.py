from django.contrib import admin
from django.utils.html import format_html
from .models import (
	Category,
	CarnaticSyllabus,
	CarnaticSyllabusVideoSample,
	CarnaticKacheri,
	CarnaticClassAudio,
	CarnaticLessonPractice,
	CarnaticLessonPracticeAudio,
	CarnaticLessonPracticeVideo,
	RagamLesson,
	RagamLessonAudio,
	RagamLessonVideo,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'order', 'name', 'colorCode', 'created_at')
	search_fields = ('name',)
	readonly_fields = ('created_at', 'updated_at')
	fields = ('order', 'name', 'colorCode', 'created_at', 'updated_at')


class CarnaticSyllabusVideoSampleInline(admin.TabularInline):
	model = CarnaticSyllabusVideoSample
	extra = 1
	fields = ('url',)


@admin.register(CarnaticSyllabus)
class CarnaticSyllabusAdmin(admin.ModelAdmin):
	list_display = ('topic', 'id', 'category', 'created_at')
	list_display_links = ('topic',)
	list_filter = ('category',)
	search_fields = ('category__name', 'topic', 'lesson')
	list_select_related = ('category',)
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


class CarnaticLessonPracticeAudioInline(admin.TabularInline):
	model = CarnaticLessonPracticeAudio
	extra = 1
	readonly_fields = ('audio_preview', 'created_at', 'updated_at')
	fields = ('audioPathName', 'audioPath', 'audio_preview', 'sort_order')

	def audio_preview(self, obj):
		if obj and obj.audioPath:
			return format_html(
				'<audio controls preload="none" style="max-width: 280px;"><source src="{}">Your browser does not support the audio element.</audio>',
				obj.audioPath.url,
			)
		return 'No audio uploaded yet.'

	audio_preview.short_description = 'AudioPathPreview'


class CarnaticLessonPracticeVideoInline(admin.TabularInline):
	model = CarnaticLessonPracticeVideo
	extra = 1
	fields = ('youtubevideoUrl', 'sort_order')


@admin.register(CarnaticLessonPractice)
class CarnaticLessonPracticeAdmin(admin.ModelAdmin):
	list_display = (
		'lessonName',
		'category',
		'orderNumber',
		'number_of_audio_lessons',
		'is_video_available',
	)
	list_display_links = ('lessonName',)
	list_editable = ('orderNumber',)
	list_filter = ('category',)
	search_fields = ('lessonName', 'category__name')
	readonly_fields = ('created_at', 'updated_at')
	fields = ('orderNumber', 'category', 'lessonName', 'created_at', 'updated_at')
	inlines = [CarnaticLessonPracticeAudioInline, CarnaticLessonPracticeVideoInline]

	def number_of_audio_lessons(self, obj):
		return obj.audios.count()

	number_of_audio_lessons.short_description = 'Number of Audio Lessons'

	def is_video_available(self, obj):
		return obj.videos.exists()

	is_video_available.boolean = True
	is_video_available.short_description = 'Is Video Available?'


class RagamLessonAudioInline(admin.TabularInline):
	model = RagamLessonAudio
	extra = 1
	readonly_fields = ('audio_preview', 'created_at', 'updated_at')
	fields = ('songName', 'audioPath', 'audio_preview', 'sort_order')

	def audio_preview(self, obj):
		if obj and obj.audioPath:
			return format_html(
				'<audio controls preload="none" style="max-width: 280px;"><source src="{}">Your browser does not support the audio element.</audio>',
				obj.audioPath.url,
			)
		return 'No audio uploaded yet.'

	audio_preview.short_description = 'Audio Preview'


class RagamLessonVideoInline(admin.TabularInline):
	model = RagamLessonVideo
	extra = 1
	fields = ('title', 'youtubevideoUrl', 'sort_order')


@admin.register(RagamLesson)
class RagamLessonAdmin(admin.ModelAdmin):
	list_display = (
		'raga_name',
		'melakarthaNumber',
		'swarasthanas',
		'audio_count',
		'video_count',
		'created_at',
	)
	list_display_links = ('raga_name',)
	list_filter = ('melakarthaNumber',)
	search_fields = ('raga_name', 'swarasthanas', 'arohanam_avarohanam', 'famousCompositions', 'description')
	readonly_fields = ('created_at', 'updated_at')
	fields = (
		'raga_name',
		'melakarthaNumber',
		'swarasthanas',
		'arohanam_avarohanam',
		'description',
		'famousCompositions',
		'created_at',
		'updated_at',
	)
	inlines = [RagamLessonAudioInline, RagamLessonVideoInline]

	def audio_count(self, obj):
		return obj.audios.count()

	audio_count.short_description = 'Audios'

	def video_count(self, obj):
		return obj.videos.count()

	video_count.short_description = 'Videos'


