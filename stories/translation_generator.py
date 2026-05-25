"""
AI-powered translation helper for story content.
Returns translated main topic, sub topic, and article body.
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


def _build_system_prompt(target_language: str) -> str:
    lang_name = LANGUAGE_NAMES.get(target_language.lower(), target_language)
    return f"""You are an expert devotional content translator.
Translate the provided story content from English into {lang_name}.

Requirements:
- Preserve meaning, tone, and devotional context.
- Translate all three fields: main topic, sub topic, and article.
- Keep article structure readable with natural paragraphing.
- Do not add new facts or remove key meaning.
- Output must be in {lang_name} only.
- Return ONLY valid JSON with exactly these keys:

{{
  \"mainTopic\": \"<translated main topic in {lang_name}>\",
  \"subTopic\": \"<translated sub topic in {lang_name}>\",
  \"article\": \"<translated article in {lang_name}>\"
}}
"""


def translate_story_content(main_topic: str, sub_topic: str, article_text: str, target_language: str) -> dict:
    api_key = settings.OPENAI_API_KEY
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not configured in settings.")

    model = getattr(settings, 'OPENAI_MODEL', 'gpt-4o-mini')
    base_url = getattr(settings, 'OPENAI_BASE_URL', 'https://api.openai.com/v1/')
    client = OpenAI(api_key=api_key, base_url=base_url)

    user_message = (
        f"Target language: {LANGUAGE_NAMES.get(target_language.lower(), target_language)}\\n\\n"
        f"Main topic (English):\\n{main_topic}\\n\\n"
        f"Sub topic (English):\\n{sub_topic}\\n\\n"
        f"Article (English):\\n{article_text[:12000]}"
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": _build_system_prompt(target_language)},
            {"role": "user", "content": user_message},
        ],
        temperature=0.3,
        response_format={"type": "json_object"},
    )

    raw = response.choices[0].message.content
    data = json.loads(raw)

    required_keys = ["mainTopic", "subTopic", "article"]
    for key in required_keys:
        value = data.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Missing or empty translated field: {key}")

    return {
        "mainTopic": data["mainTopic"].strip(),
        "subTopic": data["subTopic"].strip(),
        "article": data["article"].strip(),
    }
