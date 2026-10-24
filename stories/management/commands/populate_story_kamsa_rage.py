# -*- coding: utf-8 -*-
import logging
from django.core.management.base import BaseCommand
from stories.models import StoryMainTopic, Story, StoryTranslation, StoryQuestion, StoryQuestionOption

logger = logging.getLogger(__name__)

ARTICLE_EN = """## The Royal Wedding and Kamsa's Sudden Rage

### 1. The Joyous Wedding in Mathura
In the sacred and prosperous city of Mathura, King Surasena ruled with nobility. His virtuous and pious son, **Vasudeva**, was united in holy matrimony with **Devaki**, the beautiful and chaste daughter of King Devaka. 

The royal wedding was celebrated with unmatched opulence and grandeur. King Devaka, overflowing with fatherly affection for his daughter, presented an extraordinary dowry: hundreds of golden chariots studded with dazzling jewels, thousands of caparisoned elephants, magnificent horses, cows, and hundreds of well-decorated maidservants. Musical instruments including mridangas, conch shells, bugles, and kettledrums echoed joyfully throughout the decorated streets of Mathura.

### 2. Kamsa at the Chariot Reins
Devaki’s cousin-brother, **Prince Kamsa**—the ambitious and powerful son of King Ugrasena—wished to show his immense royal affection for the newlyweds. To honor his sister and brother-in-law before the gathered citizens, Kamsa himself took hold of the golden reins and mounted the driver's seat of the wedding chariot. 

As the chariot moved gracefully along the flower-strewn royal avenue, surrounded by royal guards and cheered by thousands of citizens, Kamsa smiled proudly, enjoying the adoration of the people and relishing his role as the affectionate brother and protector of Devaki.

### 3. The Terrifying Voice from the Sky
Suddenly, without warning, the joyous celebrations were shattered. An unembodied, thunderous celestial voice (*Akashavani*) resonated from the heavens, shaking the atmosphere:

> *"O Kamsa, you foolish rascal! You are affectionately driving the chariot of your sister, but you are completely ignorant of your own doom! The eighth child born of her womb will kill you!"*

The words reverberated like a sudden lightning strike across Mathura. The celestial declaration pierced Kamsa's ears with terrifying clarity.

### 4. Demonic Fury Unveiled
Kamsa was not a saintly prince; beneath his royal ornaments lay the heart of an envious and cruel demon. In the Vedic understanding, a demon is one who possesses immense material power but has zero regard for dharma, truth, or loving relationships when his own selfish interest is threatened.

In an instant, all brotherly affection evaporated from Kamsa's heart. Overcome by frantic terror of death and boiling demonic rage, Kamsa dropped the chariot reins. With eyes bulging like fiery coals, he drew his gleaming, double-edged sword from its scabbard. 

Reaching back into the chariot with his left hand, Kamsa ruthlessly seized his newly married sister Devaki by her long, fragrant bridal hair. Raising his sword high above her neck, he prepared to slaughter her mercilessly right before the eyes of the horrified citizens and royal guests!

Devaki trembled violently in sheer terror. Only moments earlier, her brother had been smiling with affection; now, he stood over her like an merciless executioner.

### 5. Vasudeva's Calm Wisdom & Diplomacy
While everyone else was paralyzed with shock, **Vasudeva** remained poised, calm, and deeply thoughtful. He understood that a person consumed by sudden anger and fear of death cannot be pacified by counter-aggression or shouting. As an intelligent and righteous leader, Vasudeva decided to pacify Kamsa through polite praise, philosophical wisdom, and skillful diplomacy.

Standing up respectfully in the chariot, Vasudeva gently raised his hand and spoke with sweet, soothing words:

> *"My dear brother-in-law Kamsa, you are the most renowned and heroic warrior of the Bhoja dynasty. Renowned kings praise your valor and nobility. How can a heroic prince like you commit such a cowardly and abominable act as killing your own innocent sister on the auspicious day of her wedding?"*

Vasudeva then presented profound philosophical truths from the Vedic scriptures regarding the nature of life, the body, and the inevitability of death:

*Srimad-Bhagavatam (Canto 10, Chapter 1, Verse 34):*
> *mṛtyuḥ janmavatāṁ vīra dehena saha jāyate |*  
> *adya vābda-śatānte vā mṛtyur vai prāṇināṁ dhruvaḥ ||*  
>  
> *"O great hero, for every living entity who accepts a material body, death is born along with that body. Whether death comes today or after a hundred years, it is absolutely certain for all embodied souls."*

Vasudeva continued:
> *"When the body perishes, the soul does not die; it simply migrates to another body according to its karma, just as a walking person places one foot firmly on the ground before lifting the other. If you murder your own sister, the heavy reaction of this sinful deed will follow you into your next life, dragging you into the darkest hell. For an illustrious prince like you, infamy and sinful degradation are far worse than death. Therefore, please control your anger and spare her life."*

### 6. The Solemn Vow that Saved Devaki
Despite Vasudeva’s sublime philosophical counseling, Kamsa’s demonic mind remained unmoved. He cared nothing for spiritual consequences, virtue, or future lives; his only obsession was preserving his temporary material body. Seeing that Kamsa was unyielding, Vasudeva applied a second strategy: practical compromise.

Vasudeva reflected: *"A wise person must protect the present danger by whatever means possible. If Devaki lives, there will be time to handle future situations. The future is in the hands of the Supreme Lord."*

Vasudeva looked directly into Kamsa's eyes and made a solemn, unbreakable vow:

> *"O Kamsa, your fear is not from your sister Devaki, but from the sons she will bear in the future. Therefore, I make this solemn promise to you: whenever a child is born to Devaki, I personally will deliver that newborn baby directly into your hands!"*

### 7. Peace Restored
Kamsa knew Vasudeva’s sterling character. Throughout Aryavarta, Vasudeva was renowned as a man of absolute truth (*satya-vakya*) who would rather give up his life than break a promise. Satisfied that his personal safety was guaranteed by Vasudeva's pledge, Kamsa lowered his sword, released Devaki's hair, and resumed his composure.

With heavy hearts and deep contemplation of the mysterious plans of providence, Vasudeva and Devaki proceeded to their new home in Mathura, knowing that the Supreme Lord’s divine arrangement had begun to unfold.

---

### Key Spiritual Lessons:
1. **Material Relationships are Fragile:** Mundane affection based purely on bodily identification vanishes the instant personal survival or selfish interest is challenged, as shown by Kamsa's sudden turn from affectionate brother to would-be murderer.
2. **Facing Danger with Equanimity:** Vasudeva demonstrates how a devotee remains self-controlled in moments of extreme crisis, using patience, intelligence, and diplomacy rather than succumbing to blind panic.
3. **The Inevitability of Death:** Material life is temporary. Fearing death is natural for the conditioned soul, but committing abominable sins to protect the mortal body only guarantees spiritual ruin.
"""

