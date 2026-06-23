from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Roadmap, RoadmapSubtopic
from .serializers import RoadmapSerializer, RoadmapListSerializer
from django.conf import settings
from openai import OpenAI

class ExplainSubtopicAPIView(APIView):
    def post(self, request):
        subtopic_id = request.data.get('subtopic_id')
        reference_url = request.data.get('reference_url')

        if not subtopic_id or not reference_url:
            return Response({'detail': 'subtopic_id and reference_url are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            subtopic = RoadmapSubtopic.objects.get(id=subtopic_id)
        except RoadmapSubtopic.DoesNotExist:
            return Response({'detail': 'Subtopic not found.'}, status=status.HTTP_404_NOT_FOUND)

        if subtopic.explanation:
            return Response({'explanation': subtopic.explanation}, status=status.HTTP_200_OK)

        api_key = settings.OPENAI_API_KEY
        if not api_key:
            return Response({'detail': 'OPENAI_API_KEY is not configured in settings.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        model = getattr(settings, "OPENAI_MODEL", "gpt-4o-mini")
        base_url = getattr(settings, "OPENAI_BASE_URL", "https://api.openai.com/v1/")
        client = OpenAI(api_key=api_key, base_url=base_url)

        system_prompt = (
            "You are an authentic Vaishnava teacher and representative of A.C. Bhaktivedanta Swami Prabhupada. "
            f"Explain the following subtopic purely based on Srila Prabhupada's teachings. "
            f"Use the provided reference url ({reference_url}) as the primary source of truth. "
            "Respond directly with the explanation in markdown format."
        )

        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": subtopic.subtopicName}
                ]
            )
            
            explanation = response.choices[0].message.content
            
            subtopic.explanation = explanation
            subtopic.save()
            
            return Response({'explanation': explanation}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': f'Failed to generate explanation: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from mcq_shared import generate_mcqs, save_mcqs
from .models import RoadmapSubtopicQuestion, RoadmapSubtopicOption
from .serializers import RoadmapSubtopicQuestionSerializer

class SubtopicQuizAPIView(APIView):
    def post(self, request):
        subtopic_id = request.data.get('subtopic_id')
        if not subtopic_id:
            return Response({'detail': 'subtopic_id is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            subtopic = RoadmapSubtopic.objects.get(id=subtopic_id)
        except RoadmapSubtopic.DoesNotExist:
            return Response({'detail': 'Subtopic not found.'}, status=status.HTTP_404_NOT_FOUND)

        if subtopic.questions.exists():
            serializer = RoadmapSubtopicQuestionSerializer(subtopic.questions.all().order_by('order'), many=True)
            return Response({'questions': serializer.data}, status=status.HTTP_200_OK)

        if not subtopic.explanation:
            return Response({'detail': 'Explanation not generated yet. Please explain the subtopic first.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            questions_data = generate_mcqs(
                article_text=subtopic.explanation,
                language="en"
            )
            
            save_mcqs(
                parent_obj=subtopic,
                questions=questions_data,
                question_model=RoadmapSubtopicQuestion,
                option_model=RoadmapSubtopicOption,
                parent_field_name="subtopic",
                question_field_name="question_text"
            )

            serializer = RoadmapSubtopicQuestionSerializer(subtopic.questions.all().order_by('order'), many=True)
            return Response({'questions': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': f'Failed to generate quiz: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PushRoadmapAPIView(APIView):
    def post(self, request):
        serializer = RoadmapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoadmapListView(generics.ListAPIView):
    queryset = Roadmap.objects.all().order_by('-created_at')
    serializer_class = RoadmapListSerializer

class RoadmapDetailView(generics.RetrieveAPIView):
    queryset = Roadmap.objects.all()
    serializer_class = RoadmapSerializer
    lookup_field = 'routerLink'
