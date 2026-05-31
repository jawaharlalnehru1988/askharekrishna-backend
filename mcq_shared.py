"""
Shared MCQ generation helpers for devotional article modules.
"""

import json
import re
from typing import Optional

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


def build_mcq_system_prompt(language: str, extra_rules: str = "") -> str:
    lang_name = LANGUAGE_NAMES.get((language or "").lower(), language)
    normalized_extra_rules = (extra_rules or "").strip()
    if normalized_extra_rules and not normalized_extra_rules.endswith("\n"):
        normalized_extra_rules += "\n"

    return f"""You are a quiz-question generator for devotional / spiritual articles.
Given an article text, produce EXACTLY 10 multiple-choice questions that test
comprehension of the article content.

IMPORTANT: The article is in {lang_name}. You MUST write ALL questions and ALL
answer options in {lang_name}. Do NOT translate to any other language.

Rules:
- Each question must have EXACTLY 4 answer options (A, B, C, D).
- Exactly ONE option per question must be correct.
- Questions and options must be based solely on the article provided.
- Questions must be standalone and directly understandable by the learner without referencing the source text.
- Do NOT use meta-referential phrasing such as "according to the article", "in the article", "the article says", "as mentioned in the passage", or similar wording.
- Ask directly about principles, philosophies, morals, values, key teachings, and the main theme.
- Prefer conceptual understanding over surface wording recall.
{normalized_extra_rules}- Make wrong options (distractors) plausible and close to the correct answer, not obviously wrong.
- Keep all 4 options in the same semantic category and similar style/length.
- Avoid giveaway patterns (like one option being much longer, more specific, or more devotional sounding).
- Do NOT use options such as "All of the above", "None of the above", or humorous/irrelevant distractors.
- For each question, ensure all options are distinct and non-overlapping in meaning.
- Distribute the correct option position across 1-4 across the 10 questions; do not keep it fixed at one position.
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


_DISALLOWED_QUESTION_PATTERNS = [
    re.compile(r"\baccording to (the )?(article|passage|text|content)\b", re.IGNORECASE),
    re.compile(r"\bin (the )?(article|passage|text|content)\b", re.IGNORECASE),
    re.compile(r"\bthe (article|passage|text|content) (says|states|mentions|explains|discusses)\b", re.IGNORECASE),
    re.compile(r"\bas (mentioned|stated|described|explained) in (the )?(article|passage|text|content)\b", re.IGNORECASE),
    re.compile(r"\bfrom (the )?(article|passage|text|content)\b", re.IGNORECASE),
]


def _validate_questions(questions: list) -> None:
    if len(questions) != 10:
        raise ValueError(
            f"OpenAI returned {len(questions)} questions instead of 10. "
            "Try again or edit manually."
        )

    for q in questions:
        question_text = (q.get("question") or "").strip()
        if not question_text:
            raise ValueError("A generated question is empty.")

        for pattern in _DISALLOWED_QUESTION_PATTERNS:
            if pattern.search(question_text):
                raise ValueError(
                    "Generated MCQ contains meta-referential phrasing "
                    "(e.g., 'according to the article')."
                )

        options = q.get("options", [])
        if len(options) != 4:
            raise ValueError(
                f"Question '{question_text}' does not have 4 options."
            )

        correct_count = sum(1 for opt in options if bool(opt.get("is_correct")))
        if correct_count != 1:
            raise ValueError(
                f"Question '{question_text}' must have exactly one correct option."
            )


def generate_mcqs(
    article_text: str,
    language: str = "en",
    *,
    extra_rules: str = "",
    article_char_limit: int = 6000,
    temperature: float = 0.4,
) -> list:
    api_key = settings.OPENAI_API_KEY
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not configured in settings.")

    model = getattr(settings, "OPENAI_MODEL", "gpt-4o-mini")
    base_url = getattr(settings, "OPENAI_BASE_URL", "https://api.openai.com/v1/")
    client = OpenAI(api_key=api_key, base_url=base_url)

    user_message = (
        f"Language of the article: {LANGUAGE_NAMES.get((language or '').lower(), language)}\\n\\n"
        f"Article:\\n{(article_text or '')[:article_char_limit]}"
    )

    max_attempts = 3
    last_error: Optional[Exception] = None

    for _ in range(max_attempts):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": build_mcq_system_prompt(language, extra_rules=extra_rules)},
                    {"role": "user", "content": user_message},
                ],
                temperature=temperature,
                response_format={"type": "json_object"},
            )

            raw = response.choices[0].message.content
            data = json.loads(raw)
            questions = data.get("questions", [])
            _validate_questions(questions)
            return questions
        except Exception as exc:
            last_error = exc

    raise ValueError(f"MCQ generation failed after retries: {last_error}")


def save_mcqs(
    parent_obj,
    questions: list,
    *,
    question_model,
    option_model,
    parent_field_name: str,
    question_field_name: str,
) -> int:
    parent_obj.questions.all().delete()

    for q_data in questions:
        question = question_model.objects.create(
            **{
                parent_field_name: parent_obj,
                question_field_name: q_data["question"],
                "order": q_data["order"],
                "is_active": True,
            }
        )
        for opt in q_data["options"]:
            option_model.objects.create(
                question=question,
                option_text=opt["text"],
                order=opt["order"],
                is_correct=opt["is_correct"],
            )

    return len(questions)
