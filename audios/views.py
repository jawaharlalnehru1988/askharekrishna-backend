from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from askharekrishna_backend.permissions import IsAdminOrReadOnly

from .models import Audio
from .serializers import AudioSerializer


class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all().order_by('id')
    serializer_class = AudioSerializer
    permission_classes = [IsAdminOrReadOnly]


@api_view(['GET'])
@permission_classes([IsAdminOrReadOnly])
def audio_bg_seed(request):
    # Return the seeded list (live from DB if present; otherwise static default)
    if Audio.objects.exists():
        data = AudioSerializer(Audio.objects.all().order_by('id'), many=True).data
        return Response(data)

    # Default seed payload if DB is empty
    seed = [
        {
            "id": 1,
            "audioListId": 1,
            "title": "Chapter 1: Observing the Armies",
            "description": "The armies of the Pandavas and Kauravas assemble on the battlefield.",
            "language": "English",
            "duration": "45:00",
            "audioUrl": "https://example.com/audio/1.mp3",
            "isPlaying": True
        },
        {
            "id": 2,
            "audioListId": 1,
            "title": "Chapter 2: Contents of the Gita Summarized",
            "description": "Arjuna surrenders to Lord Krishna and asks for instruction.",
            "language": "English",
            "duration": "58:20",
            "audioUrl": "https://example.com/audio/2.mp3"
        },
        {
            "id": 3,
            "audioListId": 1,
            "title": "Chapter 3: Karma Yoga",
            "description": "The path of selfless service and action without attachment.",
            "language": "Hindi",
            "duration": "42:15",
            "audioUrl": "https://example.com/audio/3.mp3"
        },
        {
            "id": 4,
            "audioListId": 1,
            "title": "Chapter 4: Transcendental Knowledge",
            "description": "Approaching a spiritual master and receiving knowledge.",
            "language": "Bengali",
            "duration": "48:10",
            "audioUrl": "https://example.com/audio/4.mp3"
        },
        {
            "id": 5,
            "audioListId": 1,
            "title": "Chapter 5: Karma-yoga Action in Krishna Consciousness",
            "description": "Performing action without desiring the fruits.",
            "language": "English",
            "duration": "39:45",
            "audioUrl": "https://example.com/audio/5.mp3"
        }
    ]
    return Response(seed)
