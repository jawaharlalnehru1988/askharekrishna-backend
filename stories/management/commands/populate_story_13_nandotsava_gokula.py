import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askharekrishna_backend.settings')
django.setup()

from django.core.management.base import BaseCommand
from stories.models import StoryMainTopic, Story, StoryTranslation, StoryQuestion, StoryQuestionOption

class Command(BaseCommand):
    help = "Populate Story 13: Nandotsava: The Grand Festival in Gokula across 7 languages"

    def handle(self, *args, **options):
        topic = StoryMainTopic.objects.get(name="Krishna Pastimes")

        story_slug = "krishna-pastimes-nandotsava-the-grand-festival-in-gokula"
        image_path = "stories/images/nandotsava_gokula.jpg"

        story, created = Story.objects.get_or_create(
            slug=story_slug,
            defaults={
                "topic": topic,
                "order": 12,
                "imagePath": image_path,
            }
        )
        if not created:
            story.topic = topic
            story.order = 12
            story.imagePath = image_path
            story.save()

        stories_data = {
            "en": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "Nandotsava: The Grand Festival in Gokula",
                "content": """### Transcendental Joy Awakens in Gokula

When dawn broke over the pastoral village of Gokula, Mother Yashoda awakened to find a radiant, beautiful baby boy nestled beside her on the bed. His complexion was like a fresh, dark monsoon cloud, His eyes resembled blooming lotus petals, and His face radiated a divine, celestial innocence. 

Seeing the newborn son, Nanda Maharaja’s heart surged with boundless transcendental joy. For many years, Nanda and Yashoda had prayed and yearned for a son. Now, in their advanced age, their greatest desire had been fulfilled. The news spread like wild wildfire from house to house throughout the cowherd community: "A son has been born to Nanda Maharaja and Yashoda!"

Immediately, the entire pastoral settlement of Gokula was transformed into a realm of celebration and jubilant festivity known as **Nandotsava**.

### Nanda Maharaja's Magnanimous Charity

Nanda Maharaja, being naturally magnanimous and saintly, immediately prepared to perform the purificatory birth rites for his beloved child:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 5, Verses 1–3**
> 
> *nandas tv ātmaja utpanne jātāhlādo mahā-manāḥ*  
> *āhūya viprān veda-jñān snātaḥ śucir alaṅkṛtaḥ*  
> *vācayitvā svasty-ayanaṁ kārayām āsa jātakam*  
> 
> **Translation:** "Nanda Maharaja was naturally very magnanimous, and upon the birth of his son he was overwhelmed with transcendental bliss. Purifying himself with a sacred bath and dressing in clean, auspicious garments, he summoned learned brāhmaṇas who knew the Vedic rituals to chant auspicious hymns and perform the Vedic birth ceremony (*jātakarman*)."

To invoke blessings upon the child, Nanda Maharaja donated two hundred thousand well-decorated cows to the brāhmaṇas. The cows' horns were enveloped in gold leaf, their hooves were adorned with brass, and their backs were covered with silken cloths embroidered with pearls and jewels. In addition, Nanda distributed mountains of grains, golden ornaments, and fine garments to the brāhmaṇas, musicians, singers, and bards.

### The Gopīs Rush to See Baby Krishna

Hearing of the prince's birth, the cowherd women of Vrindavana—the gopīs—became restless with love. Putting aside all household chores, they dressed themselves in gorgeous silken saris of vivid hues, draped their long braids with fresh jasmine flowers, and adorned themselves with shimmering golden necklaces, earrings, and ankle-bells that jingled with every joyful step.

Carrying golden plates filled with auspicious gifts—fresh butter, yogurt, fragrant turmeric, yellow gorocanā, and betel nuts—they hastened toward Nanda Maharaja’s courtyard. Gazing upon the divine child, the gopīs showered Him with heartfelt blessings: "May this jewel of a child live for millions of years and protect all the cows and inhabitants of Gokula!"

### The Playful Splashing of Butter and Curd

The cowherd men (*gopas*), dressed in jewel-studded turbans and fine silk dhutis, brought gifts of fresh milk, thickened cream, and earthen pots of butter to honor Nanda Maharaja. Overwhelmed by unrestrained spiritual ecstasy, the celebration erupted into playful, joyous revelry:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 5, Verse 14**
> 
> *dadhi-kṣīra-ghṛta-kṣodaiḥ sikto ’nyonyaṁ vilepanaiḥ*  
> *cikṣipus tarasā gopā dadhi-bhaṇḍāny udīrayan*  
> 
> **Translation:** "The cowherd men, overwhelmed with jubilation, playfully threw yogurt, milk, ghee, and water mixed with turmeric upon one another. They broke clay pots filled with curd and smeared these auspicious substances all over each other in ecstatic celebration."

Clay pots of churned yogurt and butter were overturned in joy. The men and boys splashed fragrant yellow turmeric water, threw lumps of white butter, and smeared sweetened milk upon one another until the entire courtyard flowed like an ocean of milk and butter. Musicians joyfully played *mṛdaṅga* drums, clay kettledrums, horns, and flutes, while professional dancers danced in celebration.

Mother Yashoda and Mother Rohini generously distributed costly gifts, jewels, and silken garments to all who arrived, satisfying every living entity. Thus, by the supreme presence of Lord Śrī Kṛṣṇa, Gokula became eternally endowed with all transcendental opulences, beauty, and auspiciousness.""",
                "questions": [
                    {
                        "question": "What great news spread throughout Gokula on the morning after Krishna's descent?",
                        "options": [
                            {"text": "A son has been born to Nanda Maharaja and Mother Yashoda", "is_correct": True},
                            {"text": "A new king has taken over Mathura", "is_correct": False},
                            {"text": "A gold mine was discovered in Gokula", "is_correct": False},
                            {"text": "A great flood had destroyed the pastures", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What is the traditional name of the joyous festival celebrating the birth of Lord Krishna in Gokula?",
                        "options": [
                            {"text": "Nandotsava", "is_correct": True},
                            {"text": "Rathayatra", "is_correct": False},
                            {"text": "Govardhana Puja", "is_correct": False},
                            {"text": "Holi", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What Vedic purificatory ceremony did Nanda Maharaja perform for baby Krishna?",
                        "options": [
                            {"text": "Jatakarman (the Vedic birth ceremony)", "is_correct": True},
                            {"text": "Upanayana (sacred thread ceremony)", "is_correct": False},
                            {"text": "Vivaha (marriage ceremony)", "is_correct": False},
                            {"text": "Sannyasa", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How many decorated cows did Nanda Maharaja donate to the brahmanas?",
                        "options": [
                            {"text": "200,000 decorated cows", "is_correct": True},
                            {"text": "Only 10 cows", "is_correct": False},
                            {"text": "500 cows", "is_correct": False},
                            {"text": "1,000 cows", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How were the donated cows decorated for the ceremony?",
                        "options": [
                            {"text": "With horns covered in gold leaf, brass hooves, and pearl-embroidered silk cloths", "is_correct": True},
                            {"text": "With iron chains", "is_correct": False},
                            {"text": "With leather ropes", "is_correct": False},
                            {"text": "With peacock feathers only", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What auspicious gifts did the gopis bring on golden plates to see baby Krishna?",
                        "options": [
                            {"text": "Fresh butter, yogurt, fragrant turmeric, and yellow gorocana", "is_correct": True},
                            {"text": "Weapons and armor", "is_correct": False},
                            {"text": "Wine and meat", "is_correct": False},
                            {"text": "Gold coins from Mathura", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What blessing did the gopis shower upon baby Krishna?",
                        "options": [
                            {"text": "May this child live for millions of years and protect all the cows and inhabitants of Gokula", "is_correct": True},
                            {"text": "May He conquer the whole world by military force", "is_correct": False},
                            {"text": "May He become the richest merchant", "is_correct": False},
                            {"text": "May He leave Gokula and never return", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What playful activity did the cowherd men (gopas) engage in during the festival?",
                        "options": [
                            {"text": "They playfully threw yogurt, milk, butter, and turmeric water upon one another", "is_correct": True},
                            {"text": "They had a fierce duel with swords", "is_correct": False},
                            {"text": "They gambled with dice", "is_correct": False},
                            {"text": "They slept all day", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Who helped Mother Yashoda generously distribute gifts and ornaments to all visitors?",
                        "options": [
                            {"text": "Mother Rohini (mother of Balarama)", "is_correct": True},
                            {"text": "Devaki", "is_correct": False},
                            {"text": "Kunti", "is_correct": False},
                            {"text": "Gandhari", "is_correct": False}
                        ]
                    },
                    {
                        "question": "In which chapter of Srimad-Bhagavatam Canto 10 is the Nandotsava festival described?",
                        "options": [
                            {"text": "Chapter 5", "is_correct": True},
                            {"text": "Chapter 1", "is_correct": False},
                            {"text": "Chapter 3", "is_correct": False},
                            {"text": "Chapter 8", "is_correct": False}
                        ]
                    }
                ]
            },
            "ta": {
                "mainTopic": "கிருஷ்ண லீலைகள்",
                "subTopic": "நந்தோத்ஸவம்: கோகுலத்தில் நிகழ்ந்த மாபெரும் திருவிழா",
                "content": """### கோகுலத்தில் விடிந்த திவ்ய ஆனந்தம்

கோகுலத்தின் ஆயர்பாடியில் அதிகாலை விடிந்தபோது, அன்னை யசோதை விழித்தெழுந்து தனது படுக்கையில் பேரழகு வாய்ந்த ஒரு பச்சிளம் ஆண் குழந்தையைக் கண்டாள். அக்குழந்தையின் திருமேனி புது கார்மேகம் போல சியாமள வர்ணத்திலும், கண்கள் விரிந்த தாமரை மலர் போலவும், திருமுகம் திவ்ய வசீகரத்தோடும் காட்சியளித்தது.

தனக்குப் பிறந்த புதல்வனைக் கண்ட நந்த மகாராஜாவின் உள்ளத்தில் எல்லையற்ற பரமானந்தம் அலைமோதியது. பல ஆண்டுகளாக நந்தரும் யசோதையும் ஒரு புதல்வனுக்காக ஏங்கித் தவம் புரிந்தவர்கள். இப்போது, முதிர்ந்த வயதில் தங்களின் வாழ்நாள் பெருவிருப்பம் நிறைவேறியதைக் கண்டு ஆனந்தக் கண்ணீர் வடித்தனர். "நந்த மகாராஜாவுக்கும் யசோதைக்கும் ஓர் அழகான ஆண் குழந்தை பிறந்துள்ளது!" என்ற செய்தி காட்டுத்தீ போல கோகுலத்தின் வீடுதோறும் பரவியது.

உடனே கோகுலமே பரவசக் கடலில் மூழ்கியது. அந்த மாபெரும் மங்களகரமான திருவிழா **நந்தோத்ஸவம்** என்று அழைக்கப்படுகிறது.

### நந்த மகாராஜாவின் அளப்பரிய தானங்கள்

இயற்கையிலேயே பெருந்தன்மையும் தர்ம சிந்தனையும் கொண்ட நந்த மகாராஜா, தனது அருமைப் புதல்வனுக்கு ஜாதகர்மம் எனும் மங்களகரமான வேத சடங்குகளைச் செய்யத் தொடங்கினார்:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 5, சுலோகங்கள் 1–3**
> 
> *நந்தஸ் த்வாத்மஜ உத்பன்னே ஜாதாஹ்லாதோ மஹா-மனா: |*  
> *ஆஹூய விப்ரான் வேத-ஜ்ஞான் ஸ்னாத: ஶுசிர் அலங்க்ருத: |*  
> *வாசயித்வா ஸ்வஸ்த்யயனம் காரயாமாஸ ஜாதகம் ||*  
> 
> **பொருள்:** "புதல்வன் அவதரித்ததைக் கண்டு, பெருந்தன்மை கொண்ட நந்த மகாராஜா எல்லையற்ற திவ்ய ஆனந்தத்தில் மூழ்கினார். புனித நீராடி, தூய மங்களகரமான ஆடைகளை அணிந்து, வேதங்களை நன்கு உணர்ந்த பிராமணர்களை அழைத்து, மங்கள சுலோகங்களை ஓதச் செய்து, பிறப்பு சடங்கான ஜாதகர்மத்தை முறையாகச் செய்தார்."

குழந்தைக்கு சகல மங்களங்களும் உண்டாக வேண்டி, நந்த மகாராஜா இரண்டு லட்சம் அலங்கரிக்கப்பட்ட கறவை பசுக்களை பிராமணர்களுக்கு தானமாக வழங்கினார். அப்பசுக்களின் கொம்புகள் தங்கத் தகடுகளாலும், குளம்புகள் பித்தளையாலும், உடல்கள் முத்துக்கள் பதிக்கப்பட்ட பட்டாடைகளாலும் அலங்கரிக்கப்பட்டிருந்தன. அத்துடன் மலைபோன்ற தானியக் குவியல்களையும், தங்க நகைகளையும், பட்டாடைகளையும் பிராமணர்களுக்கும், பாடகர்களுக்கும், ஏழைகளுக்கும் மனமுவந்து வழங்கினார்.

### குழந்தை கிருஷ்ணரைக் காண விரைந்த கோபியர்கள்

இளவரசன் அவதரித்த நற்செய்தியைக் கேட்ட பிருந்தாவனத்தின் இடைப் பெண்கள் (கோபியர்கள்), எல்லையற்ற பக்தியினாலும் வாத்ஸல்ய பாசத்தினாலும் பரவசமடைந்தனர். வீட்டு வேலைகளை அப்படியே போட்டுவிட்டு, வண்ண வண்ண பட்டுப் புடவைகளை உடுத்தி, தங்களின் கூந்தலில் மல்லிகைப் பூக்களைச் சூடி, பொன் நகைகளையும் மணி மாலைகளையும் அணிந்து விரைந்தனர்.

தங்கத் தட்டுகளில் மங்களப் பொருட்களான புது வெண்ணெய், தயிர், மஞ்சள், ரோசனை, வெற்றிலை பாக்குகளை ஏந்தியபடி, கால் சிலம்புகள் ஒலிக்க நந்தரின் திருமாளிகையை நோக்கி ஓடி வந்தனர். அந்த திவ்ய குழந்தையைக் கண்டு உள்ளம் உருகிய கோபியர்கள், "இந்த பாலன் கோடிக்கணக்கான ஆண்டுகள் வாழ்ந்து கோகுலத்தின் அனைத்து பசுக்களையும் ஆயர்களையும் காத்தருள வேண்டும்!" என்று மனமார ஆசீர்வதித்தனர்.

### வெண்ணெய் மற்றும் தயிரை வாரி இறைத்து ஆனந்தக் கூத்து

தலையில் மாணிக்கங்கள் பதித்த தலைப்பாகைகளையும் பட்டு ஆடைகளையும் அணிந்த இடைச் சிறுவர்களும் பெரியவர்களும் (கோபர்கள்), மண்பாண்டங்களில் பாலைக் காய்ச்சி, புது வெண்ணெயையும் தயிரையும் சுமந்து கொண்டு நந்தரின் முற்றத்தில் கூடினர். அவர்களின் எல்லையற்ற ஆனந்தம் ஒரு திவ்ய விளையாட்டுத் திருவிழாவாக வெடித்தது:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 5, சுலோகம் 14**
> 
> *ததி-க்ஷீர-க்ருத-க்ஷோதை: ஸிக்தோ ‘ன்யோன்யம் விலேபனை: |*  
> *சிக்ஷிபுஸ் தரஸா கோபா ததி-பாண்டான்யுதீரயன் ||*  
> 
> **பொருள்:** "மகிழ்ச்சி வெள்ளத்தில் திளைத்த கோபர்கள், தயிர், பால், நெய் மற்றும் மஞ்சள் கலந்த நறுமண நீரை ஒருவர் மீது ஒருவர் ஆவலோடு வாரி இறைத்தனர். தயிர்ப் பானைகளை உடைத்து, அந்த மங்களப் பொருட்களை ஒருவர் மீது ஒருவர் பூசி ஆனந்தக் கூத்தாடினர்."

தயிர் பானைகளும் வெண்ணெய் பானைகளும் மகிழ்ச்சியில் தலைகீழாகக் கவிழ்க்கப்பட்டன. இடைச் சிறுவர்கள் மஞ்சள் கலந்த நீரை பீய்ச்சியடித்தனர்; வெண்ணெய் உருண்டைகளை ஒருவர் மீது ஒருவர் வீசி எறிந்தனர். அந்த முற்றமே பால் கடலாகவும் வெண்ணெய் ஆறாகவும் மாறியது. மிருதங்கம், கொம்பு, புல்லாங்குழல் இன்னிசைகள் முழங்க, நடனக் கலைஞர்கள் பரவச நடனமாடினர்.

அன்னை யசோதையும், அன்னை ரோகிணியும் வந்திருந்த அனைவருக்கும் நவரத்தினங்களையும் பட்டு ஆடைகளையும் தானமாக வாரி வழங்கினர். இவ்வாறு முழுமுதற் கடவுளான பகவான் ஸ்ரீ கிருஷ்ணரின் வருகையினால் கோகுலம் சகல மங்களங்களும், அழகும், செல்வமும் நிறைந்த திவ்ய பூமியாக விளங்கியது.""",
                "questions": [
                    {
                        "question": "கிருஷ்ணரின் வருகைக்குப் பின் கோகுலத்தில் விடிந்த காலையில் பரவிய நற்செய்தி என்ன?",
                        "options": [
                            {"text": "நந்த மகாராஜாவுக்கும் அன்னை யசோதைக்கும் ஓர் ஆண் குழந்தை பிறந்துள்ளது", "is_correct": True},
                            {"text": "மதுராவில் புதிய மன்னன் முடிசூடினான்", "is_correct": False},
                            {"text": "கோகுலத்தில் தங்கச் சுரங்கம் கண்டறியப்பட்டது", "is_correct": False},
                            {"text": "வெள்ளப்பெருக்கு ஏற்பட்டது", "is_correct": False}
                        ]
                    },
                    {
                        "question": "கோகுலத்தில் ஸ்ரீ கிருஷ்ணரின் பிறப்பைக் கொண்டாடிய மாபெரும் திருவிழாவின் பெயர் என்ன?",
                        "options": [
                            {"text": "நந்தோத்ஸவம்", "is_correct": True},
                            {"text": "ரத யாத்திரை", "is_correct": False},
                            {"text": "கோவர்த்தன பூஜை", "is_correct": False},
                            {"text": "ஹோலி", "is_correct": False}
                        ]
                    },
                    {
                        "question": "குழந்தை கிருஷ்ணருக்கு நந்த மகாராஜா செய்த வேத சடங்கு எது?",
                        "options": [
                            {"text": "ஜாதகர்மம் (பிறப்பு சடங்கு)", "is_correct": True},
                            {"text": "உபநயனம் (பூணூல் சடங்கு)", "is_correct": False},
                            {"text": "விவாஹம்", "is_correct": False},
                            {"text": "சந்நியாசம்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "நந்த மகாராஜா பிராமணர்களுக்கு எத்தனை பசுக்களை தானமாக வழங்கினார்?",
                        "options": [
                            {"text": "2,00,000 அலங்கரிக்கப்பட்ட கறவை பசுக்கள்", "is_correct": True},
                            {"text": "10 பசுக்கள் மட்டும்", "is_correct": False},
                            {"text": "500 பசுக்கள்", "is_correct": False},
                            {"text": "1,000 பசுக்கள்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "தானமாக வழங்கப்பட்ட பசுக்கள் எவ்வாறு அலங்கரிக்கப்பட்டிருந்தன?",
                        "options": [
                            {"text": "தங்க முலாம் பூசப்பட்ட கொம்புகள், பித்தளை குளம்புகள், முத்து பதித்த பட்டு ஆடைகள்", "is_correct": True},
                            {"text": "இரும்பு சங்கிலிகளால்", "is_correct": False},
                            {"text": "தோல் கயிறுகளால்", "is_correct": False},
                            {"text": "மயில் இறகுகளால் மட்டும்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "குழந்தை கிருஷ்ணரைக் காண வந்த கோபியர்கள் தங்கத் தட்டுகளில் என்ன மங்களப் பொருட்களை ஏந்தி வந்தனர்?",
                        "options": [
                            {"text": "புதிய வெண்ணெய், தயிர், மஞ்சள் மற்றும் ரோசனை", "is_correct": True},
                            {"text": "ஆயுதங்கள்", "is_correct": False},
                            {"text": "மது மற்றும் மாமிசம்", "is_correct": False},
                            {"text": "மதுரா பொற்காசுகள்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "குழந்தை கிருஷ்ணருக்கு கோபியர்கள் வழங்கிய உன்னத ஆசி என்ன?",
                        "options": [
                            {"text": "இக்குழந்தை பல கோடி ஆண்டுகள் வாழ்ந்து கோகுலத்தின் பசுக்களையும் ஆயர்களையும் காக்க வேண்டும்", "is_correct": True},
                            {"text": "படையெடுத்து உலகை வெல்ல வேண்டும்", "is_correct": False},
                            {"text": "பெரிய வணிகராக வேண்டும்", "is_correct": False},
                            {"text": "கோகுலத்தை விட்டு உடனே வெளியேற வேண்டும்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "திருவிழாவின்போது இடைச் சிறுவர்களும் ஆண்களும் என்ன விளையாட்டு விளையாடினர்?",
                        "options": [
                            {"text": "தயிர், பால், வெண்ணெய், மஞ்சள் நீரை ஒருவர் மீது ஒருவர் வாரி இறைத்து ஆனந்தக் கூத்தாடினர்", "is_correct": True},
                            {"text": "வாள் சண்டை போட்டனர்", "is_correct": False},
                            {"text": "சூதாடினர்", "is_correct": False},
                            {"text": "நாள் முழுவதும் உறங்கினர்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "வந்திருந்த அனைவருக்கும் நகைகளையும் ஆடைகளையும் தானமாக வழங்க அன்னை யசோதைக்கு உதவியவர் யார்?",
                        "options": [
                            {"text": "அன்னை ரோகிணி (பலராமரின் தாய்)", "is_correct": True},
                            {"text": "தேவகி", "is_correct": False},
                            {"text": "குந்தி", "is_correct": False},
                            {"text": "காந்தாரி", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ஸ்ரீமத் பாகவதம் பத்தாம் ஸ்கந்தத்தில் நந்தோத்ஸவம் எந்த அத்தியாயத்தில் விவரிக்கப்படுகிறது?",
                        "options": [
                            {"text": "அத்தியாயம் 5", "is_correct": True},
                            {"text": "அத்தியாயம் 1", "is_correct": False},
                            {"text": "அத்தியாயம் 3", "is_correct": False},
                            {"text": "அத்தியாயம் 8", "is_correct": False}
                        ]
                    }
                ]
            },
            "hi": {
                "mainTopic": "कृष्ण लीलाएं",
                "subTopic": "नंदोत्सव: गोकुल में श्रीकृष्ण जन्मोत्सव का दिव्य महामहोत्सव",
                "content": """### गोकुल में दिव्य आनंद का उदय

जब गोकुल में प्रभात हुआ, तो यशोदा मैया ने अपनी शय्या पर एक अत्यंत रूपवान, अलौकिक बालक को देखा। उस बालक का श्रीअंग नवीन मेघ के समान श्यामल था, नेत्र खिले हुए कमल के समान विशाल थे और मुखमंडल पर दिव्य सम्मोहन था।

पुत्र के जन्म का समाचार पाकर नंद महाराज का हृदय ब्रह्मानंद से भर गया। अनेक वर्षों से नंदबाबा और यशोदा मैया एक संतान के लिए तरस रहे थे। वृद्धावस्था में अपनी मनोकामना पूर्ण होते देख उनकी आंखों से प्रेमाश्रु बहने लगे। घर-घर यह शुभ समाचार फैल गया: "नंदबाबा और यशोदा मैया के घर लाला हुआ है!"

संपूर्ण गोकुल महामहोत्सव के रूप में परिवर्तित हो गया, जिसे **नंदोत्सव** कहा जाता है।

### नंद महाराज का विराट दान

नंद महाराज स्वभाव से ही अत्यंत उदार और धर्मात्मा थे। उन्होंने तत्काल वेदज्ञ ब्राह्मणों को बुलाकर बालक के जातकर्म संस्कार का आयोजन किया:

> **श्रीमद्भागवतम्, स्कंध 10, अध्याय 5, श्लोक 1–3**
> 
> *नन्दस् त्वात्मज उत्पन्ने जाताह्लादो महा-मनाः ।*  
> *आहूय विप्रान् वेद-ज्ञान् स्नातः शुचिर् अलंकृतः ।*  
> *वाचयित्वा स्वस्त्ययनं कारयामास जातकम् ॥*  
> 
> **भावार्थ:** "पुत्र उत्पन्न होने पर परम उदारमना नंद महाराज परमानंद में मग्न हो गए। उन्होंने पवित्र स्नान कर स्वच्छ वस्त्र और आभूषण धारण किए और वेदज्ञ ब्राह्मणों को बुलाकर स्वस्तिवाचन कराते हुए बालक का जातकर्म संस्कार संपन्न कराया।"

बालक के कल्याण की कामना से नंद महाराज ने ब्राह्मणों को दो लाख सुसज्जित दुग्धवती गौएं दान में दीं। गौओं के सींग स्वर्णपत्रों से मढ़े थे, खुरों पर पीतल जड़ा था और उनकी पीठ पर मोतियों से जड़ी रेशमी चादरें थीं। इसके साथ ही उन्होंने ब्राह्मणों और गायकों को पर्वताकार अन्न, स्वर्ण और वस्त्र दान किए।

### लाला के दर्शन को दौड़ पड़ीं गोपियां

नंदभवन में लाला के जन्म का समाचार सुनते ही ब्रज की गोपियां अपने सुध-बुध भूल बैठीं। घर के कामकाज छोड़कर, सुंदर रेशमी साड़ियां पहन, जूड़े में चमेली के फूल गूंथकर और स्वर्णिम आभूषण पहन वे नंदभवन की ओर दौड़ पड़ीं।

थालों में ताजा मक्खन, दही, हल्दी और रोली सजाकर, पायलों की झंकार करती हुई वे दौड़ी आईं। लाला के रूप को देखकर गोपियों ने आशीर्वाद दिया: "यह बालक करोड़ों वर्षों तक जिए और गोकुल की समस्त गौओं और ग्वालों की रक्षा करे!"

### दधि-कांदो और माखन की होली

गोपगण बहुमूल्य वस्त्र और पगड़ियां पहनकर दूध-दही के मटके लेकर नंदभवन पहुंचे। अत्यधिक आनंद के कारण वहां माखन और दही की होली प्रारंभ हो गई:

> **श्रीमद्भागवतम्, स्कंध 10, अध्याय 5, श्लोक 14**
> 
> *दधि-क्षीर-घृत-क्षोदैः सक्तो ’न्योन्यं विलेपनैः ।*  
> *चिक्षिपुस् तरसा गोपा दधि-भाण्डान्य् उदीरयन् ॥*  
> 
> **भावार्थ:** "परमानंद में मग्न होकर ग्वालबाल एक-दूसरे पर दही, दूध, घी और हल्दी मिश्रित सुगंधित जल डालने लगे। वे दही के मटके फोड़कर एक-दूसरे पर मक्खन और दही का लेप करने लगे।"

मृदंग, ढोल और बांसुरी की मधुर ध्वनियों के बीच गोप-गोपियां नृत्य करने लगे। संपूर्ण आंगन माखन और दूध की नदी बन गया।

यशोदा मैया और रोहिणी जी ने सभी आगंतुकों को वस्त्र और रत्न भेंट किए। भगवान श्री कृष्ण के शुभागमन से गोकुल समस्त ऐश्वर्यों और आनंद का धाम बन गया।""",
                "questions": [
                    {
                        "question": "गोकुल में प्रभात होते ही कौन सा शुभ समाचार फैला?",
                        "options": [
                            {"text": "नंद महाराज और यशोदा मैया के यहां पुत्र का जन्म हुआ है", "is_correct": True},
                            {"text": "कंस ने कर माफ कर दिया", "is_correct": False},
                            {"text": "गोकुल में सोने की खदान मिली", "is_correct": False},
                            {"text": "बाढ़ आ गई", "is_correct": False}
                        ]
                    },
                    {
                        "question": "गोकुल में श्री कृष्ण के जन्मोत्सव को किस नाम से जाना जाता है?",
                        "options": [
                            {"text": "नंदोत्सव", "is_correct": True},
                            {"text": "रथयात्रा", "is_correct": False},
                            {"text": "गोवर्धन पूजा", "is_correct": False},
                            {"text": "होली", "is_correct": False}
                        ]
                    },
                    {
                        "question": "नंद महाराज ने बालक के लिए कौन सा वैदिक संस्कार संपन्न कराया?",
                        "options": [
                            {"text": "जातकर्म संस्कार", "is_correct": True},
                            {"text": "उपनयन संस्कार", "is_correct": False},
                            {"text": "विवाह संस्कार", "is_correct": False},
                            {"text": "संन्यास संस्कार", "is_correct": False}
                        ]
                    },
                    {
                        "question": "नंद महाराज ने ब्राह्मणों को कितनी गौएं दान में दीं?",
                        "options": [
                            {"text": "दो लाख सुसज्जित गौएं", "is_correct": True},
                            {"text": "केवल 10 गौएं", "is_correct": False},
                            {"text": "500 गौएं", "is_correct": False},
                            {"text": "1,000 गौएं", "is_correct": False}
                        ]
                    },
                    {
                        "question": "दान की गई गौओं का श्रृंगार कैसा था?",
                        "options": [
                            {"text": "सोने से मढ़े सींग, पीतल के खुर और मोतियों से सजी रेशमी चादरें", "is_correct": True},
                            {"text": "लोहे की जंजीरें", "is_correct": False},
                            {"text": "चमड़े की रस्सियां", "is_correct": False},
                            {"text": "केवल मोरपंख", "is_correct": False}
                        ]
                    },
                    {
                        "question": "गोपियां थालों में कौन सी मांगलिक वस्तुएं लेकर नंदभवन आईं?",
                        "options": [
                            {"text": "ताजा मक्खन, दही, हल्दी और रोली", "is_correct": True},
                            {"text": "अस्त्र-शस्त्र", "is_correct": False},
                            {"text": "मदिरा और मांस", "is_correct": False},
                            {"text": "मथुरा के सिक्के", "is_correct": False}
                        ]
                    },
                    {
                        "question": "गोपियों ने लाला को क्या आशीर्वाद दिया?",
                        "options": [
                            {"text": "यह बालक करोड़ों वर्षों तक जिए और गोकुल की रक्षा करे", "is_correct": True},
                            {"text": "वह युद्ध में संसार को जीते", "is_correct": False},
                            {"text": "वह बड़ा व्यापारी बने", "is_correct": False},
                            {"text": "वह गोकुल छोड़कर चला जाए", "is_correct": False}
                        ]
                    },
                    {
                        "question": "उत्सव में ग्वालबालों ने क्या आनंदमयी क्रीड़ा की?",
                        "options": [
                            {"text": "एक-दूसरे पर दही, दूध, मक्खन और हल्दी का जल उड़ेला", "is_correct": True},
                            {"text": "तलवार युद्ध किया", "is_correct": False},
                            {"text": "जुआ खेला", "is_correct": False},
                            {"text": "दिनभर सोए रहे", "is_correct": False}
                        ]
                    },
                    {
                        "question": "आगंतुकों को वस्त्र और आभूषण बांटने में यशोदा मैया की सहायता किसने की?",
                        "options": [
                            {"text": "माता रोहिणी ने", "is_correct": True},
                            {"text": "देवकी ने", "is_correct": False},
                            {"text": "कुंती ने", "is_correct": False},
                            {"text": "गांधारी ने", "is_correct": False}
                        ]
                    },
                    {
                        "question": "श्रीमद्भागवतम् के दसवें स्कंध के किस अध्याय में नंदोत्सव वर्णित है?",
                        "options": [
                            {"text": "अध्याय 5", "is_correct": True},
                            {"text": "अध्याय 1", "is_correct": False},
                            {"text": "अध्याय 3", "is_correct": False},
                            {"text": "अध्याय 8", "is_correct": False}
                        ]
                    }
                ]
            },
            "ml": {
                "mainTopic": "കൃഷ്ണ ലീലകൾ",
                "subTopic": "നന്ദോത്സവം: ഗോകുലത്തിലെ മഹാവിശേഷവും ആനന്ദനൃത്തവും",
                "content": """### ഗോകുലത്തിലെ ദിവ്യപ്രഭാതം

ഗോകുലത്തിൽ പ്രഭാതമായപ്പോൾ യശോദാമയുടെ അരികിൽ അതിസുന്ദരനായ ഒരു ആൺകുഞ്ഞ് കിടക്കുന്നതു കണ്ട് എല്ലാവരും ആനന്ദഭരിതരായി. കാർമേഘവർണ്ണമുള്ള തിരുമേനിയും വിടർന്ന താമരയിതൾ പോലെയുള്ള കണ്ണുകളുമുള്ള ആ ഉണ്ണിയെക്കണ്ട് നന്ദഗോപരുടെ ഹൃദയം പരമാനന്ദത്തിൽ മുഴുകി.

വർഷങ്ങളായി ഒരു ഉണ്ണിക്കായി പ്രാർത്ഥിച്ച നന്ദനും യശോദയ്ക്കും വാർദ്ധക്യത്തിൽ ലഭിച്ച ഈ വരദാനം ഗോകുലത്തിലെങ്ങും കാട്ടുതീപോലെ പടർന്നുപിടിച്ചു: "നന്ദഗോപർക്കും യശോദയ്ക്കും ഒരു ഉണ്ണികൃഷ്ണൻ പിറന്നിരിക്കുന്നു!"

ഗോകുലം മുഴുവൻ ആഘോഷത്തിമിർപ്പിലായി. ഈ മഹോത്സവം **നന്ദോത്സവം** എന്നറിയപ്പെടുന്നു.

### നന്ദഗോപരുടെ മഹാദാനം

ഉദാരമനസ്കനായ നന്ദഗോപർ ഉണ്ണിക്കായി വേദവിധിയനുസരിച്ച് ജാതകർമ്മം നടത്തി:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അദ്ധ്യായം 5, ശ്ലോകങ്ങൾ 1–3**
> 
> *നന്ദസ് ത്വാത്മജ ഉത്പന്നേ ജാതാഹ്ലാതോ മഹാമനാഃ |*  
> *ആഹൂയ വിപ്രാൻ വേദജ്ഞാൻ സ്നാതഃ ശുചിർ അലംകൃതഃ |*  
> *വാചയിത്വാ സ്വസ്ത്യയനം കാരയാമാസ ജാതകമ് ||*  
> 
> **അർത്ഥം:** "പുത്രജനനത്താൽ പരമാനന്ദഭരിതനായ നന്ദഗോപർ ശുദ്ധസ്നാനം ചെയ്ത് മംഗളവസ്ത്രങ്ങളണിഞ്ഞ്, വേദജ്ഞരായ ബ്രാഹ്മണരെ ക്ഷണിച്ചുവരുത്തി സ്വസ്തിവാചനം നടത്തിച്ച് ജാതകർമ്മം നിർവ്വഹിച്ചു."

കുഞ്ഞിന്റെ ആയുരാരോഗ്യത്തിനായി നന്ദഗോപർ രണ്ടുലക്ഷം അലങ്കരിച്ച പശുക്കളെ ദാനം ചെയ്തു. പശുക്കളുടെ കൊമ്പുകൾ സ്വർണ്ണത്തകിടുകൊണ്ടും കുളമ്പുകൾ പിച്ചളകൊണ്ടും പൊതിഞ്ഞിരുന്നു; മുതുകിൽ രത്നപ്പട്ടുപുതപ്പിച്ചിരുന്നു. കൂടാതെ ധാന്യക്കുന്നുകളും സ്വർണ്ണവും വസ്ത്രങ്ങളും ബ്രാഹ്മണർക്ക് സമർപ്പിച്ചു.

### ഉണ്ണിയെക്കാണാൻ ഗോപികമാർ എത്തുന്നു

ഉണ്ണിയുടെ ജനനവാർത്ത കേട്ട മാത്രയിൽ ഗോപികമാർ വീട്ടുജോലികളെല്ലാം ഉപേക്ഷിച്ച്, മനോഹരമായ പട്ടുസാരികളും ആഭരണങ്ങളും അണിഞ്ഞ്, കാൽച്ചിലമ്പുകൾ കിലുങ്ങിക്കൊണ്ട് നന്ദഭവനത്തിലേക്ക് പാഞ്ഞെത്തി.

താലങ്ങളിൽ വെണ്ണയും തൈരും മഞ്ഞളും നിറച്ച് അവർ ഉണ്ണിയെക്കണ്ട് അനുഗ്രഹിച്ചു: "ഈ ഉണ്ണി കോടിക്കണക്കിന് വർഷങ്ങൾ ജീവിച്ച് ഗോകുലത്തെയും പശുക്കളെയും രക്ഷിക്കട്ടെ!"

### തൈരും വെണ്ണയും കൊണ്ടുള്ള ആനന്ദക്കളി

ഗോപന്മാർ തൈരും വെണ്ണയും നിറഞ്ഞ മൺകലങ്ങളുമായി നന്ദഭവനത്തിൽ എത്തി. ആനന്ദാതിരേകത്താൽ അവർ തൈരും വെണ്ണയും വാരിയെറിഞ്ഞ് ആഘോഷിച്ചു:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അദ്ധ്യായം 5, ശ്ലോകം 14**
> 
> *ദധി-ക്ഷീര-ഘൃത-ക്ഷോദൈഃ സിക്തോ ’ന്യോന്യം വിലേപനൈഃ |*  
> *ചിക്ഷിപുസ് തരസാ ഗോപാ ദധി-ഭാണ്ഡാന്യ് ഉദീരയൻ ||*  
> 
> **അർത്ഥം:** "ആനന്ദത്താൽ ഉന്മത്തരായ ഗോപന്മാർ തൈരും പാലും നെയ്യും മഞ്ഞൾവെള്ളവും പരസ്പരം തളിക്കുകയും തൈർക്കുടങ്ങൾ ഉടച്ച് വെണ്ണ വാരിപ്പൂശുകയും ചെയ്തു."

മുറ്റമാകെ പാൽക്കടലായി മാറി. മൃദംഗവും പുല്ലാങ്കുഴലും നാദസ്വരവും മുഴങ്ങി. യശോദാമയും രോഹിണിദേവിയും എല്ലാവർക്കും ഉപഹാരങ്ങൾ നൽകി. ഭഗവാൻ ശ്രീകൃഷ്ണന്റെ സാന്നിധ്യത്താൽ ഗോകുലം സകല ഐശ്വര്യങ്ങളുടെയും സങ്കേതമായി മാറി.""",
                "questions": [
                    {
                        "question": "ഗോകുലത്തിൽ പരന്ന സന്തോഷവാർത്ത എന്തായിരുന്നു?",
                        "options": [
                            {"text": "നന്ദഗോപർക്കും യശോദയ്ക്കും ഒരു ആൺകുഞ്ഞ് ജനിച്ചു", "is_correct": True},
                            {"text": "മഥുരയിൽ പുതിയ രാജാവ് വന്നു", "is_correct": False},
                            {"text": "സ്വർണ്ണഖനി കണ്ടെത്തി", "is_correct": False},
                            {"text": "വെള്ളപ്പൊക്കമുണ്ടായി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ശ്രീകൃഷ്ണന്റെ ജനനത്തോടനുബന്ധിച്ച് ഗോകുലത്തിൽ നടന്ന ഉത്സവത്തിന്റെ പേരെന്ത്?",
                        "options": [
                            {"text": "നന്ദോത്സവം", "is_correct": True},
                            {"text": "രഥയാത്ര", "is_correct": False},
                            {"text": "ഗോവർദ്ധന പൂജ", "is_correct": False},
                            {"text": "ഹോളി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "നന്ദഗോപർ ഉണ്ണിക്കായി നടത്തിയ വൈദിക ചടങ്ങേത്?",
                        "options": [
                            {"text": "ജാതകർമ്മം", "is_correct": True},
                            {"text": "ഉപനയനം", "is_correct": False},
                            {"text": "വിവാഹം", "is_correct": False},
                            {"text": "സന്യാസം", "is_correct": False}
                        ]
                    },
                    {
                        "question": "നന്ദഗോപർ എത്ര പശുക്കളെ ദാനം ചെയ്തു?",
                        "options": [
                            {"text": "രണ്ടുലക്ഷം അലങ്കരിച്ച പശുക്കളെ", "is_correct": True},
                            {"text": "10 പശുക്കളെ മാത്രം", "is_correct": False},
                            {"text": "500 പശുക്കളെ", "is_correct": False},
                            {"text": "1,000 പശുക്കളെ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ദാനം ചെയ്ത പശുക്കളെ എങ്ങനെയാണ് അലങ്കരിച്ചിരുന്നത്?",
                        "options": [
                            {"text": "കൊമ്പിൽ സ്വർണ്ണവും കുളമ്പിൽ പിച്ചളയും മുതുകിൽ രത്നപ്പട്ടും ചാർത്തി", "is_correct": True},
                            {"text": "ഇരുമ്പുചങ്ങലയിട്ട്", "is_correct": False},
                            {"text": "തോൽക്കയറുകൊണ്ട്", "is_correct": False},
                            {"text": "മയിൽപ്പീലി മാത്രം വെച്ച്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഗോപികമാർ താലങ്ങളിൽ എന്തൊക്കെ മംഗളവസ്തുക്കളാണ് കൊണ്ടുവന്നത്?",
                        "options": [
                            {"text": "വെണ്ണ, തൈര്, മഞ്ഞൾ, റോചന", "is_correct": True},
                            {"text": "ആയുധങ്ങൾ", "is_correct": False},
                            {"text": "മദ്യം", "is_correct": False},
                            {"text": "സ്വർണ്ണനാണയം മാത്രം", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഗോപികമാർ ഉണ്ണിയെ എങ്ങനെയാണ് അനുഗ്രഹിച്ചത്?",
                        "options": [
                            {"text": "ഈ കുഞ്ഞ് കോടിക്കണക്കിന് വർഷം ജീവിച്ച് ഗോകുലത്തെ രക്ഷിക്കട്ടെ എന്ന്", "is_correct": True},
                            {"text": "യുദ്ധത്തിൽ ജയിക്കട്ടെ എന്ന്", "is_correct": False},
                            {"text": "വലിയ വ്യാപാരിയാകട്ടെ എന്ന്", "is_correct": False},
                            {"text": "നാടുവിട്ടുപോകട്ടെ എന്ന്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഉത്സവത്തിൽ ഗോപന്മാർ എന്തു കളിയാണ് നടത്തിയത്?",
                        "options": [
                            {"text": "തൈരും വെണ്ണയും മഞ്ഞൾവെള്ളവും പരസ്പരം വാരിയെറിഞ്ഞു", "is_correct": True},
                            {"text": "വാൾപ്പയറ്റ് നടത്തി", "is_correct": False},
                            {"text": "ചൂതുകളിച്ചു", "is_correct": False},
                            {"text": "ഉറങ്ങി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "സമ്മാനങ്ങൾ നൽകാൻ യശോദയെ സഹായിച്ചത് ആരാണ്?",
                        "options": [
                            {"text": "രോഹിണിദേവി", "is_correct": True},
                            {"text": "ദേവകി", "is_correct": False},
                            {"text": "കുന്തി", "is_correct": False},
                            {"text": "ഗാന്ധാരി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ശ്രീമദ് ഭാഗവതം പത്താം സ്കന്ധത്തിലെ ഏത് അദ്ധ്യായത്തിലാണ് നന്ദോത്സവം വർണ്ണിച്ചിരിക്കുന്നത്?",
                        "options": [
                            {"text": "അദ്ധ്യായം 5", "is_correct": True},
                            {"text": "അദ്ധ്യായം 1", "is_correct": False},
                            {"text": "അദ്ധ്യായം 3", "is_correct": False},
                            {"text": "അദ്ധ്യായം 8", "is_correct": False}
                        ]
                    }
                ]
            },
            "bn": {
                "mainTopic": "কৃষ্ণ লীলা",
                "subTopic": "নন্দোৎসব: গোকুলে পরম আনন্দঘন মহোৎসব",
                "content": """### গোকুলে দিব্য আনন্দের উদয়

গোকুলে যখন প্রভাত হলো, তখন মাতা যশোদা শয্যায় পার্শ্বে শায়িত এক অপূর্ব সুন্দর দেবশিশুকে দেখে পরমানন্দে আপ্লুত হলেন। নবীন জলধরের ন্যায় শ্যামল শ্রীঅঙ্গ, প্রস্ফুটিত পদ্মের ন্যায় নয়নযুগল এবং মুখে অলৌকিক মোহনীয় মাধুর্য।

নন্দ মহারাজ এই শুভ সংবাদ পেয়ে দিব্য আনন্দে নিমগ্ন হলেন। বহু বছর ধরে একটি সন্তানের জন্য প্রার্থনা করা নন্দ ও যশোদার এই বার্ধক্যে পরম মনস্কামনা পূর্ণ হলো। গোকুলে ঘরে ঘরে বার্তা ছড়িয়ে পড়ল: "নন্দ মহারাজের ঘরে চাঁদের মতো পুত্রসন্তান জন্মেছে!"

সমগ্র গোকুল পরম আনন্দঘন মহোৎসবে রূপ নিল, যা **নন্দোৎসব** নামে খ্যাত।

### নন্দ মহারাজের অতুলনীয় দান

স্বভাবতই পরম উদারচেতা নন্দ মহারাজ তৎক্ষণাৎ শাস্ত্রবিধি অনুসারে বালকের জাতকর্ম সংস্কার সম্পাদন করলেন:

> **শ্রীমদ্ভাগবত, স্কন্ধ ১০, অধ্যায় ৫, শ্লোক ১–৩**
> 
> *নন্দস্ত্বাত্মজ উৎপন্নে জাতাহ্লাদো মহামনাঃ ।*  
> *আহূয় বিপ্রান্ বেদজ্ঞান্ স্নাতঃ শুচিরলঙ্কৃতঃ ।*  
> *বাচয়িত্বা স্বস্ত্যয়নং কারয়ামাস জাতকম্ ॥*  
> 
> **অনুবাদ:** "পুত্র জন্মানোয় পরম উদারচেতা নন্দ মহারাজ পরমানন্দে মগ্ন হলেন। তিনি পবিত্র স্নান করে শুদ্ধ বস্ত্রালঙ্কারে ভূষিত হলেন এবং বেদজ্ঞ ব্রাহ্মণদের আহ্বান করে স্বস্তিবাচনপূর্বক বালকের জাতকর্ম সম্পন্ন করলেন।"

বালকের মঙ্গলের জন্য নন্দ মহারাজ ব্রাহ্মণদের দুই লক্ষ সুসজ্জিত পয়স্বিনী গাভী দান করলেন। গাভীদের শিং স্বর্ণমণ্ডিত, খুর পিত্তলে মোড়া এবং পৃষ্ঠদেশ রত্নখচিত রেশমি বস্ত্রে আচ্ছাদিত ছিল। সঙ্গে পর্বতের ন্যায় খাদ্যশস্য ও সুবর্ণালঙ্কার দান করা হলো।

### গোপীদের আনন্দযাত্রা

লালার জন্মের কথা শুনে ব্রজের গোপীরা গৃহকর্ম ফেলে সুসজ্জিত হয়ে নূপুর বাজিয়ে নন্দভবনে ছুটে এলেন।

স্বর্ণথালায় নবনীত, দধি ও চন্দন সাজিয়ে তাঁরা খোকাকে দেখে আশীর্বাদ করলেন: "এই শিশু কোটি কোটি বছর বেঁচে থাকুক এবং গোকুলকে রক্ষা করুক!"

### দধি ও মাখনের আনন্দমেলা

গোপগণ দুধ ও মাখনের ভাণ্ড নিয়ে উপস্থিত হলেন। পরমানন্দে তারা একে অপরের ওপর দধি, মাখন ও হলুদমিশ্রিত সুগন্ধি জল নিক্ষেপ করতে লাগলেন:

> **শ্রীমদ্ভাগবত, স্কন্ধ ১০, অধ্যায় ৫, শ্লোক ১৪**
> 
> *দধি-ক্ষীর-ঘৃত-ক্ষোদৈঃ সিক্তো ’ন্যোন্যং বিলেপনৈঃ ।*  
> *চিক্ষিপুস্তরসা গোপা দধিভাণ্ডান্যুদীরয়ন্ ॥*  
> 
> **অনুবাদ:** "পরমানন্দে মগ্ন হয়ে গোপগণ একে অপরের ওপর দধি, ক্ষীর, ঘৃত ও হলুদ জল ছিটিয়ে আনন্দ করতে লাগল। তারা দধির হাঁড়ি ভেঙে একে অপরের অঙ্গে মাখন লেপন করে নৃত্য করতে লাগল।"

মৃদঙ্গ ও বাঁশির ধ্বনিতে গোকুল মুখরিত হয়ে উঠল। মাতা যশোদা ও রোহিণী দেবী সকলকে রত্ন ও বস্ত্র বিতরণ করলেন। পরমেশ্বর শ্রীকৃষ্ণের আগমনে গোকুল পরম ঐশ্বর্যময় হয়ে উঠল।""",
                "questions": [
                    {
                        "question": "গোকুলে প্রভাতে কি শুভ সংবাদ প্রচারিত হয়েছিল?",
                        "options": [
                            {"text": "নন্দ মহারাজ ও যশোদা দেবীর ঘরে পুত্রসন্তান জন্মেছে", "is_correct": True},
                            {"text": "মথুরায় নতুন রাজা হয়েছে", "is_correct": False},
                            {"text": "স্বর্ণখনি পাওয়া গেছে", "is_correct": False},
                            {"text": "বন্যা এসেছে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "গোকুলে শ্রীকৃষ্ণের আবির্ভাব উৎসবের নাম কি?",
                        "options": [
                            {"text": "নন্দোৎসব", "is_correct": True},
                            {"text": "রথযাত্রা", "is_correct": False},
                            {"text": "গোবর্ধন পূজা", "is_correct": False},
                            {"text": "হোলি", "is_correct": False}
                        ]
                    },
                    {
                        "question": "নন্দ মহারাজ বালকের জন্য কোন সংস্কার করেছিলেন?",
                        "options": [
                            {"text": "জাতকর্ম সংস্কার", "is_correct": True},
                            {"text": "উপনয়ন", "is_correct": False},
                            {"text": "বিবাহ", "is_correct": False},
                            {"text": "সন্ন্যাস", "is_correct": False}
                        ]
                    },
                    {
                        "question": "নন্দ মহারাজ ব্রাহ্মণদের কত গাভী দান করেছিলেন?",
                        "options": [
                            {"text": "দুই লক্ষ সুসজ্জিত গাভী", "is_correct": True},
                            {"text": "১০টি গাভী", "is_correct": False},
                            {"text": "৫০০টি গাভী", "is_correct": False},
                            {"text": "১,০০০টি গাভী", "is_correct": False}
                        ]
                    },
                    {
                        "question": "দান করা গাভীদের কীভাবে সাজানো হয়েছিল?",
                        "options": [
                            {"text": "স্বর্ণমণ্ডিত শিং, পিতলের খুর ও রত্নখচিত রেশমি বস্ত্রে", "is_correct": True},
                            {"text": "লোহার শিকলে", "is_correct": False},
                            {"text": "চামড়ার দড়িতে", "is_correct": False},
                            {"text": "ময়ূরপুচ্ছে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "গোপীরা থালায় কি নিয়ে এসেছিলেন?",
                        "options": [
                            {"text": "মাখন, দধি, হলুদ ও রোচনা", "is_correct": True},
                            {"text": "অস্ত্রশস্ত্র", "is_correct": False},
                            {"text": "মদ্য ও মাংস", "is_correct": False},
                            {"text": "মুদ্রা", "is_correct": False}
                        ]
                    },
                    {
                        "question": "গোপীরা শিশুকে কি আশীর্বাদ করেছিলেন?",
                        "options": [
                            {"text": "এই শিশু কোটি বছর বেঁচে থাকুক ও গোকুলকে রক্ষা করুক", "is_correct": True},
                            {"text": "যুদ্ধ জয় করুক", "is_correct": False},
                            {"text": "বণিক হোক", "is_correct": False},
                            {"text": "গোকুল ছেড়ে চলে যাক", "is_correct": False}
                        ]
                    },
                    {
                        "question": "উৎসবে গোপরা কি আনন্দময় খেলা করেছিলেন?",
                        "options": [
                            {"text": "দধি, মাখন ও হলুদ জল একে অপরের ওপর ছিটিয়েছিলেন", "is_correct": True},
                            {"text": "তলোয়ার যুদ্ধ করেছিলেন", "is_correct": False},
                            {"text": "পাশা খেলেছিলেন", "is_correct": False},
                            {"text": "ঘুমিয়েছিলেন", "is_correct": False}
                        ]
                    },
                    {
                        "question": "যশোদা দেবীকে দান বিতরণে কে সাহায্য করেছিলেন?",
                        "options": [
                            {"text": "মাতা রোহিণী", "is_correct": True},
                            {"text": "দেবকী", "is_correct": False},
                            {"text": "কুন্তী", "is_correct": False},
                            {"text": "গান্ধারী", "is_correct": False}
                        ]
                    },
                    {
                        "question": "শ্রীমদ্ভাগবতের দশম স্কন্ধের কোন অধ্যায়ে নন্দোৎসব বর্ণিত?",
                        "options": [
                            {"text": "অধ্যায় ৫", "is_correct": True},
                            {"text": "অধ্যায় ১", "is_correct": False},
                            {"text": "অধ্যায় ৩", "is_correct": False},
                            {"text": "অধ্যায় ৮", "is_correct": False}
                        ]
                    }
                ]
            },
            "te": {
                "mainTopic": "కృష్ణ లీలలు",
                "subTopic": "నందోత్సవం: గోకులంలో శ్రీకృష్ణ జన్మోత్సవ వైభవం",
                "content": """### గోకులంలో దివ్య ఆనందోదయం

గోకులంలో తెల్లవారగానే యశోదమ్మ తన పక్కన శ్యామల వర్ణంతో మెరిసిపోతున్న ఒక దివ్య బాలుని చూసి అమితానందం పొందింది. తామర రేకుల వంటి కన్నులు, ముగ్ధ మోహన రూపంతో ఉన్న ఆ బాలుని చూసి నందమహారాజు హృదయం బ్రహ్మానందంతో పొంగిపొర్లింది.

ఎన్నో ఏళ్ళుగా సంతానం కోసం తపించిన నందుడు, యశోదలకు వృద్ధాప్యంలో ఈ వరప్రసాదం లభించడంతో ఆ శుభవార్త గోకులమంతటా దావానలంలా వ్యాపించింది: "నందమహారాజుకు మగబిడ్డ పుట్టాడు!"

గోకులమంతా ఒక మహా వేడుకగా మారింది. ఈ ఉత్సవమే **నందోత్సవం**.

### నందమహారాజు విరాళాలు మరియు జాతకర్మ

ధర్మాత్ముడైన నందుడు వేద పండితులను పిలిపించి పవిత్ర జాతకర్మ సంస్కారాన్ని జరిపించాడు:

> **శ్రీమద్భాగవతం, స్కంధం 10, అధ్యాయం 5, శ్లోకాలు 1–3**
> 
> *నందస్ త్వాత్మజ ఉత్పన్నే జాతాహ్లాదో మహామనాః |*  
> *ఆహూయ విప్రాన్ వేదజ్ఞాన్ స్నాతః శుచిర్ అలంకృతః |*  
> *వాచయిత్వా స్వస్త్యయనం కారయామాస జాతకమ్ ||*  
> 
> **తాత్పర్యం:** "కుమారుడు జన్మించడంతో పరమానందభరితుడైన నందమహారాజు పవిత్ర స్నానమాచరించి శుభ్రవస్త్రాలు ధరించి, వేదజ్ఞులైన బ్రాహ్మణులను పిలిపించి స్వస్తివాచనం చేయిస్తూ జాతకర్మ సంస్కారాన్ని శాస్త్రోక్తంగా నిర్వహించాడు."

బిడ్డ ఆయురారోగ్యాల కోసం నందుడు రెండు లక్షల అలంకరించిన పాడి ఆవులను దానం చేశాడు. ఆవుల కొమ్ములకు బంగారు తొడుగులు, గిట్టలకు ఇత్తడి, వీపులపై ముత్యాలు పొదిగిన పట్టు వస్త్రాలు అలంకరించారు. ధాన్యరాశులను, సువర్ణాన్ని బ్రాహ్మణులకు సమర్పించాడు.

### కృష్ణుని చూడవచ్చిన గోపికలు

శుభవార్త విన్న గోపికలు పనులన్నీ వదిలి, పట్టుచీరలు, ఆభరణాలు ధరించి నందభవనానికి పరుగుతీశారు.

బంగారు పళ్ళాలలో వెన్న, పెరుగు, పసుపు తీసుకొచ్చి ఉయ్యాలలో ఉన్న కృష్ణుని చూసి ఇలా ఆశీర్వదించారు: "ఈ బాలుడు కోట్లాది సంవత్సరాలు జీవించి గోకుల ప్రజలను, ఆవులను రక్షించుగాక!"

### పెరుగు, వెన్నల హోలీ

గోపకులు పాలు, వెన్న కుండలతో నందభవనానికి చేరుకున్నారు. పట్టరాని ఆనందంతో వారు ఒకరిపై ఒకరు పాలు, పెరుగు, పసుపు నీళ్ళు చల్లుకున్నారు:

> **శ్రీమద్భాగవతం, స్కంధం 10, అధ్యాయం 5, శ్లోకం 14**
> 
> *దధి-క్షీర-ఘృత-క్షోదైః సిక్తో ’న్యోన్యం విలేపనైః |*  
> *చిక్షిపుస్ తరసా గోపా దధి-భాండ్యాన్యుదీరయన్ ||*  
> 
> **తాత్పర్యం:** "ఆనందంలో మునిగిపోయిన గోపకులు ఒకరిపై ఒకరు పెరుగు, పాలు, నెయ్యి, పసుపు నీళ్ళు చల్లుకున్నారు. పెరుగు కుండలు పగలగొట్టి ఒకరికొకరు వెన్న పూసుకుంటూ నృత్యం చేశారు."

ఆంగణమంతా పాల సముద్రంలా మారింది. మృదంగాలు, వేణువుల నాదాలతో గోకులం మార్మోగింది. యశోదమ్మ, రోహిణీదేవి అందరికీ వస్త్రాలు, ఆభరణాలు దానం చేశారు. శ్రీకృష్ణుని రాకతో గోకులం సమస్త సంపదలతో విరాజిల్లింది.""",
                "questions": [
                    {
                        "question": "గోకులంలో తెల్లవారగానే వ్యాపించిన శుభవార్త ఏమిటి?",
                        "options": [
                            {"text": "నంద యశోదలకు మగబిడ్డ పుట్టాడని", "is_correct": True},
                            {"text": "మథురలో కొత్త రాజు వచ్చాడని", "is_correct": False},
                            {"text": "బంగారు గని దొరికిందని", "is_correct": False},
                            {"text": "వరద వచ్చిందని", "is_correct": False}
                        ]
                    },
                    {
                        "question": "శ్రీకృష్ణుని జన్మ సందర్భంగా గోకులంలో జరిగిన వేడుక పేరేమిటి?",
                        "options": [
                            {"text": "నందోత్సవం", "is_correct": True},
                            {"text": "రథయాత్ర", "is_correct": False},
                            {"text": "గోవర్ధన పూజ", "is_correct": False},
                            {"text": "హోలీ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "నందమహారాజు బాలునికి ఏ సంస్కారం జరిపించాడు?",
                        "options": [
                            {"text": "జాతకర్మ సంస్కారం", "is_correct": True},
                            {"text": "ఉపనయనం", "is_correct": False},
                            {"text": "వివాహం", "is_correct": False},
                            {"text": "సన్యాసం", "is_correct": False}
                        ]
                    },
                    {
                        "question": "నందుడు బ్రాహ్మణులకు ఎన్ని ఆవులను దానం చేశాడు?",
                        "options": [
                            {"text": "రెండు లక్షల ఆవులను", "is_correct": True},
                            {"text": "10 ఆవులు మాత్రమే", "is_correct": False},
                            {"text": "500 ఆవులు", "is_correct": False},
                            {"text": "1,000 ఆవులు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "దానం చేసిన ఆవులను ఎలా అలంకరించారు?",
                        "options": [
                            {"text": "బంగారు కొమ్ములు, ఇత్తడి గిట్టలు, ముత్యాల పట్టు వస్త్రాలతో", "is_correct": True},
                            {"text": "ఇనుప గొలుసులతో", "is_correct": False},
                            {"text": "తోలు తాళ్ళతో", "is_correct": False},
                            {"text": "నెమలి ఈకలతో మాత్రమే", "is_correct": False}
                        ]
                    },
                    {
                        "question": "గోపికలు పళ్ళాలలో ఏ శుభ వస్తువులను తెచ్చారు?",
                        "options": [
                            {"text": "వెన్న, పెరుగు, పసుపు, రోచన", "is_correct": True},
                            {"text": "ఆయుధాలు", "is_correct": False},
                            {"text": "మద్యం", "is_correct": False},
                            {"text": "నాణాలు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "గోపికలు బాలుని ఏమని దీవించారు?",
                        "options": [
                            {"text": "ఈ బిడ్డ కోట్లాది ఏళ్ళు జీవించి గోకులాన్ని కాపాడుగాక", "is_correct": True},
                            {"text": "యుద్ధంలో గెలవాలని", "is_correct": False},
                            {"text": "వ్యాపారి కావాలని", "is_correct": False},
                            {"text": "గోకులం విడిచి వెళ్ళాలని", "is_correct": False}
                        ]
                    },
                    {
                        "question": "వేడుకలో గోపకులు ఏ ఆట ఆడారు?",
                        "options": [
                            {"text": "ఒకరిపై ఒకరు పెరుగు, పాలు, వెన్న, పసుపు నీళ్ళు చల్లుకున్నారు", "is_correct": True},
                            {"text": "కత్తి యుద్ధం చేశారు", "is_correct": False},
                            {"text": "జూదం ఆడారు", "is_correct": False},
                            {"text": "నిద్రపోయారు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "దానాలు పంచడంలో యశోదమ్మకు ఎవరు సహాయం చేశారు?",
                        "options": [
                            {"text": "రోహిణీదేవి", "is_correct": True},
                            {"text": "దేవకి", "is_correct": False},
                            {"text": "కుంతి", "is_correct": False},
                            {"text": "గాంధారి", "is_correct": False}
                        ]
                    },
                    {
                        "question": "భాగవతంలో పదవ స్కంధంలో ఏ అధ్యాయంలో నందోత్సవం వర్ణించబడింది?",
                        "options": [
                            {"text": "అధ్యాయం 5", "is_correct": True},
                            {"text": "అధ్యాయం 1", "is_correct": False},
                            {"text": "అధ్యాయం 3", "is_correct": False},
                            {"text": "అధ్యాయం 8", "is_correct": False}
                        ]
                    }
                ]
            },
            "kn": {
                "mainTopic": "ಕೃಷ್ಣ ಲೀಲೆಗಳು",
                "subTopic": "ನಂದೋತ್ಸವ: ಗೋಕುಲದಲ್ಲಿ ಶ್ರೀಕೃಷ್ಣನ ದಿವ್ಯ ಜನ್ಮ ಮಹೋತ್ಸವ",
                "content": """### ಗೋಕುಲದಲ್ಲಿ ದಿವ್ಯ ಆನಂದೋದಯ

ಗೋಕುಲದಲ್ಲಿ ಬೆಳಗಾಗುತ್ತಿದ್ದಂತೆ ಯಶೋದೆಯು ತನ್ನ ಪಕ್ಕದಲ್ಲಿ ಕಡುನೀಲಿ ಮೇಘಶ್ಯಾಮಲ ವರ್ಣದ, ತಾವರೆಯಂತಹ ವಿಶಾಲ ಕಣ್ಣುಗಳುಳ್ಳ ದಿವ್ಯ ಬಾಲಕನನ್ನು ಕಂಡು ಆನಂದತುಂದಿಲಳಾದಳು. ಮಗುವನ್ನು ಕಂಡ ನಂದಮಹಾರಾಜರ ಹೃದಯವು ಪರಮಾನಂದದಿಂದ ತುಂಬಿಹೋಯಿತು.

ಅನೇಕ ವರ್ಷಗಳಿಂದ ಸಂತಾನಕ್ಕಾಗಿ ಹಾತೊರೆಯುತ್ತಿದ್ದ ನಂದ ಮತ್ತು ಯಶೋದೆಯರಿಗೆ ಈ ವಯಸ್ಸಿನಲ್ಲಿ ದೊರೆತ ವರಪ್ರಸಾದವನ್ನು ಕೇಳಿ ಇಡೀ ಗೋಕುಲದಲ್ಲಿ ಶುಭವಾರ್ತೆ ಹಬ್ಬಿತು: "ನಂದಮಹಾರಾಜರಿಗೆ ಗಂಡು ಮಗು ಜನಿಸಿದೆ!"

ಇಡೀ ಗೋಕುಲವು ಮಹೋತ್ಸವದ ತಾಣವಾಯಿತು. ಈ ಹಬ್ಬವೇ **ನಂದೋತ್ಸವ**.

### ನಂದಮಹಾರಾಜರ ಮಹಾದಾನ

ಧರ್ಮಾತ್ಮರಾದ ನಂದಮಹಾರಾಜರು ವೇದಜ್ಞ ಬ್ರಾಹ್ಮಣರನ್ನು ಕರೆಸಿ ಶಾಸ್ತ್ರೋಕ್ತವಾಗಿ ಜಾತಕರ್ಮ ಸಂಸ್ಕಾರವನ್ನು ನೆರವೇರಿಸಿದರು:

> **ಶ್ರೀಮದ್ಭಾಗವತ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 5, ಶ್ಲೋಕಗಳು 1–3**
> 
> *ನಂದಸ್ ತ್ವಾತ್ಮಜ ಉತ್ಪನ್ನೇ ಜಾತಹ್ಲಾದೋ ಮಹಾಮನಾಃ |*  
> *ಆಹೂಯ ವಿಪ್ರಾನ್ ವೇದಜ್ಞಾನ್ ಸ್ನಾತಃ ಶುಚಿರ್ ಅಲಂಕೃತಃ |*  
> *ವಾಚಯಿತ್ವಾ ಸ್ವಸ್ತ್ಯಯನಂ ಕಾರಯಾಮಾಸ ಜಾತಕಮ್ ||*  
> 
> **ಭಾವಾರ್ಥ:** "ಪುತ್ರ ಜನನದಿಂದ ಪರಮಾನಂದಭರಿತರಾದ ಮಹೋದಾರಿ ನಂದಮಹಾರಾಜರು ಪವಿತ್ರ ಸ್ನಾನ ಮಾಡಿ, ಶುಭ್ರವಸ್ತ್ರಗಳನ್ನು ಧರಿಸಿ, ವೇದಜ್ಞ ಬ್ರಾಹ್ಮಣರನ್ನು ಕರೆಸಿ ಸ್ವಸ್ತಿವಾಚನ ಮಾಡಿಸುತ್ತಾ ಮಗುವಿನ ಜಾತಕರ್ಮ ಸಂಸ್ಕಾರವನ್ನು ನೆರವೇರಿಸಿದರು."

ಮಗುವಿನ ಆಯುರಾರೋಗ್ಯಕ್ಕಾಗಿ ನಂದರು ಎರಡು ಲಕ್ಷ ಅಲಂಕೃತ ಹಸುಗಳನ್ನು ಬ್ರಾಹ್ಮಣರಿಗೆ ದಾನ ಮಾಡಿದರು. ಹಸುಗಳ ಕೊಂಬುಗಳಿಗೆ ಚಿನ್ನ, ಗೊರಸುಗಳಿಗೆ ಹಿತ್ತಾಳೆ ಮತ್ತು ಬೆನ್ನಿಗೆ ಮುತ್ತುಗಳಿಂದ ಕೂಡಿದ ರೇಷ್ಮೆ ವಸ್ತ್ರಗಳನ್ನು ಹೊದಿಸಲಾಗಿತ್ತು. ಧಾನ್ಯದ ರಾಶಿಗಳನ್ನು, ಚಿನ್ನಾಭರಣಗಳನ್ನು ದಾನ ನೀಡಿದರು.

### ಬಾಲಕೃಷ್ಣನ ದರ್ಶನಕ್ಕೆ ಧಾವಿಸಿದ ಗೋಪಿಯರು

ಸುದ್ದಿ ಕೇಳಿದ ಗೋಪಿಯರು ಮನೆಗೆಲಸಗಳನ್ನು ಬಿಟ್ಟು, ಸುಂದರ ರೇಷ್ಮೆ ಸೀರೆ, ಒಡವೆಗಳನ್ನು ಧರಿಸಿ ನಂದಭವನಕ್ಕೆ ಧಾವಿಸಿದರು.

ಬಂಗಾರದ ತಟ್ಟೆಗಳಲ್ಲಿ ತಾಜಾ ಬೆಣ್ಣೆ, ಮೊಸರು, ಅರಿಶಿನ, ಕುಂಕುಮವನ್ನು ತಂದು ತೊಟ್ಟಿಲಲ್ಲಿದ್ದ ಕೃಷ್ಣನನ್ನು ಕಂಡು ಆಶೀರ್ವದಿಸಿದರು: "ಈ ಕಂದನು ಕೋಟಿ ವರ್ಷ ಬಾಳಿ ಗೋಕುಲವನ್ನು ಕಾಪಾಡಲಿ!"

### ಬೆಣ್ಣೆ, ಮೊಸರಿನ ರಂಗಿನಾಟ

ಗೋಪಾಲಕರು ಮೊಸರು, ಬೆಣ್ಣೆಯ ಗಡಿಗೆಗಳೊಂದಿಗೆ ಆಗಮಿಸಿದರು. ಪರಮಾನಂದದಿಂದ ಅವರು ಪರಸ್ಪರ ಮೊಸರು, ಹಾಲು, ಬೆಣ್ಣೆ, ಅರಿಶಿನದ ನೀರನ್ನು ಎರಚಿಕೊಂಡು ಸಂಭ್ರಮಿಸಿದರು:

> **ಶ್ರೀಮದ್ಭಾಗವತ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 5, ಶ್ಲೋಕ 14**
> 
> *ದಧಿ-ಕ್ಷೀರ-ಘೃತ-ಕ್ಷೋದೈಃ ಸಿಕ್ತೋ ’ನ್ಯೋನ್ಯಂ ವಿಲೇಪನೈಃ |*  
> *ಚಿಕ್ಷಿಪುಸ್ ತರಸಾ ಗೋಪಾ ದಧಿ-ಭಾಂಡಾನ್ಯ್ ಉದೀರಯನ್ ||*  
> 
> **ಭಾವಾರ್ಥ:** "ಆನಂದದಲ್ಲಿ ಮೈಮರೆತ ಗೋಪಾಲಕರು ಪರಸ್ಪರ ಮೊಸರು, ಹಾಲು, ತುಪ್ಪ, ಅರಿಶಿನದ ನೀರನ್ನು ಎರಚಿಕೊಂಡರು. ಮೊಸರಿನ ಮಡಕೆಗಳನ್ನು ಒಡೆದು ಒಬ್ಬರಿಗೊಬ್ಬರು ಬೆಣ್ಣೆ ಹಚ್ಚಿಕೊಳ್ಳುತ್ತಾ ನರ್ತಿಸಿದರು."

ಅಂಗಳವೆಲ್ಲ ಹಾಲಿನ ಕಡಲಿನಂತಾಯಿತು. ಮೃದಂಗ, ಕೊಳಲುಗಳ ನಾದದಿಂದ ಗೋಕುಲವು ಕಂಗೊಳಿಸಿತು. ಯಶೋದಾದೇವಿ ಮತ್ತು ರೋಹಿಣಿದೇವಿಯರು ಎಲ್ಲರಿಗೂ ವಸ್ತ್ರ, ಆಭರಣಗಳನ್ನು ದಾನ ಮಾಡಿದರು. ಶ್ರೀಕೃಷ್ಣನ ಆಗಮನದಿಂದ ಗೋಕುಲವು ಸಕಲ ಸಂಪತ್ತುಗಳಿಂದ ಶೋಭಿಸಿತು.""",
                "questions": [
                    {
                        "question": "ಗೋಕುಲದಲ್ಲಿ ಬೆಳಗಾಗುತ್ತಿದ್ದಂತೆ ಹರಡಿದ ಶುಭಸುದ್ದಿ ಯಾವುದು?",
                        "options": [
                            {"text": "ನಂದ-ಯಶೋದೆಯರಿಗೆ ಗಂಡು ಮಗು ಜನಿಸಿದೆ ಎಂದು", "is_correct": True},
                            {"text": "ಮಥುರೆಯಲ್ಲಿ ಹೊಸ ರಾಜ ಬಂದನೆಂದು", "is_correct": False},
                            {"text": "ಚಿನ್ನದ ಗಣಿ ಸಿಕ್ಕಿತೆಂದು", "is_correct": False},
                            {"text": "ಪ್ರವಾಹ ಬಂದಿತೆಂದು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಶ್ರೀಕೃಷ್ಣನ ಜನ್ಮದ ಅಂಗವಾಗಿ ಗೋಕುಲದಲ್ಲಿ ನಡೆದ ಉತ್ಸವದ ಹೆಸರೇನು?",
                        "options": [
                            {"text": "ನಂದೋತ್ಸವ", "is_correct": True},
                            {"text": "ರಥಯಾತ್ರೆ", "is_correct": False},
                            {"text": "ಗೋವರ್ಧನ ಪೂಜೆ", "is_correct": False},
                            {"text": "ಹೋಳಿ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ನಂದಮಹಾರಾಜರು ಮಗುವಿಗಾಗಿ ನಡೆಸಿದ ವೈದಿಕ ಸಂಸ್ಕಾರ ಯಾವುದು?",
                        "options": [
                            {"text": "ಜಾತಕರ್ಮ ಸಂಸ್ಕಾರ", "is_correct": True},
                            {"text": "ಉಪನಯನ", "is_correct": False},
                            {"text": "ವಿವಾಹ", "is_correct": False},
                            {"text": "ಸನ್ಯಾಸ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ನಂದಮಹಾರಾಜರು ಬ್ರಾಹ್ಮಣರಿಗೆ ಎಷ್ಟು ಹಸುಗಳನ್ನು ದಾನ ಮಾಡಿದರು?",
                        "options": [
                            {"text": "ಎರಡು ಲಕ್ಷ ಹಸುಗಳನ್ನು", "is_correct": True},
                            {"text": "10 ಹಸುಗಳನ್ನು ಮಾತ್ರ", "is_correct": False},
                            {"text": "500 ಹಸುಗಳನ್ನು", "is_correct": False},
                            {"text": "1,000 ಹಸುಗಳನ್ನು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ದಾನ ಮಾಡಿದ ಹಸುಗಳನ್ನು ಹೇಗೆ ಅಲಂಕರಿಸಲಾಗಿತ್ತು?",
                        "options": [
                            {"text": "ಚಿನ್ನದ ಕೊಂಬುಗಳು, ಹಿತ್ತಾಳೆಯ ಗೊರಸುಗಳು, ಮುತ್ತಿನ ರೇಷ್ಮೆ ವಸ್ತ್ರಗಳಿಂದ", "is_correct": True},
                            {"text": "ಕಬ್ಬಿಣದ ಸರಪಳಿಗಳಿಂದ", "is_correct": False},
                            {"text": "ಚರ್ಮದ ಹಗ್ಗಗಳಿಂದ", "is_correct": False},
                            {"text": "ಕೇವಲ ನವಿಲುಗರಿಗಳಿಂದ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಗೋಪಿಯರು ತಟ್ಟೆಯಲ್ಲಿ ತಂದ ಮಂಗಳಕರ ವಸ್ತುಗಳು ಯಾವುವು?",
                        "options": [
                            {"text": "ಬೆಣ್ಣೆ, ಮೊಸರು, ಅರಿಶಿನ, ಕುಂಕುಮ", "is_correct": True},
                            {"text": "ಆಯುಧಗಳು", "is_correct": False},
                            {"text": "ಮದ್ಯ", "is_correct": False},
                            {"text": "ನಾಣ್ಯಗಳು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಗೋಪಿಯರು ಬಾಲಕೃಷ್ಣನಿಗೆ ನೀಡಿದ ಆಶೀರ್ವಾದವೇನು?",
                        "options": [
                            {"text": "ಈ ಮಗು ಕೋಟಿ ವರ್ಷ ಬಾಳಿ ಗೋಕುಲವನ್ನು ರಕ್ಷಿಸಲಿ ಎಂದು", "is_correct": True},
                            {"text": "ಯುದ್ಧ ಗೆಲ್ಲಲಿ ಎಂದು", "is_correct": False},
                            {"text": "ದೊಡ್ಡ ವ್ಯಾಪಾರಿಯಾಗಲಿ ಎಂದು", "is_correct": False},
                            {"text": "ಗೋಕುಲ ಬಿಟ್ಟು ಹೋಗಲಿ ಎಂದು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಉತ್ಸವದಲ್ಲಿ ಗೋಪಾಲಕರು ಯಾವ ಆಟವಾಡಿದರು?",
                        "options": [
                            {"text": "ಮೊಸರು, ಹಾಲು, ಬೆಣ್ಣೆ, ಅರಿಶಿನದ ನೀರನ್ನು ಪರಸ್ಪರ ಎರಚಿಕೊಂಡರು", "is_correct": True},
                            {"text": "ಕತ್ತಿ ಕಾಳಗ ಮಾಡಿದರು", "is_correct": False},
                            {"text": "ಜೂಜಾಡಿದರು", "is_correct": False},
                            {"text": "ಮಲಗಿಕೊಂಡರು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ದಾನ ವಿತರಣೆಯಲ್ಲಿ ಯಶೋದೆಯೊಂದಿಗೆ ನೆರವಾದವರು ಯಾರು?",
                        "options": [
                            {"text": "ರೋಹಿಣಿದೇವಿ", "is_correct": True},
                            {"text": "ದೇವಕಿ", "is_correct": False},
                            {"text": "ಕುಂತಿ", "is_correct": False},
                            {"text": "ಗಾಂಧಾರಿ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಭಾಗವತದ ಹತ್ತನೇ ಸ್ಕಂಧದ ಯಾವ ಅಧ್ಯಾಯದಲ್ಲಿ ನಂದೋತ್ಸವವನ್ನು ವರ್ಣಿಸಲಾಗಿದೆ?",
                        "options": [
                            {"text": "ಅಧ್ಯಾಯ 5", "is_correct": True},
                            {"text": "ಅಧ್ಯಾಯ 1", "is_correct": False},
                            {"text": "ಅಧ್ಯಾಯ 3", "is_correct": False},
                            {"text": "ಅಧ್ಯಾಯ 8", "is_correct": False}
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

        self.stdout.write(self.style.SUCCESS(f"Successfully populated Story 13 (ID: {story.id}) across all 7 languages!"))
