"""
AI-powered translation helper for story content.
Returns translated main topic, sub topic, and article body.
"""
import json
from typing import List

from django.conf import settings
from openai import OpenAI
from translation_prompts import (
    build_story_chunk_system_prompt,
    build_story_meta_system_prompt,
    get_language_name,
)

# Hard limits to prevent runaway requests.
MAX_ARTICLE_CHARS = 50000
MAX_CHUNK_CHARS = 3500
MAX_CHUNKS = 25
MAX_ATTEMPTS_PER_CALL = 2
REQUEST_TIMEOUT_SECONDS = 90

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
            # Fallback for very long single paragraph.
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


def translate_story_content(
    main_topic: str,
    sub_topic: str,
    article_text: str,
    source_language: str,
    target_language: str,
) -> dict:
    api_key = settings.OPENAI_API_KEY
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not configured in settings.")

    if not article_text or not article_text.strip():
        raise ValueError("Article text is empty.")

    source_language_code = (source_language or "").lower()
    target_language_code = (target_language or "").lower()
    if not source_language_code:
        raise ValueError("Source language is required.")
    if not target_language_code:
        raise ValueError("Target language is required.")
    if source_language_code == target_language_code:
        raise ValueError("Source and target languages must be different.")

    model = getattr(settings, "OPENAI_MODEL", "gpt-4o-mini")
    base_url = getattr(settings, "OPENAI_BASE_URL", "https://api.openai.com/v1/")
    client = OpenAI(api_key=api_key, base_url=base_url)

    article = article_text.strip()[:MAX_ARTICLE_CHARS]
    article_chunks = _split_into_chunks(article, MAX_CHUNK_CHARS)

    if len(article_chunks) > MAX_CHUNKS:
        raise ValueError(
            "Article is too large to translate safely in one request. "
            "Please shorten the article and try again."
        )

    source_lang_name = get_language_name(source_language_code) or source_language
    lang_name = get_language_name(target_language_code) or target_language

    meta_payload = _call_json_completion(
        client=client,
        model=model,
        system_prompt=build_story_meta_system_prompt(target_language_code),
        user_message=(
            f"Source language: {source_lang_name}\\n"
            f"Target language: {lang_name}\\n\\n"
            f"Main topic ({source_lang_name}):\\n{main_topic}\\n\\n"
            f"Sub topic ({source_lang_name}):\\n{sub_topic}"
        ),
    )

    translated_main_topic = (meta_payload.get("mainTopic") or "").strip()
    translated_sub_topic = (meta_payload.get("subTopic") or "").strip()

    if not translated_main_topic or not translated_sub_topic:
        raise ValueError("Missing or empty translated main topic/sub topic.")

    translated_chunks: List[str] = []
    total_chunks = len(article_chunks)

    for idx, chunk in enumerate(article_chunks, start=1):
        chunk_payload = _call_json_completion(
            client=client,
            model=model,
            system_prompt=build_story_chunk_system_prompt(target_language_code),
            user_message=(
                f"Source language: {source_lang_name}\\n"
                f"Target language: {lang_name}\\n"
                f"Chunk {idx} of {total_chunks}\\n\\n"
                f"Article chunk ({source_lang_name}):\\n{chunk}"
            ),
        )

        translated_chunk = (chunk_payload.get("articleChunk") or "").strip()
        if not translated_chunk:
            raise ValueError(f"Missing translated content for chunk {idx}/{total_chunks}.")

        translated_chunks.append(translated_chunk)

    translated_article = "\n\n".join(translated_chunks).strip()
    if not translated_article:
        raise ValueError("Translated article is empty.")

    return {
        "mainTopic": translated_main_topic,
        "subTopic": translated_sub_topic,
        "article": translated_article,
    }
