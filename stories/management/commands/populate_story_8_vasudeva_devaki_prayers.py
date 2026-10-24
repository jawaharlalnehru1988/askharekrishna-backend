import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askharekrishna_backend.settings')
django.setup()

from django.core.management.base import BaseCommand
from stories.models import StoryMainTopic, Story, StoryTranslation, StoryQuestion, StoryQuestionOption

class Command(BaseCommand):
    help = "Populate Story 8: Vasudeva and Devaki's Heartfelt Prayers to the Newborn Lord across 7 languages"

    def handle(self, *args, **options):
        topic = StoryMainTopic.objects.get(name="Krishna Pastimes")

        story_slug = "krishna-pastimes-vasudeva-and-devakis-prayers-to-the-newborn-lord"
        image_path = "stories/images/devaki_vasudeva_prayers.jpg"

        story, created = Story.objects.get_or_create(
            slug=story_slug,
            defaults={
                "topic": topic,
                "order": 7,
                "imagePath": image_path,
            }
        )
        if not created:
            story.topic = topic
            story.order = 7
            story.imagePath = image_path
            story.save()

        stories_data = {
            "en": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "Vasudeva and Devaki's Heartfelt Prayers to the Newborn Lord",
                "content": """### Vasudeva's Philosophical Adoration

Standing in the stone dungeon of Mathura, illuminated by the radiant golden-blue aura of the newborn child, Vasudeva folded his hands with deep reverence. He understood with complete philosophical clarity that the child before him was not an ordinary mortal offspring, but the transcendental Supreme Personality of Godhead, Lord Śrī Viṣṇu Himself.

Vasudeva prayed: "My dear Lord, You are the original transcendental Person, existing beyond the cosmic manifestation and beyond the three modes of material nature—goodness, passion, and ignorance. By Your spiritual energy, You create, maintain, and dissolve the entire material cosmos, yet You remain eternally untouched by material qualities. Just as a light shines through a glass window without being altered by the glass, You have entered the material universe and appeared before us in Your original spiritual form."

Vasudeva then expressed his practical apprehension: "Lord, the atrocious King Kamsa has already slaughtered all our previous six newborn babies because of the celestial voice that foretold his death at Your hands. As soon as his spies and guards report Your appearance, he will immediately rush here with weapons to take Your life. Therefore, we pray for Your protection."

### Mother Devaki's Loving Maternal Plea

Hearing Vasudeva's prayers, Mother Devaki gazed upon the Lord with a heart overflowing with maternal affection (*vātsalya-rasa*). While Vasudeva saw the Lord primarily with awe and reverence (*śānta* and *dāsya*), Devaki's motherly instincts overwhelmed her. She trembled in anxiety for the physical safety of her divine child.

Devaki offered her fervent prayers: "My Lord, the entire cosmic creation, with all its planetary systems, rests safely within Your abdomen during the cosmic annihilation. Yet, by Your inconceivable sweet mercy, You have now appeared from my womb! You are Time itself, the inexorable force that destroys all mundane powers. Even the powerful demigods run in fear of Your formidable Time factor. But now, King Kamsa, who is puffed up with demonic pride, seeks to harm You."

Then, with folded hands and tearful eyes, Mother Devaki made a tender, heartfelt request:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 3, Verse 31**
> 
> *upasaṁhara viśvātman rūpam etat catur-bhujam*  
> *yāt te chāndasam etac ca rāma-lakṣma-dharāyudham*  
> 
> **Translation:** O Soul of the universe, please withdraw this four-armed transcendental form of Yours, which holds the weapons of conchshell, disc, club, and lotus flower, and which is adorned with all the celestial ornaments of the spiritual world. Please conceal this majestic form from mortal vision!

Devaki pleaded: "My dear son, if Kamsa sees this magnificent four-armed form holding weapons and adorned with jewels, he will immediately know that You are the Supreme Lord who has descended to slay him. Please, withdraw this form and appear as an ordinary, two-armed human infant so that we may keep You safe from Kamsa's wrath!"

### The Lord Reveals Their Three Past Lifetimes

Smiling with tender compassion upon His loving parents, the Supreme Lord addressed Vasudeva and Devaki with soothing, nectar-like words. He explained that this was not the first time they were playing the role of His father and mother.

1. **Their First Birth (Sutapa and Pṛśni):**  
   In the Svāyambhuva manvantara, Vasudeva was the Prajāpati named Sutapa, and Devaki was his chaste wife Pṛśni. Desiring to have a child equal to the Lord, they performed severe austerities for twelve thousand celestial years. When the Supreme Lord appeared before them and offered any benediction, they asked three times: "We desire a son exactly like You!" Because no one else in the entire existence is equal to the Lord, the Lord Himself agreed to become their son. Thus, the Lord appeared as their child named **Pṛśnigarbha**.

2. **Their Second Birth (Kaśyapa and Aditi):**  
   In their next lifetime, Sutapa took birth as the great sage Kaśyapa, and Pṛśni took birth as Mother Aditi, the mother of the demigods. Remembering His eternal promise, the Supreme Lord appeared as their son **Upendra** (the dwarf-incarnation, Lord Vāmanadeva), who restored the heavenly kingdom to King Indra.

3. **Their Third Birth (Vasudeva and Devaki):**  
   Now, in their third lifetime, they had taken birth as Vasudeva and Devaki in Mathura. The Lord had descended personally as **Śrī Kṛṣṇa** to fulfill His promise for the third time and complete their eternal parental relationship.

The Lord explained: "I have manifested this four-armed Viṣṇu form before your eyes first so that you may recognize My supreme identity without any doubt and remember My eternal relationship with you across all your births. Otherwise, if I had appeared merely as an ordinary human child, you might not have realized that the Supreme Personality of Godhead had entered your family."

Having comforted their hearts and revived their spiritual memories, the Lord prepared to fulfill Devaki's loving desire by assuming the form of an infant.""",
                "questions": [
                    {
                        "question": "How did Vasudeva describe the Supreme Lord's relationship to the three modes of material nature?",
                        "options": [
                            {"text": "The Lord is transcendental and completely untouched by the material modes", "is_correct": True},
                            {"text": "The Lord is bound by the mode of goodness", "is_correct": False},
                            {"text": "The Lord is controlled by material passion", "is_correct": False},
                            {"text": "The Lord is a product of material nature", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What primary fear did Vasudeva express regarding King Kamsa?",
                        "options": [
                            {"text": "That Kamsa's guards would discover the Lord and rush to attack Him with weapons", "is_correct": True},
                            {"text": "That Kamsa would demand more taxes", "is_correct": False},
                            {"text": "That Kamsa would banish them to a distant kingdom", "is_correct": False},
                            {"text": "That Kamsa would refuse to feed them", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What loving request did Mother Devaki make to the newborn Lord?",
                        "options": [
                            {"text": "To withdraw His four-armed form and appear as an ordinary two-armed child", "is_correct": True},
                            {"text": "To summon an army of demigods immediately", "is_correct": False},
                            {"text": "To fly them away in a celestial chariot", "is_correct": False},
                            {"text": "To turn the prison into a golden palace", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Why did Mother Devaki want the Lord to conceal His four-armed form?",
                        "options": [
                            {"text": "So that cruel King Kamsa would not easily identify Him as the Supreme Lord", "is_correct": True},
                            {"text": "Because the four arms were too heavy to carry", "is_correct": False},
                            {"text": "Because she disliked celestial jewelry", "is_correct": False},
                            {"text": "Because the light was too dazzling for her eyes", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Who were Vasudeva and Devaki in their first past lifetime when they performed austerities?",
                        "options": [
                            {"text": "Sutapa and Prisni", "is_correct": True},
                            {"text": "Kashyapa and Diti", "is_correct": False},
                            {"text": "Dasharatha and Kaushalya", "is_correct": False},
                            {"text": "Manu and Shatarupa", "is_correct": False}
                        ]
                    },
                    {
                        "question": "As which incarnation did the Supreme Lord appear to Sutapa and Prisni?",
                        "options": [
                            {"text": "Prisnigarbha", "is_correct": True},
                            {"text": "Matsya", "is_correct": False},
                            {"text": "Kurma", "is_correct": False},
                            {"text": "Narasimha", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Who were Vasudeva and Devaki in their second past lifetime?",
                        "options": [
                            {"text": "Kashyapa and Aditi", "is_correct": True},
                            {"text": "Janaka and Sunayana", "is_correct": False},
                            {"text": "Angira and Shraddha", "is_correct": False},
                            {"text": "Pulastya and Havirbhu", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Which incarnation of the Supreme Lord was born as the son of Kashyapa and Aditi?",
                        "options": [
                            {"text": "Lord Vamanadeva (Upendra)", "is_correct": True},
                            {"text": "Lord Parashurama", "is_correct": False},
                            {"text": "Lord Varaha", "is_correct": False},
                            {"text": "Lord Buddha", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Why did the Supreme Lord show His four-armed form to Vasudeva and Devaki first?",
                        "options": [
                            {"text": "To confirm His divine identity and revive their remembrance of their eternal bond", "is_correct": True},
                            {"text": "To frighten them into obedience", "is_correct": False},
                            {"text": "To demonstrate His physical strength", "is_correct": False},
                            {"text": "To test whether they could recognize His weapons", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How many times across their lifetimes did the Lord fulfill His promise to be their son?",
                        "options": [
                            {"text": "Three times", "is_correct": True},
                            {"text": "Only once", "is_correct": False},
                            {"text": "Five times", "is_correct": False},
                            {"text": "Seven times", "is_correct": False}
                        ]
                    }
                ]
            },
            "ta": {
                "mainTopic": "கிருஷ்ண லீலைகள்",
                "subTopic": "வசுதேவர் மற்றும் தேவகியின் திவ்ய பிரார்த்தனைகள்",
                "content": """### வசுதேவரின் தத்துவார்த்த போற்றுதல்

மதுராவின் சிறைக் கொட்டடியில், புதிதாக அவதரித்த குழந்தையின் தங்க-நீல திவ்ய ஒளியில் நனைந்தபடி, வசுதேவர் கைகூப்பி பணிவுடன் நின்றார். தமக்கு முன்னே தோன்றிய குழந்தை சாதாரண மானிடக் குழந்தை அல்ல; சத்வ, ரஜோ, தமோ குணங்களைக் கடந்த முழுமுதற் கடவுளான பகவான் ஸ்ரீ விஷ்ணுவே என்பதை வசுதேவர் தத்துவார்த்தமாக பூரணமாக உணர்ந்தார்.

வசுதேவர் பிரார்த்தித்தார்: "அன்புள்ள பகவானே! நீர் பௌதிகப் பிரபஞ்சத்திற்கும் முக்குணங்களுக்கும் அப்பாற்பட்ட ஆதிபுருஷர். உமது திவ்ய ஆன்மீக சக்தியினால் நீர் இந்த அகிலங்களை சிருஷ்டித்து, காத்து, அழிக்கின்றீர்; ஆயினும் ஒருபோதும் ஜடகுணங்களால் தீண்டப்படுவதில்லை. கண்ணாடி வழியே ஒளி புகுந்தாலும், அந்தக் கண்ணாடி ஒளியை மாற்ற முடியாதது போல, நீர் ஜட உலகினுள் பிரவேசித்த போதிலும் உமது நித்திய ஆன்மீக சொரூபத்திலேயே அவதரித்துள்ளீர்."

தொடர்ந்து வசுதேவர் தமது நடைமுறை கவலையைத் தெரிவித்தார்: "பகவானே! உமது கரங்களால் தனக்கு மரணம் நிகழும் என்ற அசரீரி வாக்கை கேட்டு, கொடுங்கோலன் கம்சன் எங்களின் முந்தைய ஆறு குழந்தைகளையும் கொடூரமாகக் கொன்றான். நீர் அவதரித்த செய்தி அவனது ஒற்றர்களுக்கும் காவலாளிகளுக்கும் தெரிந்த உடனே, அவன் ஆயுதங்களோடு விரைந்து வந்து உம்மைத் தாக்க முற்படுவான். எனவே, எங்களை காத்தருள வேண்டும் பகவானே!"

### தாய் தேவகியின் வாத்ஸல்ய வேண்டுகோள்

வசுதேவரின் பிரார்த்தனைகளைக் கேட்ட தாய் தேவகி, எல்லையற்ற தாய்மைப் பாசத்தோடு (*வாத்ஸல்ய ரஸம்*) பகவானைத் தரிசித்தார். வசுதேவர் பகவானை பயபக்தியோடு நோக்கினார்; ஆனால் தேவகியின் தாய்மை உள்ளமோ தனது திவ்யக் குழந்தையின் பாதுகாப்பைக் குறித்து ஏங்கித் தவித்தது.

தேவகி பக்தியோடு பிரார்த்தித்தார்: "பகவானே! பிரளய காலத்தில் அனைத்து அண்ட சராசரங்களையும் உமது திருவுதரத்தினுள் அடக்கிக் காக்கின்றீர். அத்தகைய உன்னத பகவான், உமது எல்லையற்ற கருணையினால் அடியவளின் கர்ப்பத்தில் தோன்றியுள்ளீர்! அனைத்து உலக சக்திகளையும் அழிக்கவல்ல காலமே நீர்தான். சக்திவாய்ந்த தேவர்களும் உமது கால சக்தியைக் கண்டு அஞ்சுகின்றனர். ஆனால், அசுர கர்வத்தால் மதியிழந்த கம்சன் உமக்குத் தீங்கு செய்ய முனைகிறான்."

பின்னர், கண்களில் ஆனந்தக் கண்ணீரோடு கை கூப்பியபடி, தாய் தேவகி உள்ளம் உருகும் ஒரு மென்மையான வேண்டுகோளை வைத்தார்:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 3, சுலோகம் 31**
> 
> *உபஸம்ஹர விஶ்வாத்மன் ரூபம் ஏதத் சதுர்புஜம் |*  
> *யாத் தே சாந்தஸம் ஏதச் ச ராம-லக்ஷ்ம-தராயுதம் ||*  
> 
> **பொருள்:** அகிலத்தின் ஆத்மாவான பகவானே! சங்கு, சக்கரம், கதை, தாமரையை ஏந்தியுள்ள இந்த திவ்ய நான்கு கர ரூபத்தையும், ஆன்மீக லோகத்தின் ஆபரணங்களையும் தயவுசெய்து மறைத்துக் கொள்வீராக. மனித கண்களுக்குத் தெரியாதவாறு இந்த கம்பீர ரூபத்தை மறைத்து அருள்வீராக!

தேவகி மன்றாடினார்: "மகனே! ஆயுதங்களை ஏந்தி ஆபரணங்கள் மின்னும் இந்த உன்னத நான்கு கர ரூபத்தை கம்சன் கண்டால், தன்னை வதம் செய்ய வந்த முழுமுதற் கடவுள் நீரே என்பதை உடனே அறிந்துகொள்வான். எனவே, இந்த உன்னத ரூபத்தை மறைத்துக் கொண்டு, எளிய இரண்டு கரங்கள் கொண்ட மானிடக் குழந்தையாகத் தோன்றி எங்களை கம்சனின் கோபத்திலிருந்து காப்பாற்றுங்கள்!"

### தங்களின் கடந்த மூன்று பிறவிகளை வெளிப்படுத்திய பகவான்

தமது பெற்றோரின் தூய அன்பைக் கண்டு கருணையோடு புன்னகைத்த பகவான், தேவகிக்கும் வசுதேவருக்கும் அமிர்தம் போன்ற இனிமையான மொழிகளால் ஆறுதல் கூறினார். அவர்கள் தமக்குத் தாய்-தந்தையராக விளங்குவது இது முதல் முறை அல்ல என்பதை பகவான் நினைவூட்டினார்:

1. **முதல் பிறவி (சுதபஸ் மற்றும் பிருஸ்னி):**  
   சுவாயம்புவ மன்வந்தரத்தில், வசுதேவர் சுதபஸ் என்ற பிரஜாபதியாகவும், தேவகி பிருஸ்னி என்ற பதிவிரதையாகவும் வாழ்ந்தனர். பகவானைப் போன்றே ஒரு புதல்வன் தங்களுக்கு வேண்டும் என்று விரும்பி, பன்னிரண்டாயிரம் தேவ ஆண்டுகள் அவர்கள் கடும் தவம் புரிந்தனர். பகவான் அவர்கள் முன்னே தோன்றி வரம் கேட்கச் சொன்னபோது, "உம்மைப் போன்ற ஒரு மகனே எங்களுக்கு வேண்டும்!" என்று மும்முறை வேண்டினர். பகவானுக்கு நிகரானவர் எவருமே இல்லாததால், பகவானே அவர்களுக்கு மகனாக அவதரிக்க சம்மதித்தார். அவ்வாறு பகவான் அவர்களுக்கு **பிருஸ்னிகர்ப்பர்** என்ற திருநாமத்துடன் மகனாக அவதரித்தார்.

2. **இரண்டாம் பிறவி (காஷ்யபர் மற்றும் அதிதி):**  
   அடுத்த பிறவியில், சுதபஸ் காஷ்யப முனிவராகவும், பிருஸ்னி தேவர்களின் தாயான அதிதியாகவும் தோன்றினர். தமது வாக்கைக் காப்பாற்றும் பொருட்டு பகவான் அவர்களின் மகனாக **உபேந்திரன்** (வாமனதேவர்) என்ற திருநாமத்தில் அவதரித்து, தேவேந்திரனுக்கு தேவலோக ஆட்சியை மீட்டுக் கொடுத்தார்.

3. **மூன்றாம் பிறவி (வசுதேவர் மற்றும் தேவகி):**  
   இப்போது, மூன்றாவது பிறவியில் அவர்கள் மதுராவில் வசுதேவராகவும் தேவகியாகவும் தோன்றியுள்ளனர். பகவான் அளித்த வரத்தை மூன்றாவது முறையும் பூர்த்தி செய்வதற்காகவே, முழுமுதற் கடவுளான பகவான் தாமே நேரில் **ஸ்ரீ கிருஷ்ணராக** அவதரித்துள்ளார்.

பகவான் தெளிவுபடுத்தினார்: "உங்களின் முற்பிறவிகளின் நித்திய பந்தத்தையும், எனது முழுமுதற் சொரூபத்தையும் நீங்கள் ஐயமற உணர்ந்து கொள்ளவே, முதலில் இந்த நான்கு கர விஷ்ணு ரூபத்தை உங்களுக்குக் காட்டினேன். இல்லாவிடில், சாதாரண மானிடக் குழந்தையாக நான் தோன்றியிருந்தால், முழுமுதற் கடவுளான பகவானே உங்கள் மகனாக வந்துள்ளார் என்பதை உங்களால் உணர்ந்திருக்க முடியாது."

இவ்வாறாக பெற்றோரின் அச்சத்தைப் போக்கி, அவர்களின் ஆன்மீக நினைவுகளை மீட்டெடுத்த பகவான், தேவகியின் வேண்டுகோளை ஏற்று ஒரு சாதாரண பச்சிளம் குழந்தையின் ரூபத்தை எடுத்தார்.""",
                "questions": [
                    {
                        "question": "முக்குணங்களுக்கும் பகவானுக்கும் உள்ள தொடர்பை வசுதேவர் எவ்வாறு விவரித்தார்?",
                        "options": [
                            {"text": "பகவான் முக்குணங்களுக்கும் அப்பாற்பட்டவர், ஜடகுணங்களால் தீண்டப்படாதவர்", "is_correct": True},
                            {"text": "பகவான் சத்வ குணத்தால் கட்டுப்பட்டவர்", "is_correct": False},
                            {"text": "பகவான் ரஜோ குணத்திற்கு உட்பட்டவர்", "is_correct": False},
                            {"text": "பகவான் ஜட இயற்கையின் விளைவு", "is_correct": False}
                        ]
                    },
                    {
                        "question": "கம்சனைப் பற்றி வசுதேவர் வெளிப்படுத்திய முக்கிய அச்சம் என்ன?",
                        "options": [
                            {"text": "கம்சனின் ஒற்றர்கள் பகவானை அறிந்து ஆயுதங்களுடன் தாக்க வருவார்கள்", "is_correct": True},
                            {"text": "கம்சன் அதிக வரி விதிப்பான்", "is_correct": False},
                            {"text": "கம்சன் அவர்களை வேறு நாட்டிற்கு நாடு கடத்துவான்", "is_correct": False},
                            {"text": "கம்சன் உணவு தர மாட்டான்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "தாய் தேவகி புதிதாக அவதரித்த பகவானிடம் வைத்த அன்பான வேண்டுகோள் என்ன?",
                        "options": [
                            {"text": "நான்கு கர ரூபத்தை மறைத்து சாதாரண இரண்டு கர குழந்தையாக மாற வேண்டும்", "is_correct": True},
                            {"text": "தேவலோகப் படைகளை வரவழைக்க வேண்டும்", "is_correct": False},
                            {"text": "சிறையை தங்க அரண்மனையாக மாற்ற வேண்டும்", "is_correct": False},
                            {"text": "தேவலோக ரதத்தில் தங்களை அழைத்துச் செல்ல வேண்டும்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பகவானின் நான்கு கர ரூபத்தை மறைக்க தேவகி ஏன் விரும்பினார்?",
                        "options": [
                            {"text": "கொடிய கம்சன் பகவானை எளிதில் அடையாளம் கண்டுவிடக் கூடாது என்பதற்காக", "is_correct": True},
                            {"text": "நான்கு கரங்களைத் தூக்குவது கடினம் என்பதால்", "is_correct": False},
                            {"text": "ஆபரணங்கள் தேவகிக்குப் பிடிக்கவில்லை என்பதால்", "is_correct": False},
                            {"text": "ஒளி கண்களைக் கூசியதால்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "வசுதேவரும் தேவகியும் தங்களின் முதல் பிறவியில் யார்?",
                        "options": [
                            {"text": "சுதபஸ் மற்றும் பிருஸ்னி", "is_correct": True},
                            {"text": "காஷ்யபர் மற்றும் திதி", "is_correct": False},
                            {"text": "தசரதர் மற்றும் கௌசல்யா", "is_correct": False},
                            {"text": "மனு மற்றும் சதரூபா", "is_correct": False}
                        ]
                    },
                    {
                        "question": "சுதபஸ் மற்றும் பிருஸ்னிக்கு பகவான் எந்த அவதாரமாகத் தோன்றினார்?",
                        "options": [
                            {"text": "பிருஸ்னிகர்ப்பர்", "is_correct": True},
                            {"text": "மத்ஸ்யர்", "is_correct": False},
                            {"text": "கூர்மர்", "is_correct": False},
                            {"text": "நரசிம்மர்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "வசுதேவரும் தேவகியும் தங்களின் இரண்டாம் பிறவியில் யார்?",
                        "options": [
                            {"text": "காஷ்யபர் மற்றும் அதிதி", "is_correct": True},
                            {"text": "ஜனகர் மற்றும் சுனயனா", "is_correct": False},
                            {"text": "அங்கிரசர் மற்றும் சிரத்தா", "is_correct": False},
                            {"text": "புலஸ்தியர் மற்றும் ஹவிர்பூ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "காஷ்யபர் மற்றும் அதிதியின் மகனாகத் தோன்றிய பகவானின் அவதாரம் எது?",
                        "options": [
                            {"text": "பகவான் வாமனதேவர் (உபேந்திரன்)", "is_correct": True},
                            {"text": "பரசுராமர்", "is_correct": False},
                            {"text": "வராகர்", "is_correct": False},
                            {"text": "புத்தர்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பகவான் வசுதேவர் மற்றும் தேவகிக்கு முதலில் நான்கு கர ரூபத்தை ஏன் காட்டினார்?",
                        "options": [
                            {"text": "தமது திவ்ய சொரூபத்தையும் நித்திய பந்தத்தையும் அவர்கள் உணர வேண்டும் என்பதற்காக", "is_correct": True},
                            {"text": "அவர்களைப் பயமுறுத்துவதற்காக", "is_correct": False},
                            {"text": "தமது உடற்பலத்தைக் காட்டுவதற்காக", "is_correct": False},
                            {"text": "ஆயுதங்களை அவர்கள் அடையாளம் காண்கிறார்களா என்று பார்க்க", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பகவான் அவர்களுக்கு மகனாகப் பிறப்பதாக அளித்த வாக்குறுதியை எத்தனை முறை நிறைவேற்றினார்?",
                        "options": [
                            {"text": "மூன்று முறை", "is_correct": True},
                            {"text": "ஒரு முறை மட்டும்", "is_correct": False},
                            {"text": "ஐந்து முறை", "is_correct": False},
                            {"text": "ஏழு முறை", "is_correct": False}
                        ]
                    }
                ]
            },
            "hi": {
                "mainTopic": "कृष्ण लीलाएं",
                "subTopic": "वसुदेव और देवकी की हृदयस्पर्शी प्रार्थनाएं",
                "content": """### वसुदेव जी की दार्शनिक स्तुति

मथुरा के अंधकारमय कारागार में नवजात बालक की दिव्य स्वर्णिम-नीलमणि आभा से आलोकित होकर, वसुदेव जी ने हाथ जोड़कर अत्यंत विनम्र भाव से स्तुति की। वे दार्शनिक रूप से भली-भांति समझ गए थे कि उनके सम्मुख खड़ा यह बालक कोई साधारण भौतिक बालक नहीं, अपितु प्रकृति के तीनों गुणों से परे स्वयं साक्षात् पूर्ण पुरुषोत्तम भगवान श्री विष्णु हैं।

वसुदेव जी ने प्रार्थना की: "हे परम प्रभु! आप मूल आदिपुरुष हैं, जो इस भौतिक सृष्टि और सत्व, रज, तम—इन तीनों गुणों से सर्वथा परे हैं। आप अपनी दिव्य शक्ति से इस संपूर्ण ब्रह्मांड का सृजन, पालन और संहार करते हैं, फिर भी आप भौतिक गुणों से कभी लिप्त नहीं होते। जैसे कांच से होकर प्रकाश गुजरता है परंतु कांच प्रकाश के स्वरूप को नहीं बदल सकता, उसी प्रकार आप इस भौतिक जगत में अवतरित होकर भी अपने नित्य आध्यात्मिक स्वरूप में ही स्थित हैं।"

फिर वसुदेव जी ने अपनी सांसारिक चिंता प्रकट की: "प्रभु! दुराचारी कंस ने आकाशवाणी के भय से हमारे पहले छह नवजात शिशुओं की नृशंस हत्या कर दी थी। जैसे ही उसके पहरेदारों और गुप्तचरों को आपके प्राकट्य की सूचना मिलेगी, वह अस्त्र-शस्त्र लेकर आपके प्राण लेने दौड़ा आएगा। अतः हे नाथ, हमारी रक्षा कीजिए।"

### माता देवकी की वात्सल्यमयी प्रार्थना

वसुदेव जी की स्तुतियों के उपरांत, माता देवकी ने परम वात्सल्य प्रेम से भरकर भगवान को देखा। जहां वसुदेव जी में आदर और श्रद्धा का भाव प्रधान था, वहीं माता देवकी के हृदय में माता का वात्सल्य उमड़ पड़ा। वे अपने दिव्य बालक की रक्षा के लिए व्याकुल हो उठीं।

देवकी जी ने स्तुति की: "हे प्रभु! प्रलय के समय यह संपूर्ण ब्रह्मांड आपके उदर में सुरक्षित रहता है। वही परमेश्वर आज अपनी अहैतुकी कृपा से मेरे गर्भ से प्रकट हुए हैं! आप साक्षात् काल हैं, जो समस्त भौतिक शक्तियों का विनाश कर देता है। आपके काल-रूप से बड़े-बड़े देवता भी भयभीत रहते हैं। परंतु यह पापी कंस, जो अज्ञान और अहंकार में अंधा है, आपको हानि पहुंचाने की चेष्टा करेगा।"

इसके पश्चात हाथ जोड़कर, अश्रुपूर्ण नेत्रों से माता देवकी ने अत्यंत विनम्र व करुणामयी प्रार्थना की:

> **श्रीमद्भागवतम्, स्कंध 10, अध्याय 3, श्लोक 31**
> 
> *उपसंहर विश्वात्मन् रूपम् एतत् चतुर्भुजम् ।*  
> *यात् ते च्छान्दसम् एतच् च रामलक्ष्मधरायुधम् ॥*  
> 
> **भावार्थ:** हे विश्वात्मन्! शंख, चक्र, गदा और पद्म धारण किए हुए तथा दिव्य आभूषणों से सुशोभित अपने इस चतुर्भुज रूप को आप समेट लीजिए। कृपा करके इस ऐश्वर्यमय रूप को सांसारिक दृष्टि से छिपा लीजिए!

देवकी जी ने अनुनय किया: "मेरे प्यारे पुत्र! यदि कंस ने आपके इस चार भुजाओं वाले रूप को देख लिया, तो वह तुरंत जान जाएगा कि आप ही उसका वध करने वाले साक्षात् भगवान हैं। अतः कृपा करके इस रूप को अंतर्हित कर एक सामान्य दो भुजाओं वाले शिशु का रूप धारण कीजिए, ताकि हम आपको कंस के कोप से बचा सकें!"

### भगवान द्वारा पूर्व जन्मों का रहस्योद्घाटन

अपने माता-पिता के इस विशुद्ध वात्सल्य भाव को देखकर भगवान मंद-मंद मुस्कुराए और अमृतमयी वाणी से उन्हें सांत्वना दी। भगवान ने स्मरण कराया कि वे पहली बार उनके माता-पिता नहीं बने हैं:

1. **प्रथम जन्म (सुतपा और पृश्नि):**  
   स्वायम्भुव मन्वन्तर में वसुदेव जी 'सुतपा' नामक प्रजापति थे और देवकी जी उनकी पतिव्रता पत्नी 'पृश्नि' थीं। भगवान के समान पुत्र पाने की इच्छा से उन्होंने बारह हजार दिव्य वर्षों तक कठोर तपस्या की थी। जब भगवान ने प्रसन्न होकर वर मांगने को कहा, तो उन्होंने तीन बार यही मांगा: "हमें आपके समान ही पुत्र चाहिए!" चूंकि संपूर्ण अस्तित्व में भगवान के समान कोई अन्य नहीं है, अतः भगवान ने स्वयं उनका पुत्र बनना स्वीकार किया और वे **पृश्निगर्भ** के रूप में अवतरित हुए।

2. **द्वितीय जन्म (कश्यप और अदिति):**  
   अगले जन्म में सुतपा महर्षि कश्यप बने और पृश्नि देवमाता अदिति बनीं। अपने वचन का पालन करते हुए भगवान उनके पुत्र **उपेंद्र** (भगवान वामनदेव) के रूप में प्रकट हुए और उन्होंने देवराज इंद्र को स्वर्ग का राज्य पुनः दिलाया।

3. **तृतीय जन्म (वसुदेव और देवकी):**  
   अब, तीसरे जन्म में वे मथुरा में वसुदेव और देवकी के रूप में अवतरित हुए हैं। अपने वचन को तीसरी बार पूर्ण करने के लिए स्वयं पूर्ण पुरुषोत्तम भगवान **श्री कृष्ण** के रूप में अवतरित हुए हैं।

भगवान ने समझाया: "मैंने सबसे पहले अपने इस चतुर्भुज विष्णु रूप का दर्शन इसलिए कराया ताकि आप मेरी वास्तविक दिव्य सत्ता को पहचान सकें और हमारे शाश्वत संबंध को स्मरण कर सकें। यदि मैं केवल एक सामान्य मानव शिशु के रूप में आता, तो आप यह नहीं जान पाते कि साक्षात् भगवान आपके यहां पधारे हैं।"

अपने माता-पिता के भय को दूर कर, भगवान ने देवकी की प्रार्थना स्वीकार करते हुए एक नन्हे बालक का रूप धारण कर लिया।""",
                "questions": [
                    {
                        "question": "वसुदेव जी ने भौतिक प्रकृति के तीनों गुणों और भगवान के संबंध को कैसे बताया?",
                        "options": [
                            {"text": "भगवान तीनों गुणों से सर्वथा परे और अलिप्त हैं", "is_correct": True},
                            {"text": "भगवान सत्व गुण के अधीन हैं", "is_correct": False},
                            {"text": "भगवान रजोगुण से बंधे हैं", "is_correct": False},
                            {"text": "भगवान भौतिक प्रकृति की रचना हैं", "is_correct": False}
                        ]
                    },
                    {
                        "question": "वसुदेव जी ने कंस के विषय में क्या मुख्य भय व्यक्त किया?",
                        "options": [
                            {"text": "कंस के पहरेदार भगवान को देखकर तुरंत अस्त्र-शस्त्र लेकर आक्रमण करेंगे", "is_correct": True},
                            {"text": "कंस अधिक कर मांग लेगा", "is_correct": False},
                            {"text": "कंस उन्हें देश निकाला दे देगा", "is_correct": False},
                            {"text": "कंस भोजन नहीं देगा", "is_correct": False}
                        ]
                    },
                    {
                        "question": "माता देवकी ने नवजात भगवान से क्या प्रेमपूर्ण विनती की?",
                        "options": [
                            {"text": "चतुर्भुज रूप को छिपाकर सामान्य दो भुजाओं वाले शिशु का रूप धारण करें", "is_correct": True},
                            {"text": "देवताओं की सेना को बुला लें", "is_correct": False},
                            {"text": "कारागार को सोने का महल बना दें", "is_correct": False},
                            {"text": "उन्हें दिव्य रथ में उड़ा ले जाएं", "is_correct": False}
                        ]
                    },
                    {
                        "question": "माता देवकी भगवान के चतुर्भुज रूप को क्यों छिपाना चाहती थीं?",
                        "options": [
                            {"text": "ताकि पापी कंस भगवान को पहचान न सके", "is_correct": True},
                            {"text": "चार भुजाओं को संभालना कठिन था", "is_correct": False},
                            {"text": "उन्हें आभूषण पसंद नहीं थे", "is_correct": False},
                            {"text": "प्रकाश से उनकी आंखें चौंधिया रही थीं", "is_correct": False}
                        ]
                    },
                    {
                        "question": "वसुदेव और देवकी अपने पहले जन्म में कौन थे?",
                        "options": [
                            {"text": "सुतपा और पृश्नि", "is_correct": True},
                            {"text": "कश्यप और दिति", "is_correct": False},
                            {"text": "दशरथ और कौशल्या", "is_correct": False},
                            {"text": "मनु और शतरूपा", "is_correct": False}
                        ]
                    },
                    {
                        "question": "सुतपा और पृश्नि के पुत्र रूप में भगवान किस अवतार में प्रकट हुए थे?",
                        "options": [
                            {"text": "पृश्निगर्भ", "is_correct": True},
                            {"text": "मत्स्य", "is_correct": False},
                            {"text": "कूर्म", "is_correct": False},
                            {"text": "नृसिंह", "is_correct": False}
                        ]
                    },
                    {
                        "question": "वसुदेव और देवकी अपने दूसरे जन्म में कौन थे?",
                        "options": [
                            {"text": "कश्यप और अदिति", "is_correct": True},
                            {"text": "जनक और सुनयना", "is_correct": False},
                            {"text": "अंगिरा और श्रद्धा", "is_correct": False},
                            {"text": "पुलस्त्य और हविर्भु", "is_correct": False}
                        ]
                    },
                    {
                        "question": "कश्यप और अदिति के पुत्र रूप में भगवान का कौन सा अवतार हुआ था?",
                        "options": [
                            {"text": "भगवान वामनदेव (उपेंद्र)", "is_correct": True},
                            {"text": "परशुराम", "is_correct": False},
                            {"text": "वराह", "is_correct": False},
                            {"text": "बुद्ध", "is_correct": False}
                        ]
                    },
                    {
                        "question": "भगवान ने पहले अपना चतुर्भुज रूप क्यों दिखाया?",
                        "options": [
                            {"text": "ताकि वे भगवान की दिव्यता और शाश्वत संबंध को पहचान सकें", "is_correct": True},
                            {"text": "उन्हें डराने के लिए", "is_correct": False},
                            {"text": "अपनी शारीरिक शक्ति दिखाने के लिए", "is_correct": False},
                            {"text": "यह परखने के लिए कि वे शस्त्र पहचानते हैं या नहीं", "is_correct": False}
                        ]
                    },
                    {
                        "question": "भगवान ने उनका पुत्र बनने का वचन कितनी बार पूर्ण किया?",
                        "options": [
                            {"text": "तीन बार", "is_correct": True},
                            {"text": "केवल एक बार", "is_correct": False},
                            {"text": "पांच बार", "is_correct": False},
                            {"text": "सात बार", "is_correct": False}
                        ]
                    }
                ]
            },
            "ml": {
                "mainTopic": "കൃഷ്ണ ലീലകൾ",
                "subTopic": "വസുദേവരുടെയും ദേവകിയുടെയും ഹൃദയംഗമമായ പ്രാർത്ഥനകൾ",
                "content": """### വസുദേവരുടെ തത്ത്വചിന്താപരമായ സ്തുതി

മഥുരയിലെ കാരാഗൃഹത്തിൽ, ആവിർഭവിച്ച ദിവ്യബാലന്റെ സുവർണ്ണ-നീലിമ പ്രഭയിൽ മുഴുകി വസുദേവർ അതീവ ഭക്തിയോടെ കൈകൂപ്പി നിന്നു. തങ്ങളുടെ മുന്നിൽ നിൽക്കുന്നത് ഒരു സാധാരണ മനുഷ്യശിശുവല്ല, മറിച്ച് ത്രിഗുണങ്ങൾക്ക് അതീതനായ സാക്ഷാൽ പൂർണ്ണപുരുഷോത്തമനായ ഭഗവാൻ വിഷ്ണുവാണെന്ന് വസുദേവർ തത്ത്വചിന്താപരമായി തിരിച്ചറിഞ്ഞു.

വസുദേവർ പ്രാർത്ഥിച്ചു: "ഹേ ഭഗവാനേ! അങ്ങ് ഭൗതിക പ്രപഞ്ചത്തിനും സത്വം, രജസ്സ്, തമസ്സ് എന്നീ മൂന്നു ഗുണങ്ങൾക്കും അതീതനായ ആദിപുരുഷനാണ്. അവിടുത്തെ ദിവ്യമായ ചിച്ഛക്തിയാൽ അങ്ങ് ഈ പ്രപഞ്ചത്തെ സൃഷ്ടിക്കുകയും പാലിക്കുകയും സംഹരിക്കുകയും ചെയ്യുന്നു; എങ്കിലും മായാഗുണങ്ങളാൽ ഒരിക്കലും ബാധിക്കപ്പെടുന്നില്ല. സ്ഫടികത്തിലൂടെ കടന്നുപോകുന്ന പ്രകാശം സ്ഫടികത്താൽ മാറ്റപ്പെടാത്തതുപോലെ, അങ്ങ് ഭൗതിക ലോകത്തിൽ പ്രവേശിച്ചാലും അവിടുത്തെ നിത്യമായ ദിവ്യരൂപത്തിൽ തന്നെ വിരാജിക്കുന്നു."

തുടർന്ന് വസുദേവർ തന്റെ പ്രായോഗികമായ ആശങ്ക പങ്കുവെച്ചു: "ഭഗവാനേ! അങ്ങയുടെ കൈകളാൽ വധിക്കപ്പെടുമെന്ന അശരീരി കേട്ട് ഭയന്ന ക്രൂരനായ കംസൻ ഞങ്ങളുടെ ആദ്യത്തെ ആറ് കുഞ്ഞുങ്ങളെയും നിഷ്കരുണം വധിച്ചു. അങ്ങയുടെ ജനനവാർത്ത അവന്റെ കാവൽക്കാരിലൂടെ അറിയുന്ന മാത്രയിൽ അവൻ ആയുധങ്ങളുമായി അങ്ങയെ വധിക്കാൻ പാഞ്ഞെത്തും. അതിനാൽ ഹേ നാഥാ, ഞങ്ങളെ കാത്തരുളേണമേ!"

### മാതാ ദേവകിയുടെ വാത്സല്യനിർഭരമായ അപേക്ഷ

വസുദേവരുടെ പ്രാർത്ഥനകൾക്ക് ശേഷം, മാതൃവാത്സല്യത്തോടെ ദേവകി ഭഗവാനെ നോക്കി. വസുദേവരിൽ ആദരവും ഭക്തിയുമാണ് മുന്നിട്ടുനിന്നതെങ്കിൽ, ദേവകിയുടെ മാതൃഹൃദയം ഉണ്ണിയുടെ സുരക്ഷയെക്കുറിച്ചുള്ള ആകുലതകളാൽ നിറഞ്ഞു.

ദേവകി പ്രാർത്ഥിച്ചു: "ഹേ പ്രഭോ! പ്രളയകാലത്ത് സകല പ്രപഞ്ചങ്ങളെയും അങ്ങ് ഉദരത്തിൽ സംരക്ഷിക്കുന്നു. അങ്ങനെയുള്ള അങ്ങ് അവിടുത്തെ നിർഹേതുകമായ കാരുണ്യത്താൽ എന്റെ ഗർഭത്തിൽ നിന്നും ജനിച്ചിരിക്കുന്നു! സമസ്ത ഭൗതിക ശക്തികളെയും നശിപ്പിക്കുന്ന കാലം അങ്ങുതന്നെയാണ്. അങ്ങയുടെ കാലശക്തിയെക്കണ്ട് ദേവന്മാർ പോലും ഭയക്കുന്നു. എന്നാൽ അഹങ്കാരത്താൽ അന്ധനായ കംസൻ അങ്ങയെ ഉപദ്രവിക്കാൻ മുതിരുന്നു."

തുടർന്ന് കണ്ണീരോടെ കൈകൂപ്പി മാതാ ദേവകി അതീവ വിനീതമായ ഒരു യാചന നടത്തി:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അദ്ധ്യായം 3, ശ്ലോകം 31**
> 
> *ഉപസംഹര വിശ്വാത്മൻ രൂപമ് ഏതത് ചതുർഭുജമ് |*  
> *യാത് തേ ച്ഛാന്ദസം ഏതച് ച രാമലക്ഷ്മധരായുധമ് ||*  
> 
> **അർത്ഥം:** ഹേ വിശ്വാത്മാവായ ഭഗവാനേ! ശംഖ്, ചക്രം, ഗദ, താമര എന്നിവ ധരിച്ചതും ദിവ്യാഭരണങ്ങളാൽ അലംകൃതമായതുമായ അങ്ങയുടെ ഈ ചതുർഭുജ രൂപത്തെ പിൻവലിച്ചാലും. ഭൗതിക ദൃഷ്ടികളിൽ നിന്നും ഈ ഐശ്വര്യപൂർണ്ണമായ രൂപത്തെ മറച്ചുവെച്ചാലും!

ദേവകി യാചിച്ചു: "എന്റെ ഓമനക്കുഞ്ഞേ! ഈ ദിവ്യമായ ചതുർഭുജ രൂപം കംസൻ കണ്ടാൽ, തന്നെ വധിക്കാൻ വന്ന പരമപുരുഷൻ അങ്ങാണെന്ന് അവൻ ഉടൻ തിരിച്ചറിയും. അതിനാൽ ഈ രൂപം മറച്ച്, സാധാരണ രണ്ടു കൈകളുള്ള ശിശുവായി മാറിയാലും, ഞങ്ങൾ അങ്ങയെ കംസന്റെ കോപത്തിൽ നിന്നും രക്ഷിക്കട്ടെ!"

### മുൻജന്മങ്ങളുടെ രഹസ്യം ഭഗവാൻ വെളിപ്പെടുത്തുന്നു

മാതാപിതാക്കളുടെ നിഷ്കളങ്കമായ വാത്സല്യം കണ്ട് ഭഗവാൻ പുഞ്ചിരിച്ചുകൊണ്ട് അമൃതവാണികളാൽ അവരെ ആശ്വസിപ്പിച്ചു. തങ്ങളുടെ മാതാപിതാക്കളാകുന്നത് ഇതാദ്യമല്ലെന്ന് ഭഗവാൻ അവർക്ക് ഓർമ്മിപ്പിച്ചു കൊടുത്തു:

1. **ഒന്നാം ജന്മം (സുതപസ്സും പൃശ്നിയും):**  
   സ്വയംഭുവ മന്വന്തരത്തിൽ വസുദേവർ 'സുതപസ്സ്' എന്ന പ്രജാപതിയും ദേവകി 'പൃശ്നി' എന്ന പതിവ്രതയുമായിരുന്നു. ഭഗവാനെപ്പോലൊരു പുത്രനെ ലഭിക്കാനായി അവർ പന്തീരായിരം ദിവ്യവർഷങ്ങൾ കഠിനതപം അനുഷ്ഠിച്ചു. ഭഗവാൻ പ്രത്യക്ഷപ്പെട്ട് വരം ചോദിക്കാൻ പറഞ്ഞപ്പോൾ, "അങ്ങയെപ്പോലൊരു പുത്രനെ വേണം!" എന്ന് അവർ മൂന്നുതവണ യാചിച്ചു. പ്രപഞ്ചത്തിൽ ഭഗവാന് തുല്യനായി മറ്റാരുമില്ലാത്തതിനാൽ, ഭഗവാൻ തന്നെ അവരുടെ പുത്രനായി **പൃശ്നിഗർഭൻ** എന്ന നാമത്തിൽ അവതരിച്ചു.

2. **രണ്ടാം ജന്മം (കശ്യപനും അദിതിയും):**  
   അടുത്ത ജന്മത്തിൽ സുതപസ്സ് കശ്യപമഹർഷിയായും പൃശ്നി ദേവമാതാവായ അദിതിയായും ജനിച്ചു. തന്റെ വാക്ക് പാലിച്ച് ഭഗവാൻ അവരുടെ പുത്രനായി **ഉപേന്ദ്രൻ** (വാമനദേവൻ) എന്ന നാമത്തിൽ അവതരിച്ച് ഇന്ദ്രന് സ്വർഗ്ഗരാജ്യം വീണ്ടെടുത്തു കൊടുത്തു.

3. **മൂന്നാം ജന്മം (വസുദേവരും ദേവകിയും):**  
   ഇപ്പോൾ, മൂന്നാമത്തെ ജന്മത്തിൽ അവർ മഥുരയിൽ വസുദേവരും ദേവകിയുമായി ജനിച്ചിരിക്കുന്നു. തന്റെ വാഗ്ദാനം മൂന്നാമതും നിറവേറ്റാനായി ഭഗവാൻ സാക്ഷാൽ **ശ്രീകൃഷ്ണനായി** അവതരിച്ചിരിക്കുന്നു.

ഭഗവാൻ വ്യക്തമാക്കി: "ഞാൻ ആദ്യം ഈ ചതുർഭുജ വിഷ്ണുരൂപം കാട്ടിയത്, അവിടുത്തെ എന്റെ പരമസത്യത്തെയും നമ്മുടെ ശാശ്വതമായ ബന്ധത്തെയും തിരിച്ചറിയുന്നതിനു വേണ്ടിയാണ്. അല്ലാത്തപക്ഷം, ഒരു സാധാരണ ശിശുവായി മാത്രം ഞാൻ വന്നിരുന്നെങ്കിൽ, സാക്ഷാൽ പരമപുരുഷനാണ് നിങ്ങളുടെ പുത്രനായി വന്നതെന്ന് നിങ്ങൾക്ക് മനസ്സിലാകുമായിരുന്നില്ല."

മാതാപിതാക്കളുടെ ഭയം അകറ്റി, ദേവകിയുടെ പ്രാർത്ഥന സ്വീകരിച്ച് ഭഗവാൻ ഒരു സാധാരണ നവജാതശിശുവിന്റെ രൂപം സ്വീകരിച്ചു.""",
                "questions": [
                    {
                        "question": "ഭൗതിക പ്രകൃതിയുടെ ത്രിഗുണങ്ങളുമായി ഭഗവാനുള്ള ബന്ധത്തെക്കുറിച്ച് വസുദേവർ എന്താണ് പറഞ്ഞത്?",
                        "options": [
                            {"text": "ഭഗവാൻ ത്രിഗുണങ്ങൾക്ക് അതീതനും മായാഗുണങ്ങളാൽ സ്പർശിക്കപ്പെടാത്തവനുമാണ്", "is_correct": True},
                            {"text": "ഭഗവാൻ സത്വഗുണത്തിന് വിധേയനാണ്", "is_correct": False},
                            {"text": "ഭഗവാൻ രജോഗുണത്താൽ ബന്ധിതനാണ്", "is_correct": False},
                            {"text": "ഭഗവാൻ ഭൗതിക പ്രകൃതിയുടെ സൃഷ്ടിയാണ്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "കംസനെക്കുറിച്ച് വസുദേവർ പ്രകടിപ്പിച്ച പ്രധാന ഭയം എന്തായിരുന്നു?",
                        "options": [
                            {"text": "കംസന്റെ കാവൽക്കാർ ഭഗവാനെ കണ്ട് ഉടൻ ആയുധങ്ങളുമായി ആക്രമിക്കാൻ വരും", "is_correct": True},
                            {"text": "കംസൻ കൂടുതൽ നികുതി ചോദിക്കും", "is_correct": False},
                            {"text": "കംസൻ അവരെ നാടുകടത്തും", "is_correct": False},
                            {"text": "കംസൻ ഭക്ഷണം തരില്ല", "is_correct": False}
                        ]
                    },
                    {
                        "question": "മാതാ ദേവകി ഭഗവാനോട് സ്നേഹപൂർവ്വം എന്താണ് അപേക്ഷിച്ചത്?",
                        "options": [
                            {"text": "ചതുർഭുജ രൂപം പിൻവലിച്ച് സാധാരണ രണ്ടു കൈകളുള്ള ശിശുവായി മാറാൻ", "is_correct": True},
                            {"text": "ദേവസേനയെ വിളിച്ചുവരുത്താൻ", "is_correct": False},
                            {"text": "കാരാഗൃഹം സ്വർണ്ണക്കൊട്ടാരമാക്കാൻ", "is_correct": False},
                            {"text": "ദിവ്യരഥത്തിൽ തങ്ങളെ രക്ഷിക്കാൻ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ദേവകി ഭഗവാന്റെ ചതുർഭുജ രൂപം മറയ്ക്കാൻ ആഗ്രഹിച്ചത് എന്തുകൊണ്ട്?",
                        "options": [
                            {"text": "ക്രൂരനായ കംസൻ ഭഗവാനെ എളുപ്പത്തിൽ തിരിച്ചറിയാതിരിക്കാൻ", "is_correct": True},
                            {"text": "നാലു കൈകൾ താങ്ങാൻ പ്രയാസമായതുകൊണ്ട്", "is_correct": False},
                            {"text": "ആഭരണങ്ങൾ ഇഷ്ടപ്പെടാത്തതുകൊണ്ട്", "is_correct": False},
                            {"text": "പ്രകാശം കണ്ണഞ്ചിപ്പിച്ചതുകൊണ്ട്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "വസുദേവരും ദേവകിയും അവരുടെ ആദ്യ ജന്മത്തിൽ ആരായിരുന്നു?",
                        "options": [
                            {"text": "സുതപസ്സും പൃശ്നിയും", "is_correct": True},
                            {"text": "കശ്യപനും ദിതിയും", "is_correct": False},
                            {"text": "ദശരഥനും കൗസല്യയും", "is_correct": False},
                            {"text": "മനുവും ശതരൂപയും", "is_correct": False}
                        ]
                    },
                    {
                        "question": "സുതപസ്സിനും പൃശ്നിക്കും ഭഗവാൻ ഏത് അവതാരമായാണ് ജനിച്ചത്?",
                        "options": [
                            {"text": "പൃശ്നിഗർഭൻ", "is_correct": True},
                            {"text": "മത്സ്യം", "is_correct": False},
                            {"text": "കൂർമ്മം", "is_correct": False},
                            {"text": "നരസിംഹം", "is_correct": False}
                        ]
                    },
                    {
                        "question": "വസുദേവരും ദേവകിയും അവരുടെ രണ്ടാമത്തെ ജന്മത്തിൽ ആരായിരുന്നു?",
                        "options": [
                            {"text": "കശ്യപനും അദിതിയും", "is_correct": True},
                            {"text": "ജനകനും സുനയനയും", "is_correct": False},
                            {"text": "അംഗിരസ്സും ശ്രദ്ധയും", "is_correct": False},
                            {"text": "പുലസ്ത്യനും ഹവിർഭൂവും", "is_correct": False}
                        ]
                    },
                    {
                        "question": "കശ്യപന്റെയും അദിതിയുടെയും പുത്രനായി അവതരിച്ച ഭഗവാന്റെ അവതാരം ഏതാണ്?",
                        "options": [
                            {"text": "ഭഗവാൻ വാമനദേവൻ (ഉപേന്ദ്രൻ)", "is_correct": True},
                            {"text": "പരശുരാമൻ", "is_correct": False},
                            {"text": "വരാഹം", "is_correct": False},
                            {"text": "ബുദ്ധൻ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഭഗവാൻ ആദ്യം തന്റെ ചതുർഭുജ രൂപം കാട്ടിയത് എന്തുകൊണ്ട്?",
                        "options": [
                            {"text": "അവിടുത്തെ ദിവ്യത്വവും നിത്യബന്ധവും അവർ തിരിച്ചറിയാൻ", "is_correct": True},
                            {"text": "അവരെ ഭയപ്പെടുത്താൻ", "is_correct": False},
                            {"text": "ശാരീരികശക്തി തെളിയിക്കാൻ", "is_correct": False},
                            {"text": "ആയുധങ്ങൾ തിരിച്ചറിയുന്നുണ്ടോ എന്ന് പരീക്ഷിക്കാൻ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "അവരുടെ പുത്രനായി ജനിക്കാമെന്ന വാഗ്ദാനം ഭഗവാൻ എത്ര തവണ നിറവേറ്റി?",
                        "options": [
                            {"text": "മൂന്നു തവണ", "is_correct": True},
                            {"text": "ഒരു തവണ മാത്രം", "is_correct": False},
                            {"text": "അഞ്ചു തവണ", "is_correct": False},
                            {"text": "ഏഴു തവണ", "is_correct": False}
                        ]
                    }
                ]
            },
            "bn": {
                "mainTopic": "কৃষ্ণ লীলা",
                "subTopic": "বসুদেব ও দেবকীর ভক্তিপূর্ণ দিব্য প্রার্থনা",
                "content": """### বসুদেবের দার্শনিক স্তুতি

মথুরার অন্ধকার কারাগারে নবজাত শিশুর দিব্য স্বর্ণ-নীলিম আভায় উদ্ভাসিত হয়ে বসুদেব পরম শ্রদ্ধায় করজোড়ে দাঁড়িয়ে রইলেন। তিনি দার্শনিক দৃষ্টিতে নিশ্চিতরূপে উপলব্ধি করলেন যে, তাঁর সম্মুখে বিরাজমান এই শিশু কোনো প্রাকৃত মানবসন্তান নন, তিনি ত্রিগুণের অতীত স্বয়ং পরম পুরুষোত্তম ভগবান শ্রীবিষ্ণু।

বসুদেব স্তুতি করলেন: "হে পরমেশ্বর! আপনি এই প্রাকৃত জগৎ এবং সত্ত্ব, রজ ও তম—এই ত্রিগুণের অতীত আদিপুরুষ। আপনার চিন্ময়ী শক্তির দ্বারা আপনি সমগ্র বিশ্বব্রহ্মাণ্ড সৃষ্টি, পালন ও সংহার করেন; তথাপি আপনি কখনো জড়গুণের দ্বারা স্পর্শিত হন না। যেমন স্ফটিকের মধ্য দিয়ে আলো গমন করলেও স্ফটিক আলোকে পরিবর্তন করতে পারে না, তদ্রূপ আপনি জড়জগতে প্রবেশ করলেও সর্বদা আপনার নিত্য চিন্ময় রূপেই বিদ্যমান থাকেন।"

অতঃপর বসুদেব তাঁর জাগতিক আশঙ্কার কথা ব্যক্ত করলেন: "প্রভু! আপনার হস্তে নিধনের দৈববাণী শুনে দুরাচারী কংস আমাদের পূর্ববর্তী ছয়টি নবজাত শিশুকে নির্মমভাবে হত্যা করেছে। আপনার আবির্ভাবের সংবাদ পাওয়া মাত্রই তার প্রহরীরা কংসকে জানাবে এবং সে অস্ত্রশস্ত্র নিয়ে আপনাকে বধ করতে ছুটে আসবে। অতএব হে নাথ, আপনি আমাদের রক্ষা করুন।"

### মাতা দেবকীর বাৎসল্যপূর্ণ কাতর প্রার্থনা

বসুদেবের স্তুতির পর মাতা দেবকী পরম বাৎসল্যপ্রেমে আপ্লুত হয়ে ভগবানের দিকে তাকালেন। যেখানে বসুদেবের মধ্যে সম্ভ্রম ও শ্রদ্ধার ভাব ছিল, সেখানে মাতা দেবকীর মাতৃস্নেহ ব্যাকুল হয়ে উঠল। তিনি তাঁর দিব্য সন্তানের নিরাপত্তার কথা ভেবে অত্যন্ত শঙ্কিত হলেন।

দেবকী প্রার্থনা করলেন: "হে প্রভু! মহাপ্রলয়ের সময় নিখিল ব্রহ্মাণ্ড আপনার উদরে নিরাপদে অবস্থান করে। সেই পরমেশ্বর আজ অসীম কৃপায় আমার গর্ভে আবির্ভূত হয়েছেন! আপনিই কালের স্বরূপ, যা সকল জড়শক্তিকে বিনাশ করে। আপনার কালশক্তিকে দেবতারাও ভয় পান। অথচ এই অহংকারী কংস আপনাকে বিনাশ করতে উদ্যত হয়েছে।"

অতঃপর বাষ্পাকুল লোচনে করজোড়ে মাতা দেবকী এক পরম করুণ নিবেদন করলেন:

> **শ্রীমদ্ভাগবত, স্কন্ধ ১০, অধ্যায় ৩, শ্লোক ৩১**
> 
> *উপসংহর বিশ্বাত্মন্ রূপম্ এতৎ চতুর্ভুজম্ ।*  
> *যাৎ তে চ্ছান্দসম্ এতচ্ চ রামলক্ষমধরায়ুধম্ ॥*  
> 
> **অনুবাদ:** হে বিশ্বাত্মন! শঙ্খ, চক্র, গদা ও পদ্মধারী এবং অপ্রাকৃত ভূষণে সুশোভিত আপনার এই ঐশ্বর্যময় চতুর্ভুজ রূপটি সংবরণ করুন। দয়া করে এই রূপটি মর্ত্যের দৃষ্টি থেকে গোপন করুন!

দেবকী মিনতি করলেন: "হে বাছা! কংস যদি আপনার এই চতুর্ভুজ দিব্য রূপ প্রত্যক্ষ করে, তবে সে তৎক্ষণাৎ জেনে ফেলবে যে আপনিই তাকে বধ করতে অবতীর্ণ পরমেশ্বর। অতএব দয়া করে এই রূপ সংবরণ করে একটি সাধারণ দ্বিভুজ শিশুর রূপ ধারণ করুন, যাতে আমরা আপনাকে কংসের রোষ থেকে রক্ষা করতে পারি!"

### ভগবান কর্তৃক পূর্বজন্মের রহস্য প্রকাশ

পিতামাতার এই অকৃত্রিম বাৎসল্যভাব দেখে ভগবান মৃদু হাস্য করে অমৃতময় বাণীতে তাঁদের সান্ত্বনা দিলেন। ভগবান স্মরণ করিয়ে দিলেন যে, তাঁরা এই প্রথমবার তাঁর পিতামাতা হননি:

1. **প্রথম জন্ম (সুতপা ও পৃশ্নি):**  
   স্বায়ম্ভুব মন্বন্তরে বসুদেব ছিলেন প্রজাপতি 'সুতপা' এবং দেবকী ছিলেন তাঁর সাধ্বী পত্নী 'পৃশ্নি'। ভগবানের ন্যায় পুত্রলাভের আশায় তাঁরা দ্বাদশ সহস্র দিব্য বৎসর কঠোর তপস্যা করেছিলেন। ভগবান সন্তুষ্ট হয়ে বর প্রদান করতে চাইলে তাঁরা তিনবার প্রার্থনা করেছিলেন: "আমরা আপনার ন্যায় পুত্র চাই!" যেহেতু সমগ্র অস্তিত্বে ভগবানের সমকক্ষ কেউ নেই, তাই ভগবান নিজেই তাঁদের পুত্ররূপে **পৃশ্নিগর্ভ** নামে অবতীর্ণ হয়েছিলেন।

2. **দ্বিতীয় জন্ম (কশ্যপ ও অদিতি):**  
   পরবর্তী জন্মে সুতপা হলেন মহর্ষি কশ্যপ এবং পৃশ্নি হলেন দেবমাতা অদিতি। স্বীয় প্রতিশ্রুতি রক্ষার্থে ভগবান তাঁদের পুত্র **উপেন্দ্র** (বামনদেব) রূপে অবতীর্ণ হয়ে ইন্দ্রকে স্বর্গরাজ্য ফিরিয়ে দেন।

3. **তৃতীয় জন্ম (বসুদেব ও দেবকী):**  
   এখন, তৃতীয় জন্মে তাঁরা মথুরায় বসুদেব ও দেবকী রূপে অবতীর্ণ হয়েছেন। ভগবান তাঁর প্রদত্ত বর তৃতীয়বারের মতো পূর্ণ করতে স্বয়ং **শ্রীকৃষ্ণরূপে** অবতীর্ণ হয়েছেন।

ভগবান বুঝিয়ে বললেন: "আমি প্রথমে আমার এই চতুর্ভুজ রূপ প্রদর্শন করেছি যাতে আপনারা আমার পরমেশ্বরত্ব উপলব্ধি করতে পারেন এবং আমাদের শাশ্বত সম্পর্কটি স্মরণ করতে পারেন। অন্যথায়, কেবল সাধারণ শিশুরূপে এলে আপনারা বুঝতে পারতেন না যে স্বয়ং ভগবান আপনাদের গৃহে এসেছেন।"

পিতামাতার শঙ্কা দূর করে ভগবান দেবকীর প্রার্থনা মঞ্জুর করলেন এবং একটি ক্ষুদ্র শিশুর রূপ ধারণ করলেন।""",
                "questions": [
                    {
                        "question": "বসুদেব প্রকৃতির ত্রিগুণের সাথে ভগবানের সম্পর্ককে কীভাবে বর্ণনা করেছেন?",
                        "options": [
                            {"text": "ভগবান ত্রিগুণের অতীত এবং জড়গুণের দ্বারা অস্পৃষ্ট", "is_correct": True},
                            {"text": "ভগবান সত্ত্বগুণের অধীন", "is_correct": False},
                            {"text": "ভগবান রজোগুণের দ্বারা নিয়ন্ত্রিত", "is_correct": False},
                            {"text": "ভগবান জড় প্রকৃতির সৃষ্টি", "is_correct": False}
                        ]
                    },
                    {
                        "question": "কংসের বিষয়ে বসুদেব কি প্রধান ভয় ব্যক্ত করেছিলেন?",
                        "options": [
                            {"text": "কংসের প্রহরীরা ভগবানকে দেখে অস্ত্রশস্ত্র নিয়ে আক্রমণ করতে ছুটে আসবে", "is_correct": True},
                            {"text": "কংস অতিরিক্ত কর চাইবে", "is_correct": False},
                            {"text": "কংস তাঁদের নির্বাসনে পাঠাবে", "is_correct": False},
                            {"text": "কংস খাদ্য দেবে না", "is_correct": False}
                        ]
                    },
                    {
                        "question": "মাতা দেবকী ভগবানের কাছে কি ব্যাকুল প্রার্থনা করেছিলেন?",
                        "options": [
                            {"text": "চতুর্ভুজ রূপ সংবরণ করে সাধারণ দ্বিভুজ শিশুর রূপ ধারণ করতে", "is_correct": True},
                            {"text": "দেবতাদের বাহিনীকে আহ্বান করতে", "is_correct": False},
                            {"text": "কারাগারকে স্বর্ণের প্রাসাদে পরিণত করতে", "is_correct": False},
                            {"text": "তাঁদের উড়িয়ে নিয়ে যেতে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "দেবকী কেন ভগবানের চতুর্ভুজ রূপ গোপন করতে চেয়েছিলেন?",
                        "options": [
                            {"text": "যাতে নিষ্ঠুর কংস ভগবানকে সহজে চিনতে না পারে", "is_correct": True},
                            {"text": "চারটি হাত বহন করা কঠিন ছিল বলে", "is_correct": False},
                            {"text": "তিনি অলঙ্কার পছন্দ করতেন না বলে", "is_correct": False},
                            {"text": "আলো তাঁর চোখ ধাঁধিয়ে দিয়েছিল বলে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "বসুদেব ও দেবকী তাঁদের প্রথম জন্মে কে ছিলেন?",
                        "options": [
                            {"text": "সুতপা ও পৃশ্নি", "is_correct": True},
                            {"text": "কশ্যপ ও দিতি", "is_correct": False},
                            {"text": "দশরথ ও কৌশল্যা", "is_correct": False},
                            {"text": "মনু ও শতরূপা", "is_correct": False}
                        ]
                    },
                    {
                        "question": "সুতপা ও পৃশ্নির পুত্ররূপে ভগবান কোন অবতারে এসেছিলেন?",
                        "options": [
                            {"text": "পৃশ্নিগর্ভ", "is_correct": True},
                            {"text": "মৎস্য", "is_correct": False},
                            {"text": "কূর্ম", "is_correct": False},
                            {"text": "নৃসিংহ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "বসুদেব ও দেবকী তাঁদের দ্বিতীয় জন্মে কে ছিলেন?",
                        "options": [
                            {"text": "কশ্যপ ও অদিতি", "is_correct": True},
                            {"text": "জনক ও সুনয়না", "is_correct": False},
                            {"text": "অঙ্গিরা ও শ্রদ্ধা", "is_correct": False},
                            {"text": "পুলস্ত্য ও হবির্ভূ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "কশ্যপ ও অদিতির পুত্ররূপে ভগবানের কোন অবতার আবির্ভূত হয়েছিলেন?",
                        "options": [
                            {"text": "ভগবান বামনদেব (উপেন্দ্র)", "is_correct": True},
                            {"text": "পরশুরাম", "is_correct": False},
                            {"text": "বরাহ", "is_correct": False},
                            {"text": "বুদ্ধ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ভগবান প্রথমে কেন তাঁর চতুর্ভুজ রূপ প্রদর্শন করেছিলেন?",
                        "options": [
                            {"text": "তাঁরা যেন ভগবানের দিব্য স্বরূপ ও শাশ্বত সম্পর্ক উপলব্ধি করতে পারেন", "is_correct": True},
                            {"text": "তাঁদের ভয় দেখানোর জন্য", "is_correct": False},
                            {"text": "শারীরিক শক্তি প্রদর্শনের জন্য", "is_correct": False},
                            {"text": "অস্ত্রশস্ত্র চিনতে পারে কি না তা পরীক্ষা করতে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ভগবান তাঁদের পুত্র হবার প্রতিশ্রুতি কতবার পূরণ করেছিলেন?",
                        "options": [
                            {"text": "তিনবার", "is_correct": True},
                            {"text": "কেবল একবার", "is_correct": False},
                            {"text": "পাঁচবার", "is_correct": False},
                            {"text": "সাতবার", "is_correct": False}
                        ]
                    }
                ]
            },
            "te": {
                "mainTopic": "కృష్ణ లీలలు",
                "subTopic": "వసుదేవ దేవకీల హృదయపూర్వక దివ్య ప్రార్థనలు",
                "content": """### వసుదేవుని తాత్త్విక స్తుతి

మథుర చెరసాలలో నవజాత శిశువు యొక్క దివ్య కాంతిలో మునిగిపోయిన వసుదేవుడు వినయంతో చేతులు జోడించి నిలబడ్డాడు. తన ఎదుట ఉన్నది సాధారణ శిశువు కాదని, సత్వ, రజో, తమో గుణాలకు అతీతుడైన సాక్షాత్తు పూర్ణ పురుషోత్తముడైన భగవాన్ శ్రీవిష్ణువేనని ఆయన గ్రహించాడు.

వసుదేవుడు ప్రార్థించాడు: "ఓ పరమేశ్వరా! నీవు సృష్టికి పూర్వమే ఉన్న ఆదిపురుషుడవు. భౌతిక గుణాలైన త్రిగుణాలకు నీవు అతీతుడవు. నీ దివ్య చిచ్ఛక్తితో ఈ సమస్త జగత్తును సృష్టించి, రక్షించి, లయింపజేస్తావు; అయినప్పటికీ నీవు భౌతిక గుణాలతో ఎన్నడూ బంధింపబడవు. గాజు గుండా ప్రకాశించే కాంతిని గాజు మార్చలేనట్లుగానే, నీవు భౌతిక ప్రపంచంలోకి దిగివచ్చినా నీ నిత్య దివ్య రూపంలోనే ఉంటావు."

అనంతరం వసుదేవుడు తన ఆందోళనను వ్యక్తపరిచాడు: "ప్రభూ! నీ చేతిలో మరణం తథ్యమనే ఆకాశవాణిని విని దుర్మార్గుడైన కంసుడు మా మునుపటి ఆరుగురు బిడ్డలను దారుణంగా చంపేశాడు. నీ ఆవిర్భావం గురించి గూఢచారుల ద్వారా తెలియగానే అతడు ఆయుధాలతో నిన్ను వధించడానికి దూసుకువస్తాడు. కాబట్టి ప్రభూ, మమ్మల్ని రక్షించు!"

### తల్లి దేవకి వాత్సల్య ప్రార్థన

వసుదేవుని స్తుతుల తర్వాత, దేవకీదేవి మాతృవాత్సల్యంతో భగవంతుని చూసింది. వసుదేవునిలో భక్తి ప్రపత్తులు ఉంటే, దేవకి హృదయం బిడ్డ రక్షణ గురించిన భయంతో నిండిపోయింది.

ఆమె ప్రార్థించింది: "ప్రభూ! ప్రళయకాలంలో సకల బ్రహ్మాండాలు నీ ఉదరంలో భద్రంగా ఉంటాయి. అటువంటి పరమేశ్వరుడవు నా గర్భంలో జన్మించావు! సమస్త శక్తులను నాశనం చేసే కాలస్వరూపుడవు నీవే. నీ కాలశక్తికి దేవతలు సైతం భయపడతారు. కానీ అహంకారంతో కళ్ళు మూసుకుపోయిన కంసుడు నిన్ను సంహరించాలని చూస్తున్నాడు."

తరువాత కన్నీటితో చేతులు జోడించి దేవకి ఒక ఆర్తితో కూడిన విన్నపం చేసింది:

> **శ్రీమద్భాగవతం, స్కంధం 10, అధ్యాయం 3, శ్లోకం 31**
> 
> *ఉపసంహర విశ్వాత్మన్ రూపమ్ ఏతత్ చతుర్భుజమ్ |*  
> *యాత్ తే చ్ఛాందసం ఏతచ్ చ రామలక్ష్మధరాయుధమ్ ||*  
> 
> **తాత్పర్యం:** ఓ విశ్వాత్మా! శంఖ, చక్ర, గదా, పద్మాలను ధరించిన ఈ దివ్య చతుర్భుజ రూపాన్ని, వైకుంఠ ఆభరణాలను దయచేసి ఉపసంహరించుకో. ఈ దివ్య రూపాన్ని లౌకిక దృష్టికి కనిపించకుండా దాచిపెట్టు!

దేవకి వేడుకుంది: "నాయనా! ఈ నాలుగు చేతుల దివ్య రూపాన్ని కంసుడు చూస్తే, తనను సంహరించడానికి వచ్చిన భగవంతుడవు నీవేనని సులభంగా గుర్తిస్తాడు. కాబట్టి ఈ రూపాన్ని ఉపసంహరించి సాధారణ రెండు చేతుల శిశువుగా మారు, తద్వారా నిన్ను కంసుని కోపం నుండి కాపాడుకోగలం!"

### గత మూడు జన్మల రహస్యాన్ని వివరించిన భగవానుడు

తల్లిదండ్రుల నిష్కల్మషమైన వాత్సల్యాన్ని చూసి భగవంతుడు మందహాసంతో అమృతపు పలుకులతో వారికి సాంత్వన పలికాడు. వారు తనకు తల్లిదండ్రులు కావడం ఇది మొదటిసారి కాదని గుర్తుచేశాడు:

1. **మొదటి జన్మ (సుతపస్సు మరియు పృష్ని):**  
   స్వాయంభువ మన్వంతరంలో వసుదేవుడు 'సుతపస్సు' అనే ప్రజాపతిగా, దేవకి 'పృష్ని' అనే పతివ్రతగా ఉన్నారు. భగవంతుని వంటి కుమారుడు కావాలని వారు పన్నెండు వేల దివ్య సంవత్సరాలు కఠోర తపస్సు చేశారు. భగవంతుడు ప్రత్యక్షమై వరం కోరుకోమన్నప్పుడు, "నీ వంటి కుమారుడే మాకు కావాలి!" అని మూడుసార్లు కోరారు. సృష్టిలో భగవంతునికి సాటి ఎవరూ లేకపోవడంతో, భగవంతుడే స్వయంగా వారి కుమారుడిగా **పృష్నిగర్భుడు**గా జన్మించాడు.

2. **రెండవ జన్మ (కశ్యపుడు మరియు అదితి):**  
   తరువాతి జన్మలో సుతపస్సు కశ్యప మహర్షిగా, పృష్ని దేవమాత అదితిగా జన్మించారు. తన వాగ్దానాన్ని నిలబెట్టుకోవడానికి భగవంతుడు వారి కుమారుడిగా **ఉపేంద్రుడు** (వామనుడు)గా అవతరించి ఇంద్రునికి స్వర్గ రాజ్యాన్ని తిరిగి ఇప్పించాడు.

3. **మూడవ జన్మ (వసుదేవుడు మరియు దేవకి):**  
   ఇప్పుడు, మూడవ జన్మలో వారు మథురలో వసుదేవ దేవకీలుగా జన్మించారు. తన వాగ్దానాన్ని మూడవసారి నెరవేర్చడానికి భగవానుడు స్వయంగా **శ్రీకృష్ణునిగా** అవతరించాడు.

భగవానుడు వివరించాడు: "నా దివ్య తత్త్వాన్ని మీరు నిస్సందేహంగా గుర్తించి, మన శాశ్వత బంధాన్ని గుర్తుంచుకోవడానికే నేను మొదట ఈ చతుర్భుజ విష్ణు రూపాన్ని మీకు చూపించాను. అలా కాకుండా కేవలం సాధారణ శిశువుగా వచ్చి ఉంటే, సాక్షాత్తు పరమేశ్వరుడే మీ ఇంట జన్మించాడని మీరు గ్రహించి ఉండేవారు కాదు."

తల్లిదండ్రుల భయాన్ని పోగొట్టి, దేవకి ప్రార్థనను మన్నిస్తూ భగవానుడు ఒక చిన్న పసిబిడ్డ రూపాన్ని ధరించాడు.""",
                "questions": [
                    {
                        "question": "భౌతిక ప్రకృతి త్రిగుణాలతో భగవంతునికి గల సంబంధాన్ని వసుదేవుడు ఎలా వివరించాడు?",
                        "options": [
                            {"text": "భగవంతుడు త్రిగుణాలకు అతీతుడు మరియు భౌతిక గుణాలచే అంటబడనివాడు", "is_correct": True},
                            {"text": "భగవంతుడు సత్వగుణానికి లోబడి ఉంటాడు", "is_correct": False},
                            {"text": "భగవంతుడు రజోగుణంతో బంధించబడ్డాడు", "is_correct": False},
                            {"text": "భగవంతుడు భౌతిక ప్రకృతి సృష్టి", "is_correct": False}
                        ]
                    },
                    {
                        "question": "కంసుని గురించి వసుదేవుడు వ్యక్తం చేసిన ముఖ్యమైన భయం ఏమిటి?",
                        "options": [
                            {"text": "కంసుని సైనికులు భగవంతుని చూసి ఆయుధాలతో దాడి చేయడానికి వస్తారు", "is_correct": True},
                            {"text": "కంసుడు ఎక్కువ పన్ను అడుగుతాడు", "is_correct": False},
                            {"text": "కంసుడు దేశ బహిష్కరణ చేస్తాడు", "is_correct": False},
                            {"text": "కంసుడు ఆహారం ఇవ్వడు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "తల్లి దేవకి భగవంతుని ఏమని ప్రార్థించింది?",
                        "options": [
                            {"text": "చతుర్భుజ రూపాన్ని దాచి సాధారణ రెండు చేతుల శిశువుగా మారమని", "is_correct": True},
                            {"text": "దేవతల సైన్యాన్ని పిలవమని", "is_correct": False},
                            {"text": "చెరసాలను బంగారు భవంతిగా మార్చమని", "is_correct": False},
                            {"text": "రథంలో ఎక్కించుకుని తీసుకువెళ్ళమని", "is_correct": False}
                        ]
                    },
                    {
                        "question": "దేవకి భగవంతుని చతుర్భుజ రూపాన్ని ఎందుకు దాచాలనుకుంది?",
                        "options": [
                            {"text": "క్రూరుడైన కంసుడు భగవంతుని సులభంగా గుర్తించకుండా ఉండటానికి", "is_correct": True},
                            {"text": "నాలుగు చేతులను మోయడం కష్టమని", "is_correct": False},
                            {"text": "ఆభరణాలు నచ్చలేదని", "is_correct": False},
                            {"text": "కాంతి కళ్ళను జిగేల్మనిపించిందని", "is_correct": False}
                        ]
                    },
                    {
                        "question": "వసుదేవ దేవకీలు తమ మొదటి జన్మలో ఎవరు?",
                        "options": [
                            {"text": "సుతపస్సు మరియు పృష్ని", "is_correct": True},
                            {"text": "కశ్యపుడు మరియు దితి", "is_correct": False},
                            {"text": "దశరథుడు మరియు కౌసల్య", "is_correct": False},
                            {"text": "మనువు మరియు శతరూప", "is_correct": False}
                        ]
                    },
                    {
                        "question": "సుతపస్సు మరియు పృష్నిలకు భగవంతుడు ఏ అవతారంలో జన్మించాడు?",
                        "options": [
                            {"text": "పృష్నిగర్భుడు", "is_correct": True},
                            {"text": "మత్స్య", "is_correct": False},
                            {"text": "కూర్మ", "is_correct": False},
                            {"text": "నరసింహ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "వసుదేవ దేవకీలు తమ రెండవ జన్మలో ఎవరు?",
                        "options": [
                            {"text": "కశ్యపుడు మరియు అదితి", "is_correct": True},
                            {"text": "జనకుడు మరియు సునయన", "is_correct": False},
                            {"text": "అంగిరసుడు మరియు శ్రద్ధ", "is_correct": False},
                            {"text": "పులస్త్యుడు మరియు హవిర్భువు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "కశ్యపుడు మరియు అదితుల కుమారునిగా అవతరించిన భగవంతుని అవతారం ఏది?",
                        "options": [
                            {"text": "భగవాన్ వామనుడు (ఉపేంద్రుడు)", "is_correct": True},
                            {"text": "పరశురాముడు", "is_correct": False},
                            {"text": "వరాహ", "is_correct": False},
                            {"text": "బుద్ధుడు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "భగవంతుడు మొదట తన చతుర్భుజ రూపాన్ని ఎందుకు చూపించాడు?",
                        "options": [
                            {"text": "తన దివ్యతత్త్వాన్ని మరియు శాశ్వత బంధాన్ని వారు గుర్తించడానికి", "is_correct": True},
                            {"text": "వారిని భయపెట్టడానికి", "is_correct": False},
                            {"text": "శారీరక బలాన్ని ప్రదర్శించడానికి", "is_correct": False},
                            {"text": "ఆయుధాలను గుర్తిస్తారో లేదో పరీక్షించడానికి", "is_correct": False}
                        ]
                    },
                    {
                        "question": "వారి కుమారునిగా జన్మిస్తానన్న వాగ్దానాన్ని భగవంతుడు ఎన్నిసార్లు నెరవేర్చాడు?",
                        "options": [
                            {"text": "మూడుసార్లు", "is_correct": True},
                            {"text": "ఒక్కసారి మాత్రమే", "is_correct": False},
                            {"text": "ఐదుసార్లు", "is_correct": False},
                            {"text": "ఏడుసార్లు", "is_correct": False}
                        ]
                    }
                ]
            },
            "kn": {
                "mainTopic": "ಕೃಷ್ಣ ಲೀಲೆಗಳು",
                "subTopic": "ವಸುದೇವ ಮತ್ತು ದೇವಕಿಯರ ಭಕ್ತಿಪೂರ್ಣ ದಿವ್ಯ ಪ್ರಾರ್ಥನೆಗಳು",
                "content": """### ವಸುದೇವರ ತತ್ತ್ವಪೂರ್ಣ ಸ್ತುತಿ

ಮಥುರೆಯ ಕತ್ತಲೆಯ ಸೆರೆಮನೆಯಲ್ಲಿ ನವಜಾತ ಬಾಲಕನ ದಿವ್ಯ ತೇಜಸ್ಸನ್ನು ಕಂಡ ವಸುದೇವರು ಕೈಮುಗಿದು ಭಕ್ತಿಯಿಂದ ನಿಂತರು. ತಮ್ಮೆದುರು ಪ್ರಕಟವಾಗಿರುವುದು ಸಾಮಾನ್ಯ ಮಗುವಲ್ಲ, ಪ್ರಕೃತಿಯ ತ್ರಿಗುಣಗಳಿಗೆ ಅತೀತನಾದ ಸಾಕ್ಷಾತ್ ಪರಮ ಪುರುಷೋತ್ತಮ ಭಗವಾನ್ ಶ್ರೀವಿಷ್ಣುವೇ ಎಂದು ಅವರು ಅರಿತರು.

ವಸುದೇವರು ಪ್ರಾರ್ಥಿಸಿದರು: "ಹೇ ಪರಮ ಪ್ರಭು! ನೀನು ಸೃಷ್ಟಿಗೆ ಮುಂಚೆಯೇ ಇರುವ ಆದಿಪುರುಷ. ಸತ್ವ, ರಜ, ತಮ ಎಂಬ ತ್ರಿಗುಣಗಳಿಗೆ ನೀನು ಅತೀತ. ನಿನ್ನ ದಿವ್ಯ ಶಕ್ತಿಯಿಂದ ಸಮಸ್ತ ಬ್ರಹ್ಮಾಂಡವನ್ನು ಸೃಷ್ಟಿಸಿ, ರಕ್ಷಿಸಿ, ಲಯಗೊಳಿಸುತ್ತೀ; ಆದರೂ ನೀನು ಎಂದಿಗೂ ಭೌತಿಕ ಗುಣಗಳಿಂದ ಸ್ಪರ್ಶಿಸಲ್ಪಡುವುದಿಲ್ಲ. ಗಾಜಿನ ಮೂಲಕ ಹಾದುಹೋಗುವ ಬೆಳಕನ್ನು ಗಾಜು ಬದಲಾಯಿಸಲಾಗದಂತೆ, ನೀನು ಭೌತಿಕ ಜಗತ್ತಿಗೆ ಬಂದರೂ ನಿನ್ನ ನಿತ್ಯ ದಿವ್ಯ ರೂಪದಲ್ಲಿಯೇ ಇರುತ್ತೀ."

ನಂತರ ವಸುದೇವರು ತಮ್ಮ ಕಳವಳವನ್ನು ವ್ಯಕ್ತಪಡಿಸಿದರು: "ಪ್ರಭು! ನಿನ್ನಿಂದ ತನಗೆ ಮೃತ್ಯು ಎಂಬ ಅಶರೀರವಾಣಿಯನ್ನು ಕೇಳಿ ಕ್ರೂರಿ ಕಂಸನು ನಮ್ಮ ಹಿಂದಿನ ಆರು ಮಕ್ಕಳನ್ನು ನಿರ್ದಯವಾಗಿ ಕೊಂದನು. ನಿನ್ನ ಜನನದ ಸುದ್ದಿ ತಿಳಿಯುತ್ತಿದ್ದಂತೆ ಆತನು ಆಯುಧಗಳನ್ನು ಹಿಡಿದು ನಿನ್ನನ್ನು ಕೊಲ್ಲಲು ಧಾವಿಸಿ ಬರುತ್ತಾನೆ. ಆದ್ದರಿಂದ ಪ್ರಭು, ನಮ್ಮನ್ನು ರಕ್ಷಿಸು!"

### ತಾಯಿ ದೇವಕಿಯ ವಾತ್ಸಲ್ಯಪೂರ್ಣ ಪ್ರಾರ್ಥನೆ

ವಸುದೇವರ ಸ್ತುತಿಯ ನಂತರ, ತಾಯಿ ದೇವಕಿಯು ಮಮತೆಯಿಂದ ಭಗವಂತನನ್ನು ನೋಡಿದಳು. ವಸುದೇವರಲ್ಲಿ ಭಕ್ತಿ ಗೌರವಗಳಿದ್ದರೆ, ದೇವಕಿಯ ತಾಯ್ಮನಸ್ಸು ಮಗುವಿನ ರಕ್ಷಣೆಯ ಚಿಂತೆಯಿಂದ ತತ್ತರಿಸಿತು.

ದೇವಕಿಯು ಪ್ರಾರ್ಥಿಸಿದಳು: "ಪ್ರಭು! ಪ್ರಳಯಕಾಲದಲ್ಲಿ ಸಮಸ್ತ ವಿಶ್ವಗಳು ನಿನ್ನ ಹೊಟ್ಟೆಯಲ್ಲಿ ಸುರಕ್ಷಿತವಾಗಿರುತ್ತವೆ. ಅಂತಹ ಪರಮೇಶ್ವರನು ನನ್ನ ಗರ್ಭದಲ್ಲಿ ಜನಿಸಿದ್ದಾನೆ! ಸಕಲ ಶಕ್ತಿಗಳನ್ನು ನಾಶಮಾಡುವ ಕಾಲವೇ ನೀನು. ನಿನ್ನ ಕಾಲಶಕ್ತಿಗೆ ದೇವತೆಗಳೂ ಹೆದರುತ್ತಾರೆ. ಆದರೆ ಅಹಂಕಾರದಿಂದ ಕುರುಡಾದ ಕಂಸನು ನಿನಗೆ ಹಾನಿಮಾಡಲು ಸಂಚು ರೂಪಿಸುತ್ತಿದ್ದಾನೆ."

ನಂತರ ಕಣ್ಣೀರು ತುಂಬಿದ ಕಣ್ಣುಗಳಿಂದ ಕೈಮುಗಿದು ದೇವಕಿಯು ಕರುಣಾಪೂರ್ಣ ಪ್ರಾರ್ಥನೆ ಮಾಡಿದಳು:

> **ಶ್ರೀಮದ್ಭಾಗವತ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 3, ಶ್ಲೋಕ 31**
> 
> *ಉಪಸಂಹರ ವಿಶ್ವಾತ್ಮನ್ ರೂಪಮ್ ಏತತ್ ಚತುರ್ಭುಜಮ್ |*  
> *ಯಾತ್ ತೇ ಚ್ಛಾಂದಸಮ್ ಏತಚ್ ಚ ರಾಮಲಕ್ಷ್ಮಧರಾಯುಧಮ್ ||*  
> 
> **ಭಾವಾರ್ಥ:** ಹೇ ವಿಶ್ವಾತ್ಮನೇ! ಶಂಖ, ಚಕ್ರ, ಗದಾ, ಪದ್ಮಗಳನ್ನು ಧರಿಸಿದ ಮತ್ತು ದಿವ್ಯಾಭರಣಗಳಿಂದ ಕಂಗೊಳಿಸುವ ನಿನ್ನ ಈ ಚತುರ್ಭುಜ ರೂಪವನ್ನು ಹಿಂತೆಗೆದುಕೋ. ಈ ದಿವ್ಯ ರೂಪವನ್ನು ಲೌಕಿಕ ದೃಷ್ಟಿಯಿಂದ ಮರೆಮಾಚು!

ದೇವಕಿಯು ಬೇಡಿಕೊಂಡಳು: "ನನ್ನ ಕಂದಾ! ಈ ನಾಲ್ಕು ಕೈಗಳ ರೂಪವನ್ನು ಕಂಸನು ನೋಡಿದರೆ, ತನ್ನನ್ನು ಕೊಲ್ಲಲು ಬಂದ ಪರಮಾತ್ಮನೇ ನೀನು ಎಂದು ತಕ್ಷಣ ತಿಳಿದುಕೊಳ್ಳುತ್ತಾನೆ. ಆದ್ದರಿಂದ ದಯವಿಟ್ಟು ಈ ರೂಪವನ್ನು ಮರೆಮಾಚಿ ಸಾಮಾನ್ಯ ಎರಡು ಕೈಗಳ ಮಗುವಿನ ರೂಪವನ್ನು ಧರಿಸು, ಇದರಿಂದ ನಾವು ನಿನ್ನನ್ನು ಕಂಸನ ಕೋಪದಿಂದ ರಕ್ಷಿಸಬಹುದು!"

### ಹಿಂದಿನ ಮೂರು ಜನ್ಮಗಳ ರಹಸ್ಯವನ್ನು ತಿಳಿಸಿದ ಭಗವಂತ

ತಂದೆ-ತಾಯಿಯರ ನಿಸ್ವಾರ್ಥ ವಾತ್ಸಲ್ಯವನ್ನು ಕಂಡು ಭಗವಂತನು ಮಂದಹಾಸ ಬೀರುತ್ತಾ ಮಧುರ ವಾಣಿಯಿಂದ ಸಮಾಧಾನಪಡಿಸಿದನು. ಅವರು ತನಗೆ ತಂದೆ-ತಾಯಿಯಾಗಿರುವುದು ಇದೇ ಮೊದಲಲ್ಲ ಎಂದು ನೆನಪಿಸಿದನು:

1. **ಮೊದಲ ಜನ್ಮ (ಸುತಪ ಮತ್ತು ಪೃಶ್ನಿ):**  
   ಸ್ವಾಯಂಭುವ ಮನ್ವಂತರದಲ್ಲಿ ವಸುದೇವರು 'ಸುತಪ' ಎಂಬ ಪ್ರಜಾಪತಿಯಾಗಿದ್ದರು ಮತ್ತು ದೇವಕಿಯು 'ಪೃಶ್ನಿ' ಎಂಬ ಪತಿವ್ರತೆಯಾಗಿದ್ದಳು. ಭಗವಂತನಂತಹ ಮಗನನ್ನು ಪಡೆಯಲು ಅವರು ಹನ್ನೆರಡು ಸಾವಿರ ದಿವ್ಯ ವರ್ಷಗಳ ಕಾಲ ಕಠಿಣ ತಪಸ್ಸು ಮಾಡಿದರು. ಭಗವಂತನು ಪ್ರತ್ಯಕ್ಷನಾಗಿ ವರ ಕೇಳಲು ಹೇಳಿದಾಗ, "ನಿನ್ನಂತಹ ಮಗನೇ ನಮಗೆ ಬೇಕು!" ಎಂದು ಮೂರು ಬಾರಿ ಕೇಳಿದರು. ಸೃಷ್ಟಿಯಲ್ಲಿ ಭಗವಂತನಿಗೆ ಸಮಾನರಾದವರು ಯಾರೂ ಇಲ್ಲದ್ದರಿಂದ, ಭಗವಂತನೇ ಅವರ ಮಗನಾಗಿ **ಪೃಶ್ನಿಗರ್ಭ** ಎಂಬ ಹೆಸರಿನಿಂದ ಜನಿಸಿದನು.

2. **ಎರಡನೇ ಜನ್ಮ (ಕಶ್ಯಪ ಮತ್ತು ಅದಿತಿ):**  
   ಮುಂದಿನ ಜನ್ಮದಲ್ಲಿ ಸುತಪರು ಕಶ್ಯಪ ಮಹರ್ಷಿಯಾಗಿಯೂ, ಪೃಶ್ನಿಯು ದೇವಮಾತೆ ಅದಿತಿಯಾಗಿಯೂ ಜನಿಸಿದರು. ತನ್ನ ಮಾತನ್ನು ಉಳಿಸಿಕೊಳ್ಳಲು ಭಗವಂತನು ಅವರ ಮಗನಾಗಿ **ಉಪೇಂದ್ರ** (ವಾಮನದೇವ) ಎಂಬ ಹೆಸರಿನಿಂದ ಅವತರಿಸಿ ಇಂದ್ರನಿಗೆ ಸ್ವರ್ಗವನ್ನು ಮರಳಿ ಕೊಡಿಸಿದನು.

3. **ಮೂರನೇ ಜನ್ಮ (ವಸುದೇವ ಮತ್ತು ದೇವಕಿ):**  
   ಈಗ, ಮೂರನೇ ಜನ್ಮದಲ್ಲಿ ಅವರು ಮಥುರೆಯಲ್ಲಿ ವಸುದೇವ ಮತ್ತು ದೇವಕಿಯಾಗಿ ಜನಿಸಿದ್ದಾರೆ. ತನ್ನ ವಾಗ್ದಾನವನ್ನು ಮೂರನೇ ಬಾರಿಗೆ ಪೂರೈಸಲು ಭಗವಂತನು ಸ್ವಯಂ **ಶ್ರೀಕೃಷ್ಣನಾಗಿ** ಅವತರಿಸಿದ್ದಾನೆ.

ಭಗವಂತನು ವಿವರಿಸಿದನು: "ನನ್ನ ದಿವ್ಯ ಸ್ವರೂಪವನ್ನು ಮತ್ತು ನಮ್ಮ ಶಾಶ್ವತ ಸಂಬಂಧವನ್ನು ನೀವು ಅರಿಯಲಿ ಎಂದೇ ನಾನು ಮೊದಲು ಈ ಚತುರ್ಭುಜ ವಿಷ್ಣು ರೂಪವನ್ನು ತೋರಿಸಿದೆ. ಹಾಗಲ್ಲದೆ ಕೇವಲ ಸಾಮಾನ್ಯ ಮಗುವಾಗಿ ಬಂದಿದ್ದರೆ, ಸಾಕ್ಷಾತ್ ಪರಮಾತ್ಮನೇ ನಿಮ್ಮಲ್ಲಿ ಬಂದಿದ್ದಾನೆ ಎಂದು ನಿಮಗೆ ತಿಳಿಯುತ್ತಿರಲಿಲ್ಲ."

ತಂದೆ-ತಾಯಿಯರ ಭಯವನ್ನು ಹೋಗಲಾಡಿಸಿ, ದೇವಕಿಯ ಪ್ರಾರ್ಥನೆಯಂತೆ ಭಗವಂತನು ಒಂದು ಚಿಕ್ಕ ಕಂದಮ್ಮನ ರೂಪವನ್ನು ಧರಿಸಿದನು.""",
                "questions": [
                    {
                        "question": "ಪ್ರಕೃತಿಯ ತ್ರಿಗುಣಗಳೊಂದಿಗೆ ಭಗವಂತನಿಗಿರುವ ಸಂಬಂಧವನ್ನು ವಸುದೇವರು ಹೇಗೆ ವಿವರಿಸಿದರು?",
                        "options": [
                            {"text": "ಭಗವಂತನು ತ್ರಿಗುಣಗಳಿಗೆ ಅತೀತ ಮತ್ತು ಭೌತಿಕ ಗುಣಗಳಿಂದ ಸ್ಪರ್ಶಿಸಲ್ಪಡದವನು", "is_correct": True},
                            {"text": "ಭಗವಂತನು ಸತ್ವಗುಣಕ್ಕೆ ಅಧೀನ", "is_correct": False},
                            {"text": "ಭಗವಂತನು ರಜೋಗುಣದಿಂದ ಬದ್ಧ", "is_correct": False},
                            {"text": "ಭಗವಂತನು ಪ್ರಕೃತಿಯ ಸೃಷ್ಟಿ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಕಂಸನ ಬಗ್ಗೆ ವಸುದೇವರು ವ್ಯಕ್ತಪಡಿಸಿದ ಮುಖ್ಯ ಭಯವೇನು?",
                        "options": [
                            {"text": "ಕಂಸನ ಕಾವಲುಗಾರರು ಭಗವಂತನನ್ನು ಕಂಡು ಆಯುಧಗಳಿಂದ ದಾಳಿ ಮಾಡಲು ಬರುತ್ತಾರೆ", "is_correct": True},
                            {"text": "ಕಂಸನು ಹೆಚ್ಚು ತೆರಿಗೆ ಕೇಳುತ್ತಾನೆ", "is_correct": False},
                            {"text": "ಕಂಸನು ದೇಶಭ್ರಷ್ಟರನ್ನಾಗಿ ಮಾಡುತ್ತಾನೆ", "is_correct": False},
                            {"text": "ಕಂಸನು ಆಹಾರ ನೀಡುವುದಿಲ್ಲ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ತಾಯಿ ದೇವಕಿಯು ಭಗವಂತನಲ್ಲಿ ಪ್ರೀತಿಯಿಂದ ಏನು ಬೇಡಿಕೊಂಡಳು?",
                        "options": [
                            {"text": "ಚತುರ್ಭುಜ ರೂಪವನ್ನು ಮರೆಮಾಚಿ ಸಾಮಾನ್ಯ ಎರಡು ಕೈಗಳ ಮಗುವಾಗಲು", "is_correct": True},
                            {"text": "ದೇವತೆಗಳ ಸೈನ್ಯವನ್ನು ಕರೆಯಲು", "is_correct": False},
                            {"text": "ಸೆರೆಮನೆಯನ್ನು ಚಿನ್ನದ ಅರಮನೆಯನ್ನಾಗಿ ಮಾಡಲು", "is_correct": False},
                            {"text": "ರಥದಲ್ಲಿ ಹಾರಿಸಿಕೊಂಡು ಹೋಗಲು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ದೇವಕಿಯು ಭಗವಂತನ ಚತುರ್ಭುಜ ರೂಪವನ್ನು ಏಕೆ ಮರೆಮಾಡಲು ಬಯಸಿದಳು?",
                        "options": [
                            {"text": "ಕ್ರೂರ ಕಂಸನು ಭಗವಂತನನ್ನು ಸುಲಭವಾಗಿ ಗುರುತಿಸಬಾರದು ಎಂದು", "is_correct": True},
                            {"text": "ನಾಲ್ಕು ಕೈಗಳನ್ನು ಎತ್ತಲು ಕಷ್ಟವೆಂದು", "is_correct": False},
                            {"text": "ಆಭರಣಗಳು ಇಷ್ಟವಿಲ್ಲವೆಂದು", "is_correct": False},
                            {"text": "ಬೆಳಕು ಕಣ್ಣು ಕೋರೈಸಿದ್ದರಿಂದ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ವಸುದೇವ ಮತ್ತು ದೇವಕಿಯರು ತಮ್ಮ ಮೊದಲ ಜನ್ಮದಲ್ಲಿ ಯಾರಾಗಿದ್ದರು?",
                        "options": [
                            {"text": "ಸುತಪ ಮತ್ತು ಪೃಶ್ನಿ", "is_correct": True},
                            {"text": "ಕಶ್ಯಪ ಮತ್ತು ದಿತಿ", "is_correct": False},
                            {"text": "ದಶರಥ ಮತ್ತು ಕೌಸಲ್ಯ", "is_correct": False},
                            {"text": "ಮನು ಮತ್ತು ಶತರೂಪ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಸುತಪ ಮತ್ತು ಪೃಶ್ನಿಯರ ಮಗನಾಗಿ ಭಗವಂತನು ಯಾವ ಅವತಾರದಲ್ಲಿ ಬಂದನು?",
                        "options": [
                            {"text": "ಪೃಶ್ನಿಗರ್ಭ", "is_correct": True},
                            {"text": "ಮತ್ಸ್ಯ", "is_correct": False},
                            {"text": "ಕೂರ್ಮ", "is_correct": False},
                            {"text": "ನರಸಿಂಹ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ವಸುದೇವ ಮತ್ತು ದೇವಕಿಯರು ತಮ್ಮ ಎರಡನೇ ಜನ್ಮದಲ್ಲಿ ಯಾರಾಗಿದ್ದರು?",
                        "options": [
                            {"text": "ಕಶ್ಯಪ ಮತ್ತು ಅದಿತಿ", "is_correct": True},
                            {"text": "ಜನಕ ಮತ್ತು ಸುನಯನ", "is_correct": False},
                            {"text": "ಅಂಗಿರಸ ಮತ್ತು ಶ್ರದ್ಧಾ", "is_correct": False},
                            {"text": "ಪುಲಸ್ತ್ಯ ಮತ್ತು ಹವಿರ್ಭೂ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಕಶ್ಯಪ ಮತ್ತು ಅದಿತಿಯರ ಮಗನಾಗಿ ಬಂದ ಭಗವಂತನ ಅವತಾರ ಯಾವುದು?",
                        "options": [
                            {"text": "ಭಗವಾನ್ ವಾಮನದೇವ (ಉಪೇಂದ್ರ)", "is_correct": True},
                            {"text": "ಪರಶುರಾಮ", "is_correct": False},
                            {"text": "ವರಾಹ", "is_correct": False},
                            {"text": "ಬುದ್ಧ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಭಗವಂತನು ಮೊದಲು ತನ್ನ ಚತುರ್ಭುಜ ರೂಪವನ್ನು ಏಕೆ ತೋರಿಸಿದನು?",
                        "options": [
                            {"text": "ತನ್ನ ದಿವ್ಯಸ್ವರೂಪ ಮತ್ತು ಶಾಶ್ವತ ಬಂಧವನ್ನು ಅವರು ತಿಳಿಯಲಿ ಎಂದು", "is_correct": True},
                            {"text": "ಅವರನ್ನು ಹೆದರಿಸಲು", "is_correct": False},
                            {"text": "ದೈಹಿಕ ಶಕ್ತಿ ಪ್ರದರ್ಶಿಸಲು", "is_correct": False},
                            {"text": "ಆಯುಧಗಳನ್ನು ಗುರುತಿಸುತ್ತಾರೆಯೇ ಎಂದು ನೋಡಲು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಅವರ ಮಗನಾಗುವ ಭರವಸೆಯನ್ನು ಭಗವಂತನು ಎಷ್ಟು ಬಾರಿ ಪೂರೈಸಿದನು?",
                        "options": [
                            {"text": "ಮೂರು ಬಾರಿ", "is_correct": True},
                            {"text": "ಕೇವಲ ಒಂದು ಬಾರಿ", "is_correct": False},
                            {"text": "ಐದು ಬಾರಿ", "is_correct": False},
                            {"text": "ಏಳು ಬಾರಿ", "is_correct": False}
                        ]
                    }
                ]
            }
        }

        for lang, data in stories_data.items():
            translation, _ = StoryTranslation.objects.get_or_create(
                story=story,
                language_code=lang,
                defaults={
                    "mainTopic": data["mainTopic"],
                    "subTopic": data["subTopic"],
                    "article": data["content"]
                }
            )
            translation.mainTopic = data["mainTopic"]
            translation.subTopic = data["subTopic"]
            translation.article = data["content"]
            translation.save()

            # Clear existing questions for fresh population
            translation.questions.all().delete()

            for order, q_data in enumerate(data["questions"], start=1):
                question = StoryQuestion.objects.create(
                    translation=translation,
                    question_text=q_data["question"],
                    order=order
                )
                for opt_idx, opt in enumerate(q_data["options"], start=1):
                    StoryQuestionOption.objects.create(
                        question=question,
                        order=opt_idx,
                        option_text=opt["text"],
                        is_correct=opt["is_correct"]
                    )
            self.stdout.write(f"Saved {lang} translation with {len(data['questions'])} questions.")

        self.stdout.write(self.style.SUCCESS(f"Successfully populated Story 8 (ID: {story.id}) across all 7 languages!"))
