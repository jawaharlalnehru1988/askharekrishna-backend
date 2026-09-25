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
"""

    return ""