ARTICLE_TA = """## ராஜ திருமணம் மற்றும் கம்சரின் கொடிய கோபம்

### 1. மதுராவில் மங்களகரமான திருமணம்
புனித பூமியான மதுராபுரியில் சூரசேன மன்னரின் குலத்தில் பிறந்தவரும், தர்மத்தின் சிகரமுமான **ஸ்ரீ வசுதேவர்**, தேவக மன்னரின் உன்னத மகளான **தேவகி பிராட்டியை** முறைப்படி மணம் புரிந்தார். 

இந்த மங்களகரமான திருமண விழா அளப்பரிய ஆடம்பரத்துடனும் மகிழ்ச்சியுடனும் நடைபெற்றது. தன் அன்பு மகளுக்கு விடை கொடுக்கும் தருணத்தில் தேவக மன்னர் சீர்வரிசைகளாக நூற்றுக்கணக்கான பொன் தேர்கள், பல்லாயிரக்கணக்கான யானைகள், குதிரைகள், பசுக்கள் மற்றும் சிறந்த தோழியர்களைப் பரிசளித்தார். மத்தளம், சங்கு, பேரிகை உள்ளிட்ட மங்கள வாத்தியங்கள் மதுராவின் வீதிகள் எங்கும் முழங்கின.

### 2. தேரோட்டியாக வந்த கம்சன்
உக்கிரசேன மன்னனின் மகனும், தேவகியின் ஒன்றுவிட்ட சகோதரனுமான **இளவரசன் கம்சன்**, மணமக்களுக்குத் தனது அளப்பரிய பாசத்தை வெளிப்படுத்த விரும்பினான். மணமக்களை கௌரவிக்கும் பொருட்டு, தானே தங்க லகான்களைக் கையில் பிடித்துக் கொண்டு, திருமணத் தேரை மதுராவின் ராஜவீதிகளில் ஓட்டிச் சென்றான். 

மலர் தூவி வாழ்த்திய பல்லாயிரக்கணக்கான மக்களின் ஆரவாரத்தைக் கண்டு கம்சன் கர்வத்துடனும் பெருமகிழ்ச்சியுடனும் தேரைச் செலுத்தினான்.

### 3. வானில் ஒலித்த அதிர்ச்சியூட்டும் அசரீரி
திருமண ஊர்வலம் பேரானந்தத்துடன் சென்றுகொண்டிருந்த வேளையில், திடீரென வானத்திலிருந்து இடிமுழக்கம் போன்ற ஓர் அசரீரி வாக்கு ஒலித்தது:

> *"அடேய் அறிவிலி கம்சா! பாசமுள்ள சகோதரனைப் போல நீ உன் தங்கையின் தேரை ஓட்டிச் செல்கிறாய். ஆனால் உனக்குக் காத்திருக்கும் மரணத்தை நீ அறியவில்லை! இவளது வயிற்றில் பிறக்கப் போகும் எட்டாவது குழந்தையே உன்னைக் கொல்லப் போகிறது!"*

அந்த அசரீரி வாக்கு மின்னல் தாக்கியது போல கம்சனுடைய காதுகளில் விழுந்தது.

### 4. வெளிப்பட்ட அசுர சுபாவம்
கம்சன் வெளித்தோற்றத்தில் இளவரசனாகத் திகழ்ந்தாலும், உள்ளத்தில் கொடிய அசுர சுபாவம் கொண்டவனாக இருந்தான். சொந்த நலனுக்கும் உயிருக்கும் ஆபத்து நேரும் போது பாசம், தர்மம், நியாயம் அனைத்தையும் காலில் போட்டு மிதிப்பவனே அசுரன் ஆவான்.

அசரீரியைக் கேட்ட அடுத்த கணமே கம்சனிடமிருந்த சகோதர பாசம் அனைத்தும் சுவடின்றி மறைந்தது. மரண பயத்தினாலும் கொடிய கோபத்தினாலும் கண்கள் சிவக்க, கம்சன் தேரின் லகான்களைக் கீழே எறிந்தான். தனது உறையிலிருந்து கூர்மையான வாளை உருவினான்.

மணக்கோலத்தில் இருந்த தேவகியின் நீண்ட கூந்தலைப் பற்றிப் பிடித்துக் கீழே இழுத்து, ஊரறிய அவளது தலையைத் துண்டித்துக் கொல்ல வாளை உயர்த்தினான்! 

சில நிமிடங்களுக்கு முன்பு பாசத்தோடு சிரித்த தன் சகோதரன், இப்போது கொலைவெறி கொண்ட எமனாக நிற்பதைக் கண்டு தேவகி தேவி பேரதிர்ச்சியிலும் பயத்திலும் நடுங்கினாள்.

### 5. வசுதேவரின் நிதானமும் ஆன்மீக உபதேசமும்
அங்கிருந்த அனைவரும் திகைத்து நின்ற அந்த இக்கட்டான தருணத்தில், **வசுதேவர்** சிறிதும் பதற்றமடையாமல் மிகுந்த பொறுமையுடனும் ஞானத்துடனும் செயல்பட்டார். கோபத்தில் அறிவை இழந்த ஒருவனை எதிர்த்துக் கூச்சலிடுவதால் எந்தப் பயனும் இல்லை என்பதை அவர் உணர்ந்தார். எனவே இனிமையான வார்த்தைகளாலும், தர்ம சாஸ்திர உண்மைகளாலும் கம்சனை அமைதிப்படுத்த முற்பட்டார்.

வசுதேவர் கம்சனை நோக்கித் தனது கரங்களை உயர்த்திப் பணிவுடன் கூறினார்:

> *"போஜ வம்சத்தின் வீரத் திலகமே கம்சா! மாபெரும் மன்னர்கள் அனைவரும் உனது வீரத்தைப் போற்றுகின்றனர். அப்படிப்பட்ட புகழ்பெற்ற நீ, மங்களகரமான திருமண நாளன்று, எவ்விதக் குற்றமும் செய்யாத உனது சொந்தச் சகோதரியைக் கொன்று தீராத பழியைச் சுமக்கலாமா?"*

தொடர்ந்து, உடலின் நிலையாமையையும் மரணத்தின் தவிர்க்க முடியாத நியதியையும் வசுதேவர் அவனுக்கு நினைவூட்டினார்:

*ஸ்ரீமத் பாகவதம் (ஸ்கந்தம் 10, அத்தியாயம் 1, சுலோகம் 34):*
> *ம்ருத்யு: ஜன்மவதாம் வீர தேஹேன ஸஹ ஜாயதே |*  
> *அத்ய வாப்த-சதாந்தே வா ம்ருத்யுர் வை ப்ராணினாம் துருவ: ||*  
>  
> *"வீரனே! இந்த உலகத்தில் உடல் எடுக்கும் ஒவ்வொரு உயிருக்கும் பிறக்கும் போதே மரணமும் கூடவே பிறந்து விடுகிறது. அந்த மரணம் இன்றே வந்தாலும் சரி, அல்லது நூறு ஆண்டுகளுக்குப் பிறகு வந்தாலும் சரி, உடலெடுத்த அனைத்து ஜீவன்களுக்கும் மரணம் என்பது தவிர்க்க முடியாத உண்மையாகும்."*

வசுதேவர் மேலும் கூறினார்:
> *"நடக்கின்ற ஒரு மனிதன் அடுத்த காலை ஊன்றுவதற்கு முன்பே ஒரு காலைத் தூக்குவது போல, ஜீவாத்மா இந்த உடலை விட்டுப் பிரிந்து தனது கர்ம வினைகளுக்கு ஏற்ப மற்றொரு உடலை அடைகிறது. அப்பாவியான ஒரு பெண்ணைக் கொல்வதால் விளையும் பயங்கர பாவம் உன்னை நரகத்தில் தள்ளும். எனவே உனது கோபத்தைக் கட்டுப்படுத்தி தேவகியைக் காப்பாற்று."*

### 6. தேவகியைக் காத்த சத்திய வாக்குறுதி
வசுதேவரின் தத்துவ உபதேசங்கள் எதனாலும் கம்சனுடைய கல்நெஞ்சம் உருகவில்லை. மறுபிறவி, தர்மம், பாவம் எதைப் பற்றியும் அவனுக்குக் கவலை இல்லை; தனது உடலைக் காப்பாற்றிக் கொள்வது மட்டுமே அவனது ஒரே குறிக்கோளாக இருந்தது. 

இதைக் கண்ட வசுதேவர் சாதுரியமாக ஒரு முடிவுக்கு வந்தார்: *"தற்கால ஆபத்திலிருந்து தேவகியைக் காப்பாற்றுவதே இப்போதைய தலையாய கடமை. எதிர்காலம் பகவானின் திருவுள்ளப்படி நடக்கும்."*

வசுதேவர் கம்சனை நோக்கி ஓர் உறுதியான சத்திய வாக்குறுதியை அளித்தார்:

> *"கம்சா! உனக்கு அச்சம் தேவகியால் அல்ல, அவளுக்குப் பிறக்கும் குழந்தைகளால் தானே? நான் உனக்குச் சத்தியம் செய்து தருகிறேன்: தேவகியின் வயிற்றில் பிறக்கும் ஒவ்வொரு குழந்தையையும் பிறந்தவுடனேயே உனது கைகளில் கொண்டு வந்து ஒப்படைக்கிறேன்!"*

### 7. தற்காலிக அமைதி
வசுதேவர் கொடுத்த வாக்கை ஒருபோதும் மீறாத சத்தியவான் என்பதை கம்சன் நன்கு அறிவான். வசுதேவரின் வாக்குறுதியால் தனக்கு ஆபத்து இல்லை என்று நம்பிய கம்சன், தனது வாளை உறைக்குள் செலுத்தி தேவகியை விடுவித்தான்.

பகவானின் தெய்வீகத் திட்டம் தொடங்கப்பட்டு விட்டதை உணர்ந்த வசுதேவரும் தேவகியும் கலங்கிய மனதுடன் மதுராவில் உள்ள தங்களது இல்லத்திற்குப் புறப்பட்டுச் சென்றனர்.

---

### ஆன்மீகப் பாடங்கள்:
1. **உலகியல் பாசத்தின் நிலையாமை:** ஆன்மீக ஞானமற்ற உலகியல் பாசம் சுயநலமும் மரண பயமும் வரும்போது நொடிப்பொழுதில் மறைந்துவிடும் என்பதை கம்சரின் செயல் காட்டுகிறது.
2. **ஆபத்துக்காலத்தில் பக்தரின் நிதானம்:** கொடிய ஆபத்து நேரும் போது பதற்றமடையாமல், விவேகத்துடனும் பொறுமையுடனும் செயல்பட வேண்டும் என்பதை வசுதேவரின் அணுகுமுறை நமக்குக் கற்பிக்கிறது.
3. **மரணத்தின் தவிர்க்க முடியாத நியதி:** பிறக்கும் ஒவ்வொரு உயிருக்கும் மரணம் நிச்சயம். அழியும் உடலைக் காப்பாற்ற அதர்ம வழியைத் தேர்ந்தெடுப்பது ஆத்மாவிற்குப் பேரழிவையே தரும்.
"""

