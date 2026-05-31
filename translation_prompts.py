"""
Shared prompt builders for devotional translation modules.
Update prompt wording here to apply across Story, Pooja Vidhis, and Brahmhacarya.
"""

from translation_rules import get_language_specific_rules


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


def get_language_name(language_code: str) -> str:
    return LANGUAGE_NAMES.get((language_code or "").lower(), language_code)


def build_story_meta_system_prompt(target_language: str) -> str:
    lang_name = get_language_name(target_language)
    language_rules = get_language_specific_rules(target_language)
    return f"""You are an expert devotional content translator.
Translate only short labels from the source language into {lang_name}.

Rules:
- Preserve meaning and devotional tone.
- Keep output concise and natural.
{language_rules}- Use strict {lang_name} output for the translated text unless the source includes a proper noun that should remain recognizable.
- Return ONLY valid JSON with exactly these keys:
{{
  \"mainTopic\": \"<translated main topic in {lang_name}>\",
  \"subTopic\": \"<translated sub topic in {lang_name}>\"
}}
"""


def build_story_chunk_system_prompt(target_language: str) -> str:
    lang_name = get_language_name(target_language)
    language_rules = get_language_specific_rules(target_language)
    return f"""You are an expert devotional content translator.
Translate the provided article chunk from the source language into {lang_name}.

Rules:
- Preserve meaning, tone, and devotional context.
- Keep paragraphs natural and readable.
- Do not add new facts and do not omit meaning.
- Keep the translation strictly in {lang_name} script/style for normal translated text.
{language_rules}- Maintain devotional consistency for repeated sacred terms across the whole article.
- Return ONLY valid JSON with exactly this key:
{{
  \"articleChunk\": \"<translated chunk in {lang_name}>\"
}}
"""


def build_pooja_meta_system_prompt(target_language: str) -> str:
    # Pooja Vidhis follows the same prompt policy as Stories.
    return build_story_meta_system_prompt(target_language)


def build_pooja_chunk_system_prompt(target_language: str) -> str:
    # Pooja Vidhis follows the same prompt policy as Stories.
    return build_story_chunk_system_prompt(target_language)


def build_brahmhacarya_meta_system_prompt(target_language: str) -> str:
    lang_name = get_language_name(target_language)
    language_rules = get_language_specific_rules(target_language)
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


def build_brahmhacarya_chunk_system_prompt(target_language: str) -> str:
    lang_name = get_language_name(target_language)
    language_rules = get_language_specific_rules(target_language)
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
