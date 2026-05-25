from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    """
    API Root - List all available API endpoints
    """
    return Response({
        'audios': reverse('audio-bg-list', request=request, format=format),
        'document_library': reverse('document-library-list', request=request, format=format),
        'stories': reverse('story-article-list', request=request, format=format),
        'kirtans': reverse('kirtan-list', request=request, format=format),
        'kirtan_categories': reverse('kirtan-category-list', request=request, format=format),
        'brahmhacarya': reverse('brahmhacarya-list', request=request, format=format),
        'brahmhacarya_registration': reverse('brahmhacarya-registration', request=request, format=format),
        'image_gallery': reverse('image-gallery-list', request=request, format=format),
        'imageGalleryCategories': reverse('imageGalleryCategories-list', request=request, format=format),
        'video_gallery': reverse('video-gallery-list', request=request, format=format),
        'carnatic_categories': reverse('carnatic-categories-list', request=request, format=format),
        'carnatic_kacheri': reverse('carnatic-kacheri-list', request=request, format=format),
        'carnatic_questions': reverse('carnatic-questions-list', request=request, format=format),
        'carnatic_syllabus': reverse('carnatic-syllabus-list', request=request, format=format),
        'carnatic_lesson_practice': reverse('carnatic-lesson-practice-list', request=request, format=format),
        'ourOtherSites': reverse('our-other-sites-list', request=request, format=format),
        'chanting_articles': reverse('chanting-article-list', request=request, format=format),
        'cooking_articles': reverse('cooking-article-list', request=request, format=format),
        'debate_articles': reverse('debate-article-list', request=request, format=format),
        'debate_categories': reverse('debate-article-categories', request=request, format=format),
        'pooja_vidhis': reverse('pooja-vidhi-article-list', request=request, format=format),
        'vaishnava_etiquettes': reverse('vaishnava-etiquette-article-list', request=request, format=format),
        'book_distribution': reverse('book-distribution-article-list', request=request, format=format),
        'kirtan_tutorials': reverse('kirtan-tutorial-article-list', request=request, format=format),
        'resources_links': reverse('weburlresource-list', request=request, format=format),
        'subscribers': reverse('subscriber-list', request=request, format=format),
    })