ARTICLE_HI = """## राजसी विवाह एवं कंस का भयंकर क्रोध

### 1. मथुरा में भव्य वैवाहिक उत्सव
शूरसेन जनपद की राजधानी पावन नगरी मथुरा में परम धर्मात्मा और शांत स्वभाव के **श्री वसुदेव जी** का विवाह राजा देवक की रूपवती और पतिव्रता कन्या **देवकी** के साथ संपन्न हुआ। 

इस वैवाहिक समारोह में राजा देवक ने अपनी प्रिय पुत्री को विदा करते समय अपार दहेज प्रदान किया—सैकड़ों स्वर्ण-जड़ित रथ, सहस्रों हाथी, श्रेष्ठ अश्व, गौएं और सुंदर दासियां। मृदंग, शंख और नगाड़ों की मंगल ध्वनियों से संपूर्ण मथुरा नगरी गुंजायमान हो उठी।

### 2. रथ का सारथी बना कंस
देवकी के चचेरे भाई **राजकुमार कंस** (राजा उग्रसेन के पुत्र) ने नवदंपति के प्रति अपना विशेष स्नेह प्रदर्शित करने के लिए स्वयं रथ की बागडोर थाम ली और सारथी बनकर मथुरा के मुख्य राजमार्ग पर रथ हांकने लगा। 

मार्ग के दोनों ओर खड़े हजारों नागरिकों ने पुष्पवर्षा कर उनका अभिनंदन किया। कंस अपनी बहन के प्रति स्नेह दिखाकर अत्यंत गर्व और प्रसन्नता का अनुभव कर रहा था।

### 3. आकाशवाणी की प्रलयंकारी चेतावनी
किंतु उसी क्षण, समस्त आनंदोत्सव को स्तब्ध कर देने वाली एक भीषण अशरीरी आकाशवाणी गूंज उठी:

> *"अरे मूर्ख कंस! तू जिस बहन को इतने प्रेम से रथ में बैठाकर ले जा रहा है, उसी के गर्भ से उत्पन्न होने वाला आठवां बालक तेरा वध करेगा!"*

यह सुनते ही कंस के पैरों तले से जमीन खिसक गई।

### 4. कंस का आसुरी स्वरूप
कंस मात्र बाह्य रूप से राजकुमार था, भीतर से वह क्रूर और आसुरी प्रवृत्ति का व्यक्ति था। जब किसी स्वार्थी व्यक्ति के प्राणों पर संकट आता है, तो उसका सारा सांसारिक प्रेम एक क्षण में समाप्त हो जाता है।

आकाशवाणी सुनते ही कंस का सारा भ्रातृ-प्रेम क्रोध की ज्वाला में भस्म हो गया। उसने रथ की लगाम फेंक दी, म्यान से चमकती तलवार खींच ली और देवकी के विवाह-केशों को क्रूरतापूर्वक पकड़कर उसका वध करने के लिए तलवार उठा ली!

देवकी भय से थर-थर कांपने लगी। अभी कुछ क्षण पहले जो भाई स्नेह से मुस्कुरा रहा था, वह यमराज बनकर उसके सिर पर खड़ा था।

### 5. वसुदेव जी का धैर्य एवं दार्शनिक विवेक
इस अत्यंत भयावह परिस्थिति में भी **वसुदेव जी** विचलित नहीं हुए। वे जानते थे कि क्रोधाग्नि में जल रहे व्यक्ति को क्रोध से शांत नहीं किया जा सकता। अतः उन्होंने अत्यंत विनम्रता, बुद्धिबल और धर्मशास्त्रों के सिद्धांतों के द्वारा कंस को समझाने का प्रयास किया।

वसुदेव जी ने हाथ जोड़कर कहा:
> *"हे भोजवंश-भूषण वीर कंस! संसार के बड़े-बड़े शूरवीर आपकी कीर्ति का गान करते हैं। आप जैसे पराक्रमी राजकुमार अपनी ही निर्दोष बहन का उसके विवाह के पावन अवसर पर वध करके अपने कुल को कलंकित कैसे कर सकते हैं?"*

तदुपरांत वसुदेव जी ने देह की नश्वरता का परम सत्य उद्घाटित किया:

*श्रीमद्भागवत (स्कंध 10, अध्याय 1, श्लोक 34):*
> *मृत्युः जन्मवतां वीर देहेन सह जायते ।*  
> *अद्य वाब्द-शतान्ते वा मृत्युर् वै प्राणिनां ध्रुवः ॥*  
>  
> *"हे वीर! इस संसार में जन्म लेने वाले प्रत्येक प्राणी के शरीर के साथ ही मृत्यु भी उत्पन्न होती है। वह मृत्यु चाहे आज आए या सौ वर्ष बाद, प्रत्येक देहधारी जीव के लिए मृत्यु अटल और निश्चित है।"*

वसुदेव जी ने समझाया कि शरीर तो वस्त्र के समान बदलता रहता है, किंतु निरपराध स्त्री की हत्या का घोर पाप जीव को कई जन्मों तक नरक की घोर यातनाओं में धकेलता है।

### 6. वह प्रतिज्ञा जिसने देवकी के प्राण बचाए
इतने उच्च आध्यात्मिक उपदेश के बाद भी कंस का आसुरी हृदय नहीं पिघला। उसे केवल अपने नश्वर शरीर की रक्षा की चिंता थी। तब वसुदेव जी ने व्यावहारिक कूटनीति का आश्रय लिया: *"अभी तात्कालिक संकट टालना ही श्रेष्ठ है; भविष्य भगवान के हाथों में है।"*

वसुदेव जी ने दृढ़ स्वर में प्रतिज्ञा की:
> *"हे कंस! तुम्हें देवकी से कोई भय नहीं है, भय केवल उसके होने वाले पुत्रों से है। अतः मैं तुम्हें सत्यनिष्ठ वचन देता हूं कि देवकी के गर्भ से जो भी बालक जन्म लेगा, उसे मैं स्वयं लाकर तुम्हारे हाथों में सौंप दूंगा!"*

### 7. शांति की पुनर्स्थापना
कंस जानता था कि वसुदेव जी परम सत्यवादी हैं और अपने वचन से कभी पीछे नहीं हटते। अतः अपने प्राणों की सुरक्षा के प्रति आश्वस्त होकर उसने तलवार म्यान में रख ली और देवकी को छोड़ दिया।

भगवान की अचिंत्य लीला की पूर्वपीठिका रचते हुए वसुदेव और देवकी भारी मन से अपने गृह की ओर प्रस्थान कर गए।
"""

