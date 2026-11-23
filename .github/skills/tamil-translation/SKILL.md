---
name: tamil-translation-pure
summary: Generate pure Tamil translations for repository content with strict language discipline.
---

# Skill: Pure Tamil Translation

Use this skill whenever translating any content into Tamil for this repository.

## Step 0 — Read Vocabulary First (MANDATORY)

Before writing a single Tamil word, open and read:

```
.github/skills/tamil-translation/VOCABULARY.md
```

Every term that appears in that file **must** use the exact approved Tamil equivalent
listed there. Do not use your own alternative translation for any listed term.
If a term you encounter is not listed, use natural Tamil and add it to the vocabulary
file under `(REVIEW NEEDED)` so it can be approved later.

---

## Hard Rules

1. Tamil-only output for narrative fields such as title, excerpt, and content.
2. Do not mix other languages (English, Hindi, Telugu, etc.) inside Tamil sentences.
3. 🚫 Strictly avoid English parenthetical translations or crutches in headings, subtitles, or body text (e.g. NEVER write `**துணைத்தலைப்பு:** ... (Why did Krishna...)` or `மன அழுத்தம் (stress)` or `(ஆததாயிகள் - Atatayis)`). Use pure, self-sufficient Tamil directly.
4. 🚫 Strictly avoid the archaic letter 'ஶ'. Use standard contemporary Grantha/Tamil letters 'ஸ', 'ஷ', or 'ச'. For Sanskrit 'श' (ś / śa), strictly use 'ஷ' (e.g., `அஷோச்யான்`, `ஷரீராணி`, `ஷாஷ்வத:`).
5. For Sanskrit Visarga (ः / ḥ) in Tamil script, strictly use colon (`:`) (e.g. `பண்டிதா:`, `ராம:`), NEVER the Tamil Aytham letter `ஃ`.
6. All quoted scriptural verses (Shastra Pramana) must be transliterated into Tamil script, never left in Roman/English transliteration.
7. Always use explicit hierarchical scriptural citations (e.g. `பகவத் கீதை, அத்தியாயம் 2, சுலோகம் 11`), never bare numerical codes like `(2.11)`.
8. Proper Names & Epics: Draupadi must strictly be spelled as 'திரௌபதி' (திரௌபதியின், திரௌபதியை, திரௌபதிக்கு, திரௌபதியிடம்), NEVER as 'துரோபதை' or 'துரோபதி'.
9. Keep DB field keys, API field names, slug values, category strings, and `language` code unchanged.
10. Keep source meaning accurate; do not shorten critical spiritual or philosophical meaning.

## Formatting Rules

1. Preserve original markdown hierarchy (headings, bullets, blockquotes, tables).
2. Preserve numbered flow where it exists in the source.
3. Keep verse references, chapter numbers, and citations intact in Tamil rendering.
4. Keep tone clear, devotional, and natural Tamil — not stilted or over-formal.

## Quality Checklist (run before finalising)

1. Did you consult VOCABULARY.md for every spiritual/technical term?
2. Is every sentence in Tamil script only?
3. Are there any accidental characters from other scripts?
4. Does the meaning match the source accurately?
5. Are DB field-length constraints satisfied (excerpt ≤ 500 chars, title ≤ 255 chars)?

## Allowed Form Examples

- `மனம் அமைதியடைகிறது (Neural Regulation)` — technical term in brackets after Tamil
- `ஜபம்` — Sanskrit devotional term used directly (listed in VOCABULARY.md)
- `பிரம்மச்சரியம்` — correct form (see VOCABULARY.md Section 1)

## Not Allowed Form Examples

- `மனம் calm ஆகும்` — English word inside sentence
- `இந்த section மிகவும் important` — English nouns without brackets
- `பிரம்மசர்யம்` — incorrect spelling (correct form is listed in VOCABULARY.md)
