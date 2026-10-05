"""
Shared translation rule snippets for devotional content modules.
"""


def get_language_specific_rules(target_language: str) -> str:
    language_code = (target_language or "").lower()

    if language_code == "ta":
        return """Tamil-specific rules:
- Use only Tamil script for translated Tamil text. Do NOT mix in Devanagari or any other Indic script.
- If a Sanskrit devotional term must be retained, write it in Tamil script, not Devanagari.
- If the English source contains the name "Krishna", translate/render it as "பகவான் ஸ்ரீ கிருஷ்ணர்".
- In this devotional context, "பகவான்" is reserved for Lord Krishna and His Vishnu-tattva forms/avataras (for example: நரசிம்ஹர், விஷ்ணு, நாராயணர், மதுசூதனர், கோபாலர், கிரிதாரி, கேசவர், மாதவர், கோவிந்தர், திரிவிக்ரமர், ராமர், பலராமர், கல்கி, புத்தர், பரசுராமர், வாமனர், ஸ்ரீதரர், தாமோதரர்).
- Do NOT use "பகவான்" for demigods.
- If English has "Lord Shiva", render as "சிவ பெருமான்".
- If English has "Lord Muruga" or "Lord Karthikeya", render as "முருக பெருமான்".
- If English has "Lord Ganesha", render as "விநாயக பெருமான்".
- For other demigods, use "தேவர்" as suffix (for example: "Brahma" -> "ப்ரஹ்ம தேவர்", "Indra" -> "இந்திர தேவர்", "Chandra" -> "சந்திர தேவர்", "Surya" -> "சூர்ய தேவர்", "Varuna" -> "வருண தேவர்").
- Even when English does NOT use the prefix "Lord", still keep respectful demigod titles in Tamil according to position.
- Use "பெருமான்" for Shiva, Muruga/Karthikeya, and Ganesha by default when these names appear.
- Use "தேவர்" for Brahma, Indra, Chandra, Surya, Varuna and similar demigods by default when these names appear.
- If the English source contains the word "transcendental", translate/render it as "தெய்வீகமான" in Tamil.
- If the English source contains the word "divine", translate/render it as "தெய்வீகமான" or "தெய்வீக" based on natural Tamil sentence flow.
- If the English source contains "Supreme Personality of Godhead", translate/render it as "பூரண புருஷோத்தமரான பகவான்".
- If the English source contains "Personality of Godhead", translate/render it as "புருஷோத்தமரான பகவான்".
- If the English source contains "Supreme Lord", translate/render it as "பரம புருஷ பகவான்".
- Do NOT translate "Lord" or "God" as "ஆண்டவர்" or "கர்த்தர்" in this devotional context.
- Translate "deity" as "விக்ரஹம்" in devotional temple/worship context.
- Do NOT translate "deity" as "தெய்வம்" in this devotional context.
- Instead of using the words "இந்து" or "இந்து மதம்", strictly use "சனாதன" or "சனாதன தர்மம்" (for example: "சனாதன தர்மம்", "சனாதன தத்துவ", "சனாதன பாரம்பரியம்", "சனாதன தர்மத்தைப் பின்பற்றுவோர்").
- Do NOT include English parenthetical expressions or English terms in brackets (e.g., '(The Postbox Analogy)', '(Omnipresent)', '(Translation)') in headings or body text. Tamil is self-sufficient.
- All Sanskrit shlokas, verses, mantras, and quotes MUST be transliterated accurately into Tamil script. Do NOT leave shlokas in English, Roman, or IAST script.
"""

    if language_code == "kn":
        return """Kannada-specific rules:
- Use only pure Kannada script for translated text. Do NOT mix Devanagari or English script.
- If the English source contains the name "Krishna", translate/render it as "ಭಗವಾನ್ ಶ್ರೀಕೃಷ್ಣ" or "ಶ್ರೀಕೃಷ್ಣ".
- In this devotional context, "ಭಗವಾನ್" / "ಭಗವಂತ" is reserved for Lord Krishna and His Vishnu-tattva forms/avataras (ಕೃಷ್ಣ, ವಿಷ್ಣು, ನಾರಾಯಣ, ನರಸಿಂಹ, ರಾಮ, ಬಲರಾಮ, ವರಾಹ, ವಾಮನ, ಮಧುಸೂದನ, ಗೋಪಾಲ, ಗಿರಿಧಾರಿ, ಕೇಶವ, ಮಾಧವ, ಗೋವಿಂದ, ತ್ರಿವಿಕ್ರಮ, ಪದ್ಮನಾಭ, ದಾಮೋದರ ಇತ್ಯಾದಿ).
- Do NOT use "ಭಗವಾನ್" for demigods.
- If English has "Lord Shiva", render as "ಶಿವ ದೇವರು" or "ಶ್ರೀ ಶಂಕರ".
- If English has "Lord Brahma", render as "ಬ್ರಹ್ಮ ದೇವರು".
- If English has "Lord Indra", render as "ಇಂದ್ರ ದೇವರು".
- If English has "Lord Ganesha", render as "ಗಣೇಶ ದೇವರು".
- If the English source contains "Supreme Personality of Godhead", render as "ಪರಮ ಪುರುಷೋತ್ತಮ ಭಗವಾನ್".
- If the English source contains "Personality of Godhead", render as "ಪುರುಷೋತ್ತಮ ಭಗವಂತ".
- If the English source contains "Supreme Lord", render as "ಪರಮ ಪ್ರಭು ಭಗವಂತ".
- If the English source contains "transcendental", render as "ದಿವ್ಯ" or "ಚಿನ್ಮಯ".
- If the English source contains "divine", render as "ದಿವ್ಯ" or "ದೈವಿಕ".
- Translate "deity" as "ವಿಗ್ರಹ" or "ಶ್ರೀಮೂರ್ತಿ" in temple/worship context.
- All Sanskrit shlokas, mantras, and quotes MUST be transliterated accurately into Kannada script with proper pronunciation.
- Do NOT include English parenthetical expressions or English terms in brackets in headings or body text.
"""

    if language_code == "hi":
        return """Hindi-specific rules:
- Use only pure Devanagari script for translated text.
- If the English source contains the name "Krishna", translate/render it as "भगवान श्री कृष्ण".
- In this devotional context, "भगवान" is strictly reserved for Lord Krishna and His Vishnu-tattva forms/avataras (श्री कृष्ण, विष्णु, नारायण, नृसिंह, राम, बलराम, वराह, वामन, आदि).
- Do NOT use "भगवान" for demigods (use "देवता", e.g., "शिव जी" / "महादेव", "ब्रह्मा जी", "इंद्र देव", "श्री गणेश").
- If the English source contains "Supreme Personality of Godhead", render as "परम पुरुषोत्तम भगवान श्री कृष्ण".
- If the English source contains "Personality of Godhead", render as "पुरुषोत्तम भगवान".
- If the English source contains "Supreme Lord", render as "परमेश्वर भगवान".
- If the English source contains "transcendental", render as "दिव्य" or "चिन्मय".
- If the English source contains "divine", render as "दिव्य" or "दैवीय".
- Translate "deity" as "श्री विग्रह" in temple/worship context.
- All Sanskrit shlokas, mantras, and quotes MUST be written accurately in Devanagari script with correct pronunciation.
- Do NOT include English parenthetical expressions or English terms in brackets in headings or body text.
- Philosophy must adhere strictly to Srila Prabhupada's authentic Gaudiya Vaishnava siddhanta.
"""

    if language_code == "te":
        return """Telugu-specific rules:
- Use only pure Telugu script for translated text.
- If the English source contains the name "Krishna", translate/render it as "భగవాన్ శ్రీకృష్ణుడు" or "శ్రీకృష్ణ భగవానుడు".
- In this devotional context, "భగవాన్" / "భగవంతుడు" is strictly reserved for Lord Krishna and His Vishnu-tattva forms/avataras (కృష్ణ, విష్ణు, నారాయణ, నరసింహ, రామ, బలరామ, వరాహ, వామన, మొదలైనవి).
- Do NOT use "భగవాన్" for demigods (use "దేవతలు", e.g., "పరమశివుడు / శివుడు", "బ్రహ్మ దేవుడు", "ఇంద్రుడు", "గణపతి").
- If the English source contains "Supreme Personality of Godhead", render as "పరమ పురుషోత్తమ భగవానుడు".
- If the English source contains "Personality of Godhead", render as "పురుషోత్తమ భగవంతుడు".
- If the English source contains "Supreme Lord", render as "పరమేశ్వరుడైన భగవానుడు".
- If the English source contains "transcendental", render as "దివ్యమైన" or "చిన్మయ".
- If the English source contains "divine", render as "దివ్య" or "దైవిక".
- Translate "deity" as "శ్రీ విగ్రహం" in temple/worship context.
- All Sanskrit shlokas, mantras, and quotes MUST be transliterated accurately into Telugu script.
- Do NOT include English parenthetical expressions or English terms in brackets in headings or body text.
- Philosophy must adhere strictly to Srila Prabhupada's authentic Gaudiya Vaishnava siddhanta.
"""

    if language_code == "ml":
        return """Malayalam-specific rules:
- Use only pure Malayalam script for translated text.
- If the English source contains the name "Krishna", translate/render it as "ഭഗവാൻ ശ്രീകൃഷ്ണൻ".
- In this devotional context, "ഭഗവാൻ" is strictly reserved for Lord Krishna and His Vishnu-tattva forms/avataras (കൃഷ്ണൻ, വിഷ്ണു, നാരായണൻ, നരസിംഹം, രാമൻ, ബലരാമൻ, വരാഹം, വാമനൻ, മുതലായവ).
- Do NOT use "ഭഗവാൻ" for demigods (use "ദേവന്മാർ", e.g., "പരമശിവൻ / മഹാദേവൻ", "ബ്രഹ്മാവ്", "ഇന്ദ്രൻ", "ഗണപതി").
- If the English source contains "Supreme Personality of Godhead", render as "പരമ പുരുഷോത്തമ ഭഗവാൻ".
- If the English source contains "Personality of Godhead", render as "പുരുഷോത്തമനായ ഭഗവാൻ".
- If the English source contains "Supreme Lord", render as "പരമേശ്വരനായ ഭഗവാൻ".
- If the English source contains "transcendental", render as "ദിവ്യമായ" or "ചിന്മയമായ".
- If the English source contains "divine", render as "ദിവ്യ".
- Translate "deity" as "ശ്രീ വിഗ്രഹം" in temple/worship context.
- All Sanskrit shlokas, mantras, and quotes MUST be transliterated accurately into Malayalam script.
- Do NOT include English parenthetical expressions or English terms in brackets in headings or body text.
- Philosophy must adhere strictly to Srila Prabhupada's authentic Gaudiya Vaishnava siddhanta.
"""

    if language_code == "bn":
        return """Bengali-specific rules:
- Use only pure Bengali script for translated text.
- If the English source contains the name "Krishna", translate/render it as "ভগবান শ্রীকৃষ্ণ".
- In this devotional context, "ভগবান" is strictly reserved for Lord Krishna and His Vishnu-tattva forms/avataras (শ্রীকৃষ্ণ, বিষ্ণু, নারায়ণ, নৃসিংহ, রাম, বলরাম, বরাহ, বামন, ইত্যাদি).
- Do NOT use "ভগবান" for demigods (use "দেবগণ", e.g., "মহাদেব / শিবঠাকুর", "ব্রহ্মা", "ইন্দ্র", "শ্রীগণেশ").
- If the English source contains "Supreme Personality of Godhead", render as "পরম পুরুষোত্তম ভগবান শ্রীকৃষ্ণ".
- If the English source contains "Personality of Godhead", render as "পুরুষোত্তম ভগবান".
- If the English source contains "Supreme Lord", render as "পরমেশ্বর ভগবান".
- If the English source contains "transcendental", render as "দিব্য" or "চিন্ময়".
- If the English source contains "divine", render as "দিব্য" or "দৈবী".
- Translate "deity" as "শ্রী বিগ্রহ" in temple/worship context.
- All Sanskrit shlokas, mantras, and quotes MUST be written accurately in Bengali script with proper pronunciation.
- Do NOT include English parenthetical expressions or English terms in brackets in headings or body text.
- Philosophy must adhere strictly to Srila Prabhupada's authentic Gaudiya Vaishnava siddhanta.
"""

    return ""