QUESTIONS_DATA = [
    {
        'en': {
            'q': "Who drove the royal wedding chariot of Vasudeva and Devaki through the streets of Mathura?",
            'options': [
                ("King Ugrasena", False),
                ("Prince Kamsa", True),
                ("King Devaka", False),
                ("Akurura", False),
            ]
        },
        'ta': {
            'q': "மதுராவின் வீதிகளில் வசுதேவர் மற்றும் தேவகியின் திருமணத் தேரை ஓட்டிச் சென்றவர் யார்?",
            'options': [
                ("உக்கிரசேன மன்னர்", False),
                ("இளவரசன் கம்சன்", True),
                ("தேவக மன்னர்", False),
                ("அக்ரூரர்", False),
            ]
        },
        'hi': {
            'q': "मथुरा के राजमार्ग पर वसुदेव जी और देवकी के विवाह-रथ का सारथी कौन बना था?",
            'options': [
                ("राजा उग्रसेन", False),
                ("राजकुमार कंस", True),
                ("राजा देवक", False),
                ("अक्रूर जी", False),
            ]
        }
    },
    {
        'en': {
            'q': "What alarming message did the unembodied voice from the sky (Akashavani) declare to Kamsa?",
            'options': [
                ("Mathura would be conquered by a foreign king", False),
                ("Devaki's eighth child would kill him", True),
                ("His father would disown him from the kingdom", False),
                ("A devastating drought was about to strike Mathura", False),
            ]
        },
        'ta': {
            'q': "வானிலிருந்து ஒலித்த அசரீரி வாக்கு கம்சனுக்கு என்ன எச்சரிக்கை விடுத்தது?",
            'options': [
                ("மதுராபுரி அந்நிய மன்னனால் தாக்கப்படும்", False),
                ("தேவகியின் எட்டாவது குழந்தையே அவனைக் கொல்லும்", True),
                ("அவனது தந்தை அவனை நாட்டை விட்டுத் துரத்துவார்", False),
                ("மதுராவில் பெரும் பஞ்சம் ஏற்படும்", False),
            ]
        },
        'hi': {
            'q': "आकाशवाणी ने कंस को क्या भयंकर चेतावनी दी थी?",
            'options': [
                ("मथुरा पर विदेशी राजा का आक्रमण होगा", False),
                ("देवकी का आठवां बालक उसका वध करेगा", True),
                ("उसके पिता उसे राज्य से निष्कासित कर देंगे", False),
                ("मथुरा में भीषण सूखा पड़ेगा", False),
            ]
        }
    },
    {
        'en': {
            'q': "How did Kamsa react immediately upon hearing the divine omen?",
            'options': [
                ("He abandoned the chariot and fled into the forest", False),
                ("He drew his sword and grabbed Devaki by the hair to kill her", True),
                ("He performed penances to appease the demigods", False),
                ("He asked Vasudeva for spiritual advice", False),
            ]
        },
        'ta': {
            'q': "அசரீரியைக் கேட்டவுடன் கம்சன் உடனடியாக என்ன செய்தான்?",
            'options': [
                ("தேரை விட்டுவிட்டு காட்டிற்கு ஓடினான்", False),
                ("வாளை உருவி தேவகியின் கூந்தலைப் பற்றி அவளைக் கொல்ல முற்பட்டான்", True),
                ("தேவர்களை சமாதானப்படுத்த தவம் செய்யத் தொடங்கினான்", False),
                ("வசுதேவரிடம் ஆன்மீக ஆலோசனை கேட்டான்", False),
            ]
        },
        'hi': {
            'q': "आकाशवाणी सुनते ही कंस की पहली प्रतिक्रिया क्या थी?",
            'options': [
                ("वह रथ छोड़कर वन की ओर भाग गया", False),
                ("उसने तलवार निकाल ली और देवकी के बाल पकड़कर उसे मारने दौड़ा", True),
                ("उसने देवताओं को प्रसन्न करने हेतु तपस्या शुरू कर दी", False),
                ("उसने वसुदेव जी से आध्यात्मिक मार्गदर्शन मांगा", False),
            ]
        }
    },
    {
        'en': {
            'q': "How did Vasudeva conduct himself when confronted with Kamsa's sudden violent fury?",
            'options': [
                ("He drew his own weapons and attacked Kamsa", False),
                ("He remained calm and spoke with gentle diplomacy and wisdom", True),
                ("He jumped out of the chariot and left Devaki behind", False),
                ("He began crying out loudly for the citizens to help him", False),
            ]
        },
        'ta': {
            'q': "கம்சனின் கொலைவெறித் தாக்குதலைக் கண்டு வசுதேவர் எவ்வாறு நடந்து கொண்டார்?",
            'options': [
                ("தானும் ஆயுதத்தை எடுத்து கம்சனைத் தாக்கினார்", False),
                ("பதற்றமின்றி நிதானத்துடனும், சாதுரியமான ஞானத்துடனும் பேசினார்", True),
                ("தேரிலிருந்து குதித்து தேவகியை விட்டுவிட்டு ஓடினார்", False),
                ("உதவி கேட்டு பொதுமக்களை நோக்கிக் கூச்சலிட்டார்", False),
            ]
        },
        'hi': {
            'q': "कंस के अचानक हुए हिंसक आक्रमण के समय वसुदेव जी ने कैसा व्यवहार किया?",
            'options': [
                ("उन्होंने अपने अस्त्र निकाल कर कंस पर प्रहार किया", False),
                ("वे शांत रहे और अत्यंत धैर्य, विनम्रता व विवेक से बात की", True),
                ("वे रथ से कूदकर देवकी को छोड़कर भाग गए", False),
                ("वे सहायता के लिए नागरिकों को पुकारने लगे", False),
            ]
        }
    },
    {
        'en': {
            'q': "According to Srimad-Bhagavatam (10.1.34), what fundamental truth about material existence did Vasudeva remind Kamsa?",
            'options': [
                ("Only evil beings experience death", False),
                ("Death is born along with the body and is certain for every living entity", True),
                ("Death can be permanently avoided through mystic power", False),
                ("Rulers are exempt from the laws of karma and death", False),
            ]
        },
        'ta': {
            'q': "ஸ்ரீமத் பாகவதம் (10.1.34) சுலோகத்தின்படி, வசுதேவர் கம்சனுக்கு நினைவூட்டிய வாழ்வின் அடிப்படை உண்மை என்ன?",
            'options': [
                ("கொடிய மனிதர்களுக்கு மட்டுமே மரணம் சம்பவிக்கிறது", False),
                ("உடலெடுத்த ஒவ்வொரு உயிருக்கும் மரணம் பிறக்கும் போதே நிச்சயிக்கப்பட்டு விடுகிறது", True),
                ("யோக சக்திகளால் மரணத்தை நிரந்தரமாகத் தவிர்க்க முடியும்", False),
                ("மன்னர்களுக்கு கர்ம வினைகளும் மரணமும் கிடையாது", False),
            ]
        },
        'hi': {
            'q': "श्रीमद्भागवत (10.1.34) के अनुसार वसुदेव जी ने कंस को जीवन का कौन-सा शाश्वत सत्य स्मरण कराया?",
            'options': [
                ("केवल दुष्ट व्यक्तियों की ही मृत्यु होती है", False),
                ("जन्म लेने वाले प्रत्येक देहधारी के साथ ही मृत्यु भी निश्चित उत्पन्न होती है", True),
                ("तांत्रिक शक्तियों द्वारा मृत्यु से सदा के लिए बचा जा सकता है", False),
                ("राजाओं पर कर्म और मृत्यु का नियम लागू नहीं होता", False),
            ]
        }
    },
    {
        'en': {
            'q': "What analogy did Vasudeva use to explain the soul's transmigration from one body to another?",
            'options': [
                ("A bird flying from one tree to another", False),
                ("A caterpillar placing one foot forward before lifting the other", True),
                ("A boat crossing from one shore of a river to another", False),
                ("Water evaporating into the clouds", False),
            ]
        },
        'ta': {
            'q': "ஆத்மா ஒரு உடலிலிருந்து மற்றொரு உடலுக்குச் செல்வதை விளக்க வசுதேவர் எந்த உதாரணத்தைக் கூறினார்?",
            'options': [
                ("ஒரு மரத்திலிருந்து மற்றொரு மரத்திற்குப் பறக்கும் பறவை", False),
                ("ஒரு காலை ஊன்றி பின்னரே அடுத்த காலைத் தூக்கும் புழு அல்லது நடக்கும் மனிதன்", True),
                ("ஆற்றின் ஒரு கரையிலிருந்து மறுகரைக்குச் செல்லும் படகு", False),
                ("மேகமாக மாறும் ஆவியாகும் தண்ணீர்", False),
            ]
        },
        'hi': {
            'q': "आत्मा के एक शरीर से दूसरे शरीर में जाने को समझाने हेतु वसुदेव जी ने कौन-सा दृष्टांत दिया?",
            'options': [
                ("एक वृक्ष से दूसरे वृक्ष पर उड़ता पक्षी", False),
                ("घास पर चलने वाला कीड़ा (तृण-जलौका) जो अगला पैर रखने पर ही पिछला पैर उठाता है", True),
                ("नदी के एक तट से दूसरे तट जाती नौका", False),
                ("जल का भाप बनकर आकाश में विलीन होना", False),
            ]
        }
    },
    {
        'en': {
            'q': "Why did Vasudeva first praise Kamsa's dynasty and martial reputation?",
            'options': [
                ("Because Vasudeva genuinely approved of Kamsa's behavior", False),
                ("To appeal to Kamsa's sense of honor and shame to prevent a hasty crime", True),
                ("Because Kamsa had paid him a large amount of wealth", False),
                ("To distract the guards while Devaki escaped", False),
            ]
        },
        'ta': {
            'q': "வசுதேவர் முதலில் கம்சனுடைய வம்சப் பெருமையையும் வீரத்தையும் புகழ்ந்து பேசியதன் நோக்கம் என்ன?",
            'options': [
                ("கம்சனின் செயலை வசுதேவர் உண்மையிலேயே ஆதரித்ததால்", False),
                ("கம்சனுக்கு மான உணர்வையும் குலப்பெருமையையும் நினைவூட்டி அவசரப் பாவத்தைத் தடுக்க", True),
                ("கம்சன் அவருக்கு ஏராளமான செல்வத்தைக் கொடுத்திருந்ததால்", False),
                ("தேவகி தப்பித்து ஓட காவலர்களின் கவனத்தைத் திசைதிருப்ப", False),
            ]
        },
        'hi': {
            'q': "वसुदेव जी ने पहले कंस के वंश और वीरता की प्रशंसा क्यों की?",
            'options': [
                ("क्योंकि वसुदेव जी कंस के आचरण से प्रसन्न थे", False),
                ("ताकि कंस के भीतर कुल-मर्यादा और लज्जा का भाव जगाकर उसे पाप कर्म से रोका जा सके", True),
                ("क्योंकि कंस ने उन्हें धन दिया था", False),
                ("ताकि देवकी के भागने तक सैनिकों का ध्यान भटकाया जा सके", False),
            ]
        }
    },
    {
        'en': {
            'q': "What solemn promise did Vasudeva make to convince Kamsa to spare Devaki's life?",
            'options': [
                ("To give up all his royal kingdom and live as an ascetic in the forest", False),
                ("To personally deliver every child born of Devaki into Kamsa's hands", True),
                ("To never allow Devaki to bear any children", False),
                ("To fight on Kamsa's side in all future wars", False),
            ]
        },
        'ta': {
            'q': "தேவகியின் உயிரைக் காப்பாற்ற வசுதேவர் கம்சனுக்கு என்ன சத்திய வாக்குறுதி அளித்தார்?",
            'options': [
                ("தனது நாட்டைத் துறந்து காட்டில் துறவியாக வாழ்வதாக", False),
                ("தேவகிக்குப் பிறக்கும் ஒவ்வொரு குழந்தையையும் கம்சனிடம் நேரடியாகக் கொண்டு வந்து ஒப்படைப்பதாக", True),
                ("தேவகிக்குக் குழந்தைகள் பிறக்காமல் பார்த்துக் கொள்வதாக", False),
                ("வருங்காலப் போர்களில் கம்சனுக்கு ஆதரவாகப் போரிடுவதாக", False),
            ]
        },
        'hi': {
            'q': "देवकी के प्राणों की रक्षा हेतु वसुदेव जी ने कंस को क्या वचन दिया?",
            'options': [
                ("वे अपना राजपाट त्याग कर वन में सन्यासी बन जाएंगे", False),
                ("देवकी के गर्भ से उत्पन्न प्रत्येक बालक को वे स्वयं कंस के हाथों में सौंप देंगे", True),
                ("वे देवकी से कोई संतान उत्पन्न नहीं होने देंगे", False),
                ("वे भविष्य के सभी युद्धों में कंस का साथ देंगे", False),
            ]
        }
    },
    {
        'en': {
            'q': "Why did Kamsa accept Vasudeva's promise and sheath his sword?",
            'options': [
                ("Because he feared Vasudeva's martial prowess in combat", False),
                ("Because Vasudeva was widely known as a man of absolute truth who never broke his word", True),
                ("Because the celestial voice commanded him to spare her", False),
                ("Because King Ugrasena arrived and ordered Kamsa to stop", False),
            ]
        },
        'ta': {
            'q': "வசுதேவரின் வாக்குறுதியை ஏற்றுக்கொண்டு கம்சன் தனது வாளை உறைக்குள் போட்டதன் காரணம் என்ன?",
            'options': [
                ("வசுதேவருடன் போரிடப் பயந்ததால்", False),
                ("வசுதேவர் ஒருபோதும் சத்தியத்தை மீறாத உத்தமர் என்பதை அறிந்திருந்ததால்", True),
                ("அவளைக் கொல்ல வேண்டாம் என்று அசரீரி மீண்டும் கட்டளையிட்டதால்", False),
                ("உக்கிரசேன மன்னர் அங்கு வந்து கம்சனைத் தடுத்ததால்", False),
            ]
        },
        'hi': {
            'q': "कंस ने वसुदेव जी के वचन पर विश्वास करके तलवार म्यान में क्यों रख ली?",
            'options': [
                ("क्योंकि वह वसुदेव जी के बाहुबल से डर गया था", False),
                ("क्योंकि वसुदेव जी परम सत्यवादी के रूप में प्रसिद्ध थे और कभी वचन नहीं तोड़ते थे", True),
                ("क्योंकि आकाशवाणी ने उसे रुकने का आदेश दिया था", False),
                ("क्योंकि राजा उग्रसेन ने आकर उसे रोक दिया था", False),
            ]
        }
    },
    {
        'en': {
            'q': "What vital spiritual lesson does Vasudeva's conduct teach devotees when facing sudden crisis?",
            'options': [
                ("To surrender to fear and despair immediately", False),
                ("To remain peaceful, use practical intelligence, and rely on the Supreme Lord's ultimate protection", True),
                ("To compromise spiritual principles and join the wrongdoers", False),
                ("To retaliate with unbridled anger and physical violence", False),
            ]
        },
        'ta': {
            'q': "திடீர் ஆபத்துக்கள் நேரும் போது எவ்வாறு செயல்பட வேண்டும் என்பதை வசுதேவரின் நடத்தை நமக்கு எவ்வாறு கற்பிக்கிறது?",
            'options': [
                ("பயத்திற்கும் விரக்திக்கும் உடனே அடிபணிந்து விடுவது", False),
                ("மன அமைதியோடும், விவேகத்தோடும் செயல்பட்டு, பகவானின் முழு பாதுகாப்பைச் சார்ந்திருப்பது", True),
                ("ஆன்மீகக் கொள்கைகளை விட்டுக்கொடுத்து தீயவர்களுடன் சேர்ந்து விடுவது", False),
                ("கட்டுப்பாடற்ற கோபத்துடனும் வன்முறையுடனும் பதிலடி கொடுப்பது", False),
            ]
        },
        'hi': {
            'q': "अचानक आए संकट के समय वसुदेव जी का आचरण हमें क्या आध्यात्मिक शिक्षा देता है?",
            'options': [
                ("भय और निराशा के आगे तुरंत घुटने टेक देना चाहिए", False),
                ("क्रोध त्यागकर धैर्य, विवेक और भगवान के संरक्षण पर पूर्ण विश्वास रखना चाहिए", True),
                ("अपने सिद्धांतों से समझौता कर अधर्मियों का साथ देना चाहिए", False),
                ("अंधे क्रोध और प्रतिशोध की भावना से कार्य करना चाहिए", False),
            ]
        }
    }
]


