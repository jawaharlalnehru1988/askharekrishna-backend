"""
Shared translation rule snippets for devotional content modules.
"""


def get_language_specific_rules(target_language: str) -> str:
    language_code = (target_language or "").lower()

    if language_code == "ta":
        return """Tamil-specific rules:
- Strictly adhere to authentic Gaudiya Vaishnava siddhanta (teachings of Srila Prabhupada / AC Bhaktivedanta Swami).
- Use only Tamil script for translated Tamil text. Do NOT mix in Devanagari or any other Indic script.
- If a Sanskrit devotional term must be retained, write it in Tamil script, not Devanagari.
- If the English source contains the name "Krishna", translate/render it as "பகவான் ஸ்ரீ கிருஷ்ணர்".
- In this devotional context, "பகவான்" is reserved for Lord Krishna and His Vishnu-tattva forms/avataras (for example: நரசிம்ஹர், விஷ்ணு, நாராயணர், மதுசூதனர், கோபாலர், கிரிதாரி, கேசவர், மாதவர், கோவிந்தர், திரிவிக்ரமர், ராமர், பலராமர், கல்கி, புத்தர், பரசுராமர், வாமனர், ஸ்ரீதரர், தாமோதரர்).
- Tamil terms for Bhagavan: strictly use பகவான், பகவானின், பகவானே, பகவானை, பகவானுக்கு, பகவானிடம், பகவானால்.
- Do NOT translate "Lord" or "God" as "ஆண்டவர்", "ஆண்டவரே", "ஆண்டவரின்", "ஆண்டவரை", "ஆண்டவருக்கு", or "கர்த்தர்".
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
- Translate "deity" as "விக்ரஹம்" in devotional temple/worship context.
- Do NOT translate "deity" as "தெய்வம்" in this devotional context.
- Instead of using the words "இந்து" or "இந்து மதம்", strictly use "சனாதன" or "சனாதன தர்மம்" (for example: "சனாதன தர்மம்", "சனாதன தத்துவ", "சனாதன பாரம்பரியம்", "சனாதன தர்மத்தைப் பின்பற்றுவோர்").
- Do NOT include English parenthetical expressions or English words in brackets (e.g., '(research)', '(stress)', '(brain waves)', '(theory)', '(The Postbox Analogy)', '(Omnipresent)', '(Translation)') in headings or body text. Tamil vocabulary is rich and self-sufficient. Use the appropriate Tamil word directly without parenthetical English crutches.
- All Sanskrit shlokas, verses, mantras, and quotes MUST be transliterated accurately into Tamil script. Do NOT leave shlokas in English, Roman, or IAST script.
- In Tamil transliterations of Sanskrit shlokas, mantras, and sandhi compounds, the Sanskrit visarga (ः / ḥ) must strictly be written with a colon (':'), e.g., 'ராம:', 'தர்ம:', 'ஸ:', 'ய:', 'ஜனா:', 'து:கம்', 'அந்த:புரம்'. NEVER use the Tamil Aytham letter ('ஃ') for Sanskrit Visarga (never write 'ராமஃ', 'தர்மஃ', 'துஃகம்'). The letter 'ஃ' is exclusively reserved for authentic native Tamil words ('எஃகு', 'அஃது') or loanwords with 'f'.
- No personal or organizational attacks: strictly avoid personal attacks or attacks against organizations/movements (never use aggressive rhetoric like 'சாட்டையடி', 'மோசடி'). Refute the proposition or misconception objectively by quoting it in context first, then analyzing with scriptural and historical evidence.
"""

    if language_code == "kn":
        return """Kannada-specific rules:
- Strictly adhere to authentic Gaudiya Vaishnava siddhanta (teachings of Srila Prabhupada / AC Bhaktivedanta Swami).
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
- Do NOT include English parenthetical expressions or English words in brackets (e.g., '(research)', '(stress)', '(brain waves)', '(theory)') in headings or body text. The regional language is self-sufficient; do NOT place English words in brackets after regional words.
"""

    if language_code == "hi":
        return """Hindi-specific rules:
- Strictly adhere to authentic Gaudiya Vaishnava siddhanta (teachings of Srila Prabhupada / AC Bhaktivedanta Swami).
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
- Do NOT include English parenthetical expressions or English words in brackets (e.g., '(research)', '(stress)', '(brain waves)', '(theory)') in headings or body text. The regional language is self-sufficient; do NOT place English words in brackets after regional words.
- Philosophy must adhere strictly to Srila Prabhupada's authentic Gaudiya Vaishnava siddhanta.
"""

    if language_code == "te":
        return """Telugu-specific rules:
- Strictly adhere to authentic Gaudiya Vaishnava siddhanta (teachings of Srila Prabhupada / AC Bhaktivedanta Swami).
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
- Do NOT include English parenthetical expressions or English words in brackets (e.g., '(research)', '(stress)', '(brain waves)', '(theory)') in headings or body text. The regional language is self-sufficient; do NOT place English words in brackets after regional words.
- Philosophy must adhere strictly to Srila Prabhupada's authentic Gaudiya Vaishnava siddhanta.
"""

    if language_code == "ml":
        return """Malayalam-specific rules:
- Strictly adhere to authentic Gaudiya Vaishnava siddhanta (teachings of Srila Prabhupada / AC Bhaktivedanta Swami).
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
- Do NOT include English parenthetical expressions or English words in brackets (e.g., '(research)', '(stress)', '(brain waves)', '(theory)') in headings or body text. The regional language is self-sufficient; do NOT place English words in brackets after regional words.
- Philosophy must adhere strictly to Srila Prabhupada's authentic Gaudiya Vaishnava siddhanta.
"""

    if language_code == "bn":
        return """Bengali-specific rules:
- Strictly adhere to authentic Gaudiya Vaishnava siddhanta (teachings of Srila Prabhupada / AC Bhaktivedanta Swami).
- Use only pure Bengali script for translated text.
- If the English source contains the name "Krishna", translate/render it as "ভগবান শ্রীকৃষ্ণ".
- In this devotional context, "ভগবান" is strictly reserved for Lord Krishna and His Vishnu-tattva forms/avataras (শ্রীকৃষ্ণ, বিষ্ণু, নারায়ণ, নৃসিংহ, রাম, বলরাম, বরাহ, বামন, ইত্যাদি).
- Do NOT use "ভগবান" for demigods (use "দেবগণ", e.g., "মহাদেব / শিবঠাকুর", "ব্রহ্মা", "ইন্দ্র", "শ্রীগণেশ").
- If the English source contains "Supreme Personality of Godhead", render as "পরম পুরুষোত্তম ভগবান শ্রীকৃষ্ণ".
- If the English source contains "Personality of Godhead", render as "পুরুষোত্তম ভগবান".
- If the English source contains "Supreme Lord", render as "পরমেশ্বর ভগবান".
- If the English source contains "transcendental", render as "দিব্য" or "চিন্ময়".
- If the English source contains "divine", render as "দিব্য" or "দৈবী".
- Translate "deity" as "শ্রী বিग्रह" in temple/worship context.
- All Sanskrit shlokas, mantras, and quotes MUST be written accurately in Bengali script with proper pronunciation.
- Do NOT include English parenthetical expressions or English words in brackets (e.g., '(research)', '(stress)', '(brain waves)', '(theory)') in headings or body text. The regional language is self-sufficient; do NOT place English words in brackets after regional words.
- Philosophy must adhere strictly to Srila Prabhupada's authentic Gaudiya Vaishnava siddhanta.
"""

    if language_code == "en":
        return """English-specific rules:
- Strictly adhere to authentic Gaudiya Vaishnava siddhanta (teachings of Srila Prabhupada / AC Bhaktivedanta Swami).
- Follow the Srila Prabhupada Standard of Direct Clarity: write in simple, plain, and powerful English that ordinary people, students, and seekers can easily understand.
- Do NOT use pretentious, fancy English, academic jargon, or thesaurus words (e.g., strictly avoid 'ontological chasm', 'epistemological framework', 'mechanistic materialism wielded as a bludgeon', 'anthropocene', 'dialectician', 'apologist', 'preceding treatise', 'qualia').
- Use plain, devotional equivalents: use 'devotee' instead of 'apologist/dialectician', 'previous discussion' instead of 'preceding treatise', 'spiritual reality' instead of 'ontological reality'.
- Use direct, relatable analogies following Srila Prabhupada's style (e.g., watch in the desert, car and driver, pocket dictionary, puppet and puppeteer).
- No personal or organizational attacks: strictly avoid ad hominem attacks against individuals, organizations, or political movements. Attack only the false opinion or proposition using scripture and facts. If counteracting an opposing party, quote the exact statement in context first, then analyze it objectively.
"""

    return ""


