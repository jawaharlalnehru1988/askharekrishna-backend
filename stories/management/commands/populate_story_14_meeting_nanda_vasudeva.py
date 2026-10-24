import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askharekrishna_backend.settings')
django.setup()

from django.core.management.base import BaseCommand
from stories.models import StoryMainTopic, Story, StoryTranslation, StoryQuestion, StoryQuestionOption

class Command(BaseCommand):
    help = "Populate Story 14: The Affectionate Meeting of Nanda Maharaja and Vasudeva in Mathura across 7 languages"

    def handle(self, *args, **options):
        topic = StoryMainTopic.objects.get(name="Krishna Pastimes")

        story_slug = "krishna-pastimes-the-affectionate-meeting-of-nanda-maharaja-and-vasudeva-in-mathura"
        image_path = "stories/images/meeting_nanda_vasudeva.jpg"

        story, created = Story.objects.get_or_create(
            slug=story_slug,
            defaults={
                "topic": topic,
                "order": 13,
                "imagePath": image_path,
            }
        )
        if not created:
            story.topic = topic
            story.order = 13
            story.imagePath = image_path
            story.save()

        stories_data = {
            "en": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "The Affectionate Meeting of Nanda Maharaja and Vasudeva in Mathura",
                "content": """### Nanda Maharaja Travels to Mathura

After the joyous celebrations of Nandotsava in Gokula, Nanda Maharaja, as the noble leader and chieftain of the cowherd community, prepared to travel to the capital city of Mathura. It was the duty of vassal chieftains to submit their annual royal taxes and tribute to King Kamsa. Entrusting the protection of Gokula and baby Krishna to elderly, responsible cowherd men, Nanda set out with bullock carts loaded with royal tribute, butter, and ghee.

Meanwhile, in Mathura, Sri Vasudeva was living in freedom after Kamsa had released him from the dungeon. As soon as Vasudeva heard that his dearest friend and brother Nanda Maharaja had arrived in Mathura to submit his taxes, his heart leaped with joyful anticipation. Vasudeva immediately set out for Nanda’s encampment.

### The Emotional Embrace of Two Great Souls

When Vasudeva entered the tent and beheld Nanda Maharaja, an overwhelming surge of fraternal affection flooded his heart:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 5, Verse 20**
> 
> *taṁ dṛṣṭvā sahasotthāya dehaḥ prāṇam ivāgatam*  
> *prītaḥ priyatamaṁ dorbhyāṁ sasvañje prema-vihvalaḥ*  
> 
> **Translation:** "Seeing his dearest friend and brother Nanda Maharaja, Vasudeva stood up abruptly, feeling as if life air had returned to a lifeless body. Overwhelmed by transcendental love, Vasudeva embraced him tightly with both arms."

Tears of affection poured from their eyes as the two great souls held each other. After surviving Kamsa’s cruel persecutions and the murder of his previous sons, seeing Nanda Maharaja felt to Vasudeva like a rebirth. 

Vasudeva seated Nanda comfortably and began to inquire affectionately about the welfare of his loved ones: "My dear brother Nanda, it is by supreme divine fortune that you have been blessed with a son in your advanced age! I hope our dear brother Balarama, son of Rohini, is growing happily under your loving care in Gokula? And is your newly born baby boy healthy and joyful? Are the lush pastures, clean waters, and sacred cows of Gokula thriving peacefully?"

### Nanda's Heartfelt Condolences

Nanda Maharaja, deeply touched by Vasudeva's kind inquiries, replied with profound sympathy: "My dear brother Vasudeva, we know of the monstrous tragedies you have suffered. The cruel King Kamsa slaughtered your six noble sons, and your eighth child, a daughter, flew into the sky as Goddess Durga! Truly, the fruits of one's past karma and the arrangements of destiny are unavoidable. Yet, one who remains fixed in spiritual consciousness is never disturbed by temporary happiness and distress."

### Vasudeva's Urgent Prophetic Warning

Vasudeva knew the terrifying secret that Nanda did not: that baby Krishna was the Supreme Personality of Godhead, and that King Kamsa’s demonic council had just unleashed fierce demons to hunt down and kill all newborn children across the land! 

Because of his deep love for Krishna and Nanda, Vasudeva became acutely anxious for their safety. He gave Nanda an urgent, life-saving warning:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 5, Verse 30**
> 
> *tātānugamya tāvat tvaṁ gokulaṁ rakṣa putraka*  
> *utpātā bahavas tatra dṛśyante hy a-śubhāvahāḥ*  
> 
> **Translation:** "My dear brother Nanda, now that you have paid your annual taxes to the king, do not linger here in Mathura even for a single day! Return immediately to Gokula to protect your son and family, for I foresee many inauspicious portents and demonic disturbances arising there!"

Vasudeva urged: "When the taxes are paid, a wise man does not linger in the capital of a tyrannical king. Dangerous omens are appearing in the sky and on earth. Great disasters may soon strike Gokula. Return without delay to protect the children!"

Recognizing the saintly wisdom in Vasudeva’s words, Nanda Maharaja did not hesitate. He immediately assembled his cowherd companions, mounted his bullock cart, and hastened back along the road toward Gokula, earnestly praying to the Supreme Lord for the protection of baby Krishna.""",
                "questions": [
                    {
                        "question": "Why did Nanda Maharaja travel from Gokula to Mathura after Nandotsava?",
                        "options": [
                            {"text": "To pay the annual royal taxes and tribute to King Kamsa", "is_correct": True},
                            {"text": "To purchase royal horses", "is_correct": False},
                            {"text": "To challenge Kamsa to a duel", "is_correct": False},
                            {"text": "To attend a political debate", "is_correct": False}
                        ]
                    },
                    {
                        "question": "To whom did Nanda Maharaja entrust the protection of Gokula and baby Krishna while away?",
                        "options": [
                            {"text": "Elderly, responsible cowherd men (gopas)", "is_correct": True},
                            {"text": "Royal soldiers from Mathura", "is_correct": False},
                            {"text": "Mercenary warriors", "is_correct": False},
                            {"text": "Foreign merchants", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How did Srimad-Bhagavatam describe Vasudeva's feeling upon seeing Nanda Maharaja?",
                        "options": [
                            {"text": "As if life air had returned to a lifeless, dead body", "is_correct": True},
                            {"text": "As if he had found a bag of diamonds", "is_correct": False},
                            {"text": "As if he had conquered an empire", "is_correct": False},
                            {"text": "Indifferent and cold", "is_correct": False}
                        ]
                    },
                    {
                        "question": "About which two children did Vasudeva specifically inquire from Nanda Maharaja?",
                        "options": [
                            {"text": "Balarama (Rohini's son) and the newly born baby boy (Krishna)", "is_correct": True},
                            {"text": "The sons of Pandu", "is_correct": False},
                            {"text": "The sons of Dhritarashtra", "is_correct": False},
                            {"text": "Abhimanyu and Parikshit", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What sympathy did Nanda Maharaja express to Vasudeva?",
                        "options": [
                            {"text": "He offered condolences for Kamsa's past slaughter of Vasudeva's six sons", "is_correct": True},
                            {"text": "He offered money to pay Vasudeva's debts", "is_correct": False},
                            {"text": "He advised Vasudeva to leave Mathura forever", "is_correct": False},
                            {"text": "He blamed Vasudeva for Kamsa's anger", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What secret danger was Vasudeva aware of that Nanda Maharaja did not know?",
                        "options": [
                            {"text": "Kamsa's demonic council had just ordered the slaughter of newborn children", "is_correct": True},
                            {"text": "A severe drought was coming", "is_correct": False},
                            {"text": "Kamsa was planning to invade Gokula for butter", "is_correct": False},
                            {"text": "A tiger had entered Gokula", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What urgent advice did Vasudeva give Nanda Maharaja?",
                        "options": [
                            {"text": "Do not linger in Mathura; return immediately to Gokula to protect the children", "is_correct": True},
                            {"text": "Stay in Mathura for a month of sightseeing", "is_correct": False},
                            {"text": "Bring baby Krishna to Mathura to meet Kamsa", "is_correct": False},
                            {"text": "Go on a pilgrimage to Kashi", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Why does Srimad-Bhagavatam advise against lingering in a tyrant king's capital after paying taxes?",
                        "options": [
                            {"text": "Because whimsical and demonic kings can create dangerous disturbances at any moment", "is_correct": True},
                            {"text": "Because hotels in the capital are too expensive", "is_correct": False},
                            {"text": "Because bullocks dislike city streets", "is_correct": False},
                            {"text": "Because trading is forbidden after sunset", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How did Nanda Maharaja react to Vasudeva's warning?",
                        "options": [
                            {"text": "He took it to heart immediately, mounted his cart, and hurried back to Gokula", "is_correct": True},
                            {"text": "He ignored the warning and went shopping", "is_correct": False},
                            {"text": "He laughed at Vasudeva's fears", "is_correct": False},
                            {"text": "He challenged Kamsa to battle", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Which chapter of Srimad-Bhagavatam Canto 10 describes the meeting of Nanda and Vasudeva?",
                        "options": [
                            {"text": "Chapter 5", "is_correct": True},
                            {"text": "Chapter 2", "is_correct": False},
                            {"text": "Chapter 7", "is_correct": False},
                            {"text": "Chapter 12", "is_correct": False}
                        ]
                    }
                ]
            },
            "ta": {
                "mainTopic": "கிருஷ்ண லீலைகள்",
                "subTopic": "மதுராவில் நந்த மகாராஜாவும் வசுதேவரும் பாசத்துடன் சந்தித்த திவ்ய லீலை",
                "content": """### நந்த மகாராஜாவின் மதுரைப் பயணம்

கோகுலத்தில் நந்தோத்ஸவக் கொண்டாட்டங்கள் இனிதே முடிந்த பின்னர், ஆயர்களின் தலைவரான நந்த மகாராஜா மதுரைக்குச் செல்ல ஆயத்தமானார். மன்னன் கம்சனுக்கு செலுத்த வேண்டிய வருடாந்திர வரியையும் காணிக்கைகளையும் செலுத்துவது சிற்றரசர்களின் கடமையாகும். கோகுலத்தின் பாதுகாப்பையும், குழந்தை கிருஷ்ணரையும் அனுபவம் வாய்ந்த முதிய ஆயர்களிடம் ஒப்படைத்துவிட்டு, காணிக்கைப் பொருட்களோடும் வெண்ணெய், நெய் நிறைந்த வண்டிகளோடும் நந்தர் மதுரைக்குப் புறப்பட்டார்.

அச்சமயம் மதுராவில் சிறையிலிருந்து விடுபட்ட வசுதேவர் சுதந்திரமாக வாழ்ந்து வந்தார். தனது ஆருயிர் நண்பரும் சகோதரருமான நந்த மகாராஜா வரி செலுத்த மதுரை வந்துள்ளார் என்ற நற்செய்தியைக் கேட்ட மாத்திரத்தில் வசுதேவரின் உள்ளம் எல்லையற்ற மகிழ்ச்சியால் துள்ளியது. உடனே அவர் நந்தர் தங்கியிருந்த கூடாரத்தை நோக்கி விரைந்தார்.

### இரு உன்னத பக்தர்களின் பாசத் தழுவல்

கூடாரத்தினுள் நுழைந்த வசுதேவர் நந்த மகாராஜாவைக் கண்ட கணமே, சகோதர பாசத்தின் பெருவெள்ளம் அவரது இதயத்தை ஆட்கொண்டது:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 5, சுலோகம் 20**
> 
> *தம் த்ருஷ்ட்வா ஸஹஸோத்தாய தேஹ: ப்ராணம் இவாகதம் |*  
> *ப்ரீத: ப்ரியதமம் தோர்ப்யாம் ஸஸ்வஞ்ஜே ப்ரேம-விஹ்வல: ||*  
> 
> **பொருள்:** "தனது ஆருயிர் நண்பரும் சகோதரருமான நந்த மகாராஜாவைக் கண்ட வசுதேவர், உயிரற்ற உடலுக்குள் மீண்டும் உயிர் மூச்சு திரும்பியது போல உடனே எழுந்து நின்றார். எல்லையற்ற திவ்ய பிரேமையினால் பரவசமடைந்து, தனது இரு கரங்களாலும் அவரை இறுகத் தழுவிக்கொண்டார்."

இருவரின் கண்களிலிருந்தும் பாசக் கண்ணீர் பெருக்கெடுத்து ஓடியது. கம்சனின் கொடூரக் கொடுமைகளைத் தாங்கி, ஆறு குழந்தைகளையும் பறிகொடுத்த வசுதேவருக்கு, நந்தரைக் கண்ட அந்த கணம் ஒரு புதிய மறுபிறவி போலத் தோன்றியது.

நந்தரை ஆசனத்தில் அமரச்செய்து வசுதேவர் பாசத்தோடு நலம் விசாரித்தார்: "அன்புச் சகோதரரே நந்தரே! தங்களின் முதிர்ந்த வயதில் தங்களுக்கு ஓர் அழகிய ஆண் குழந்தை பிறந்திருப்பது எப்பேர்ப்பட்ட பாக்கியம்! கோகுலத்தில் ரோகிணியின் மகனான நமது பாலன் பலராமன் உங்களின் அன்பான அரவணைப்பில் நலமாக வளர்கிறானா? தங்களின் புதிய குழந்தையும் மகிழ்ச்சியாக உள்ளதா? கோகுலத்தின் வளமான புல்வெளிகளும், புனித பசுக்களும் நலமாக உள்ளவையா?"

### நந்தரின் ஆறுதல் மொழிகள்

வசுதேவரின் அன்பான விசாரிப்பினால் நெகிழ்ந்த நந்த மகாராஜா ஆழ்ந்த அனுதாபத்துடன் கூறினார்: "அன்புச் சகோதரரே வசுதேவரே! நீங்கள் அனுபவித்த சொல்லொணாத துயரங்களை நாங்கள் அறிவோம். கொடிய கம்சன் தங்களின் ஆறு குழந்தைகளையும் கொன்றான்; எட்டாவது பெண் குழந்தையோ ஆகாயத்திற்குள் மறைந்தது! கர்ம வினைகளும் இறைவனின் சங்கல்பமும் எவராலும் வெல்ல முடியாதவை. ஆயினும், ஆன்மீக ஞானத்தில் நிலைத்திருப்போர் இந்த தற்காலிக சுக-துக்கங்களால் ஒருபோதும் கலங்குவதில்லை."

### வசுதேவரின் அவசர எச்சரிக்கை

நந்தர் அறியாத ஒரு பயங்கரமான ரகசியத்தை வசுதேவர் அறிந்திருந்தார்: கோகுலத்தில் இருப்பது சாட்சாத் முழுமுதற் கடவுளான பகவான் ஸ்ரீ கிருஷ்ணர் என்பதும், கம்சனின் அசுர சபை நாடெங்கும் குழந்தைகளைக் கொன்று குவிக்க படைகளை ஏவியுள்ளது என்பதும் வசுதேவருக்குத் தெரியும்!

எனவே, கிருஷ்ணரின் பாதுகாப்பைக் குறித்து வசுதேவர் பேரச்சம் கொண்டார். அவர் நந்தருக்கு ஓர் அவசர எச்சரிக்கையை விடுத்தார்:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 5, சுலோகம் 30**
> 
> *தாதானுகம்ய தாவத் த்வம் கோகுலம் ரக்ஷ புத்ரக |*  
> *உத்பாதா பஹவஸ் தத்ர த்ருஶ்யந்தே ஹ்ய அஶுபாவஹா: ||*  
> 
> **பொருள்:** "அன்புச் சகோதரரே நந்தரே! மன்னனுக்குரிய வரியைச் செலுத்திவிட்டீர்கள்; இனி ஒரு கணம் கூட மதுராவில் தாமதிக்க வேண்டாம்! உடனே கோகுலத்திற்குத் திரும்பி தங்களின் குழந்தையையும் குடும்பத்தையும் பாதுகாப்பீராக! ஏனெனில் கோகுலத்தை நோக்கி பல பயங்கரமான தீய சகுனங்களும் அமங்கலங்களும் எழுகின்றன!"

வசுதேவர் மேலும் கூறினார்: "கொடுங்கோலன் ஆளும் தலைநகரில் வரி செலுத்திய பின் நல்லவர்கள் தங்கக்கூடாது. ஆகாயத்திலும் பூமியிலும் தீய சகுனங்கள் தோன்றுகின்றன. கோகுலத்தின் குழந்தைகளுக்கு ஆபத்து நேரிடலாம். உடனே புறப்படுங்கள்!"

வசுதேவரின் தீர்க்கதரிசன எச்சரிக்கையை உணர்ந்த நந்த மகாராஜா சிறிதும் தாமதிக்கவில்லை. உடனே ஆயர்களைத் திரட்டிக்கொண்டு, தனது மாட்டு வண்டியில் ஏறி, குழந்தை கிருஷ்ணரைக் காக்க வேண்டும் என்று உள்ளூர பகவானைத் தியானித்தபடி கோகுலம் நோக்கி விரைந்தார்.""",
                "questions": [
                    {
                        "question": "நந்தோத்ஸவத்திற்குப் பின் நந்த மகாராஜா எதற்காக மதுரைக்குச் சென்றார்?",
                        "options": [
                            {"text": "மன்னன் கம்சனுக்கு செலுத்த வேண்டிய வருடாந்திர வரியைச் செலுத்த", "is_correct": True},
                            {"text": "குதிரைகளை வாங்க", "is_correct": False},
                            {"text": "கம்சனுடன் சண்டை போட", "is_correct": False},
                            {"text": "அரசவையில் வாதாட", "is_correct": False}
                        ]
                    },
                    {
                        "question": "மதுரை செல்லும் முன் கோகுலத்தின் பாதுகாப்பை நந்தர் யாரிடம் ஒப்படைத்தார்?",
                        "options": [
                            {"text": "அனுபவம் வாய்ந்த முதிய ஆயர்களிடம்", "is_correct": True},
                            {"text": "மதுரை காவலர்களிடம்", "is_correct": False},
                            {"text": "கூலிப் படைகளிடம்", "is_correct": False},
                            {"text": "வணிகர்களிடம்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "நந்த மகாராஜாவைக் கண்ட வசுதேவரின் மனநிலை சாஸ்திரத்தில் எவ்வாறு விவரிக்கப்படுகிறது?",
                        "options": [
                            {"text": "உயிரற்ற உடலுக்குள் மீண்டும் உயிர் மூச்சு திரும்பியது போல", "is_correct": True},
                            {"text": "வைரச் சுரங்கம் கிடைத்தது போல", "is_correct": False},
                            {"text": "நாட்டை வென்றது போல", "is_correct": False},
                            {"text": "அமைதியாகவும் சாதாரணமாகவும்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "நந்தரிடம் வசுதேவர் பிரத்யேகமாக விசாரித்த இரு குழந்தைகள் யார்?",
                        "options": [
                            {"text": "பலராமன் (ரோகிணியின் மகன்) மற்றும் புதிய குழந்தை (கிருஷ்ணர்)", "is_correct": True},
                            {"text": "பாண்டவர்கள்", "is_correct": False},
                            {"text": "கௌரவர்கள்", "is_correct": False},
                            {"text": "அபிமன்யு மற்றும் பரீக்ஷித்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "வசுதேவருக்கு நந்தர் கூறிய ஆறுதல் என்ன?",
                        "options": [
                            {"text": "ஆறு குழந்தைகளை இழந்த வசுதேவரின் துயரத்திற்கு ஆழ்ந்த அனுதாபம் தெரிவித்தார்", "is_correct": True},
                            {"text": "கடன் அடைக்க பணம் தந்தார்", "is_correct": False},
                            {"text": "மதுரையை விட்டு ஓடச் சொன்னார்", "is_correct": False},
                            {"text": "வசுதேவரைக் குற்றம் சாட்டினார்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "நந்தர் அறியாத எந்த ஆபத்தை வசுதேவர் அறிந்திருந்தார்?",
                        "options": [
                            {"text": "நாடெங்கும் பச்சிளம் குழந்தைகளைக் கொல்ல கம்சனின் அசுர சபை முடிவெடுத்துள்ளது என்பதை", "is_correct": True},
                            {"text": "வறட்சி வரப்போகிறது என்பதை", "is_correct": False},
                            {"text": "கம்சன் வெண்ணெய் திருட வருவான் என்பதை", "is_correct": False},
                            {"text": "புலி ஒன்று புகுந்துள்ளது என்பதை", "is_correct": False}
                        ]
                    },
                    {
                        "question": "நந்தருக்கு வசுதேவர் விடுத்த அவசர எச்சரிக்கை என்ன?",
                        "options": [
                            {"text": "மதுரையில் தங்காதீர், உடனே கோகுலம் சென்று குழந்தைகளைப் பாதுகாப்பீர்", "is_correct": True},
                            {"text": "மதுரையில் ஒரு மாதம் தங்கிச் செல்லுங்கள்", "is_correct": False},
                            {"text": "கிருஷ்ணரை மதுரைக்கு அழைத்து வாருங்கள்", "is_correct": False},
                            {"text": "காசிக்கு யாத்திரை செல்லுங்கள்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "வரி செலுத்திய பின் கொடுங்கோலன் ஆளும் நகரில் தங்கக் கூடாது என்று சாஸ்திரம் ஏன் கூறுகிறது?",
                        "options": [
                            {"text": "அசுர மன்னர்களால் எந்நேரமும் விபரீதமான ஆபத்துகள் நிகழலாம் என்பதால்", "is_correct": True},
                            {"text": "விடுதிகள் விலை அதிகம் என்பதால்", "is_correct": False},
                            {"text": "மாடுகளுக்கு நகரம் பிடிக்காது என்பதால்", "is_correct": False},
                            {"text": "சூரிய அஸ்தமனத்திற்குப் பின் வாணிகம் தடை என்பதால்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "வசுதேவரின் எச்சரிக்கையைக் கேட்ட நந்த மகாராஜா என்ன செய்தார்?",
                        "options": [
                            {"text": "உடனே தனது வண்டியில் ஏறி கோகுலம் நோக்கி விரைந்தார்", "is_correct": True},
                            {"text": "அதை அலட்சியம் செய்து மதுராவில் ஷாப்பிங் செய்தார்", "is_correct": False},
                            {"text": "வசுதேவரைப் பார்த்து சிரித்தார்", "is_correct": False},
                            {"text": "கம்சனிடம் சண்டைக்குச் சென்றார்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "நந்தர்-வசுதேவர் சந்திப்பு ஸ்ரீமத் பாகவதம் பத்தாம் ஸ்கந்தத்தில் எந்த அத்தியாயத்தில் உள்ளது?",
                        "options": [
                            {"text": "அத்தியாயம் 5", "is_correct": True},
                            {"text": "அத்தியாயம் 2", "is_correct": False},
                            {"text": "அத்தியாயம் 7", "is_correct": False},
                            {"text": "அத்தியாயம் 12", "is_correct": False}
                        ]
                    }
                ]
            },
            "hi": {
                "mainTopic": "कृष्ण लीलाएं",
                "subTopic": "मथुरा में नंद महाराज और वसुदेव का स्नेहपूर्ण मिलन",
                "content": """### नंद महाराज की मथुरा यात्रा

गोकुल में नंदोत्सव की आनंदमयी समाप्ति के उपरांत, गोपों के मुखिया नंद महाराज राजा कंस को वार्षिक कर चुकाने के लिए मथुरा जाने की तैयारी करने लगे। गोकुल और नन्हें कन्हैया की सुरक्षा का भार वृद्ध एवं विश्वस्त गोपों को सौंपकर, नंदबाबा कर की सामग्री, मक्खन और घी से भरी गाड़ियां लेकर मथुरा के लिए रवाना हुए।

उधर मथुरा में कंस द्वारा कारागार से मुक्त किए गए वसुदेव जी स्वतंत्र रूप से रह रहे थे। जब वसुदेव जी ने सुना कि उनके परम मित्र और भाई नंद महाराज कर चुकाने मथुरा आए हैं, तो उनका हृदय प्रेम से भर गया। वे तुरंत नंदबाबा से मिलने उनके पड़ाव की ओर चल पड़े।

### दो महाभागवतों का भावुक आलिंगन

शिविर में पहुंचकर जैसे ही वसुदेव जी ने नंद महाराज को देखा, उनके हृदय में भ्रातृ-प्रेम की लहरें उमड़ पड़ीं:

> **श्रीमद्भागवतम्, स्कंध 10, अध्याय 5, श्लोक 20**
> 
> *तं दृष्ट्वा सहसोत्थाय देहः प्राणम् इवागतम् ।*  
> *प्रीतः प्रियतमं दोर्भ्यां सस्वञ्जे प्रेम-विह्वलः ॥*  
> 
> **भावार्थ:** "अपने परम प्रिय मित्र और भाई नंद महाराज को देखकर वसुदेव जी ऐसे उठ खड़े हुए मानो किसी निर्जीव शरीर में प्राण लौट आए हों। परम प्रेम में विह्वल होकर वसुदेव जी ने दोनों भुजाओं से उन्हें कसकर गले लगा लिया।"

दोनों के नेत्रों से प्रेमाश्रुओं की धारा बह निकली। कंस के अत्याचारों और अपने छह पुत्रों के वध के बाद नंदबाबा से मिलना वसुदेव जी के लिए नवजीवन के समान था।

वसुदेव जी ने नंदबाबा को आसन पर बैठाकर कुशल-क्षेम पूछा: "प्रिय भाई नंद! बड़े सौभाग्य की बात है कि वृद्धावस्था में आपको पुत्ररत्न प्राप्त हुआ है! रोहिणी का पुत्र हमारा बालक बलराम आपके वात्सल्य में सुखी है न? और आपका नवजात कन्हैया भी आनंदपूर्वक है न? गोकुल की गऊएं और गोपगण सब कुशल से हैं न?"

### नंद महाराज की सांत्वना

नंद महाराज ने अत्यंत करुणापूर्वक कहा: "प्रिय भाई वसुदेव! आपके ऊपर जो विपत्तियों का पहाड़ टूटा, उसका हमें अत्यंत दुःख है। पापी कंस ने आपके छह बालकों का वध कर दिया और आठवीं कन्या आकाश में उड़ गई! प्रारब्ध और कर्म की गति बड़ी बलवान है, परंतु जो तत्वज्ञानी हैं वे सुख-दुःख में कभी विचलित नहीं होते।"

### वसुदेव जी की अत्यावश्यक चेतावनी

वसुदेव जी उस भयानक सत्य को जानते थे जिससे नंदबाबा अनभिज्ञ थे: गोकुल में पलने वाला बालक साक्षात् भगवान श्री कृष्ण हैं और कंस की आसुरी सभा ने नवजात शिशुओं के वध का आदेश दिया है!

कन्हैया और गोकुल की सुरक्षा को लेकर चिंतित वसुदेव जी ने नंदबाबा को तत्काल मथुरा छोड़ने की चेतावनी दी:

> **श्रीमद्भागवतम्, स्कंध 10, अध्याय 5, श्लोक 30**
> 
> *तातानुगम्य तावत् त्वं गोकुलं रक्ष पुत्रक ।*  
> *उत्पाता बहवस् तत्र दृश्यन्ते ह्य् अशुभावहाः ॥*  
> 
> **भावार्थ:** "प्रिय भाई नंद! अब जब आपने राजा को वार्षिक कर चुका दिया है, तो मथुरा में एक क्षण भी न रुकें! तुरंत गोकुल लौटकर अपने पुत्र और परिवार की रक्षा करें, क्योंकि मुझे वहां अनेक प्रकार के अशुभ उपद्रव और भयंकर उत्पात होते दिखाई दे रहे हैं!"

वसुदेव जी ने आग्रह किया: "अत्याचारी राजा की राजधानी में कर चुकाने के बाद अधिक रुकना उचित नहीं। प्रकृति में भयंकर अपशकुन दिखाई दे रहे हैं। गोकुल में बालकों पर विपत्ति आ सकती है। अतः बिना विलंब किए तुरंत लौट जाएं!"

वसुदेव जी के वचनों की गंभीरता को समझकर नंद महाराज ने तनिक भी विलंब नहीं किया। वे तुरंत अपने गोपों के साथ बैलगाड़ियों पर सवार होकर, मन ही मन भगवान से कन्हैया की रक्षा की प्रार्थना करते हुए गोकुल की ओर तीव्र गति से लौट पड़े।""",
                "questions": [
                    {
                        "question": "नंदोत्सव के बाद नंद महाराज मथुरा क्यों गए थे?",
                        "options": [
                            {"text": "कंस को वार्षिक कर और भेंट चुकाने के लिए", "is_correct": True},
                            {"text": "घोड़े खरीदने", "is_correct": False},
                            {"text": "कंस को युद्ध की चुनौती देने", "is_correct": False},
                            {"text": "घूमने-फिरने", "is_correct": False}
                        ]
                    },
                    {
                        "question": "मथुरा जाते समय गोकुल की रक्षा का भार नंदबाबा ने किन्हें सौंपा?",
                        "options": [
                            {"text": "वृद्ध और विश्वस्त गोपों को", "is_correct": True},
                            {"text": "कंस के सैनिकों को", "is_correct": False},
                            {"text": "भाड़े के सैनिकों को", "is_correct": False},
                            {"text": "व्यापारियों को", "is_correct": False}
                        ]
                    },
                    {
                        "question": "नंदबाबा को देखकर वसुदेव जी को कैसा अनुभव हुआ?",
                        "options": [
                            {"text": "जैसे निर्जीव शरीर में पुनः प्राण लौट आए हों", "is_correct": True},
                            {"text": "जैसे खजाना मिल गया हो", "is_correct": False},
                            {"text": "जैसे युद्ध जीत लिया हो", "is_correct": False},
                            {"text": "सामान्य अनुभव", "is_correct": False}
                        ]
                    },
                    {
                        "question": "वसुदेव जी ने नंद महाराज से किन दो बालकों के विषय में पूछा?",
                        "options": [
                            {"text": "बलराम (रोहिणी के पुत्र) और नवजात कन्हैया के विषय में", "is_correct": True},
                            {"text": "पांडवों के विषय में", "is_correct": False},
                            {"text": "कौरवों के विषय में", "is_correct": False},
                            {"text": "अभिमन्यु के विषय में", "is_correct": False}
                        ]
                    },
                    {
                        "question": "नंद महाराज ने वसुदेव जी को किस बात की सांत्वना दी?",
                        "options": [
                            {"text": "कंस द्वारा उनके छह बालकों की हत्या के प्रति गहरी संवेदना व्यक्त की", "is_correct": True},
                            {"text": "कर्ज चुकाने के लिए धन दिया", "is_correct": False},
                            {"text": "मथुरा छोड़कर भागने को कहा", "is_correct": False},
                            {"text": "वसुदेव को दोष दिया", "is_correct": False}
                        ]
                    },
                    {
                        "question": "वसुदेव जी किस गुप्त संकट से भली-भांति परिचित थे?",
                        "options": [
                            {"text": "कि कंस की आसुरी सभा ने नवजात बालकों के संहार का आदेश दिया है", "is_correct": True},
                            {"text": "कि अकाल पड़ने वाला है", "is_correct": False},
                            {"text": "कि कंस मक्खन छीनने आएगा", "is_correct": False},
                            {"text": "कि बाघ आ गया है", "is_correct": False}
                        ]
                    },
                    {
                        "question": "वसुदेव जी ने नंद महाराज को क्या गंभीर चेतावनी दी?",
                        "options": [
                            {"text": "मथुरा में तनिक भी न रुकें और तुरंत गोकुल लौटकर बालकों की रक्षा करें", "is_correct": True},
                            {"text": "मथुरा में एक महीना रुकें", "is_correct": False},
                            {"text": "कन्हैया को मथुरा ले आएं", "is_correct": False},
                            {"text": "काशी यात्रा पर जाएं", "is_correct": False}
                        ]
                    },
                    {
                        "question": "अत्याचारी राजा की राजधानी में कर चुकाने के बाद क्यों नहीं रुकना चाहिए?",
                        "options": [
                            {"text": "क्योंकि क्रूर राजा कभी भी अकारण संकट उत्पन्न कर सकता है", "is_correct": True},
                            {"text": "क्योंकि वहां भोजन महंगा है", "is_correct": False},
                            {"text": "क्योंकि बैल थक जाते हैं", "is_correct": False},
                            {"text": "क्योंकि सूर्यास्त के बाद यात्रा निषिद्ध है", "is_correct": False}
                        ]
                    },
                    {
                        "question": "वसुदेव जी की चेतावनी पर नंद महाराज ने क्या किया?",
                        "options": [
                            {"text": "उन्होंने तुरंत गाड़ियां जोड़ीं और गोकुल की ओर प्रस्थान किया", "is_correct": True},
                            {"text": "उन्होंने चेतावनी की उपेक्षा की", "is_correct": False},
                            {"text": "वे हंसने लगे", "is_correct": False},
                            {"text": "वे कंस से लड़ने चले गए", "is_correct": False}
                        ]
                    },
                    {
                        "question": "श्रीमद्भागवतम् के दसवें स्कंध का कौन सा अध्याय नंद-वसुदेव मिलन का वर्णन करता है?",
                        "options": [
                            {"text": "अध्याय 5", "is_correct": True},
                            {"text": "अध्याय 2", "is_correct": False},
                            {"text": "अध्याय 7", "is_correct": False},
                            {"text": "अध्याय 12", "is_correct": False}
                        ]
                    }
                ]
            },
            "ml": {
                "mainTopic": "കൃഷ്ണ ലീലകൾ",
                "subTopic": "മഥുരയിൽ നന്ദഗോപരും വസുദേവരും തമ്മിലുള്ള സ്നേഹസമാഗമം",
                "content": """### നന്ദഗോപരുടെ മഥുരായാത്ര

ഗോകുലത്തിലെ നന്ദോത്സവത്തിനു ശേഷം, ഗോപന്മാരുടെ മുഖ്യനായ നന്ദഗോപർ കംസരാജാവിന് നൽകേണ്ട വാർഷിക നികുതി സമർപ്പിക്കാനായി മഥുരയിലേക്ക് പോകാൻ തീരുമാനിച്ചു. ഗോകുലത്തിന്റെയും ഉണ്ണികൃഷ്ണന്റെയും സംരക്ഷണച്ചുമതല വിശ്വസ്തരായ മുതിർന്ന ഗോപന്മാരെ ഏൽപ്പിച്ച്, വെണ്ണയും നെയ്യും നികുതിദ്രവ്യങ്ങളും വണ്ടികളിൽ കയറ്റി നന്ദഗോപർ മഥുരയിലേക്ക് തിരിച്ചു.

അക്കാലത്ത് കാരാഗൃഹത്തിൽ നിന്നും മോചിതനായ വസുദേവർ മഥുരയിൽ സമാധാനമായി ജീവിക്കുകയായിരുന്നു. തന്റെ പ്രിയമിത്രമായ നന്ദഗോപർ മഥുരയിലെത്തിയ വിവരം അറിഞ്ഞപ്പോൾത്തന്നെ വസുദേവർ അദ്ദേഹത്തെ കാണാൻ പുറപ്പെട്ടു.

### സ്നേഹനിർഭരമായ ആലിംഗനം

നന്ദഗോപരെ കണ്ടമാത്രയിൽ വസുദേവരുടെ ഹൃദയം സ്നേഹത്താൽ നിറഞ്ഞുതുളുമ്പി:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അദ്ധ്യായം 5, ശ്ലോകം 20**
> 
> *തം ദൃഷ്ട്വാ സഹസോത്ഥായ ദേഹഃ പ്രാണം ഇവാഗതം |*  
> *പ്രീതഃ പ്രിയതമം ദോർഭ്യാം സസ്വഞ്ജേ പ്രേമ-വിഹ്വലഃ ||*  
> 
> **അർത്ഥം:** "തന്റെ പ്രിയമിത്രമായ നന്ദഗോപരെ കണ്ട വസുദേവർ, ജീവനില്ലാത്ത ശരീരത്തിലേക്ക് പ്രാണൻ തിരിച്ചെത്തിയതുപോലെ പെട്ടെന്ന് എഴുന്നേറ്റുനിന്ന്, പ്രേമവിഹ്വലനായി രണ്ടു കൈകളും നീട്ടി അദ്ദേഹത്തെ ഗാഢമായി ആലിംഗനം ചെയ്തു."

കംസന്റെ ക്രൂരതകൾ അനുഭവിച്ച് മക്കളെ നഷ്ടപ്പെട്ട വസുദേവർക്ക് നന്ദഗോപരുമായുള്ള സമാഗമം ഒരു പുനർജന്മം പോലെയായിരുന്നു.

നന്ദഗോപരെ ആദരവോടെ ഇരുത്തി വസുദേവർ കുശലാന്വേഷണം നടത്തി: "പ്രിയ സഹോദരാ നന്ദരേ! അങ്ങേയ്ക്ക് ഈ വാർദ്ധക്യത്തിൽ ഒരു ഉണ്ണി പിറന്നത് വലിയ ഭാഗ്യം തന്നെ! രോഹിണിയുടെ മകനായ ബലരാമൻ അങ്ങയുടെ സ്നേഹത്തിൽ സുഖമായിരിക്കുന്നുവോ? അങ്ങയുടെ നവജാതശിശുവും ഗോകുലത്തിലെ പശുക്കളും സുഖമായിരിക്കുന്നുവോ?"

### നന്ദഗോപരുടെ സാന്ത്വനവാക്കുകൾ

നന്ദഗോപർ തികഞ്ഞ അനുകമ്പയോടെ പറഞ്ഞു: "പ്രിയ വസുദേവരാ! അങ്ങ് അനുഭവിച്ച കഷ്ടപ്പാടുകൾ ഞങ്ങൾക്കറിയാം. ക്രൂരനായ കംസൻ അങ്ങയുടെ ആറു മക്കളെ കൊന്നു, എട്ടാമത്തെ പെൺകുഞ്ഞ് ആകാശത്തേക്കു മറഞ്ഞു. കർമ്മഫലവും വിധിയും ആർക്കും തടുക്കാനാവില്ല. എങ്കിലും ആത്മജ്ഞാനികൾ സുഖദുഃഖങ്ങളിൽ തളരുകയില്ല."

### വസുദേവരുടെ മുന്നറിയിപ്പ്

കംസന്റെ അസുരസഭ കുഞ്ഞുങ്ങളെ കൊല്ലാൻ ഉത്തരവിട്ടിട്ടുണ്ടെന്ന ഭയാനകമായ രഹസ്യം വസുദേവർക്കറിയാമായിരുന്നു. അതിനാൽ ഉണ്ണികൃഷ്ണന്റെ സുരക്ഷയോർത്ത് വസുദേവർ നന്ദഗോപർക്ക് അടിയന്തര മുന്നറിയിപ്പ് നൽകി:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അദ്ധ്യായം 5, ശ്ലോകം 30**
> 
> *താതാനുഗമ്യ താവത് ത്വം ഗോകുലം രക്ഷ പുത്രക |*  
> *ഉത്പാതാ ബഹവസ് തത്ര ദൃശ്യന്തേ ഹ്യ് അശുഭാവഹാഃ ||*  
> 
> **അർത്ഥം:** "പ്രിയ സഹോദരാ നന്ദരേ! രാജാവിനുള്ള നികുതി നൽകിക്കഴിഞ്ഞ സ്ഥിതിക്ക് ഇനി ഒരു നിമിഷംപോലും മഥുരയിൽ തങ്ങരുത്! ഉടൻതന്നെ ഗോകുലത്തിലേക്ക് മടങ്ങി അങ്ങയുടെ മകനെയും കുടുംബത്തെയും സംരക്ഷിക്കൂ; അവിടെ പലവിധ ദുർന്നിമിത്തങ്ങളും വിപത്തുകളും സംഭവിക്കാൻ സാധ്യതയുണ്ട്!"

വസുദേവർ തുടർന്നു: "ക്രൂരരാജാവിന്റെ തലസ്ഥാനത്ത് നികുതി കൊടുത്തുകഴിഞ്ഞാൽ കൂടുതൽ സമയം തങ്ങുന്നത് ഉചിതമല്ല. ഉടൻ മടങ്ങുക!"

വസുദേവരുടെ വാക്കുകളുടെ ഗൗരവം മനസ്സിലാക്കിയ നന്ദഗോപർ ഒട്ടും വൈകാതെ വണ്ടികളുമായി ഗോകുലത്തിലേക്ക് യാത്ര തിരിച്ചു.""",
                "questions": [
                    {
                        "question": "നന്ദോത്സവത്തിനു ശേഷം നന്ദഗോപർ എന്തിനാണ് മഥുരയിലേക്ക് പോയത്?",
                        "options": [
                            {"text": "കംസന് വാർഷിക നികുതി നൽകാൻ", "is_correct": True},
                            {"text": "കുതിരകളെ വാങ്ങാൻ", "is_correct": False},
                            {"text": "കംസനോട് യുദ്ധം ചെയ്യാൻ", "is_correct": False},
                            {"text": "വിനോദസഞ്ചാരത്തിന്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "മഥുരയിലേക്ക് പോകുമ്പോൾ ഗോകുലത്തിന്റെ ചുമതല ആരെയാണ് ഏൽപ്പിച്ചത്?",
                        "options": [
                            {"text": "വിശ്വസ്തരായ മുതിർന്ന ഗോപന്മാരെ", "is_correct": True},
                            {"text": "കംസന്റെ സൈന്യത്തെ", "is_correct": False},
                            {"text": "കൂലിപ്പട്ടാളത്തെ", "is_correct": False},
                            {"text": "കച്ചവടക്കാരെ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "നന്ദഗോപരെ കണ്ടപ്പോൾ വസുദേവർക്ക് എന്തു തോന്നി?",
                        "options": [
                            {"text": "നിർജ്ജീവ ശരീരത്തിലേക്ക് പ്രാണൻ തിരിച്ചെത്തിയതുപോലെ", "is_correct": True},
                            {"text": "നിധി കിട്ടിയതുപോലെ", "is_correct": False},
                            {"text": "യുദ്ധം ജയിച്ചതുപോലെ", "is_correct": False},
                            {"text": "യാതൊരു ഭാവവ്യത്യാസവുമില്ലാതെ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഏതു രണ്ടു കുട്ടികളെക്കുറിച്ചാണ് വസുദേവർ ചോദിച്ചറിഞ്ഞത്?",
                        "options": [
                            {"text": "ബലരാമനെയും നവജാതനായ ഉണ്ണികൃഷ്ണനെയും കുറിച്ച്", "is_correct": True},
                            {"text": "പാണ്ഡവരെക്കുറിച്ച്", "is_correct": False},
                            {"text": "കൗരവരെക്കുറിച്ച്", "is_correct": False},
                            {"text": "അഭിമന്യുവിനെക്കുറിച്ച്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "നന്ദഗോപർ വസുദേവർക്ക് എന്തു സാന്ത്വനമാണ് നൽകിയത്?",
                        "options": [
                            {"text": "ആറു മക്കൾ കൊല്ലപ്പെട്ടതിൽ അഗാധമായ അനുശോചനം അറിയിച്ചു", "is_correct": True},
                            {"text": "പണം കൊടുത്തു", "is_correct": False},
                            {"text": "നാടുവിട്ടുപോകാൻ പറഞ്ഞു", "is_correct": False},
                            {"text": "വസുദേവരെ കുറ്റപ്പെടുത്തി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "നന്ദഗോപർക്ക് അറിയാത്ത ഏതു രഹസ്യമാണ് വസുദേവർ അറിഞ്ഞിരുന്നത്?",
                        "options": [
                            {"text": "കംസന്റെ അസുരന്മാർ കുഞ്ഞുങ്ങളെ കൊല്ലാൻ ഇറങ്ങിത്തിരിച്ചിട്ടുണ്ടെന്ന്", "is_correct": True},
                            {"text": "ക്ഷാമം വരുന്നുണ്ടെന്ന്", "is_correct": False},
                            {"text": "കംസൻ വെണ്ണ മോഷ്ടിക്കുമെന്ന്", "is_correct": False},
                            {"text": "കടുവ വന്നിട്ടുണ്ടെന്ന്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "വസുദേവർ നന്ദഗോപർക്ക് നൽകിയ മുന്നറിയിപ്പ് എന്തായിരുന്നു?",
                        "options": [
                            {"text": "മഥുരയിൽ തങ്ങാതെ ഉടൻ ഗോകുലത്തിൽ മടങ്ങിയെത്തി കുഞ്ഞുങ്ങളെ സംരക്ഷിക്കുക", "is_correct": True},
                            {"text": "ഒരു മാസം മഥുരയിൽ താമസിക്കുക", "is_correct": False},
                            {"text": "കൃഷ്ണനെ മഥുരയിലേക്ക് കൊണ്ടുവരിക", "is_correct": False},
                            {"text": "കാശിയിലേക്ക് തീർത്ഥാടനം പോവുക", "is_correct": False}
                        ]
                    },
                    {
                        "question": "നികുതി കൊടുത്ത ശേഷം ക്രൂരരാജാവിന്റെ നഗരത്തിൽ തങ്ങരുതെന്ന് ശാസ്ത്രം പറയുന്നത് എന്തുകൊണ്ട്?",
                        "options": [
                            {"text": "ക്രൂരരാജാക്കന്മാർ എപ്പോൾ വേണമെങ്കിലും വിപത്തുണ്ടാക്കാം എന്നതുകൊണ്ട്", "is_correct": True},
                            {"text": "ഹോട്ടലുകൾക്ക് വിലകൂടുതലായതുകൊണ്ട്", "is_correct": False},
                            {"text": "കാളകൾ ക്ഷീണിക്കുന്നതുകൊണ്ട്", "is_correct": False},
                            {"text": "സന്ധ്യയ്ക്കു ശേഷം യാത്ര നിരോധിച്ചതുകൊണ്ട്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "വസുദേവരുടെ മുന്നറിയിപ്പ് കേട്ട് നന്ദഗോപർ എന്തു ചെയ്തു?",
                        "options": [
                            {"text": "ഒട്ടും വൈകാതെ വണ്ടികളുമായി ഗോകുലത്തിലേക്ക് മടങ്ങി", "is_correct": True},
                            {"text": "മുന്നറിയിപ്പ് അവഗണിച്ചു", "is_correct": False},
                            {"text": "ചിരിച്ചു തള്ളി", "is_correct": False},
                            {"text": "കംസനോട് യുദ്ധം ചെയ്യാൻ പോയി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ശ്രീമദ് ഭാഗവതം പത്താം സ്കന്ധത്തിലെ ഏത് അദ്ധ്യായത്തിലാണ് നന്ദ-വസുദേവ സമാഗമം?",
                        "options": [
                            {"text": "അദ്ധ്യായം 5", "is_correct": True},
                            {"text": "അദ്ധ്യായം 2", "is_correct": False},
                            {"text": "അദ്ധ്യായം 7", "is_correct": False},
                            {"text": "അദ്ധ്യായം 12", "is_correct": False}
                        ]
                    }
                ]
            },
            "bn": {
                "mainTopic": "কৃষ্ণ লীলা",
                "subTopic": "মথুরায় নন্দ মহারাজ ও বসুদেবের পরম স্নেহময় মিলন",
                "content": """### নন্দ মহারাজের মথুরা যাত্রা

গোকুলে নন্দোৎসব উদযাপনের পর, গোপপ্রধান নন্দ মহারাজ রাজা কংসের বার্ষিক রাজকর পরিশোধের উদ্দেশ্যে মথুরায় গমনের প্রস্তুতি গ্রহণ করলেন। গোকুল ও বালক কৃষ্ণের সুরক্ষার দায়িত্ব বিশ্বস্ত বৃদ্ধ গোপদের হস্তে সমর্পণ করে, তিনি করের দ্রব্যাদি, নবনীত ও ঘৃতপূর্ণ শকটসহ মথুরায় উপনীত হলেন।

এদিকে মথুরায় কারাগার থেকে মুক্ত বসুদেব স্বাধীনভাবে বাস করছিলেন। প্রিয় ভ্রাতা নন্দ মহারাজ মথুরায় উপস্থিত হয়েছেন শ্রবণমাত্র বসুদেবের অন্তর অপার্থিব আনন্দে উদ্বেলিত হলো। তিনি কালবিলম্ব না করে নন্দের শিবিরের অভিমুখে গমন করলেন।

### দুই ভক্তের পরম স্নেহময় আলিঙ্গন

শিবিরে প্রবেশ করে নন্দ মহারাজকে দর্শনমাত্র বসুদেবের অন্তরে ভ্রাতৃস্নেহের প্লাবন দেখা দিল:

> **শ্রীমদ্ভাগবত, স্কন্ধ ১০, অধ্যায় ৫, শ্লোক ২০**
> 
> *তং দৃষ্ট্বা সহসোত্থায় দেহঃ প্রাণম্ ইবাগতম্ ।*  
> *প্রীতঃ প্রিয়তমং দোর্ব্যাং সস্বঞ্জে প্রেম-বিহ্বলঃ ॥*  
> 
> **অনুবাদ:** "পরম প্রিয় সুহৃদ নন্দ মহারাজকে দর্শন করে বসুদেব সহসা গাত্রোত্থান করলেন, যেন নির্জীব দেহে পুনরায় প্রাণবায়ু সঞ্চারিত হলো। পরম প্রেমে বিহ্বল হয়ে তিনি উভয় বাহু দ্বারা নন্দকে গাঢ় আলিঙ্গন করলেন।"

উভয়ের নয়ন হতে প্রেমাশ্রুধারা প্রবাহিত হলো। কংসের অমানুষিক নিগ্রহ সহ্য করে ছয়টি পুত্র হারানোর পর নন্দের দর্শন বসুদেবের নিকট নবজীবনের তুল্য প্রতিভাত হলো।

বসুদেব নন্দকে সসম্মানে উপবেশন করিয়ে কুশলবার্তা জিজ্ঞাসা করলেন: "প্রিয় ভ্রাতা নন্দ! অতিশয় সৌভাগ্যের বিষয় যে পরিণত বয়সে আপনি পুত্ররত্ন লাভ করেছেন! রোহিণীপুত্র বলরাম আপনার স্নেহে কুশলে আছে তো? আপনার নবজাত শিশুটি সুস্থ ও আনন্দময় আছে তো? গোকুলের গাভী ও গোপগণ নিরাপদে আছেন তো?"

### নন্দের সান্ত্বনা প্রদান

নন্দ মহারাজ পরম সহানুভূতির সহিত বললেন: "প্রিয় ভ্রাতা বসুদেব! আপনার প্রতি কংসের নির্মম অত্যাচারের কথা স্মরণ করে আমরা ব্যথিত। কংস আপনার ছয়টি পুত্রকে হত্যা করেছে এবং অষ্টম কন্যা আকাশে অন্তর্হিতা হয়েছে। প্রারব্ধ ও কর্মের গতি দুর্লঙ্ঘ্য, কিন্তু তত্ত্বজ্ঞ ব্যক্তিরা জাগতিক সুখ-দুঃখে বিচলিত হন না।"

### বসুদেবের সতর্কবার্তা

বসুদেব সেই গুপ্ত বিপদের কথা জানতেন যা নন্দ জানতেন না: কংসের অসুর মন্ত্রীরা নবজাতকদের হত্যার ষড়যন্ত্র করেছে!

কৃষ্ণের সুরক্ষায় উদ্বিগ্ন বসুদেব নন্দকে অবিলম্বে মথুরা ত্যাগের পরামর্শ দিলেন:

> **শ্রীমদ্ভাগবত, স্কন্ধ ১০, অধ্যায় ৫, শ্লোক ৩০**
> 
> *তাতানুগম্য তাবৎ ত্বং গোকুলং রক্ষ পুত্রক ।*  
> *উৎপাতা বহবস্তত্র দৃশ্যন্তে হ্য্ অশুভাবহাহ্ ॥*  
> 
> **অনুবাদ:** "হে ভ্রাতঃ নন্দ! রাজকর পরিশোধ হয়ে গেছে, অতএব মথুরায় আর একটি মুহূর্তও বিলম্ব করবেন না! অবিলম্বে গোকুলে ফিরে আপনার পুত্র ও পরিবারকে রক্ষা করুন, কেননা সেখানে বহু অশুভ উৎপাত ও অমঙ্গলের সম্ভাবনা দেখা যাচ্ছে!"

বসুদেবের প্রজ্ঞাপূর্ণ বাক্যের গুরুত্ব উপলব্ধি করে নন্দ মহারাজ বিন্দুমাত্র কালক্ষেপ না করে শকটসহ গোকুলাভিমুখে দ্রুত যাত্রা করলেন।""",
                "questions": [
                    {
                        "question": "নন্দ মহারাজ কেন মথুরায় গিয়েছিলেন?",
                        "options": [
                            {"text": "রাজা কংসকে বার্ষিক রাজকর পরিশোধ করতে", "is_correct": True},
                            {"text": "ঘোড়া কিনতে", "is_correct": False},
                            {"text": "যুদ্ধ করতে", "is_correct": False},
                            {"text": "ভ্রমণ করতে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "মথুরা যাবার সময় গোকুলের দায়িত্ব কার ওপর অর্পণ করা হয়েছিল?",
                        "options": [
                            {"text": "বৃদ্ধ ও বিশ্বস্ত গোপদের ওপর", "is_correct": True},
                            {"text": "কংসের সৈন্যদের ওপর", "is_correct": False},
                            {"text": "ভাড়াটে প্রহরীদের ওপর", "is_correct": False},
                            {"text": "বণিকদের ওপর", "is_correct": False}
                        ]
                    },
                    {
                        "question": "নন্দ মহারাজকে দেখে বসুদেবের কি অনুভূতি হয়েছিল?",
                        "options": [
                            {"text": "নির্জীব দেহে যেন প্রাণ ফিরে এলো", "is_correct": True},
                            {"text": "রত্নভাণ্ডার পাওয়ার মতো", "is_correct": False},
                            {"text": "যুদ্ধজয়ের মতো", "is_correct": False},
                            {"text": "স্বাভাবিক", "is_correct": False}
                        ]
                    },
                    {
                        "question": "বসুদেব বিশেষ করে কোন দুটি শিশুর কুশল জানতে চেয়েছিলেন?",
                        "options": [
                            {"text": "বলরাম এবং নবজাত শিশু কৃষ্ণের", "is_correct": True},
                            {"text": "পাণ্ডবদের", "is_correct": False},
                            {"text": "কৌরবদের", "is_correct": False},
                            {"text": "অভিমন্যুর", "is_correct": False}
                        ]
                    },
                    {
                        "question": "নন্দ মহারাজ বসুদেবকে কি বিষয়ে সান্ত্বনা দিয়েছিলেন?",
                        "options": [
                            {"text": "ছয়টি পুত্রের মৃত্যুর বিষয়ে গভীর সমবেদনা জানিয়েছিলেন", "is_correct": True},
                            {"text": "ঋণ শোধের অর্থ দিয়েছিলেন", "is_correct": False},
                            {"text": "পলায়ন করতে বলেছিলেন", "is_correct": False},
                            {"text": "দোষারোপ করেছিলেন", "is_correct": False}
                        ]
                    },
                    {
                        "question": "বসুদেব কোন বিপদের কথা জানতেন যা নন্দ জানতেন না?",
                        "options": [
                            {"text": "অসুরেরা নবজাতকদের হত্যার ষড়যন্ত্র করেছে", "is_correct": True},
                            {"text": "দুর্ভিক্ষ আসছে", "is_correct": False},
                            {"text": "কংস মাখন লুট করবে", "is_correct": False},
                            {"text": "বাঘ এসেছে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "বসুদেব নন্দকে কি জরুরী নির্দেশ দিয়েছিলেন?",
                        "options": [
                            {"text": "মথুরায় না থেমে অবিলম্বে গোকুলে ফিরে শিশুদের রক্ষা করতে", "is_correct": True},
                            {"text": "এক মাস মথুরায় থাকতে", "is_correct": False},
                            {"text": "কৃষ্ণকে মথুরায় নিয়ে আসতে", "is_correct": False},
                            {"text": "কাশী তীর্থে যেতে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "কর দেবার পর অত্যাচারী রাজার রাজধানীতে কেন বিলম্ব করা অনুচিত?",
                        "options": [
                            {"text": "অত্যাচারী রাজা যে কোনো সময় আকস্মিক বিপদ সৃষ্টি করতে পারে", "is_correct": True},
                            {"text": "হোটেল ব্যয়বহুল বলে", "is_correct": False},
                            {"text": "বলদ ক্লান্ত হয় বলে", "is_correct": False},
                            {"text": "সন্ধ্যায় ভ্রমণ নিষেধ বলে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "বসুদেবের সাবধানবাণী শুনে নন্দ কি করলেন?",
                        "options": [
                            {"text": "বিলম্বে না করে দ্রুত গোকুলাভিমুখে রওয়ানা হলেন", "is_correct": True},
                            {"text": "উপেক্ষা করলেন", "is_correct": False},
                            {"text": "হাসাহাসি করলেন", "is_correct": False},
                            {"text": "যুদ্ধ করতে গেলেন", "is_correct": False}
                        ]
                    },
                    {
                        "question": "শ্রীমদ্ভাগবতের দশম স্কন্ধের কোন অধ্যায়ে নন্দ-বসুদেব মিলন বর্ণিত?",
                        "options": [
                            {"text": "অধ্যায় ৫", "is_correct": True},
                            {"text": "অধ্যায় ২", "is_correct": False},
                            {"text": "অধ্যায় ৭", "is_correct": False},
                            {"text": "অধ্যায় ১২", "is_correct": False}
                        ]
                    }
                ]
            },
            "te": {
                "mainTopic": "కృష్ణ లీలలు",
                "subTopic": "మథురలో నందమహారాజు మరియు వసుదేవుల స్నేహపూర్వక కలయిక",
                "content": """### నందుని మథురా ప్రయాణం

గోకులంలో నందోత్సవం ముగిసిన తర్వాత, నందమహారాజు కంసునికి చెల్లించాల్సిన వార్షిక పన్నులను సమర్పించడానికి మథురకు వెళ్ళడానికి సిద్ధమయ్యాడు. గోకులాన్ని, బాలకృష్ణుని సంరక్షించే బాధ్యతను అనుభవజ్ఞులైన వృద్ధ గోపకులకు అప్పగించి, పన్నుల సామగ్రితో నందుడు మథురకు బయలుదేరాడు.

ఆ సమయంలో కారాగార విముక్తుడైన వసుదేవుడు మథురలో నివసిస్తున్నాడు. తన ప్రాణస్నేహితుడైన నందమహారాజు మథురకు వచ్చాడని తెలియగానే వసుదేవుని హృదయం ఆనందంతో ఉప్పొంగింది. వెంటనే నందుని విడిది వైపు వెళ్ళాడు.

### ఇరువురు భక్తుల దివ్య ఆలింగనం

నందమహారాజును చూడగానే వసుదేవునికి కలిగిన అనుభూతిని భాగవతం ఇలా వర్ణిస్తోంది:

> **శ్రీమద్భాగవతం, స్కంధం 10, అధ్యాయం 5, శ్లోకం 20**
> 
> *తం దృష్ట్వా సహసోత్థాయ దేహః ప్రాణమ్ ఇవాగతమ్ |*  
> *ప్రీతః ప్రియతమం దోర్భ్యాం సస్వఞ్జే ప్రేమ-విహ్వలః ||*  
> 
> **తాత్పర్యం:** "తన ప్రియతమ మిత్రుడైన నందమహారాజును చూడగానే వసుదేవుడు ప్రాణం లేని శరీరంలోకి ప్రాణం తిరిగి వచ్చినట్లుగా లేచి నిలబడి, ప్రేమతో తన రెండు చేతులతో ఆయనను గాఢంగా ఆలింగనం చేసుకున్నాడు."

కంసుని బాధల తర్వాత నందుని కలవడం వసుదేవునికి పునర్జన్మలా అనిపించింది.

వసుదేవుడు నందుని కుశలప్రశ్నలు అడిగాడు: "మిత్రమా నందా! వృద్ధాప్యంలో నీకు కుమారుడు జన్మించడం మహాభాగ్యం! రోహిణీదేవి కుమారుడు బలరాముడు మీ ప్రేమలో క్షేమంగా ఉన్నాడా? నీ పసికందు కృష్ణుడు ఆనందంగా ఉన్నాడా? గోకులంలోని గోవులు క్షేమమేనా?"

### నందుని ఓదార్పు

నందుడు ఎంతో సానుభూతితో ఇలా అన్నాడు: "వసుదేవా! కంసుడు నీ ఆరుగురు బిడ్డలను చంపడం, ఎనిమిదవ సంతానం ఆకాశంలోకి వెళ్ళిపోవడం ఎంతటి ఘోరమో మాకు తెలుసు. కర్మఫలం అనివార్యం, కానీ జ్ఞానులు సుఖదుఃఖాలలో చలించరు."

### వసుదేవుని అత్యవసర హెచ్చరిక

కంసుని అసుర సభ పసిపిల్లలను సంహరించడానికి ఆజ్ఞాపించిందన్న రహస్యం వసుదేవునికి మాత్రమే తెలుసు. కాబట్టి కృష్ణుని రక్షణ కోసం వసుదేవుడు నందుని ఇలా హెచ్చరించాడు:

> **శ్రీమద్భాగవతం, స్కంధం 10, అధ్యాయం 5, శ్లోకం 30**
> 
> *తాతానుగమ్య తావత్ త్వం గోకులం రక్ష పుత్రక |*  
> *ఉత్పాతా బహవస్ తత్ర దృశ్యంతే హ్య్ అశుభావహాః ||*  
> 
> **తాత్పర్యం:** "ప్రియ సోదరా నందా! రాజుకు పన్నులు చెల్లించావు కదా, ఇక మథురలో ఒక్క క్షణం కూడా ఆలస్యం చేయకు! వెంటనే గోకులానికి వెళ్ళి నీ కుమారుని, కుటుంబాన్ని రక్షించుకో; అక్కడ అనేక అశుభాలు, ఉత్పాతాలు జరిగే సూచనలు కనిపిస్తున్నాయి!"

వసుదేవుని మాటలలోని ఆంతర్యాన్ని గ్రహించిన నందమహారాజు ఆలస్యం చేయకుండా గోకుల ప్రయాణమయ్యాడు.""",
                "questions": [
                    {
                        "question": "నందోత్సవం తర్వాత నందమహారాజు మథురకు ఎందుకు వెళ్ళాడు?",
                        "options": [
                            {"text": "కంసునికి వార్షిక పన్నులు చెల్లించడానికి", "is_correct": True},
                            {"text": "గుర్రాలు కొనడానికి", "is_correct": False},
                            {"text": "కంసునితో యుద్ధం చేయడానికి", "is_correct": False},
                            {"text": "విహారయాత్రకు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "మథురకు వెళ్ళేటప్పుడు గోకుల రక్షణను ఎవరికి అప్పగించారు?",
                        "options": [
                            {"text": "వృద్ధ, అనుభవజ్ఞులైన గోపకులకు", "is_correct": True},
                            {"text": "కంసుని సైనికులకు", "is_correct": False},
                            {"text": "రక్షకభటులకు", "is_correct": False},
                            {"text": "వర్తకులకు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "నందుని చూడగానే వసుదేవునికి కలిగిన భావన ఏమిటి?",
                        "options": [
                            {"text": "నిర్జీవ శరీరంలోకి ప్రాణం వచ్చినట్లుగా", "is_correct": True},
                            {"text": "నిధి దొరికినట్లుగా", "is_correct": False},
                            {"text": "యుద్ధం గెలిచినట్లుగా", "is_correct": False},
                            {"text": "సాధారణంగా", "is_correct": False}
                        ]
                    },
                    {
                        "question": "వసుదేవుడు ఏ ఇద్దరు పిల్లల గురించి ప్రత్యేకంగా అడిగాడు?",
                        "options": [
                            {"text": "బలరాముడు మరియు పసికందు కృష్ణుని గురించి", "is_correct": True},
                            {"text": "పాండవుల గురించి", "is_correct": False},
                            {"text": "కౌరవుల గురించి", "is_correct": False},
                            {"text": "అభిమన్యుని గురించి", "is_correct": False}
                        ]
                    },
                    {
                        "question": "నందుడు వసుదేవుని ఏ విషయమై ఓదార్చాడు?",
                        "options": [
                            {"text": "ఆరుగురు పిల్లల మరణం పట్ల సానుభూతి తెలిపాడు", "is_correct": True},
                            {"text": "ధనం ఇచ్చాడు", "is_correct": False},
                            {"text": "పారిపోమన్నాడు", "is_correct": False},
                            {"text": "నిందించాడు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "నందునికి తెలియని ఏ ప్రమాదం వసుదేవునికి తెలుసు?",
                        "options": [
                            {"text": "రాక్షసులు పసిపిల్లలను చంపడానికి కుట్ర పన్నారని", "is_correct": True},
                            {"text": "కరువు వస్తుందని", "is_correct": False},
                            {"text": "వెన్న దొంగిలిస్తారని", "is_correct": False},
                            {"text": "పులి వచ్చిందని", "is_correct": False}
                        ]
                    },
                    {
                        "question": "వసుదేవుడు నందునికి ఇచ్చిన హెచ్చరిక ఏమిటి?",
                        "options": [
                            {"text": "మథురలో ఉండకుండా వెంటనే గోకులానికి వెళ్ళి పిల్లలను రక్షించుకోమని", "is_correct": True},
                            {"text": "నెల రోజులు మథురలో ఉండమని", "is_correct": False},
                            {"text": "కృష్ణుని మథురకు తీసుకురమ్మని", "is_correct": False},
                            {"text": "కాశీకి వెళ్ళమని", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పన్నులు చెల్లించాక దుష్టరాజు నగరంలో ఎందుకు ఆగకూడదు?",
                        "options": [
                            {"text": "క్రూరరాజులు ఎప్పుడైనా హాని తలపెట్టవచ్చు కాబట్టి", "is_correct": True},
                            {"text": "ఖర్చులు ఎక్కువని", "is_correct": False},
                            {"text": "ఎడ్లు అలసిపోతాయని", "is_correct": False},
                            {"text": "చీకటి పడుతుందని", "is_correct": False}
                        ]
                    },
                    {
                        "question": "వసుదేవుని హెచ్చరిక విన్న నందుడు ఏమి చేశాడు?",
                        "options": [
                            {"text": "వెంటనే బండ్లతో గోకులానికి బయలుదేరాడు", "is_correct": True},
                            {"text": "పట్టించుకోలేదు", "is_correct": False},
                            {"text": "నవ్వేశాడు", "is_correct": False},
                            {"text": "యుద్ధానికి వెళ్ళాడు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "భాగవతంలో ఏ అధ్యాయం నంద-వసుదేవుల కలయికను వివరిస్తుంది?",
                        "options": [
                            {"text": "అధ్యాయం 5", "is_correct": True},
                            {"text": "అధ్యాయం 2", "is_correct": False},
                            {"text": "అధ్యాయం 7", "is_correct": False},
                            {"text": "అధ్యాయం 12", "is_correct": False}
                        ]
                    }
                ]
            },
            "kn": {
                "mainTopic": "ಕೃಷ್ಣ ಲೀಲೆಗಳು",
                "subTopic": "ಮಥುರೆಯಲ್ಲಿ ನಂದಮಹಾರಾಜ ಮತ್ತು ವಸುದೇವರ ಸ್ನೇಹಪೂರ್ಣ ದಿವ್ಯ ಮಿಲನ",
                "content": """### ನಂದಮಹಾರಾಜರ ಮಥುರಾ ಯಾತ್ರೆ

ಗೋಕುಲದಲ್ಲಿ ನಂದೋತ್ಸವ ಮುಗಿದ ನಂತರ, ಗೋಪರ ಮುಖ್ಯಸ್ಥರಾದ ನಂದಮಹಾರಾಜರು ಕಂಸನಿಗೆ ವಾರ್ಷಿಕ ಕಪ್ಪಕಾಣಿಕೆಗಳನ್ನು ಸಲ್ಲಿಸಲು ಮಥುರೆಗೆ ತೆರಳಲು ಸಿದ್ಧರಾದರು. ಗೋಕುಲದ ಮತ್ತು ಬಾಲಕೃಷ್ಣನ ರಕ್ಷಣೆಯನ್ನು ಹಿರಿಯ ಗೋಪಾಲಕರಿಗೆ ಒಪ್ಪಿಸಿ, ಕಪ್ಪದ ಸಾಮಗ್ರಿಗಳು, ಬೆಣ್ಣೆ ಮತ್ತು ತುಪ್ಪದ ಬಂಡಿಗಳೊಂದಿಗೆ ನಂದರು ಮಥುರೆಗೆ ತೆರಳಿದರು.

ಆ ಸಮಯದಲ್ಲಿ ಕಾರಾಗೃಹದಿಂದ ಮುಕ್ತರಾಗಿದ್ದ ವಸುದೇವರು ಮಥುರೆಯಲ್ಲಿದ್ದರು. ತಮ್ಮ ಪ್ರಿಯಮಿತ್ರ ನಂದರು ಬಂದಿರುವ ಸುದ್ದಿ ತಿಳಿಯುತ್ತಿದ್ದಂತೆ ವಸುದೇವರ ಹೃದಯವು ಆನಂದದಿಂದ ತುಂಬಿಹೋಯಿತು. ತಕ್ಷಣವೇ ಅವರು ನಂದರ ಬಿಡಾರಕ್ಕೆ ಧಾವಿಸಿದರು.

### ಇಬ್ಬರು ಭಕ್ತರ ದಿವ್ಯ ಆಲಿಂಗನ

ನಂದಮಹಾರಾಜರನ್ನು ಕಂಡ ಕ್ಷಣದಲ್ಲಿ ವಸುದೇವರಿಗೆ ಉಂಟಾದ ಅನುಭವವನ್ನು ಭಾಗವತವು ಹೀಗೆ ವರ್ಣಿಸುತ್ತದೆ:

> **ಶ್ರೀಮದ್ಭಾಗವತ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 5, ಶ್ಲೋಕ 20**
> 
> *ತಂ ದೃಷ್ಟ್ವಾ ಸಹಸೋತ್ಥಾಯ ದೇಹಃ ಪ್ರಾಣಮ್ ಇವಾಗತಮ್ |*  
> *ಪ್ರೀತಃ ಪ್ರಿಯತಮಂ ದೋರ್ಭ್ಯಾಂ ಸಸ್ವಞ್ಜೇ ಪ್ರೇಮ-ವಿಹ್ವಲಃ ||*  
> 
> **ಭಾವಾರ್ಥ:** "ತಮ್ಮ ಪ್ರಿಯ ಮಿತ್ರ ನಂದಮಹಾರಾಜರನ್ನು ಕಂಡ ವಸುದೇವರು ನಿರ್ಜೀವ ದೇಹಕ್ಕೆ ಪ್ರಾಣ ಮರಳಿ ಬಂದಂತೆ ಎದ್ದುನಿಂತು, ಅಪಾರ ಪ್ರೇಮದಿಂದ ಕೈಗಳನ್ನು ಚಾಚಿ ಅವರನ್ನು ಗಟ್ಟಿಯಾಗಿ ಆಲಂಗಿಸಿಕೊಂಡರು."

ಕಂಸನ ಹಿಂಸೆಗಳ ನಂತರ ನಂದರನ್ನು ಭೇಟಿಯಾದ ವಸುದೇವರಿಗೆ ಇದು ಪುನರ್ಜನ್ಮದಂತಿತ್ತು.

ವಸುದೇವರು ನಂದರ ಕುಶಲತೆಯನ್ನು ವಿಚಾರಿಸಿದರು: "ಮಿತ್ರ ನಂದರೇ! ವೃದ್ಧಾಪ್ಯದಲ್ಲಿ ನಿಮಗೆ ಗಂಡು ಮಗು ಜನಿಸಿದ್ದು ಮಹಾಭಾಗ್ಯ! ರೋಹಿಣಿಯ ಮಗ ಬಲರಾಮನು ನಿಮ್ಮ ವಾತ್ಸಲ್ಯದಲ್ಲಿ ಸುಖವಾಗಿದ್ದಾನೆಯೇ? ನಿಮ್ಮ ಮಗುವೂ ಕ್ಷೇಮವಾಗಿದೆಯೇ? ಗೋಕುಲದ ಹಸುಗಳು ಮತ್ತು ಗೋಪಾಲಕರು ಚೆನ್ನಾಗಿದ್ದಾರೆಯೇ?"

### ನಂದರ ಸಾಂತ್ವನ

ನಂದರು ಕರುಣೆಯಿಂದ ಹೇಳಿದರು: "ವಸುದೇವನೇ! ನಿಮ್ಮ ಆರು ಮಕ್ಕಳನ್ನು ಕಂಸನು ಕೊಂದ ಘೋರ ದುರಂತವನ್ನು ನೆನೆದು ನಮಗೆ ಅತೀವ ದುಃಖವಿದೆ. ವಿಧಿಯಾಟವನ್ನು ಯಾರೂ ತಪ್ಪಿಸಲಾರರು, ಆದರೆ ಆತ್ಮಜ್ಞಾನಿಗಳು ಸುಖದುಃಖಗಳಲ್ಲಿ ಧೃತಿಗೆಡುವುದಿಲ್ಲ."

### ವಸುದೇವರ ಎಚ್ಚರಿಕೆ

ಕಂಸನ ರಾಕ್ಷಸ ಮಂತ್ರಿಗಳು ಶಿಶುಗಳನ್ನು ಕೊಲ್ಲಲು ಸಂಚು ರೂಪಿಸಿರುವ ರಹಸ್ಯವು ವಸುದೇವರಿಗೆ ತಿಳಿದಿತ್ತು. ಆದ್ದರಿಂದ ಕೃಷ್ಣನ ರಕ್ಷಣೆಗಾಗಿ ವಸುದೇವರು ತುರ್ತು ಎಚ್ಚರಿಕೆ ನೀಡಿದರು:

> **ಶ್ರೀಮದ್ಭಾಗವತ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 5, ಶ್ಲೋಕ 30**
> 
> *ತಾತಾನುಗಮ್ಯ ತಾವತ್ ತ್ವಂ ಗೋಕುಲಂ ರಕ್ಷ ಪುತ್ರಕ |*  
> *ಉತ್ಪಾತಾ ಬಹವಸ್ ತತ್ರ ದೃಶ್ಯಂತೇ ಹ್ಯ್ ಅಶುಭಾವಹಾಃ ||*  
> 
> **ಭಾವಾರ್ಥ:** "ಪ್ರೀತಿಯ ಮಿತ್ರ ನಂದರೇ! ರಾಜನಿಗೆ ಕಪ್ಪ ಸಲ್ಲಿಸಿದ್ದಾಯಿತಲ್ಲವೇ, ಇನ್ನು ಮಥುರೆಯಲ್ಲಿ ಒಂದು ಕ್ಷಣವೂ ತಡಮಾಡಬೇಡಿ! ತಕ್ಷಣವೇ ಗೋಕುಲಕ್ಕೆ ಮರಳಿ ನಿಮ್ಮ ಮಗುವನ್ನು ಮತ್ತು ಕುಟುಂಬವನ್ನು ರಕ್ಷಿಸಿ; ಅಲ್ಲಿ ಅನೇಕ ದುಶ್ಯಕುನಗಳು ಮತ್ತು ಆಪತ್ತುಗಳು ಕಾಣಿಸುತ್ತಿವೆ!"

ವಸುದೇವರ ಮಾತಿನ ಗಂಭೀರತೆಯನ್ನು ಅರಿತ ನಂದಮಹಾರಾಜರು ತಡಮಾಡದೆ ಬಂಡಿಗಳೊಂದಿಗೆ ಗೋಕುಲದ ಕಡೆಗೆ ತಕ್ಷಣವೇ ಪ್ರಯಾಣ ಬೆಳೆಸಿದರು.""",
                "questions": [
                    {
                        "question": "ನಂದೋತ್ಸವದ ನಂತರ ನಂದಮಹಾರಾಜರು ಮಥುರೆಗೆ ಏಕೆ ಹೋದರು?",
                        "options": [
                            {"text": "ಕಂಸನಿಗೆ ವಾರ್ಷಿಕ ಕಪ್ಪಕಾಣಿಕೆ ಸಲ್ಲಿಸಲು", "is_correct": True},
                            {"text": "ಕುದುರೆಗಳನ್ನು ಖರೀದಿಸಲು", "is_correct": False},
                            {"text": "ಯುದ್ಧ ಮಾಡಲು", "is_correct": False},
                            {"text": "ಪ್ರವಾಸಕ್ಕೆಂದು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಮಥುರೆಗೆ ಹೋಗುವಾಗ ಗೋಕುಲದ ರಕ್ಷಣೆಯನ್ನು ಯಾರಿಗೆ ಒಪ್ಪಿಸಿದರು?",
                        "options": [
                            {"text": "ಅನುಭವಿ ಹಿರಿಯ ಗೋಪಾಲಕರಿಗೆ", "is_correct": True},
                            {"text": "ಕಂಸನ ಸೈನಿಕರಿಗೆ", "is_correct": False},
                            {"text": "ಕಾವಲುಗಾರರಿಗೆ", "is_correct": False},
                            {"text": "ವರ್ತಕರಿಗೆ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ನಂದರನ್ನು ಕಂಡಾಗ ವಸುದೇವರಿಗೆ ಏನನ್ನಿಸಿತು?",
                        "options": [
                            {"text": "ನಿರ್ಜೀವ ದೇಹಕ್ಕೆ ಪ್ರಾಣ ಮರಳಿ ಬಂದಂತೆ", "is_correct": True},
                            {"text": "ನಿಧಿ ಸಿಕ್ಕಂತೆ", "is_correct": False},
                            {"text": "ಯುದ್ಧ ಗೆದ್ದಂತೆ", "is_correct": False},
                            {"text": "ಸಾಮಾನ್ಯವಾಗಿ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ವಸುದೇವರು ಯಾವ ಇಬ್ಬರು ಮಕ್ಕಳ ಬಗ್ಗೆ ವಿಚಾರಿಸಿದರು?",
                        "options": [
                            {"text": "ಬಲರಾಮ ಮತ್ತು ನವಜಾತ ಕೃಷ್ಣನ ಬಗ್ಗೆ", "is_correct": True},
                            {"text": "ಪಾಂಡವರ ಬಗ್ಗೆ", "is_correct": False},
                            {"text": "ಕೌರವರ ಬಗ್ಗೆ", "is_correct": False},
                            {"text": "ಅಭಿಮನ್ಯುವಿನ ಬಗ್ಗೆ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ನಂದರು ವಸುದೇವರಿಗೆ ಯಾವ ಸಾಂತ್ವನ ನೀಡಿದರು?",
                        "options": [
                            {"text": "ಆರು ಮಕ್ಕಳ ಹತ್ಯೆಗೆ ತೀವ್ರ ಸಂತಾಪ ವ್ಯಕ್ತಪಡಿಸಿದರು", "is_correct": True},
                            {"text": "ಹಣ ನೀಡಿದರು", "is_correct": False},
                            {"text": "ಓಡಿಹೋಗಲು ಹೇಳಿದರು", "is_correct": False},
                            {"text": "ದೂಷಿಸಿದರು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ನಂದರಿಗೆ ತಿಳಿಯದ ಯಾವ ಅಪಾಯವು ವಸುದೇವರಿಗೆ ತಿಳಿದಿತ್ತು?",
                        "options": [
                            {"text": "ಅಸುರರು ಹಸುಗೂಸುಗಳನ್ನು ಕೊಲ್ಲಲು ಸಂಚು ರೂಪಿಸಿದ್ದಾರೆ ಎಂಬುದು", "is_correct": True},
                            {"text": "ಬರಗಾಲ ಬರುತ್ತಿದೆ ಎಂದು", "is_correct": False},
                            {"text": "ಬೆಣ್ಣೆ ಕದಿಯುತ್ತಾರೆ ಎಂದು", "is_correct": False},
                            {"text": "ಹುಲಿ ಬಂದಿದೆ ಎಂದು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ವಸುದೇವರು ನಂದರಿಗೆ ನೀಡಿದ ಎಚ್ಚರಿಕೆಯೇನು?",
                        "options": [
                            {"text": "ಮಥುರೆಯಲ್ಲಿ ತಡಮಾಡದೆ ಗೋಕುಲಕ್ಕೆ ಮರಳಿ ಮಕ್ಕಳನ್ನು ರಕ್ಷಿಸಿ", "is_correct": True},
                            {"text": "ಒಂದು ತಿಂಗಳು ಮಥುರೆಯಲ್ಲೇ ಇರಿ", "is_correct": False},
                            {"text": "ಕೃಷ್ಣನನ್ನು ಮಥುರೆಗೆ ತನ್ನಿ", "is_correct": False},
                            {"text": "ಕಾಶಿ ಯಾತ್ರೆಗೆ ಹೋಗಿ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ದುಷ್ಟರಾಜನ ನಗರದಲ್ಲಿ ಕಪ್ಪ ಸಲ್ಲಿಸಿದ ನಂತರ ಏಕೆ ಇರಬಾರದು?",
                        "options": [
                            {"text": "ಕ್ರೂರ ರಾಜರು ಯಾವಾಗ ಬೇಕಾದರೂ ಆಪತ್ತು ತರಬಹುದು ಎಂದು", "is_correct": True},
                            {"text": "ವೆಚ್ಚ ಹೆಚ್ಚು ಎಂದು", "is_correct": False},
                            {"text": "ಎತ್ತುಗಳು ದಣಿಯುತ್ತವೆ ಎಂದು", "is_correct": False},
                            {"text": "ಕತ್ತಲೆಯಾಗುತ್ತದೆ ಎಂದು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಎಚ್ಚರಿಕೆ ಕೇಳಿದ ನಂದರು ಏನು ಮಾಡಿದರು?",
                        "options": [
                            {"text": "ತಕ್ಷಣವೇ ಬಂಡಿಗಳೊಂದಿಗೆ ಗೋಕುಲದ ಕಡೆಗೆ ಮರಳಿದರು", "is_correct": True},
                            {"text": "ನಿರ್ಲಕ್ಷಿಸಿದರು", "is_correct": False},
                            {"text": "ನಕ್ಕರು", "is_correct": False},
                            {"text": "ಯುದ್ಧಕ್ಕೆ ಹೋದರು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಭಾಗವತದ ಯಾವ ಅಧ್ಯಾಯವು ನಂದ-ವಸುದೇವರ ಮಿಲನವನ್ನು ವರ್ಣಿಸುತ್ತದೆ?",
                        "options": [
                            {"text": "ಅಧ್ಯಾಯ 5", "is_correct": True},
                            {"text": "ಅಧ್ಯಾಯ 2", "is_correct": False},
                            {"text": "ಅಧ್ಯಾಯ 7", "is_correct": False},
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

        self.stdout.write(self.style.SUCCESS(f"Successfully populated Story 14 (ID: {story.id}) across all 7 languages!"))