class Command(BaseCommand):
    help = 'Populate Story 2: The Royal Wedding and Kamsa’s Sudden Rage under Krishna Pastimes'

    def handle(self, *args, **options):
        topic = StoryMainTopic.objects.get(id=2)
        slug = 'krishna-pastimes-the-royal-wedding-and-kamsas-sudden-rage'
        image_path = 'stories/images/kamsa_wedding_rage.jpg'

        story, created = Story.objects.get_or_create(
            slug=slug,
            defaults={
                'topic': topic,
                'order': 1,
                'imagePath': image_path,
            }
        )
        if not created:
            story.topic = topic
            story.order = 1
            story.imagePath = image_path
            story.save()

        # Translations
        trans_data = {
            'en': ('Krishna Pastimes', "The Royal Wedding and Kamsa's Sudden Rage", ARTICLE_EN),
            'ta': ('கிருஷ்ண லீலைகள்', "ராஜ திருமணம் மற்றும் கம்சரின் கொடிய கோபம்", ARTICLE_TA),
            'hi': ('श्रीकृष्ण की दिव्य लीलाएँ', "राजसी विवाह एवं कंस का भयंकर क्रोध", ARTICLE_HI),
        }

        created_trans = {}
        for lang, (main_topic, sub_topic, article) in trans_data.items():
            tr, _ = StoryTranslation.objects.get_or_create(
                story=story,
                language_code=lang,
                defaults={
                    'mainTopic': main_topic,
                    'subTopic': sub_topic,
                    'article': article,
                }
            )
            tr.mainTopic = main_topic
            tr.subTopic = sub_topic
            tr.article = article
            tr.save()
            created_trans[lang] = tr
            self.stdout.write(f"Saved translation for {lang}")

        # Questions
        for idx, q_item in enumerate(QUESTIONS_DATA, start=1):
            for lang in ['en', 'ta', 'hi']:
                tr = created_trans[lang]
                data = q_item[lang]

                question, _ = StoryQuestion.objects.get_or_create(
                    translation=tr,
                    order=idx,
                    defaults={'question_text': data['q']}
                )
                question.question_text = data['q']
                question.save()

                # Options
                question.options.all().delete()
                for opt_idx, (opt_text, is_correct) in enumerate(data['options'], start=1):
                    StoryQuestionOption.objects.create(
                        question=question,
                        option_text=opt_text,
                        order=opt_idx,
                        is_correct=is_correct
                    )

        self.stdout.write(self.style.SUCCESS(f"Successfully populated Story 2 (ID: {story.id}) with translations and questions!"))
