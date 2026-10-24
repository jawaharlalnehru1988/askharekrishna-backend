import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askharekrishna_backend.settings')
django.setup()

from django.core.management.base import BaseCommand
from stories.models import StoryMainTopic, Story, StoryTranslation, StoryQuestion, StoryQuestionOption

class Command(BaseCommand):
    help = "Populate Story 10: Kamsa and the Eight-Armed Goddess Durga across 7 languages"

    def handle(self, *args, **options):
        topic = StoryMainTopic.objects.get(name="Krishna Pastimes")

        story_slug = "krishna-pastimes-kamsa-and-the-eight-armed-goddess-durga"
        image_path = "stories/images/kamsa_goddess_durga.jpg"

        story, created = Story.objects.get_or_create(
            slug=story_slug,
            defaults={
                "topic": topic,
                "order": 9,
                "imagePath": image_path,
            }
        )
        if not created:
            story.topic = topic
            story.order = 9
            story.imagePath = image_path
            story.save()

        stories_data = {
            "en": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "Kamsa and the Eight-Armed Goddess Durga",
                "content": """### Dawn in Mathura and Kamsa's Panic

As the first golden rays of dawn touched the stone fortress of Mathura, the newborn infant girl lying in Devaki's lap began to cry loudly. The hypnotic slumber cast over the prison guards by Yogamāyā wore off. Rubbing their eyes and jumping to their feet in alarm, the sentries heard the infant's cries coming from the cell.

Remembering King Kamsa's strict, life-or-death order that he must be informed the instant Devaki gave birth to her eighth child, the terrified guards ran at top speed to the royal palace. They burst into Kamsa's chamber, breathlessly announcing: "O King! The eighth child has been born to Devaki!"

Upon hearing these words, King Kamsa sprang from his bed in utter dread. All his limbs trembled violently, his hair stood on end, and he snatched his gleaming sword. Looking like personified death, wild with terror, Kamsa rushed through the palace corridors straight to the prison dungeon.

### Mother Devaki's Desperate Pleading

Bursting through the heavy iron doors into the dark cell, Kamsa saw Mother Devaki clutching her newborn child tightly against her chest. Devaki was trembling with maternal grief and terror. 

Falling to her knees before her cruel brother, Mother Devaki wept bitterly, begging for the life of the innocent child: "My dear brother Kamsa, please do not slay this infant! This child is a female, a girl! The celestial voice foretold that your death would be caused by an eighth son, not a daughter. A female child can never cause you any harm in battle. She will be your niece, a daughter to you! I have already offered my first six sons to your cruel hands, and the seventh child was lost. I am now childless and brokenhearted. Please, I beg you with folded hands, leave this one helpless baby girl as solace for my old age!"

### Kamsa's Merciless Cruelty

Devaki's agonizing tears and heartfelt lamentations would have melted even a heart of stone, but Kamsa was thoroughly consumed by demonic fear and cruelty. Deaf to all moral principles, brotherly affection, and natural mercy, Kamsa ruthlessly scolded his sister. 

Stepping forward with brutal force, Kamsa snatched the crying baby girl out of Devaki's arms by her tiny feet. With cold, venomous fury, Kamsa raised the infant high above his head and violently hurled her downward against a massive slab of stone to smash her to pieces, just as he had mercilessly slaughtered Devaki's previous infants.

### The Appearance of Eight-Armed Goddess Durgā

At that very instant, an astounding, terrifying cosmic miracle occurred before Kamsa's eyes!

The infant girl did not strike the stone slab. Instead, she miraculously slipped straight out of Kamsa's grasp and soared gracefully high into the morning sky. Enveloped in a blinding, golden-red celestial effulgence that illuminated the entire sky of Mathura, she revealed her true, majestic identity:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 4, Verse 9**
> 
> *sā tad-dhastāt samutpatya sadyo devy ambaraṁ gatā*  
> *adṛśyatānujā viṣṇoḥ sāyudhāṣṭa-mahā-bhujā*  
> 
> **Translation:** The child slipped from Kamsa's hands and immediately ascended into the sky. She appeared as Goddess Durgā (the younger sister of Lord Viṣṇu), equipped with weapons in her eight huge, transcendental arms.

She stood resplendent in the sky, adorned with magnificent celestial silks, flower garlands of heavenly Parijata blossoms, and precious jewels. In her eight powerful arms, she held a bow, trident (*triśūla*), arrows, shield, gleaming sword, conchshell, disc (*cakra*), and club. Celestial demigods, Siddhas, and Gandharvas hovered in the clouds around her, offering fragrant flower garlands and reciting Vedic hymns in her praise.

### The Cosmic Warning

Looking down upon King Kamsa with flashing, fiery eyes and an amused, mocking laugh, the supreme goddess addressed the terrified demon:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 4, Verse 12**
> 
> *kiṁ mayā hatayā manda jātaḥ khalu tavānta-kṛt*  
> *yatra kva vā pūrva-śatrus taṁ mā hiṁsīḥ kathañcana*  
> 
> **Translation:** O foolish demon Kamsa! What will you gain by trying to kill me? The Supreme Lord, who is destined to be your slayer—your eternal enemy from past lives—has already taken birth elsewhere! Therefore, do not needlessly persecute or slaughter other innocent children!

Having delivered this thunderous warning to King Kamsa, the goddess Durgā (Yogamāyā) disappeared from mortal sight. She became renowned throughout the universe under various sacred names such as Durgā, Bhadrakālī, Vijayā, Vaiṣṇavī, Kumudā, Caṇḍikā, Kṛṣṇā, Mādhavī, Kanyā, and Māyā, honored by devotees everywhere with temples and devotional offerings.

Below in the courtyard, King Kamsa collapsed onto the stone floor, his crown knocked askew and his sword fallen from his trembling fingers, utterly paralyzed by shock, cosmic humiliation, and dread.""",
                "questions": [
                    {
                        "question": "What caused the prison guards to awaken at dawn?",
                        "options": [
                            {"text": "The loud crying of the newborn infant girl in Devaki's lap", "is_correct": True},
                            {"text": "A loud blast of a royal trumpet", "is_correct": False},
                            {"text": "An earthquake shaking the fortress", "is_correct": False},
                            {"text": "Kamsa shouting outside the cell", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How did King Kamsa react when the guards told him Devaki's eighth child was born?",
                        "options": [
                            {"text": "He sprang from bed trembling with terror, hair on end, and rushed with sword drawn", "is_correct": True},
                            {"text": "He celebrated with wine and music", "is_correct": False},
                            {"text": "He went back to sleep peacefully", "is_correct": False},
                            {"text": "He ordered the guards to reward Devaki", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What key argument did Mother Devaki make to plead for the child's life?",
                        "options": [
                            {"text": "The baby is a female child and can cause Kamsa no harm in battle", "is_correct": True},
                            {"text": "The baby had golden hair", "is_correct": False},
                            {"text": "The baby was promised to the demigods", "is_correct": False},
                            {"text": "Vasudeva offered gold in exchange", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What cruel action did Kamsa attempt against the infant girl?",
                        "options": [
                            {"text": "He snatched her by the feet and hurled her against a stone slab", "is_correct": True},
                            {"text": "He threw her into the Yamuna river", "is_correct": False},
                            {"text": "He locked her in an iron box", "is_correct": False},
                            {"text": "He gave her poison", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What happened when Kamsa hurled the baby girl toward the stone?",
                        "options": [
                            {"text": "She slipped from his hands and ascended into the sky as eight-armed Goddess Durga", "is_correct": True},
                            {"text": "She shattered the stone into pieces", "is_correct": False},
                            {"text": "She disappeared into a cloud of smoke", "is_correct": False},
                            {"text": "She struck the stone and cried", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How many arms did Goddess Durga manifest in the sky?",
                        "options": [
                            {"text": "Eight arms holding celestial weapons", "is_correct": True},
                            {"text": "Two arms holding lotus flowers", "is_correct": False},
                            {"text": "Four arms holding scriptures", "is_correct": False},
                            {"text": "A thousand arms", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What weapons and items did Goddess Durga hold in her eight hands?",
                        "options": [
                            {"text": "Trident, bow, arrows, sword, shield, conch, disc, and club", "is_correct": True},
                            {"text": "Only books and water pots", "is_correct": False},
                            {"text": "A flute and peacock feather", "is_correct": False},
                            {"text": "A golden plough and pestle", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What momentous truth did Goddess Durga reveal to Kamsa?",
                        "options": [
                            {"text": "The Supreme Lord destined to slay him has already been born elsewhere", "is_correct": True},
                            {"text": "Kamsa would live forever as king", "is_correct": False},
                            {"text": "The demigods had surrendered to him", "is_correct": False},
                            {"text": "Vasudeva was his real father", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What advice did Goddess Durga give Kamsa regarding other children?",
                        "options": [
                            {"text": "Do not needlessly persecute or harm other innocent children", "is_correct": True},
                            {"text": "Imprison all children in Mathura", "is_correct": False},
                            {"text": "Adopt all newborn boys", "is_correct": False},
                            {"text": "Perform a child sacrifice", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How is Goddess Durga identified in relation to the Supreme Lord in this verse?",
                        "options": [
                            {"text": "Anuja Vishnoh (the younger sister of Lord Vishnu / Yogamaya)", "is_correct": True},
                            {"text": "The creator of Lord Vishnu", "is_correct": False},
                            {"text": "An enemy of Lord Vishnu", "is_correct": False},
                            {"text": "A mortal princess of Mathura", "is_correct": False}
                        ]
                    }
                ]
            },
            "ta": {
                "mainTopic": "கிருஷ்ண லீலைகள்",
                "subTopic": "கம்சனும் எட்டு கரங்களைக் கொண்ட துர்கா தேவியும்",
                "content": """### மதுராவில் விடியலும் கம்சனின் நடுக்கமும்

மதுராவின் சிறைச்சாலை மீது அதிகாலையின் பொற்கதிர்கள் படர்ந்தபோது, தாய் தேவகியின் மடியில் கிடந்த பச்சிளம் பெண் குழந்தை உரக்க அழத் தொடங்கியது. பகவானின் யோகமாயா சக்தியினால் சிறைக் காவலர்களை ஆட்கொண்டிருந்த மாய நித்திரை விலகியது. கண்களைக் கசக்கியபடி பதறியெழுந்த காவலர்கள், சிறைக் கொட்டடியிலிருந்து குழந்தையின் அழுகுரலைக் கேட்டனர்.

தேவகியின் எட்டாவது குழந்தை பிறந்த மறுகணமே தமக்குத் தெரிவிக்க வேண்டும் என்ற கம்சனின் கொடூரமான கட்டளையை நினைவுகூர்ந்த காவலர்கள், பயந்து நடுங்கியபடி அரசவைக்கு ஓடினர். கம்சனின் அந்தப்புரத்தினுள் நுழைந்த அவர்கள் மூச்சிரைக்கக் கூறினர்: "மன்னரே! தேவகிக்கு எட்டாவது குழந்தை பிறந்துவிட்டது!"

இதைக் கேட்ட கணமே கம்சனுக்கு மரண பயம் கவ்வியது. அவனது உடல் முழுவதும் நடுங்கியது; ரோமங்கள் சிலிர்த்தன. பயங்கரமான வாளை உருவியபடி, எமதர்மனைப் போல கண்களில் வெறியோடு சிறைச்சாலை நோக்கி கம்சன் விரைந்தான்.

### அன்னை தேவகியின் கண்ணீர் மன்றாடல்

சிறைக் கொட்டடியினுள் இடிபோல நுழைந்த கம்சன், தேவகி தனது குழந்தையை நெஞ்சோடு அணைத்துப் பிடித்திருப்பதை கண்டான். தனது கொடுங்கோல் சகோதரனின் கால்களில் விழுந்து தேவகி கதறி அழுதாள்:

"அன்பான சகோதரனே கம்சா! தயவுசெய்து இந்த பச்சிளம் குழந்தையைக் கொல்லாதே! இது ஒரு பெண் குழந்தை! எட்டாவது ஆண் மகனால் மட்டுமே உனக்கு மரணம் என்று அசரீரி கூறியது. ஒரு பெண் குழந்தையால் போர்க்களத்தில் உனக்கு எவ்வித ஆபத்தும் வர முடியாது. இவள் உனது மருமகள், உனக்கும் ஒரு மகளைப் போன்றவள்! ஏற்கனவே எனது ஆறு மகன்களை உனது கொடூர கரங்களில் பலிகொடுத்துவிட்டேன்; ஏழாவது குழந்தையையும் இழந்துவிட்டேன். என் மடியில் எஞ்சியிருக்கும் இந்த ஒரே ஒரு பெண் குழந்தையையாவது எனது முதுமைக்கால ஆறுதலுக்காக விட்டுவிடு, உன் காலில் விழுந்து மன்றாடுகிறேன்!"

### கம்சனின் கொடூர செயல்

கல்லையும் கரைக்கவல்ல தேவகியின் கண்ணீரைக் கண்டும், அசுர பயத்தால் மதிமயங்கிய கம்சனின் மனம் சிறிதும் இரங்கவில்லை. தர்ம நெறிகளையும், சகோதர பாசத்தையும், இயற்கையான இரக்கத்தையும் காற்றில் பறக்கவிட்ட கம்சன், தேவகியைக் கடுமையாக ஏசினான்.

முன்னேறிச் சென்று, தேவகியின் கரங்களிலிருந்து அந்த பச்சிளம் பெண் குழந்தையின் கால்களைப் பிடித்து பலவந்தமாகப் பறித்தான். நச்சுப் பாம்பைப் போன்ற கொடூர வெறியோடு, குழந்தையை தலைக்கு மேல் தூக்கி, முன்னைய குழந்தைகளை பாறையில் அடித்துக் கொன்றது போலவே, ஒரு பெரிய கருங்கல் பாறையின் மீது ஓங்கி வீசி எறிந்தான்!

### எட்டு கரங்களுடன் தோன்றிய துர்கா தேவி

அந்த கணமே, கம்சனின் கண்களுக்கு முன்னே உலகமே நடுங்கும் மாபெரும் திவ்ய அற்புதம் நிகழ்ந்தது!

அந்த பச்சிளம் பெண் குழந்தை பாறையின் மீது மோதவில்லை. மாறாக, கம்சனின் கைகளிலிருந்து நழுவி, உடனே ஆகாயத்திற்குள் பாய்ந்து சென்றாள்! மதுராவின் வானத்தையே ஒளிவெள்ளத்தில் ஆழ்த்திய பொன்னிற-சிவப்பு திவ்ய ஜோதியோடு, அவள் தனது உண்மையான திவ்ய சொரூபத்தை வெளிப்படுத்தினாள்:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 4, சுலோகம் 9**
> 
> *ஸா தத்-தஸ்தாத் ஸமுத்பத்ய ஸத்யோ தேவ்யம்பரம் கதா |*  
> *அத்ருஶ்யதானுஜா விஷ்ணோ: ஸாயுதாஷ்ட-மஹா-புஜா ||*  
> 
> **பொருள்:** அந்த குழந்தை கம்சனின் கைகளிலிருந்து நழுவி, உடனே ஆகாயத்திற்குள் உயர்ந்தாள். பகவான் ஸ்ரீ விஷ்ணுவின் இளைய சகோதரியான துர்கா தேவியாக, எட்டு பெரிய திவ்ய கரங்களில் திவ்ய ஆயுதங்களைத் தாங்கியவளாக அவள் காட்சியளித்தாள்.

அவள் திவ்ய பட்டாடைகளாலும், பாரிஜாத மலர் மாலைகளாலும், ஒளிரும் ஆபரணங்களாலும் அலங்கரிக்கப்பட்டு ஆகாயத்தில் கம்பீரமாக நின்றாள். தனது எட்டு கரங்களில் வில், திரிசூலம், அம்புகள், கேடயம், சுடர்விடும் வாள், சங்கு, சக்கரம், கதை ஆகியவற்றை ஏந்தியிருந்தாள். தேவர்களும் சித்தர்களும் கந்தர்வர்களும் அவளைச் சூழ்ந்து மலர்களைத் தூவி வேத மந்திரங்களால் போற்றினர்.

### கம்சனுக்கு விடுக்கப்பட்ட எச்சரிக்கை

பயந்து நடுங்கிய கம்சனை எள்ளி நகையாடி, சுடர்விடும் கண்களோடு அந்த திவ்ய தேவி கர்ஜித்தாள்:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 4, சுலோகம் 12**
> 
> *கிம் மயா ஹதயா மந்த ஜாத: கலு தவாந்த-க்ருத் |*  
> *யத்ர க்வ வா பூர்வ-ஶத்ருஸ் தம் மா ஹிம்ஸீ: கதஞ்சன ||*  
> 
> **பொருள்:** மூடனான கம்சா! என்னைக் கொல்வதால் உனக்கு என்ன பயன் கிடைக்கப்போகிறது? உன்னை வதம் செய்யப்போகும் முழுமுதற் கடவுளான பகவான்—உனது பூர்வஜென்ம நித்திய எதிரி—ஏற்கனவே வேறிடத்தில் பிறந்துவிட்டார்! எனவே, வீணாக பிற நிரபராதி குழந்தைகளை துன்புறுத்தாதே!

கம்சனுக்கு இந்த இடி போன்ற எச்சரிக்கையை விடுத்த பின்னர், துர்கா தேவி (யோகமாயா) மறைந்தருளினாள். துர்கா, பத்ரகாளி, விஜயா, வைஷ்ணவி, குமுதா, சண்டிகா, கிருஷ்ணா, மாதவி, கன்யா, மாயா என்ற திருநாமங்களுடன் அகிலமெங்கும் போற்றப்பட்டு பக்தர்களால் வழிபடப்படுகிறாள்.

கீழே சிறைச்சாலை முற்றத்தில், கிரீடம் கீழே உருள, கை வாள் நழுவி விழ, எல்லையற்ற அதிர்ச்சியிலும் அவமானத்திலும் மரண பயத்திலும் கம்சன் தரையில் சுருண்டு விழுந்தான்.""",
                "questions": [
                    {
                        "question": "விடியற்காலையில் சிறைக் காவலர்கள் எதனால் விழித்தெழுந்தனர்?",
                        "options": [
                            {"text": "தேவகியின் மடியில் இருந்த பச்சிளம் பெண் குழந்தையின் அழுகுரல் கேட்டு", "is_correct": True},
                            {"text": "அரச எக்காள சத்தம் கேட்டு", "is_correct": False},
                            {"text": "பூகம்ப அதிர்வால்", "is_correct": False},
                            {"text": "கம்சனின் கூச்சல் கேட்டு", "is_correct": False}
                        ]
                    },
                    {
                        "question": "எட்டாவது குழந்தை பிறந்துவிட்டது என்ற செய்தியைக் கேட்ட கம்சனின் நிலை என்ன?",
                        "options": [
                            {"text": "உடல் நடுங்கி, மயிர் சிலிர்த்து, பயங்கர வாளோடு சிறையை நோக்கி ஓடினான்", "is_correct": True},
                            {"text": "மகிழ்ச்சியில் இசை பாடினான்", "is_correct": False},
                            {"text": "அமைதியாக உறங்கினான்", "is_correct": False},
                            {"text": "தேவகிக்கு பரிசுகள் வழங்கினான்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "குழந்தையைக் காப்பாற்ற தேவகி கம்சனிடம் கூறிய முக்கிய காரணம் என்ன?",
                        "options": [
                            {"text": "இது ஒரு பெண் குழந்தை, போர்க்களத்தில் உனக்கு எவ்வித ஆபத்தும் செய்யாது", "is_correct": True},
                            {"text": "குழந்தைக்கு தங்க முடி இருந்தது", "is_correct": False},
                            {"text": "குழந்தையை தேவர்களுக்கு தருவதாகக் கூறினாள்", "is_correct": False},
                            {"text": "வசுதேவர் பொன் தருவதாகக் கூறினார்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பச்சிளம் பெண் குழந்தையைக் கொல்ல கம்சன் என்ன செய்தான்?",
                        "options": [
                            {"text": "கால்களைப் பிடித்து தூக்கி பாறையின் மீது ஓங்கி வீசி எறிந்தான்", "is_correct": True},
                            {"text": "யமுனை நதியில் வீசினான்", "is_correct": False},
                            {"text": "இரும்புப் பெட்டியில் அடைத்தான்", "is_correct": False},
                            {"text": "விஷம் கொடுத்தான்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "குழந்தையை பாறையில் எறிந்தபோது என்ன அற்புதம் நிகழ்ந்தது?",
                        "options": [
                            {"text": "கை நழுவி ஆகாயத்தில் எட்டு கரங்கள் கொண்ட துர்கா தேவியாகத் தோன்றினாள்", "is_correct": True},
                            {"text": "பாறை சுக்குநூறாக உடைந்தது", "is_correct": False},
                            {"text": "புகையாக மறைந்தது", "is_correct": False},
                            {"text": "பாறையில் பட்டு அழுதது", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ஆகாயத்தில் தோன்றிய தேவிக்கு எத்தனை கரங்கள் இருந்தன?",
                        "options": [
                            {"text": "ஆயுதங்கள் தாங்கிய எட்டு கரங்கள்", "is_correct": True},
                            {"text": "இரண்டு கரங்கள்", "is_correct": False},
                            {"text": "நான்கு கரங்கள்", "is_correct": False},
                            {"text": "ஆயிரம் கரங்கள்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "துர்கா தேவி தனது கரங்களில் ஏந்தியிருந்த ஆயுதங்கள் யாவை?",
                        "options": [
                            {"text": "வில், அம்பு, சூலம், வாள், கேடயம், சங்கு, சக்கரம், கதை", "is_correct": True},
                            {"text": "புத்தகம் மற்றும் கமண்டலம் மட்டும்", "is_correct": False},
                            {"text": "புல்லாங்குழல்", "is_correct": False},
                            {"text": "கலப்பை மற்றும் உலக்கை", "is_correct": False}
                        ]
                    },
                    {
                        "question": "கம்சனிடம் தேவி வெளிப்படுத்திய திடுக்கிடும் உண்மை என்ன?",
                        "options": [
                            {"text": "உன்னை வதம் செய்யப்போகும் பகவான் ஏற்கனவே வேறிடத்தில் பிறந்துவிட்டார்", "is_correct": True},
                            {"text": "கம்சன் என்றும் சாகமாட்டான்", "is_correct": False},
                            {"text": "தேவர்கள் சரணடைந்துவிட்டனர்", "is_correct": False},
                            {"text": "வசுதேவரே அவனது தந்தை", "is_correct": False}
                        ]
                    },
                    {
                        "question": "மற்ற குழந்தைகளைப் பற்றி கம்சனுக்கு தேவி கூறிய அறிவுரை என்ன?",
                        "options": [
                            {"text": "வீணாக பிற நிரபராதி குழந்தைகளை துன்புறுத்தாதே", "is_correct": True},
                            {"text": "எல்லா குழந்தைகளையும் சிறையில் அடை", "is_correct": False},
                            {"text": "குழந்தைகளை தத்தெடு", "is_correct": False},
                            {"text": "குழந்தைப் பலி கொடு", "is_correct": False}
                        ]
                    },
                    {
                        "question": "சாஸ்திரத்தில் இந்த தேவி பகவானுக்கு எவ்வாறு குறிப்பிடப்படுகிறாள்?",
                        "options": [
                            {"text": "அனுஜா விஷ்ணோ: (பகவான் விஷ்ணுவின் இளைய சகோதரி / யோகமாயா)", "is_correct": True},
                            {"text": "விஷ்ணுவை சிருஷ்டித்தவள்", "is_correct": False},
                            {"text": "விஷ்ணுவின் எதிரி", "is_correct": False},
                            {"text": "மதுராவின் மானிட இளவரசி", "is_correct": False}
                        ]
                    }
                ]
            },
            "hi": {
                "mainTopic": "कृष्ण लीलाएं",
                "subTopic": "कंस और अष्टभुजा दुर्गा देवी का प्राकट्य",
                "content": """### प्रभात वेला और कंस का आतंक

मथुरा के कारागार पर जब प्रभात की प्रथम किरणें पड़ीं, तो देवकी की गोद में रखी नवजात कन्या जोर-जोर से रोने लगी। योगमाया के प्रभाव से सोए हुए पहरेदारों की निद्रा टूटी। आंखें मलते हुए जब वे उठे, तो कारागार से शिशु के रोने का स्वर आ रहा था।

कंस के इस कठोर आदेश को याद करते हुए कि देवकी की आठवीं संतान के जन्म लेते ही तुरंत सूचित किया जाए, भयभीत पहरेदार राजमहल की ओर भागे। उन्होंने कंस के कक्ष में प्रवेश कर हांफते हुए कहा: "महाराज! देवकी की आठवीं संतान उत्पन्न हो चुकी है!"

यह सुनते ही कंस शय्या से उछल पड़ा। उसके सारे अंग कांपने लगे, रोंगटे खड़े हो गए। नंगी तलवार खींचकर, साक्षात् यमराज की भांति काल का रूप धरे, भय से व्याकुल कंस सीधे कारागार की ओर दौड़ा।

### माता देवकी की करुण याचना

कारागार में पहुंचकर कंस ने देखा कि देवकी नवजात बालिका को अपने वक्ष से चिपकाए कांप रही हैं। देवकी अपने क्रूर भाई के चरणों में गिर पड़ीं और विलाप करते हुए प्रार्थना करने लगीं:

"हे भ्राता कंस! कृपया इस नन्हीं बालिका का वध न करें! यह तो एक कन्या है। आकाशवाणी ने कहा था कि आपका वध आठवें पुत्र द्वारा होगा, कन्या द्वारा नहीं। एक स्त्री युद्ध में आपका क्या अहित कर सकती है? यह आपकी भतीजी है, आपकी पुत्री के समान है! मैंने अपने पहले छह पुत्र आपके हाथों में सौंप दिए, और सातवां नष्ट हो गया। अब मेरे इस बुढ़ापे के सहारे के लिए केवल इस एक कन्या को छोड़ दीजिए, मैं आपके हाथ जोड़ती हूं!"

### कंस की नृशंस क्रूरता

देवकी के इस विलाप से पाषाण भी पिघल जाता, परंतु कंस का हृदय आसुरी भय से सर्वथा कठोर हो चुका था। धर्म, भ्रातृ-प्रेम और स्वाभाविक दया को त्यागकर कंस ने देवकी को फटकारा।

उसने आगे बढ़कर देवकी की बांहों से उस रोती हुई नन्हीं कन्या को उसके कोमल पैरों से पकड़कर निर्दयतापूर्वक छीन लिया। अत्यंत विषैले क्रोध में उसने उस बालिका को अपने सिर के ऊपर उठाया और पूर्व बालकों की भांति एक विशाल शिलाखंड पर पटक कर टुकड़े-टुकड़े करने के लिए पूरी शक्ति से नीचे फेंका!

### अष्टभुजा दुर्गा देवी का प्राकट्य

उसी क्षण, कंस के सम्मुख एक अत्यंत विस्मयकारी और अलौकिक चमत्कार घटित हुआ!

वह बालिका शिला पर नहीं गिरी, अपितु कंस के हाथों से छूटकर सीधे आकाश की ओर उड़ गई! संपूर्ण मथुरा के आकाश को अपनी स्वर्णिम-अरुण प्रभा से आलोकित करते हुए उसने अपना वास्तविक भगवती स्वरूप प्रकट किया:

> **श्रीमद्भागवतम्, स्कंध 10, अध्याय 4, श्लोक 9**
> 
> *सा तद्धस्तात् समुत्पत्य सद्यो देव्यम्बरं गता ।*  
> *अदृश्यतानुजा विष्णोः सायुधाष्टमहाभुजा ॥*  
> 
> **भावार्थ:** वह बालिका कंस के हाथों से छूटकर तुरंत आकाश में चली गई। वह भगवान श्री विष्णु की अनुजा (छोटी बहन योगमाया) दुर्गा देवी के रूप में प्रकट हुईं, जिनकी आठ विशाल भुजाओं में दिव्य अस्त्र-शस्त्र सुशोभित थे।

वे आकाश में दिव्य परिधानों, पारिजात पुष्पों की मालाओं और जगमगाते आभूषणों से सुसज्जित होकर विराजमान थीं। अपनी आठ भुजाओं में उन्होंने धनुष, त्रिशूल, बाण, ढाल, चमचमाती तलवार, शंख, चक्र और गदा धारण कर रखी थी। आकाश में सिद्ध, गंधर्व और देवता पुष्पवर्षा करते हुए उनकी स्तुति कर रहे थे।

### कंस को दिव्य चेतावनी

कांपते हुए कंस की ओर अपनी प्रज्वलित दृष्टि डालते हुए और अट्टहास करते हुए भगवती दुर्गा ने कहा:

> **श्रीमद्भागवतम्, स्कंध 10, अध्याय 4, श्लोक 12**
> 
> *किं मया हतया मन्द जातः खलु तवान्तकृत् ।*  
> *यत्र क्व वा पूर्वशत्रुस् तं मा हिंसीः कथञ्चन ॥*  
> 
> **भावार्थ:** अरे मूर्ख कंस! मुझे मारने से तुझे क्या प्राप्त होगा? तेरा वध करने वाला पूर्ण पुरुषोत्तम भगवान्—तेरा पूर्व जन्मों का काल—कहीं और जन्म ले चुका है! अतः अब व्यर्थ ही अन्य निर्दोष बालकों पर अत्याचार मत कर!

कंस को यह भीषण चेतावनी देकर भगवती दुर्गा अंतर्ध्यान हो गईं। वे संसार में दुर्गा, भद्रकाली, विजया, वैष्णवी, कुमुदा, चंडिका, कृष्णा, माधवी, कन्या और माया जैसे पावन नामों से प्रसिद्ध हुईं और संपूर्ण जगत में पूजित हुईं।

नीचे कारागार के आंगन में कंस का मुकुट गिर गया, तलवार छूट गई और वह अत्यंत भय, लज्जा और सदमे से पत्थर की भांति भूमि पर गिर पड़ा।""",
                "questions": [
                    {
                        "question": "प्रभात वेला में पहरेदारों की नींद कैसे खुली?",
                        "options": [
                            {"text": "देवकी की गोद में नवजात कन्या के रोने का स्वर सुनकर", "is_correct": True},
                            {"text": "राजसी नगाड़े की आवाज से", "is_correct": False},
                            {"text": "भूकंप के झटके से", "is_correct": False},
                            {"text": "कंस के चिल्लाने से", "is_correct": False}
                        ]
                    },
                    {
                        "question": "आठवीं संतान के जन्म का समाचार सुनकर कंस की क्या दशा हुई?",
                        "options": [
                            {"text": "वह भय से कांप उठा, रोंगटे खड़े हो गए और तलवार लेकर कारागार की ओर दौड़ा", "is_correct": True},
                            {"text": "उसने उत्सव मनाया", "is_correct": False},
                            {"text": "वह शांति से सोता रहा", "is_correct": False},
                            {"text": "उसने देवकी को पुरस्कार भेजा", "is_correct": False}
                        ]
                    },
                    {
                        "question": "माता देवकी ने बच्ची की रक्षा के लिए क्या मुख्य तर्क दिया?",
                        "options": [
                            {"text": "यह एक कन्या है और युद्ध में कंस का कोई अहित नहीं कर सकती", "is_correct": True},
                            {"text": "बच्ची के बाल सुनहरे हैं", "is_correct": False},
                            {"text": "बच्ची देवताओं को समर्पित है", "is_correct": False},
                            {"text": "वसुदेव सोना देंगे", "is_correct": False}
                        ]
                    },
                    {
                        "question": "कंस ने उस नवजात कन्या के साथ क्या क्रूरता की?",
                        "options": [
                            {"text": "पैरों से पकड़कर शिला पर पटकने के लिए फेंका", "is_correct": True},
                            {"text": "यमुना में फेंक दिया", "is_correct": False},
                            {"text": "लोहे के बक्से में बंद किया", "is_correct": False},
                            {"text": "विष दे दिया", "is_correct": False}
                        ]
                    },
                    {
                        "question": "जब कंस ने बच्ची को शिला पर फेंका तो क्या चमत्कार हुआ?",
                        "options": [
                            {"text": "वह हाथ से छूटकर आकाश में अष्टभुजा दुर्गा के रूप में प्रकट हुई", "is_correct": True},
                            {"text": "शिला टूट गई", "is_correct": False},
                            {"text": "वह धुएं में बदल गई", "is_correct": False},
                            {"text": "शिला पर गिरकर रोने लगी", "is_correct": False}
                        ]
                    },
                    {
                        "question": "आकाश में प्रकट देवी की कितनी भुजाएं थीं?",
                        "options": [
                            {"text": "अस्त्र-शस्त्रों से सुसज्जित आठ भुजाएं", "is_correct": True},
                            {"text": "दो भुजाएं", "is_correct": False},
                            {"text": "चार भुजाएं", "is_correct": False},
                            {"text": "सहस्र भुजाएं", "is_correct": False}
                        ]
                    },
                    {
                        "question": "दुर्गा देवी ने अपने हाथों में कौन से प्रमुख आयुध धारण कर रखे थे?",
                        "options": [
                            {"text": "धनुष, बाण, त्रिशूल, तलवार, ढाल, शंख, चक्र और गदा", "is_correct": True},
                            {"text": "केवल पुस्तक और कमंडल", "is_correct": False},
                            {"text": "बांसुरी", "is_correct": False},
                            {"text": "हल और मूसल", "is_correct": False}
                        ]
                    },
                    {
                        "question": "दुर्गा देवी ने कंस को क्या चौंकाने वाला सत्य बताया?",
                        "options": [
                            {"text": "तेरा वध करने वाला शत्रु कहीं और जन्म ले चुका है", "is_correct": True},
                            {"text": "कंस कभी नहीं मरेगा", "is_correct": False},
                            {"text": "देवताओं ने हार मान ली है", "is_correct": False},
                            {"text": "वसुदेव ही उसके पिता हैं", "is_correct": False}
                        ]
                    },
                    {
                        "question": "देवी ने कंस को अन्य बालकों के संबंध में क्या चेतावनी दी?",
                        "options": [
                            {"text": "व्यर्थ ही अन्य निर्दोष बालकों पर अत्याचार मत कर", "is_correct": True},
                            {"text": "सभी बालकों को बंदी बना ले", "is_correct": False},
                            {"text": "सभी बालकों को गोद ले ले", "is_correct": False},
                            {"text": "बालक बलि दे", "is_correct": False}
                        ]
                    },
                    {
                        "question": "शास्त्र में इस देवी को भगवान श्री विष्णु से क्या संबंध बताया गया है?",
                        "options": [
                            {"text": "अनुजा विष्णोः (भगवान विष्णु की अनुजा बहन / योगमाया)", "is_correct": True},
                            {"text": "विष्णु की जननी", "is_correct": False},
                            {"text": "विष्णु की शत्रु", "is_correct": False},
                            {"text": "मथुरा की साधारण राजकुमारी", "is_correct": False}
                        ]
                    }
                ]
            },
            "ml": {
                "mainTopic": "കൃഷ്ണ ലീലകൾ",
                "subTopic": "കംസനും അഷ്ടഭുജ ദുർഗ്ഗാദേവിയും",
                "content": """### പ്രഭാതവും കംസന്റെ പരിഭ്രാന്തിയും

മഥുരയിലെ കാരാഗൃഹത്തിൽ പ്രഭാതകിരണങ്ങൾ വീണപ്പോൾ, ദേവകിയുടെ മടിയിൽ കിടന്ന പെൺകുഞ്ഞ് ഉറക്കെ കരയാൻ തുടങ്ങി. യോഗമായാപ്രഭാവത്താൽ ഉറങ്ങിപ്പോയ കാവൽക്കാർ ഞെട്ടിയുണർന്നു. കാരാഗൃഹത്തിൽ നിന്ന് കുഞ്ഞിന്റെ കരച്ചിൽ കേട്ട അവർ ഭയന്നുവിറച്ചു.

എട്ടാമത്തെ കുഞ്ഞ് ജനിച്ചയുടൻ അറിയിക്കണമെന്ന കംസന്റെ കഠിനമായ ആജ്ഞയോർത്ത് കാവൽക്കാർ കൊട്ടാരത്തിലേക്ക് ഓടി. അവർ കിതച്ചുകൊണ്ട് കംസനോട് പറഞ്ഞു: "മഹാരാജാവേ! ദേവകി എട്ടാമത്തെ കുഞ്ഞിന് ജന്മം നൽകിയിരിക്കുന്നു!"

ഇതുകേട്ട മാത്രയിൽ കംസൻ വിറച്ചുപോയി. ശരീരം തളരുകയും രോമാഞ്ചമുണ്ടാവുകയും ചെയ്തു. ഉറയിൽ നിന്ന് വാളൂരിയെടുത്ത്, യമനെപ്പോലെ രൗദ്രഭാവത്തിൽ കംസൻ കാരാഗൃഹത്തിലേക്ക് പാഞ്ഞെത്തി.

### മാതാ ദേവകിയുടെ കണ്ണീരപേക്ഷ

കാരാഗൃഹത്തിലെത്തിയ കംസൻ കണ്ടത് തന്റെ കുഞ്ഞിനെ നെഞ്ചോടുചേർത്ത് വിറച്ചുനിൽക്കുന്ന ദേവകിയെയാണ്. ക്രൂരനായ സഹോദരന്റെ കാൽക്കൽ വീണ് ദേവകി കരഞ്ഞു യാചിച്ചു:

"പ്രിയപ്പെട്ട സഹോദരാ! ഈ നിഷ്കളങ്കയായ കുഞ്ഞിനെ കൊല്ലരുതേ! ഇതൊരു പെൺകുഞ്ഞാണ്. എട്ടാമത്തെ ആൺകുഞ്ഞാണ് നിന്നെ വധിക്കുകയെന്നാണ് അശരീരി പറഞ്ഞത്. ഒരു പെൺകുഞ്ഞിന് നിന്നോട് യുദ്ധം ചെയ്യാനാകില്ല. ഇവൾ നിന്റെ മരുമകളാണ്. എന്റെ ആദ്യത്തെ ആറു മക്കളെയും നീ കൊന്നു, ഏഴാമത്തെ കുഞ്ഞിനെയും നഷ്ടപ്പെട്ടു. ഈ വാർദ്ധക്യത്തിൽ എനിക്കൊരാശ്വാസമായി ഈ പെൺകുഞ്ഞിനെയെങ്കിലും ജീവിക്കാൻ അനുവദിക്കൂ!"

### കംസന്റെ ക്രൂരത

പാറയെപ്പോലും അലിയിക്കുന്ന ദേവകിയുടെ വിലാപം കംസന്റെ അസുരഹൃദയത്തിൽ ഒരു മാറ്റവുമുണ്ടാക്കിയില്ല. ധർമ്മവും വാത്സല്യവും മറന്ന കംസൻ ദേവകിയെ ആട്ടിപ്പായിച്ചു.

അവൻ ആ കുഞ്ഞിന്റെ ഇളംകാലുകളിൽ പിടിച്ച് ദേവകിയുടെ മടിയിൽ നിന്നും തട്ടിയെടുത്തു. മുൻപത്തെ കുഞ്ഞുങ്ങളെപ്പോലെ ആ കുഞ്ഞിനെയും തലയ്ക്കുമുകളിലുയർത്തി പാറയിലേക്ക് ആഞ്ഞടിച്ചു!

### അഷ്ടഭുജ ദുർഗ്ഗാദേവിയുടെ ആവിർഭാവം

ആ നിമിഷത്തിൽ സകലരെയും അത്ഭുതപ്പെടുത്തിക്കൊണ്ട് ഒരു മഹാത്ഭുതം സംഭവിച്ചു!

കുഞ്ഞ് പാറയിൽ വീണില്ല; മറിച്ച്, കംസന്റെ കൈകളിൽ നിന്നും തെന്നിമാറി ആകാശത്തിലേക്ക് ഉയർന്നുപൊങ്ങി! സുവർണ്ണപ്രഭ പരത്തിക്കൊണ്ട് ആ കുഞ്ഞ് തന്റെ യഥാർത്ഥ ദിവ്യരൂപം വെളിപ്പെടുത്തി:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അദ്ധ്യായം 4, ശ്ലോകം 9**
> 
> *സാ തദ്ധസ്താത് സമുത്പത്യ സദ്യോ ദേവ്യമ്പരം ഗതാ |*  
> *അദൃശ്യതാനുജാ വിഷ്ണോഃ സായുധാഷ്ടമഹാഭുജാ ||*  
> 
> **അർത്ഥം:** ആ ശിശു കംസന്റെ കൈകളിൽ നിന്ന് തെന്നിമാറി ആകാശത്തേക്ക് ഉയർന്നു. ഭഗവാൻ വിഷ്ണുവിന്റെ അനുജത്തിയായ (യോഗമായയായ) ദുർഗ്ഗാദേവിയായി, ദിവ്യായുധങ്ങൾ ധരിച്ച എട്ടു തൃക്കൈകളോടെ അവൾ പ്രത്യക്ഷപ്പെട്ടു.

ആകാശത്തിൽ ദിവ്യാഭരണങ്ങളും പാരിജാതമാലകളും അണിഞ്ഞ് ദേവി ശോഭിച്ചു. തന്റെ എട്ടു കൈകളിൽ വില്ല്, അമ്പ്, തൃശ്ശൂലം, വാൾ, പരിച, ശംഖ്, ചക്രം, ഗദ എന്നിവ ധരിച്ചിരുന്നു. ദേവന്മാരും സിദ്ധന്മാരും പൂക്കൾ വർഷിച്ച് ദേവിയെ സ്തുതിച്ചു.

### കംസനുള്ള മുന്നറിയിപ്പ്

ഭയന്നുവിറച്ചുനിൽക്കുന്ന കംസനെ നോക്കി പരിഹാസത്തോടെ ദേവി പറഞ്ഞു:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അദ്ധ്യായം 4, ശ്ലോകം 12**
> 
> *കിം മയാ ഹതയാ മന്ദ ജാതഃ ഖലു തവാന്തകൃത് |*  
> *യത്ര ക്വ വാ പൂർവ്വശത്രുസ് തം മാ ഹിംസീഃ കഥഞ്ചന ||*  
> 
> **അർത്ഥം:** അല്ലയോ മൂഢനായ കംസാ! എന്നെ കൊല്ലാൻ ശ്രമിച്ചതുകൊണ്ട് നിനക്കെന്തു ലഭിക്കാൻ? നിന്നെ വധിക്കാനുള്ളവൻ—നിന്റെ പൂർവ്വജന്മശത്രുവായ പരമപുരുഷൻ—മറ്റൊരിടത്ത് ജനിച്ചുകഴിഞ്ഞു! അതിനാൽ മറ്റു നിരപരാധികളായ കുഞ്ഞുങ്ങളെ വെറുതെ ഉപദ്രവിക്കാതിരിക്കൂ!

ഇത്രയും പറഞ്ഞ് ദേവി അന്തർദ്ധാനം ചെയ്തു. ദുർഗ്ഗ, ഭദ്രകാളി, വിജയ, വൈഷ്ണവി, കുമുദ, ചണ്ഡിക, കൃഷ്ണ, മാധവി, കന്യ, മായ എന്നീ നാമങ്ങളിൽ ദേവി പ്രശസ്തയായി.

താഴെ കാരാഗൃഹത്തിൽ കിരീടം തെറിച്ചുവീണ്, വാളും നഷ്ടപ്പെട്ട് കംസൻ ഭയത്താൽ നിലത്തുപതിച്ചു.""",
                "questions": [
                    {
                        "question": "പ്രഭാതത്തിൽ കാവൽക്കാർ ഉണർന്നത് എന്തുകൊണ്ടാണ്?",
                        "options": [
                            {"text": "ദേവകിയുടെ മടിയിലുള്ള പെൺകുഞ്ഞിന്റെ കരച്ചിൽ കേട്ട്", "is_correct": True},
                            {"text": "കൊട്ടാരത്തിലെ കാഹളനാദം കേട്ട്", "is_correct": False},
                            {"text": "ഭൂകമ്പം ഉണ്ടായതുകൊണ്ട്", "is_correct": False},
                            {"text": "കംസന്റെ അലർച്ച കേട്ട്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "എട്ടാമത്തെ കുഞ്ഞ് ജനിച്ചതറിഞ്ഞ് കംസന് എന്തു സംഭവിച്ചു?",
                        "options": [
                            {"text": "ഭയത്താൽ വിറച്ച് വാളൂരി കാരാഗൃഹത്തിലേക്ക് പാഞ്ഞു", "is_correct": True},
                            {"text": "സന്തോഷിച്ച് പാട്ടുപാടി", "is_correct": False},
                            {"text": "ശാന്തമായി ഉറങ്ങി", "is_correct": False},
                            {"text": "ദേവകിക്ക് സമ്മാനങ്ങൾ നൽകി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "കുഞ്ഞിന്റെ ജീവനുവേണ്ടി ദേവകി പറഞ്ഞ പ്രധാന കാരണം എന്തായിരുന്നു?",
                        "options": [
                            {"text": "ഇതൊരു പെൺകുഞ്ഞാണ്, യുദ്ധത്തിൽ കംസന് യാതൊരു ദോഷവും ചെയ്യില്ല", "is_correct": True},
                            {"text": "കുഞ്ഞിന് സ്വർണ്ണമുടിയുണ്ട്", "is_correct": False},
                            {"text": "കുഞ്ഞിനെ ദേവന്മാർക്ക് നൽകാം", "is_correct": False},
                            {"text": "വസുദേവർ സ്വർണ്ണം തരാമെന്ന് പറഞ്ഞു", "is_correct": False}
                        ]
                    },
                    {
                        "question": "കംസൻ ആ പെൺകുഞ്ഞിനോട് ചെയ്ത ക്രൂരത എന്താണ്?",
                        "options": [
                            {"text": "കാലുകളിൽ പിടിച്ച് പാറയിലേക്ക് ആഞ്ഞടിച്ചു", "is_correct": True},
                            {"text": "യമുനയിലെറിഞ്ഞു", "is_correct": False},
                            {"text": "ഇരുമ്പുപെട്ടിയിലാക്കി", "is_correct": False},
                            {"text": "വിഷം കൊടുത്തു", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പാറയിലേക്ക് എറിഞ്ഞപ്പോൾ കുഞ്ഞിന് എന്തു സംഭവിച്ചു?",
                        "options": [
                            {"text": "കൈകളിൽ നിന്ന് തെന്നിമാറി ആകാശത്തിൽ അഷ്ടഭുജ ദുർഗ്ഗയായി പ്രത്യക്ഷപ്പെട്ടു", "is_correct": True},
                            {"text": "പാറ തകർന്നു", "is_correct": False},
                            {"text": "പുകയായി മാറി", "is_correct": False},
                            {"text": "പാറയിൽ വീണ് കരഞ്ഞു", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ആകാശത്തു പ്രത്യക്ഷപ്പെട്ട ദേവിക്ക് എത്ര കൈകളുണ്ടായിരുന്നു?",
                        "options": [
                            {"text": "ആയുധങ്ങൾ ധരിച്ച എട്ടു കൈകൾ", "is_correct": True},
                            {"text": "രണ്ടു കൈകൾ", "is_correct": False},
                            {"text": "നാലു കൈകൾ", "is_correct": False},
                            {"text": "ആയിരം കൈകൾ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ദുർഗ്ഗാദേവി കൈകളിൽ ധരിച്ചിരുന്ന ആയുധങ്ങൾ ഏവ?",
                        "options": [
                            {"text": "വില്ല്, അമ്പ്, തൃശ്ശൂലം, വാൾ, പരിച, ശംഖ്, ചക്രം, ഗദ", "is_correct": True},
                            {"text": "പുസ്തകവും കമണ്ഡലുവും മാത്രം", "is_correct": False},
                            {"text": "പുല്ലാങ്കുഴൽ", "is_correct": False},
                            {"text": "കലപ്പയും ഉലക്കയും", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ദേവി കംസനോട് വെളിപ്പെടുത്തിയ സത്യമെന്തായിരുന്നു?",
                        "options": [
                            {"text": "നിന്നെ വധിക്കാനുള്ളവൻ മറ്റൊരിടത്ത് ജനിച്ചുകഴിഞ്ഞു", "is_correct": True},
                            {"text": "കംസൻ ഒരിക്കലും മരിക്കില്ല", "is_correct": False},
                            {"text": "ദേവന്മാർ തോറ്റു", "is_correct": False},
                            {"text": "വസുദേവനാണ് അവന്റെ അച്ഛൻ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "മറ്റു കുഞ്ഞുങ്ങളെക്കുറിച്ച് ദേവി കംസന് നൽകിയ മുന്നറിയിപ്പ് എന്തായിരുന്നു?",
                        "options": [
                            {"text": "മറ്റു നിരപരാധികളായ കുഞ്ഞുങ്ങളെ വെറുതെ ഉപദ്രവിക്കരുത്", "is_correct": True},
                            {"text": "എല്ലാ കുഞ്ഞുങ്ങളെയും തടവിലാക്കുക", "is_correct": False},
                            {"text": "കുഞ്ഞുങ്ങളെ ദത്തെടുക്കുക", "is_correct": False},
                            {"text": "കുട്ടികളെ ബലികൊടുക്കുക", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഈ ശ്ലോകത്തിൽ ഭഗവാനുമായി ദേവിക്കുള്ള ബന്ധം എന്താണ്?",
                        "options": [
                            {"text": "അനുജാ വിഷ്ണോഃ (ഭഗവാൻ വിഷ്ണുവിന്റെ സഹോദരി / യോഗമായ)", "is_correct": True},
                            {"text": "വിഷ്ണുവിന്റെ മാതാവ്", "is_correct": False},
                            {"text": "വിഷ്ണുവിന്റെ ശത്രു", "is_correct": False},
                            {"text": "മഥുരയിലെ സാധാരണ രാജകുമാരി", "is_correct": False}
                        ]
                    }
                ]
            },
            "bn": {
                "mainTopic": "কৃষ্ণ লীলা",
                "subTopic": "কংস ও অষ্টভুজা দুর্গা দেবীর আবির্ভাব",
                "content": """### প্রভাত কাল ও কংসের ত্রাস

মথুরার কারাগারে যখন প্রভাতের প্রথম কিরণ প্রতিফলিত হলো, তখন দেবকীর ক্রোড়ে শায়িত নবজাত কন্যা সশব্দে ক্রন্দন করতে লাগল। যোগমায়ার প্রভাবে ঘুমিয়ে থাকা প্রহরীদের তন্দ্রা ভঙ্গ হলো। চোখ কচলাতে কচলাতে তারা কারাগৃহ থেকে শিশুর ক্রন্দনধ্বনি শুনে চমকে উঠল।

দেবকীর অষ্টম সন্তান জন্মানো মাত্রই কংসকে সংবাদ দেবার কঠোর রাজাদেশ স্মরণ করে ভীত প্রহরীরা রাজপ্রাসাদে ছুটে গেল। তারা হাঁপাতে হাঁপাতে বলল: "মহারাজ! দেবকীর অষ্টম সন্তান ভূমিষ্ঠ হয়েছে!"

এ কথা শোনামাত্র কংস শয্যা থেকে লাফিয়ে উঠল। ভয়ে তার অঙ্গপ্রত্যঙ্গ কাঁপতে লাগল, গাত্ররোম শিহরিত হলো। কোষমুক্ত কৃপাণ হস্তে যমদূতের ন্যায় উন্মত্ত হয়ে কংস কারাগারের দিকে ছুটে গেল।

### মাতা দেবকীর কাতর মিনতি

কারাগারে প্রবেশ করে কংস দেখল দেবকী নবজাত শিশুকে বুকে জড়িয়ে ধরে ভয়ে কাঁপছেন। দেবকী ক্রূর ভ্রাতার চরণে লুটিয়ে পড়ে ক্রন্দনরত কণ্ঠে অনুনয় করলেন:

"হে ভাই কংস! কৃপা করে এই নিষ্পাপ বালিকাকে হত্যা কোরো না! এ তো কন্যাশিশু। দৈববাণী হয়েছিল যে অষ্টম পুত্রের দ্বারা তোমার মৃত্যু হবে, কন্যার দ্বারা নয়। এক অবলা কন্যা যুদ্ধে তোমার কি ক্ষতি করতে পারে? এ তোমার ভাগিনী, তোমার কন্যার সমান! আমার পূর্বের ছয়টি পুত্রকে তোমার নিষ্ঠুর হাতে তুলে দিয়েছি, সপ্তমটিও নষ্ট হয়েছে। আমার এই বার্ধক্যের একমাত্র সান্ত্বনা হিসেবে এই কন্যাটিকে প্রাণভিক্ষা দাও!"

### কংসের পৈশাচিক নিষ্ঠুরতা

দেবকীর এই ক্রন্দন পাষাণকেও বিগলিত করতে পারত, কিন্তু কংসের হৃদয় আসুরিক ভয়ে অন্ধ ও নিষ্ঠুর হয়ে গিয়েছিল। সে দেবকীকে তিরস্কার করে বলপূর্বক তার কোল থেকে শিশুটির পা ধরে ছিনিয়ে নিল।

অত্যন্ত বিষাক্ত ক্রোধে কংস শিশুটিকে মাথার ওপর তুলে পূর্বের সন্তানদের ন্যায় এক বিশাল প্রস্তরখণ্ডের ওপর সজোরে আছাড় মারল!

### অষ্টভুজা দুর্গা দেবীর আবির্ভাব

সেই মুহূর্তে কংসের চোখের সামনে এক পরম অলৌকিক দৃশ্য উদ্ভাসিত হলো!

শিশু কন্যাটি পাথরের ওপর পড়ল না; বরং কংসের হাত থেকে পিছলে সরাসরি আকাশে উঠে গেল! সমগ্র মথুরার আকাশকে দিব্য আলোয় উদ্ভাসিত করে সেই কন্যা তাঁর পরম ঐশ্বর্যময় রূপ প্রকাশ করলেন:

> **শ্রীমদ্ভাগবত, স্কন্ধ ১০, অধ্যায় ৪, শ্লোক ৯**
> 
> *সা তদ্ধস্তাৎ সমুৎপত্য সদ্যো দেব্যম্বরং গতা ।*  
> *অদৃশ্যতানুজা বিষ্ণোঃ সায়ুধাষ্টমহাবুজা ॥*  
> 
> **অনুবাদ:** সেই শিশুটি কংসের হাত থেকে পিছলে তখনই আকাশে উঠে গেল। তিনি ভগবান শ্রীবিষ্ণুর অনুজা (ভগবতী যোগমায়া) দুর্গা দেবীরূপে আবির্ভূতা হলেন, যাঁর আটটি বিশাল হস্তে দিব্য অস্ত্রসমূহ শোভা পাচ্ছিল।

তিনি দিব্য বস্ত্র, পারিজাত পুষ্পের মালা ও রত্নালঙ্কারে সুসজ্জিতা হয়ে আকাশে অবস্থান করছিলেন। তাঁর আটটি হস্তে শোভা পাচ্ছিল ধনু, ত্রিশূল, বাণ, ঢাল, খড়্গ, শঙ্খ, চক্র ও গদা। দেবতারা পুষ্পবৃষ্টি করে তাঁর স্তব করছিলেন।

### কংসকে দেবীর দৈব সাবধানবাণী

কম্পমান কংসের প্রতি হাস্য করে দেবী বজ্রনির্ঘোষে বললেন:

> **শ্রীমদ্ভাগবত, স্কন্ধ ১০, অধ্যায় ৪, শ্লোক ১২**
> 
> *কিং ময়া হতয়া মন্দ জাতঃ খলু তবান্তকৃৎ ।*  
> *যত্র ক্ব বা পূর্বশত্রুস তং মা হিংসীঃ কথঞ্চন ॥*  
> 
> **অনুবাদ:** ওরে নির্বোধ কংস! আমাকে হত্যা করার চেষ্টা করে তোর কি লাভ হবে? তোকে সংহারকারী পরমেশ্বর—তোর পূর্বজন্মের চিরশত্রু—ইতিমধ্যেই অন্য কোথাও জন্মগ্রহণ করেছেন! অতএব অনর্থক অন্য নির্দোষ শিশুদের ওপর অত্যাচার করিস না!

কংসকে এই মহাবাণী শুনিয়ে দেবী দুর্গা অন্তর্হিতা হলেন। তিনি জগতে দুর্গা, ভদ্রকালী, বিজয়া, বৈষ্ণবী, কুমুদা, চণ্ডিকা, কৃষ্ণা, মাধবী, কন্যা ও মায়া নামে সুপ্রসিদ্ধ হলেন।

নিচে কারাগারের প্রাঙ্গণে কংসের মুকুট খসে পড়ল, তলোয়ার হাত থেকে পড়ে গেল এবং সে পরম ভয়ে ও অপমানে অচেতন হয়ে মাটিতে লুটিয়ে পড়ল।""",
                "questions": [
                    {
                        "question": "ভোরবেলা প্রহরীদের ঘুম কীভাবে ভেঙেছিল?",
                        "options": [
                            {"text": "দেবকীর কোলে নবজাত কন্যার ক্রন্দন শুনে", "is_correct": True},
                            {"text": "তূর্যধ্বনিতে", "is_correct": False},
                            {"text": "ভূমিকম্পের ঝাঁকুনিতে", "is_correct": False},
                            {"text": "কংসের চিৎকারে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "অষ্টম সন্তানের জন্মের কথা শুনে কংসের কি অবস্থা হয়েছিল?",
                        "options": [
                            {"text": "ভয়ে কাঁপতে কাঁপতে অস্ত্র হাতে কারাগারের দিকে ছুটে গিয়েছিল", "is_correct": True},
                            {"text": "আনন্দোৎসব করেছিল", "is_correct": False},
                            {"text": "শান্তভাবে ঘুমিয়েছিল", "is_correct": False},
                            {"text": "দেবকীকে উপহার পাঠিয়েছিল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "সন্তানের প্রাণভিক্ষা চাইতে গিয়ে দেবকী কি যুক্তি দিয়েছিলেন?",
                        "options": [
                            {"text": "এটি একটি কন্যাশিশু এবং যুদ্ধে কংসের কোন ক্ষতি করতে পারবে না", "is_correct": True},
                            {"text": "শিশুর চুল সোনালী ছিল", "is_correct": False},
                            {"text": "শিশুটি দেবতাদের উৎসর্গীকৃত", "is_correct": False},
                            {"text": "বসুদেব স্বর্ণ দেবেন", "is_correct": False}
                        ]
                    },
                    {
                        "question": "কংস শিশুটির ওপর কি নিষ্ঠুরতা করেছিল?",
                        "options": [
                            {"text": "পা ধরে পাথরের ওপর আছাড় মারার জন্য নিক্ষেপ করেছিল", "is_correct": True},
                            {"text": "যমুনায় ফেলে দিয়েছিল", "is_correct": False},
                            {"text": "লোহার বাক্সে বন্ধ করেছিল", "is_correct": False},
                            {"text": "বিষ দিয়েছিল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "পাথরে নিক্ষেপ করার সময় কি অলৌকিক ঘটনা ঘটেছিল?",
                        "options": [
                            {"text": "হাত পিছলে আকাশে উড়ে গিয়ে অষ্টভুজা দুর্গারূপে আবির্ভূত হয়েছিল", "is_correct": True},
                            {"text": "পাথর ভেঙে চুরমার হয়েছিল", "is_correct": False},
                            {"text": "ধোঁয়ায় পরিণত হয়েছিল", "is_correct": False},
                            {"text": "পাথরে লেগে কেঁদেছিল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "আকাশে আবির্ভূত দেবীর কয়টি হাত ছিল?",
                        "options": [
                            {"text": "অস্ত্রধারী আটটি হাত", "is_correct": True},
                            {"text": "দুটি হাত", "is_correct": False},
                            {"text": "চারটি হাত", "is_correct": False},
                            {"text": "সহস্র হাত", "is_correct": False}
                        ]
                    },
                    {
                        "question": "দেবী দুর্গা হস্তে কি কি অস্ত্র ধারণ করেছিলেন?",
                        "options": [
                            {"text": "ধনু, বাণ, ত্রিশূল, খড়্গ, ঢাল, শঙ্খ, চক্র ও গদা", "is_correct": True},
                            {"text": "কেবল পুস্তক ও কমণ্ডলু", "is_correct": False},
                            {"text": "বাঁশি", "is_correct": False},
                            {"text": "লাঙ্গল ও মুষল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "দেবী কংসকে কি বিস্ময়কর সত্য জানিয়েছিলেন?",
                        "options": [
                            {"text": "তোকে সংহারকারী শত্রু অন্যত্র জন্মগ্রহণ করেছে", "is_correct": True},
                            {"text": "কংস চিরকাল বাঁচবে", "is_correct": False},
                            {"text": "দেবতারা পরাজয় মেনে নিয়েছে", "is_correct": False},
                            {"text": "বসুদেবই তার পিতা", "is_correct": False}
                        ]
                    },
                    {
                        "question": "অন্য শিশুদের বিষয়ে দেবী কংসকে কি সাবধান করেছিলেন?",
                        "options": [
                            {"text": "অনর্থক অন্য নির্দোষ শিশুদের ওপর অত্যাচার করিস না", "is_correct": True},
                            {"text": "সকল শিশুকে বন্দী কর", "is_correct": False},
                            {"text": "শিশুদের দত্তক নে", "is_correct": False},
                            {"text": "শিশুবলি দে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "শাস্ত্রে দেবীকে শ্রীবিষ্ণুর সাথে কি সম্পর্কে উল্লেখ করা হয়েছে?",
                        "options": [
                            {"text": "অনুজা বিষ্ণোঃ (শ্রীবিষ্ণুর কনিষ্ঠা ভগিনী / যোগমায়া)", "is_correct": True},
                            {"text": "বিষ্ণুর মাতা", "is_correct": False},
                            {"text": "বিষ্ণুর শত্রু", "is_correct": False},
                            {"text": "মথুরার সাধারণ রাজকন্যা", "is_correct": False}
                        ]
                    }
                ]
            },
            "te": {
                "mainTopic": "కృష్ణ లీలలు",
                "subTopic": "కంసుడు మరియు అష్టభుజ దుర్గాదేవి ఆవిర్భావం",
                "content": """### ఉదయపు వేళ మరియు కంసుని భయం

మథుర చెరసాలపై ఉదయపు కిరణాలు ప్రసరించిన సమయంలో, దేవకి ఒడిలో ఉన్న పసిపాప పెద్దగా ఏడవడం ప్రారంభించింది. యోగమాయ ప్రభావం తొలగిపోవడంతో కాపలాదారులు నిద్రలేచారు. చెరసాల నుండి పాప ఏడుపు విని వారు ఉలిక్కిపడ్డారు.

ఎనిమిదవ సంతానం జన్మించిన వెంటనే తనకు తెలియజేయాలన్న కంసుని కఠినమైన ఆజ్ఞను గుర్తుచేసుకుంటూ వారు భయంతో రాజభవనానికి పరుగుతీశారు. వారు రొప్పుతూ కంసునికి చెప్పారు: "మహారాజా! దేవకికి ఎనిమిదవ సంతానం జన్మించింది!"

ఆ మాట వినగానే కంసుడు మంచంపై నుండి ఉలిక్కిపడి లేచాడు. భయంతో అతని శరీరమంతా వణికింది, వెండ్రుకలు నిక్కబొడుచుకున్నాయి. ఒర నుండి కత్తి దూసి, యమునిలాగా భయంకర రూపంతో చెరసాల వైపు పరుగుతీశాడు.

### తల్లి దేవకి కన్నీటి వేడుకోలు

చెరసాలలోకి అడుగుపెట్టిన కంసునికి, తన బిడ్డను గుండెలకు హత్తుకుని వణుకుతున్న దేవకి కనిపించింది. క్రూరమైన అన్న పాదాలపై పడి దేవకి కన్నీరుమున్నీరుగా వేడుకుంది:

"అన్నా కంసా! దయచేసి ఈ పసిపాపను చంపవద్దు! ఇది ఆడపిల్ల. ఎనిమిదవ కుమారుని వల్ల నీకు మరణం అని ఆకాశవాణి పలికింది కానీ ఆడపిల్ల వల్ల కాదు. ఒక స్త్రీ యుద్ధంలో నీకేం హాని చేయగలదు? ఈమె నీ మేనకోడలు, నీ కూతురితో సమానం! నా మొదటి ఆరుగురు కుమారులను నీ చేతుల్లో బలిచ్చాను, ఏడవ సంతానాన్ని పోగొట్టుకున్నాను. నా వృద్ధాప్యానికి ఆధారంగా ఈ ఒక్క ఆడబిడ్డనైనా బ్రతకనివ్వు, నీ పాదాలు పట్టుకుని వేడుకుంటున్నాను!"

### కంసుని కర్కశ క్రూరత్వం

రాతిని సైతం కరిగించే దేవకి రోదన కంసుని అసుర హృదయాన్ని ఏమాత్రం కరిగించలేకపోయింది. ధర్మాన్ని, తోబుట్టువుల ప్రేమానురాగాలను తుంగలో తొక్కి కంసుడు దేవకిని దూషించాడు.

ముందుకు వచ్చి, దేవకి చేతుల్లోంచి ఆ పసిపాప కాళ్ళను పట్టుకుని నిర్దయగా లాక్కున్నాడు. కసిగా ఆ పాపను తలపైకి ఎత్తి, మునుపటి పిల్లలలాగే బండరాయిపై వేసి ముక్కలు చేయడానికి విసిరికొట్టాడు!

### అష్టభుజ దుర్గాదేవి ఆవిర్భావం

ఆ క్షణంలోనే కంసుని కళ్ళముందు ఒక మహా అద్భుతం జరిగింది!

ఆ పసిపాప బండరాయిపై పడలేదు; కంసుని చేతుల్లోంచి జారిపోయి ఆకాశంలోకి ఎగిరిపోయింది! మథుర ఆకాశమంతా దివ్య కాంతులతో నిండిపోగా, ఆ దేవి తన నిజ దివ్య రూపాన్ని ప్రదర్శించింది:

> **శ్రీమద్భాగవతం, స్కంధం 10, అధ్యాయం 4, శ్లోకం 9**
> 
> *సా తద్ధస్తాత్ సముత్పత్య సద్యో దేవ్యంబరం గతా |*  
> *అదృశ్యతానుజా విష్ణోః సాయుధాష్టమహాభుజా ||*  
> 
> **తాత్పర్యం:** ఆ పసిపాప కంసుని చేతుల నుండి జారి తక్షణమే ఆకాశంలోకి వెళ్ళిపోయింది. శ్రీమహావిష్ణువు అనుజ (చెల్లెలు/యోగమాయ) అయిన దుర్గాదేవిగా, తన ఎనిమిది చేతులలో దివ్యాయుధాలను ధరించి ప్రత్యక్షమైంది.

ఆమె ఆకాశంలో దివ్యాభరణాలు, పారిజాత పుష్పమాలలతో వెలిగిపోతూ నిలిచింది. తన ఎనిమిది చేతులలో ధనుస్సు, త్రిశూలం, బాణాలు, కత్తి, డాలు, శంఖం, చక్రం, గదలను ధరించింది. దేవతలు పుష్పవృష్టి కురిపిస్తూ ఆమెను స్తుతించారు.

### కంసునికి హెచ్చరిక

భయంతో వణుకుతున్న కంసుని చూసి నవ్వుతూ దుర్గాదేవి గంభీరంగా ఇలా హెచ్చరించింది:

> **శ్రీమద్భాగవతం, స్కంధం 10, అధ్యాయం 4, శ్లోకం 12**
> 
> *కిం మయా హతయా మంద జాతః ఖలు తవాంతకృత్ |*  
> *యత్ర క్వ వా పూర్వశత్రుస్ తం మా హింసీః కథంచన ||*  
> 
> **తాత్పర్యం:** ఓరి మూర్ఖ కంసా! నన్ను చంపడానికి ప్రయత్నించి నువ్వేం సాధిస్తావు? నిన్ను సంహరించే పరమేశ్వరుడు—నీ పూర్వజన్మల శత్రువు—ఇప్పటికే వేరొకచోట జన్మించాడు! కాబట్టి అమాయకులైన ఇతర పసిపిల్లలను అనవసరంగా హింసించకు!

ఈ హెచ్చరిక చేసి దుర్గాదేవి అంతర్థానమైంది. ఆమె దుర్గ, భద్రకాళి, విజయ, వైష్ణవి, కుముద, చండిక, కృష్ణ, మాధవి, కన్య, మాయ అనే దివ్య నామాలతో జగమంతా పూజింపబడింది.

కింద ప్రాంగణంలో కిరీటం నేలపడి, కత్తి చేజారి, తీవ్ర భయాందోళనలతో కంసుడు నేలపై కూలిపోయాడు.""",
                "questions": [
                    {
                        "question": "ఉదయాన కాపలాదారులకు మెలకువ ఎలా వచ్చింది?",
                        "options": [
                            {"text": "దేవకి ఒడిలోని పసిపాప ఏడుపు విని", "is_correct": True},
                            {"text": "బాకా శబ్దం విని", "is_correct": False},
                            {"text": "భూకంపం వల్ల", "is_correct": False},
                            {"text": "కంసుని కేకల వల్ల", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ఎనిమిదవ బిడ్డ పుట్టిందని వినగానే కంసుని పరిస్థితి ఏమిటి?",
                        "options": [
                            {"text": "భయంతో వణికి, కత్తితో చెరసాల వైపు పరుగుతీశాడు", "is_correct": True},
                            {"text": "సంతోషంతో పాటలు పాడాడు", "is_correct": False},
                            {"text": "ప్రశాంతంగా పడుకున్నాడు", "is_correct": False},
                            {"text": "దేవకికి బహుమతులు పంపాడు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పాపను కాపాడటానికి దేవకి చెప్పిన ముఖ్య కారణం ఏమిటి?",
                        "options": [
                            {"text": "ఇది ఆడపిల్ల, యుద్ధంలో కంసునికి ఏ హానీ చేయలేదు", "is_correct": True},
                            {"text": "పాపకు బంగారు జుట్టు ఉంది", "is_correct": False},
                            {"text": "పాపను దేవతలకు ఇస్తానని", "is_correct": False},
                            {"text": "వసుదేవుడు బంగారం ఇస్తానని", "is_correct": False}
                        ]
                    },
                    {
                        "question": "కంసుడు ఆ పసిపాపకు ఏమి చేయాలని చూశాడు?",
                        "options": [
                            {"text": "కాళ్ళతో పట్టుకుని బండరాయిపైకి విసిరాడు", "is_correct": True},
                            {"text": "యమునలో పడేశాడు", "is_correct": False},
                            {"text": "పెట్టెలో బంధించాడు", "is_correct": False},
                            {"text": "విషం ఇచ్చాడు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "బండరాయిపైకి విసిరినప్పుడు ఏమి జరిగింది?",
                        "options": [
                            {"text": "చేతి నుండి జారి ఆకాశంలో అష్టభుజ దుర్గాదేవిగా ఆవిర్భవించింది", "is_correct": True},
                            {"text": "రాయి పగిలిపోయింది", "is_correct": False},
                            {"text": "పొగగా మారింది", "is_correct": False},
                            {"text": "రాయిపై పడి ఏడ్చింది", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ఆకాశంలో కనిపించిన దేవికి ఎన్ని చేతులు ఉన్నాయి?",
                        "options": [
                            {"text": "ఆయుధాలు ధరించిన ఎనిమిది చేతులు", "is_correct": True},
                            {"text": "రెండు చేతులు", "is_correct": False},
                            {"text": "నాలుగు చేతులు", "is_correct": False},
                            {"text": "వేయి చేతులు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "దుర్గాదేవి చేతుల్లో ధరించిన ఆయుధాలు ఏవి?",
                        "options": [
                            {"text": "ధనుస్సు, బాణాలు, త్రిశూలం, ఖడ్గం, డాలు, శంఖం, చక్రం, గద", "is_correct": True},
                            {"text": "పుస్తకం మరియు కమండలం మాత్రమే", "is_correct": False},
                            {"text": "వేణువు", "is_correct": False},
                            {"text": "నాగలి మరియు రోకలి", "is_correct": False}
                        ]
                    },
                    {
                        "question": "దుర్గాదేవి కంసునికి వెల్లడించిన ఆశ్చర్యకరమైన నిజం ఏమిటి?",
                        "options": [
                            {"text": "నిన్ను చంపే శత్రువు వేరొకచోట జన్మించాడు", "is_correct": True},
                            {"text": "కంసుడు ఎప్పటికీ చనిపోడు", "is_correct": False},
                            {"text": "దేవతలు ఓడిపోయారు", "is_correct": False},
                            {"text": "వసుదేవుడే అతని తండ్రి", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ఇతర పిల్లల గురించి దేవి కంసునికి ఇచ్చిన హెచ్చరిక ఏమిటి?",
                        "options": [
                            {"text": "అమాయకులైన ఇతర పసిపిల్లలను హింసించకు", "is_correct": True},
                            {"text": "అందరు పిల్లలను బంధించు", "is_correct": False},
                            {"text": "పిల్లలను దత్తత తీసుకో", "is_correct": False},
                            {"text": "పిల్లలను బలివ్వు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "శాస్త్రాలలో ఈ దేవి విష్ణువుతో ఎలాంటి సంబంధం కలిగి ఉందని చెప్పబడింది?",
                        "options": [
                            {"text": "అనుజా విష్ణోః (విష్ణువు సోదరి / యోగమాయ)", "is_correct": True},
                            {"text": "విష్ణువు తల్లి", "is_correct": False},
                            {"text": "విష్ణువు శత్రువు", "is_correct": False},
                            {"text": "మథుర సాధారణ రాజకుమారి", "is_correct": False}
                        ]
                    }
                ]
            },
            "kn": {
                "mainTopic": "ಕೃಷ್ಣ ಲೀಲೆಗಳು",
                "subTopic": "ಕಂಸ ಮತ್ತು ಅಷ್ಟಭುಜ ದುರ್ಗಾದೇವಿಯ ಆವಿರ್ಭಾವ",
                "content": """### ಮುಂಜಾನೆ ಮತ್ತು ಕಂಸನ ಭಯಾನಕ ಆತಂಕ

ಮಥುರೆಯ ಸೆರೆಮನೆಯ ಮೇಲೆ ಮುಂಜಾನೆಯ ಸೂರ್ಯಕಿರಣಗಳು ಬಿದ್ದಾಗ, ದೇವಕಿಯ ಮಡಿಲಲ್ಲಿದ್ದ ನವಜಾತ ಹೆಣ್ಣು ಮಗುವು ಜೋರಾಗಿ ಅಳತೊಡಗಿತು. ಯೋಗಮಾಯೆಯ ಪ್ರಭಾವದಿಂದ ನಿದ್ರಿಸುತ್ತಿದ್ದ ಕಾವಲುಗಾರರು ಎಚ್ಚರಗೊಂಡರು. ಸೆರೆಮನೆಯಿಂದ ಮಗುವಿನ ಅಳು ಕೇಳಿ ಅವರು ಬೆಚ್ಚಿಬಿದ್ದರು.

ದೇವಕಿಗೆ ಎಂಟನೆಯ ಮಗು ಜನಿಸಿದ ತಕ್ಷಣ ತಿಳಿಸಬೇಕೆಂಬ ಕಂಸನ ಕಠಿಣ ಆಜ್ಞೆಯನ್ನು ನೆನೆದು, ಭಯಭೀತರಾದ ಕಾವಲುಗಾರರು ಅರಮನೆಗೆ ಓಡಿದರು. ಅವರು ಉಸಿರೆಳೆದುಕೊಳ್ಳುತ್ತಾ ಕಂಸನಿಗೆ ಹೇಳಿದರು: "ಮಹಾರಾಜರೇ! ದೇವಕಿಗೆ ಎಂಟನೆಯ ಮಗು ಜನಿಸಿದೆ!"

ಇದನ್ನು ಕೇಳಿದ ತಕ್ಷಣ ಕಂಸನು ಹಾಸಿಗೆಯಿಂದ ಜಿಗಿದೆದ್ದನು. ಭಯದಿಂದ ಆತನ ಅಂಗಾಂಗಗಳು ನಡುಗಿದವು, ರೋಮಗಳು ನಿಮಿರಿ ನಿಂತವು. ಕತ್ತಿಯನ್ನು ಹಿರಿದು, ಯಮಧರ್ಮನಂತೆ ರೋಷದಿಂದ ಸೆರೆಮನೆಯ ಕಡೆಗೆ ಧಾವಿಸಿದನು.

### ತಾಯಿ ದೇವಕಿಯ ಕರುಣಾಜನಕ ಮೊರೆ

ಸೆರೆಮನೆಗೆ ನುಗ್ಗಿದ ಕಂಸನಿಗೆ, ಮಗುವನ್ನು ಎದೆಗಪ್ಪಿಕೊಂಡು ನಡುಗುತ್ತಿದ್ದ ದೇವಕಿ ಕಂಡಳು. ಆಕೆಯು ಕ್ರೂರಿ ಅಣ್ಣನ ಪಾದಗಳಿಗೆ ಬಿದ್ದು ಕಣ್ಣೀರು ಸುರಿಸುತ್ತಾ ಬೇಡಿಕೊಂಡಳು:

"ಅಣ್ಣಾ ಕಂಸ! ದಯವಿಟ್ಟು ಈ ಮುಗ್ಧ ಮಗುವನ್ನು ಕೊಲ್ಲಬೇಡ! ಇದು ಹೆಣ್ಣು ಮಗು. ಎಂಟನೇ ಗಂಡು ಮಗುವಿನಿಂದ ನಿನಗೆ ಮೃತ್ಯು ಎಂದು ಅಶರೀರವಾಣಿ ಹೇಳಿತ್ತೇ ಹೊರತು ಹೆಣ್ಣು ಮಗುವಿನಿಂದಲ್ಲ. ಹೆಣ್ಣು ಮಗು ಯುದ್ಧದಲ್ಲಿ ನಿನಗೆ ಯಾವ ಹಾನಿಯನ್ನೂ ಮಾಡಲಾರದು. ಈಕೆ ನಿನ್ನ ಅಳಿಯ/ಮಗಳ ಸಮಾನ! ಈಗಾಗಲೇ ನನ್ನ ಆರು ಗಂಡು ಮಕ್ಕಳನ್ನು ಕೊಂದಿದ್ದೀ, ಏಳನೆಯ ಮಗುವೂ ಇಲ್ಲವಾಯಿತು. ನನ್ನ ಈ ವೃದ್ಧಾಪ್ಯದ ಸಮಾಧಾನಕ್ಕಾಗಿ ಈ ಒಬ್ಬಳೇ ಹೆಣ್ಣು ಮಗುವನ್ನು ಬಿಟ್ಟುಬಿಡು, ನಿನ್ನ ಕಾಲಿಗೆ ಬಿದ್ದು ಬೇಡಿಕೊಳ್ಳುತ್ತೇನೆ!"

### ಕಂಸನ ಪೈಶಾಚಿಕ ಕ್ರೂರತೆ

ಕಲ್ಲನ್ನೂ ಕರಗಿಸುವಂತಿದ್ದ ದೇವಕಿಯ ರೋದನವು ಕಂಸನ ಅಸುರೀ ಹೃದಯವನ್ನು ಕರಗಿಸಲಿಲ್ಲ. ಧರ್ಮ, ಸಹೋದರ ಪ್ರೇಮವನ್ನು ಮರೆತ ಕಂಸನು ದೇವಕಿಯನ್ನು ನಿಂದಿಸಿದನು.

ಮುಂದೆ ಬಂದು, ದೇವಕಿಯ ಕೈಯಿಂದ ಆ ಹಸುಗೂಸಿನ ಕಾಲುಗಳನ್ನು ಹಿಡಿದು ಬಲವಂತವಾಗಿ ಕಸಿದುಕೊಂಡನು. ವಿಷಪೂರಿತ ಕೋಪದಿಂದ ಮಗುವನ್ನು ತಲೆಯ ಮೇಲೆತ್ತಿ, ಹಿಂದಿನ ಮಕ್ಕಳಂತೆಯೇ ಕಲ್ಲಿನ ಬಂಡೆಯ ಮೇಲೆ ಅಪ್ಪಳಿಸಿ ಕೊಲ್ಲಲು ಬಲವಾಗಿ ಎಸೆದನು!

### ಅಷ್ಟಭುಜ ದುರ್ಗಾದೇವಿಯ ಆವಿರ್ಭಾವ

ಆ ಕ್ಷಣದಲ್ಲಿಯೇ ಕಂಸನ ಕಣ್ಣಮುಂದೆ ಒಂದು ಮಹಾನ್ ಪವಾಡ ನಡೆಯಿತು!

ಆ ಮಗುವು ಕಲ್ಲಿನ ಮೇಲೆ ಬೀಳಲಿಲ್ಲ; ಕಂಸನ ಕೈಯಿಂದ ಜಾರಿ ಆಕಾಶಕ್ಕೆ ಚಿಮ್ಮಿತು! ಸಮಸ್ತ ಮಥುರೆಯ ಆಕಾಶವನ್ನು ದಿವ್ಯ ತೇಜಸ್ಸಿನಿಂದ ಬೆಳಗುತ್ತಾ ಆ ದೇವಿಯು ತನ್ನ ನಿಜವಾದ ದಿವ್ಯ ಸ್ವರೂಪವನ್ನು ಪ್ರಕಟಿಸಿದಳು:

> **ಶ್ರೀಮದ್ಭಾಗವತ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 4, ಶ್ಲೋಕ 9**
> 
> *ಸಾ ತದ್ಧಸ್ತಾತ್ ಸಮುತ್ಪತ್ಯ ಸದ್ಯೋ ದೇವ್ಯಂಬರಂ ಗತಾ |*  
> *ಅದೃಶ್ಯತಾನುಜಾ ವಿಷ್ಣೋಃ ಸಾಯುಧಾಷ್ಟಮಹಾಭುಜಾ ||*  
> 
> **ಭಾವಾರ್ಥ:** ಆ ಮಗುವು ಕಂಸನ ಕೈಯಿಂದ ಜಾರಿ ತಕ್ಷಣವೇ ಆಕಾಶಕ್ಕೆ ಹಾರಿತು. ಶ್ರೀಮಹಾವಿಷ್ಣುವಿನ ಸಹೋದರಿಯಾದ (ಯೋಗಮಾಯಾ) ದುರ್ಗಾದೇವಿಯಾಗಿ, ತನ್ನ ಎಂಟು ಕೈಗಳಲ್ಲಿ ದಿವ್ಯಾಯುಧಗಳನ್ನು ಧರಿಸಿ ಪ್ರತ್ಯಕ್ಷಳಾದಳು.

ಆಕೆಯು ಆಕಾಶದಲ್ಲಿ ದಿವ್ಯಾಭರಣಗಳು, ಪಾರಿಜಾತ ಪುಷ್ಪಮಾಲೆಗಳಿಂದ ಶೋಭಿಸುತ್ತಾ ನಿಂತಳು. ತನ್ನ ಎಂಟು ಕೈಗಳಲ್ಲಿ ಧನುಸ್ಸು, ಬಾಣ, ತ್ರಿಶೂಲ, ಖಡ್ಗ, ಗುರಾಣಿ, ಶಂಖ, ಚಕ್ರ ಮತ್ತು ಗದೆಯನ್ನು ಧರಿಸಿದ್ದಳು. ದೇವತೆಗಳು ಆಕೆಯ ಮೇಲೆ ಪುಷ್ಪವೃಷ್ಟಿ ಮಾಡಿ ಸ್ತುತಿಸಿದರು.

### ಕಂಸನಿಗೆ ದಿವ್ಯ ಎಚ್ಚರಿಕೆ

ಭಯದಿಂದ ನಡುಗುತ್ತಿದ್ದ ಕಂಸನನ್ನು ನೋಡಿ ನಗುತ್ತಾ ದುರ್ಗಾದೇವಿಯು ಹೀಗೆ ಎಚ್ಚರಿಸಿದಳು:

> **ಶ್ರೀಮದ್ಭಾಗವತ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 4, ಶ್ಲೋಕ 12**
> 
> *ಕಿಂ ಮಯಾ ಹತಯಾ ಮಂದ ಜಾತಃ ಖಲು ತವಾಂತಕೃತ್ |*  
> *ಯತ್ರ ಕ್ವ ವಾ ಪೂರ್ವಶತ್ರುಸ್ ತಂ ಮಾ ಹಿಂಸೀಃ ಕಥಂಚನ ||*  
> 
> **ಭಾವಾರ್ಥ:** ಎಲೈ ಮೂಢ ಕಂಸನೇ! ನನ್ನನ್ನು ಕೊಲ್ಲಲು ಪ್ರಯತ್ನಿಸಿ ನಿನಗೇನು ಸಿಗುತ್ತದೆ? ನಿನ್ನನ್ನು ಕೊಲ್ಲುವ ಪರಮಾತ್ಮನು—ನಿನ್ನ ಪೂರ್ವಜನ್ಮದ ಶತ್ರು—ಈಗಾಗಲೇ ಬೇರೆಲ್ಲಿಯೋ ಜನಿಸಿದ್ದಾನೆ! ಆದ್ದರಿಂದ ಅಮಾಯಕರಾದ ಇತರ ಮಕ್ಕಳನ್ನು ಅನವಶ್ಯಕವಾಗಿ ಹಿಂಸಿಸಬೇಡ!

ಈ ಎಚ್ಚರಿಕೆಯನ್ನು ನೀಡಿ ದುರ್ಗಾದೇವಿಯು ಅಂತರ್ಧಾನಳಾದಳು. ಆಕೆಯು ದುರ್ಗಾ, ಭದ್ರಕಾಳಿ, ವಿಜಯಾ, ವೈಷ್ಣವಿ, ಕುಮುದಾ, ಚಂಡಿಕಾ, ಕೃಷ್ಣಾ, ಮಾಧವಿ, ಕನ್ಯಾ ಮತ್ತು ಮಾಯಾ ಎಂಬ ಹೆಸರುಗಳಿಂದ ಜಗತ್ತಿನಾದ್ಯಂತ ಪೂಜಿಸಲ್ಪಟ್ಟಳು.

ಕೆಳಗೆ ಸೆರೆಮನೆಯ ಅಂಗಳದಲ್ಲಿ ಕಂಸನ ಕಿರೀಟ ನೆಲಕ್ಕುರುಳಿತು, ಕೈಯಿಂದ ಕತ್ತಿ ಜಾರಿತು, ಆತನು ತೀವ್ರ ಆಘಾತ ಮತ್ತು ಭಯದಿಂದ ನೆಲಕ್ಕುರುಳಿದನು.""",
                "questions": [
                    {
                        "question": "ಮುಂಜಾನೆ ಕಾವಲುಗಾರರು ಎಚ್ಚರಗೊಂಡಿದ್ದು ಹೇಗೆ?",
                        "options": [
                            {"text": "ದೇವಕಿಯ ಮಡಿಲಲ್ಲಿದ್ದ ಹೆಣ್ಣು ಮಗುವಿನ ಅಳು ಕೇಳಿ", "is_correct": True},
                            {"text": "ಕಹಳೆಯ ಶಬ್ದದಿಂದ", "is_correct": False},
                            {"text": "ಭೂಕಂಪದಿಂದ", "is_correct": False},
                            {"text": "ಕಂಸನ ಕೂಗಿನಿಂದ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಎಂಟನೆಯ ಮಗು ಜನಿಸಿತು ಎಂದು ಕೇಳಿದಾಗ ಕಂಸನ ಪ್ರತಿಕ್ರಿಯೆ ಹೇಗಿತ್ತು?",
                        "options": [
                            {"text": "ಭಯದಿಂದ ನಡುಗಿ, ಕತ್ತಿ ಹಿರಿದು ಸೆರೆಮನೆಗೆ ಓಡಿದನು", "is_correct": True},
                            {"text": "ಸಂತೋಷದಿಂದ ಹಾಡಿದನು", "is_correct": False},
                            {"text": "ಶಾಂತವಾಗಿ ಮಲಗಿದನು", "is_correct": False},
                            {"text": "ದೇವಕಿಗೆ ಉಡುಗೊರೆ ಕಳುಹಿಸಿದನು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಮಗುವಿನ ಪ್ರಾಣಭಿಕ್ಷೆಗಾಗಿ ದೇವಕಿ ನೀಡಿದ ಪ್ರಮುಖ ಕಾರಣವೇನು?",
                        "options": [
                            {"text": "ಇದು ಹೆಣ್ಣು ಮಗು, ಯುದ್ಧದಲ್ಲಿ ಕಂಸನಿಗೆ ಯಾವುದೇ ಹಾನಿ ಮಾಡಲಾರದು", "is_correct": True},
                            {"text": "ಮಗುವಿಗೆ ಚಿನ್ನದ ಕೂದಲಿತ್ತು", "is_correct": False},
                            {"text": "ಮಗುವನ್ನು ದೇವತೆಗಳಿಗೆ ನೀಡುವುದಾಗಿ", "is_correct": False},
                            {"text": "ವಸುದೇವನು ಚಿನ್ನ ಕೊಡುವನೆಂದು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಕಂಸನು ಆ ಹೆಣ್ಣು ಮಗುವಿಗೆ ಏನು ಮಾಡಲು ಯತ್ನಿಸಿದನು?",
                        "options": [
                            {"text": "ಕಾಲುಗಳನ್ನು ಹಿಡಿದು ಕಲ್ಲಿನ ಬಂಡೆಗೆ ಅಪ್ಪಳಿಸಲು ಎಸೆದನು", "is_correct": True},
                            {"text": "ಯಮುನೆಗೆ ಎಸೆದನು", "is_correct": False},
                            {"text": "ಪೆಟ್ಟಿಗೆಯಲ್ಲಿ ಕೂಡಿಹಾಕಿದನು", "is_correct": False},
                            {"text": "ವಿಷ ನೀಡಿದನು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಮಗುವನ್ನು ಕಲ್ಲಿಗೆ ಎಸೆದಾಗ ನಡೆದ ಪವಾಡವೇನು?",
                        "options": [
                            {"text": "ಕೈಯಿಂದ ಜಾರಿ ಆಕಾಶದಲ್ಲಿ ಅಷ್ಟಭುಜ ದುರ್ಗಾದೇವಿಯಾಗಿ ಪ್ರಕಟವಾಯಿತು", "is_correct": True},
                            {"text": "ಬಂಡೆ ಚೂರುಚೂರಾಯಿತು", "is_correct": False},
                            {"text": "ಹೊಗೆಯಾಗಿ ಬದಲಾಯಿತು", "is_correct": False},
                            {"text": "ಕಲ್ಲಿಗೆ ಬಿದ್ದು ಅಳತೊಡಗಿತು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಆಕಾಶದಲ್ಲಿ ಪ್ರಕಟವಾದ ದೇವಿಗೆ ಎಷ್ಟು ಕೈಗಳಿದ್ದವು?",
                        "options": [
                            {"text": "ಆಯುಧಗಳನ್ನು ಧರಿಸಿದ ಎಂಟು ಕೈಗಳು", "is_correct": True},
                            {"text": "ಎರಡು ಕೈಗಳು", "is_correct": False},
                            {"text": "ನಾಲ್ಕು ಕೈಗಳು", "is_correct": False},
                            {"text": "ಸಾವಿರ ಕೈಗಳು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ದುರ್ಗಾದೇವಿಯು ಕೈಗಳಲ್ಲಿ ಧರಿಸಿದ್ದ ಆಯುಧಗಳು ಯಾವುವು?",
                        "options": [
                            {"text": "ಧನುಸ್ಸು, ಬಾಣ, ತ್ರಿಶೂಲ, ಖಡ್ಗ, ಗುರಾಣಿ, ಶಂಖ, ಚಕ್ರ, ಗದೆ", "is_correct": True},
                            {"text": "ಪುಸ್ತಕ ಮತ್ತು ಕಮಂಡಲ ಮಾತ್ರ", "is_correct": False},
                            {"text": "ಕೊಳಲು", "is_correct": False},
                            {"text": "ನೇಗಿಲು ಮತ್ತು ಒನಕೆ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ದುರ್ಗಾದೇವಿಯು ಕಂಸನಿಗೆ ತಿಳಿಸಿದ ಆಘಾತಕಾರಿ ಸತ್ಯವೇನು?",
                        "options": [
                            {"text": "ನಿನ್ನನ್ನು ಕೊಲ್ಲುವ ಶತ್ರುವು ಈಗಾಗಲೇ ಬೇರೆಲ್ಲಿಯೋ ಜನಿಸಿದ್ದಾನೆ", "is_correct": True},
                            {"text": "ಕಂಸನು ಎಂದಿಗೂ ಸಾಯುವುದಿಲ್ಲ", "is_correct": False},
                            {"text": "ದೇವತೆಗಳು ಸೋತಿದ್ದಾರೆ", "is_correct": False},
                            {"text": "ವಸುದೇವನೇ ಆತನ ತಂದೆ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಇತರ ಮಕ್ಕಳ ಬಗ್ಗೆ ದೇವಿಯು ಕಂಸನಿಗೆ ನೀಡಿದ ಎಚ್ಚರಿಕೆಯೇನು?",
                        "options": [
                            {"text": "ಅಮಾಯಕರಾದ ಇತರ ಮಕ್ಕಳನ್ನು ಅನವಶ್ಯಕವಾಗಿ ಹಿಂಸಿಸಬೇಡ", "is_correct": True},
                            {"text": "ಎಲ್ಲಾ ಮಕ್ಕಳನ್ನು ಬಂಧಿಸು", "is_correct": False},
                            {"text": "ಮಕ್ಕಳನ್ನು ದತ್ತು ಪಡೆ", "is_correct": False},
                            {"text": "ಮಕ್ಕಳ ಬಲಿ ಕೊಡು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಶಾಸ್ತ್ರಗಳಲ್ಲಿ ಈ ದೇವಿಗೆ ಮಹಾವಿಷ್ಣುವಿನೊಂದಿಗಿರುವ ಸಂಬಂಧವೇನು?",
                        "options": [
                            {"text": "ಅನುಜಾ ವಿಷ್ಣೋಃ (ಮಹಾವಿಷ್ಣುವಿನ ಸಹೋದರಿ / ಯೋಗಮಾಯೆ)", "is_correct": True},
                            {"text": "ವಿಷ್ಣುವಿನ ತಾಯಿ", "is_correct": False},
                            {"text": "ವಿಷ್ಣುವಿನ ಶತ್ರು", "is_correct": False},
                            {"text": "ಮಥುರೆಯ ಸಾಮಾನ್ಯ ರಾಜಕುಮಾರಿ", "is_correct": False}
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

        self.stdout.write(self.style.SUCCESS(f"Successfully populated Story 10 (ID: {story.id}) across all 7 languages!"))
