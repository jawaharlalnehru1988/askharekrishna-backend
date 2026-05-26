"""
AI-powered translation helper for Brahmhacarya articles.
Returns translated title, excerpt, and content body.
"""
import json
from typing import List

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

MAX_CONTENT_CHARS = 50000
MAX_CHUNK_CHARS = 3500
MAX_CHUNKS = 25
MAX_ATTEMPTS_PER_CALL = 2
REQUEST_TIMEOUT_SECONDS = 90


def _language_specific_rules(target_language: str) -> str:
    language_code = (target_language or "").lower()

    if language_code == "ta":
        return """Tamil-specific rules:
- Use only Tamil script for translated Tamil text. Do NOT mix in Devanagari or any other Indic script.
- If a Sanskrit devotional term must be retained, write it in Tamil script, not Devanagari.
- Translate "Lord" and "God" as "பகவான்" when referring to the Supreme Lord in devotional context.
- Do NOT translate "Lord" or "God" as "ஆண்டவர்" in this devotional context.
- Translate "deity" as "விக்ரஹம்" in devotional temple/worship context.
- Do NOT translate "deity" as "தெய்வம்" in this devotional context.
"""

    return ""


def _build_meta_system_prompt(target_language: str) -> str:
    lang_name = LANGUAGE_NAMES.get(target_language.lower(), target_language)
    language_rules = _language_specific_rules(target_language)
    return f"""You are an expert devotional content translator.
Translate the provided English Brahmacharya article title and excerpt into {lang_name}.

Rules:
- Preserve meaning, tone, and spiritual context.
- Keep output concise and natural.
{language_rules}- Use strict {lang_name} output for the translated text unless the source includes a proper noun that should remain recognizable.
- If the source excerpt is empty, return an empty string for the excerpt.
- Return ONLY valid JSON with exactly these keys:
{{
  \"title\": \"<translated title in {lang_name}>\",
  \"excerpt\": \"<translated excerpt in {lang_name}>\"
}}
"""


def _build_content_system_prompt(target_language: str) -> str:
    lang_name = LANGUAGE_NAMES.get(target_language.lower(), target_language)
    language_rules = _language_specific_rules(target_language)
    return f"""You are an expert devotional content translator.
Translate the provided English Brahmacharya article chunk into {lang_name}.

Rules:
- Preserve meaning, tone, and spiritual context.
- Keep paragraphs natural and readable.
- Do not add new facts and do not omit meaning.
- Keep the translation strictly in {lang_name} script/style for normal translated text.
{language_rules}- Maintain devotional consistency for repeated sacred terms across the whole article.
- Return ONLY valid JSON with exactly this key:
{{
  \"articleChunk\": \"<translated chunk in {lang_name}>\"
}}
"""


def _call_json_completion(client: OpenAI, model: str, system_prompt: str, user_message: str) -> dict:
    last_error = None
    for _ in range(MAX_ATTEMPTS_PER_CALL):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message},
                ],
                temperature=0.2,
                response_format={"type": "json_object"},
                timeout=REQUEST_TIMEOUT_SECONDS,
            )
            raw = response.choices[0].message.content
            return json.loads(raw)
        except Exception as exc:
            last_error = exc
    raise ValueError(f"Translation request failed after retries: {last_error}")


def _split_into_chunks(text: str, max_chunk_chars: int) -> List[str]:
    if len(text) <= max_chunk_chars:
        return [text]

    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    if not paragraphs:
        paragraphs = [text]

    chunks: List[str] = []
    current = ""

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        if len(para) > max_chunk_chars:
            if current:
                chunks.append(current)
                current = ""
            start = 0
            while start < len(para):
                chunks.append(para[start:start + max_chunk_chars])
                start += max_chunk_chars
            continue

        candidate = para if not current else f"{current}\n\n{para}"
        if len(candidate) <= max_chunk_chars:
            current = candidate
        else:
            chunks.append(current)
            current = para

    if current:
        chunks.append(current)

    return chunks


def translate_brahmhacarya_article(title: str, excerpt: str, content: str, target_language: str) -> dict:
    api_key = settings.OPENAI_API_KEY
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not configured in settings.")

    if not content or not content.strip():
        raise ValueError("Article content is empty.")

    model = getattr(settings, "OPENAI_MODEL", "gpt-4o-mini")
    base_url = getattr(settings, "OPENAI_BASE_URL", "https://api.openai.com/v1/")
    client = OpenAI(api_key=api_key, base_url=base_url)

    article = content.strip()[:MAX_CONTENT_CHARS]
    article_chunks = _split_into_chunks(article, MAX_CHUNK_CHARS)

    if len(article_chunks) > MAX_CHUNKS:
        raise ValueError(
            "Article is too large to translate safely in one request. "
            "Please shorten the article and try again."
        )

    lang_name = LANGUAGE_NAMES.get(target_language.lower(), target_language)

    meta_payload = _call_json_completion(
        client=client,
        model=model,
        system_prompt=_build_meta_system_prompt(target_language),
        user_message=(
            f"Target language: {lang_name}\n\n"
            f"Title (English):\n{title}\n\n"
            f"Excerpt (English):\n{excerpt or ''}"
        ),
    )

    translated_title = (meta_payload.get("title") or "").strip()
    translated_excerpt = (meta_payload.get("excerpt") or "").strip() if (excerpt or "").strip() else ""

    if not translated_title:
        raise ValueError("Missing or empty translated title.")

    translated_chunks: List[str] = []
    total_chunks = len(article_chunks)

    for idx, chunk in enumerate(article_chunks, start=1):
        chunk_payload = _call_json_completion(
            client=client,
            model=model,
            system_prompt=_build_content_system_prompt(target_language),
            user_message=(
                f"Target language: {lang_name}\n"
                f"Chunk {idx} of {total_chunks}\n\n"
                f"English article chunk:\n{chunk}"
            ),
        )

        translated_chunk = (chunk_payload.get("articleChunk") or "").strip()
        if not translated_chunk:
            raise ValueError(f"Missing translated content for chunk {idx}/{total_chunks}.")

        translated_chunks.append(translated_chunk)

    translated_content = "\n\n".join(translated_chunks).strip()
    if not translated_content:
        raise ValueError("Translated article content is empty.")

    return {
        "title": translated_title,
        "excerpt": translated_excerpt,
        "content": translated_content,
    }
