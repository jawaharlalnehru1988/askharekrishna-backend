"""
MCQ generation from OpenAI for Pooja Vidhi articles.
Returns a list of exactly 10 questions, each with 4 options.
"""
import json

from django.conf import settings
from openai import OpenAI


LANGUAGE_NAMES = {
    "en": "English",
    "ta": "Tamil",
    "hi": "Hindi",
    "te": "Telugu",
    "kn": "Kannada",
    "ml": "Malayalam",
    "mr": "Marathi",
    "bn": "Bengali",
    "gu": "Gujarati",
    "pa": "Punjabi",
    "or": "Odia",
    "sa": "Sanskrit",
}


def _build_system_prompt(language: str) -> str:
    lang_name = LANGUAGE_NAMES.get(language.lower(), language)
    return f"""You are a quiz-question generator for devotional / spiritual articles.
Given an article text, produce EXACTLY 10 multiple-choice questions that test
comprehension of the article content.

IMPORTANT: The article is in {lang_name}. You MUST write ALL questions and ALL
answer options in {lang_name}. Do NOT translate to any other language.

Rules:
- Each question must have EXACTLY 4 answer options (A, B, C, D).
- Exactly ONE option per question must be correct.
- Questions and options must be based solely on the article provided.
- Keep language simple and clear.
- Return ONLY valid JSON in this exact structure (no markdown, no extra keys):

{{
    "questions": [
        {{
            "order": 1,
            "question": "<question text in {lang_name}>",
            "options": [
                {{"order": 1, "text": "<option A in {lang_name}>", "is_correct": false}},
                {{"order": 2, "text": "<option B in {lang_name}>", "is_correct": false}},
                {{"order": 3, "text": "<option C in {lang_name}>", "is_correct": true}},
                {{"order": 4, "text": "<option D in {lang_name}>", "is_correct": false}}
            ]
        }}
    ]
}}
"""


def generate_mcqs(article_text: str, language: str = "en") -> list:
    api_key = settings.OPENAI_API_KEY
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not configured in settings.")

    model = getattr(settings, 'OPENAI_MODEL', 'gpt-4o-mini')
    base_url = getattr(settings, 'OPENAI_BASE_URL', 'https://api.openai.com/v1/')
    client = OpenAI(api_key=api_key, base_url=base_url)

    user_message = (
        f"Language of the article: {LANGUAGE_NAMES.get(language.lower(), language)}\n\n"
        f"Article:\n{article_text[:6000]}"
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": _build_system_prompt(language)},
            {"role": "user", "content": user_message},
        ],
        temperature=0.4,
        response_format={"type": "json_object"},
    )

    raw = response.choices[0].message.content
    data = json.loads(raw)
    questions = data.get("questions", [])

    if len(questions) != 10:
        raise ValueError(
            f"OpenAI returned {len(questions)} questions instead of 10. "
            "Try again or edit manually."
        )

    for q in questions:
        if len(q.get("options", [])) != 4:
            raise ValueError(
                f"Question '{q.get('question', '')}' does not have 4 options."
            )

    return questions


def save_mcqs(pooja_vidhi, questions: list) -> int:
    from .models import PoojaVidhiQuestion, PoojaVidhiQuestionOption

    pooja_vidhi.questions.all().delete()

    for q_data in questions:
        question = PoojaVidhiQuestion.objects.create(
            pooja_vidhi=pooja_vidhi,
            question_text=q_data["question"],
            order=q_data["order"],
            is_active=True,
        )
        for opt in q_data["options"]:
            PoojaVidhiQuestionOption.objects.create(
                question=question,
                option_text=opt["text"],
                order=opt["order"],
                is_correct=opt["is_correct"],
            )

    return len(questions)
