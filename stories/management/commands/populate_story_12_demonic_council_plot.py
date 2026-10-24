import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askharekrishna_backend.settings')
django.setup()

from django.core.management.base import BaseCommand
from stories.models import StoryMainTopic, Story, StoryTranslation, StoryQuestion, StoryQuestionOption

class Command(BaseCommand):
    help = "Populate Story 12: The Demonic Council: The Plot to Persecute Saintly Persons and Children across 7 languages"

    def handle(self, *args, **options):
        topic = StoryMainTopic.objects.get(name="Krishna Pastimes")

        story_slug = "krishna-pastimes-the-demonic-council-the-plot-to-persecute-saintly-persons-and-children"
        image_path = "stories/images/demonic_council_kamsa.jpg"

        story, created = Story.objects.get_or_create(
            slug=story_slug,
            defaults={
                "topic": topic,
                "order": 11,
                "imagePath": image_path,
            }
        )
        if not created:
            story.topic = topic
            story.order = 11
            story.imagePath = image_path
            story.save()

        stories_data = {
            "en": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "The Demonic Council: The Plot to Persecute Saintly Persons and Children",
                "content": """### The Morning Assembly of Demons

The morning after releasing Vasudeva and Devaki, King Kamsa summoned a council of his most trusted ministers, counselors, and demon warlords—figures like Pralamba, Baka, Cāṇūra, Tṛṇāvarta, and Aghāsura.

Deeply troubled and anxious, Kamsa narrated to them everything that had transpired in the dungeon courtyard: how the newborn infant girl had slipped from his hands, flown into the sky as the eight-armed Goddess Durgā, and announced that his destined slayer was already alive and thriving in another land.

Upon hearing this, Kamsa's demonic ministers, whose intelligence was blinded by passion and ignorance, burst into loud laughter. Naturally envious of the Supreme Lord, the demigods, and saintly persons, they began to boast of their invincible prowess and offered Kamsa sinister counsel.

### The Demonic Counselors Boast and Mock the Demigods

The demonic ministers flattered Kamsa and scoffed at the demigods: "O Emperor Kamsa! What reason have you to fear? The demigods are utterly powerless before our might. In the battlefield, whenever our bows twang, the demigods flee in all directions like frightened deer. 

Lord Śiva has abandoned worldly affairs and lives in the forest or cremation grounds. Lord Brahmā is merely an ascetic engaged in meditation on his lotus flower. Indra is a coward who runs in fear of our weapons. And as for Lord Viṣṇu—He is the greatest coward of all! He never fights openly in battle; instead, He hides within the dark ocean of milk, or conceals Himself within the hearts of living entities! How can such a hiding coward ever harm a mighty hero like you?"

### The Root of Lord Viṣṇu: Cows and Brāhmaṇas

The ministers then presented a thoroughly calculated, diabolical strategy to uproot Lord Viṣṇu from existence. They explained to Kamsa the spiritual secret of where the Supreme Lord's power manifests in human society:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 4, Verse 39**
> 
> *viprā gāvaś ca vedāś ca tapaḥ satyaṁ damaḥ śamaḥ*  
> *śraddhā dayā titikṣā ca kratavaś ca hares tanūḥ*  
> 
> **Translation:** "The learned brāhmaṇas, the sacred cows, the Vedic scriptures, austerity, truthfulness, sense control, mind control, faith, mercy, tolerance, and the performance of Vedic sacrifices—all these constitute the transcendental limbs and foundation of Lord Hari."

The demons reasoned: "Just as a massive tree automatically withers and dies when its roots are cut, similarly, Lord Viṣṇu will perish if we destroy His foundation! 

1. **Slaughter All Newborn Infants:** Let our soldiers roam through every village, town, and pastoral district, killing every infant boy and girl born within the last ten days!
2. **Persecute the Brāhmaṇas and Stop Sacrifices:** Let us persecute, harass, and kill the pious brāhmaṇas who study the Vedas, perform penances, and offer sacrifices to Viṣṇu. Without brāhmaṇas, no ghee will be offered into sacrificial fires.
3. **Slaughter the Sacred Cows:** The cows supply milk, butter, and ghee for sacrifices. By slaughtering the cows, the demigods and Viṣṇu will be starved of sacrificial offerings and will lose all their power!"

### Kamsa Embraces His Own Doom

Blind to truth and gripped by the fear of death, King Kamsa enthusiastically embraced this demonic advice. His temporary feelings of remorse from the previous evening evaporated completely. He commanded his demon generals and soldiers to fan out across the entire kingdom and begin a ruthless campaign of persecuting cows, brāhmaṇas, saintly persons, and newborn infants.

Śrīla Prabhupāda explains that demonic rulers in every age follow this identical pattern: whenever they feel threatened, they attack religion, kill innocent animals, and harass saintly devotees. However, Śrīmad-Bhāgavatam records the immutable cosmic law regarding such offenses:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 4, Verse 46**
> 
> *āyuḥ śriyaṁ yaśo dharmaṁ lokān āśiṣa eva ca*  
> *hanti śreyāṁsi sarvāṇi puṁso mahad-atikramaḥ*  
> 
> **Translation:** "When a person commits offenses and atrocities against great souls, saintly persons, and innocent devotees of the Lord, such offenses immediately destroy his duration of life, his beauty, his fame, his religious merit, his future destinations, and all auspicious blessings."

By launching this campaign of terror against saintly persons and innocent children, King Kamsa unknowingly sealed his own inevitable destruction, setting the stage for Lord Śrī Kṛṣṇa to vanquish his demonic reign.""",
                "questions": [
                    {
                        "question": "Whom did King Kamsa summon to council the morning after releasing Vasudeva and Devaki?",
                        "options": [
                            {"text": "His evil ministers and demon warlords such as Chanura, Pralamba, and Baka", "is_correct": True},
                            {"text": "Saintly rishis from the forest", "is_correct": False},
                            {"text": "Ambassadors from Hastinapura", "is_correct": False},
                            {"text": "Demigods from Svargaloka", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How did Kamsa's demonic ministers react to his story of Goddess Durga's warning?",
                        "options": [
                            {"text": "They scoffed with loud laughter, mocked the demigods, and offered sinister advice", "is_correct": True},
                            {"text": "They surrendered to Lord Vishnu", "is_correct": False},
                            {"text": "They fled the kingdom in fear", "is_correct": False},
                            {"text": "They advised Kamsa to become an ascetic", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How did the demonic counselors insult Lord Vishnu?",
                        "options": [
                            {"text": "They called Him a coward who hides in the ocean or within the hearts of living entities", "is_correct": True},
                            {"text": "They said He was too powerful to fight", "is_correct": False},
                            {"text": "They praised His beauty", "is_correct": False},
                            {"text": "They said He was their best friend", "is_correct": False}
                        ]
                    },
                    {
                        "question": "According to the demonic counselors, what are the roots or limbs of Lord Hari in human society?",
                        "options": [
                            {"text": "The brahmanas, sacred cows, Vedas, austerities, and Vedic sacrifices", "is_correct": True},
                            {"text": "Gold mines and weapon arsenals", "is_correct": False},
                            {"text": "Royal palaces and battle chariots", "is_correct": False},
                            {"text": "Taverns and gambling dens", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What analogy did the demonic ministers use to justify their plot?",
                        "options": [
                            {"text": "Just as a tree dies when its roots are cut, Vishnu will perish if cows and brahmanas are destroyed", "is_correct": True},
                            {"text": "Like a river joining the sea", "is_correct": False},
                            {"text": "Like birds flying south in winter", "is_correct": False},
                            {"text": "Like a pot baked in a kiln", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What ruthless order did Kamsa issue regarding newborn children?",
                        "options": [
                            {"text": "To search out and kill all children born within the last ten days throughout the kingdom", "is_correct": True},
                            {"text": "To give golden coins to every newborn child", "is_correct": False},
                            {"text": "To educate all children in archery", "is_correct": False},
                            {"text": "To send all children to Ayodhya", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Why did the demons plan to slaughter the sacred cows?",
                        "options": [
                            {"text": "To stop milk and ghee from being offered to Lord Vishnu in Vedic sacrifices", "is_correct": True},
                            {"text": "Because they had no grass to feed them", "is_correct": False},
                            {"text": "Because cows were attacking citizens", "is_correct": False},
                            {"text": "To make leather armor", "is_correct": False}
                        ]
                    },
                    {
                        "question": "According to Srimad-Bhagavatam (10.4.46), what happens to someone who persecutes saintly persons?",
                        "options": [
                            {"text": "His lifespan, beauty, fame, religious merits, and all auspiciousness are instantly ruined", "is_correct": True},
                            {"text": "He becomes an immortal emperor", "is_correct": False},
                            {"text": "He attains liberation", "is_correct": False},
                            {"text": "The demigods become his servants", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What happened to Kamsa's remorse from the previous evening?",
                        "options": [
                            {"text": "It completely evaporated under the wicked counsel of his demonic ministers", "is_correct": True},
                            {"text": "It deepened into saintly surrender", "is_correct": False},
                            {"text": "He handed his kingdom to Vasudeva", "is_correct": False},
                            {"text": "He retired to Vrindavana", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Which chapter of Srimad-Bhagavatam Canto 10 concludes with Kamsa's demonic council?",
                        "options": [
                            {"text": "Chapter 4", "is_correct": True},
                            {"text": "Chapter 2", "is_correct": False},
                            {"text": "Chapter 6", "is_correct": False},
                            {"text": "Chapter 10", "is_correct": False}
                        ]
                    }
                ]
            },
            "ta": {
                "mainTopic": "கிருஷ்ண லீலைகள்",
                "subTopic": "அசுரர்களின் சபை: சாதுக்களையும் குழந்தைகளையும் துன்புறுத்த தீட்டிய சதி",
                "content": """### அசுரர்களின் காலையரங்கு

வசுதேவர் மற்றும் தேவகியை விடுவித்த மறுநாள் காலையில், மன்னன் கம்சன் தனது நம்பிக்கைக்குரிய அசுர மந்திரிகளையும் தளபதிகளையும் அழைத்தான். பிரலம்பன், பகன், சாணூரன், திருணாவர்த்தன், அகாசுரன் போன்ற கொடூர அசுரர்கள் அந்த அவையில் கூடினர்.

தீவிர அச்சத்தோடும் கவலையோடும் கம்சன் இரவில் நடந்தவற்றை விவரித்தான்: எட்டாவது பச்சிளம் பெண் குழந்தை தனது கைகளிலிருந்து நழுவி, ஆகாயத்தில் எட்டு கரங்கள் கொண்ட துர்கா தேவியாகத் தோன்றி, தன்னைக் கொல்லும் எதிரி வேறிடத்தில் பிறந்துவிட்டதாக எச்சரித்ததை அவர்களுக்குக் கூறினான்.

இதைக் கேட்ட அசுர மந்திரிகள் பரிகாசமாக உரக்கச் சிரித்தனர். தங்களின் அறியாமையினாலும் மமதையினாலும் மதிமயங்கிய அந்த அசுரர்கள், தேவர்களையும் சாதுக்களையும் பகவானையும் இழிவாகப் பேசி, கம்சனுக்கு கொடூரமான ஆலோசனைகளைக் கூறினர்.

### தேவர்களையும் பகவானையும் ஏளனம் செய்த அசுரர்கள்

அசுர மந்திரிகள் தங்களின் அசுர பலத்தைப் புகழ்ந்துரைத்து, தேவர்களை ஏளனம் செய்தனர்: "பேரரசே கம்சா! நீர் எதைக் கண்டு அஞ்சுகிறீர்? நமது வில்லின் நாணொலி கேட்டாலே தேவர்கள் அஞ்சி நடுங்கி காடுகளுக்குள் மான்போல ஓடி ஒளிகின்றனர்!

சிவபெருமான் உலகப் பற்றை விட்டுவிட்டு சுடுகாட்டிலும் காட்டிலும் வாழ்கிறார். பிரம்மதேவர் தனது தாமரை மலரில் அமர்ந்து தவம் செய்வதிலேயே காலம் கழிக்கிறார். இந்திரனோ நமது ஆயுதங்களைக் கண்டு பயந்தோடும் கோழை. பகவான் விஷ்ணுவோ அனைவரிலும் மிகப்பெரிய கோழை! அவர் போர்க்களத்தில் நேரில் போரிடுவதில்லை; மாறாக, பாற்கடலினுள் சென்று மறைந்துகொள்கிறார், அல்லது ஜீவன்களின் இதயங்களுக்குள் ஒளிந்துகொள்கிறார்! அத்தகைய கோழையான விஷ்ணுவினால் உமக்கு என்ன தீங்கிழைக்க முடியும்?"

### பகவானின் மூலவேர்: பசுக்களும் பிராமணர்களும்

தொடர்ந்து அந்த அசுரர்கள் பகவான் விஷ்ணுவை இந்த உலகிலிருந்து வேரோடு அழிப்பதற்கான ஒரு கொடூரத் திட்டத்தை முன்வைத்தனர். மனித சமுதாயத்தில் பகவானின் திவ்ய சக்தி எங்கே வேரூன்றியுள்ளது என்பதை அவர்கள் விளக்கினர்:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 4, சுலோகம் 39**
> 
> *விப்ரா காவஶ் ச வேதாஶ் ச தப: ஸத்யம் தம: ஶம: |*  
> *ஶ்ரத்தா தயா திதிக்ஷா ச க்ரதவஶ் ச ஹரேஸ் தனூ: ||*  
> 
> **பொருள்:** "வேதம் ஓதும் பிராமணர்கள், புனிதமான பசுக்கள், வேத சாஸ்திரங்கள், தவம், வாய்மை, புலனடக்கம், மனவடக்கம், பக்தி, கருணை, பொறுமை மற்றும் யாகங்கள்—இவையனைத்தும் பகவான் ஸ்ரீ ஹரியின் திவ்ய திருமேனியின் அங்கங்களாகவும் அடித்தளமாகவும் விளங்குகின்றன."

அசுரர்கள் தர்க்கம் செய்தனர்: "ஒரு பெரிய மரத்தின் வேர்களை வெட்டினால் அம்மரம் தானாகவே காய்ந்து பட்டுப்போவது போல, விஷ்ணுவின் அடித்தளத்தை நாம் அழித்துவிட்டால் விஷ்ணு தானாகவே அழிந்துவிடுவார்!

1. **பச்சிளம் குழந்தைகளைக் கொல்வோம்:** நமது வீரர்கள் அனைத்து ஊர்களுக்கும் சென்று, கடந்த பத்து நாட்களில் பிறந்த அனைத்து ஆண், பெண் குழந்தைகளையும் ஈவுஇரக்கமின்றி கொல்லட்டும்!
2. **பிராமணர்களைத் துன்புறுத்துவோம்:** வேதம் ஓதி யாகங்கள் செய்யும் பிராமணர்களைத் துன்புறுத்திக் கொல்வோம். பிராமணர்கள் இல்லாவிட்டால் யாகத் தீயில் நெய் அர்ப்பணிக்கப்பட மாட்டாது.
3. **பசுக்களை வதைப்போம்:** யாகத்திற்குத் தேவையான பால், வெண்ணெய், நெய் ஆகியவற்றை பசுக்களே தருகின்றன. பசுக்களைக் கொன்றுவிட்டால் யாகங்கள் நின்றுபோகும்; உணவின்றி விஷ்ணுவும் தேவர்களும் பலமிழந்து மடிவார்கள்!"

### தனது அழிவைத் தானே தேடிக்கொண்ட கம்சன்

உண்மையறியாத அறிவிலியான கம்சன், மரண பயத்தினால் இந்த அசுர ஆலோசனையை ஆர்வத்தோடு ஏற்றுக்கொண்டான். முந்தைய நாள் மாலையில் அவனுக்கு ஏற்பட்ட தற்காலிக மனவருத்தம் முற்றிலுமாக மறைந்துபோனது. உடனடியாக நாடு முழுவதும் சென்று சாதுக்களையும், பசுக்களையும், பிராமணர்களையும், பச்சிளம் குழந்தைகளையும் துன்புறுத்துமாறு தனது அசுரப் படைகளுக்கு அவன் கட்டளையிட்டான்.

அசுர குணமுடைய ஆட்சியாளர்கள் ஒவ்வொரு யுகத்திலும் தங்களுக்கு ஆபத்து நேரும்போது தர்மத்தையும், பக்தர்களையும், பசுக்களையும் தாக்குவது வழக்கம் என்று ஸ்ரீல பிரபுபாதர் விளக்குகிறார். ஆனால் சாதுக்களுக்கு இழைக்கப்படும் அநீதியின் மாறாத விதியை ஸ்ரீமத் பாகவதம் எச்சரிக்கிறது:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 4, சுலோகம் 46**
> 
> *ஆயு: ஶ்ரியம் யஶோ தர்மம் லோகான் ஆஶிஷ ஏவ ச |*  
> *ஹந்தி ஶ்ரேயாம்ஸி ஸர்வாணி பும்ஸோ மஹத்-அதிக்ரம: ||*  
> 
> **பொருள்:** "ஒருவன் பகவானின் தூய பக்தர்களுக்கும், மகாத்மாக்களுக்கும், சாதுக்களுக்கும் அநீதியும் கொடுமையும் இழைக்கும்போது, அந்த அபராதம் அவனது ஆயுள், செல்வம், புகழ், தர்மம், மறுலோக நற்பேறுகள் மற்றும் அனைத்து மங்களங்களையும் உடனடியாக அடியோடு அழித்துவிடுகிறது."

சாதுக்களுக்கும் பச்சிளம் குழந்தைகளுக்கும் எதிரான இந்த அநீதியை ஏவிவிட்டதன் மூலம், கம்சன் தனது தவிர்க்க முடியாத பேரழிவை தானே உறுதி செய்துகொண்டான். பகவான் ஸ்ரீ கிருஷ்ணர் அவனது அசுர ஆட்சியை முடிவுக்குக் கொண்டுவருவதற்கான களம் தயாரானது.""",
                "questions": [
                    {
                        "question": "வசுதேவர்-தேவகியை விடுவித்த மறுநாள் காலையில் கம்சன் யாரைக் கூட்டினான்?",
                        "options": [
                            {"text": "சாணூரன், பிரலம்பன், பகன் போன்ற அசுர மந்திரிகளையும் தளபதிகளையும்", "is_correct": True},
                            {"text": "காட்டு முனிவர்களை", "is_correct": False},
                            {"text": "ஹஸ்தினாபுர தூதர்களை", "is_correct": False},
                            {"text": "தேவர்களை", "is_correct": False}
                        ]
                    },
                    {
                        "question": "துர்கா தேவியின் எச்சரிக்கையைக் கேட்ட அசுர மந்திரிகள் என்ன செய்தனர்?",
                        "options": [
                            {"text": "ஏளனமாக உரக்கச் சிரித்து, தேவர்களைப் பழித்து அசுர ஆலோசனையைக் கூறினர்", "is_correct": True},
                            {"text": "விஷ்ணுவிடம் சரணடைந்தனர்", "is_correct": False},
                            {"text": "பயந்து நாட்டை விட்டு ஓடினர்", "is_correct": False},
                            {"text": "கம்சனை தவம் செய்யச் சொன்னார்கள்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பகவான் விஷ்ணுவை அசுரர்கள் எவ்வாறு ஏளனம் செய்தனர்?",
                        "options": [
                            {"text": "நேரில் போரிடாமல் கடலிலும் இதயத்திலும் ஒளியும் கோழை என்று கூறினர்", "is_correct": True},
                            {"text": "அவரை மிகவும் பலசாலி என்றனர்", "is_correct": False},
                            {"text": "அவரது அழகைப் புகழ்ந்தனர்", "is_correct": False},
                            {"text": "அவர் தங்களின் நண்பர் என்றனர்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "அசுரர்களின் வாதப்படி பகவான் விஷ்ணுவின் மூலவேர்கள் சமுதாயத்தில் எவை?",
                        "options": [
                            {"text": "பிராமணர்கள், புனித பசுக்கள், வேதங்கள், தவம் மற்றும் யாகங்கள்", "is_correct": True},
                            {"text": "தங்கச் சுரங்கங்கள் மற்றும் ஆயுதக் கிடங்குகள்", "is_correct": False},
                            {"text": "அரண்மனைகள் மற்றும் போர்த் தேர்கள்", "is_correct": False},
                            {"text": "மதுபானக் கூடங்கள்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "தங்களின் திட்டத்தை நியாயப்படுத்த அசுரர்கள் என்ன உவமையைக் கூறினர்?",
                        "options": [
                            {"text": "மரத்தின் வேர்களை வெட்டினால் மரம் பட்டுப்போவது போல பசுக்களையும் பிராமணர்களையும் அழித்தால் விஷ்ணு அழிவார்", "is_correct": True},
                            {"text": "கடலில் கலக்கும் நதி போல", "is_correct": False},
                            {"text": "பறவைகள் பறப்பது போல", "is_correct": False},
                            {"text": "மண்பானை போல", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பச்சிளம் குழந்தைகள் குறித்து கம்சன் இட்ட கொடூர ஆணை என்ன?",
                        "options": [
                            {"text": "கடந்த பத்து நாட்களில் பிறந்த அனைத்து பச்சிளம் குழந்தைகளையும் தேடிக் கொல்ல வேண்டும்", "is_correct": True},
                            {"text": "குழந்தைகளுக்கு பொற்காசு வழங்க வேண்டும்", "is_correct": False},
                            {"text": "வில்வித்தை பயிற்றுவிக்க வேண்டும்", "is_correct": False},
                            {"text": "குழந்தைகளை அயோத்திக்கு அனுப்ப வேண்டும்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பசுக்களை வதைக்க அசுரர்கள் திட்டமிட்டதன் நோக்கம் என்ன?",
                        "options": [
                            {"text": "யாகங்களுக்குப் பயன்படும் பால், நெய் அர்ப்பணிப்பைத் தடுத்து விஷ்ணுவை பலவீனப்படுத்த", "is_correct": True},
                            {"text": "புல் இல்லாததால்", "is_correct": False},
                            {"text": "பசுக்கள் மக்களைத் தாக்கியதால்", "is_correct": False},
                            {"text": "தோல் கவசம் செய்ய", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ஸ்ரீமத் பாகவதத்தின்படி சாதுக்களுக்கு அபராதம் இழைப்பவருக்கு என்ன நேரும்?",
                        "options": [
                            {"text": "அவனது ஆயுள், செல்வம், புகழ், தர்மம் மற்றும் மங்களங்கள் அனைத்தும் உடனடியாக அழியும்", "is_correct": True},
                            {"text": "அவன் சாகா வரம் பெறுவான்", "is_correct": False},
                            {"text": "அவன் முக்தி அடைவான்", "is_correct": False},
                            {"text": "தேவர்கள் அடிமையாவார்கள்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "முந்தைய நாள் மாலையில் கம்சனுக்கு ஏற்பட்ட மனவருத்தம் என்னவானது?",
                        "options": [
                            {"text": "அசுரர்களின் தீய ஆலோசனையைக் கேட்டு முற்றிலும் ஆவியாகி மறைந்தது", "is_correct": True},
                            {"text": "பக்தியாக மாறியது", "is_correct": False},
                            {"text": "நாட்டை வசுதேவரிடம் கொடுத்தான்", "is_correct": False},
                            {"text": "பிருந்தாவனத்திற்குச் சென்றான்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "கம்சனின் அசுர சபையுடன் ஸ்ரீமத் பாகவதம் பத்தாம் ஸ்கந்தத்தில் எந்த அத்தியாயம் நிறைவடைகிறது?",
                        "options": [
                            {"text": "அத்தியாயம் 4", "is_correct": True},
                            {"text": "அத்தியாயம் 2", "is_correct": False},
                            {"text": "அத்தியாயம் 6", "is_correct": False},
                            {"text": "அத்தியாயம் 10", "is_correct": False}
                        ]
                    }
                ]
            },
            "hi": {
                "mainTopic": "कृष्ण लीलाएं",
                "subTopic": "कंस की आसुरी सभा: साधु-संतों और शिशुओं के उत्पीड़न का षड्यंत्र",
                "content": """### आसुरी सभा का आयोजन

वसुदेव और देवकी को मुक्त करने की अगली सुबह, राजा कंस ने अपने सबसे विश्वासपात्र मंत्रियों, सलाहकारों और असुर सेनापतियों की एक गुप्त सभा बुलाई। प्रलंब, बक, चाणूर, तृणावर्त और अघासुर जैसे क्रूर दैत्य उस सभा में उपस्थित हुए।

अत्यंत व्यथित और भयभीत होकर कंस ने रात्रि की संपूर्ण घटना सुनाई: कैसे वह नवजात कन्या उसके हाथों से फिसलकर आकाश में अष्टभुजा दुर्गा बन गई और उसने घोषणा की कि उसका संहारक किसी अन्य स्थान पर जन्म ले चुका है।

यह सुनकर कंस के आसुरी मंत्रियों ने अट्टहास किया। तमोगुण और रजोगुण से अंधे हुए उन दैत्यों ने देवताओं और भगवान का उपहास उड़ाया और कंस को अत्यंत कुत्सित सलाह दी।

### दैत्यों द्वारा देवताओं और भगवान विष्णु का उपहास

असुर मंत्रियों ने अपनी शक्ति का बखान करते हुए कहा: "महाराज कंस! आप व्यर्थ ही भयभीत हो रहे हैं। देवता हमारे पराक्रम के सम्मुख तिनके के समान हैं। हमारे धनुष की टंकार सुनते ही वे भयभीत मृगों की भांति भाग जाते हैं।

शिव जी श्मशान या वनों में विरक्त होकर रहते हैं। ब्रह्मा जी अपने कमल पर बैठकर केवल तपस्या में लीन रहते हैं। इंद्र तो हमारे वज्र प्रहार से डरकर भागने वाला कायर है। और जहां तक विष्णु का प्रश्न है—वह सबसे बड़ा कायर है! वह कभी आमने-सामने युद्ध नहीं करता, अपितु क्षीरसागर में छिप जाता है या प्राणियों के हृदयों में दुबक कर बैठता है! ऐसे छिपने वाले से आपको क्या भय?"

### भगवान विष्णु की जड़ें: गौ और ब्राह्मण

इसके पश्चात दैत्यों ने भगवान विष्णु को समूल नष्ट करने का एक अत्यंत धूर्त षड्यंत्र प्रस्तुत किया:

> **श्रीमद्भागवतम्, स्कंध 10, अध्याय 4, श्लोक 39**
> 
> *विप्रा गावश् च वेदाश् च तपः सत्यं दमः शमः ।*  
> *श्रद्धा दया तितिक्षा च क्रतवश् च हरेస్ तनूः ॥*  
> 
> **भावार्थ:** "वेदपाठी ब्राह्मण, पवित्र गौएं, वेद, तपस्या, सत्य, इंद्रिय-निग्रह, मनोनिग्रह, श्रद्धा, दया, क्षमा और यज्ञ—ये सभी साक्षात् भगवान श्री हरि के दिव्य अंग और आधार हैं।"

दैत्यों ने कुतर्क दिया: "जैसे किसी विशाल वृक्ष की जड़ें काट दी जाएं तो वह वृक्ष स्वतः सूखकर गिर जाता है, उसी प्रकार यदि हम विष्णु के आधार को ही नष्ट कर दें, तो विष्णु स्वतः समाप्त हो जाएगा!

1. **शिशुओं का संहार:** हमारे सैनिक राज्य के प्रत्येक गांव और नगर में जाकर पिछले दस दिनों में जन्मे सभी नवजात बालकों का वध कर दें!
2. **ब्राह्मणों का उत्पीड़न:** वेदों का अध्ययन और यज्ञ करने वाले तपस्वी ब्राह्मणों को प्रताड़ित कर मार डालें, ताकि यज्ञ बंद हो जाएं।
3. **गौ-हत्या:** यज्ञों के लिए दूध और घृत गौओं से ही प्राप्त होता है। गौओं को मार डालने से आहुतियां बंद हो जाएंगी और विष्णु तथा देवता भूख से दुर्बल होकर नष्ट हो जाएंगे!"

### कंस ने स्वयं अपने विनाश को आमंत्रित किया

मृत्यु के भय से व्याकुल मूर्ख कंस ने इस विनाशकारी आसुरी सलाह को सहर्ष स्वीकार कर लिया। पिछली संध्या का उसका सारा पश्चाताप पल भर में उड़ गया। उसने अपने सैनिकों को संपूर्ण राज्य में गौओं, ब्राह्मणों और निर्दोष शिशुओं पर अत्याचार करने की आज्ञा दे दी।

श्रील प्रभुपाद समझाते हैं कि आसुरी शासक सदैव धर्म और भक्तों पर प्रहार करते हैं। परंतु श्रीमद्भागवतम् ऐसे अपराधों के अटल परिणाम की चेतावनी देता है:

> **श्रीमद्भागवतम्, स्कंध 10, अध्याय 4, श्लोक 46**
> 
> *आयुः श्रियं यशो धर्मं लोकानाशिष एव च ।*  
> *हन्ति श्रेयांसि सर्वाणि पुंसो महदतिक्रमः ॥*  
> 
> **भावार्थ:** "जब कोई व्यक्ति भगवान के महान भक्तों, संतों और निर्दोष जीवों पर अत्याचार करता है, तो वह अपराध तुरंत उसकी आयु, ऐश्वर्य, यश, धर्म, परलोक और सभी मंगलों को समूल नष्ट कर देता है।"

इस प्रकार निर्दोष संतों और शिशुओं पर अत्याचार का आदेश देकर कंस ने अपने निश्चित विनाश की नींव रख दी।""",
                "questions": [
                    {
                        "question": "कंस ने अगली सुबह किन आसुरी मंत्रियों को बुलाया?",
                        "options": [
                            {"text": "चाणूर, प्रलंब और बक जैसे क्रूर दैत्यों को", "is_correct": True},
                            {"text": "वन के ऋषियों को", "is_correct": False},
                            {"text": "हस्तिनापुर के दूतों को", "is_correct": False},
                            {"text": "देवताओं को", "is_correct": False}
                        ]
                    },
                    {
                        "question": "दुर्गा देवी की चेतावनी सुनकर मंत्रियों की क्या प्रतिक्रिया थी?",
                        "options": [
                            {"text": "वे अट्टहास कर देवताओं का उपहास उड़ाने लगे और कुत्सित सलाह दी", "is_correct": True},
                            {"text": "उन्होंने विष्णु की शरण ली", "is_correct": False},
                            {"text": "वे राज्य छोड़कर भाग गए", "is_correct": False},
                            {"text": "कंस को तपस्या करने को कहा", "is_correct": False}
                        ]
                    },
                    {
                        "question": "दैत्यों ने भगवान विष्णु का क्या कहकर उपहास उड़ाया?",
                        "options": [
                            {"text": "कि वे क्षीरसागर या जीवों के हृदयों में छिपने वाले कायर हैं", "is_correct": True},
                            {"text": "कि वे बहुत शक्तिशाली हैं", "is_correct": False},
                            {"text": "उनकी सुंदरता की प्रशंसा की", "is_correct": False},
                            {"text": "उन्हें अपना मित्र बताया", "is_correct": False}
                        ]
                    },
                    {
                        "question": "दैत्यों के अनुसार मानव समाज में भगवान श्री हरि के आधार या अंग क्या हैं?",
                        "options": [
                            {"text": "ब्राह्मण, पवित्र गौएं, वेद, तपस्या और यज्ञ", "is_correct": True},
                            {"text": "सोने की खदानें", "is_correct": False},
                            {"text": "राजमहल और रथ", "is_correct": False},
                            {"text": "मदिरालय", "is_correct": False}
                        ]
                    },
                    {
                        "question": "दैत्यों ने अपनी योजना को सिद्ध करने के लिए क्या उपमा दी?",
                        "options": [
                            {"text": "जड़ कटने पर जैसे वृक्ष सूख जाता है, वैसे गौ और ब्राह्मणों के नाश से विष्णु नष्ट हो जाएगा", "is_correct": True},
                            {"text": "नदी के समुद्र में मिलने की", "is_correct": False},
                            {"text": "पक्षियों के उड़ने की", "is_correct": False},
                            {"text": "मिट्टी के घड़े की", "is_correct": False}
                        ]
                    },
                    {
                        "question": "कंस ने नवजात शिशुओं के संबंध में क्या क्रूर आदेश दिया?",
                        "options": [
                            {"text": "पिछले दस दिनों में जन्मे सभी शिशुओं को खोजकर मार डाला जाए", "is_correct": True},
                            {"text": "शिशुओं को स्वर्ण मुद्राएं दी जाएं", "is_correct": False},
                            {"text": "उन्हें धनुर्विद्या सिखाई जाए", "is_correct": False},
                            {"text": "उन्हें अयोध्या भेजा जाए", "is_correct": False}
                        ]
                    },
                    {
                        "question": "असुरों ने गौ-हत्या की योजना क्यों बनाई?",
                        "options": [
                            {"text": "यज्ञों में दूध और घृत की आहुतियों को रोककर विष्णु को दुर्बल करने के लिए", "is_correct": True},
                            {"text": "घास की कमी के कारण", "is_correct": False},
                            {"text": "गौएं हमला कर रही थीं", "is_correct": False},
                            {"text": "चमड़े के लिए", "is_correct": False}
                        ]
                    },
                    {
                        "question": "श्रीमद्भागवतम् (10.4.46) के अनुसार संतों पर अत्याचार करने वाले का क्या नष्ट हो जाता है?",
                        "options": [
                            {"text": "आयु, ऐश्वर्य, यश, धर्म और समस्त मंगल नष्ट हो जाते हैं", "is_correct": True},
                            {"text": "वह अमर हो जाता है", "is_correct": False},
                            {"text": "उसे मोक्ष मिल जाता है", "is_correct": False},
                            {"text": "देवता उसके दास बन जाते हैं", "is_correct": False}
                        ]
                    },
                    {
                        "question": "कंस के पिछले दिन के पश्चाताप का क्या हुआ?",
                        "options": [
                            {"text": "दुष्ट मंत्रियों की संगति से वह पूरी तरह समाप्त हो गया", "is_correct": True},
                            {"text": "वह भक्त बन गया", "is_correct": False},
                            {"text": "उसने राज्य छोड़ दिया", "is_correct": False},
                            {"text": "वह वृंदावन चला गया", "is_correct": False}
                        ]
                    },
                    {
                        "question": "श्रीमद्भागवतम् के दसवें स्कंध का कौन सा अध्याय कंस की आसुरी सभा के साथ समाप्त होता है?",
                        "options": [
                            {"text": "अध्याय 4", "is_correct": True},
                            {"text": "अध्याय 2", "is_correct": False},
                            {"text": "अध्याय 6", "is_correct": False},
                            {"text": "अध्याय 10", "is_correct": False}
                        ]
                    }
                ]
            },
            "ml": {
                "mainTopic": "കൃഷ്ണ ലീലകൾ",
                "subTopic": "അസുരസഭ: സാധുക്കളെയും കുഞ്ഞുങ്ങളെയും പീഡിപ്പിക്കാനുള്ള ഗൂഢാലോചന",
                "content": """### അസുരസഭയുടെ പ്രഭാതസമ്മേളനം

വസുദേവ-ദേവകിമാരെ മോചിപ്പിച്ചതിന്റെ പിറ്റേന്ന് രാവിലെ, കംസൻ തന്റെ വിശ്വസ്തരായ അസുരമന്ത്രിമാരെയും സേനാപതികളെയും വിളിച്ചുകൂട്ടി. പ്രലംബൻ, ബകൻ, ചാണൂരൻ, തൃണാവർത്തൻ, അഘാസുരൻ തുടങ്ങിയ ദുഷ്ടന്മാരായ അസുരന്മാർ അവിടെ ഒത്തുകൂടി.

ഭയചകിതനായ കംസൻ കാരാഗൃഹത്തിൽ നടന്നതെല്ലാം അവരോട് വിവരിച്ചു: പെൺകുഞ്ഞ് ആകാശത്തേക്ക് ഉയർന്നുപോയി അഷ്ടഭുജ ദുർഗ്ഗയായി പ്രത്യക്ഷപ്പെട്ടതും, തന്നെ വധിക്കാനുള്ളവൻ മറ്റൊരിടത്ത് വളരുന്നുവെന്ന് മുന്നറിയിപ്പ് നൽകിയതും അവൻ അറിയിച്ചു.

ഇതുകേട്ട അസുരന്മാർ ഉറക്കെ പരിഹസിച്ചു ചിരിച്ചു. അഹങ്കാരത്താൽ ബുദ്ധി നഷ്ടപ്പെട്ട അവർ കംസന് പൈശാചികമായ ഉപദേശങ്ങൾ നൽകി.

### ഭഗവാനെയും ദേവന്മാരെയും അസുരന്മാർ പരിഹസിക്കുന്നു

അസുരന്മാർ കംസനെ പ്രശംസിച്ചുകൊണ്ട് പറഞ്ഞു: "മഹാരാജാവേ! അങ്ങ് എന്തിനാണ് ഭയപ്പെടുന്നത്? നമ്മുടെ ബാണങ്ങളുടെ ശബ്ദം കേട്ടാൽത്തന്നെ ദേവന്മാർ മാനുകളെപ്പോലെ ഓടിയൊളിക്കും.

ശിവൻ ശ്മശാനത്തിലും കാട്ടിലും കഴിയുന്നു. ബ്രഹ്മാവ് താമരപ്പൂവിൽ കണ്ണടച്ചിരിക്കുന്നു. ഇന്ദ്രൻ ഭയം കാരണം ഒളിച്ചോടുന്നവനാണ്. വിഷ്ണുവാകട്ടെ, ഏറ്റവും വലിയ ഭീരുവാണ്! അവൻ ഒരിക്കലും നേർക്കുനേർ യുദ്ധം ചെയ്യാറില്ല; പകരം പാലാഴിയിലോ ജീവികളുടെ ഹൃദയങ്ങളിലോ ഒളിച്ചിരിക്കുന്നു! അങ്ങനെ ഒളിച്ചിരിക്കുന്നവനെ നാം എന്തിന് ഭയക്കണം?"

### ഭഗവാന്റെ വേരുകൾ: പശുക്കളും ബ്രാഹ്മണരും

തുടർന്ന് ഭഗവാനെ വേരോടെ പിഴുതെറിയാനുള്ള ഒരു കുടിലതന്ത്രം അസുരന്മാർ ഉപദേശിച്ചു:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അദ്ധ്യായം 4, ശ്ലോകം 39**
> 
> *വിപ്രാ ഗാവശ് ച വേദാശ് ച തപഃ സത്യം ദമഃ ശമഃ |*  
> *ശ്രദ്ധാ ദയാ തിതിക്ഷാ ച ക്രതവശ് ച ഹരേസ് തനൂഃ ||*  
> 
> **അർത്ഥം:** "വേദം പഠിക്കുന്ന ബ്രാഹ്മണർ, വിശുദ്ധ പശുക്കൾ, വേദങ്ങൾ, തപസ്സ്, സത്യം, ഇന്ദ്രിയനിഗ്രഹം, മനസ്സംയമനം, ശ്രദ്ധ, ദയ, ക്ഷമ, യജ്ഞങ്ങൾ എന്നിവയെല്ലാം സാക്ഷാൽ ശ്രീഹരിയുടെ ദിവ്യാംഗങ്ങളും അടിസ്ഥാനവുമാകുന്നു."

അസുരന്മാർ പറഞ്ഞു: "ഒരു വന്മരത്തിന്റെ വേരറുത്താൽ മരം തനിയെ ഉണങ്ങി വീഴുന്നതുപോലെ, വിഷ്ണുവിന്റെ ഈ അടിസ്ഥാനങ്ങളെ തകർത്താൽ വിഷ്ണു തനിയെ നശിക്കും!

1. **ശിശുക്കളെ വധിക്കുക:** കഴിഞ്ഞ പത്തു ദിവസങ്ങൾക്കുള്ളിൽ ജനിച്ച സകല ആൺ-പെൺ കുഞ്ഞുങ്ങളെയും നമ്മുടെ പടയാളികൾ കൊന്നൊടുക്കട്ടെ!
2. **ബ്രാഹ്മണരെ പീഡിപ്പിക്കുക:** യജ്ഞം നടത്തുന്ന ബ്രാഹ്മണരെ വധിച്ചാൽ യാഗങ്ങൾ നിലയ്ക്കും.
3. **പശുക്കളെ കൊല്ലുക:** യാഗത്തിനുള്ള നെയ്യും പാലും നൽകുന്നത് പശുക്കളാണ്. പശുക്കളെ കൊന്നാൽ ഹവിസ്സില്ലാതെ വിഷ്ണുവും ദേവന്മാരും പട്ടിണിയിലായി നശിക്കും!"

### കംസൻ സ്വന്തം നാശം ഉറപ്പുവരുത്തുന്നു

ഈ ഉപദേശം കേട്ട് മൂഢനായ കംസൻ സന്തോഷിച്ചു. തലേദിവസത്തെ പശ്ചാത്താപം പൂർണ്ണമായും ഇല്ലാതായി. അവൻ പശുക്കളെയും ബ്രാഹ്മണരെയും കുഞ്ഞുങ്ങളെയും പീഡിപ്പിക്കാൻ അസുരന്മാരോട് ആജ്ഞാപിച്ചു.

ഭക്തരെയും സാധുക്കളെയും പീഡിപ്പിക്കുന്നവരുടെ വിധി എന്താണെന്ന് ശ്രീമദ് ഭാഗവതം ഓർമ്മിപ്പിക്കുന്നു:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അദ്ധ്യായം 4, ശ്ലോകം 46**
> 
> *ആയുഃ ശ്രിയം യശോ ധർമ്മം ലോകാനാശിഷ ഏവ ച |*  
> *ഹന്തി ശ്രേയാംസി സർവ്വാണി പുംസോ മഹദതിക്രമഃ ||*  
> 
> **അർത്ഥം:** "മഹാത്മാക്കളോടും സാധുക്കളോടും ഈശ്വരഭക്തരോടും അതിക്രമം കാണിക്കുന്നവന്റെ ആയുസ്സും ഐശ്വര്യവും യശസ്സും ധർമ്മവും സകല മംഗളങ്ങളും ഉടനടി നശിച്ചുപോകുന്നു."

ഇങ്ങനെ നിരപരാധികളെ പീഡിപ്പിക്കാൻ ഉത്തരവിട്ടതിലൂടെ കംസൻ സ്വന്തം സർവ്വനാശത്തിന് അടിത്തറയിട്ടു.""",
                "questions": [
                    {
                        "question": "പിറ്റേന്ന് രാവിലെ കംസൻ ആരെയാണ് വിളിച്ചുകൂട്ടിയത്?",
                        "options": [
                            {"text": "ചാണൂരൻ, പ്രലംബൻ, ബകൻ തുടങ്ങിയ ദുഷ്ട അസുരന്മാരെ", "is_correct": True},
                            {"text": "കാട്ടിലെ മുനിമാരെ", "is_correct": False},
                            {"text": "ഹസ്തിനപുരത്തിലെ ദൂതന്മാരെ", "is_correct": False},
                            {"text": "ദേവന്മാരെ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ദുർഗ്ഗാദേവിയുടെ മുന്നറിയിപ്പ് കേട്ട് മന്ത്രിമാർ എന്തു ചെയ്തു?",
                        "options": [
                            {"text": "ഉറക്കെ ചിരിച്ച് ദേവന്മാരെ പരിഹസിക്കുകയും കുടിലതന്ത്രങ്ങൾ ഉപദേശിക്കുകയും ചെയ്തു", "is_correct": True},
                            {"text": "വിഷ്ണുവിനെ ശരണം പ്രാപിച്ചു", "is_correct": False},
                            {"text": "നാടുവിട്ടോടി", "is_correct": False},
                            {"text": "കംസനോട് തപസ്സു ചെയ്യാൻ പറഞ്ഞു", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഭഗവാൻ വിഷ്ണുവിനെ അസുരന്മാർ എങ്ങനെയാണ് പരിഹസിച്ചത്?",
                        "options": [
                            {"text": "കടലിലും ഹൃദയങ്ങളിലും ഒളിച്ചിരിക്കുന്ന ഭീരുവെന്ന് പരിഹസിച്ചു", "is_correct": True},
                            {"text": "അവൻ ശക്തനാണെന്ന് പറഞ്ഞു", "is_correct": False},
                            {"text": "സൗന്ദര്യത്തെ പുകഴ്ത്തി", "is_correct": False},
                            {"text": "സുഹൃത്താണെന്ന് പറഞ്ഞു", "is_correct": False}
                        ]
                    },
                    {
                        "question": "അസുരന്മാരുടെ അഭിപ്രായത്തിൽ സമൂഹത്തിൽ ഭഗവാന്റെ വേരുകൾ ഏവയാണ്?",
                        "options": [
                            {"text": "ബ്രാഹ്മണർ, പശുക്കൾ, വേദങ്ങൾ, തപസ്സ്, യജ്ഞങ്ങൾ", "is_correct": True},
                            {"text": "സ്വർണ്ണഖനികൾ", "is_correct": False},
                            {"text": "കൊട്ടാരങ്ങളും രഥങ്ങളും", "is_correct": False},
                            {"text": "മദ്യശാലകൾ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "തന്ത്രം ന്യായീകരിക്കാൻ അസുരന്മാർ നൽകിയ ഉപമ എന്തായിരുന്നു?",
                        "options": [
                            {"text": "വേരറുത്താൽ മരം നശിക്കുന്നതുപോലെ പശുക്കളെയും ബ്രാഹ്മണരെയും നശിപ്പിച്ചാൽ വിഷ്ണു നശിക്കും", "is_correct": True},
                            {"text": "നദി കടലിൽ ചേരുന്നതുപോലെ", "is_correct": False},
                            {"text": "പക്ഷികൾ പറക്കുന്നതുപോലെ", "is_correct": False},
                            {"text": "മൺപാത്രം പോലെ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "നവജാതശിശുക്കളെക്കുറിച്ച് കംസൻ നൽകിയ ക്രൂരമായ ഉത്തരവ് എന്തായിരുന്നു?",
                        "options": [
                            {"text": "കഴിഞ്ഞ പത്തു ദിവസത്തിനുള്ളിൽ ജനിച്ച എല്ലാ കുഞ്ഞുങ്ങളെയും കൊന്നൊടുക്കുക", "is_correct": True},
                            {"text": "കുഞ്ഞുങ്ങൾക്ക് സ്വർണ്ണം നൽകുക", "is_correct": False},
                            {"text": "വില്ലുവിദ്യ പഠിപ്പിക്കുക", "is_correct": False},
                            {"text": "അയോദ്ധ്യയിലേക്ക് അയക്കുക", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പശുക്കളെ കൊല്ലാൻ അസുരന്മാർ തീരുമാനിച്ചത് എന്തുകൊണ്ട്?",
                        "options": [
                            {"text": "യാഗത്തിനുള്ള പാലും നെയ്യും തടഞ്ഞ് വിഷ്ണുവിനെ പട്ടിണിയിലാക്കാൻ", "is_correct": True},
                            {"text": "പുല്ലില്ലാത്തതുകൊണ്ട്", "is_correct": False},
                            {"text": "പശുക്കൾ ആക്രമിച്ചതുകൊണ്ട്", "is_correct": False},
                            {"text": "തോലിനുവേണ്ടി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ശ്രീമദ് ഭാഗവതപ്രകാരം സാധുക്കളെ ഉപദ്രവിക്കുന്നവന് എന്തു സംഭവിക്കും?",
                        "options": [
                            {"text": "ആയുസ്സും ഐശ്വര്യവും യശസ്സും സകല മംഗളങ്ങളും നശിക്കും", "is_correct": True},
                            {"text": "അവൻ അമരനാകും", "is_correct": False},
                            {"text": "മോക്ഷം ലഭിക്കും", "is_correct": False},
                            {"text": "ദേവന്മാർ ദാസന്മാരാകും", "is_correct": False}
                        ]
                    },
                    {
                        "question": "കംസന്റെ തലേന്നത്തെ പശ്ചാത്താപത്തിന് എന്തു സംഭവിച്ചു?",
                        "options": [
                            {"text": "ദുഷ്ടമന്ത്രിമാരുടെ വാക്കുകൾ കേട്ട് പൂർണ്ണമായും ഇല്ലാതായി", "is_correct": True},
                            {"text": "ഭക്തിയായി മാറി", "is_correct": False},
                            {"text": "രാജ്യം ഉപേക്ഷിച്ചു", "is_correct": False},
                            {"text": "വൃന്ദാവനത്തിലേക്ക് പോയി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ശ്രീമദ് ഭാഗവതം പത്താം സ്കന്ധത്തിലെ ഏത് അദ്ധ്യായമാണ് കംസന്റെ അസുരസഭയോടെ അവസാനിക്കുന്നത്?",
                        "options": [
                            {"text": "അദ്ധ്യಾಯം 4", "is_correct": True},
                            {"text": "അദ്ധ്യായം 2", "is_correct": False},
                            {"text": "അദ്ധ്യായം 6", "is_correct": False},
                            {"text": "അദ്ധ്യായം 10", "is_correct": False}
                        ]
                    }
                ]
            },
            "bn": {
                "mainTopic": "কৃষ্ণ লীলা",
                "subTopic": "অসুর সভা: সাধু-সন্ন্যাসী ও শিশুদের নিধনের কুচক্রান্ত",
                "content": """### কংসের অসুর সভার অধিবেশন

বসুদেব ও দেবকীকে মুক্তি দেবার পরদিন প্রাতে রাজা কংস তার অতি বিশ্বস্ত মন্ত্রী ও অসুর সেনাপতিদের এক সভা আহ্বান করল। প্রলম্ব, বক, চাণূর, তৃণাবর্ত ও অঘাসুরের ন্যায় ভয়ঙ্কর অসুরেরা সেখানে সমবেত হলো।

কংস পরম উদ্বেগে রজনীর সমস্ত ঘটনা বিবৃত করল: কীভাবে নবজাত কন্যা তার হাত থেকে ফসকে আকাশে অষ্টভুজা দুর্গারূপে আবির্ভূতা হয়ে ঘোষণা করেছে যে তার সংহারকারী অন্যত্র জীবিত রয়েছে।

এ কথা শুনে কংসের তমোগুণাচ্ছন্ন অসুর মন্ত্রীরা উচ্চৈঃস্বরে উপহাস করতে লাগল। তারা দেবতাদের ও ভগবানকে অবজ্ঞা করে কংসকে এক নারকীয় পরামর্শ দিল।

### দেবতাদের ও শ্রীবিষ্ণুকে অসুরদের উপহাস

অসুরেরা নিজেদের বাহুবলের দম্ভ প্রকাশ করে বলল: "মহারাজ কংস! আপনি বৃথা ভয় পাচ্ছেন। আমাদের ধনুকের টঙ্কার শুনলেই দেবতারা ভীত হরিণের মতো পলায়ন করে।

শিব তো শ্মশানে বা বনে সন্ন্যাসী হয়ে থাকেন। ব্রহ্মা পদ্মের ওপর বসে ধ্যানমগ্ন। ইন্দ্র আমাদের ভয়ে পলায়নপর এক কাপুরুষ। আর বিষ্ণুর কথা কি বলব—সে তো সবচেয়ে বড় কাপুরুষ! সে কখনো মুখোমুখি যুদ্ধ করে না; সে ক্ষীরোদসাগরে লুকিয়ে থাকে অথবা জীবের হৃদয়ে বাস করে! এমন গোপনকারীকে কি ভয় পাওয়ার কিছু আছে?"

### শ্রীহরির মূল ভিত্তি: গো ও ব্রাহ্মণ

এরপর অসুরেরা শ্রীবিষ্ণুর অস্তিত্বকে সমূলে বিনষ্ট করার এক কুটিল পরিকল্পনা উপস্থাপন করল:

> **শ্রীমদ্ভাগবত, স্কন্ধ ১০, অধ্যায় ৪, শ্লোক ৩৯**
> 
> *বিপ্রা গাবশ্চ বেদাশ্চ তপঃ সত্যং দমঃ শমঃ ।*  
> *শ্রদ্ধা দয়া তিতিক্ষা চ ক্রতবশ্চ হরেস্তনুঃ ॥*  
> 
> **অনুবাদ:** "বেদজ্ঞ ব্রাহ্মণ, পবিত্র গাভী, বেদসমূহ, তপস্যা, সত্য, ইন্দ্রিয়সংযম, মনের স্থিরতা, শ্রদ্ধা, দয়া, ক্ষমা ও যজ্ঞানুষ্ঠান—এই সমস্তই শ্রীহরির চিন্ময় অঙ্গ ও ভিত্তি।"

অসুরেরা যুক্তি দিল: "যেমন বৃক্ষের মূলচ্ছেদ করলে বিশাল বৃক্ষও শুকিয়ে মরে যায়, তদ্রূপ বিষ্ণুর এই ভিত্তিকে ধ্বংস করলে বিষ্ণু আপনা থেকেই বিনষ্ট হবে!

১. **নবজাতকদের সংহার:** আমাদের সৈন্যরা রাজ্যে গত দশ দিনে জন্মগ্রহণকারী সমস্ত শিশুকে হত্যা করুক!
২. **ব্রাহ্মণদের নিধন:** যজ্ঞকারী ব্রাহ্মণদের হত্যা করলে যজ্ঞ বন্ধ হয়ে যাবে।
৩. **গো-হত্যা:** যজ্ঞের ঘৃত ও দুগ্ধ গাভী প্রদান করে। গাভী হত্যা করলে যজ্ঞে কোনো আহুতি দেওয়া যাবে না এবং অনাহারে বিষ্ণু ও দেবতারা ধ্বংস হয়ে যাবে!"

### কংসের স্বীয় ধ্বংসের পথ বরণ

ভয়ার্ত কংস পরম উল্লাসে এই আসুরিক প্রস্তাব গ্রহণ করল। পূর্বরাত্রির তার সমস্ত অনুশোচনা কর্পূরের মতো উবে গেল। সে রাজ্যে সাধু, গাভী, ব্রাহ্মণ ও শিশুদের ওপর নির্মম অত্যাচার চালানোর নির্দেশ দিল।

শ্রীমদ্ভাগবত সাধু ও নিরপরাধের ওপর অত্যাচারের অমোঘ ফলের বিষয়ে সাবধান করে:

> **শ্রীমদ্ভাগবত, স্কন্ধ ১০, অধ্যায় ৪, শ্লোক ৪৬**
> 
> *আয়ুঃ শ্রিয়ং যশো ধর্মং লোকানাশিষ এব চ ।*  
> *হন্তি শ্রেয়াংসি সর্বাণি পুংসো মহদতিক্রমঃ ॥*  
> 
> **অনুবাদ:** "যখন কোনো ব্যক্তি ভগবানের মহান ভক্ত, সাধু ও নিষ্পাপ প্রাণীর ওপর অত্যাচার করে, তখন সেই অপরাধ তৎক্ষণাৎ তার আয়ু, ঐশ্বর্য, যশ, ধর্ম ও সমস্ত মঙ্গলকে সমূলে বিনাশ করে।"

এই পৈশাচিক আদেশের মাধ্যমে কংস তার নিজের অনিবার্য ধ্বংসের পথ সুনিশ্চিত করল।""",
                "questions": [
                    {
                        "question": "পরদিন সকালে কংস কাদের নিয়ে সভা ডেকেছিল?",
                        "options": [
                            {"text": "চাণূর, প্রলম্ব ও বকের মতো অসুর মন্ত্রীদের", "is_correct": True},
                            {"text": "বনের ঋষিদের", "is_correct": False},
                            {"text": "হস্তিনাপুরের দূতদের", "is_correct": False},
                            {"text": "দেবতাদের", "is_correct": False}
                        ]
                    },
                    {
                        "question": "দেবী দুর্গার সাবধানবাণী শুনে অসুরেরা কি করেছিল?",
                        "options": [
                            {"text": "উপহাস করে দেবতাদের অবজ্ঞা করেছিল এবং কুটিল পরামর্শ দিয়েছিল", "is_correct": True},
                            {"text": "বিষ্ণুর শরণাপন্ন হয়েছিল", "is_correct": False},
                            {"text": "রাজ্য ছেড়ে পালিয়েছিল", "is_correct": False},
                            {"text": "কংসকে সাধু হতে বলেছিল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "অসুরেরা ভগবান বিষ্ণুকে কি বলে উপহাস করেছিল?",
                        "options": [
                            {"text": "সাগরে বা হৃদয়ে লুকিয়ে থাকা কাপুরুষ", "is_correct": True},
                            {"text": "অতি পরাক্রমশালী", "is_correct": False},
                            {"text": "রূপবান", "is_correct": False},
                            {"text": "তাদের পরম বন্ধু", "is_correct": False}
                        ]
                    },
                    {
                        "question": "অসুরদের মতে সমাজে শ্রীহরির মূল ভিত্তি কি?",
                        "options": [
                            {"text": "ব্রাহ্মণ, গাভী, বেদ, তপস্যা ও যজ্ঞ", "is_correct": True},
                            {"text": "সোনার খনি", "is_correct": False},
                            {"text": "অস্ত্রাগার ও রথ", "is_correct": False},
                            {"text": "মদ্যশালা", "is_correct": False}
                        ]
                    },
                    {
                        "question": "পরিকল্পনা বোঝাতে অসুরেরা কি উপমা দিয়েছিল?",
                        "options": [
                            {"text": "মূল কাটলে যেমন গাছ মরে যায়, তেমনি গাভী ও ব্রাহ্মণ ধ্বংস হলে বিষ্ণু মরবে", "is_correct": True},
                            {"text": "নদী সাগরে মেশার মতো", "is_correct": False},
                            {"text": "পাখি ওড়ার মতো", "is_correct": False},
                            {"text": "মাটির পাত্রের মতো", "is_correct": False}
                        ]
                    },
                    {
                        "question": "নবজাতকদের বিষয়ে কংস কি আদেশ দিয়েছিল?",
                        "options": [
                            {"text": "গত দশ দিনে জন্ম নেওয়া সকল শিশুকে খুঁজে হত্যা করা", "is_correct": True},
                            {"text": "স্বর্ণমুদ্রা উপহার দেওয়া", "is_correct": False},
                            {"text": "ধনুুর্বিদ্যা শেখানো", "is_correct": False},
                            {"text": "অযোধ্যায় পাঠানো", "is_correct": False}
                        ]
                    },
                    {
                        "question": "অসুরেরা কেন গো-হত্যার পরিকল্পনা করেছিল?",
                        "options": [
                            {"text": "যজ্ঞের দুধ ও ঘি বন্ধ করে বিষ্ণুকে অনাহারে দুর্বল করতে", "is_correct": True},
                            {"text": "ঘাসের অভাব ছিল বলে", "is_correct": False},
                            {"text": "গাভী আক্রমণ করছিল বলে", "is_correct": False},
                            {"text": "চামড়ার জন্য", "is_correct": False}
                        ]
                    },
                    {
                        "question": "শ্রীমদ্ভাগবত (১০.৪.৪৬) অনুসারে সাধুদের ওপর অত্যাচার করলে কি ঘটে?",
                        "options": [
                            {"text": "আয়ু, ঐশ্বর্য, যশ, ধর্ম ও সকল মঙ্গল তৎক্ষণাৎ বিনষ্ট হয়", "is_correct": True},
                            {"text": "অমরত্ব লাভ হয়", "is_correct": False},
                            {"text": "মোক্ষ লাভ হয়", "is_correct": False},
                            {"text": "দেবতারা দাস হয়", "is_correct": False}
                        ]
                    },
                    {
                        "question": "কংসের পূর্বরাত্রির অনুশোচনার কি হলো?",
                        "options": [
                            {"text": "অসুরদের কুসঙ্গের প্রভাবে তা সম্পূর্ণ মিলিয়ে গেল", "is_correct": True},
                            {"text": "ভক্তিভাবে পরিণত হলো", "is_correct": False},
                            {"text": "রাজ্য ত্যাগ করল", "is_correct": False},
                            {"text": "বৃন্দাবনে গেল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "শ্রীমদ্ভাগবতের দশম স্কন্ধের কোন অধ্যায় কংসের অসুর সভার সাথে সমাপ্ত হয়?",
                        "options": [
                            {"text": "অধ্যায় ৪", "is_correct": True},
                            {"text": "অধ্যায় ২", "is_correct": False},
                            {"text": "অধ্যায় ৬", "is_correct": False},
                            {"text": "অধ্যায় ১০", "is_correct": False}
                        ]
                    }
                ]
            },
            "te": {
                "mainTopic": "కృష్ణ లీలలు",
                "subTopic": "అసుర సభ: సాధువులను, పసిపిల్లలను హింసించేందుకు పన్నిన కుట్ర",
                "content": """### ఉదయపు అసుర సభ

వసుదేవ దేవకీలను విడిపించిన మరుసటి రోజు ఉదయం, కంసరాజు తన నమ్మకమైన మంత్రులను, సేనాపతులను పిలిపించాడు. ప్రలంబ, బక, చాణూర, తృణావర్త, అఘాసురుడు వంటి భయంకర రాక్షసులు అక్కడ సమావేశమయ్యారు.

రాత్రి జరిగిన వింతను కంసుడు తీవ్ర ఆందోళనతో వారికి వివరించాడు: ఆ పసిపాప తన చేతుల నుండి జారి ఆకాశంలో అష్టభుజ దుర్గాదేవిగా మారి, తనను సంహరించే శత్రువు వేరొకచోట క్షేమంగా ఉన్నాడని చెప్పిన విషయాన్ని తెలిపాడు.

అది విన్న అసురులు బిగ్గరగా నవ్వారు. అహంకారంతో కళ్ళు మూసుకుపోయిన వారు దేవతలను, భగవంతుని నిందిస్తూ కంసునికి దుష్ట సలహాలు ఇచ్చారు.

### భగవంతుని, దేవతలను అసురులు పరిహసించుట

అసురులు తమ బలాన్ని పొగుడుకుంటూ ఇలా అన్నారు: "మహారాజా! మీరెందుకు భయపడుతున్నారు? మన వింటి నారి మోత వింటేనే దేవతలు జింకల్లా పారిపోతారు.

శివుడు అడవులలో, శ్మశానాలలో విరక్తుడై ఉంటాడు. బ్రహ్మ కమలంలో కళ్ళు మూసుకుని తపస్సు చేసుకుంటాడు. ఇంద్రుడు పిరికివాడు. ఇక విష్ణువైతే అందరికంటే పిరికివాడు! ఆయన ఎదురుపడి యుద్ధం చేయడు; పాలకడలిలోనో, ప్రాణుల హృదయాలలోనో దాక్కుంటాడు! అలా దాక్కునేవాడికి మనమంటే ఎందుకు భయం ఉండదు?"

### విష్ణువు యొక్క మూలాలు: గోవులు మరియు బ్రాహ్మణులు

అనంతరం విష్ణువును సమూలంగా నాశనం చేయడానికి రాక్షసులు ఒక కుట్రను పన్నారు:

> **శ్రీమద్భాగవతం, స్కంధం 10, అధ్యాయం 4, శ్లోకం 39**
> 
> *విప్రా గావశ్ చ వేదాశ్ చ తపః సత్యం దమః శమః |*  
> *శ్రద్ధా దయా తితిక్షా చ క్రతవశ్ చ హరేస్ తనూః ||*  
> 
> **తాత్పర్యం:** "వేదపఠనం చేసే బ్రాహ్మణులు, పవిత్ర గోవులు, వేదాలు, తపస్సు, సత్యం, ఇంద్రియ నిగ్రహం, మనోనిగ్రహం, శ్రద్ధ, దయ, క్షమ, యజ్ఞాలు—ఇవన్నీ సాక్షాత్తు శ్రీహరి యొక్క దివ్య శరీర అంగాలు మరియు మూలములు."

రాక్షసులు ఇలా చెప్పారు: "చెట్టు వేర్లు నరికితే చెట్టు ఎండిపోయినట్లే, విష్ణువుకు ఆధారమైన వీటిని నాశనం చేస్తే విష్ణువు వాటంతట తానే నశిస్తాడు!

1. **శిశువుల సంహారం:** మన సైనికులు గత పది రోజులలో జన్మించిన సకల పసిపిల్లలను వెతికి చంపాలి!
2. **బ్రాహ్మణుల హింస:** యజ్ఞాలు చేసే బ్రాహ్మణులను చంపితే యజ్ఞాలు ఆగిపోతాయి.
3. **గోవధ:** యజ్ఞాలకు అవసరమైన నెయ్యి, పాలు గోవులే ఇస్తాయి. గోవులను చంపేస్తే హవిస్సులు లేక విష్ణువు, దేవతలు బలహీనులై నశిస్తారు!"

### తన వినాశనాన్ని తానే కోరి తెచ్చుకున్న కంసుడు

మరణ భయంతో ఉన్న మూర్ఖ కంసుడు ఈ దుష్ట సలహాను ఉత్సాహంగా అంగీకరించాడు. నిన్నటి అతని పశ్చాత్తాపమంతా ఆవిరైపోయింది. గోవులను, బ్రాహ్మణులను, పసిపిల్లలను హింసించాలని సైన్యానికి ఆజ్ఞాపించాడు.

భాగవతం దీని పర్యవసానాన్ని ఇలా హెచ్చరిస్తోంది:

> **శ్రీమద్భాగవతం, స్కంధం 10, అధ్యాయం 4, శ్లోకం 46**
> 
> *ఆయుః శ్రియం యశో ధర్మం లోకానాశిష ఏవ చ |*  
> *హంతి శ్రేయాంసి సర్వాణి పుంసో మహదతిక్రమః ||*  
> 
> **తాత్పర్యం:** "మహాత్ములను, భగవద్భక్తులను, అమాయక జీవులను హింసించేవాని ఆయువు, సంపద, యశస్సు, ధర్మం మరియు సమస్త శుభాలు తక్షణమే నాశనమవుతాయి."

ఈ విధంగా కంసుడు సాధువులను, పసిపిల్లలను హింసించమని ఆజ్ఞాపించి తన సర్వనాశనానికి తానే నాంది పలికాడు.""",
                "questions": [
                    {
                        "question": "మరుసటి రోజు ఉదయం కంసుడు ఎవరిని పిలిపించాడు?",
                        "options": [
                            {"text": "చాణూర, ప్రలంబ, బక వంటి క్రూర అసురులను", "is_correct": True},
                            {"text": "అడవిలోని మునులను", "is_correct": False},
                            {"text": "హస్తినాపుర దూతలను", "is_correct": False},
                            {"text": "దేవతలను", "is_correct": False}
                        ]
                    },
                    {
                        "question": "దుర్గాదేవి హెచ్చరిక విన్న మంత్రుల స్పందన ఏమిటి?",
                        "options": [
                            {"text": "నవ్వి దేవతలను పరిహసించి కుట్ర పన్నారు", "is_correct": True},
                            {"text": "విష్ణువును శరణు వేడారు", "is_correct": False},
                            {"text": "రాజ్యం విడిచి పారిపోయారు", "is_correct": False},
                            {"text": "కంసుడిని తపస్సు చేయమన్నారు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "విష్ణువును రాక్షసులు ఎలా ఎగతాళి చేశారు?",
                        "options": [
                            {"text": "సముద్రంలో లేదా హృదయాలలో దాక్కునే పిరికివాడని", "is_correct": True},
                            {"text": "శక్తిమంతుడని", "is_correct": False},
                            {"text": "అందగాడని", "is_correct": False},
                            {"text": "స్నేహితుడని", "is_correct": False}
                        ]
                    },
                    {
                        "question": "రాక్షసుల ప్రకారం సమాజంలో శ్రీహరి మూలాలు ఏవి?",
                        "options": [
                            {"text": "బ్రాహ్మణులు, గోవులు, వేదాలు, తపస్సు, యజ్ఞాలు", "is_correct": True},
                            {"text": "బంగారు గనులు", "is_correct": False},
                            {"text": "భవనాలు మరియు రథాలు", "is_correct": False},
                            {"text": "మద్యం దుకాణాలు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "తమ పథకాన్ని సమర్థించడానికి రాక్షసులు ఏ ఉపమానం చెప్పారు?",
                        "options": [
                            {"text": "వేర్లు నరికితే చెట్టు చనిపోయినట్లు గోవులు, బ్రాహ్మణులను నాశనం చేస్తే విష్ణువు నశిస్తాడు", "is_correct": True},
                            {"text": "నది సముద్రంలో కలవడం లాంటిది", "is_correct": False},
                            {"text": "పక్షులు ఎగరడం", "is_correct": False},
                            {"text": "కుండ పగలడం", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పసిపిల్లల గురించి కంసుడు ఇచ్చిన క్రూరమైన ఆజ్ఞ ఏమిటి?",
                        "options": [
                            {"text": "గత పది రోజులలో పుట్టిన పిల్లలందరినీ చంపడం", "is_correct": True},
                            {"text": "బంగారు నాణేలు ఇవ్వడం", "is_correct": False},
                            {"text": "విలువిద్య నేర్పడం", "is_correct": False},
                            {"text": "అయోధ్యకు పంపడం", "is_correct": False}
                        ]
                    },
                    {
                        "question": "గోవులను చంపాలని రాక్షసులు ఎందుకు నిర్ణయించారు?",
                        "options": [
                            {"text": "యజ్ఞాలకు పాలు, నెయ్యి అందకుండా విష్ణువును బలహీనపరచడానికి", "is_correct": True},
                            {"text": "గడ్డి లేక", "is_correct": False},
                            {"text": "గోవులు దాడి చేశాయని", "is_correct": False},
                            {"text": "చర్మం కోసం", "is_correct": False}
                        ]
                    },
                    {
                        "question": "శ్రీమద్భాగవతం (10.4.46) ప్రకారం సాధువులను హింసించేవానికి ఏమవుతుంది?",
                        "options": [
                            {"text": "ఆయువు, సంపద, యశస్సు, ధర్మం అన్నీ తక్షణమే నశిస్తాయి", "is_correct": True},
                            {"text": "అమరుడవుతాడు", "is_correct": False},
                            {"text": "మోక్షం వస్తుంది", "is_correct": False},
                            {"text": "దేవతలు బానిసలవుతారు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "కంసుని మునుపటి రోజు పశ్చాత్తాపం ఏమైంది?",
                        "options": [
                            {"text": "దుష్ట మంత్రుల మాటలతో పూర్తిగా ఆవిరైపోయింది", "is_correct": True},
                            {"text": "భక్తిగా మారింది", "is_correct": False},
                            {"text": "రాజ్యాన్ని విడిచాడు", "is_correct": False},
                            {"text": "బృందావనానికి వెళ్ళాడు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "శ్రీమద్భాగవతంలో పదవ స్కంధంలో ఏ అధ్యాయం కంసుని అసుర సభతో ముగుస్తుంది?",
                        "options": [
                            {"text": "అధ్యాయం 4", "is_correct": True},
                            {"text": "అధ్యాయం 2", "is_correct": False},
                            {"text": "అధ్యాయం 6", "is_correct": False},
                            {"text": "అధ్యాయం 10", "is_correct": False}
                        ]
                    }
                ]
            },
            "kn": {
                "mainTopic": "ಕೃಷ್ಣ ಲೀಲೆಗಳು",
                "subTopic": "ಅಸುರ ಸಭೆ: ಸಾಧು-ಸಂತರನ್ನು ಮತ್ತು ಶಿಶುಗಳನ್ನು ಹಿಂಸಿಸುವ ದುಷ್ಟ ಸಂಚು",
                "content": """### ಅಸುರ ಸಭೆಯ ಪ್ರಭಾತ ಸಮ್ಮೇಳನ

ವಸುದೇವ ಮತ್ತು ದೇವಕಿಯರನ್ನು ಬಿಡುಗಡೆ ಮಾಡಿದ ಮರುದಿನ ಮುಂಜಾನೆ, ರಾಜ ಕಂಸನು ತನ್ನ ನಂಬಿಕಸ್ಥ ಮಂತ್ರಿಗಳನ್ನು ಮತ್ತು ಅಸುರ ಸೇನಾಪತಿಗಳನ್ನು ಕರೆಸಿದನು. ಪ್ರಲಂಬ, ಬಕ, ಚಾಣೂರ, ತೃಣಾವರ್ತ ಮತ್ತು ಅಘಾಸುರನಂತಹ ಘೋರ ಅಸುರರು ಅಲ್ಲಿ ಸೇರಿದರು.

ತೀವ್ರ ಆತಂಕದಿಂದ ಕಂಸನು ರಾತ್ರಿ ನಡೆದ ಘಟನೆಯನ್ನು ವಿವರಿಸಿದನು: ಆ ಹೆಣ್ಣು ಮಗುವು ಕೈಯಿಂದ ಜಾರಿ ಆಕಾಶದಲ್ಲಿ ಅಷ್ಟಭುಜ ದುರ್ಗಾದೇವಿಯಾಗಿ ನಿಂತು, ತನ್ನನ್ನು ಕೊಲ್ಲುವ ಶತ್ರುವು ಬೇರೆಲ್ಲಿಯೋ ಜೀವಂತವಾಗಿದ್ದಾನೆ ಎಂದು ಎಚ್ಚರಿಸಿದ ವಿಷಯವನ್ನು ತಿಳಿಸಿದನು.

ಇದನ್ನು ಕೇಳಿದ ಅಸುರ ಮಂತ್ರಿಗಳು ಗಟ್ಟಿಯಾಗಿ ನಕ್ಕರು. ಅಹಂಕಾರದಿಂದ ಕಣ್ಣು ಕಾಣದ ಆ ರಾಕ್ಷಸರು ದೇವತೆಗಳನ್ನು, ಭಗವಂತನನ್ನು ಹೀಯಾಳಿಸಿ ಕಂಸನಿಗೆ ದುಷ್ಟ ಸಲಹೆಯನ್ನು ನೀಡಿದರು.

### ಭಗವಂತ ಮತ್ತು ದೇವತೆಗಳನ್ನು ಹೀಯಾಳಿಸಿದ ಅಸುರರು

ಅಸುರರು ತಮ್ಮ ಭುಜಬಲವನ್ನು ಹೊಗಳಿಕೊಳ್ಳುತ್ತಾ ಹೇಳಿದರು: "ಮಹಾರಾಜ ಕಂಸನೇ! ನೀವೇಕೆ ಹೆದರುತ್ತೀರಿ? ನಮ್ಮ ಬಿಲ್ಲುಗಳ ಶಬ್ದ ಕೇಳಿದರೆ ಸಾಕು ದೇವತೆಗಳು ಜಿಂಕೆಗಳಂತೆ ಓಡಿಹೋಗುತ್ತಾರೆ.

ಶಿವನು ಕಾಡಿನಲ್ಲಿ ಅಥವಾ ಸ್ಮಶಾನದಲ್ಲಿ ವಿರಕ್ತನಾಗಿರುತ್ತಾನೆ. ಬ್ರಹ್ಮನು ಕಮಲದಲ್ಲಿ ಕಣ್ಣುಮುಚ್ಚಿ ತಪಸ್ಸಿನಲ್ಲಿರುತ್ತಾನೆ. ಇಂದ್ರನು ಹೆದರಿ ಓಡುವ ಹೇಡಿ. ಇನ್ನು ವಿಷ್ಣುವಂತೂ ಎಲ್ಲರಿಗಿಂತ ದೊಡ್ಡ ಹೇಡಿ! ಆತನು ಮುಖಾಮುಖಿ ಯುದ್ಧ ಮಾಡದೆ ಕ್ಷೀರಸಾಗರದಲ್ಲೋ ಅಥವಾ ಜೀವಿಗಳ ಹೃದಯದಲ್ಲೋ ಅಡಗಿಕೊಳ್ಳುತ್ತಾನೆ! ಅಂತಹ ಹೇಡಿಯಿಂದ ನಿಮಗೇನು ಭಯ?"

### ಶ್ರೀಹರಿಯ ಮೂಲಗಳು: ಗೋವುಗಳು ಮತ್ತು ಬ್ರಾಹ್ಮಣರು

ನಂತರ ವಿಷ್ಣುವನ್ನು ಬುಡಸಮೇತ ಕಿತ್ತೊಗೆಯಲು ಅಸುರರು ಒಂದು ಕುತಂತ್ರವನ್ನು ರೂಪಿಸಿದರು:

> **ಶ್ರೀಮದ್ಭಾಗವತ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 4, ಶ್ಲೋಕ 39**
> 
> *ವಿಪ್ರಾ ಗಾವಶ್ಚ ವೇದಾಶ್ಚ ತಪಃ ಸತ್ಯಂ ದಮಃ ಶಮಃ |*  
> *ಶ್ರದ್ಧಾ ದಯಾ ತಿತಿಕ್ಷಾ ಚ ಕ್ರತವಶ್ಚ ಹರೇಸ್ತನೂಃ ||*  
> 
> **ಭಾವಾರ್ಥ:** "ವೇದಾಧ್ಯಯನ ಮಾಡುವ ಬ್ರಾಹ್ಮಣರು, ಪವಿತ್ರ ಗೋವುಗಳು, ವೇದಗಳು, ತಪಸ್ಸು, ಸತ್ಯ, ಇಂದ್ರಿಯನಿಗ್ರಹ, ಮನೋನಿಗ್ರಹ, ಶ್ರದ್ಧೆ, ದಯೆ, ಕ್ಷಮೆ ಮತ್ತು ಯಜ್ಞಗಳು—ಇವೆಲ್ಲವೂ ಸಾಕ್ಷಾತ್ ಶ್ರೀಹರಿಯ ದಿವ್ಯ ಶರೀರದ ಅಂಗಗಳು ಮತ್ತು ಅಡಿಪಾಯ."

ಅಸುರರು ವಾದಿಸಿದರು: "ಮರದ ಬೇರುಗಳನ್ನು ಕಡಿದರೆ ಮರವು ಒಣಗಿ ಬೀಳುವಂತೆ, ವಿಷ್ಣುವಿನ ಈ ಅಡಿಪಾಯವನ್ನು ನಾಶಮಾಡಿದರೆ ವಿಷ್ಣುವು ತಾನಾಗಿಯೇ ನಾಶವಾಗುತ್ತಾನೆ!

1. **ಶಿಶುಗಳ ಹತ್ಯೆ:** ನಮ್ಮ ಸೈನಿಕರು ಕಳೆದ ಹತ್ತು ದಿನಗಳಲ್ಲಿ ಜನಿಸಿದ ಸಕಲ ಹಸುಗೂಸುಗಳನ್ನು ಹುಡುಕಿ ಕೊಲ್ಲಲಿ!
2. **ಬ್ರಾಹ್ಮಣರ ಹಿಂಸೆ:** ಯಜ್ಞಗಳನ್ನು ಮಾಡುವ ಬ್ರಾಹ್ಮಣರನ್ನು ಕೊಂದರೆ ಯಜ್ಞಗಳು ನಿಲ್ಲುತ್ತವೆ.
3. **ಗೋಹತ್ಯೆ:** ಯಜ್ಞಕ್ಕೆ ಹಾಲು, ತುಪ್ಪವನ್ನು ಗೋವುಗಳೇ ನೀಡುತ್ತವೆ. ಗೋವುಗಳನ್ನು ಕೊಂದರೆ ಹವಿಸ್ಸಿಲ್ಲದೆ ವಿಷ್ಣು ಮತ್ತು ದೇವತೆಗಳು ಹಸಿವಿನಿಂದ ಸಾಯುತ್ತಾರೆ!"

### ತನ್ನ ವಿನಾಶವನ್ನು ತಾನೇ ಬರಮಾಡಿಕೊಂಡ ಕಂಸ

ಮೃತ್ಯುಭಯದಲ್ಲಿದ್ದ ಮೂಢ ಕಂಸನು ಈ ದುಷ್ಟ ಸಲಹೆಯನ್ನು ಸಂತೋಷದಿಂದ ಒಪ್ಪಿಕೊಂಡನು. ಹಿಂದಿನ ಸಂಜೆಯ ಆತನ ಪಶ್ಚಾತ್ತಾಪವೆಲ್ಲವೂ ಕರಗಿಹೋಯಿತು. ರಾಜ್ಯಾದ್ಯಂತ ಗೋವುಗಳು, ಬ್ರಾಹ್ಮಣರು ಮತ್ತು ಶಿಶುಗಳನ್ನು ಹಿಂಸಿಸಲು ಸೈನ್ಯಕ್ಕೆ ಆಜ್ಞಾಪಿಸಿದನು.

ಭಾಗವತವು ಇಂತಹ ಅಪರಾಧಗಳ ಅಂತಿಮ ಫಲವನ್ನು ಹೀಗೆ ಎಚ್ಚರಿಸುತ್ತದೆ:

> **ಶ್ರೀಮದ್ಭಾಗವತ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 4, ಶ್ಲೋಕ 46**
> 
> *ಆಯುಃ ಶ್ರಿಯಂ ಯಶೋ ಧರ್ಮಂ ಲೋಕಾನಾಶಿಷ ಏವ ಚ |*  
> *ಹಂತಿ ಶ್ರೇಯಾಂಸಿ ಸರ್ವಾಣಿ ಪುಂಸೋ ಮಹದತಿಕ್ರಮಃ ||*  
> 
> **ಭಾವಾರ್ಥ:** "ಮಹಾತ್ಮರು, ಸಾಧುಗಳು ಮತ್ತು ಭಗವದ್ಭಕ್ತರನ್ನು ಪೀಡಿಸುವವನ ಆಯುಷ್ಯ, ಸಂಪತ್ತು, ಕೀರ್ತಿ, ಧರ್ಮ ಮತ್ತು ಸಕಲ ಮಂಗಳಗಳು ತಕ್ಷಣವೇ ನಾಶವಾಗುತ್ತವೆ."

ಹೀಗೆ ಮುಗ್ಧ ಸಾಧು-ಸಂತರನ್ನು ಮತ್ತು ಶಿಶುಗಳನ್ನು ಹಿಂಸಿಸಲು ಆಜ್ಞೆ ನೀಡುವ ಮೂಲಕ ಕಂಸನು ತನ್ನ ಸರ್ವನಾಶಕ್ಕೆ ತಾನೇ ನಾಂದಿ ಹಾಡಿದನು.""",
                "questions": [
                    {
                        "question": "ಮರುದಿನ ಮುಂಜಾನೆ ಕಂಸನು ಯಾರನ್ನು ಕರೆಸಿದನು?",
                        "options": [
                            {"text": "ಚಾಣೂರ, ಪ್ರಲಂಬ, ಬಕರಂತಹ ಅಸುರ ಮಂತ್ರಿಗಳನ್ನು", "is_correct": True},
                            {"text": "ಕಾಡಿನ ಮುನಿಗಳನ್ನು", "is_correct": False},
                            {"text": "ಹಸ್ತಿನಾಪುರದ ದೂತರನ್ನು", "is_correct": False},
                            {"text": "ದೇವತೆಗಳನ್ನು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ದುರ್ಗಾದೇವಿಯ ಎಚ್ಚರಿಕೆ ಕೇಳಿ ಅಸುರ ಮಂತ್ರಿಗಳು ಏನು ಮಾಡಿದರು?",
                        "options": [
                            {"text": "ನಕ್ಕು ದೇವತೆಗಳನ್ನು ಹೀಯಾಳಿಸಿ ದುಷ್ಟ ಸಲಹೆ ನೀಡಿದರು", "is_correct": True},
                            {"text": "ವಿಷ್ಣುವಿನ ಶರಣು ಹೋದರು", "is_correct": False},
                            {"text": "ರಾಜ್ಯ ಬಿಟ್ಟು ಓಡಿದರು", "is_correct": False},
                            {"text": "ಕಂಸನಿಗೆ ತಪಸ್ಸು ಮಾಡಲು ಹೇಳಿದರು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ವಿಷ್ಣುವನ್ನು ಅಸುರರು ಹೇಗೆ ಗೇಲಿ ಮಾಡಿದರು?",
                        "options": [
                            {"text": "ಸಮುದ್ರದಲ್ಲೋ ಅಥವಾ ಹೃದಯದಲ್ಲೋ ಅಡಗಿಕೊಳ್ಳುವ ಹೇಡಿ ಎಂದು", "is_correct": True},
                            {"text": "ಬಹಳ ಶಕ್ತಿಶಾಲಿ ಎಂದು", "is_correct": False},
                            {"text": "ಸೌಂದರ್ಯವನ್ನು ಹೊಗಳಿದರು", "is_correct": False},
                            {"text": "ತಮ್ಮ ಮಿತ್ರ ಎಂದು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಅಸುರರ ಪ್ರಕಾರ ಸಮಾಜದಲ್ಲಿ ಶ್ರೀಹರಿಯ ಮೂಲಗಳು ಯಾವುವು?",
                        "options": [
                            {"text": "ಬ್ರಾಹ್ಮಣರು, ಗೋವುಗಳು, ವೇದಗಳು, ತಪಸ್ಸು, ಯಜ್ಞಗಳು", "is_correct": True},
                            {"text": "ಚಿನ್ನದ ಗಣಿಗಳು", "is_correct": False},
                            {"text": "ಅರಮನೆಗಳು ಮತ್ತು ರಥಗಳು", "is_correct": False},
                            {"text": "ಮದ್ಯದ ಅಂಗಡಿಗಳು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ತಮ್ಮ ಸಂಚನ್ನು ಸಮರ್ಥಿಸಲು ಅಸುರರು ಯಾವ ಉಪಮೆ ನೀಡಿದರು?",
                        "options": [
                            {"text": "ಬೇರು ಕಡಿದರೆ ಮರ ಒಣಗುವಂತೆ ಗೋವುಗಳು, ಬ್ರಾಹ್ಮಣರನ್ನು ನಾಶಮಾಡಿದರೆ ವಿಷ್ಣು ನಾಶವಾಗುತ್ತಾನೆ", "is_correct": True},
                            {"text": "ನದಿ ಸಮುದ್ರ ಸೇರುವಂತೆ", "is_correct": False},
                            {"text": "ಪಕ್ಷಿಗಳು ಹಾರುವಂತೆ", "is_correct": False},
                            {"text": "ಮಡಕೆ ಒಡೆಯುವಂತೆ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ನವಜಾತ ಶಿಶುಗಳ ಬಗ್ಗೆ ಕಂಸನು ನೀಡಿದ ಕ್ರೂರ ಆಜ್ಞೆಯೇನು?",
                        "options": [
                            {"text": "ಕಳೆದ ಹತ್ತು ದಿನಗಳಲ್ಲಿ ಜನಿಸಿದ ಸಕಲ ಮಕ್ಕಳನ್ನು ಕೊಲ್ಲುವುದು", "is_correct": True},
                            {"text": "ಚಿನ್ನದ ನಾಣ್ಯ ನೀಡುವುದು", "is_correct": False},
                            {"text": "ಬಿಲ್ಲುಗಾರಿಕೆ ಕಲಿಸುವುದು", "is_correct": False},
                            {"text": "ಅಯೋಧ್ಯೆಗೆ ಕಳುಹಿಸುವುದು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಗೋವುಗಳನ್ನು ಕೊಲ್ಲಲು ಅಸುರರು ಏಕೆ ಯೋಜಿಸಿದರು?",
                        "options": [
                            {"text": "ಯಜ್ಞಕ್ಕೆ ಹಾಲು, ತುಪ್ಪ ಸಿಗದಂತೆ ಮಾಡಿ ವಿಷ್ಣುವನ್ನು ಹಸಿವಿನಿಂದ ಕೊಲ್ಲಲು", "is_correct": True},
                            {"text": "ಹುಲ್ಲು ಇಲ್ಲದ್ದರಿಂದ", "is_correct": False},
                            {"text": "ಗೋವುಗಳು ದಾಳಿ ಮಾಡಿದ್ದರಿಂದ", "is_correct": False},
                            {"text": "ಚರ್ಮಕ್ಕಾಗಿ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಶ್ರೀಮದ್ಭಾಗವತದ (10.4.46) ಪ್ರಕಾರ ಸಾಧುಗಳನ್ನು ಪೀಡಿಸುವವನಿಗೆ ಏನಾಗುತ್ತದೆ?",
                        "options": [
                            {"text": "ಆಯುಷ್ಯ, ಸಂಪತ್ತು, ಕೀರ್ತಿ, ಧರ್ಮ ಎಲ್ಲವೂ ತಕ್ಷಣ ನಾಶವಾಗುತ್ತವೆ", "is_correct": True},
                            {"text": "ಅಮರನಾಗುತ್ತಾನೆ", "is_correct": False},
                            {"text": "ಮೋಕ್ಷ ಸಿಗುತ್ತದೆ", "is_correct": False},
                            {"text": "ದೇವತೆಗಳು ದಾಸರಾಗುತ್ತಾರೆ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಕಂಸನ ಹಿಂದಿನ ದಿನದ ಪಶ್ಚಾತ್ತಾಪಕ್ಕೆ ಏನಾಯಿತು?",
                        "options": [
                            {"text": "ದುಷ್ಟ ಮಂತ್ರಿಗಳ ಮಾತಿನಿಂದ ಸಂಪೂರ್ಣವಾಗಿ ಕರಗಿಹೋಯಿತು", "is_correct": True},
                            {"text": "ಭಕ್ತಿಯಾಗಿ ಬದಲಾಯಿತು", "is_correct": False},
                            {"text": "ರಾಜ್ಯ ತ್ಯಜಿಸಿದನು", "is_correct": False},
                            {"text": "ಬೃಂದಾವನಕ್ಕೆ ಹೋದನು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಶ್ರೀಮದ್ಭಾಗವತದ ಹತ್ತನೇ ಸ್ಕಂಧದ ಯಾವ ಅಧ್ಯಾಯವು ಕಂಸನ ಅಸುರ ಸಭೆಯೊಂದಿಗೆ ಮುಕ್ತಾಯವಾಗುತ್ತದೆ?",
                        "options": [
                            {"text": "ಅಧ್ಯಾಯ 4", "is_correct": True},
                            {"text": "ಅಧ್ಯಾಯ 2", "is_correct": False},
                            {"text": "ಅಧ್ಯಾಯ 6", "is_correct": False},
                            {"text": "ಅಧ್ಯಾಯ 10", "is_correct": False}
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

        self.stdout.write(self.style.SUCCESS(f"Successfully populated Story 12 (ID: {story.id}) across all 7 languages!"))
