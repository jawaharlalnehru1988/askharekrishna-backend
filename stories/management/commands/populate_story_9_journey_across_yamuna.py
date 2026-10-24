import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askharekrishna_backend.settings')
django.setup()

from django.core.management.base import BaseCommand
from stories.models import StoryMainTopic, Story, StoryTranslation, StoryQuestion, StoryQuestionOption

class Command(BaseCommand):
    help = "Populate Story 9: The Midnight Journey Across the Yamuna to Gokula across 7 languages"

    def handle(self, *args, **options):
        topic = StoryMainTopic.objects.get(name="Krishna Pastimes")

        story_slug = "krishna-pastimes-the-midnight-journey-across-the-yamuna-to-gokula"
        image_path = "stories/images/vasudeva_crossing_yamuna.jpg"

        story, created = Story.objects.get_or_create(
            slug=story_slug,
            defaults={
                "topic": topic,
                "order": 8,
                "imagePath": image_path,
            }
        )
        if not created:
            story.topic = topic
            story.order = 8
            story.imagePath = image_path
            story.save()

        stories_data = {
            "en": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "The Midnight Journey Across the Yamuna to Gokula",
                "content": """### The Lord's Instruction and Transformation

Having comforted the hearts of Vasudeva and Devaki, the Supreme Personality of Godhead turned Himself into a sweet, two-armed human infant. At that very moment, the Lord instructed Vasudeva by divine inspiration: "Take Me immediately to the pastoral settlement of Gokula across the Yamuna river. Mother Yashoda, wife of Nanda Maharaja, has just given birth to a daughter. Place Me silently on her bed, take her newborn daughter, and bring her back to this prison cell before anyone awakens."

Vasudeva was filled with renewed courage, yet he wondered how he could carry out this miraculous task while shackled in iron fetters and locked behind multiple thick dungeon gates guarded by ferocious soldiers.

### The Power of Yogamāyā: Shackles Fall and Gates Open

Just then, by the supreme mystic potency of Yogamāyā, a miraculous transformation took place throughout the royal fortress of Mathura.

1. **A Deep Slumber Overcomes All:** All the ferocious prison guards, gatekeepers, watchdogs, and citizens of Mathura were overwhelmed by an irresistible, deep hypnotic sleep. No one could stir, speak, or open their eyes.
2. **Iron Shackles Disintegrate:** As Vasudeva prepared to lift his newborn child, the heavy iron shackles, chains, and manacles binding his hands and feet loosened instantly and fell away to the stone floor without a sound.
3. **Massive Iron Gates Swing Wide Open:** The fortress of Mathura was secured by heavy iron doors bolted with massive iron rods, chains, and padlocks. But as soon as Vasudeva approached holding baby Krishna, all the locks snapped open of their own accord, and the massive iron doors swung wide open automatically, exactly like darkness dispelled by the rising sun.

Placing the divine baby gently into a handwoven wicker basket cushioned with soft cloths, Vasudeva raised the basket onto his head and stepped out fearlessly into the pitch-black midnight.

### Torrential Rains and the Umbrella of Śeṣanāga

As Vasudeva walked through the desolate streets of Mathura toward the riverbank, a ferocious monsoon thunderstorm erupted. Heavy rain poured incessantly from the dark midnight clouds, lightning flashed across the sky, and thunder roared violently.

To protect the infant Supreme Lord from the driving rain, Lord Ananta Śeṣanāga—the cosmic serpent who expands as the Lord's celestial couch—appeared invisibly from the spiritual sky. Following behind Vasudeva, Śeṣanāga spread His radiant, jewel-adorned hoods like a wide umbrella over the basket, ensuring that not a single droplet of cold rain touched the tender lotus body of baby Krishna.

### The Raging Yamuna Parts Her Waters

When Vasudeva reached the bank of the Yamuna, he beheld a terrifying sight. Swollen by heavy monsoon downpours, the holy river was roaring with ferocious speed, foaming with rushing white waves and churning with hundreds of dangerous whirlpools. Human crossing seemed utterly impossible.

Yet, as soon as Vasudeva stepped boldly into the surging torrent carrying the Supreme Personality of Godhead upon his head, a sublime miracle unfolded:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 3, Verse 50**
> 
> *maghoni varṣaty asakṛd yam-ānujā*  
> *gabhīra-toyaugha-javormi-pheṇilā*  
> *bhayānakāvartta-śatākulā nadī*  
> *mārgaṁ dadau sindhur iva śriyaḥ pateḥ*  
> 
> **Translation:** While heavy rain poured incessantly from the sky, the Yamuna river, sister of Yamarāja, which was swollen with deep, rushing water, foaming with roaring waves, and filled with hundreds of terrifying whirlpools, gave way to Vasudeva, just as the Indian Ocean had formerly parted to provide a passage for Lord Śrī Rāmacandra to cross to Laṅkā.

Recognizing the lotus feet of her eternal Lord, the river Yamuna receded respectfully, lowering her waters to waist-height and dividing into two calm banks. Vasudeva walked smoothly across the riverbed as if traversing dry land, completely dry and safe under Śeṣanāga's protective hoods.

### The Divine Exchange in Gokula

Reaching the other shore, Vasudeva arrived at the peaceful pastoral settlement of Gokula. Guided by Yogamāyā, he entered the house of his dear friend Nanda Maharaja unnoticed. Inside the bedchamber, Mother Yashoda lay in deep, exhausted slumber after giving birth to her child, completely unaware whether her newborn had been a boy or a girl.

With silent reverence and tears in his eyes, Vasudeva gently placed baby Krishna beside the sleeping Mother Yashoda. Then, picking up Yashoda's newborn infant daughter—who was none other than the internal energy of the Lord, Yogamāyā—Vasudeva slipped out quietly into the night.

Crossing the parted Yamuna river once more, Vasudeva returned safely to Kamsa's dungeon in Mathura before the break of dawn. As soon as he entered the cell, the heavy iron doors slammed shut, the padlocks locked automatically, and the iron chains bound Vasudeva's wrists and ankles once again. Vasudeva placed the baby girl tenderly in Devaki's lap and waited for the cosmic drama to unfold.""",
                "questions": [
                    {
                        "question": "What form did the Supreme Lord assume after speaking with Vasudeva and Devaki?",
                        "options": [
                            {"text": "A sweet, two-armed human infant", "is_correct": True},
                            {"text": "A roaring half-man half-lion", "is_correct": False},
                            {"text": "A celestial youth holding a bow", "is_correct": False},
                            {"text": "An effulgent pillar of light", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Where did the Lord instruct Vasudeva to carry Him?",
                        "options": [
                            {"text": "To the house of Nanda Maharaja in Gokula across the Yamuna", "is_correct": True},
                            {"text": "To the kingdom of Hastinapura", "is_correct": False},
                            {"text": "To the peak of Mount Govardhana", "is_correct": False},
                            {"text": "To the deep forest of Dandakaranya", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What happened to the prison guards and citizens of Mathura when Vasudeva prepared to leave?",
                        "options": [
                            {"text": "They were overcome by an irresistible deep slumber by Yogamaya's potency", "is_correct": True},
                            {"text": "They ran away in fear of thunder", "is_correct": False},
                            {"text": "They revolted against King Kamsa", "is_correct": False},
                            {"text": "They turned to stone", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What happened to the heavy iron shackles and locked gates of the prison?",
                        "options": [
                            {"text": "The shackles loosened and fell off, and the massive gates swung open automatically", "is_correct": True},
                            {"text": "Vasudeva cut them with a hidden file", "is_correct": False},
                            {"text": "The guards gave Vasudeva the keys", "is_correct": False},
                            {"text": "They were smashed by an earthquake", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How did Vasudeva carry baby Krishna through the night?",
                        "options": [
                            {"text": "In a handwoven wicker basket balanced carefully on his head", "is_correct": True},
                            {"text": "In a golden royal chariot", "is_correct": False},
                            {"text": "On the back of a royal horse", "is_correct": False},
                            {"text": "Hidden inside a leather pouch", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Who protected baby Krishna from the torrential monsoon rain?",
                        "options": [
                            {"text": "Lord Ananta Sheshanaga spreading His radiant hoods like an umbrella", "is_correct": True},
                            {"text": "A silk parasol held by Devaki", "is_correct": False},
                            {"text": "A large banyan leaf", "is_correct": False},
                            {"text": "A magical raincoat", "is_correct": False}
                        ]
                    },
                    {
                        "question": "To what historic event does Srimad-Bhagavatam compare the parting of the Yamuna river?",
                        "options": [
                            {"text": "The Indian Ocean parting for Lord Ramachandra to cross to Lanka", "is_correct": True},
                            {"text": "The descent of the Ganges on Shiva's matted locks", "is_correct": False},
                            {"text": "The churning of the Milk Ocean by the demigods", "is_correct": False},
                            {"text": "The flooding of Ayodhya", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Why did Mother Yashoda not realize she had given birth to a daughter?",
                        "options": [
                            {"text": "She was overwhelmed by deep, exhausted sleep after labor due to Yogamaya", "is_correct": True},
                            {"text": "The room was too dark to see", "is_correct": False},
                            {"text": "She was away from her house", "is_correct": False},
                            {"text": "The child was taken immediately by midwives", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Who was the newborn daughter born to Mother Yashoda in reality?",
                        "options": [
                            {"text": "Yogamaya, the internal energy of the Supreme Lord", "is_correct": True},
                            {"text": "A demigoddess from Svargaloka", "is_correct": False},
                            {"text": "An ordinary cowherd girl", "is_correct": False},
                            {"text": "Putana in disguise", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What happened when Vasudeva returned to the Mathura prison cell with the baby girl?",
                        "options": [
                            {"text": "The gates closed, locks snapped shut, and iron chains bound him again automatically", "is_correct": True},
                            {"text": "The prison was completely destroyed", "is_correct": False},
                            {"text": "Kamsa was waiting with drawn sword", "is_correct": False},
                            {"text": "Devaki had escaped through the window", "is_correct": False}
                        ]
                    }
                ]
            },
            "ta": {
                "mainTopic": "கிருஷ்ண லீலைகள்",
                "subTopic": "நள்ளிரவில் யமுனையைக் கடந்து கோகுலம் சென்ற திவ்ய பயணம்",
                "content": """### பகவானின் கட்டளையும் ரூப மாற்றமும்

வசுதேவர் மற்றும் தேவகியின் உள்ளங்களுக்கு ஆறுதல் அளித்த பின்னர், முழுமுதற் கடவுளான பகவான் ஸ்ரீ கிருஷ்ணர் தம்மை இனிமையான இரண்டு கரங்கள் கொண்ட ஒரு பச்சிளம் குழந்தையாக மாற்றிக் கொண்டார். அந்த கணத்தில், பகவான் வசுதேவரின் உள்ளுணர்வில் திவ்ய கட்டளையை விடுத்தார்: "என்னை உடனே யமுனை நதியைக் கடந்து ஆயர்பாடியான கோகுலத்திற்கு எடுத்துச் செல்வீராக. நந்த மகாராஜாவின் மனைவியான யசோதை இப்போதுதான் ஒரு பெண் குழந்தையைப் பெற்றெடுத்துள்ளாள். அவளது படுக்கையில் என்னை வைத்துவிட்டு, அந்த பச்சிளம் பெண் குழந்தையை எடுத்துக்கொண்டு, எவரும் விழித்தெழுவதற்கு முன் இந்த சிறைச்சாலைக்குத் திரும்பி வாருங்கள்."

வசுதேவர் அளவில்லா ஆன்மீக தைரியம் பெற்றார். எனினும், கடுமையான இரும்பு விலங்குகளால் பிணைக்கப்பட்டு, கொடூரமான ஆயுதம் தாங்கிய காவலர்களால் சூழப்பட்ட பல அடுக்கு இரும்பு வாயில்களைக் கொண்ட இந்த சிறையிலிருந்து எவ்வாறு வெளியேறுவது என்று அவர் யோசித்தார்.

### யோகமாயையின் அற்புதம்: விலங்குகள் உடைந்தன, கதவுகள் திறந்தன

அந்த கணமே, பகவானின் யோகமாயா சக்தியினால் மதுரா நகரெங்கும் வியக்கத்தக்க அற்புதங்கள் நிகழ்ந்தன:

1. **அனைவரையும் ஆட்கொண்ட ஆழ்ந்த நித்திரை:** சிறைக் காவலர்கள், வாயிற்காப்பாளர்கள், காவல் நாய்கள் மற்றும் மதுரா நகர மக்கள் அனைவரும் யோகமாயையின் சக்தியினால் தவிர்க்க முடியாத ஆழ்ந்த மாய நித்திரையில் ஆழ்ந்தனர். ஒருவராலும் அசையவோ, கண்களைத் திறக்கவோ இயலவில்லை.
2. **இரும்பு விலங்குகள் தாமாகவே கழன்றன:** புதிதாக அவதரித்த திவ்ய குழந்தையை வசுதேவர் கைகளில் ஏந்திய உடனே, அவரது கைகளையும் கால்களையும் பிணைத்திருந்த கனத்த இரும்பு சங்கிலிகளும் பூட்டுகளும் எவ்வித சத்தமுமின்றி கழன்று தரையில் விழுந்தன.
3. **கனத்த இரும்பு கதவுகள் தாமாகவே திறந்தன:** மதுராவின் சிறைச்சாலை கனத்த மரக்கதவுகளாலும், இரும்புத் தண்டுகளாலும், பூட்டுகளாலும் பலமாக பூட்டப்பட்டிருந்தது. ஆனால், குழந்தை கிருஷ்ணரை ஏந்தியபடி வசுதேவர் நெருங்கியதும், அனைத்து பூட்டுகளும் தாமாகவே திறந்துகொண்டன; சூரியன் உதித்ததும் இருள் விலகுவது போல கனத்த இரும்பு கதவுகள் தாமாகவே அகலத் திறந்தன.

மெல்லிய ஆடைகளால் மெத்தென அமைக்கப்பட்ட பிரம்புப் கூடைக்குள் திவ்ய குழந்தையை மென்மையாக வைத்த வசுதேவர், அந்தக் கூடையைத் தமது தலையில் சுமந்து கொண்டு, நள்ளிரவின் காரிருளில் அஞ்சாமல் சிறையை விட்டு வெளியேறினார்.

### கொட்டும் மழையும் ஆதிசேஷனின் குடையும்

மதுராவின் வெறிச்சோடிய வீதிகள் வழியே யமுனைக் கரையை நோக்கி வசுதேவர் நடந்து சென்றபோது, வானில் பலத்த பெருமழை கொட்டத் தொடங்கியது. இருண்ட நள்ளிரவு மேகங்களிலிருந்து பெருமழை விடாமல் பொழிந்தது; மின்னல் வெட்டியது, இடி பயங்கரமாக முழங்கியது.

பச்சிளம் குழந்தையான பகவான் ஸ்ரீ கிருஷ்ணரை மழையிலிருந்து காப்பதற்காக, பகவானின் நித்திய சேவகரான பகவான் அனந்த ஆதிசேஷன் ஆன்மீக உலகிலிருந்து அரூபமாகத் தோன்றினார். வசுதேவரின் பின்னால் தொடர்ந்து வந்த ஆதிசேஷன், ரத்தினங்கள் மின்னும் தமது ஆயிரக்கணக்கான திருமுடிகளை ஒரு பெரிய குடையைப் போல விரித்து, பச்சிளம் குழந்தை கிருஷ்ணரின் தாமரைத் திருமேனியில் ஒரு துளி குளிர்ந்த மழைநீரும் படாதவாறு பாதுகாத்தார்.

### வழிவிட்ட கொந்தளித்த யமுனை நதி

வசுதேவர் யமுனைக் கரையை அடைந்தபோது, அங்கே ஒரு பயங்கரமான காட்சியைக் கண்டார். பெருமழையினால் பெருக்கெடுத்து ஓடிய புனித யமுனை நதி, நுரை ததும்பும் ஆக்ரோஷமான அலைகளுடனும், நூற்றுக்கணக்கான சுழல்களுடனும் பயங்கரமாக கர்ஜித்துக் கொண்டிருந்தது. மனித சக்தியால் அந்த நதியைக் கடப்பது சாத்தியமற்றதாகத் தோன்றியது.

ஆயினும், முழுமுதற் கடவுளான பகவானைத் தலையில் சுமந்தபடி வசுதேவர் யமுனை வெள்ளத்தில் தைரியமாக இறங்கிய உடனே, ஓர் உன்னத அற்புதம் நிகழ்ந்தது:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 3, சுலோகம் 50**
> 
> *மகோனி வர்ஷத்யஸக்ருத் யமானுஜா*  
> *கபீர-தோயௌக-ஜவோர்மி-பேனிலா |*  
> *பயானகாவர்த்த-ஶதாகுலா நதீ*  
> *மார்கம் ததௌ ஸிந்துரிவ ஶ்ரிய: பதே: ||*  
> 
> **பொருள்:** மேகங்கள் ஓயாமல் பெருமழையைப் பொழிந்து கொண்டிருந்த வேளையில், யமராஜரின் சகோதரியான யமுனை நதி, ஆழமான நீரினாலும், சுழல்களினாலும், நுரைத்தெழும் ஆக்ரோஷ அலைகளினாலும் கொந்தளித்த போதிலும், முன்னொரு காலத்தில் பகவான் ஸ்ரீ ராமச்சந்திரருக்கு இலங்கை செல்ல சமுத்திர ராஜன் வழிவிட்டது போல, வசுதேவருக்கு பணிவோடு வழிவிட்டது.

தமது நித்திய எஜமானரின் தாமரைத் திருவடிகளை அடையாளம் கண்டுகொண்ட யமுனை நதி, வெள்ளத்தைக் குறைத்துக் கொண்டு வசுதேவருக்கு இடுப்பளவு நீராக அமைதியடைந்தது. நிலத்தில் நடப்பது போல வசுதேவர் நதியைக் கடந்து அக்கரை சென்றார்.

### கோகுலத்தில் நிகழ்ந்த திவ்ய பரிமாற்றம்

அக்கரை சேர்ந்த வசுதேவர், அமைதியான ஆயர்பாடியான கோகுலத்தை அடைந்தார். யோகமாயையின் வழிகாட்டுதலால், எவரும் அறியாவண்ணம் தமது அன்பு நண்பரான நந்த மகாராஜாவின் மாளிகைக்குள் நுழைந்தார். அங்கே அன்னை யசோதை பிரசவக் களைப்பினால் ஆழ்ந்த நித்திரையில் படுத்திருந்தாள்; தமக்குத் தோன்றிய குழந்தை ஆண் குழந்தையா அல்லது பெண் குழந்தையா என்பதைக் கூட அவள் அறியாத நிலையில் இருந்தாள்.

கண்களில் பக்திப் பெருக்குடன் வசுதேவர், குழந்தை கிருஷ்ணரை தூங்கிக்கொண்டிருந்த யசோதையின் அருகில் மென்மையாக கிடத்தினார். பின்னர், யசோதைக்குப் பிறந்திருந்த பெண் குழந்தையை—பகவானின் அந்தரங்க சக்தியான யோகமாயையை—மென்மையாகத் தமது கைகளில் ஏந்திக்கொண்டு, அமைதியாக அங்கிருந்து புறப்பட்டார்.

மீண்டும் வழிவிட்ட யமுனையைக் கடந்து, விடிவதற்கு முன்பே மதுராவின் சிறைச்சாலைக்கு வசுதேவர் பாதுகாப்பாகத் திரும்பினார். அவர் உள்ளே நுழைந்த உடனே, கனத்த கதவுகள் தாமாகவே மூடிக்கொண்டன; பூட்டுகள் தானாகப் பூட்டிக்கொண்டன; இரும்புச் சங்கிலிகள் மீண்டும் வசுதேவரின் கைகால்களைப் பிணைத்தன. வசுதேவர் அந்த பெண் குழந்தையை தாய் தேவகியின் மடியில் கிடத்திவிட்டு, அடுத்த லீலைக்காக அமைதியோடு காத்திருந்தார்.""",
                "questions": [
                    {
                        "question": "வசுதேவர் மற்றும் தேவகியிடம் பேசிய பின்னர் பகவான் எந்த ரூபத்தை ஏற்றார்?",
                        "options": [
                            {"text": "இனிமையான இரண்டு கரங்கள் கொண்ட பச்சிளம் குழந்தை ரூபம்", "is_correct": True},
                            {"text": "நரசிம்ம ரூபம்", "is_correct": False},
                            {"text": "வில்லேந்திய இளைஞன் ரூபம்", "is_correct": False},
                            {"text": "ஜோதிப் பிழம்பு", "is_correct": False}
                        ]
                    },
                    {
                        "question": "குழந்தையைக் கொண்டு செல்லும்படி பகவான் வசுதேவருக்கு எங்கு வழிகாட்டினார்?",
                        "options": [
                            {"text": "யமுனைக்கு அப்பால் உள்ள கோகுலத்தில் நந்த மகாராஜாவின் இல்லத்திற்கு", "is_correct": True},
                            {"text": "ஹஸ்தினாபுரத்திற்கு", "is_correct": False},
                            {"text": "கோவர்த்தன மலை உச்சிக்கு", "is_correct": False},
                            {"text": "தண்டகாரண்ய காட்டுக்கு", "is_correct": False}
                        ]
                    },
                    {
                        "question": "வசுதேவர் புறப்பட்டபோது சிறைக் காவலர்களுக்கும் மதுரா மக்களுக்கும் என்ன நேர்ந்தது?",
                        "options": [
                            {"text": "யோகமாயையின் சக்தியினால் அனைவரும் ஆழ்ந்த மாய நித்திரையில் ஆழ்ந்தனர்", "is_correct": True},
                            {"text": "இடிக்கு பயந்து ஓடினர்", "is_correct": False},
                            {"text": "கம்சனுக்கு எதிராகப் போரிட்டனர்", "is_correct": False},
                            {"text": "கல்லாக மாறினர்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "சிறைச்சாலையின் இரும்பு விலங்குகளுக்கும் கதவுகளுக்கும் என்ன அற்புதம் நிகழ்ந்தது?",
                        "options": [
                            {"text": "விலங்குகள் தாமாகவே கழன்று விழுந்தன, கதவுகள் தானாக அகலத் திறந்தன", "is_correct": True},
                            {"text": "வசுதேவர் ரகசியமாக அறுத்தெறிந்தார்", "is_correct": False},
                            {"text": "காவலர்கள் சாவி கொடுத்தனர்", "is_correct": False},
                            {"text": "பூகம்பத்தால் உடைந்தன", "is_correct": False}
                        ]
                    },
                    {
                        "question": "வசுதேவர் குழந்தை கிருஷ்ணரை எவ்வாறு சுமந்து சென்றார்?",
                        "options": [
                            {"text": "பிரம்புப் கூடையில் கிடத்தி தலையில் சுமந்து சென்றார்", "is_correct": True},
                            {"text": "தங்க ரதத்தில் வைத்து", "is_correct": False},
                            {"text": "குதிரையின் மீது வைத்து", "is_correct": False},
                            {"text": "தோல் பையில் மறைத்து", "is_correct": False}
                        ]
                    },
                    {
                        "question": "கொட்டும் பெருமழையிலிருந்து குழந்தை கிருஷ்ணரை யார் பாதுகாத்தது?",
                        "options": [
                            {"text": "பகவான் அனந்த ஆதிசேஷன் தமது திருமுடிகளை குடையாக விரித்து", "is_correct": True},
                            {"text": "பட்டுக்குடை", "is_correct": False},
                            {"text": "ஆலமர இலை", "is_correct": False},
                            {"text": "மழை அங்கி", "is_correct": False}
                        ]
                    },
                    {
                        "question": "யமுனை நதி வழிவிட்டதை ஸ்ரீமத் பாகவதம் எந்த வரலாற்று நிகழ்வோடு ஒப்பிடுகிறது?",
                        "options": [
                            {"text": "பகவான் ஸ்ரீ ராமச்சந்திரருக்கு இலங்கை செல்ல சமுத்திர ராஜன் வழிவிட்டது போல", "is_correct": True},
                            {"text": "சிவபெருமானின் ஜடையில் கங்கை இறங்கியது போல", "is_correct": False},
                            {"text": "பாற்கடலைக் கடைந்தது போல", "is_correct": False},
                            {"text": "அயோத்தி வெள்ளம் போல", "is_correct": False}
                        ]
                    },
                    {
                        "question": "அன்னை யசோதை தமக்கு பெண் குழந்தை பிறந்ததை ஏன் அறியவில்லை?",
                        "options": [
                            {"text": "பிரசவக் களைப்பினால் யோகமாயையின் ஆழ்ந்த நித்திரையில் இருந்தாள்", "is_correct": True},
                            {"text": "அறை மிகவும் இருட்டாக இருந்தது", "is_correct": False},
                            {"text": "அவள் வீட்டில் இல்லை", "is_correct": False},
                            {"text": "மருத்துவர்கள் குழந்தையை உடனே எடுத்துச் சென்றனர்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "அன்னை யசோதைக்குப் பிறந்த அந்த பெண் குழந்தை உண்மையில் யார்?",
                        "options": [
                            {"text": "பகவானின் அந்தரங்க சக்தியான யோகமாயா", "is_correct": True},
                            {"text": "தேவலோக தேவதை", "is_correct": False},
                            {"text": "சாதாரண ஆயர்பாடி பெண்", "is_correct": False},
                            {"text": "மாறுவேடமிட்ட பூதனை", "is_correct": False}
                        ]
                    },
                    {
                        "question": "வசுதேவர் பெண் குழந்தையோடு சிறைக்குத் திரும்பியவுடன் என்ன நிகழ்ந்தது?",
                        "options": [
                            {"text": "கதவுகள் மூடிக்கொண்டன, விலங்குகள் தானாக மீண்டும் பிணைத்துக் கொண்டன", "is_correct": True},
                            {"text": "சிறைச்சாலை இடிந்து விழுந்தது", "is_correct": False},
                            {"text": "கம்சன் வாளோடு காத்திருந்தான்", "is_correct": False},
                            {"text": "தேவகி தப்பியோடிவிட்டாள்", "is_correct": False}
                        ]
                    }
                ]
            },
            "hi": {
                "mainTopic": "कृष्ण लीलाएं",
                "subTopic": "मध्यरात्रि में यमुना पार कर गोकुल की दिव्य यात्रा",
                "content": """### भगवान का निर्देश और शिशु रूप धारण करना

वसुदेव और देवकी के हृदयों को सांत्वना देने के उपरांत, पूर्ण पुरुषोत्तम भगवान श्री कृष्ण ने अपने ऐश्वर्यमय चतुर्भुज रूप को समेटकर एक अत्यंत मनमोहक, द्विभुज शिशु का रूप धारण कर लिया। उसी क्षण, भगवान ने वसुदेव जी को अंतःप्रेरणा द्वारा निर्देश दिया: "मुझे अविलंब यमुना पार गोकुल में नंद महाराज के घर ले जाएं। नंदबाबा की पत्नी यशोदा ने अभी-अभी एक कन्या को जन्म दिया है। मुझे चुपचाप यशोदा के पलंग पर लिटा दें और उनकी नवजात कन्या को लेकर किसी के जागने से पूर्व इस कारागार में लौट आएं।"

वसुदेव जी का हृदय असीम साहस से भर गया, परंतु वे सोचने लगे कि पैरों में बंधी लोहे की बेड़ियों और भारी पहरे में वे कारागार से बाहर कैसे निकल सकेंगे।

### योगमाया का प्रभाव: बेड़ियां टूटीं और कपाट खुल गए

तभी भगवान की अचिंत्य शक्ति 'योगमाया' के प्रभाव से संपूर्ण मथुरा नगरी में अद्भुत चमत्कार हुए:

1. **सब पर गहरी निद्रा छा गई:** कारागार के समस्त क्रूर पहरेदार, द्वारपाल, कुत्ते और मथुरा के नागरिक योगमाया के प्रभाव से गहरी, अचेत निद्रा में सो गए। कोई भी अपनी आंखें खोलने में समर्थ न रहा।
2. **लोहे की बेड़ियां स्वतः खुल गईं:** जैसे ही वसुदेव जी ने नवजात शिशु को अपनी गोद में उठाया, उनके हाथों और पैरों में बंधी भारी लोहे की बेड़ियां और जंजीरें बिना किसी ध्वनि के स्वतः खुल गईं।
3. **विशाल कपाट स्वतः खुल गए:** मथुरा के राजमहल और कारागार के भारी लोहे के दरवाजे मजबूत तालों और लोहे की छड़ों से बंद थे। परंतु जैसे ही वसुदेव जी बालक कृष्ण को लेकर आगे बढ़े, सारे ताले स्वतः टूट गए और भारी कपाट अपने आप ऐसे खुल गए जैसे सूर्य के उदय होने पर अंधकार छंट जाता है।

वसुदेव जी ने एक सुंदर सूप (बांस की टोकरी) में कोमल वस्त्र बिछाकर दिव्य बालक को उसमें लिटाया और उस टोकरी को अपने सिर पर रखकर निडर होकर मध्यरात्रि के अंधकार में चल पड़े।

### घनघोर वर्षा और शेषनाग का छत्र

जब वसुदेव जी मथुरा की निर्जन गलियों से होते हुए यमुना तट की ओर बढ़ रहे थे, तभी आकाश में मूसलाधार वर्षा होने लगी। काले-कजरारे बादलों से जल की धाराएं बरसने लगीं, बिजली चमकने लगी और मेघ गर्जना करने लगे।

अपने परम प्रभु बालक कृष्ण को वर्षा की बूंदों से बचाने के लिए, भगवान के नित्य सेवक शेषनाग अदृश्य रूप से प्रकट हो गए। वसुदेव जी के पीछे-पीछे चलते हुए, शेषनाग ने अपने अनेक मणियों से जगमगाते फनों को एक विशाल छत्र की भांति फैला दिया, जिससे ठंडे पानी की एक भी बूंद बालक कृष्ण के सुकोमल अंगों पर न पड़ी।

### उफनती यमुना ने दिया मार्ग

जब वसुदेव जी यमुना तट पर पहुंचे, तो उन्होंने देखा कि वर्षा ऋतु के कारण यमुना जी अत्यंत भयानक रूप धारण किए हुए थीं। गहरा जल, तीव्र गति से बहती सफेद फेनिल तरंगें और सैकड़ों भयावह भंवरें यमुना के प्रवाह को अत्यंत विकराल बना रही थीं। साधारण मनुष्य के लिए उसे पार करना असंभव था।

परंतु जैसे ही वसुदेव जी पूर्ण पुरुषोत्तम भगवान को सिर पर धारण किए यमुना के अथाह जल में उतरे, एक परम पावन चमत्कार घटित हुआ:

> **श्रीमद्भागवतम्, स्कंध 10, अध्याय 3, श्लोक 50**
> 
> *मघोनि वर्षत्यसकृद् यमानुजा*  
> *गभीरतोयौघजवोर्मिफेणिला ।*  
> *भयानकावर्त्तशताकुला नदी*  
> *मार्गं ददौ सिंधुरिव श्रियः पतेः ॥*  
> 
> **भावार्थ:** जिस समय मूसलाधार वर्षा हो रही थी, उस समय यमराज की बहन यमुना जी, जो गहरे जलप्रवाह, तीव्र तरंगों, फेन और सैकड़ों भयानक भंवरों से भरी हुई थीं, उन्होंने वसुदेव जी को उसी प्रकार मार्ग दे दिया, जैसे पूर्वकाल में लंका जाने के लिए समुद्र ने भगवान श्री रामचंद्र जी को मार्ग दिया था।

अपने नित्य स्वामी के चरणकमलों को स्पर्श करने की अभिलाषा से यमुना जी आगे बढ़ीं और भगवान का स्पर्श पाते ही शांत हो गईं। यमुना का जल घटकर कमर तक रह गया और बीच में सूखा मार्ग बन गया। वसुदेव जी सरलता से यमुना पार कर गए।

### गोकुल में दिव्य अदला-बदली

यमुना पार कर वसुदेव जी गोकुल पहुंचे। योगमाया की कृपा से वे बिना किसी के देखे नंद महाराज के भवन में प्रविष्ट हुए। वहां यशोदा मैया प्रसव की थकान के कारण अचेत होकर सो रही थीं; उन्हें यह भी ज्ञात न था कि उन्हें पुत्र हुआ है या पुत्री।

वसुदेव जी ने अत्यंत सावधानी और अश्रुपूरित नेत्रों से बालक कृष्ण को यशोदा के पास सुला दिया। फिर यशोदा की नवजात कन्या को—जो साक्षात् योगमाया थीं—अपनी गोद में लेकर चुपचाप वहां से चल पड़े।

पुनः यमुना पार कर वे भोर होने से पहले मथुरा के कारागार में लौट आए। उनके प्रवेश करते ही कारागार के कपाट स्वतः बंद हो गए, ताले लग गए और लोहे की बेड़ियां पूर्ववत उनके हाथ-पैरों में बंध गईं। वसुदेव जी ने उस कन्या को देवकी की गोद में रख दिया और आगामी लीला की प्रतीक्षा करने लगे।""",
                "questions": [
                    {
                        "question": "माता-पिता से बात करने के बाद भगवान ने कौन सा रूप धारण किया?",
                        "options": [
                            {"text": "अत्यंत मनमोहक दो भुजाओं वाले शिशु का रूप", "is_correct": True},
                            {"text": "नृसिंह रूप", "is_correct": False},
                            {"text": "धनुर्धारी योद्धा रूप", "is_correct": False},
                            {"text": "अग्नि स्तंभ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "भगवान ने वसुदेव जी को बालक को कहां ले जाने का निर्देश दिया?",
                        "options": [
                            {"text": "यमुना पार गोकुल में नंद महाराज के घर", "is_correct": True},
                            {"text": "हस्तिनापुर", "is_correct": False},
                            {"text": "गोवर्धन पर्वत", "is_correct": False},
                            {"text": "दंडकारण्य वन", "is_correct": False}
                        ]
                    },
                    {
                        "question": "वसुदेव जी के चलते समय पहरेदारों और मथुरावासियों का क्या हुआ?",
                        "options": [
                            {"text": "योगमाया के प्रभाव से सब गहरी निद्रा में सो गए", "is_correct": True},
                            {"text": "वे वर्षा से डरकर भाग गए", "is_correct": False},
                            {"text": "उन्होंने कंस के विरुद्ध विद्रोह कर दिया", "is_correct": False},
                            {"text": "वे पत्थर बन गए", "is_correct": False}
                        ]
                    },
                    {
                        "question": "कारागार की बेड़ियों और दरवाजों में क्या चमत्कार हुआ?",
                        "options": [
                            {"text": "बेड़ियां स्वतः खुल गईं और भारी कपाट अपने आप खुल गए", "is_correct": True},
                            {"text": "वसुदेव जी ने रेती से काटा", "is_correct": False},
                            {"text": "पहरेदारों ने चाबियां दीं", "is_correct": False},
                            {"text": "भूकंप से दरवाजे टूट गए", "is_correct": False}
                        ]
                    },
                    {
                        "question": "वसुदेव जी ने बालक कृष्ण को किस प्रकार उठाया?",
                        "options": [
                            {"text": "बांस की टोकरी (सूप) में रखकर सिर पर", "is_correct": True},
                            {"text": "स्वर्ण रथ पर", "is_correct": False},
                            {"text": "घोड़े की पीठ पर", "is_correct": False},
                            {"text": "चमड़े की थैली में", "is_correct": False}
                        ]
                    },
                    {
                        "question": "मूसलाधार वर्षा में बालक कृष्ण की रक्षा किसने की?",
                        "options": [
                            {"text": "शेषनाग ने अपने फनों का छत्र बनाकर", "is_correct": True},
                            {"text": "रेशमी छाते ने", "is_correct": False},
                            {"text": "बरगद के पत्ते ने", "is_correct": False},
                            {"text": "देवकी के आंचल ने", "is_correct": False}
                        ]
                    },
                    {
                        "question": "यमुना के मार्ग देने की तुलना श्रीमद्भागवतम् में किस ऐतिहासिक घटना से की गई है?",
                        "options": [
                            {"text": "लंका जाने के लिए समुद्र द्वारा भगवान श्री राम को मार्ग देने से", "is_correct": True},
                            {"text": "शिव जी की जटाओं से गंगा उतरने से", "is_correct": False},
                            {"text": "समुद्र मंथन से", "is_correct": False},
                            {"text": "अयोध्या की बाढ़ से", "is_correct": False}
                        ]
                    },
                    {
                        "question": "यशोदा मैया को यह क्यों नहीं पता चला कि उन्हें कन्या हुई है?",
                        "options": [
                            {"text": "प्रसव की थकान और योगमाया के प्रभाव से वे गहरी निद्रा में थीं", "is_correct": True},
                            {"text": "कमरे में बहुत अंधेरा था", "is_correct": False},
                            {"text": "वे घर पर नहीं थीं", "is_correct": False},
                            {"text": "दाई ने तुरंत बच्चे को छिपा दिया था", "is_correct": False}
                        ]
                    },
                    {
                        "question": "यशोदा के गर्भ से जन्मी कन्या वास्तव में कौन थीं?",
                        "options": [
                            {"text": "भगवान की अंतरंग शक्ति योगमाया", "is_correct": True},
                            {"text": "स्वर्ग की अप्सरा", "is_correct": False},
                            {"text": "साधारण ग्वालिन", "is_correct": False},
                            {"text": "पूतना", "is_correct": False}
                        ]
                    },
                    {
                        "question": "वसुदेव जी के कन्या को लेकर कारागार लौटने पर क्या हुआ?",
                        "options": [
                            {"text": "दरवाजे स्वतः बंद हो गए और बेड़ियां पुनः बंध गईं", "is_correct": True},
                            {"text": "कारागार ढह गया", "is_correct": False},
                            {"text": "कंस तलवार लिए खड़ा था", "is_correct": False},
                            {"text": "देवकी भाग चुकी थी", "is_correct": False}
                        ]
                    }
                ]
            },
            "ml": {
                "mainTopic": "കൃഷ്ണ ലീലകൾ",
                "subTopic": "അർദ്ധരാത്രിയിൽ യമുന കടന്ന് ഗോകുലത്തിലേക്കുള്ള ദിവ്യയാത്ര",
                "content": """### ഭഗവാന്റെ നിർദ്ദേശവും ശിശുരൂപവും

മാതാപിതാക്കളെ സമാശ്വസിപ്പിച്ച ശേഷം, പൂർണ്ണപുരുഷോത്തമനായ ഭഗവാൻ ശ്രീകൃഷ്ണൻ തന്റെ ഐശ്വര്യപൂർണ്ണമായ ചതുർഭുജ രൂപം പിൻവലിച്ച് അതീവ മനോഹരനായ ഒരു സാധാരണ നവജാതശിശുവായി മാറി. ആ നിമിഷത്തിൽ ഭഗവാൻ വസുദേവർക്ക് ഉള്ളിൽ പ്രേരണ നൽകി: "എന്നെ ഉടനടി യമുനാനദി കടന്ന് ഗോകുലത്തിൽ നന്ദഗോപരുടെ ഭവനത്തിലേക്ക് കൊണ്ടുപോകൂ. യശോദ ഇപ്പോൾ ഒരു പെൺകുഞ്ഞിന് ജന്മം നൽകിയിട്ടുണ്ട്. എന്നെ യശോദയുടെ അരികിൽ കിടത്തി, ആ പെൺകുഞ്ഞിനെയുമെടുത്ത് ആരും ഉണരുന്നതിനു മുൻപ് ഇങ്ങോട്ട് മടങ്ങിവരൂ."

ഇതുകേട്ട് വസുദേവർ ധൈര്യം സംഭരിച്ചുവെങ്കിലും, കാൽവിലങ്ങുകളും കാവൽക്കാരും നിറഞ്ഞ ആ വലിയ കാരാഗൃഹത്തിൽ നിന്ന് എങ്ങനെ പുറത്തുകടക്കുമെന്ന് ചിന്തിച്ചു.

### യോഗമായാപ്രഭാവം: വിലങ്ങുകൾ അഴിഞ്ഞു, വാതിലുകൾ തുറക്കപ്പെട്ടു

അപ്പോൾത്തന്നെ ഭഗവാന്റെ യോഗമായാശക്തിയാൽ അത്ഭുതങ്ങൾ സംഭവിച്ചു:

1. **എല്ലാവരിലും ഗാഢനിദ്ര പടർന്നു:** കാരാഗൃഹത്തിലെ ക്രൂരന്മാരായ കാവൽക്കാരും പട്ടികളും മഥുരയിലെ പൗരന്മാരും ഉണരാനാവാത്ത വിധം ഗാഢനിദ്രയിലാണ്ടുപോയി.
2. **ഇരുമ്പുവിലങ്ങുകൾ തനിയെ അഴിഞ്ഞുവീണു:** ഉണ്ണികൃഷ്ണനെ കൈകളിലെടുത്ത മാത്രയിൽ വസുദേവരുടെ കൈകാലുകളിലെ ഭാരമേറിയ ഇരുമ്പുചങ്ങലകൾ സ്വയം അഴിഞ്ഞു താഴെവീണു.
3. **കൂറ്റൻ വാതിലുകൾ തനിയെ തുറന്നു:** വസുദേവർ മുന്നോട്ടു നടന്നപ്പോൾ കാരാഗൃഹത്തിലെ വലിയ ഇരുമ്പുവാതിലുകളിലെ പൂട്ടുകൾ തനിയെ പൊട്ടി, വാതിലുകൾ ഇരുവശത്തേക്കും മലർക്കെ തുറക്കപ്പെട്ടു.

ഒരു മുളങ്കൊട്ടയിൽ മൃദുവായ വസ്ത്രങ്ങൾ വിരിച്ച് ഉണ്ണികൃഷ്ണനെ അതിൽ കിടത്തി, കൊട്ട തലയിലേറ്റി വസുദേവർ കൂരിരുട്ടിൽ ധൈര്യത്തോടെ പുറത്തേക്കിറങ്ങി.

### പേമാരിയും അനന്തന്റെ കുടയും

യമുനാതീരത്തേക്ക് നടക്കുമ്പോൾ ആകാശത്ത് പേമാരി പെയ്തിറങ്ങി. കാറ്റും മിന്നലും ഇടിയും ആ രാത്രിയെ ഭയാനകമാക്കി.

തന്റെ പ്രിയനാഥനായ ഉണ്ണികൃഷ്ണനെ മഴവെള്ളത്തിൽ നിന്നും സംരക്ഷിക്കാനായി അനന്തശേഷൻ പിന്നാലെ എത്തി. തന്റെ അനേകം പത്തികൾ ഒരു കുടപോലെ വിടർത്തിപ്പിടിച്ച് ശേഷനാഗം ഒരു തുള്ളി മഴവെള്ളം പോലും കൃഷ്ണന്റെ ശരീരത്തിൽ വീഴാതെ സംരക്ഷിച്ചു.

### യമുന വഴിമാറിക്കൊടുക്കുന്നു

യമുനാതീരത്തെത്തിയ വസുദേവർ കണ്ടത് ഭയപ്പെടുത്തുന്ന കാഴ്ചയായിരുന്നു. മഴവെള്ളപ്പാച്ചിലിൽ പതഞ്ഞുപൊങ്ങുന്ന തിരമാലകളോടും ചുഴികളോടും കൂടി യമുന അലറിക്കൊണ്ടൊഴുകുകയായിരുന്നു.

എന്നാൽ, ഭഗവാനെ തലയിലേറ്റി വസുദേവർ വെള്ളത്തിലേക്ക് കാൽവെച്ചതും അത്ഭുതം നടന്നു:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അദ്ധ്യായം 3, ശ്ലോകം 50**
> 
> *മഘോനി വർഷത്യസകൃദ് യമാനുജാ*  
> *ഗഭീരതോയൗഘജവോർമ്മിഫേണിലാ |*  
> *ഭയാനകാവർത്തശതാകുലാ നദീ*  
> *മാർഗ്ഗം ദദൗ സിന്ധുരിവ ശ്രിയഃ പതേഃ ||*  
> 
> **അർത്ഥം:** ആകാശത്തുനിന്ന് പേമാരി ചൊരിഞ്ഞുകൊണ്ടിരിക്കെ, യമന്റെ സഹോദരിയായ യമുനാനദി ഭയാനകമായ ചുഴികളും തിരമാലകളും നിറഞ്ഞതായിരുന്നുവെങ്കിലും, പണ്ട് ലങ്കയിലേക്കു പോകാൻ സമുദ്രം ശ്രീരാമചന്ദ്രന് വഴിമാറിക്കൊടുത്തതുപോലെ വസുദേവർക്ക് വഴിമാറിക്കൊടുത്തു.

യമുന വഴിമാറിക്കൊടുത്തതോടെ വസുദേവർക്ക് അരയൊപ്പം വെള്ളത്തിലൂടെ കരയിലെന്നപോലെ മറുകരയിലെത്താൻ സാധിച്ചു.

### ഗോകുലത്തിലെ ദിവ്യമായ കൈമാറ്റം

മറുകരയിലെത്തിയ വസുദേവർ യോഗമായാപ്രഭാവത്താൽ ആരുമറിയാതെ നന്ദഗോപരുടെ ഭവനത്തിലെത്തി. പ്രസവക്ഷീണത്താൽ യശോദ അബോധാവസ്ഥയിൽ ഉറങ്ങുകയായിരുന്നു; ജനിച്ചത് ആൺകുഞ്ഞോ പെൺകുഞ്ഞോ എന്ന് അവർ അറിഞ്ഞിരുന്നില്ല.

വസുദേവർ ഉണ്ണികൃഷ്ണനെ യശോദയുടെ അരികിൽ കിടത്തി. തുടർന്ന് യശോദ പ്രസവിച്ച പെൺകുഞ്ഞിനെ—സാക്ഷാൽ യോഗമായയെ—എടുത്ത് നിശബ്ദമായി അവിടെനിന്നും മടങ്ങി.

പ്രഭാതത്തിനു മുൻപ് വസുദേവർ കാരാഗൃഹത്തിൽ തിരിച്ചെത്തി. അകത്തുകയറിയ ഉടൻ വാതിലുകൾ തനിയെ അടഞ്ഞു പൂട്ടിപ്പോവുകയും ചങ്ങലകൾ വീണ്ടും വസുദേവരെ ബന്ധിക്കുകയും ചെയ്തു. വസുദേവർ ആ പെൺകുഞ്ഞിനെ ദേവകിയുടെ മടിയിൽ കിടത്തി കാത്തിരുന്നു.""",
                "questions": [
                    {
                        "question": "മാതാപിതാക്കളോട് സംസാരിച്ച ശേഷം ഭഗവാൻ ഏതു രൂപമാണ് സ്വീകരിച്ചത്?",
                        "options": [
                            {"text": "രണ്ടു കൈകളുള്ള അതിമനോഹരമായ സാധാരണ ശിശുരൂപം", "is_correct": True},
                            {"text": "നരസിംഹ രൂപം", "is_correct": False},
                            {"text": "യോദ്ധാവിന്റെ രൂപം", "is_correct": False},
                            {"text": "ജ്യോതിസ്സ്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഉണ്ണിയെ എങ്ങോട്ടാണ് കൊണ്ടുപോകാൻ ഭഗവാൻ നിർദ്ദേശിച്ചത്?",
                        "options": [
                            {"text": "യമുന കടന്ന് ഗോകുലത്തിൽ നന്ദഗോപരുടെ ഭവനത്തിലേക്ക്", "is_correct": True},
                            {"text": "ഹസ്തിനപുരത്തിലേക്ക്", "is_correct": False},
                            {"text": "ഗോവർദ്ധന മലയിലേക്ക്", "is_correct": False},
                            {"text": "ദണ്ഡകാരണ്യത്തിലേക്ക്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "വസുദേവർ പുറപ്പെട്ടപ്പോൾ കാവൽക്കാർക്ക് എന്തു സംഭവിച്ചു?",
                        "options": [
                            {"text": "യോഗമായാപ്രഭാവത്താൽ എല്ലാവരും ഗാഢനിദ്രയിലായി", "is_correct": True},
                            {"text": "മഴ പേടിച്ച് ഓടിപ്പോയി", "is_correct": False},
                            {"text": "കംസനെതിരെ തിരിഞ്ഞു", "is_correct": False},
                            {"text": "ശിലകളായി മാറി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "കാരാഗൃഹത്തിലെ ചങ്ങലകൾക്കും വാതിലുകൾക്കും എന്തു സംഭവിച്ചു?",
                        "options": [
                            {"text": "ചങ്ങലകൾ തനിയെ അഴിഞ്ഞുവീണു, വാതിലുകൾ മലർക്കെ തുറക്കപ്പെട്ടു", "is_correct": True},
                            {"text": "വസുദേവർ മുറിച്ചുമാറ്റി", "is_correct": False},
                            {"text": "കാവൽക്കാർ താക്കോൽ നൽകി", "is_correct": False},
                            {"text": "ഭൂകമ്പത്തിൽ തകർന്നു", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഉണ്ണികൃഷ്ണനെ വസുദേവർ എങ്ങനെയാണ് കൊണ്ടുപോയത്?",
                        "options": [
                            {"text": "മുളങ്കൊട്ടയിലാക്കി തലയിലേറ്റി", "is_correct": True},
                            {"text": "സ്വർണ്ണരഥത്തിൽ", "is_correct": False},
                            {"text": "കുതിരപ്പുറത്ത്", "is_correct": False},
                            {"text": "തോൽസഞ്ചിയിൽ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പേമാരിയിൽ നിന്നും ഉണ്ണികൃഷ്ണനെ രക്ഷിച്ചത് ആരാണ്?",
                        "options": [
                            {"text": "പത്തികൾ കുടപോലെ വിടർത്തിപ്പിടിച്ച അനന്തശേഷൻ", "is_correct": True},
                            {"text": "പട്ടുക്കുട", "is_correct": False},
                            {"text": "ആലില", "is_correct": False},
                            {"text": "ദേവകിയുടെ വസ്ത്രം", "is_correct": False}
                        ]
                    },
                    {
                        "question": "യമുന വഴിമാറിയതിനെ ശ്രീമദ് ഭാഗവതത്തിൽ ഏത് സംഭവത്തോടാണ് ഉപമിച്ചിരിക്കുന്നത്?",
                        "options": [
                            {"text": "ശ്രീരാമചന്ദ്രന് സമുദ്രം വഴിമാറിക്കൊടുത്തതുപോലെ", "is_correct": True},
                            {"text": "ഗംഗ ശിവന്റെ ജടയിൽ വീണതുപോലെ", "is_correct": False},
                            {"text": "പാലാഴി മഥനത്തോട്", "is_correct": False},
                            {"text": "അയോദ്ധ്യയിലെ പ്രളയത്തോട്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പെൺകുഞ്ഞാണ് ജനിച്ചതെന്ന് യശോദ അറിയാതിരുന്നത് എന്തുകൊണ്ട്?",
                        "options": [
                            {"text": "പ്രസവക്ഷീണത്താലും യോഗമായയാലും ഗാഢനിദ്രയിലായിരുന്നു", "is_correct": True},
                            {"text": "മുറിയിൽ ഇരുട്ടായിരുന്നതുകൊണ്ട്", "is_correct": False},
                            {"text": "യശോദ വീട്ടിലില്ലാതിരുന്നതുകൊണ്ട്", "is_correct": False},
                            {"text": "ദാസിമാർ കുഞ്ഞിനെ മാറ്റിയതുകൊണ്ട്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "യശോദ പ്രസവിച്ച പെൺകുഞ്ഞ് യഥാർത്ഥത്തിൽ ആരായിരുന്നു?",
                        "options": [
                            {"text": "ഭഗവാന്റെ അന്തരംഗശക്തിയായ യോഗമായ", "is_correct": True},
                            {"text": "സ്വർഗ്ഗത്തിലെ അപ്സരസ്സ്", "is_correct": False},
                            {"text": "സാധാരണ ഇടയപ്പെൺകുട്ടി", "is_correct": False},
                            {"text": "പൂതന", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പെൺകുഞ്ഞുമായി വസുദേവർ കാരാഗൃഹത്തിൽ തിരിച്ചെത്തിയപ്പോൾ എന്തു സംഭവിച്ചു?",
                        "options": [
                            {"text": "വാതിലുകൾ തനിയെ അടഞ്ഞുപൂട്ടി, ചങ്ങലകൾ വീണ്ടും ബന്ധിച്ചു", "is_correct": True},
                            {"text": "കാരാഗൃഹം തകർന്നു", "is_correct": False},
                            {"text": "കംസൻ വാളുമായി നിന്നിരുന്നു", "is_correct": False},
                            {"text": "ദേവകി രക്ഷപ്പെട്ടു", "is_correct": False}
                        ]
                    }
                ]
            },
            "bn": {
                "mainTopic": "কৃষ্ণ লীলা",
                "subTopic": "অর্ধরাত্রে যমুনা পার হয়ে গোকুল যাত্রা",
                "content": """### ভগবানের নির্দেশ ও দ্বিভুজ শিশুরূপ ধারণ

পিতামাতাকে সান্ত্বনা প্রদানের পর পূর্ণ পুরুষোত্তম ভগবান শ্রীকৃষ্ণ তাঁর চতুর্ভুজ রূপ সংবরণ করে এক পরম মনোহর দ্বিভুজ মানবশিশুর রূপ ধারণ করলেন। সেই মুহূর্তে ভগবান বসুদেবের হৃদয়ে দৈব প্রেরণা প্রদান করলেন: "আমাকে অনতিবিলম্বে যমুনা পার করে গোকুলে নন্দ মহারাজের গৃহে নিয়ে যাও। সেখানে নন্দপত্নী যশোদা সদ্য এক কন্যার জন্ম দিয়েছেন। আমাকে নিঃশব্দে যশোদার শয্যায় রেখে তাঁর নবজাত কন্যাকে নিয়ে কেউ জেগে ওঠার আগেই এই কারাগারে ফিরে এসো।"

বসুদেবের অন্তর অভূতপূর্ব সাহসে পূর্ণ হলো, কিন্তু তিনি ভাবছিলেন যে নিগড়ে আবদ্ধ অবস্থায় প্রহরীদের নজর এড়িয়ে তিনি কীভাবে এই কারাগার থেকে বের হবেন।

### যোগমায়ার প্রভাব: শৃঙ্খলমুক্তি ও কপাট উন্মোচন

তৎক্ষণাৎ ভগবানের অচিন্ত্য যোগমায়া শক্তির প্রভাবে সমগ্র মথুরায় অলৌকিক ঘটনা ঘটতে লাগল:

1. **সকলের গভীর নিদ্রা:** কারাগারের সমস্ত হিংস্র প্রহরী, দ্বারপাল, কুকুর এবং মথুরাবাসী যোগমায়ার প্রভাবে এক গভীর অচেত নিদ্রায় আচ্ছন্ন হয়ে পড়ল।
2. **লোহার শৃঙ্খল খসে পড়ল:** বসুদেব যেমনই নবজাত শিশুকে কোলে তুলে নিলেন, অমনি তাঁর হাত ও পায়ের ভারী শৃঙ্খল আপনা থেকেই খুলে নিঃশব্দে মাটিতে পড়ে গেল।
3. **বিশাল কপাটসমূহ খুলে গেল:** কারাগারের ভারী লোহার ফটকসমূহ বিশাল শিকল ও তালায় আবদ্ধ ছিল। কিন্তু বসুদেব শিশু কৃষ্ণকে নিয়ে অগ্রসর হতেই সকল তালা আপনা থেকেই খুলে গেল এবং কপাটসমূহ সূর্যের উদয়ে অন্ধকার অপসৃত হওয়ার ন্যায় উন্মুক্ত হয়ে গেল।

একটি বেতের ডালায় কোমল বস্ত্র বিছিয়ে বসুদেব দিব্য শিশুকে তার মধ্যে শয়ন করালেন এবং সেই ডালা মাথায় তুলে নির্ভয়ে নিশীথ অন্ধকারে বেরিয়ে পড়লেন।

### প্রবল বর্ষণ ও অনন্ত শেষের ছত্র

বসুদেব যখন মথুরার জনশূন্য পথ অতিক্রম করে যমুনাতীরে উপস্থিত হলেন, তখন আকাশে প্রবল বর্ষণ শুরু হলো। ঘনকৃষ্ণ মেঘ থেকে অবিশ্রান্ত ধারায় জল পড়তে লাগল, বজ্রপাত হতে লাগল।

শিশু কৃষ্ণকে বর্ষার শীতল জল থেকে রক্ষা করতে ভগবানের নিত্য সেবক অনন্ত শেষনাগ আবির্ভূত হলেন। বসুদেবের পশ্চাতে গমন করে শেষনাগ তাঁর বহু ফণা একটি ছত্রের ন্যায় বিস্তার করে রাখলেন, যাতে একটিও জলবিন্দু কৃষ্ণের সুকোমল শ্রীঅঙ্গে না লাগে।

### উত্তাল যমুনার পথ প্রদান

যমুনাতীরে এসে বসুদেব দেখলেন যে বর্ষার জলে যমুনা অত্যন্ত ভয়াল রূপ ধারণ করেছে। গভীর জলপ্রবাহ, উত্তাল সফেন তরঙ্গ এবং শত শত ঘূর্ণাবর্তে যমুনা গর্জন করছিল।

কিন্তু বসুদেব ভগবানকে মস্তকে নিয়ে যেমনই জলে পদার্পণ করলেন, অমনি এক পরম অলৌকিক দৃশ্য দেখা গেল:

> **শ্রীমদ্ভাগবত, স্কন্ধ ১০, অধ্যায় ৩, শ্লোক ৫০**
> 
> *মঘোনি বর্ষত্যসকৃদ্ যমানুজা*  
> *গভীরতোয়ৌঘজবোর্ম্মিফেণিলা ।*  
> *ভয়ানকাবর্ত্তশতাকুলা নদী*  
> *মার্গং দদৌ সিন্ধুরিব শ্রিয়ঃ পতেঃ ॥*  
> 
> **অনুবাদ:** প্রবল বর্ষণকালে যমরাজের ভগিনী যমুনানদী গভীর জলরাশি, ফেনিল উত্তাল তরঙ্গ এবং শত শত ভয়ানক ঘূর্ণাবর্তে পূর্ণ থাকা সত্ত্বেও বসুদেবকে পথ প্রদান করল, যেমন পূর্বে সাগর ভগবান শ্রীরামচন্দ্রকে লঙ্কায় যাওয়ার পথ দিয়েছিল।

ভগবানের চরণস্পর্শ পেয়ে যমুনা শান্ত হয়ে কোমর সমান জলে পরিণত হলো। বসুদেব অক্লেশে নদী পার হয়ে গেলেন।

### গোকুলে দিব্য বিনিময়

যমুনা পার হয়ে বসুদেব গোকুলে নন্দভবনে প্রবেশ করলেন। যোগমায়ার প্রভাবে কেউই তাঁকে দেখতে পেল না। প্রসবক্লান্তিতে অচেতন হয়ে যশোদা দেবী গভীর নিদ্রায় মগ্ন ছিলেন; তিনি জানতেনও না যে তাঁর পুত্র হয়েছে না কন্যা।

বসুদেব পরম যত্নে শিশু কৃষ্ণকে যশোদার পাশে শুইয়ে দিলেন। অতঃপর যশোদার নবজাত কন্যাকে—যিনি স্বয়ং যোগমায়া—কোলে তুলে নিয়ে নিঃশব্দে মথুরার উদ্দেশ্যে যাত্রা করলেন।

ভোর হবার পূর্বেই বসুদেব পুনরায় যমুনা পার হয়ে মথুরার কারাগারে ফিরে এলেন। তিনি প্রবেশ করতেই কপাটসমূহ পুনরায় বন্ধ হয়ে গেল, তালা লেগে গেল এবং শৃঙ্খল পুনরায় তাঁর হাত-পা আবদ্ধ করল। বসুদেব সেই কন্যাকে দেবকীর কোলে সমর্পণ করে পরবর্তী লীলার প্রতীক্ষা করতে লাগলেন।""",
                "questions": [
                    {
                        "question": "পিতামাতার সাথে কথা বলার পর ভগবান কোন রূপ ধারণ করেছিলেন?",
                        "options": [
                            {"text": "মনোহর দ্বিভুজ মানবশিশুর রূপ", "is_correct": True},
                            {"text": "নৃসিংহ রূপ", "is_correct": False},
                            {"text": "ধনুর্ধর যোদ্ধা রূপ", "is_correct": False},
                            {"text": "জ্যোতির্বলয়", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ভগবান বসুদেবকে শিশুকে কোথায় নিয়ে যেতে নির্দেশ দিয়েছিলেন?",
                        "options": [
                            {"text": "যমুনা পার করে গোকুলে নন্দ মহারাজের গৃহে", "is_correct": True},
                            {"text": "হস্তিনাপুরে", "is_correct": False},
                            {"text": "গোবর্ধন পর্বতে", "is_correct": False},
                            {"text": "দণ্ডকারণ্যে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "বসুদেব বের হবার সময় প্রহরীদের কি হয়েছিল?",
                        "options": [
                            {"text": "যোগমায়ার প্রভাবে সকলে গভীর নিদ্রায় আচ্ছন্ন হয়েছিল", "is_correct": True},
                            {"text": "বৃষ্টিতে ভয় পেয়ে পালিয়েছিল", "is_correct": False},
                            {"text": "কংসের বিরুদ্ধে বিদ্রোহ করেছিল", "is_correct": False},
                            {"text": "পাথর হয়ে গিয়েছিল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "কারাগারের শৃঙ্খল ও দরজায় কি অলৌকিক ঘটনা ঘটেছিল?",
                        "options": [
                            {"text": "শৃঙ্খল খুলে পড়ে গিয়েছিল এবং কপাটসমূহ আপনা থেকেই উন্মুক্ত হয়েছিল", "is_correct": True},
                            {"text": "বসুদেব কেটে ফেলেছিলেন", "is_correct": False},
                            {"text": "প্রহরীরা চাবি দিয়েছিল", "is_correct": False},
                            {"text": "ভূমিকম্পে ভেঙেছিল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "বসুদেব শিশু কৃষ্ণকে কীভাবে বহন করেছিলেন?",
                        "options": [
                            {"text": "বেতের ডালায় রেখে মাথায় বহন করেছিলেন", "is_correct": True},
                            {"text": "স্বর্ণরথে", "is_correct": False},
                            {"text": "ঘোড়ার পিঠে", "is_correct": False},
                            {"text": "চামড়ার থলিতে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "প্রবল বৃষ্টি থেকে শিশু কৃষ্ণকে কে রক্ষা করেছিলেন?",
                        "options": [
                            {"text": "অনন্ত শেষনাগ তাঁর ফণা ছত্রের মতো বিস্তার করে", "is_correct": True},
                            {"text": "রেশমি ছাতা", "is_correct": False},
                            {"text": "বটপাতা", "is_correct": False},
                            {"text": "দেবকীর আঁচল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "যমুনার পথ প্রদানকে শ্রীমদ্ভাগবতে কোন ঘটনার সাথে তুলনা করা হয়েছে?",
                        "options": [
                            {"text": "শ্রীরামচন্দ্রকে সাগর পথ দেওয়ার ঘটনার সাথে", "is_correct": True},
                            {"text": "শিবের জটায় গঙ্গা অবতরণের সাথে", "is_correct": False},
                            {"text": "সমুদ্র মন্থনের সাথে", "is_correct": False},
                            {"text": "অযোধ্যার বন্যার সাথে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "যশোদা দেবী কেন জানতে পারেননি যে তাঁর কন্যা হয়েছে?",
                        "options": [
                            {"text": "প্রসবক্লান্তি ও যোগমায়ার প্রভাবে তিনি গভীর ঘুমে অচেতন ছিলেন", "is_correct": True},
                            {"text": "ঘরে আলো ছিল না বলে", "is_correct": False},
                            {"text": "তিনি ঘরে ছিলেন না বলে", "is_correct": False},
                            {"text": "দাসী সন্তান সরিয়ে নিয়েছিল বলে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "যশোদার গর্ভজাত কন্যা প্রকৃতপক্ষে কে ছিলেন?",
                        "options": [
                            {"text": "ভগবানের অন্তরঙ্গা শক্তি যোগমায়া", "is_correct": True},
                            {"text": "স্বর্গের অপ্সরা", "is_correct": False},
                            {"text": "সাধারণ গোপবালিকা", "is_correct": False},
                            {"text": "পূতনা", "is_correct": False}
                        ]
                    },
                    {
                        "question": "কন্যাকে নিয়ে কারাগারে ফিরে আসার পর কি ঘটেছিল?",
                        "options": [
                            {"text": "দরজা আপনা থেকেই বন্ধ হয়ে তালা লেগেছিল এবং শৃঙ্খল পুনরায় আবদ্ধ করেছিল", "is_correct": True},
                            {"text": "কারাগার ভেঙে পড়েছিল", "is_correct": False},
                            {"text": "কংস দাঁড়িয়ে ছিল", "is_correct": False},
                            {"text": "দেবকী পালিয়েছিলেন", "is_correct": False}
                        ]
                    }
                ]
            },
            "te": {
                "mainTopic": "కృష్ణ లీలలు",
                "subTopic": "అర్ధరాత్రి వేళ యమునను దాటి గోకుల ప్రయాణం",
                "content": """### భగవానుని ఆదేశం మరియు శిశు రూప ధారణ

తల్లిదండ్రులకు సాంత్వన పలికిన అనంతరం, పూర్ణ పురుషోత్తముడైన భగవాన్ శ్రీకృష్ణుడు తన చతుర్భుజ రూపాన్ని ఉపసంహరించి, అత్యంత మనోహరమైన సాధారణ రెండు చేతుల పసికందు రూపాన్ని ధరించాడు. ఆ క్షణంలో భగవంతుడు వసుదేవుని అంతరంగంలో ఇలా ఆదేశించాడు: "నన్ను వెంటనే యమునా నదిని దాటించి గోకులంలోని నందమహారాజు గృహానికి తీసుకువెళ్ళండి. యశోదాదేవి ఒక ఆడపిల్లకు జన్మనిచ్చింది. నన్ను ఆమె ప్రక్కన పడుకోబెట్టి, ఆ పసిపాపను తీసుకుని ఎవరూ మేల్కొనక ముందే ఇక్కడికి తిరిగి రండి."

వసుదేవుని హృదయం ధైర్యంతో నిండింది, కానీ కాళ్ళకు బంధించిన సంకెళ్ళు, భారీ ఇనుప తలుపులు, సాయుధులైన కాపలాదారుల మధ్య ఇది ఎలా సాధ్యమని ఆయన ఆలోచించాడు.

### యోగమాయ ప్రభావం: తెగిపడిన సంకెళ్ళు, తెరుచుకున్న తలుపులు

ఆ క్షణంలోనే భగవంతుని అచింత్య యోగమాయా శక్తి ప్రభావంతో మథురలో అద్భుతాలు జరిగాయి:

1. **అందరినీ ఆవహించిన గాఢనిద్ర:** కాపలాదారులు, ద్వారపాలకులు, కుక్కలు మరియు మథుర ప్రజలంతా యోగమాయ ప్రభావంతో గాఢనిద్రలోకి జారుకున్నారు. ఎవరూ కళ్ళు తెరవలేకపోయారు.
2. **సంకెళ్ళు వాటంతట అవే తొలగిపోయాయి:** వసుదేవుడు బాలకృష్ణుని చేతుల్లోకి తీసుకోగానే, ఆయన కాళ్ళకు చేతులకు ఉన్న బరువైన ఇనుప గొలుసులు శబ్దం లేకుండా ఊడి కిందపడిపోయాయి.
3. **భారీ తలుపులు వాటంతట అవే తెరుచుకున్నాయి:** చెరసాల యొక్క భారీ తలుపులకు వేసిన తాళాలు వాటంతట అవే ఊడిపోయాయి; సూర్యోదయానికి చీకటి తొలగిపోయినట్లుగా ఇనుప ద్వారాలు తెరుచుకున్నాయి.

వెదురు బుట్టలో మెత్తని వస్త్రాలు పరిచి, బాలకృష్ణుని అందులో పడుకోబెట్టి, ఆ బుట్టను నెత్తిన పెట్టుకుని వసుదేవుడు నిర్భయంగా అర్ధరాత్రి చీకట్లోకి అడుగుపెట్టాడు.

### కుండపోత వర్షం మరియు ఆదిశేషుని గొడుగు

వసుదేవుడు యమునా తీరానికి నడుస్తున్న సమయంలో ఆకాశంలో భీకరమైన వర్షం కురవడం ప్రారంభమైంది. చీకటి మేఘాలు కమ్ముకుని మెరుపులు, ఉరుములతో కుండపోతగా వర్షం కురిసింది.

బాలకృష్ణుని వర్షపు నీటి నుండి రక్షించడానికి, భగవంతుని నిత్య సేవకుడైన ఆదిశేషుడు అదృశ్యంగా వెన్నంటి వచ్చాడు. వసుదేవుని వెనుక నడుస్తూ, తన వేలాది పడగలను ఒక పెద్ద గొడుగులా విప్పి, ఒక్క వర్షపు చుక్క కూడా బాలకృష్ణుని సుకుమార దేహంపై పడకుండా కాపాడాడు.

### దారిచ్చిన ఉధృత యమునానది

యమునా తీరానికి చేరుకున్న వసుదేవునికి నది భయంకరంగా కనిపించింది. వర్షపు వరదతో పొంగిపొర్లుతూ, నురుగులతో, సుడిగుండాలతో యమున ఉగ్రరూపం దాల్చి ప్రవహిస్తోంది.

అయినప్పటికీ, భగవంతుని నెత్తిన మోస్తూ వసుదేవుడు నీటిలోకి దిగగానే ఒక దివ్య అద్భుతం జరిగింది:

> **శ్రీమద్భాగవతం, స్కంధం 10, అధ్యాయం 3, శ్లోకం 50**
> 
> *మఘోని వర్షత్యసకృద్ యమానుజా*  
> *గభీరతోయౌఘజవోర్మిఫేణిలా |*  
> *భయానకావర్తశతాకులా నదీ*  
> *మార్గం దదౌ సింధురివ శ్రియః పతేః ||*  
> 
> **తాత్పర్యం:** ఆకాశం నుండి కుండపోతగా వర్షం కురుస్తున్న సమయంలో, లోతైన ప్రవాహంతో, తీవ్రమైన తరంగాలతో, భయంకరమైన సుడిగుండాలతో ఉప్పొంగుతున్న యమునానది, పూర్వకాలంలో శ్రీరామచంద్రునికి సముద్రుడు దారిచ్చినట్లుగా వసుదేవునికి మార్గమిచ్చింది.

తన స్వామి పాదాలను తాకగానే యమున శాంతించి, లోతు తగ్గి మోకాళ్ళ లోతుకు మారింది. వసుదేవుడు నేలపై నడిచినట్లు నదిని దాటాడు.

### గోకులంలో దివ్య పరివర్తన

యమునను దాటి వసుదేవుడు గోకులంలోని నందుని భవనానికి చేరుకున్నాడు. యోగమాయ ప్రభావంతో ఎవరికీ కనిపించకుండా లోపలికి ప్రవేశించాడు. యశోదాదేవి ప్రసవ వేదనతో స్పృహతప్పి గాఢనిద్రలో ఉంది; పుట్టింది మగబిడ్డో ఆడబిడ్డో కూడా ఆమెకు తెలియదు.

వసుదేవుడు కృష్ణుని యశోద పక్కన పడుకోబెట్టాడు. అనంతరం ఆమె జన్మనిచ్చిన పాపను—సాక్షాత్తు యోగమాయను—చేతుల్లోకి తీసుకుని నిశ్శబ్దంగా బయలుదేరాడు.

తెల్లవారకముందే వసుదేవుడు మథుర చెరసాలకు చేరుకున్నాడు. ఆయన లోపలికి అడుగుపెట్టగానే తలుపులు వాటంతట అవే మూసుకుని తాళాలు పడ్డాయి; సంకెళ్ళు మళ్ళీ బిగుసుకున్నాయి. వసుదేవుడు ఆ పాపను దేవకి ఒడిలో పెట్టి ಮುಂದಿನ లీల కోసం ఎదురుచూశాడు.""",
                "questions": [
                    {
                        "question": "తల్లిదండ్రులతో మాట్లాడిన తర్వాత భగవంతుడు ఏ రూపాన్ని ధరించాడు?",
                        "options": [
                            {"text": "రెండు చేతుల సాధారణ పసికందు రూపం", "is_correct": True},
                            {"text": "నరసింహ రూపం", "is_correct": False},
                            {"text": "యోధుని రూపం", "is_correct": False},
                            {"text": "దివ్య జ్యోతి", "is_correct": False}
                        ]
                    },
                    {
                        "question": "బాలుని ఎక్కడికి తీసుకువెళ్ళమని భగవానుడు ఆదేశించాడు?",
                        "options": [
                            {"text": "యమున దాటి గోకులంలోని నందుని గృహానికి", "is_correct": True},
                            {"text": "హస్తినాపురానికి", "is_correct": False},
                            {"text": "గోవర్ధన పర్వతానికి", "is_correct": False},
                            {"text": "దండకారణ్యానికి", "is_correct": False}
                        ]
                    },
                    {
                        "question": "వసుదేవుడు బయలుదేరినప్పుడు కాపలాదారులకు ఏమైంది?",
                        "options": [
                            {"text": "యోగమాయ ప్రభావంతో అందరూ గాఢనిద్రలోకి జారుకున్నారు", "is_correct": True},
                            {"text": "వర్షానికి భయపడి పారిపోయారు", "is_correct": False},
                            {"text": "కంసునిపై తిరుగుబాటు చేశారు", "is_correct": False},
                            {"text": "రాళ్ళుగా మారారు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "చెరసాల సంకెళ్ళకు, తలుపులకు ఏమి జరిగింది?",
                        "options": [
                            {"text": "సంకెళ్ళు వాటంతట అవే ఊడిపోయాయి, తలుపులు తెరుచుకున్నాయి", "is_correct": True},
                            {"text": "వసుదేవుడు కోసేశాడు", "is_correct": False},
                            {"text": "కాపలాదారులు తాళాలు ఇచ్చారు", "is_correct": False},
                            {"text": "భూకంపంతో కూలిపోయాయి", "is_correct": False}
                        ]
                    },
                    {
                        "question": "బాలకృష్ణుని వసుదేవుడు ఎలా తీసుకెళ్ళాడు?",
                        "options": [
                            {"text": "వెదురు బుట్టలో పడుకోబెట్టి నెత్తిన పెట్టుకుని", "is_correct": True},
                            {"text": "బంగారు రథంలో", "is_correct": False},
                            {"text": "గుర్రంపై", "is_correct": False},
                            {"text": "తోలు సంచిలో", "is_correct": False}
                        ]
                    },
                    {
                        "question": "కుండపోత వర్షంలో బాలకృష్ణుని ఎవరు రక్షించారు?",
                        "options": [
                            {"text": "ఆదిశేషుడు తన పడగలను గొడుగులా విప్పి", "is_correct": True},
                            {"text": "పట్టు గొడుగు", "is_correct": False},
                            {"text": "మర్రి ఆకు", "is_correct": False},
                            {"text": "దేవకి చీర కొంగు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "యమున దారివ్వడాన్ని భాగవతంలో దేనితో పోల్చారు?",
                        "options": [
                            {"text": "శ్రీరామునికి సముద్రుడు దారిచ్చినట్లుగా", "is_correct": True},
                            {"text": "శివుని జటాజూటంపై గంగ దిగినట్లుగా", "is_correct": False},
                            {"text": "క్షీరసాగర మథనంతో", "is_correct": False},
                            {"text": "అయోధ్య వరదలతో", "is_correct": False}
                        ]
                    },
                    {
                        "question": "యశోదకు ఆడపిల్ల పుట్టినట్లు ఎందుకు తెలియలేదు?",
                        "options": [
                            {"text": "ప్రసవ వేదన మరియు యోగమాయ వల్ల ఆమె గాఢనిద్రలో ఉంది", "is_correct": True},
                            {"text": "చీకటిగా ఉన్నందున", "is_correct": False},
                            {"text": "ఆమె ఇంట్లో లేనందున", "is_correct": False},
                            {"text": "దాసీలు పాపను దాచినందున", "is_correct": False}
                        ]
                    },
                    {
                        "question": "యశోదకు పుట్టిన పాప వాస్తవానికి ఎవరు?",
                        "options": [
                            {"text": "భగవంతుని అంతరంగ శక్తి యోగమాయ", "is_correct": True},
                            {"text": "దేవలోకపు అప్సరస", "is_correct": False},
                            {"text": "సాధారణ పల్లెపిల్ల", "is_correct": False},
                            {"text": "పూతన", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పాపను తీసుకుని వసుదేవుడు తిరిగి రాగానే ఏమి జరిగింది?",
                        "options": [
                            {"text": "తలుపులు మూసుకుని తాళాలు పడ్డాయి, సంకెళ్ళు మళ్ళీ బంధించాయి", "is_correct": True},
                            {"text": "చెరసాల కూలిపోయింది", "is_correct": False},
                            {"text": "కంసుడు కత్తితో వేచి ఉన్నాడు", "is_correct": False},
                            {"text": "దేవకి తప్పించుకుంది", "is_correct": False}
                        ]
                    }
                ]
            },
            "kn": {
                "mainTopic": "ಕೃಷ್ಣ ಲೀಲೆಗಳು",
                "subTopic": "ಮಧ್ಯರಾತ್ರಿಯಲ್ಲಿ ಯಮುನೆಯನ್ನು ದಾಟಿ ಗೋಕುಲ ಯಾತ್ರೆ",
                "content": """### ಭಗವಂತನ ಆದೇಶ ಮತ್ತು ಶಿಶುರೂಪ ಧಾರಣೆ

ತಂದೆ-ತಾಯಿಯರನ್ನು ಸಮಾಧಾನಪಡಿಸಿದ ನಂತರ, ಪರಮ ಪುರುಷೋತ್ತಮ ಭಗವಾನ್ ಶ್ರೀಕೃಷ್ಣನು ತನ್ನ ಚತುರ್ಭುಜ ರೂಪವನ್ನು ಮರೆಮಾಚಿ, ಅತ್ಯಂತ ಮುದ್ದಾದ ಎರಡು ಕೈಗಳ ಸಾಮಾನ್ಯ ಮಗುವಿನ ರೂಪವನ್ನು ಧರಿಸಿದನು. ಆ ಕ್ಷಣದಲ್ಲಿ ಭಗವಂತನು ವಸುದೇವರ ಅಂತರಂಗದಲ್ಲಿ ಆದೇಶಿಸಿದನು: "ನನ್ನನ್ನು ತಕ್ಷಣ ಯಮುನಾ ನದಿಯನ್ನು ದಾಟಿಸಿ ಗೋಕುಲದ ನಂದಮಹಾರಾಜರ ಮನೆಗೆ ಕೊಂಡೊಯ್ಯಿರಿ. ಯಶೋದೆಯು ಈಗಷ್ಟೇ ಹೆಣ್ಣು ಮಗುವಿಗೆ ಜನ್ಮ ನೀಡಿದ್ದಾಳೆ. ನನ್ನನ್ನು ಆಕೆಯ ಪಕ್ಕದಲ್ಲಿ ಮಲಗಿಸಿ, ಆ ಹೆಣ್ಣು ಮಗುವನ್ನು ಎತ್ತಿಕೊಂಡು ಯಾರೂ ಎಚ್ಚರಗೊಳ್ಳುವ ಮುನ್ನ ಈ ಸೆರೆಮನೆಗೆ ಮರಳಿ ಬನ್ನಿ."

ವಸುದೇವರಲ್ಲಿ ಧೈರ್ಯ ತುಂಬಿತು, ಆದರೆ ಕಾಲಿಗೆ ಬಿದ್ದಿರುವ ಸರಪಳಿಗಳು ಮತ್ತು ಕಾವಲುಗಾರರ ನಡುವೆ ಇದು ಹೇಗೆ ಸಾಧ್ಯ ಎಂದು ಅವರು ಆಲೋಚಿಸಿದರು.

### ಯೋಗಮಾಯೆಯ ಪ್ರಭಾವ: ಸರಪಳಿಗಳು ಕಳಚಿದವು, ಬಾಗಿಲುಗಳು ತೆರೆದವು

ಆಗಲೇ ಭಗವಂತನ ಅಚಿಂತ್ಯ ಯೋಗಮಾಯಾ ಶಕ್ತಿಯಿಂದ ಮಥುರೆಯಲ್ಲಿ ಪವಾಡಗಳು ನಡೆದವು:

1. **ಎಲ್ಲರನ್ನೂ ಆವರಿಸಿದ ಗಾಢ ನಿದ್ರೆ:** ಸೆರೆಮನೆಯ ಕಾವಲುಗಾರರು, ಕಾವಲು ನಾಯಿಗಳು ಮತ್ತು ಮಥುರೆಯ ಪ್ರಜೆಗಳೆಲ್ಲರೂ ಯೋಗಮಾಯೆಯ ಪ್ರಭಾವದಿಂದ ಗಾಢ ನಿದ್ರೆಗೆ ಜಾರಿದರು.
2. **ಸರಪಳಿಗಳು ತಾವಾಗಿಯೇ ಕಳಚಿದವು:** ವಸುದೇವರು ಮಗುವನ್ನು ಎತ್ತಿಕೊಳ್ಳುತ್ತಿದ್ದಂತೆ, ಅವರ ಕೈಕಾಲುಗಳಲ್ಲಿದ್ದ ಭಾರವಾದ ಕಬ್ಬಿಣದ ಸರಪಳಿಗಳು ಸದ್ದಿಲ್ಲದೆ ಕಳಚಿ ಬಿದ್ದವು.
3. **ಬೃಹತ್ ಬಾಗಿಲುಗಳು ತೆರೆದುಕೊಂಡವು:** ಸೆರೆಮನೆಯ ಬೃಹತ್ ಕಬ್ಬಿಣದ ಬಾಗಿಲುಗಳು, ಬೀಗಗಳು ತಾವಾಗಿಯೇ ತೆರೆದುಕೊಂಡವು; ಸೂರ್ಯೋದಯಕ್ಕೆ ಕತ್ತಲೆ ಸರಿಯುವಂತೆ ದ್ವಾರಗಳು ತೆರೆದುಕೊಂಡವು.

ಬಿದಿರಿನ ಬುಟ್ಟಿಯಲ್ಲಿ ಮೃದುವಾದ ಬಟ್ಟೆಗಳನ್ನು ಹಾಸಿ, ಬಾಲಕೃಷ್ಣನನ್ನು ಅದರಲ್ಲಿ ಮಲಗಿಸಿ, ಬುಟ್ಟಿಯನ್ನು ತಲೆಯ ಮೇಲೆ ಹೊತ್ತು ವಸುದೇವರು ನಿರ್ಭಯವಾಗಿ ಕತ್ತಲೆಯಲ್ಲಿ ಹೊರಟರು.

### ಧಾರಾಕಾರ ಮಳೆ ಮತ್ತು ಆದಿಶೇಷನ ಛತ್ರ

ವಸುದೇವರು ಯಮುನಾ ತೀರಕ್ಕೆ ಸಾಗುತ್ತಿದ್ದಂತೆ ಆಕಾಶದಲ್ಲಿ ಧಾರಾಕಾರ ಮಳೆ ಸುರಿಯತೊಡಗಿತು. ಕಪ್ಪು ಮೋಡಗಳು, ಮಿಂಚು ಮತ್ತು ಗುಡುಗುಗಳಿಂದ ರಾತ್ರಿ ಭೀಕರವಾಯಿತು.

ಬಾಲಕೃಷ್ಣನನ್ನು ಮಳೆಯಿಂದ ರಕ್ಷಿಸಲು ಭಗವಂತನ ನಿತ್ಯ ಸೇವಕನಾದ ಆದಿಶೇಷನು ಪ್ರಕಟನಾದನು. ವಸುದೇವರ ಬೆನ್ನ ಹಿಂದೆ ಸಾಗುತ್ತಾ, ತನ್ನ ಅನೇಕ ಹೆಡೆಗಳನ್ನು ದೊಡ್ಡ ಛತ್ರಿಯಂತೆ ಚಾಚಿ, ಒಂದು ಹನಿ ಮಳೆನೀರೂ ಕೃಷ್ಣನ ಮೇಲೆ ಬೀಳದಂತೆ ರಕ್ಷಿಸಿದನು.

### ದಾರಿಬಿಟ್ಟ ಉಕ್ಕಿ ಹರಿಯುತ್ತಿದ್ದ ಯಮುನಾ ನದಿ

ಯಮುನಾ ತೀರಕ್ಕೆ ಬಂದಾಗ ನದಿಯು ಪ್ರವಾಹದಿಂದ ಉಕ್ಕಿ ಹರಿಯುತ್ತಿತ್ತು. ನೊರೆ ಮತ್ತು ಸುಳಿಗಳಿಂದ ಕೂಡಿದ ಆ ಭೀಕರ ನದಿಯನ್ನು ದಾಟಲು ಅಸಾಧ್ಯವೆನಿಸಿತು.

ಆದರೆ, ಭಗವಂತನನ್ನು ಹೊತ್ತು ವಸುದೇವರು ನೀರಿಗೆ ಇಳಿಯುತ್ತಿದ್ದಂತೆ ಪವಾಡ ನಡೆಯಿತು:

> **ಶ್ರೀಮದ್ಭಾಗವತ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 3, ಶ್ಲೋಕ 50**
> 
> *ಮಘೋನಿ ವರ್ಷತ್ಯಸಕೃದ್ ಯಮಾನುಜಾ*  
> *ಗಭೀರತೋಯೌಘಜವೋರ್ಮಿಫೇಣಿಲಾ |*  
> *ಭಯಾನಕಾವರ್ತಶತಾಕುಲಾ ನದೀ*  
> *ಮಾರ್ಗಂ ದದೌ ಸಿಂಧುರಿವ ಶ್ರಿಯಃ ಪತೇಃ ||*  
> 
> **ಭಾವಾರ್ಥ:** ಆಕಾಶದಿಂದ ಧಾರಾಕಾರವಾಗಿ ಮಳೆ ಸುರಿಯುತ್ತಿದ್ದಾಗ, ಆಳವಾದ ಪ್ರವಾಹ, ಅಲೆಗಳು ಮತ್ತು ಸುಳಿಗಳಿಂದ ತುಂಬಿದ್ದ ಯಮುನಾ ನದಿಯು, ಹಿಂದೆ ಶ್ರೀರಾಮಚಂದ್ರನಿಗೆ ಸಮುದ್ರವು ದಾರಿಬಿಟ್ಟಂತೆ ವಸುದೇವರಿಗೆ ದಾರಿ ಮಾಡಿಕೊಟ್ಟಿತು.

ತನ್ನ ಪ್ರಭುವಿನ ಪಾದಸ್ಪರ್ಶವಾಗುತ್ತಿದ್ದಂತೆ ಯಮುನೆಯು ಶಾಂತವಾಗಿ, ನೀರು ಸೊಂಟದ ಮಟ್ಟಕ್ಕೆ ಇಳಿದು ದಾರಿ ಮಾಡಿಕೊಟ್ಟಿತು. ವಸುದೇವರು ನೆಲದ ಮೇಲೆ ನಡೆದಂತೆ ನದಿಯನ್ನು ದಾಟಿದರು.

### ಗೋಕುಲದಲ್ಲಿ ಅದಲು-ಬದಲು

ಯಮುನೆಯನ್ನು ದಾಟಿ ವಸುದೇವರು ಗೋಕುಲದ ನಂದಮಹಾರಾಜರ ಭವನವನ್ನು ತಲುಪಿದರು. ಯೋಗಮಾಯೆಯ ಕೃಪೆಯಿಂದ ಯಾರೂ ಅವರನ್ನು ಗಮನಿಸಲಿಲ್ಲ. ಹೆರಿಗೆಯ ಆಯಾಸದಿಂದ ಯಶೋದೆಯು ಗಾಢ ನಿದ್ರೆಯಲ್ಲಿದ್ದಳು; ತನಗೆ ಗಂಡು ಮಗುವೋ ಹೆಣ್ಣು ಮಗುವೋ ಎಂದು ಆಕೆಗೆ ತಿಳಿದಿರಲಿಲ್ಲ.

ವಸುದೇವರು ಕೃಷ್ಣನನ್ನು ಯಶೋದೆಯ ಪಕ್ಕದಲ್ಲಿ ಮಲಗಿಸಿದರು. ನಂತರ ಯಶೋದೆಯ ಮಡಿಲಲ್ಲಿದ್ದ ಹೆಣ್ಣು ಮಗುವನ್ನು—ಸಾಕ್ಷಾತ್ ಯೋಗಮಾಯೆಯನ್ನು—ಎತ್ತಿಕೊಂಡು ಮೌನವಾಗಿ ಹೊರಟರು.

ಬೆಳಗಾಗುವ ಮುನ್ನವೇ ವಸುದೇವರು ಮಥುರೆಯ ಸೆರೆಮನೆಗೆ ಮರಳಿದರು. ಅವರು ಒಳಪ್ರವೇಶಿಸುತ್ತಿದ್ದಂತೆ ಬಾಗಿಲುಗಳು ಮುಚ್ಚಿಕೊಂಡು ಬೀಗ ಬಿದ್ದವು; ಸರಪಳಿಗಳು ಮತ್ತೆ ಬಂಧಿಸಿದವು. ವಸುದೇವರು ಆ ಹೆಣ್ಣು ಮಗುವನ್ನು ದೇವಕಿಯ ಮಡಿಲಲ್ಲಿಟ್ಟು ಮುಂದಿನ ಲೀಲೆಗಾಗಿ ಕಾಯತೊಡಗಿದರು.""",
                "questions": [
                    {
                        "question": "ತಂದೆ-ತಾಯಿಯರ ಜೊತೆ ಮಾತನಾಡಿದ ನಂತರ ಭಗವಂತನು ಯಾವ ರೂಪವನ್ನು ಧರಿಸಿದನು?",
                        "options": [
                            {"text": "ಎರಡು ಕೈಗಳ ಮುದ್ದಾದ ಸಾಮಾನ್ಯ ಮಗುವಿನ ರೂಪ", "is_correct": True},
                            {"text": "ನರಸಿಂಹ ರೂಪ", "is_correct": False},
                            {"text": "ಯೋಧನ ರೂಪ", "is_correct": False},
                            {"text": "ದಿವ್ಯ ಜ್ಯೋತಿ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಮಗುವನ್ನು ಎಲ್ಲಿಗೆ ಕೊಂಡೊಯ್ಯಲು ಭಗವಂತನು ಆದೇಶಿಸಿದನು?",
                        "options": [
                            {"text": "ಯಮುನೆ ದಾಟಿ ಗೋಕುಲದ ನಂದಮಹಾರಾಜರ ಮನೆಗೆ", "is_correct": True},
                            {"text": "ಹಸ್ತಿನಾಪುರಕ್ಕೆ", "is_correct": False},
                            {"text": "ಗೋವರ್ಧನ ಪರ್ವತಕ್ಕೆ", "is_correct": False},
                            {"text": "ದಂಡಕಾರಣ್ಯಕ್ಕೆ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ವಸುದೇವರು ಹೊರಡುವಾಗ ಕಾವಲುಗಾರರಿಗೆ ಏನಾಯಿತು?",
                        "options": [
                            {"text": "ಯೋಗಮಾಯೆಯ ಪ್ರಭಾವದಿಂದ ಎಲ್ಲರೂ ಗಾಢ ನಿದ್ರೆಗೆ ಜಾರಿದರು", "is_correct": True},
                            {"text": "ಮಳೆಗೆ ಹೆದರಿ ಓಡಿಹೋದರು", "is_correct": False},
                            {"text": "ಕಂಸನ ವಿರುದ್ಧ ದಂಗೆಯೆದ್ದರು", "is_correct": False},
                            {"text": "ಕಲ್ಲಾಗಿ ಹೋದರು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಸೆರೆಮನೆಯ ಸರಪಳಿಗಳು ಮತ್ತು ಬಾಗಿಲುಗಳಿಗೆ ಏನಾಯಿತು?",
                        "options": [
                            {"text": "ಸರಪಳಿಗಳು ಕಳಚಿದವು, ಬಾಗಿಲುಗಳು ತಾವಾಗಿಯೇ ತೆರೆದುಕೊಂಡವು", "is_correct": True},
                            {"text": "ವಸುದೇವರು ಕತ್ತರಿಸಿದರು", "is_correct": False},
                            {"text": "ಕಾವಲುಗಾರರು ಬೀಗ ಕೊಟ್ಟರು", "is_correct": False},
                            {"text": "ಭೂಕಂಪದಿಂದ ಮುರಿದವು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ವಸುದೇವರು ಬಾಲಕೃಷ್ಣನನ್ನು ಹೇಗೆ ಹೊತ್ತೊಯ್ದರು?",
                        "options": [
                            {"text": "ಬುಟ್ಟಿಯಲ್ಲಿ ಮಲಗಿಸಿ ತಲೆಯ ಮೇಲೆ ಹೊತ್ತು", "is_correct": True},
                            {"text": "ಚಿನ್ನದ ರಥದಲ್ಲಿ", "is_correct": False},
                            {"text": "ಕುದುರೆಯ ಮೇಲೆ", "is_correct": False},
                            {"text": "ಚೀಲದಲ್ಲಿ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಧಾರಾಕಾರ ಮಳೆಯಿಂದ ಕೃಷ್ಣನನ್ನು ರಕ್ಷಿಸಿದ್ದು ಯಾರು?",
                        "options": [
                            {"text": "ಹೆಡೆಗಳನ್ನು ಛತ್ರಿಯಂತೆ ಚಾಚಿದ ಆದಿಶೇಷ", "is_correct": True},
                            {"text": "ರೇಷ್ಮೆ ಛತ್ರಿ", "is_correct": False},
                            {"text": "ಆಲದ ಎಲೆ", "is_correct": False},
                            {"text": "ದೇವಕಿಯ ಸೀರೆ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಯಮುನೆಯು ದಾರಿಬಿಟ್ಟದ್ದನ್ನು ಭಾಗವತದಲ್ಲಿ ಯಾವುದಕ್ಕೆ ಹೋಲಿಸಲಾಗಿದೆ?",
                        "options": [
                            {"text": "ಶ್ರೀರಾಮಚಂದ್ರನಿಗೆ ಸಮುದ್ರವು ದಾರಿಬಿಟ್ಟ ಘಟನೆಗೆ", "is_correct": True},
                            {"text": "ಶಿವನ ಜಟೆಯಿಂದ ಗಂಗೆ ಇಳಿದದ್ದಕ್ಕೆ", "is_correct": False},
                            {"text": "ಸಮುದ್ರ ಮಥನಕ್ಕೆ", "is_correct": False},
                            {"text": "ಅಯೋಧ್ಯೆಯ ಪ್ರವಾಹಕ್ಕೆ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಯಶೋದೆಯು ಹೆಣ್ಣು ಮಗುವಿಗೆ ಜನ್ಮ ನೀಡಿದ್ದಾಳೆ ಎಂದು ಆಕೆಗೆ ಏಕೆ ತಿಳಿಯಲಿಲ್ಲ?",
                        "options": [
                            {"text": "ಹೆರಿಗೆಯ ಆಯಾಸ ಮತ್ತು ಯೋಗಮಾಯೆಯಿಂದ ಗಾಢ ನಿದ್ರೆಯಲ್ಲಿದ್ದಳು", "is_correct": True},
                            {"text": "ಕತ್ತಲೆಯಾಗಿದ್ದರಿಂದ", "is_correct": False},
                            {"text": "ಆಕೆ ಮನೆಯಲ್ಲಿ ಇಲ್ಲದಿದ್ದರಿಂದ", "is_correct": False},
                            {"text": "ದಾದಿಯರು ಮಗುವನ್ನು ಬಚ್ಚಿಟ್ಟಿದ್ದರಿಂದ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಯಶೋದೆಯ ಮಡಿಲಲ್ಲಿದ್ದ ಆ ಹೆಣ್ಣು ಮಗು ವಾಸ್ತವವಾಗಿ ಯಾರಾಗಿದ್ದರು?",
                        "options": [
                            {"text": "ಭಗವಂತನ ಅಂತರಂಗ ಶಕ್ತಿ ಯೋಗಮಾಯೆ", "is_correct": True},
                            {"text": "ಸ್ವರ್ಗದ ಅಪ್ಸರೆ", "is_correct": False},
                            {"text": "ಸಾಮಾನ್ಯ ಹಳ್ಳಿಯ ಹುಡುಗಿ", "is_correct": False},
                            {"text": "ಪೂತನೆ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಮಗುವಿನೊಂದಿಗೆ ವಸುದೇವರು ಮರಳಿದಾಗ ಏನಾಯಿತು?",
                        "options": [
                            {"text": "ಬಾಗಿಲುಗಳು ಮುಚ್ಚಿ ಬೀಗ ಬಿದ್ದವು, ಸರಪಳಿಗಳು ಮತ್ತೆ ಬಂಧಿಸಿದವು", "is_correct": True},
                            {"text": "ಸೆರೆಮನೆ ಕುಸಿಯಿತು", "is_correct": False},
                            {"text": "ಕಂಸನು ಕತ್ತಿ ಹಿಡಿದು ನಿಂತಿದ್ದನು", "is_correct": False},
                            {"text": "ದೇವಕಿ ತಪ್ಪಿಸಿಕೊಂಡಿದ್ದಳು", "is_correct": False}
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

        self.stdout.write(self.style.SUCCESS(f"Successfully populated Story 9 (ID: {story.id}) across all 7 languages!"))
