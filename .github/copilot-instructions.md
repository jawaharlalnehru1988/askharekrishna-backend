# Repository Instructions for Tamil Translation

When generating Tamil translations for this repository, follow these rules strictly:

1. Output language for `title`, `excerpt`, and `content` must be Tamil only.
2. Do not mix other languages (English, Hindi, Telugu, Bengali, etc.) inside Tamil sentences.
3. Scientific or technical terms may be kept in English only when necessary, and must appear in brackets, for example: `நரம்பியல் (Neuroscience)`.
4. Sanskrit terms used in devotional context are allowed, but the surrounding sentence must be Tamil.
5. Keep category values and language codes unchanged when required by existing schema, for example: `language='ta'`, existing English category keys.
6. Preserve markdown structure from source content (headings, bullets, blockquotes, tables) while translating text to Tamil.
7. Do not produce transliteration-heavy mixed text; use readable native Tamil script.
8. Before finalizing, do a self-check:
   - Is every sentence Tamil?
   - Are non-Tamil words present only as required terms in brackets?
   - Are there any accidental characters from other scripts?

If any rule conflicts, prefer pure Tamil readability and consistency.