def get_debate_editorial_rules() -> str:
    """
    Standard editorial rules for philosophical and debate articles.
    """
    return """Debate & Philosophical Article Standards:
1. No Personal or Organizational Attacks: Never make ad hominem attacks against specific persons, organizations, political parties, or communities.
2. Refute Propositions with Evidence: Direct all criticism strictly against the opinion, misconception, or false proposition using authentic scriptural proofs (shabda-pramana), historical facts, and sound logic.
3. Quotation and Analysis Method: When addressing opposing claims, quote the exact statement or premise in context first, and then methodically analyze and refute it respectfully and objectively.
4. Follow Srila Prabhupada's style of clarity, dignified presentation, and authentic Gaudiya Vaishnava siddhanta.
5. Explicit Scriptural Citation & Hierarchical Section Naming: Never use bare numbers like '(6.22.21–24)' or '(11.33)'. Explicitly label authentic hierarchical divisions in the target language:
   - Valmiki Ramayana: Kanda -> Sarga -> Shloka (e.g. 'யுத்த காண்டம், சர்க்கம் 22, சுலோகங்கள் 21–24' / 'Yuddha-kanda, Sarga 22, Verses 21–24' / 'युद्धकाण्ड, सर्ग 22, श्लोक 21–24').
   - Bhagavad Gita: Chapter -> Shloka (e.g. 'பகவத் கீதை, அத்தியாயம் 11, சுலோகம் 33' / 'Bhagavad-gita, Chapter 11, Verse 33').
   - Srimad Bhagavatam: Canto -> Chapter -> Verse (e.g. 'ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 5, அத்தியாயம் 19, சுலோகம் 5' / 'Srimad-Bhagavatam, Canto 5, Chapter 19, Verse 5').
   - Sri Caitanya Caritamrta: Lila -> Chapter -> Text/Verse (e.g. 'ஸ்ரீ சைதன்ய சரிதாம்ருதம், மத்திய லீலை, அத்தியாயம் 9, சுலோகம் 206').
"""

