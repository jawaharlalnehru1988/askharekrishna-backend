import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askharekrishna_backend.settings')
django.setup()

from django.core.management.base import BaseCommand
from stories.models import StoryMainTopic, Story, StoryTranslation, StoryQuestion, StoryQuestionOption

class Command(BaseCommand):
    help = "Populate Story 11: Kamsa's Temporary Remorse and Release of Vasudeva and Devaki across 7 languages"

    def handle(self, *args, **options):
        topic = StoryMainTopic.objects.get(name="Krishna Pastimes")

        story_slug = "krishna-pastimes-kamsas-temporary-remorse-and-release-of-vasudeva-and-devaki"
        image_path = "stories/images/kamsa_remorse_release.jpg"

        story, created = Story.objects.get_or_create(
            slug=story_slug,
            defaults={
                "topic": topic,
                "order": 10,
                "imagePath": image_path,
            }
        )
        if not created:
            story.topic = topic
            story.order = 10
            story.imagePath = image_path
            story.save()

        stories_data = {
            "en": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "Kamsa's Temporary Remorse and the Release of Vasudeva and Devaki",
                "content": """### Kamsa's Astonishment and Sudden Grief

When the eight-armed Goddess Durgā vanished from the sky after delivering her thunderous warning, King Kamsa remained frozen on the stone floor of the dungeon courtyard. His arrogant demonic pride was thoroughly shattered.

He realized with terrifying clarity that the celestial prophecy (*ākāśavāṇī*) had not been a lie: his destined slayer was indeed alive, fully protected by divine providence beyond his reach. Furthermore, all his ruthless atrocities—the cold-blooded slaughter of Devaki's six innocent newborn infants—had been completely futile! He had incurred monstrous sinful reactions without accomplishing anything.

Overcome by acute psychological shock, fear of hellish torment, and sudden remorse, Kamsa rushed into the dark prison cell where Vasudeva and Devaki stood.

### Kamsa Falls at Their Feet in Tears

Throwing himself flat upon the stone floor, Kamsa caught hold of the feet of his sister Devaki and his brother-in-law Vasudeva. Tears of genuine shame poured from his eyes like torrential rain, wetting their feet.

With his voice choking in lamentation, Kamsa cried:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 4, Verse 19**
> 
> *aho mayācaritaṁ pāpaṁ rākṣasair iva karkaśaiḥ*  
> *bālikā bhaginī-putrā ghātitā bahavo mayā*  
> 
> **Translation:** "Alas, what an abominable sinner I am! Like a cruel, bloodthirsty man-eating demon (*rākṣasa*), I have mercilessly slaughtered so many tender infants, the innocent children of my own loving sister!"

Kamsa continued with intense self-reproach: "I do not know what terrible, blazing hell awaits me! Because I have killed innocent babies, the citizens will condemn me, and after death, even the messengers of Yamarāja will punish me mercilessly. I have broken all sacred ties of brotherhood. O noble Vasudeva! O chaste sister Devaki! Please, I beg you, forgive this wretched sinner! What has happened was ordained by unchangeable destiny. As clouds gather and disperse in the wind, so living beings are brought together and separated by time and karma."

### Kamsa Unlocks the Chains

Displaying genuine humility and brotherly affection for the moment, King Kamsa took the heavy iron keys with his own trembling hands:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 4, Verse 23**
> 
> *iti tau dampatī ślakṣṇaiḥ sāmabhiḥ sāntvayan nṛpaḥ*  
> *mocayām āsa nigaḍāt sva-suhṛd-bhāvam udvahan*  
> 
> **Translation:** Thus speaking sweet words of appeasement to the husband and wife, King Kamsa, manifesting a sincere and affectionate heart, personally unlocked their iron fetters and released them completely from captivity.

Kamsa gently removed the clanking iron manacles from Vasudeva's wrists and ankles. He then unlocked Devaki's chains, helped them to their feet, and treated them with deep, royal honor, giving them freedom to reside peacefully in Mathura.

### Vasudeva's Saintly Forgiveness and Philosophy

Vasudeva, being a foremost devotee of the Lord and a wise, self-realized soul, harbored no bitter grudge or desire for personal revenge against Kamsa. Seeing Kamsa's distress and genuine tears, Vasudeva replied with noble philosophical equanimity:

"O King! What you have spoken is true. Living entities in this material world are bewildered by the illusory energy of the Lord (*māyā*). Covered by false ego, people think, 'I am the doer, and I am the slayer,' forgetting that all beings act under the influence of their past karma and the supreme will of Providence. When one sees the transcendental truth that the eternal soul is never slain and that the physical body is merely a temporary garment, one does not harbor hatred or enmity toward anyone."

Hearing these magnanimous words, Kamsa felt deeply relieved and pacified. He offered his prostrations once more and returned to his royal palace for the night. 

Vasudeva and Devaki, having witnessed the divine fulfillment of the Lord's appearance and now completely free from the dungeon, praised the inconceivable arrangements of the Supreme Lord with grateful hearts.""",
                "questions": [
                    {
                        "question": "What realization caused King Kamsa's sudden shock and remorse?",
                        "options": [
                            {"text": "His destined slayer was alive elsewhere and his previous child murders were completely futile", "is_correct": True},
                            {"text": "The treasury was empty", "is_correct": False},
                            {"text": "A foreign king had declared war", "is_correct": False},
                            {"text": "The palace guards had rebelled", "is_correct": False}
                        ]
                    },
                    {
                        "question": "To what cruel creature did Kamsa compare himself when lamenting his past actions?",
                        "options": [
                            {"text": "A bloodthirsty, man-eating demon (rakshasa)", "is_correct": True},
                            {"text": "A wild elephant", "is_correct": False},
                            {"text": "A poisonous scorpion", "is_correct": False},
                            {"text": "A ravenous wolf", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What did Kamsa do when he entered the cell of Vasudeva and Devaki?",
                        "options": [
                            {"text": "He fell flat on the floor at their feet and wept bitterly, begging for forgiveness", "is_correct": True},
                            {"text": "He threatened them with his sword", "is_correct": False},
                            {"text": "He demanded where Krishna was hidden", "is_correct": False},
                            {"text": "He ordered double guards", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How did Kamsa describe the coming together and separation of living beings in this world?",
                        "options": [
                            {"text": "Like clouds gathered and dispersed by the wind according to karma", "is_correct": True},
                            {"text": "Like permanent iron statues", "is_correct": False},
                            {"text": "Like eternal friendships that never change", "is_correct": False},
                            {"text": "Like rivers that never meet", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What did King Kamsa personally do to release his prisoners?",
                        "options": [
                            {"text": "He personally unlocked their heavy iron shackles and chains with keys", "is_correct": True},
                            {"text": "He ordered the guards to throw them outside", "is_correct": False},
                            {"text": "He smashed the prison with a hammer", "is_correct": False},
                            {"text": "He transferred them to another fort", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How did Sri Vasudeva respond to Kamsa's plea for forgiveness?",
                        "options": [
                            {"text": "He responded with saintly equanimity and forgiveness, explaining karma and the soul", "is_correct": True},
                            {"text": "He struck Kamsa with his iron chains", "is_correct": False},
                            {"text": "He cursed Kamsa to die immediately", "is_correct": False},
                            {"text": "He mocked Kamsa's cowardice", "is_correct": False}
                        ]
                    },
                    {
                        "question": "According to Vasudeva's philosophical reply, what causes a person to mistakenly think 'I am the slayer'?",
                        "options": [
                            {"text": "False ego and bewilderment by the Lord's illusory energy (maya)", "is_correct": True},
                            {"text": "Too much Vedic knowledge", "is_correct": False},
                            {"text": "Drinking soma-rasa", "is_correct": False},
                            {"text": "Lack of physical training", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What does Srimad-Bhagavatam teach about the eternal soul in this context?",
                        "options": [
                            {"text": "The soul is eternal and never slain; only the material body changes", "is_correct": True},
                            {"text": "The soul dies with the body", "is_correct": False},
                            {"text": "The soul is made of stone", "is_correct": False},
                            {"text": "Only kings have eternal souls", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Where did Vasudeva and Devaki reside after being released by Kamsa?",
                        "options": [
                            {"text": "Freely in Mathura without harassment", "is_correct": True},
                            {"text": "In the deep forest of Naimisharanya", "is_correct": False},
                            {"text": "In the heavenly planets", "is_correct": False},
                            {"text": "Underground in a cave", "is_correct": False}
                        ]
                    },
                    {
                        "question": "In which chapter of Srimad-Bhagavatam Canto 10 is Kamsa's remorse and the release of Vasudeva-Devaki recorded?",
                        "options": [
                            {"text": "Chapter 4", "is_correct": True},
                            {"text": "Chapter 1", "is_correct": False},
                            {"text": "Chapter 8", "is_correct": False},
                            {"text": "Chapter 15", "is_correct": False}
                        ]
                    }
                ]
            },
            "ta": {
                "mainTopic": "கிருஷ்ண லீலைகள்",
                "subTopic": "கம்சனின் தற்காலிக மனவருத்தமும் வசுதேவர்-தேவகியின் விடுதலையும்",
                "content": """### கம்சனின் பேரதிர்ச்சியும் திடீர் துயரமும்

எட்டு கரங்களைக் கொண்ட துர்கா தேவி ஆகாயத்தில் இடிபோன்ற எச்சரிக்கையை விடுத்து மறைந்ததும், சிறைச்சாலை முற்றத்தில் கம்சன் கல்லென உறைந்து நின்றான். அவனது அசுர ஆணவமும் மமதையும் சுக்குநூறாக நொறுங்கின.

வானத்து அசரீரி வாக்கு பொய்யல்ல என்பதை அவன் பேரதிர்ச்சியுடன் உணர்ந்தான்: அவனைக் கொல்லப்போகும் பகவான் அவனது கைகளுக்கு எட்டாத இடத்தில் உயிரோடு வளர்ந்து வருகிறார்! மேலும், இதுவரை அவன் செய்த கொடூர பாவங்கள்—தேவகியின் ஆறு பச்சிளம் குழந்தைகளை ஈவுஇரக்கமின்றி கொன்ற பாதகங்கள்—முற்றிலும் பயனற்றதாகப் போய்விட்டன! எந்தப் பலனும் இல்லாமல் கொடிய பாவங்களை மட்டுமே அவன் சம்பாதித்துக்கொண்டான்.

நரக வேதனையின் பயமும், தீவிர குற்ற உணர்ச்சியும் கம்சனைத் தாக்கியது. உடனே அவன் வசுதேவரும் தேவகியும் இருந்த இருண்ட சிறைக் கொட்டடியினுள் விரைந்தான்.

### கால்களில் விழுந்து கண்ணீர் வடித்த கம்சன்

சிறைக்குள் நுழைந்த கம்சன், தனது தங்கை தேவகி மற்றும் மைத்துனர் வசுதேவரின் கால்களில் சாஷ்டாங்கமாக வீழ்ந்தான். உண்மையான அவமானத்தாலும் பயத்தாலும் அவனது கண்களிலிருந்து அருவிபோல கண்ணீர் கொட்டி, அவர்களது திருவடிகளை நனைத்தது.

குரல் தழுதழுக்க, அழுது புலம்பியபடி கம்சன் கூறினான்:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 4, சுலோகம் 19**
> 
> *அஹோ மயாகரிதம் பாபம் ராக்ஷஸைர் இவ கர்கஶை: |*  
> *பாலிகா பகினீ-புத்ரா காதிதா பஹவோ மயா ||*  
> 
> **பொருள்:** "அந்தோ! நான் எப்பேர்ப்பட்ட கொடும் பாவியாகிவிட்டேன்! மனிதர்களை வேட்டையாடும் கொடூர அரக்கனைப் போல, எனது அன்புத் தங்கையின் எத்தனையோ பச்சிளம் குழந்தைகளை இரக்கமின்றி நான் கொன்று குவித்தேன்!"

கம்சன் மேலும் கதறினான்: "எனக்காக எப்பேர்ப்பட்ட பயங்கரமான நரகம் காத்திருக்கிறதோ நான் அறியேன்! பாவம் அறியா குழந்தைகளைக் கொன்றதால் மக்கள் என்னை இகழ்வார்கள்; இறந்தபின் எமதூதர்கள் என்னை கொடூரமாக தண்டிப்பார்கள். சகோதர தர்மத்தை நான் முற்றிலுமாக அழித்துவிட்டேன். உத்தமரான வசுதேவரே! பதிவிரதையான தங்கை தேவகி! இந்த இழிந்த பாவியின் குற்றங்களை தயவுசெய்து மன்னியுங்கள்! நடந்தது அனைத்தும் மாறாத விதியின் விளையாட்டே. காற்றில் மேகங்கள் கூடுவதும் கலைவதும் போல, காலத்தாலும் கர்ம வினையாலும் ஜீவராசிகள் ஒன்றிணைவதும் பிரிவதும் நிகழ்கின்றன."

### விலங்குகளைத் தாமே அவிழ்த்த கம்சன்

அந்த கணத்தில் உண்மையான பணிவையும் பாசத்தையும் காட்டிய கம்சன், தனது நடுக்கம் கொண்ட கைகளால் சாவிகளை எடுத்தான்:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 4, சுலோகம் 23**
> 
> *இதி தௌ தம்பதீ ஶ்லக்ஷ்ணை: ஸாமபி: ஸாந்த்வயன் ந்ருப: |*  
> *மோசயாம ஆஸ நிகடாத் ஸ்வ-ஸுஹ்ருத்-பாவம் உத்வஹன் ||*  
> 
> **பொருள்:** இவ்வாறு இனிமையான சமாதான வார்த்தைகளால் தம்பதியினரை ஆற்றுப்படுத்திய மன்னன் கம்சன், உண்மையான பாசத்தோடும் நட்போடும் நேரில் அவர்களது இரும்பு விலங்குகளைத் திறந்து சிறையிலிருந்து விடுதலை செய்தான்.

வசுதேவரின் கைகளிலும் கால்களிலும் இருந்த கனத்த இரும்பு சங்கிலிகளை கம்சன் தாமே கழற்றினான். தேவகியின் விலங்குகளையும் திறந்து, அவர்களைத் தாங்கிப் பிடித்து எழுப்பினான். அவர்களுக்குப் பணிவிடை செய்து, மதுராவிலேயே மரியாதையுடன் வாழும் முழு சுதந்திரத்தையும் அளித்தான்.

### வசுதேவரின் திவ்ய மன்னிப்பும் தத்துவமும்

பகவானின் உன்னத பக்தரும் தத்துவ ஞானியுமான வசுதேவர், கம்சன் மீது எவ்வித தனிப்பட்ட குரோதமோ வஞ்சகமோ கொள்ளவில்லை. கம்சனின் மனவேதனையையும் உண்மையான கண்ணீரையும் கண்டு, வசுதேவர் உயர்ந்த ஆன்மீக ஞானத்தோடு அமைதியாகப் பதிலளித்தார்:

"மன்னரே! நீர் கூறியது உண்மையே. இந்த ஜட உலகிலுள்ள ஜீவன்கள் பகவானின் மாயா சக்தியால் மதிமயக்கமடைகின்றனர். அகங்காரத்தினால் சூழப்பட்ட மனிதன் 'நானே செய்கிறேன், நானே கொல்கிறேன்' என்று தவறாக எண்ணுகிறான்; ஆனால் அனைத்தும் அவரவர் பூர்வ கர்ம வினைப்படியும், பகவானின் சங்கல்பப்படியுமே நிகழ்கின்றன. நித்தியமான ஆத்மா ஒருபோதும் அழிக்கப்படுவதில்லை என்றும், பௌதிக உடலானது மாற்றமடையும் ஆடை மட்டுமே என்றும் உணர்ந்த ஞானிகள் எவர் மீதும் பகையோ வெறுப்போ கொள்வதில்லை."

வசுதேவரின் இந்த பெருந்தன்மையான வார்த்தைகளைக் கேட்டு கம்சன் பெருமூச்சு விட்டு ஆறுதலடைந்தான். மீண்டும் அவர்களை வணங்கிவிட்டு, அன்றைய இரவுக்கு தனது அரண்மனைக்குத் திரும்பினான்.

பகவானின் அவதார வாக்கின் நிறைவேற்றத்தைக் கண்டு வியந்த வசுதேவரும் தேவகியும், சிறையிலிருந்து விடுபட்டு, முழுமுதற் கடவுளான பகவானின் கருணையை மனதாரப் போற்றினர்.""",
                "questions": [
                    {
                        "question": "கம்சனுக்கு திடீர் அதிர்ச்சியும் குற்ற உணர்ச்சியும் ஏற்படக் காரணம் என்ன?",
                        "options": [
                            {"text": "தன்னைக் கொல்லும் எதிரி உயிரோடு உள்ளார் என்பதும், தனது முந்தைய கொலைகள் வீணாயின என்பதும் உணர்ந்ததால்", "is_correct": True},
                            {"text": "கஜானா காலியாகிவிட்டது என்பதால்", "is_correct": False},
                            {"text": "பக்கத்து நாட்டு மன்னன் போர் தொடுத்ததால்", "is_correct": False},
                            {"text": "காவலர்கள் புரட்சி செய்ததால்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "தமது முந்தைய கொடூரச் செயல்களை நினைத்து கம்சன் தன்னை எதனுடன் ஒப்பிட்டான்?",
                        "options": [
                            {"text": "மனிதர்களை வேட்டையாடும் கொடூர அரக்கன் (ராட்சசன்)", "is_correct": True},
                            {"text": "காட்டு யானை", "is_correct": False},
                            {"text": "நச்சுத் தேள்", "is_correct": False},
                            {"text": "பசியுள்ள ஓநாய்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "சிறைக்குள் நுழைந்த கம்சன் என்ன செய்தான்?",
                        "options": [
                            {"text": "வசுதேவர்-தேவகியின் கால்களில் சாஷ்டாங்கமாக வீழ்ந்து அழுது மன்னிப்புக் கேட்டான்", "is_correct": True},
                            {"text": "வாளால் அவர்களை மிரட்டினான்", "is_correct": False},
                            {"text": "கிருஷ்ணர் எங்கே என்று கேட்டான்", "is_correct": False},
                            {"text": "காவலை இருமடங்காக அதிகரித்தான்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ஜீவராசிகள் ஒன்று சேர்வதையும் பிரிவதையும் கம்சன் எதனுடன் ஒப்பிட்டான்?",
                        "options": [
                            {"text": "காற்றில் மேகங்கள் கூடுவதும் கலைவதும் போல", "is_correct": True},
                            {"text": "நிலையான பாறைகள் போல", "is_correct": False},
                            {"text": "ஒருபோதும் மாறாத நட்புகள் போல", "is_correct": False},
                            {"text": "என்றும் இணையாத நதிகள் போல", "is_correct": False}
                        ]
                    },
                    {
                        "question": "சிறைக் கைதிகளை விடுவிக்க கம்சன் என்ன செய்தான்?",
                        "options": [
                            {"text": "தனது சொந்த கைகளால் இரும்பு விலங்குகளை சாவியிட்டுத் திறந்து விடுவித்தான்", "is_correct": True},
                            {"text": "வெளியே தூக்கி எறிய உத்தரவிட்டான்", "is_correct": False},
                            {"text": "சுத்தியால் சிறையை உடைத்தான்", "is_correct": False},
                            {"text": "வேறொரு கோட்டைக்கு மாற்றினான்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "கம்சனின் மன்னிப்புக் கோரலுக்கு வசுதேவர் எவ்வாறு பதிலளித்தார்?",
                        "options": [
                            {"text": "எவ்வித குரோதமும் இன்றி கர்ம வினையையும் ஆத்ம தத்துவத்தையும் விளக்கி மன்னித்தார்", "is_correct": True},
                            {"text": "இரும்பு சங்கிலியால் கம்சனைத் தாக்கினார்", "is_correct": False},
                            {"text": "கம்சனை உடனே சாகும்படி சாபமிட்டார்", "is_correct": False},
                            {"text": "கம்சனின் கோழைத்தனத்தை ஏளனம் செய்தார்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "வசுதேவரின் தத்துவ விளக்கத்தின்படி 'நானே செய்கிறேன்' என்ற மயக்கத்தை தருவது எது?",
                        "options": [
                            {"text": "அகங்காரமும் பகவானின் மாயா சக்தியின் மயக்கமும்", "is_correct": True},
                            {"text": "அதிகமான வேத ஞானம்", "is_correct": False},
                            {"text": "சோமபானம் குடிப்பது", "is_correct": False},
                            {"text": "உடற்பயிற்சி இல்லாதது", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ஆத்மாவைப் பற்றி இந்த பகுதியில் சாஸ்திரம் என்ன கற்பிக்கிறது?",
                        "options": [
                            {"text": "ஆத்மா நித்தியமானது, கொல்லப்படுவதில்லை; உடல் மட்டுமே மாறுகிறது", "is_correct": True},
                            {"text": "உடலுடன் ஆத்மாவும் அழிகிறது", "is_correct": False},
                            {"text": "ஆத்மா கல்லால் ஆனது", "is_correct": False},
                            {"text": "மன்னர்களுக்கு மட்டுமே ஆத்மா உண்டு", "is_correct": False}
                        ]
                    },
                    {
                        "question": "விடுதலைக்குப் பிறகு வசுதேவரும் தேவகியும் எங்கு வசித்தனர்?",
                        "options": [
                            {"text": "மதுராவிலேயே எவ்வித தொல்லையுமின்றி சுதந்திரமாக வசித்தனர்", "is_correct": True},
                            {"text": "நைமிசாரண்ய காட்டில்", "is_correct": False},
                            {"text": "தேவலோகத்தில்", "is_correct": False},
                            {"text": "பாதாள குகையில்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "கம்சனின் மனவருத்தமும் வசுதேவர்-தேவகியின் விடுதலையும் பாகவதத்தில் எந்த அத்தியாயத்தில் உள்ளது?",
                        "options": [
                            {"text": "அத்தியாயம் 4", "is_correct": True},
                            {"text": "அத்தியாயம் 1", "is_correct": False},
                            {"text": "அத்தியாயம் 7", "is_correct": False},
                            {"text": "அத்தியாயம் 12", "is_correct": False}
                        ]
                    }
                ]
            },
            "hi": {
                "mainTopic": "कृष्ण लीलाएं",
                "subTopic": "कंस का पश्चाताप और वसुदेव-देवकी की कारागार से मुक्ति",
                "content": """### कंस का विस्मय और तीव्र आत्मग्लानि

आकाश में अष्टभुजा भगवती दुर्गा की गर्जना सुनकर और उनके अंतर्ध्यान होने के पश्चात, कंस कारागार के आंगन में जड़वत खड़ा रह गया। उसका समस्त आसुरी अहंकार और क्रूरता पल भर में धूल-धूसरित हो गई।

उसे अत्यंत भयंकर सत्य का साक्षात्कार हुआ कि आकाशवाणी सर्वथा सत्य थी: उसका वध करने वाला परमेश्वर कहीं और सुरक्षित पहुंच चुका है! इसके साथ ही, उसने जो अमानवीय पाप किए थे—देवकी के छह निर्दोष नवजात शिशुओं की नृशंस हत्या—वे सब सर्वथा व्यर्थ सिद्ध हुए! उसे बिना किसी लाभ के केवल घोर पाप और नरक का भागी बनना पड़ा।

तीव्र भय, पश्चाताप और आत्मग्लानि से व्याकुल होकर कंस तुरंत उस अंधकारमय कारागार में गया जहां वसुदेव और देवकी उपस्थित थे।

### चरणों में गिरकर कंस का अश्रुपात

कारागार में पहुंचकर कंस अपनी बहन देवकी और बहनोई वसुदेव के चरणों में दंडवत गिर पड़ा। पश्चाताप और लज्जा के कारण उसकी आंखों से अविरल आंसुओं की धारा बह निकली, जिसने उनके चरणों को भिगो दिया।

गले में रुंधे हुए स्वर से विलाप करते हुए कंस ने कहा:

> **श्रीमद्भागवतम्, स्कंध 10, अध्याय 4, श्लोक 19**
> 
> *अहो मयाचरितं पापं राक्षसैर् इव कर्कशैः ।*  
> *बालिका भगिनी-पुत्रा घातिता बहवो मया ॥*  
> 
> **भावार्थ:** "हाय! मुझ दुराचारी ने कितना घोर पाप किया है! नरभक्षी क्रूर राक्षसों की भांति मैंने अपनी ही सगी बहन के नन्हें-मुन्हें अबोध बालकों का निर्दयतापूर्वक वध कर दिया!"

कंस विलाप करते हुए आगे बोला: "मैं नहीं जानता कि मेरे लिए कौन सा भयानक नरक प्रतीक्षा कर रहा है! निर्दोष बच्चों की हत्या के कारण जनसाधारण मुझे धिक्कारेगा और मृत्यु के उपरांत यमदूत मुझे असह्य यातनाएं देंगे। हे धर्मात्मा वसुदेव! हे पतिव्रता बहन देवकी! इस अधम पापी को क्षमा कर दो! जो कुछ हुआ, वह अटल प्रारब्ध का ही खेल था। जैसे वायु के झोंकों से आकाश में बादल मिलते और बिछड़ जाते हैं, वैसे ही कर्मों की गति से प्राणी एक-दूसरे से मिलते और बिछड़ते हैं।"

### बेड़ियों को कंस ने स्वयं खोला

उस क्षण स्वाभाविक भ्रातृ-प्रेम और नम्रता का परिचय देते हुए राजा कंस ने कांपते हाथों से चाबियां लीं:

> **श्रीमद्भागवतम्, स्कंध 10, अध्याय 4, श्लोक 23**
> 
> *इति तौ दम्पती श्लक्ष्णैः सामभिः सान्त्वयन् नृपः ।*  
> *मोचयामास निगडात् स्व-सुहृद्-भावम् उद्वहन् ॥*  
> 
> **भावार्थ:** इस प्रकार मधुर वचनों से उस पति-पत्नी को सांत्वना देते हुए राजा कंस ने सच्चे स्नेह और सौहार्दपूर्ण भाव से स्वयं उनके हाथ-पैरों की बेड़ियां खोलकर उन्हें कारागार से मुक्त कर दिया।

कंस ने वसुदेव और देवकी की भारी लोहे की जंजीरें स्वयं अपने हाथों से उतारीं। उन्हें आदरपूर्वक खड़ा किया और मथुरा में ही स्वतंत्र रूप से सम्मानपूर्वक रहने का आदेश दिया।

### वसुदेव जी की संत-सुलभ क्षमाशीलता और तत्वज्ञान

भगवान के परम भक्त और तत्वज्ञानी महात्मा वसुदेव के हृदय में कंस के प्रति तनिक भी व्यक्तिगत द्वेष या प्रतिशोध की भावना न थी। कंस के पश्चाताप और आंसुओं को देखकर वसुदेव जी ने अत्यंत शांत और दार्शनिक वाणी में कहा:

"हे राजन्! आपने जो कहा, वह सत्य है। इस संसार में सभी जीव भगवान की अचिंत्य माया के वशीभूत हैं। अहंकार से आच्छादित होकर अज्ञानी मनुष्य सोचता है कि 'मैं कर्ता हूं, मैं मारने वाला हूं', जबकि वास्तव में सभी प्राणी अपने पूर्व जन्मों के कर्मफल और ईश्वर की इच्छा से ही संचालित होते हैं। जो ज्ञानी यह जानते हैं कि अविनाशी आत्मा कभी मरती नहीं और यह भौतिक शरीर केवल वस्त्र के समान बदलता रहता है, वे किसी से भी बैर या घृणा नहीं करते।"

वसुदेव जी के इन दयालु वचनों को सुनकर कंस को बड़ी सांत्वना मिली। उसने पुनः उनके चरणों में प्रणाम किया और रात बिताने के लिए अपने राजभवन लौट गया।

वसुदेव और देवकी कारागार से पूर्णतः मुक्त होकर, भगवान के प्राकट्य और उनकी अचिंत्य लीलाओं का कृतज्ञतापूर्वक स्मरण करने लगे।""",
                "questions": [
                    {
                        "question": "कंस के अचानक पश्चाताप और भय का मुख्य कारण क्या था?",
                        "options": [
                            {"text": "उसे ज्ञात हुआ कि उसका काल जीवित है और उसकी पुरानी हत्याएं व्यर्थ थीं", "is_correct": True},
                            {"text": "उसका खजाना खाली हो गया था", "is_correct": False},
                            {"text": "पड़ोसी राजा ने आक्रमण कर दिया था", "is_correct": False},
                            {"text": "प्रजा ने विद्रोह कर दिया था", "is_correct": False}
                        ]
                    },
                    {
                        "question": "कंस ने पश्चाताप करते हुए स्वयं की तुलना किस क्रूर प्राणी से की?",
                        "options": [
                            {"text": "नरभक्षी क्रूर राक्षस से", "is_correct": True},
                            {"text": "जंगली हाथी से", "is_correct": False},
                            {"text": "बिच्छू से", "is_correct": False},
                            {"text": "भेड़िए से", "is_correct": False}
                        ]
                    },
                    {
                        "question": "कारागार में जाकर कंस ने क्या किया?",
                        "options": [
                            {"text": "वसुदेव और देवकी के चरणों में गिरकर रोते हुए क्षमा मांगी", "is_correct": True},
                            {"text": "तलवार से धमकाया", "is_correct": False},
                            {"text": "कहा कि कृष्ण कहां है", "is_correct": False},
                            {"text": "पहरेदारों को दंडित किया", "is_correct": False}
                        ]
                    },
                    {
                        "question": "संसार में जीवों के मिलने और बिछड़ने की उपमा कंस ने किससे दी?",
                        "options": [
                            {"text": "हवा के झोंकों से बादलों के मिलने और बिछड़ने से", "is_correct": True},
                            {"text": "पत्थरों से", "is_correct": False},
                            {"text": "स्थिर मित्रता से", "is_correct": False},
                            {"text": "सूखी नदियों से", "is_correct": False}
                        ]
                    },
                    {
                        "question": "कंस ने वसुदेव और देवकी को मुक्त करने के लिए क्या किया?",
                        "options": [
                            {"text": "स्वयं अपने हाथों से चाबियों द्वारा उनकी बेड़ियां खोलीं", "is_correct": True},
                            {"text": "सैनिकों से धक्का देकर बाहर निकलवाया", "is_correct": False},
                            {"text": "हथौड़े से ताले तोड़े", "is_correct": False},
                            {"text": "दूसरे किले में भेज दिया", "is_correct": False}
                        ]
                    },
                    {
                        "question": "वसुदेव जी ने कंस के पश्चाताप पर कैसी प्रतिक्रिया दी?",
                        "options": [
                            {"text": "संत-सुलभ समभाव से क्षमा करते हुए कर्म और आत्मा का तत्व समझाया", "is_correct": True},
                            {"text": "लोहे की जंजीर से कंस पर प्रहार किया", "is_correct": False},
                            {"text": "कंस को तुरंत मरने का श्राप दिया", "is_correct": False},
                            {"text": "कंस का उपहास उड़ाया", "is_correct": False}
                        ]
                    },
                    {
                        "question": "वसुदेव जी के अनुसार मनुष्य में 'मैं कर्ता हूं' का भ्रम किससे उत्पन्न होता है?",
                        "options": [
                            {"text": "अहंकार और भगवान की माया के प्रभाव से", "is_correct": True},
                            {"text": "अत्यधिक वेदों के अध्ययन से", "is_correct": False},
                            {"text": "सोमरस पीने से", "is_correct": False},
                            {"text": "शारीरिक दुर्बलता से", "is_correct": False}
                        ]
                    },
                    {
                        "question": "इस प्रसंग में श्रीमद्भागवतम् आत्मा के विषय में क्या सिखाता है?",
                        "options": [
                            {"text": "आत्मा नित्य और अविनाशी है, केवल भौतिक शरीर बदलता है", "is_correct": True},
                            {"text": "शरीर के साथ आत्मा भी मर जाती है", "is_correct": False},
                            {"text": "आत्मा पत्थर की बनी है", "is_correct": False},
                            {"text": "केवल राजाओं के पास आत्मा होती है", "is_correct": False}
                        ]
                    },
                    {
                        "question": "मुक्ति के बाद वसुदेव और देवकी कहां रहने लगे?",
                        "options": [
                            {"text": "मथुरा में ही स्वतंत्रता और सम्मानपूर्वक", "is_correct": True},
                            {"text": "नैमिषारण्य के जंगलों में", "is_correct": False},
                            {"text": "स्वर्गलोक में", "is_correct": False},
                            {"text": "भूमिगत गुफा में", "is_correct": False}
                        ]
                    },
                    {
                        "question": "कंस का पश्चाताप और वसुदेव-देवकी की मुक्ति श्रीमद्भागवतम् के किस अध्याय में है?",
                        "options": [
                            {"text": "अध्याय 4", "is_correct": True},
                            {"text": "अध्याय 1", "is_correct": False},
                            {"text": "अध्याय 9", "is_correct": False},
                            {"text": "अध्याय 14", "is_correct": False}
                        ]
                    }
                ]
            },
            "ml": {
                "mainTopic": "കൃഷ്ണ ലീലകൾ",
                "subTopic": "കംസന്റെ പശ്ചാത്താപവും വസുദേവ-ദേവകിമാരുടെ മോചനവും",
                "content": """### കംസന്റെ നടുക്കവും കഠിനമായ ദുഃഖവും

ആകാശത്തുനിന്നും ദുർഗ്ഗാദേവി നൽകിയ ഇടിത്തീപോലെയുള്ള മുന്നറിയിപ്പിനു ശേഷം ദേവി അന്തർദ്ധാനം ചെയ്തപ്പോൾ, കംസൻ കാരാഗൃഹമുറ്റത്ത് ഭയവിഹ്വലനായി നിന്നുപോയി. അവന്റെ ആസുരികമായ അഹങ്കാരം പൂർണ്ണമായും തകർന്നുപോയി.

ആകാശവാണി അസത്യമായിരുന്നില്ലെന്ന് അവൻ തിരിച്ചറിഞ്ഞു: തന്നെ വധിക്കാനുള്ളവൻ മറ്റൊരിടത്ത് സുരക്ഷിതനായി വളരുന്നു! മാത്രവുമല്ല, താൻ ഇതുവരെ ചെയ്ത ക്രൂരമായ കൊലപാതകങ്ങൾ—ദേവകിയുടെ ആറ് പിഞ്ചുകുഞ്ഞുങ്ങളെ അടിച്ചുകൊന്ന പാപം—തികച്ചും നിഷ്ഫലമായിപ്പോയി! യാതൊരു പ്രയോജനവുമില്ലാതെ കൊടുംപാപത്തിന്റെ ഭാണ്ഡം മാത്രമാണ് താൻ ചുമന്നതെന്ന് കംസൻ ഞെട്ടലോടെ മനസ്സിലാക്കി.

നരകഭയത്താലും കഠിനമായ പശ്ചാത്താപത്താലും ഉരുകിയ കംസൻ ഉടൻതന്നെ വസുദേവരും ദേവകിയും ഉണ്ടായിരുന്ന കാരാഗൃഹത്തിലേക്ക് പാഞ്ഞെത്തി.

### മാപ്പപേക്ഷിച്ച് കാൽക്കൽ വീഴുന്ന കംസൻ

കാരാഗൃഹത്തിൽ പ്രവേശിച്ച കംസൻ തന്റെ സഹോദരിയായ ദേവകിയുടെയും വസുദേവരുടെയും പാദങ്ങളിൽ സാഷ്ടാംഗം പ്രണമിച്ച് വീണു. ലജ്ജയും പശ്ചാത്താപവും കാരണം അവന്റെ കണ്ണുകളിൽ നിന്ന് കണ്ണീരൊഴുകി അവരുടെ പാദങ്ങളെ നനച്ചു.

തൊണ്ടയിടറിക്കൊണ്ട് കംസൻ വിലപിച്ചു:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അദ്ധ്യായം 4, ശ്ലോകം 19**
> 
> *അഹോ മയാചരിതം പാപം രാക്ഷസൈർ ഇവ കർക്കശൈഃ |*  
> *ബാലികാ ഭഗിനീ-പുത്രാ ഘാതിതാ ബഹവോ മയാ ||*  
> 
> **അർത്ഥം:** "അയ്യോ! ഞാൻ എന്തുമാത്രം വലിയ പാപിയാണ്! നരഭോജികളായ ക്രൂരരാക്ഷസന്മാരെപ്പോലെ എന്റെ സ്വന്തം സഹോദരിയുടെ എത്രയോ പിഞ്ചോമനകളെ ഞാൻ നിഷ്കരുണം കൊന്നൊടുക്കി!"

കംസൻ തുടർന്നു: "എനിക്കായി ഏതു ഭയാനകമായ നരകമാണ് കാത്തിരിക്കുന്നതെന്ന് എനിക്കറിയില്ല! കുഞ്ഞുങ്ങളെ കൊന്ന എന്നെ ജനങ്ങൾ ശപിക്കും, യമദൂതന്മാർ കഠിനമായി ശിക്ഷിക്കും. ധർമ്മിഷ്ഠനായ വസുദേവരേ! പതിവ്രതയായ ദേവകീ! ഈ നീചനായ പാപിയോട് ദയവുചെയ്ത് ക്ഷമിക്കൂ! സംഭവിച്ചതെല്ലാം കർമ്മഫലവും വിധിയുമാണ്. കാറ്റിൽ മേഘങ്ങൾ കൂടുകയും പിരിയുകയും ചെയ്യുന്നതുപോലെ, ജീവികൾ തങ്ങളുടെ കർമ്മഫലത്താൽ കണ്ടുമുട്ടുകയും വേർപിരിയുകയും ചെയ്യുന്നു."

### കംസൻ ചങ്ങലകൾ അഴിച്ചുമാറ്റുന്നു

ആ നിമിഷത്തിൽ യഥാർത്ഥ വാത്സല്യവും വിനയവും പ്രകടിപ്പിച്ചുകൊണ്ട് കംസൻ വിറയ്ക്കുന്ന കൈകളോടെ താക്കോലുകൾ എടുത്തു:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അദ്ധ്യായം 4, ശ്ലോകം 23**
> 
> *ഇതി തൗ ദമ്പതീ ശ്ലക്ഷ്ണൈഃ സാമഭിഃ സാന്ത്വയൻ നൃപഃ |*  
> *മോചയാമാസ നിഗഡാത് സ്വ-സുഹൃദ്-ഭാവമ് ഉദ്വഹൻ ||*  
> 
> **അർത്ഥം:** ഇപ്രകാരം മധുരവചനങ്ങളാൽ ദമ്പതികളെ സമാശ്വസിപ്പിച്ചുകൊണ്ട്, സ്നേഹവാത്സല്യങ്ങളോടെ കംസരാജാവ് സ്വയം അവരുടെ കാൽവിലങ്ങുകൾ അഴിച്ച് അവരെ പൂർണ്ണമായി മോചിപ്പിച്ചു.

വസുദേവരുടെയും ദേവകിയുടെയും ഭാരമേറിയ ഇരുമ്പുചങ്ങലകൾ കംസൻ സ്വന്തം കൈകളാൽ അഴിച്ചുമാറ്റി. അവരെ എഴുന്നേൽപ്പിച്ച് ആദരിക്കുകയും മഥുരയിൽ സമാധാനത്തോടെ ജീവിക്കാനുള്ള സ്വാതന്ത്ര്യം നൽകുകയും ചെയ്തു.

### വസുദേവരുടെ ദിവ്യമായ ക്ഷമയും തത്ത്വചിന്തയും

ഭഗവാന്റെ പരമഭക്തനായ വസുദേവർക്ക് കംസനോട് യാതൊരു വ്യക്തിവിദ്വേഷവുമുണ്ടായിരുന്നില്ല. കംസന്റെ പശ്ചാത്താപവും കണ്ണീരും കണ്ട് വസുദേവർ ശാന്തമായി പറഞ്ഞു:

"രാജാവേ! അങ്ങ് പറഞ്ഞത് സത്യമാണ്. ഈ ലോകത്തിലെ ജീവികൾ ഭഗവാന്റെ മായാശക്തിയാൽ ഭ്രമിക്കപ്പെടുന്നു. അഹംഭാവം കാരണം മനുഷ്യൻ 'ഞാനാണ് കൊല്ലുന്നത്, ഞാനാണ് ചെയ്യുന്നത്' എന്ന് തെറ്റിദ്ധരിക്കുന്നു. എന്നാൽ ജീവികളെല്ലാം തങ്ങളുടെ പൂർവ്വകർമ്മത്താലാണ് പ്രവർത്തിക്കുന്നത്. ശാശ്വതമായ ആത്മാവ് ഒരിക്കലും കൊല്ലപ്പെടുന്നില്ലെന്നും ശരീരം മാറുന്ന വസ്ത്രം മാത്രമാണെന്നും അറിയുന്ന ജ്ഞാനികൾ ആരോടും ശത്രുത പുലർത്തുന്നില്ല."

ഈ വാക്കുകൾ കേട്ട് കംസൻ ആശ്വസിച്ചു. അവൻ വീണ്ടും അവരെ വണങ്ങി തന്റെ കൊട്ടാരത്തിലേക്ക് മടങ്ങി.

കാരാഗൃഹത്തിൽ നിന്ന് മുക്തരായ വസുദേവരും ദേവകിയും ഭഗവാന്റെ ദിവ്യമായ അവതാരലീലകളെ ഓർത്ത് നന്ദിയോടെ സ്തുതിച്ചു.""",
                "questions": [
                    {
                        "question": "കംസന് പെട്ടെന്ന് പശ്ചാത്താപവും ഭയവും തോന്നാൻ കാരണമെന്ത്?",
                        "options": [
                            {"text": "തന്റെ ശത്രു ജീവിച്ചിരിപ്പുണ്ടെന്നും മുൻപത്തെ കൊലപാതകങ്ങൾ വ്യർത്ഥമാണെന്നും മനസ്സിലായതിനാൽ", "is_correct": True},
                            {"text": "ഖജനാവ് കാലിയായതുകൊണ്ട്", "is_correct": False},
                            {"text": "അയൽരാജാവ് യുദ്ധം പ്രഖ്യാപിച്ചതുകൊണ്ട്", "is_correct": False},
                            {"text": "കാവൽക്കാർ കലാപം ഉണ്ടാക്കിയതുകൊണ്ട്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "തന്റെ ക്രൂരതയെ ഓർത്ത് കംസൻ സ്വയം ഏതു ജീവിയോടാണ് ഉപമിച്ചത്?",
                        "options": [
                            {"text": "നരഭോജിയായ ക്രൂരരാക്ഷസനോട്", "is_correct": True},
                            {"text": "കാട്ടാനയോട്", "is_correct": False},
                            {"text": "തേളിനോട്", "is_correct": False},
                            {"text": "ചെന്നായയോട്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "കാരാഗൃഹത്തിൽ പ്രവേശിച്ച കംസൻ എന്താണ് ചെയ്തത്?",
                        "options": [
                            {"text": "വസുദേവ-ദേവകിമാരുടെ കാൽക്കൽ വീണ് മാപ്പപേക്ഷിച്ചു", "is_correct": True},
                            {"text": "വാളോങ്ങി ഭീഷണിപ്പെടുത്തി", "is_correct": False},
                            {"text": "കൃഷ്ണൻ എവിടെയെന്ന് ചോദിച്ചു", "is_correct": False},
                            {"text": "കാവൽ ഇരട്ടിയാക്കി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ജീവികൾ ഒന്നിക്കുന്നതിനെയും വേർപിരിയുന്നതിനെയും കംസൻ എന്തിനോടാണ് ഉപമിച്ചത്?",
                        "options": [
                            {"text": "കാറ്റിൽ മേഘങ്ങൾ കൂടുകയും പിരിയുകയും ചെയ്യുന്നതിനോട്", "is_correct": True},
                            {"text": "പാറകളോട്", "is_correct": False},
                            {"text": "സ്ഥിരമായ സൗഹൃദങ്ങളോട്", "is_correct": False},
                            {"text": "നദികളോട്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "തടവുകാരെ മോചിപ്പിക്കാൻ കംസൻ എന്താണ് ചെയ്തത്?",
                        "options": [
                            {"text": "സ്വന്തം കൈകളാൽ താക്കോൽ ഉപയോഗിച്ച് ചങ്ങലകൾ അഴിച്ചു", "is_correct": True},
                            {"text": "കാവൽക്കാരോട് പുറത്താക്കാൻ പറഞ്ഞു", "is_correct": False},
                            {"text": "ചുറ്റികകൊണ്ട് പൂട്ട് തകർത്തു", "is_correct": False},
                            {"text": "മറ്റൊരു കോട്ടയിലേക്ക് മാറ്റി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "കംസന്റെ മാപ്പപേക്ഷയോട് വസുദേവർ എങ്ങനെ പ്രതികരിച്ചു?",
                        "options": [
                            {"text": "യാതൊരു വിദ്വേഷവുമില്ലാതെ ക്ഷമിക്കുകയും ആത്മതത്ത്വം ഉപദേശിക്കുകയും ചെയ്തു", "is_correct": True},
                            {"text": "ചങ്ങലകൊണ്ട് കംസനെ അടിച്ചു", "is_correct": False},
                            {"text": "ഉടൻ മരിക്കട്ടെയെന്ന് ശപിച്ചു", "is_correct": False},
                            {"text": "കംസനെ പരിഹസിച്ചു", "is_correct": False}
                        ]
                    },
                    {
                        "question": "വസുദേവരുടെ അഭിപ്രായത്തിൽ മനുഷ്യന് 'ഞാനാണ് കൊല്ലുന്നത്' എന്ന അഹംഭാവം ഉണ്ടാകുന്നത് എന്തുകൊണ്ടാണ്?",
                        "options": [
                            {"text": "അഹങ്കാരത്താലും മായാമോഹത്താലും", "is_correct": True},
                            {"text": "വേദപഠനം കൂടിയതുകൊണ്ട്", "is_correct": False},
                            {"text": "സോമരസം കുടിച്ചതുകൊണ്ട്", "is_correct": False},
                            {"text": "ശരീരബലക്കുറവുകൊണ്ട്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ആത്മാവിനെക്കുറിച്ച് ശ്രീമദ് ഭാഗവതം ഇവിടെ എന്തു പഠിപ്പിക്കുന്നു?",
                        "options": [
                            {"text": "ആത്മാവ് ശാശ്വതമാണ്, നശിക്കുന്നില്ല; ശരീരം മാറുന്ന വസ്ത്രം മാത്രം", "is_correct": True},
                            {"text": "ശരീരത്തോടൊപ്പം ആത്മാവും മരിക്കുന്നു", "is_correct": False},
                            {"text": "ആത്മാവ് കല്ലുകൊണ്ടാണ് നിർമ്മിച്ചിരിക്കുന്നത്", "is_correct": False},
                            {"text": "രാജാക്കന്മാർക്ക് മാത്രമേ ആത്മാവുള്ളൂ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "മോചനത്തിനു ശേഷം വസുദേവരും ദേവകിയും എവിടെയാണ് താമസിച്ചത്?",
                        "options": [
                            {"text": "മഥുരയിൽത്തന്നെ സ്വതന്ത്രമായി ആദരവോടെ", "is_correct": True},
                            {"text": "നൈമിശാരണ്യത്തിലെ കാട്ടിൽ", "is_correct": False},
                            {"text": "സ്വർഗ്ഗത്തിൽ", "is_correct": False},
                            {"text": "ഗുഹയിൽ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "കംസന്റെ പശ്ചാത്താപവും വസുദേവ-ദേവകിമാരുടെ മോചനവും ഭാഗവതത്തിലെ ഏത് അദ്ധ്യായത്തിലാണ്?",
                        "options": [
                            {"text": "അദ്ധ്യായം 4", "is_correct": True},
                            {"text": "അദ്ധ്യായം 1", "is_correct": False},
                            {"text": "അദ്ധ്യായം 6", "is_correct": False},
                            {"text": "അദ്ധ്യായം 10", "is_correct": False}
                        ]
                    }
                ]
            },
            "bn": {
                "mainTopic": "কৃষ্ণ লীলা",
                "subTopic": "কংসের অনুশোচনা ও বসুদেব-দেবকীর কারামুক্তি",
                "content": """### কংসের তীব্র অনুশোচনা ও অন্তর্বেদনা

আকাশে দেবী দুর্গার সেই বজ্রনির্ঘোষ সাবধানবাণীর পর দেবী অন্তর্হিতা হলে, কংস স্তম্ভিত হয়ে কারাগারের প্রাঙ্গণে দাঁড়িয়ে রইল। তার সমস্ত আসুরিক দম্ভ ও অহংকার চূর্ণ-বিচূর্ণ হয়ে গেল।

সে নিদারুণভাবে উপলব্ধি করল যে আকাশবাণী কোনো মিথ্যা কল্পনা ছিল না: তাকে বধকারী পরমেশ্বর সত্যই অন্যত্র নিরাপদে জন্মগ্রহণ করেছেন! অধিকন্তু, এযাবৎ সে যে ভয়াবহ নৃশংসতা করেছে—দেবকীর ছয়টি নিষ্পাপ নবজাত শিশুকে নির্মমভাবে হত্যা করেছে—তা সম্পূর্ণ নিষ্ফল প্রমাণিত হয়েছে! কোনো ফল লাভ ব্যতিরেকেই সে কেবল মহাপাপের বোঝা অর্জন করেছে।

নরকযন্ত্রণার ভয়ে ও তীব্র অনুশোচনায় দগ্ধ হয়ে কংস তৎক্ষণাৎ সেই অন্ধকার কারাগারে প্রবেশ করল যেখানে বসুদেব ও দেবকী উপস্থিত ছিলেন।

### চরণে লুটিয়ে কংসের অশ্রুপাত

কারাগারে প্রবেশ করে কংস ভগিনী দেবকী ও ভগিনীপতি বসুদেবের চরণে সাষ্টাঙ্গে লুটিয়ে পড়ল। তীব্র লজ্জা ও অনুশোচনায় তার চক্ষু হতে অশ্রুধারা প্লাবনের মতো প্রবাহিত হয়ে তাঁদের চরণযুগল ভিজিয়ে দিল।

বাষ্পরুদ্ধ কণ্ঠে বিলাপ করতে করতে কংস বলল:

> **শ্রীমদ্ভাগবত, স্কন্ধ ১০, অধ্যায় ৪, শ্লোক ১৯**
> 
> *অহো ময়াচরিতং পাপং রাক্ষসৈর্ ইব কর্কশৈঃ ।*  
> *বালিকা ভগিনী-পুত্রা ঘাতিতা বহবো ময়া ॥*  
> 
> **অনুবাদ:** "হায়! আমি কি মহাপাপী! নরখাদক নিষ্ঠুর রাক্ষসদের মতো আমি আমার স্নেহের ভগিনীর কত নিষ্পাপ শিশুকে নির্মমভাবে হত্যা করেছি!"

কংস আরও বিলাপ করল: "আমি জানি না আমার জন্য কি ভয়ঙ্কর নরক প্রতীক্ষা করছে! নিষ্পাপ শিশুদের হত্যার জন্য জনসাধারণ আমাকে ধিক্কার দেবে এবং মৃত্যুর পর যমদূতরা আমাকে নির্দয় শাস্তি দেবে। হে ধার্মিকশ্রেষ্ঠ বসুদেব! হে পতিব্রতা ভগিনী দেবকী! এই অধম পাপীকে ক্ষমা করো! যা ঘটেছে তা অলঙ্ঘনীয় প্রারব্ধেরই খেলা। বাতাসে যেমন মেঘমালা মিলিত ও বিচ্ছিন্ন হয়, তদ্রূপ কর্মফলের দ্বারা জীবের মিলন ও বিয়োগ ঘটে থাকে।"

### শৃঙ্খল উন্মোচন ও মুক্তিদান

সেই মুহূর্তে অকপট অনুতাপ ও ভ্রাতৃস্নেহ প্রদর্শন করে রাজা কংস নিজ কম্পিত হস্তে চাবি তুলে নিল:

> **শ্রীমদ্ভাগবত, স্কন্ধ ১০, অধ্যায় ৪, শ্লোক ২৩**
> 
> *ইতি তৌ দম্পতী শ্লক্ষ্ণৈঃ সামভিঃ সান্ত্বয়ন্ নৃপঃ ।*  
> *মোচায়ামাস নিগড়াৎ স্ব-সুহৃদ্-ভাবম্ উদ্বহন্ ॥*  
> 
> **অনুবাদ:** এইরূপে মধুর সান্ত্বনাবাক্যে সেই দম্পতিকে প্রবোধ দিয়ে রাজা কংস সদ্ভাব ও আন্তরিক স্নেহের সহিত স্বয়ং তাঁদের হস্ত-পদের শৃঙ্খল উন্মোচন করে তাঁদের কারাগার থেকে মুক্ত করল।

কংস নিজ হস্তে বসুদেব ও দেবকীর ভারী লোহার শিকল খুলে দিল। তাঁদের সসম্মানে উত্থাপিত করে মথুরায় স্বাধীনভাবে বাস করার অধিকার প্রদান করল।

### বসুদেবের মহাত্মা-সুলভ ক্ষমা ও তত্ত্বজ্ঞান

ভগবানের অনন্য ভক্ত ও তত্ত্বজ্ঞানী বসুদেবের অন্তরে কংসের প্রতি কোনো ব্যক্তিগত ক্রোধ বা প্রতিহিংসার লেশমাত্র ছিল না। কংসের ক্রন্দন ও অনুশোচনা দেখে বসুদেব শান্ত ও পরম গম্ভীর স্বরে বললেন:

"হে রাজন! আপনি যা বলেছেন তা সত্য। এই জগতে জীবমাত্রই ভগবানের অচিন্ত্য মায়ার দ্বারা মোহিত। অহংকারে আচ্ছন্ন হয়ে অজ্ঞানী মানুষ মনে করে 'আমি কর্তা, আমি সংহারক', অথচ সকল প্রাণীই তাদের পূর্বকৃত কর্মফল এবং ঈশ্বরের ইচ্ছানুসারে পরিচালিত হয়। যিনি জানেন যে অবিনাশী আত্মা কখনো নিহত হয় না এবং জড়দেহ কেবল একটি পরিবর্তনশীল বস্ত্র মাত্র, তিনি কারো প্রতিই শত্রুতা বা ঘৃণা পোষণ করেন না।"

বসুদেবের এই পরম উদার বাক্য শ্রবণ করে কংস আশ্বস্ত হলো। সে পুনরায় তাঁদের চরণে প্রণাম করে নিজ রাজপ্রাসাদে ফিরে গেল।

কারামুক্ত বসুদেব ও দেবকী পরম শ্রদ্ধায় ভগবান শ্রীকৃষ্ণের আবির্ভাব ও তাঁর অচিন্ত্য লীলার মাহাত্ম্য কীর্তন করতে লাগলেন।""",
                "questions": [
                    {
                        "question": "কংসের হঠাৎ তীব্র অনুশোচনার প্রধান কারণ কি ছিল?",
                        "options": [
                            {"text": "তার সংহারকারী শত্রু জীবিত আছে এবং তার পূর্ববর্তী হত্যাসমূহ সম্পূর্ণ নিষ্ফল ছিল", "is_correct": True},
                            {"text": "রাজকোষ শূন্য হয়ে গিয়েছিল", "is_correct": False},
                            {"text": "শত্রু রাজা আক্রমণ করেছিল", "is_correct": False},
                            {"text": "প্রহরী বিদ্রোহ করেছিল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "কংস অনুতাপ করতে গিয়ে নিজেকে কার সাথে তুলনা করেছিল?",
                        "options": [
                            {"text": "নরখাদক নিষ্ঠুর রাক্ষসের সাথে", "is_correct": True},
                            {"text": "বুনো হাতির সাথে", "is_correct": False},
                            {"text": "বিষাক্ত বৃশ্চিকের সাথে", "is_correct": False},
                            {"text": "নেকড়ের সাথে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "কারাগারে গিয়ে কংস কি করেছিল?",
                        "options": [
                            {"text": "বসুদেব ও দেবকীর চরণে লুটিয়ে কেঁদে ক্ষমা প্রার্থনা করেছিল", "is_correct": True},
                            {"text": "তলোয়ার দিয়ে হুমকি দিয়েছিল", "is_correct": False},
                            {"text": "কৃষ্ণ কোথায় তা জানতে চেয়েছিল", "is_correct": False},
                            {"text": "পাহারাদারদের শাস্তি দিয়েছিল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "জীবের মিলন ও বিচ্ছেদের উপমা কংস কিসের সাথে দিয়েছিল?",
                        "options": [
                            {"text": "বাতাসে মেঘের মিলন ও বিচ্ছিন্ন হওয়ার সাথে", "is_correct": True},
                            {"text": "পাথরের সাথে", "is_correct": False},
                            {"text": "স্থায়ী বন্ধুত্বের সাথে", "is_correct": False},
                            {"text": "শুকনো নদীর সাথে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "বন্দীদের মুক্ত করতে কংস কি করেছিল?",
                        "options": [
                            {"text": "নিজ হস্তে চাবি দিয়ে তাদের লোহার শৃঙ্খল খুলে দিয়েছিল", "is_correct": True},
                            {"text": "প্রহরীদের ধাক্কা দিয়ে বের করতে বলেছিল", "is_correct": False},
                            {"text": "হাতুড়ি দিয়ে তালা ভেঙেছিল", "is_correct": False},
                            {"text": "অন্য দুর্গে পাঠিয়েছিল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "বসুদেব কংসের ক্ষমার আবেদনে কীভাবে সাড়া দিয়েছিলেন?",
                        "options": [
                            {"text": "মহাত্মা-সুলভ ক্ষমার সাথে কর্মফল ও আত্মতত্ত্ব ব্যাখ্যা করেছিলেন", "is_correct": True},
                            {"text": "লোহার শিকল দিয়ে কংসকে আঘাত করেছিলেন", "is_correct": False},
                            {"text": "কংসকে মৃত্যুর অভিশাপ দিয়েছিলেন", "is_correct": False},
                            {"text": "কংসের কাপুরুষতাকে উপহাস করেছিলেন", "is_correct": False}
                        ]
                    },
                    {
                        "question": "বসুদেবের মতে মানুষের মধ্যে 'আমি সংহারক' এই বিভ্রান্তি কোথা থেকে আসে?",
                        "options": [
                            {"text": "অহংকার ও ভগবানের মায়ার মোহে", "is_correct": True},
                            {"text": "অতিরিক্ত বেদচর্চা থেকে", "is_correct": False},
                            {"text": "সোমরস পান থেকে", "is_correct": False},
                            {"text": "শারীরিক দুর্বলতা থেকে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "এই প্রসঙ্গে শ্রীমদ্ভাগবত আত্মা সম্পর্কে কি শিক্ষা দেয়?",
                        "options": [
                            {"text": "আত্মা অবিনাশী ও শাশ্বত, কেবল দেহ পরিবর্তিত হয়", "is_correct": True},
                            {"text": "দেহের সাথে আত্মাও মরে যায়", "is_correct": False},
                            {"text": "আত্মা পাথরের তৈরি", "is_correct": False},
                            {"text": "কেবল রাজাদেরই আত্মা থাকে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "মুক্তির পর বসুদেব ও দেবকী কোথায় বাস করতে লাগলেন?",
                        "options": [
                            {"text": "মথুরাতেই স্বাধীন ও সম্মানজনকভাবে", "is_correct": True},
                            {"text": "নৈমিষারণ্যের বনে", "is_correct": False},
                            {"text": "স্বর্গলোকে", "is_correct": False},
                            {"text": "পাতাল গুহায়", "is_correct": False}
                        ]
                    },
                    {
                        "question": "কংসের অনুশোচনা ও বসুদেব-দেবকীর কারামুক্তি ভাগবতের কোন অধ্যায়ে বর্ণিত?",
                        "options": [
                            {"text": "অধ্যায় ৪", "is_correct": True},
                            {"text": "অধ্যায় ১", "is_correct": False},
                            {"text": "অধ্যায় ৯", "is_correct": False},
                            {"text": "অধ্যায় ১৪", "is_correct": False}
                        ]
                    }
                ]
            },
            "te": {
                "mainTopic": "కృష్ణ లీలలు",
                "subTopic": "కంసుని పశ్చాత్తాపం మరియు వసుదేవ-దేవకీల కారాగార విముక్తి",
                "content": """### కంసుని తీవ్ర దిగ్భ్రాంతి మరియు పశ్చాత్తాపం

ఆకాశంలో దుర్గాదేవి హెచ్చరిక చేసి అంతర్థానమైన తర్వాత, కంసుడు చెరసాల ప్రాంగణంలో శిలలా నిలిచిపోయాడు. అతని ఆసురీ గర్వమంతా ఒక్క క్షణంలో నేలమట్టమైంది.

ఆకాశవాణి పలికిన మాట సత్యమని అతడు గ్రహించాడు: తనను సంహరించే శత్రువు ఎక్కడో క్షేమంగా జన్మించాడు! అంతేకాక, తాను ఇప్పటివరకు చేసిన దారుణ హత్యలు—దేవకి యొక్క ఆరుగురు పసిబిడ్డలను నిర్దాక్షిణ్యంగా చంపడం—పూర్తిగా వ్యర్థమయ్యాయి! ఏ ప్రయోజనమూ లేకుండా కేవలం ఘోర పాపాలను మాత్రమే మూటగట్టుకున్నానని అతడు వణికిపోయాడు.

నరకయాతనల భయంతో, తీవ్ర పశ్చాత్తాపంతో కంసుడు వెంటనే వసుదేవ దేవకీలు ఉన్న చెరసాలలోకి పరుగుతీశాడు.

### కాళ్ళపై పడి రోదించిన కంసుడు

చెరసాలలోకి అడుగుపెట్టిన కంసుడు తన చెల్లెలు దేవకి, బావ వసుదేవుల పాదాలపై సాష్టాంగపడ్డాడు. లజ్జతో, పశ్చాత్తాపంతో అతని కళ్ళనుండి కన్నీరు ఏరులై పారి వారి పాదాలను తడిపింది.

కంఠం గద్గదమై అతడు విలపించాడు:

> **శ్రీమద్భాగవతం, స్కంధం 10, అధ్యాయం 4, శ్లోకం 19**
> 
> *అహో మయాచరితం పాపం రాక్షసైర్ ఇవ కర్కశైః |*  
> *బాలికా భగినీ-పుత్రా ఘాతితా బహవో మయా ||*  
> 
> **తాత్పర్యం:** "అయ్యో! నేను ఎంతటి ఘోర పాపాత్ముడను! రక్తపిపాసులైన రాక్షసులవలె నా తోడబుట్టిన చెల్లెలి పసిబిడ్డలను ఎంత నిర్దయగా సంహరించాను!"

కంసుడు ఇంకా ఇలా రోదించాడు: "నా కోసం ఎలాంటి భయంకర నరకం వేచి ఉందో నాకు తెలియదు! పసిపాపలను చంపినందుకు లోకం నన్ను ఛీత్కరిస్తుంది, యమదూతలు నన్ను చిత్రహింసలు పెడతారు. ధర్మాత్ముడవైన వసుదేవా! పతివ్రతవైన చెల్లెమ్మా దేవకీ! నన్ను క్షమించండి! జరిగిందంతా అనివార్యమైన విధివిలాసమే. గాలికి మేఘాలు కలవడం, విడిపోవడం లాగే, జీవులు తమ కర్మల ద్వారా కలవడం, విడిపోవడం జరుగుతుంది."

### సంకెళ్ళను స్వయంగా విప్పిన కంసుడు

ఆ క్షణంలో నిజమైన వినయాన్ని, సోదరప్రేమను ప్రదర్శిస్తూ కంసుడు తన వణుకుతున్న చేతులతో తాళాలు తీసుకున్నాడు:

> **శ్రీమద్భాగవతం, స్కంధం 10, అధ్యాయం 4, శ్లోకం 23**
> 
> *ఇతి తౌ దంపతీ శ్లక్ష్ణైః సామభిః సాంత్వయన్ నృపః |*  
> *మోచయామాస నిగడాత్ స్వ-సుహృద్-భావమ్ ఉద్వహన్ ||*  
> 
> **తాత్పర్యం:** ఈ విధంగా మధుర వచనాలతో ఆ దంపతులను అనునయిస్తూ, స్నేహభావంతో కంసరాజు స్వయంగా వారి చేతులకు, కాళ్ళకు ఉన్న ఇనుప సంకెళ్ళను విప్పి వారిని కారాగారం నుండి విముక్తులను చేశాడు.

వసుదేవ దేవకీల బరువైన గొలుసులను కంసుడే స్వయంగా తొలగించాడు. వారిని లేవనెత్తి గౌరవించి, మథురలో స్వేచ్ఛగా జీవించడానికి అనుమతించాడు.

### వసుదేవుని క్షమాగుణం మరియు తత్త్వబోధ

భగవంతుని పరమ భక్తుడు, ఆత్మజ్ఞాని అయిన వసుదేవునికి కంసునిపై ఎటువంటి వ్యక్తిగత పగ గానీ ద్వేషం గానీ లేదు. కంసుని పశ్చాత్తాపాన్ని చూసి వసుదేవుడు ప్రశాంతంగా ఇలా పలికాడు:

"రాజా! నీవు చెప్పినది నిజమే. ఈ లోకంలోని జీవులంతా భగవంతుని మాయకు లోబడి ఉన్నారు. అహంకారంతో మానవుడు 'నేనే చేస్తున్నాను, నేనే చంపుతున్నాను' అని భ్రమిస్తాడు; కానీ ప్రతిదీ వారి పూర్వకర్మల ప్రకారమే జరుగుతుంది. శాశ్వతమైన ఆత్మ ఎన్నడూ నశించదని, భౌతిక శరీరం కేవలం వస్త్రం వంటిదని గ్రహించిన జ్ఞానులు ఎవరిపైనా ద్వేషం చూపరు."

ఈ మాటలు విని కంసుడు సాంత్వన పొందాడు. వారికి ప్రణమిల్లి తన రాజభవనానికి వెళ్ళిపోయాడు.

కారాగారం నుండి విముక్తులైన వసుదేవ దేవకీలు భగవానుని అద్భుత లీలలను భక్తితో కీర్తించారు.""",
                "questions": [
                    {
                        "question": "కంసునికి హఠాత్తుగా తీవ్ర పశ్చాత్తాపం కలగడానికి కారణం ఏమిటి?",
                        "options": [
                            {"text": "తన శత్రువు బ్రతికే ఉన్నాడని, తన మునుపటి హత్యలు వ్యర్థమయ్యాయని గ్రహించినందున", "is_correct": True},
                            {"text": "ఖజానా ఖాళీ అయిందని", "is_correct": False},
                            {"text": "శత్రురాజు దండెత్తాడని", "is_correct": False},
                            {"text": "కాపలాదారులు తిరుగుబాటు చేశారని", "is_correct": False}
                        ]
                    },
                    {
                        "question": "కంసుడు తన క్రూరత్వాన్ని దేనితో పోల్చుకున్నాడు?",
                        "options": [
                            {"text": "రక్తపిపాసియైన రాక్షసునితో", "is_correct": True},
                            {"text": "ఏనుగుతో", "is_correct": False},
                            {"text": "తేలుతో", "is_correct": False},
                            {"text": "తోడేలుతో", "is_correct": False}
                        ]
                    },
                    {
                        "question": "చెరసాలలోకి వెళ్ళిన కంసుడు ఏమి చేశాడు?",
                        "options": [
                            {"text": "వసుదేవ దేవకీల పాదాలపై పడి కన్నీటితో క్షమాపణ కోరాడు", "is_correct": True},
                            {"text": "కత్తితో బెదిరించాడు", "is_correct": False},
                            {"text": "కృష్ణుడు ఎక్కడని అడిగాడు", "is_correct": False},
                            {"text": "కాపలాను పెంచాడు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "జీవులు కలవడం, విడిపోవడాన్ని కంసుడు దేనితో పోల్చాడు?",
                        "options": [
                            {"text": "గాలికి మేఘాలు కలవడం, విడిపోవడంతో", "is_correct": True},
                            {"text": "రాళ్ళతో", "is_correct": False},
                            {"text": "శాశ్వత స్నేహంతో", "is_correct": False},
                            {"text": "నదులతో", "is_correct": False}
                        ]
                    },
                    {
                        "question": "బందీలను విడుదల చేయడానికి కంసుడు ఏమి చేశాడు?",
                        "options": [
                            {"text": "తానే స్వయంగా తాళాలతో వారి సంకెళ్ళను విప్పాడు", "is_correct": True},
                            {"text": "సైనికులను నెట్టివేయమన్నాడు", "is_correct": False},
                            {"text": "సుత్తితో పగలగొట్టాడు", "is_correct": False},
                            {"text": "వేరే కోటకు మార్చాడు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "కంసుని క్షమాపణకు వసుదేవుడు ఎలా స్పందించాడు?",
                        "options": [
                            {"text": "ఎటువంటి ద్వేషం లేకుండా క్షమించి ఆత్మతత్త్వాన్ని బోధించాడు", "is_correct": True},
                            {"text": "గొలుసులతో కొట్టాడు", "is_correct": False},
                            {"text": "వెంటనే చావమని శపించాడు", "is_correct": False},
                            {"text": "పరిహసించాడు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "వసుదేవుని ప్రకారం 'నేనే చంపుతున్నాను' అనే భ్రమ దేనివల్ల కలుగుతుంది?",
                        "options": [
                            {"text": "అహంకారం మరియు భగవంతుని మాయ వల్ల", "is_correct": True},
                            {"text": "వేదాధ్యయనం వల్ల", "is_correct": False},
                            {"text": "సోమరసం వల్ల", "is_correct": False},
                            {"text": "బలహీనత వల్ల", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ఆత్మ గురించి ఈ సందర్భంలో భాగవతం ఏమి చెబుతోంది?",
                        "options": [
                            {"text": "ఆత్మ శాశ్వతమైనది, నశించదు; శరీరం మాత్రమే మారుతుంది", "is_correct": True},
                            {"text": "శరీరంతో పాటు ఆత్మ నశిస్తుంది", "is_correct": False},
                            {"text": "ఆత్మ రాతితో చేయబడింది", "is_correct": False},
                            {"text": "రాజులకే ఆత్మ ఉంటుంది", "is_correct": False}
                        ]
                    },
                    {
                        "question": "విముక్తి పొందిన తర్వాత వసుదేవ దేవకీలు ఎక్కడ నివసించారు?",
                        "options": [
                            {"text": "మథురలోనే స్వేచ్ఛగా, గౌరవంగా", "is_correct": True},
                            {"text": "నైమిశారణ్య అడవులలో", "is_correct": False},
                            {"text": "స్వర్గంలో", "is_correct": False},
                            {"text": "గుహలో", "is_correct": False}
                        ]
                    },
                    {
                        "question": "కంసుని పశ్చాత్తాపం మరియు విముక్తి భాగవతంలో ఏ అధ్యాయంలో ఉంది?",
                        "options": [
                            {"text": "అధ్యాయం 4", "is_correct": True},
                            {"text": "అధ్యాయం 1", "is_correct": False},
                            {"text": "అధ్యాయం 8", "is_correct": False},
                            {"text": "అధ్యాయం 12", "is_correct": False}
                        ]
                    }
                ]
            },
            "kn": {
                "mainTopic": "ಕೃಷ್ಣ ಲೀಲೆಗಳು",
                "subTopic": "ಕಂಸನ ಪಶ್ಚಾತ್ತಾಪ ಮತ್ತು ವಸುದೇವ-ದೇವಕಿಯರ ಕಾರಾಗೃಹ ಮುಕ್ತಿ",
                "content": """### ಕಂಸನ ತೀವ್ರ ಆಘಾತ ಮತ್ತು ಪಶ್ಚಾತ್ತಾಪ

ದುರ್ಗಾದೇವಿಯು ಆಕಾಶದಲ್ಲಿ ಗುಡುಗಿನಂತೆ ಎಚ್ಚರಿಸಿ ಅಂತರ್ಧಾನಳಾದ ನಂತರ, ಕಂಸನು ಸೆರೆಮನೆಯ ಅಂಗಳದಲ್ಲಿ ಕಲ್ಲಿನಂತೆ ನಿಂತುಹೋದನು. ಆತನ ಅಸುರೀ ಗರ್ವ ಮತ್ತು ದರ್ಪವೆಲ್ಲವೂ ಧೂಳೀಪಟವಾಯಿತು.

ಆಕಾಶವಾಣಿಯ ನುಡಿ ಸುಳ್ಳಲ್ಲ ಎಂದು ಆತನು ಭಯದಿಂದ ಅರಿತನು: ತನ್ನನ್ನು ಕೊಲ್ಲುವ ಶತ್ರುವು ಬೇರೆಲ್ಲಿಯೋ ಜೀವಂತವಾಗಿದ್ದಾನೆ! ಅಲ್ಲದೆ, ತಾನು ಈವರೆಗೆ ಮಾಡಿದ ಘೋರ ಪಾಪಗಳು—ದೇವಕಿಯ ಆರು ಮುಗ್ಧ ಮಕ್ಕಳನ್ನು ಕೊಂದ ದುಷ್ಕೃತ್ಯಗಳು—ಸಂಪೂರ್ಣ ವ್ಯರ್ಥವಾದವು! ಯಾವುದೇ ಪ್ರಯೋಜನವಿಲ್ಲದೆ ತಾನು ಕೇವಲ ಮಹಾಪಾಪದ ಹೊರೆಯನ್ನಷ್ಟೇ ಹೊತ್ತಿದ್ದೇನೆ ಎಂದು ಕಂಸನು ನಡುಗಿಹೋದನು.

ನರಕಯಾತನೆಯ ಭಯ ಮತ್ತು ತೀವ್ರ ಪಶ್ಚಾತ್ತಾಪದಿಂದ ಕಂಸನು ತಕ್ಷಣವೇ ವಸುದೇವ ಮತ್ತು ದೇವಕಿಯಿದ್ದ ಕತ್ತಲೆಯ ಕೋಣೆಗೆ ಓಡಿದನು.

### ಪಾದಗಳಿಗೆ ಬಿದ್ದು ಕಣ್ಣೀರಿಟ್ಟ ಕಂಸ

ಸೆರೆಮನೆಗೆ ನುಗ್ಗಿದ ಕಂಸನು ತನ್ನ ತಂಗಿ ದೇವಕಿ ಮತ್ತು ಭಾವ ವಸುದೇವರ ಪಾದಗಳಿಗೆ ಸಾಷ್ಟಾಂಗವಾಗಿ ಬಿದ್ದನು. ತೀವ್ರ ಲಜ್ಜೆ ಮತ್ತು ಪಶ್ಚಾತ್ತಾಪದಿಂದ ಆತನ ಕಣ್ಣುಗಳಿಂದ ಕಣ್ಣೀರು ಧಾರಾಕಾರವಾಗಿ ಹರಿದು ಅವರ ಪಾದಗಳನ್ನು ನೆನೆಸಿತು.

ಗದ್ಗದ ಕಂಠದಿಂದ ಕಂಸನು ಪ್ರಲಾಪಿಸಿದನು:

> **ಶ್ರೀಮದ್ಭಾಗವತ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 4, ಶ್ಲೋಕ 19**
> 
> *ಅಹೋ ಮಯಾಚರಿತಂ ಪಾಪಂ ರಾಕ್ಷಸೈರ್ ಇವ ಕರ್ಕಶೈಃ |*  
> *ಬಾಲಿಕಾ ಭಗಿನೀ-ಪುತ್ರಾ ಘಾತಿತಾ ಬಹವೋ ಮಯಾ ||*  
> 
> **ಭಾವಾರ್ಥ:** "ಅಯ್ಯೋ! ನಾನೆಂತಹ ಘೋರ ಪಾಪಿಯಾದೆ! ನರಭಕ್ಷಕ ಕ್ರೂರ ರಾಕ್ಷಸರಂತೆ ನಾನು ನನ್ನದೇ ಒಡಹುಟ್ಟಿದ ತಂಗಿಯ ಮುಗ್ಧ ಮಕ್ಕಳನ್ನು ನಿರ್ದಯವಾಗಿ ಕೊಂದುಹಾಕಿದೆ!"

ಕಂಸನು ಮುಂದುವರಿದು ಹೇಳಿದನು: "ನನಗಾಗಿ ಎಂತಹ ಭೀಕರ ನರಕ ಕಾದಿದೆಯೋ ನನಗೆ ತಿಳಿಯದು! ಮುಗ್ಧ ಮಕ್ಕಳನ್ನು ಕೊಂದಿದ್ದಕ್ಕಾಗಿ ಜಗತ್ತು ನನ್ನನ್ನು ಶಪಿಸುತ್ತದೆ, ಯಮದೂತರು ಶಿಕ್ಷಿಸುತ್ತಾರೆ. ಧರ್ಮಾತ್ಮ ವಸುದೇವನೇ! ಪತಿವ್ರತೆ ತಂಗಿ ದೇವಕೀ! ದಯವಿಟ್ಟು ಈ ಪಾಪಿಯನ್ನು ಕ್ಷಮಿಸಿ! ನಡೆದುದೆಲ್ಲವೂ ಅನಿವಾರ್ಯ ವಿಧಿಯಾಟ. ಗಾಳಿಗೆ ಮೋಡಗಳು ಕೂಡುವುದು ಮತ್ತು ಕರಗುವಂತೆ, ಜೀವಿಯು ಕರ್ಮಫಲದಿಂದ ಒಂದಾಗುವುದು ಮತ್ತು ಅಗಲುವುದು ನಡೆಯುತ್ತದೆ."

### ಸರಪಳಿಗಳನ್ನು ತಾನೇ ಬಿಡಿಸಿದ ಕಂಸ

ಆ ಕ್ಷಣದಲ್ಲಿ ನಿಜವಾದ ವಿನಯ ಮತ್ತು ಪ್ರೀತಿಯನ್ನು ತೋರುತ್ತಾ ಕಂಸನು ನಡುಗುವ ಕೈಗಳಿಂದ ಕೀಲಿಗಳನ್ನು ತೆಗೆದುಕೊಂಡನು:

> **ಶ್ರೀಮದ್ಭಾಗವತ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 4, ಶ್ಲೋಕ 23**
> 
> *ಇತಿ ತೌ ದಂಪತೀ ಶ್ಲಕ್ಷ್ಣೈಃ ಸಾಮಭಿಃ ಸಾಂತ್ವಯನ್ ನೃಪಃ |*  
> *ಮೋಚಯಾಮಾಸ ನಿಗಡಾತ್ ಸ್ವ-ಸುಹೃದ್-ಭಾವಮ್ ಉದ್ವಹನ್ ||*  
> 
> **ಭಾವಾರ್ಥ:** ಹೀಗೆ ಮಧುರ ವಚನಗಳಿಂದ ಆ ದಂಪತಿಗಳನ್ನು ಸಮಾಧಾನಪಡಿಸುತ್ತಾ, ರಾಜ ಕಂಸನು ನಿಜವಾದ ಪ್ರೀತಿ ಮತ್ತು ಸೌಹಾರ್ದತೆಯಿಂದ ಸ್ವತಃ ಅವರ ಕೈಕಾಲುಗಳ ಸರಪಳಿಗಳನ್ನು ಕಳಚಿ ಸೆರೆಮನೆಯಿಂದ ಮುಕ್ತಗೊಳಿಸಿದನು.

ವಸುದೇವ ಮತ್ತು ದೇವಕಿಯರ ಕಬ್ಬಿಣದ ಸರಪಳಿಗಳನ್ನು ಕಂಸನೇ ಸ್ವತಃ ತೆಗೆದನು. ಅವರನ್ನು ಗೌರವದಿಂದ ಎಬ್ಬಿಸಿ, ಮಥುರೆಯಲ್ಲಿಯೇ ಸ್ವತಂತ್ರವಾಗಿ ಗೌರವದಿಂದ ಬಾಳಲು ಅನುಮತಿ ನೀಡಿದನು.

### ವಸುದೇವರ ಮಹಾತ್ಮರ ಕ್ಷಮೆ ಮತ್ತು ತತ್ತ್ವಬೋಧೆ

ಭಗವಂತನ ಪರಮ ಭಕ್ತರಾದ ವಸುದೇವರಿಗೆ ಕಂಸನ ಮೇಲೆ ಯಾವುದೇ ವೈಯಕ್ತಿಕ ದ್ವೇಷವಿರಲಿಲ್ಲ. ಕಂಸನ ಪಶ್ಚಾತ್ತಾಪ ಮತ್ತು ಕಣ್ಣೀರನ್ನು ಕಂಡು ವಸುದೇವರು ಶಾಂತವಾಗಿ ಹೇಳಿದರು:

"ರಾಜನೇ! ನೀನು ಹೇಳಿದ್ದು ಸತ್ಯ. ಈ ಜಗತ್ತಿನಲ್ಲಿ ಜೀವಿಗಳೆಲ್ಲರೂ ಭಗವಂತನ ಮಾಯೆಗೆ ಒಳಗಾಗಿದ್ದಾರೆ. ಅಹಂಕಾರದಿಂದ ಮನುಷ್ಯನು 'ನಾನೇ ಕೊಲ್ಲುವವನು, ನಾನೇ ಮಾಡುವವನು' ಎಂದು ಭ್ರಮಿಸುತ್ತಾನೆ; ಆದರೆ ಪ್ರತಿಯೊಂದೂ ಪೂರ್ವಕರ್ಮ ಮತ್ತು ಈಶ್ವರನ ಇಚ್ಛೆಯಂತೆ ನಡೆಯುತ್ತದೆ. ಶಾಶ್ವತವಾದ ಆತ್ಮವು ಎಂದಿಗೂ ಸಾಯುವುದಿಲ್ಲ ಮತ್ತು ದೇಹವು ಕೇವಲ ಬದಲಾಗುವ ವಸ್ತ್ರ ಎಂದು ಅರಿತ ಜ್ಞಾನಿಗಳು ಯಾರ ಮೇಲೂ ದ್ವೇಷ ಸಾಧಿಸುವುದಿಲ್ಲ."

ಈ ಮಾತುಗಳಿಂದ ಕಂಸನು ಸಮಾಧಾನ ಹೊಂದಿದನು. ಅವರಿಗೆ ನಮಸ್ಕರಿಸಿ ತನ್ನ ಅರಮನೆಗೆ ಮರಳಿದನು.

ಸೆರೆಮನೆಯಿಂದ ಮುಕ್ತರಾದ ವಸುದೇವ ಮತ್ತು ದೇವಕಿಯರು ಭಗವಾನ್ ಶ್ರೀಕೃಷ್ಣನ ದಿವ್ಯ ಲೀಲೆಗಳನ್ನು ನೆನೆದು ಕೃತಜ್ಞತೆಯಿಂದ ಸ್ತುತಿಸಿದರು.""",
                "questions": [
                    {
                        "question": "ಕಂಸನಿಗೆ ಹಠಾತ್ ಪಶ್ಚಾತ್ತಾಪ ಮತ್ತು ಭಯ ಉಂಟಾಗಲು ಕಾರಣವೇನು?",
                        "options": [
                            {"text": "ತನ್ನ ಶತ್ರು ಜೀವಂತವಾಗಿದ್ದಾನೆ ಮತ್ತು ಹಿಂದಿನ ಹತ್ಯೆಗಳು ವ್ಯರ್ಥವಾದವು ಎಂದು ತಿಳಿದಿದ್ದರಿಂದ", "is_correct": True},
                            {"text": "ಖಜಾನೆ ಖಾಲಿಯಾಗಿದ್ದರಿಂದ", "is_correct": False},
                            {"text": "ಶತ್ರುರಾಜ ಯುದ್ಧ ಸಾರಿದ್ದರಿಂದ", "is_correct": False},
                            {"text": "ಕಾವಲುಗಾರರು ದಂಗೆಯೆದ್ದಿದ್ದರಿಂದ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಕಂಸನು ಪಶ್ಚಾತ್ತಾಪ ಪಡುತ್ತಾ ತನ್ನನ್ನು ಯಾವ ಕ್ರೂರ ಜೀವಿಗೆ ಹೋಲಿಸಿಕೊಂಡನು?",
                        "options": [
                            {"text": "ನರಭಕ್ಷಕ ಕ್ರೂರ ರಾಕ್ಷಸನಿಗೆ", "is_correct": True},
                            {"text": "ಕಾಡಾನೆಗೆ", "is_correct": False},
                            {"text": "ಚೇಳಿಗೆ", "is_correct": False},
                            {"text": "ತೋಳಕ್ಕೆ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಸೆರೆಮನೆಗೆ ಹೋದ ಕಂಸನು ಏನು ಮಾಡಿದನು?",
                        "options": [
                            {"text": "ವಸುದೇವ-ದೇವಕಿಯರ ಪಾದಗಳಿಗೆ ಬಿದ್ದು ಅತ್ತು ಕ್ಷಮೆಯಾಚಿಸಿದನು", "is_correct": True},
                            {"text": "ಕತ್ತಿಯಿಂದ ಬೆದರಿಸಿದನು", "is_correct": False},
                            {"text": "ಕೃಷ್ಣ ಎಲ್ಲಿದ್ದಾನೆ ಎಂದು ಕೇಳಿದನು", "is_correct": False},
                            {"text": "ಕಾವಲುಗಾರರನ್ನು ಶಿಕ್ಷಿಸಿದನು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಜೀವಿಗಳ ಕೂಡುವಿಕೆ ಮತ್ತು ಅಗಲಿಕೆಯನ್ನು ಕಂಸನು ಯಾವುದಕ್ಕೆ ಹೋಲಿಸಿದನು?",
                        "options": [
                            {"text": "ಗಾಳಿಗೆ ಮೋಡಗಳು ಕೂಡುವುದು ಮತ್ತು ಕರಗುವುದಕ್ಕೆ", "is_correct": True},
                            {"text": "ಕಲ್ಲುಗಳಿಗೆ", "is_correct": False},
                            {"text": "ಶಾಶ್ವತ ಸ್ನೇಹಕ್ಕೆ", "is_correct": False},
                            {"text": "ನದಿಗಳಿಗೆ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಬಂಧಿಗಳನ್ನು ಬಿಡುಗಡೆ ಮಾಡಲು ಕಂಸನು ಏನು ಮಾಡಿದನು?",
                        "options": [
                            {"text": "ಸ್ವತಃ ಕೈಯಿಂದ ಬೀಗ ತೆಗೆದು ಅವರ ಸರಪಳಿಗಳನ್ನು ಕಳಚಿದನು", "is_correct": True},
                            {"text": "ಕಾವಲುಗಾರರಿಂದ ಹೊರಹಾಕಿಸಿದನು", "is_correct": False},
                            {"text": "ಸುತ್ತಿಗೆಯಿಂದ ಬೀಗ ಒಡೆದನು", "is_correct": False},
                            {"text": "ಬೇರೆ ಕೋಟೆಗೆ ಕಳುಹಿಸಿದನು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಕಂಸನ ಕ್ಷಮೆಯಾಚನೆಗೆ ವಸುದೇವರು ಹೇಗೆ ಪ್ರತಿಕ್ರಿಯಿಸಿದರು?",
                        "options": [
                            {"text": "ಯಾವುದೇ ದ್ವೇಷವಿಲ್ಲದೆ ಕ್ಷಮಿಸಿ ಆತ್ಮತತ್ತ್ವವನ್ನು ಬೋಧಿಸಿದರು", "is_correct": True},
                            {"text": "ಸರಪಳಿಯಿಂದ ಕಂಸನಿಗೆ ಹೊಡೆದರು", "is_correct": False},
                            {"text": "ತಕ್ಷಣ ಸಾಯಲಿ ಎಂದು ಶಪಿಸಿದರು", "is_correct": False},
                            {"text": "ಕಂಸನನ್ನು ಗೇಲಿ ಮಾಡಿದರು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ವಸುದೇವರ ಪ್ರಕಾರ 'ನಾನೇ ಕೊಲ್ಲುವವನು' ಎಂಬ ಭ್ರಮೆ ಯಾವುದರಿಂದ ಉಂಟಾಗುತ್ತದೆ?",
                        "options": [
                            {"text": "ಅಹಂಕಾರ ಮತ್ತು ಭಗವಂತನ ಮಾಯೆಯ ಪ್ರಭಾವದಿಂದ", "is_correct": True},
                            {"text": "ಹೆಚ್ಚು ವೇದಾಧ್ಯಯನದಿಂದ", "is_correct": False},
                            {"text": "ಸೋಮರಸ ಕುಡಿಯುವುದರಿಂದ", "is_correct": False},
                            {"text": "ದೈಹಿಕ ದೌರ್ಬಲ್ಯದಿಂದ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಆತ್ಮದ ಬಗ್ಗೆ ಶ್ರೀಮದ್ಭಾಗವತವು ಇಲ್ಲಿ ಏನು ಬೋಧಿಸುತ್ತದೆ?",
                        "options": [
                            {"text": "ಆತ್ಮವು ಶಾಶ್ವತ ಮತ್ತು ನಾಶವಿಲ್ಲದ್ದು, ಕೇವಲ ದೇಹ ಬದಲಾಗುತ್ತದೆ", "is_correct": True},
                            {"text": "ದೇಹದ ಜೊತೆಗೆ ಆತ್ಮವೂ ಸಾಯುತ್ತದೆ", "is_correct": False},
                            {"text": "ಆತ್ಮವು ಕಲ್ಲಿನಿಂದ ಮಾಡಲ್ಪಟ್ಟಿದೆ", "is_correct": False},
                            {"text": "ಕೇವಲ ರಾಜರಿಗೆ ಮಾತ್ರ ಆತ್ಮವಿರುತ್ತದೆ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಬಿಡುಗಡೆಯ ನಂತರ ವಸುದೇವ ಮತ್ತು ದೇವಕಿಯರು ಎಲ್ಲಿ ನೆಲೆಸಿದರು?",
                        "options": [
                            {"text": "ಮಥುರೆಯಲ್ಲಿಯೇ ಸ್ವತಂತ್ರವಾಗಿ ಮತ್ತು ಗೌರವದಿಂದ", "is_correct": True},
                            {"text": "ನೈಮಿಷಾರಣ್ಯದ ಕಾಡಿನಲ್ಲಿ", "is_correct": False},
                            {"text": "ಸ್ವರ್ಗಲೋಕದಲ್ಲಿ", "is_correct": False},
                            {"text": "ಗುಹೆಯಲ್ಲಿ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಕಂಸನ ಪಶ್ಚಾತ್ತಾಪ ಮತ್ತು ವಸುದೇವ-ದೇವಕಿಯರ ಮುಕ್ತಿ ಭಾಗವತದ ಯಾವ ಅಧ್ಯಾಯದಲ್ಲಿದೆ?",
                        "options": [
                            {"text": "ಅಧ್ಯಾಯ 4", "is_correct": True},
                            {"text": "ಅಧ್ಯಾಯ 1", "is_correct": False},
                            {"text": "ಅಧ್ಯಾಯ 8", "is_correct": False},
                            {"text": "ಅಧ್ಯಾಯ 12", "is_correct": False}
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

        self.stdout.write(self.style.SUCCESS(f"Successfully populated Story 11 (ID: {story.id}) across all 7 languages!"))
