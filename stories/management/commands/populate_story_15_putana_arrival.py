import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askharekrishna_backend.settings')
django.setup()

from django.core.management.base import BaseCommand
from stories.models import StoryMainTopic, Story, StoryTranslation, StoryQuestion, StoryQuestionOption

class Command(BaseCommand):
    help = "Populate Story 15: The Arrival of the Witch Putana in Gokula across 7 languages"

    def handle(self, *args, **options):
        topic = StoryMainTopic.objects.get(name="Krishna Pastimes")

        story_slug = "krishna-pastimes-the-arrival-of-the-witch-putana-in-gokula"
        image_path = "stories/images/putana_arrival_gokula.jpg"

        story, created = Story.objects.get_or_create(
            slug=story_slug,
            defaults={
                "topic": topic,
                "order": 14,
                "imagePath": image_path,
            }
        )
        if not created:
            story.topic = topic
            story.order = 14
            story.imagePath = image_path
            story.save()

        stories_data = {
            "en": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "The Arrival of the Witch Putana in Gokula",
                "content": """### King Kamsa Dispatches the Deadly Witch Putana

Following his demonic council’s advice, King Kamsa unleashed his fiercest agents across the kingdom of Surasena to hunt down and slaughter every newborn child. Among all his henchmen, the most feared and ruthless was a ghastly demoness named Putana. 

Putana possessed the mystic occult power known as *khecarī-siddhi*—the supernatural ability to fly freely through outer space and travel unseen at lightning speed. Her sinister specialty was the merciless slaughter of innocent infants:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 6, Verse 4**
> 
> *sā khecary ekadotpitya pūtanā loka-bāla-ghnī*  
> *purān janapadān grāmān babhrāma śiśu-ghātinī*  
> 
> **Translation:** "Once, the witch Putana, who had the mystic occult power to fly through the sky and whose occupation was killing babies in all worlds, flew through cities, districts, and villages, mercilessly murdering innocent infants."

Guided by dark fortune, Putana arrived in the vicinity of Gokula, where the Supreme Personality of Godhead had descended as the darling child of Nanda Maharaja and Mother Yashoda. Because Gokula was a place where the holy name of the Lord was constantly chanted and where pure devotees lived, ordinary demons could not even step foot there. But by the mystic will of Providence, Putana was allowed entry so that the Lord could inaugurate His childhood pastimes.

### The Enchanting Disguise as Goddess Lakshmi

Putana knew that if she entered Gokula in her natural, terrifying monstrous form, the cowherd warriors would instantly attack her. Utilizing her demonic mystic power of shapeshifting, she disguised herself as an extraordinarily beautiful, youthful maiden:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 6, Verses 7–9**
> 
> *tāṁ prekṣya tanvīṁ taruṇīṁ sulakṣaṇāṁ*  
> *raṅgad-valagnāṁ su-kuconnatiṁ striyam*  
> *su-vāsasaṁ kāñcana-kuṇḍalollasat-*  
> *kapola-cāmīkara-karṇa-veṣṭitām*  
> 
> **Translation:** "Seeing her slender waist, youthful elegance, auspicious features, high full breasts, exquisite silken garments, and glistening gold earrings hanging against her radiant cheeks, the cowherd women were utterly astonished. They beheld her walking gracefully into the home of Nanda Maharaja like the goddess of fortune, Lakshmi herself, bearing a lotus flower."

Putana’s disguise was completely breathtaking. Her hips were gracefully shaped, her waist was slender, her long dark tresses were woven with fragrant jasmine blossoms, and sweet celestial perfumes emanated from her body. She cast gentle, alluring glances that captivated everyone who saw her. In her hand she held a lotus flower, and she stepped so lightly that she seemed to glide upon the air.

As she entered the pasturing community of Gokula, the simple-hearted cowherds and gopis did not suspect the slightest danger. They stood in awe, believing that Mother Lakshmi, the goddess of fortune, had descended personally to bless Nanda Maharaja’s home!

### Unhindered Entry into Nanda Maharaja's Home

Gliding smoothly through the streets, Putana entered the grand courtyard of Nanda Maharaja. At that time, Nanda Maharaja had not yet returned from Mathura, where he had gone to pay his royal taxes. Inside the house, Mother Yashoda and Mother Rohini were attending to household duties while keeping loving watch over baby Krishna.

Putana crossed the threshold with a sweet, disarming smile and an air of immense motherly affection. Both Yashoda and Rohini were completely stunned by her dazzling celestial beauty. In traditional Vedic culture, a guest—especially an aristocratic lady bearing auspicious lotus flowers—is received with immediate warmth and respect. Thinking her to be a heavenly benefactress, neither Yashoda nor Rohini questioned her or barred her way.

Without a moment’s hesitation, Putana walked straight into the private inner chamber where baby Krishna lay peacefully resting on a bed.

### The Deadly Plot and the All-Knowing Lord

Baby Krishna, the Supreme Personality of Godhead, was lying upon soft silken swaddling clothes. He was glowing with the soft bluish hue of a fresh rain cloud, His tiny lotus feet and lotus hands radiating divine charm.

Putana approached the bed, her demonic heart boiling with murderous venom, even while her outer face beamed with false maternal affection. Smeared upon her breast was a deadly, virulent poison called *kālakūṭa*, an instant-killing poison capable of burning a human body to ash in moments. Her wicked plan was simple: offer her poisoned breast to the child under the guise of nursing, so that the infant would perish immediately upon the first drop.

The infant Lord was fully conscious of everything. He knew that she was a witch dispatched by Kamsa, and He knew the virulent poison concealed upon her breast. Yet, showing His supreme fearlessness and playful acceptance of her challenge, baby Krishna closed His lotus eyes as Putana bent down to lift Him onto her lap. The curtain was now drawn for one of the most astonishing pastimes of the Supreme Lord in Vraja!""",
                "questions": [
                    {
                        "question": "Which ruthless witch was dispatched by King Kamsa to slaughter newborn infants?",
                        "options": [
                            {"text": "Putana", "is_correct": True},
                            {"text": "Surpanakha", "is_correct": False},
                            {"text": "Tataka", "is_correct": False},
                            {"text": "Simhika", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What mystic occult siddhi did Putana possess that allowed her to travel in the sky?",
                        "options": [
                            {"text": "Khecari-siddhi (ability to fly through outer space)", "is_correct": True},
                            {"text": "Anima-siddhi (becoming smaller than an atom)", "is_correct": False},
                            {"text": "Prapti-siddhi (acquiring anything from anywhere)", "is_correct": False},
                            {"text": "Garima-siddhi (becoming infinitely heavy)", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What disguise did Putana assume when she entered Gokula?",
                        "options": [
                            {"text": "An exquisitely beautiful celestial maiden resembling Goddess Lakshmi", "is_correct": True},
                            {"text": "An old, fragile beggar woman", "is_correct": False},
                            {"text": "A warrior in heavy golden armor", "is_correct": False},
                            {"text": "A wandering sage with matted locks", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What did Putana carry in her hand to enhance her disguise as an auspicious goddess?",
                        "options": [
                            {"text": "A lotus flower", "is_correct": True},
                            {"text": "A golden sword", "is_correct": False},
                            {"text": "A conchshell", "is_correct": False},
                            {"text": "A silver bow", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Why did the cowherd women and men allow Putana to enter Gokula without stopping her?",
                        "options": [
                            {"text": "Her ravishing beauty and celestial grace made them believe she was a divine goddess", "is_correct": True},
                            {"text": "She threatened them with a fiery weapon", "is_correct": False},
                            {"text": "She produced a royal pass signed by Kamsa", "is_correct": False},
                            {"text": "They were all fast asleep", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Who was inside the house watching baby Krishna when Putana walked in?",
                        "options": [
                            {"text": "Mother Yashoda and Mother Rohini", "is_correct": True},
                            {"text": "Nanda Maharaja and Vasudeva", "is_correct": False},
                            {"text": "Sage Gargamuni and Sandipani Muni", "is_correct": False},
                            {"text": "King Kamsa and Chanura", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Where was Nanda Maharaja when Putana arrived in Gokula?",
                        "options": [
                            {"text": "In Mathura paying royal taxes to King Kamsa", "is_correct": True},
                            {"text": "Grazing cows in Vrindavana", "is_correct": False},
                            {"text": "Sleeping in the courtyard", "is_correct": False},
                            {"text": "Hunting in the forest", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What deadly substance had Putana smeared upon her breast to kill baby Krishna?",
                        "options": [
                            {"text": "Virulent kalakuta poison", "is_correct": True},
                            {"text": "Sleeping herbs", "is_correct": False},
                            {"text": "Hot burning oil", "is_correct": False},
                            {"text": "Bitter neem juice", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What did baby Krishna do when Putana approached and picked Him up?",
                        "options": [
                            {"text": "He closed His lotus eyes knowing her demonic intention", "is_correct": True},
                            {"text": "He began crying loudly in fear", "is_correct": False},
                            {"text": "He turned into a blazing fire", "is_correct": False},
                            {"text": "He jumped off the bed and ran away", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Which chapter of Srimad-Bhagavatam Canto 10 narrates the pastime of Putana?",
                        "options": [
                            {"text": "Chapter 6", "is_correct": True},
                            {"text": "Chapter 3", "is_correct": False},
                            {"text": "Chapter 1", "is_correct": False},
                            {"text": "Chapter 10", "is_correct": False}
                        ]
                    }
                ]
            },
            "ta": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "பூதனை எனும் அரக்கி கோகுலத்திற்குள் நுழைந்த லீலை",
                "content": """### கொடூரமான பூதனையை ஏவிய கம்சன்

கம்சனின் கொடிய மந்திராலோசனையைத் தொடர்ந்து, சூரசேன தேசம் முழுவதும் பிறக்கும் பச்சிளங்குழந்தைகளைக் கண்டறிந்து கொல்வதற்காக அவனுடைய கொடூரமான அசுரர்கள் நாலாபுறமும் ஏவப்பட்டனர். அந்த அசுரர்களிலேயே மிகவும் இரக்கமற்றவளும், மாயாஜாலங்கள் நிறைந்தவளுமான ஒரு கொடிய அரக்கி பூதனை ஆவாள்.

பூதனை ஆகாயத்தில் தடையின்றி பறந்து செல்லும் *கேசரீ சித்தி* என்னும் அபூர்வ ஆற்றலைக் கொண்டிருந்தாள். அவளுடைய முக்கிய வேலையே உலகெங்கிலும் உள்ள பச்சிளங்குழந்தைகளை ஈவுஇரக்கமின்றி கொன்று குவிப்பதேயாகும்:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 6, சுலோகம் 4**
> 
> *ஸா கேசர்யேகதோத்பித்ய பூதனா லோக-பால-க்னீ*  
> *புரான் ஜனபதான் க்ராமான் பப்ராம சிசு-காதினீ*  
> 
> **பொருள்:** "வானில் பறக்கும் கேசரீ சித்தியைக் கொண்டவளும், உலகெங்கும் பச்சிளங்குழந்தைகளைக் கொல்வதையே தன் தொழிலாகக் கொண்டவளுமான பூதனை என்னும் அரக்கி, நகரங்கள், கிராமங்கள், மேய்ச்சல் நிலங்கள் எங்கும் சுற்றித்திரிந்து அப்பாவி குழந்தைகளைக் கொன்று வந்தாள்."

விதியின் விசித்திரமான ஏற்பாட்டால், பூதனை பகவான் ஸ்ரீ கிருஷ்ணர் அவதரித்திருந்த கோகுலத்தின் எல்லைக்கு வந்து சேர்ந்தாள். பகவானின் திருநாமங்கள் இடைவிடாது முழங்கப்படும் தூய பக்தர்களின் புண்ணிய பூமியான கோகுலத்திற்குள் அசுரர்கள் நுழையவே முடியாது. ஆனால், பகவான் தன்னுடைய பால லீலைகளைத் தொடங்கி அசுர வதத்தை நிகழ்த்த திருவுள்ளம் கொண்டதால், பூதனை அங்கு நுழைய அனுமதிக்கப்பட்டாள்.

### லக்ஷ்மி தேவி போன்ற மோகன ரூபம் கொண்ட பூதனை

தன்னுடைய பயங்கரமான அரக்கி உருவத்தோடு கோகுலத்திற்குள் சென்றால் கோபர்கள் தன்னை உடனே கொன்றுவிடுவார்கள் என்பதை பூதனை நன்கு அறிவாள். எனவே, தன் மாயாஜால சக்தியினால் எவரும் மயங்கிப்போகும் பேரழகு வாய்ந்த ஒரு தேவலோக கன்னிகையாகத் தன் உருவத்தை மாற்றிக்கொண்டாள்:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 6, சுலோகங்கள் 7–9**
> 
> *தாம் ப்ரேக்ஷ்ய தன்வீம் தருணீம் ஸுலக்ஷணாம்*  
> *ரங்கத்-வலக்னாம் ஸு-குசோன்னதிம் ஸ்த்ரியம்*  
> *ஸு-வாஸஸம் காஞ்சன-குண்டலோல்லஸத்-*  
> *கபோல-சாமீகர-கர்ண-வேஷ்டிதாம்*  
> 
> **பொருள்:** "மெல்லிய இடை, இளமைத் துடிப்பு, மங்களகரமான அங்க லட்சணங்கள், விலைமதிப்பற்ற பட்டு ஆடைகள், பளபளக்கும் கன்னங்களில் அசைந்தாடும் தங்கக் குண்டலங்கள் ஆகியவற்றுடன் திகழ்ந்த அவளைக் கண்டு கோகுலப் பெண்கள் பிரமித்தனர். கையில் தாமரை மலரை ஏந்தியபடி நந்த மகாராஜாவின் மாளிகைக்குள் நுழையும் லக்ஷ்மி தேவியே நேரில் வந்துவிட்டாளோ என்று அனைவரும் எண்ணினர்."

பூதனையின் இந்த மாறுவேடம் காண்போரை மெய்சிலிர்க்க வைக்கும் வண்ணம் இருந்தது. அவளுடைய அழகிய கருங்கூந்தலில் மல்லிகைப் பூக்கள் சூடப்பட்டிருந்தன. அவளுடைய உடலிலிருந்து நறுமண வாசனை வீசியது. அவளுடைய கனிவான பார்வையும், புன்னகையும் அவளுக்குள் இருந்த நஞ்சை முற்றிலும் மறைத்தன. கையில் ஒரு தாமரை மலரை ஏந்தியபடி, நிலத்தில் பாதம் படாமல் மிதப்பது போல அவள் கோகுலத்திற்குள் நுழைந்தாள்.

கோகுலத்தின் அப்பாவிகளான ஆயர்களும், கோபியர்களும் அவளைக் கண்டு கிஞ்சித்தும் சந்தேகிக்கவில்லை. நந்த மகாராஜாவின் மாளிகையை ஆசீர்வதிக்க சாட்சாத் பாக்கியவதி லக்ஷ்மி தேவியே நேரில் எழுந்தருளிவிட்டாள் என்று அவர்கள் மனதார நம்பி பரவசமடைந்தனர்.

### நந்த மகாராஜாவின் இல்லத்திற்குள் தடையின்றி நுழைதல்

கோகுலத்தின் வீதிகளைக் கடந்து, பூதனை நந்த மகாராஜாவின் திருமாளிகையின் வாயிலை அடைந்தாள். அந்த நேரத்தில், நந்த மகாராஜர் கம்சனுக்கு வருடாந்திர வரி செலுத்துவதற்காக மதுராவிற்குச் சென்றிருந்தார். மாளிகையின் உள்ளே அன்னை யசோதையும், அன்னை ரோஹிணியும் குழந்தைப் பருவம் கொண்ட பகவான் கிருஷ்ணரை அன்போடு கவனித்துக் கொண்டிருந்தனர்.

பூதனை ஒரு தாய் போன்ற வாஞ்சையான புன்னகையுடன் மாளிகையின் வாயிற்படியைத் தாண்டினாள். அவளுடைய தெய்வீகப் பேரழகையும், மங்களகரமான தோற்றத்தையும் கண்ட அன்னை யசோதையும், ரோஹிணியும் திகைத்து நின்றனர். விருந்தினர்களைத் தெய்வமாகப் போற்றும் வைதீகப் பண்பாட்டின்படி, தாமரை மலருடன் வந்த அந்தப் பெண்ணை அவர்கள் அன்போடு வரவேற்றனர். தாய்மை நிறைந்த பாசத்தோடு வந்திருக்கும் ஒரு தேவமங்கை என்று கருதியதால், அவளை எவரும் தடுத்து நிறுத்தவில்லை.

பூதனை எவ்விதத் தடையுமின்றி, பால கிருஷ்ணர் படுத்திருந்த அந்தரங்க அறைக்குள் நேராக விரைந்து சென்றாள்.

### கொடிய சதியும் சர்வக்ஞரான பகவானின் பார்வையும்

அங்கே பால கிருஷ்ணர் ஒரு அழகிய மெத்தையில் பட்டுத் துணியில் பொதிந்து படுத்திருந்தார். கார்மேக வண்ணனான அந்தத் தெய்வக் குழந்தை, தன் தாமரை மலர் போன்ற சிறிய கரங்களையும் பாதங்களையும் அசைத்து தெய்வீகப் பேரொளியுடன் திகழ்ந்தார்.

பூதனையின் உள்ளத்தில் கொலைவெறி கொப்பளித்துக் கொண்டிருந்தது; ஆனால் அவளுடைய முகத்திலோ கள்ளங்கபடமற்ற பாசப் புன்னகை தவழ்ந்தது. அவளுடைய மார்பில் *காலகூடம்* எனப்படும் கொடிய ஆலகால விஷம் பூசப்பட்டிருந்தது. அந்த விஷம் தொட்ட மாத்திரத்திலேயே எந்த உயிரையும் நொடிப்பொழுதில் சாம்பலாக்கிவிடும் தன்மை கொண்டது. குழந்தைக்குத் தாய்ப்பால் தருவது போல நடித்து, அந்த நஞ்சை ஊட்டிக் கொன்றுவிட வேண்டும் என்பதே அவளுடைய கொடிய திட்டம்.

ஆனால், அனைத்தையும் அறியும் முழுமுதற் கடவுளான பால கிருஷ்ணர் அவளுடைய வஞ்சக நோக்கத்தை முழுமையாக உணர்ந்தார். அவள் கம்சனால் அனுப்பப்பட்ட கொடிய அரக்கி என்பதையும், அவளுடைய மார்பில் ஆலகால நஞ்சு பூசப்பட்டிருப்பதையும் பகவான் அறிந்தார். இருப்பினும், அவளுடைய சவாலை ஏற்று அவளுக்கு முக்தி தரும் திருவிளையாடலை நிகழ்த்த திருவுள்ளம் கொண்ட பகவான், அவள் தன்னைத் தூக்குவதற்காகக் குனிந்தபோது, தன் தாமரை மலர்க் கண்களை மெல்ல மூடிக்கொண்டார்!""",
                "questions": [
                    {
                        "question": "சூரசேன தேசத்தில் பிறந்த பச்சிளங்குழந்தைகளைக் கொல்ல கம்சனால் அனுப்பப்பட்ட கொடிய அரக்கி யார்?",
                        "options": [
                            {"text": "பூதனை", "is_correct": True},
                            {"text": "சூர்ப்பணகை", "is_correct": False},
                            {"text": "தாடகை", "is_correct": False},
                            {"text": "சிம்மிகை", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பூதனைக்கு வானில் பறக்க உதவிய அபூர்வமான சித்திக் கலை எது?",
                        "options": [
                            {"text": "கேசரீ சித்தி", "is_correct": True},
                            {"text": "அணிமா சித்தி", "is_correct": False},
                            {"text": "ப்ராப்தி சித்தி", "is_correct": False},
                            {"text": "கரிமா சித்தி", "is_correct": False}
                        ]
                    },
                    {
                        "question": "கோகுலத்திற்குள் நுழையும் போது பூதனை எத்தகைய மாறுவேடத்தை ஏற்றாள்?",
                        "options": [
                            {"text": "லக்ஷ்மி தேவி போன்ற பேரழகு வாய்ந்த தேவலோக மங்கை", "is_correct": True},
                            {"text": "ஒரு வயதான ஏழை யாசகி", "is_correct": False},
                            {"text": "தங்கக் கவசம் அணிந்த ஒரு போர் வீரன்", "is_correct": False},
                            {"text": "சடைமுடி தரித்த ஒரு துறவி", "is_correct": False}
                        ]
                    },
                    {
                        "question": "தன் வேடத்தை மங்களகரமாகக் காட்ட பூதனை தன் கையில் எதை ஏந்தி வந்தாள்?",
                        "options": [
                            {"text": "தாமரை மலர்", "is_correct": True},
                            {"text": "தங்க வாள்", "is_correct": False},
                            {"text": "சங்கு", "is_correct": False},
                            {"text": "வெள்ளி வில்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "கோகுலத்து மக்கள் பூதனையைத் தடுக்காமல் விட்டதன் காரணம் என்ன?",
                        "options": [
                            {"text": "அவளுடைய தெய்வீகப் பேரழகைக் கண்டு அவளை லக்ஷ்மி தேவி என எண்ணினர்", "is_correct": True},
                            {"text": "அவள் கொடிய ஆயுதங்களைக் காட்டி மிரட்டினாள்", "is_correct": False},
                            {"text": "அவள் கம்சனின் அரச ஆணைக் கடிதத்தைக் காட்டினாள்", "is_correct": False},
                            {"text": "மக்கள் அனைவரும் ஆழ்ந்த உறக்கத்தில் இருந்தனர்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பூதனை மாளிகைக்குள் நுழைந்த போது பால கிருஷ்ணரைக் கவனித்துக் கொண்டிருந்தவர்கள் யார்?",
                        "options": [
                            {"text": "அன்னை யசோதையும் அன்னை ரோஹிணியும்", "is_correct": True},
                            {"text": "நந்த மகாராஜரும் வசுதேவரும்", "is_correct": False},
                            {"text": "கர்க முனிவரும் சாந்தீபனி முனிவரும்", "is_correct": False},
                            {"text": "கம்சனும் சாணூரனும்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பூதனை கோகுலத்திற்கு வந்த சமயம் நந்த மகாராஜர் எங்கு சென்றிருந்தார்?",
                        "options": [
                            {"text": "கம்சனுக்கு அரச வரி செலுத்துவதற்காக மதுராவிற்கு", "is_correct": True},
                            {"text": "பிருந்தாவனத்தில் பசுக்களை மேய்க்க", "is_correct": False},
                            {"text": "முற்றத்தில் ஓய்வெடுக்க", "is_correct": False},
                            {"text": "காட்டில் வேட்டையாட", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பால கிருஷ்ணரைக் கொல்வதற்காக பூதனை தன் மார்பில் தடவியிருந்த கொடிய பொருள் எது?",
                        "options": [
                            {"text": "காலகூட விஷம்", "is_correct": True},
                            {"text": "மயக்க மருந்து", "is_correct": False},
                            {"text": "கொதிக்கும் நெய்", "is_correct": False},
                            {"text": "கசப்பான வேப்பஞ்சாறு", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பூதனை பால கிருஷ்ணரைத் தூக்க முற்பட்ட போது பகவான் என்ன செய்தார்?",
                        "options": [
                            {"text": "அவளது வஞ்சக நோக்கத்தை அறிந்து தம் கண்களை மெல்ல மூடிக்கொண்டார்", "is_correct": True},
                            {"text": "பயந்து போய் அலறி அழுதார்", "is_correct": False},
                            {"text": "நெருப்புப் பிழம்பாக மாறினார்", "is_correct": False},
                            {"text": "படுக்கையை விட்டு ஓடினார்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பூதனையின் லீலையை விவரிக்கும் ஸ்ரீமத் பாகவதம் பத்தாம் ஸ்கந்தத்தின் அத்தியாயம் எது?",
                        "options": [
                            {"text": "அத்தியாயம் 6", "is_correct": True},
                            {"text": "அத்தியாயம் 3", "is_correct": False},
                            {"text": "அத்தியாயம் 1", "is_correct": False},
                            {"text": "அத்தியாயம் 10", "is_correct": False}
                        ]
                    }
                ]
            },
            "hi": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "पूतना राक्षसी का गोकुल में आगमन",
                "content": """### कंस द्वारा पूतना राक्षसी को भेजा जाना

अपनी आसुरी सभा के परामर्श के अनुसार, राजा कंस ने शूरसेन राज्य में नवजात शिशुओं को ढूंढकर उनकी हत्या करने के लिए अपने सबसे क्रूर असुरों को भेजा। इन सभी में सबसे भयंकर और निर्दयी पूतना नाम की राक्षसी थी।

पूतना के पास *खेचरी सिद्धि* नाम की अलौकिक शक्ति थी, जिसके बल पर वह आकाश में उड़ सकती थी और पलक झपकते ही कहीं भी पहुंच सकती थी। उसका मुख्य कार्य मासूम नन्हे शिशुओं की निर्मम हत्या करना था:

> **श्रीमद्-भागवतम, स्कंध 10, अध्याय 6, श्लोक 4**
> 
> *सा खेचर्येकदोत्पत्य पूतना लोकबालघातिनी ।*  
> *पुरान् जनपदान् ग्रामान् बभ्राम शिशून् घ्नती ॥*  
> 
> **भावार्थ:** "एक बार पूतना नाम की राक्षसी, जो आकाश में उड़ने की शक्ति रखती थी और जिसका काम ही संसार के छोटे बालकों की हत्या करना था, नगरों, जनपदों और गांवों में घूम-घूमकर अबोध शिशुओं का संहार करने लगी।"

भाग्यवश, पूतना गोकुल की सीमा पर आ पहुंची, जहां भगवान श्रीकृष्ण नंद महाराज और माता यशोदा के आंगन में बाल रूप में विराजमान थे। गोकुल एक ऐसा परम पवित्र धाम था जहां भगवान के नाम का निरंतर कीर्तन होता था और शुद्ध भक्त वास करते थे, इसलिए वहां कोई भी असुर साधारण रूप से प्रवेश नहीं कर सकता था। परंतु भगवान अपनी बाल-लीलाएं प्रकट करना चाहते थे और पूतना को परम गति देना चाहते थे, इसलिए उसने गोकुल में प्रवेश पाया।

### साक्षात लक्ष्मी जैसा रूप धारण करना

पूतना जानती थी कि यदि वह अपने भयानक राक्षसी रूप में गोकुल जाएगी, तो ग्वाले उसे तुरंत मार गिराएंगे। इसलिए उसने अपनी मायावी शक्ति से एक अत्यंत सुंदरी, नवयुवती का रूप धारण किया:

> **श्रीमद्-भागवतम, स्कंध 10, अध्याय 6, श्लोक 7–9**
> 
> *तां प्रेक्ष्य तन्वीं तरुणीं सुलक्षणಾಂ*  
> *रङ्गद्वलग्नां सुकुचोन्नतिं स्त्रियम् ।*  
> *सुवाससं काञ्चनकुण्डलोल्लसत्-*  
> *कपोलचामीकरकर्णवेष्टितम् ॥*  
> 
> **भावार्थ:** "उसकी पतली कमर, नवयौवन, सुंदर केश, कानों में झूलते स्वर्ण कुंडल और सुंदर रेशमी वस्त्रों को देखकर गोपियां चकित रह गईं। उसके हाथ में कमल का पुष्प था और वह इतनी मनमोहक लग रही थी मानो साक्षात लक्ष्मी जी नंदभवन में पधारी हों।"

पूतना का वेष अत्यंत मनमोहक था। उसने अपने लंबे काले केशों में सुगंधित चमेली के फूल गूंथ रखे थे और उसके शरीर से दिव्य सुगंध आ रही थी। हाथ में कमल पुष्प लिए वह इतनी मंद गति से चल रही थी मानो हवा में तैर रही हो।

गोकुल के सरल हृदय गोप और गोपियों को तनिक भी संदेह नहीं हुआ। वे सोचने लगे कि साक्षात भाग्य की देवी लक्ष्मी जी ही बालक को आशीर्वाद देने पधारी हैं!

### नंद भवन में निर्बाध प्रवेश

पूतना सीधे नंद महाराज के राजभवन के आंगन में प्रविष्ट हुई। उस समय नंद महाराज कंस को वार्षिक कर चुकाने के लिए मथुरा गए हुए थे। भीतर माता यशोदा और माता रोहिणी बालकृष्ण की देखरेख कर रही थीं।

पूतना ने अत्यंत वात्सल्यमयी मुस्कान के साथ भवन की देहरी लांघी। उसके अलौकिक सौंदर्य और वात्सल्य भाव को देखकर यशोदा और रोहिणी दोनों मुग्ध हो गईं। वैदिक संस्कृति में द्वार पर आए अतिथि, विशेषकर हाथ में कमल लिए किसी कुलीन स्त्री का सत्कार करना धर्म माना जाता है। इसलिए किसी ने भी उसे अंदर जाने से नहीं रोका।

पूतना बिना किसी झिझक के सीधे उस कक्ष में पहुंच गई जहां भगवान श्रीकृष्ण शय्या पर विश्राम कर रहे थे।

### कालकूट विष और अंतर्यामी भगवान

बिछौने पर लेटे हुए बालकृष्ण मेघश्याम वर्ण के थे और उनके नन्हे चरणकमल अत्यंत मनोहारी लग रहे थे। 

पूतना के हृदय में भयंकर हत्यारी भावना भरी थी, किंतु चेहरे पर उसने वात्सल्य का ढोंग रच रखा था। उसने अपने स्तनों पर *कालकूट* नामक अत्यंत भयंकर हलाहल विष लगा रखा था, जो किसी भी प्राणी को तुरंत भस्म कर सकता था। उसका दुष्ट विचार था कि बालक को दूध पिलाने के बहाने वह विष दे देगी और बालक तुरंत मर जाएगा।

किंतु सर्वज्ञ भगवान श्रीकृष्ण उसके छल और मन के भाव को भली-भांति जानते थे। वे जानते थे कि यह कंस द्वारा भेजी गई बालघातिनी राक्षसी है। फिर भी पूतना को अपनी माता के समान गति प्रदान करने के उद्देश्य से, जैसे ही पूतना ने उन्हें गोद में उठाने के लिए हाथ बढ़ाया, नन्हे भगवान ने अपने दोनों नेत्र बंद कर लिए!""",
                "questions": [
                    {
                        "question": "कंस ने शिशुओं की हत्या करने के लिए किस राक्षसी को भेजा था?",
                        "options": [
                            {"text": "पूतना", "is_correct": True},
                            {"text": "शूर्पणखा", "is_correct": False},
                            {"text": "ताड़का", "is_correct": False},
                            {"text": "सिंहिका", "is_correct": False}
                        ]
                    },
                    {
                        "question": "पूतना के पास आकाश में उड़ने की कौन सी अलौकिक सिद्धि थी?",
                        "options": [
                            {"text": "खेचरी सिद्धि", "is_correct": True},
                            {"text": "अणिमा सिद्धि", "is_correct": False},
                            {"text": "प्राप्ति सिद्धि", "is_correct": False},
                            {"text": "गरिमा सिद्धि", "is_correct": False}
                        ]
                    },
                    {
                        "question": "गोकुल में प्रवेश करते समय पूतना ने किसका रूप धारण किया था?",
                        "options": [
                            {"text": "साक्षात लक्ष्मी जी के समान अत्यंत रूपवती सुंदरी का", "is_correct": True},
                            {"text": "एक वृद्ध भिखारिन का", "is_correct": False},
                            {"text": "एक शस्त्रधारी सैनिक का", "is_correct": False},
                            {"text": "एक तपस्वी मुनि का", "is_correct": False}
                        ]
                    },
                    {
                        "question": "अपने रूप को और अधिक मंगलकारी दिखाने के लिए पूतना के हाथ में क्या था?",
                        "options": [
                            {"text": "कमल का पुष्प", "is_correct": True},
                            {"text": "स्वर्ण तलवार", "is_correct": False},
                            {"text": "शंख", "is_correct": False},
                            {"text": "धनुष", "is_correct": False}
                        ]
                    },
                    {
                        "question": "गोपियों ने पूतना को घर में आने से क्यों नहीं रोका?",
                        "options": [
                            {"text": "उसके रूप और वस्त्रों को देखकर उन्होंने उसे साक्षात लक्ष्मी समझा", "is_correct": True},
                            {"text": "उसने अस्त्र दिखाकर भयभीत किया था", "is_correct": False},
                            {"text": "उसने कंस का आदेश पत्र दिखाया था", "is_correct": False},
                            {"text": "सभी गहरी नींद में सो रहे थे", "is_correct": False}
                        ]
                    },
                    {
                        "question": "पूतना जब भवन में आई, तब वहां कौन उपस्थित था?",
                        "options": [
                            {"text": "माता यशोदा और माता रोहिणी", "is_correct": True},
                            {"text": "नंद महाराज और वसुदेव", "is_correct": False},
                            {"text": "गर्ग मुनि और सांदीपनि मुनि", "is_correct": False},
                            {"text": "कंस और चाणूर", "is_correct": False}
                        ]
                    },
                    {
                        "question": "पूतना के आने के समय नंद महाराज कहां गए हुए थे?",
                        "options": [
                            {"text": "मथुरा में राजा कंस को कर देने", "is_correct": True},
                            {"text": "वृंदावन में गायें चराने", "is_correct": False},
                            {"text": "आंगन में विश्राम करने", "is_correct": False},
                            {"text": "जंगल में आखेट करने", "is_correct": False}
                        ]
                    },
                    {
                        "question": "बालकृष्ण को मारने के लिए पूतना ने अपने स्तनों पर क्या लगा रखा था?",
                        "options": [
                            {"text": "भयंकर कालकूट विष", "is_correct": True},
                            {"text": "नींद की औषधि", "is_correct": False},
                            {"text": "गर्म तेल", "is_correct": False},
                            {"text": "कड़वा नीम का रस", "is_correct": False}
                        ]
                    },
                    {
                        "question": "पूतना जब बालक को उठाने लगी, तब भगवान श्रीकृष्ण ने क्या किया?",
                        "options": [
                            {"text": "उसके कपट को जानकर अपने दोनों नेत्र बंद कर लिए", "is_correct": True},
                            {"text": "भयभीत होकर रोने लगे", "is_correct": False},
                            {"text": "अग्नि का रूप धारण कर लिया", "is_correct": False},
                            {"text": "शय्या से उठकर भाग गए", "is_correct": False}
                        ]
                    },
                    {
                        "question": "पूतना के उद्धार की यह कथा श्रीमद्-भागवतम के किस अध्याय में आती है?",
                        "options": [
                            {"text": "अध्याय 6", "is_correct": True},
                            {"text": "अध्याय 3", "is_correct": False},
                            {"text": "अध्याय 1", "is_correct": False},
                            {"text": "अध्याय 10", "is_correct": False}
                        ]
                    }
                ]
            },
            "bn": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "পূতনা রাক্ষসীর গোকুলে আগমন",
                "content": """### কংস কর্তৃক পূতনা রাক্ষসীকে প্রেরণ

পাপী কংস তার মন্ত্রীদের কুচক্রের পর শূরসেন রাজ্যের সমস্ত সদ্যোজাত শিশুকে হত্যা করার জন্য তার অনুচরদের নির্দেশ দিল। কংসের এই সকল অনুচরদের মধ্যে সবচেয়ে নির্দয় ও কুখ্যাত ছিল পূতনা নামক এক রাক্ষসী।

পূতনার একটি অলৌকিক মায়াবী শক্তি ছিল, যাকে বলা হয় *খেচরী সিদ্ধি*—যার সাহায্যে সে আকাশে বিচরণ করতে পারত। তার প্রধান কাজই ছিল অসহায় শিশুদের নিষ্ঠুরভাবে হত্যা করা:

> **শ্রীমদ্ভাগবতম, স্কন্ধ ১০, অধ্যায় ৬, শ্লোক ৪**
> 
> *সা খেচর্য্যেকদোৎপত্য পূতনা লোকবালঘাতিনী ।*  
> *পুরান্ জনপদান্ গ্রামান্ বভ্ৰাম শিশূন্ ঘ্নতী ॥*  
> 
> **অনুবাদ:** "একদা আকাশচারিণী খেচরী পূতনা, যার কর্মই ছিল জগৎসংসারের শিশুদের হত্যা করা, সে নগর, জনপদ ও গ্রামসমূহে বিচরণ করে অবোধ শিশুদের সংহার করতে লাগল।"

দৈবক্রমে সেই পূতনা গোকুলে উপস্থিত হলো, যেখানে পূর্ণব্রহ্ম ভগবান শ্রীকৃষ্ণ নন্দ মহারাজ ও মা যশোদার ঘরে পরম সুন্দর শিশু রূপে আবির্ভূত হয়েছিলেন। গোকুল এমন এক পবিত্র স্থান যেখানে সদাসর্বদা হরিনাম কীর্তন হতো, সেখানে কোনো সাধারণ অসুর পদার্পণ করতে পারত না। কিন্তু ভগবান তাঁর বাল্যলীলা প্রদর্শন ও পূতনাকে উদ্ধার করার জন্য তাকে সেখানে প্রবেশের সুযোগ দিলেন।

### সাক্ষাৎ লক্ষ্মীদেবীর মতো মনোহর রূপ ধারণ

পূতনা জানত যে যদি সে তার আসল কুৎসিত রাক্ষসী রূপ নিয়ে গোকুলে প্রবেশ করে, তবে ব্রজবাসীরা তাকে তখনই প্রতিহত করবে। তাই সে তার মায়াবী ক্ষমতার দ্বারা এক অপ্সরার ন্যায় পরমাসুন্দরী তরুণী স্ত্রীর রূপ ধারণ করল:

> **শ্রীমদ্ভাগবতম, স্কন্ধ ১০, অধ্যায় ৬, শ্লোক ৭–৯**
> 
> *তাং প্রেক্ষ্য তন্বীং তরুণীং সুলক্ষণাং*  
> *রঙ্গদ্বলগ্নাং সুকুচোন্নতিং স্ত্রিয়ম্ ।*  
> *সুূবাসসং কাঞ্চনকুণ্ডলোল্লসৎ-*  
> *কপোলচামীকরকর্ণবেষ্টিতাম্ ॥*  
> 
> **অনুবাদ:** "তার কৃশ কটিদেশ, নবযৌবন, অলঙ্কৃত কেশবিন্যাস, উজ্জ্বল কর্ণকুণ্ডল এবং মনোহর পট্টবস্ত্র দেখে ব্রজরমণীরা বিস্ময়ে অভিভূত হলেন। তার হাতে একটি পদ্মফুল শোভা পাচ্ছিল এবং তাকে দেখে মনে হচ্ছিল যেন সাক্ষাৎ লক্ষ্মীদেবীই নন্দভবনে আগমন করেছেন।"

পূতনার সেই রূপ ছিল অপরূপা। তার সুদীর্ঘ কেশকলাপে প্রস্ফুটিত জুঁইফুল সুশোভিত ছিল এবং তার শরীর থেকে দিব্য সুবাস বের হচ্ছিল। সে এমন রাজকীয় ভঙ্গিতে পদচারণা করছিল যেন সে সাক্ষাৎ বৈকুণ্ঠের অধিষ্ঠাত্রী দেবী।

গোকুলের সরল ব্রজবাসীরা তার বাহ্যিক রূপ দেখে মোটেও সন্দেহ করলেন না। তাঁরা মনে করলেন, নবজাতক শিশুকে আশীর্বাদ করার জন্যই স্বয়ং ভাগ্যদেবী লক্ষ্মী মর্তে নেমে এসেছেন!

### নন্দভবনে প্রবেশ

পূতনা অবলীলায় নন্দ মহারাজের বিশাল ভবনে প্রবেশ করল। সেই সময় নন্দ মহারাজ বার্ষিক কর পরিশোধ করতে মথুরায় গিয়েছিলেন। ঘরের মধ্যে মা যশোদা ও মা রোহিণী পরম স্নেহে শিশু শ্রীকৃষ্ণের দেখাশোনা করছিলেন।

পূতনা অত্যন্ত মধুর ও মাতৃসুলভ হাসি নিয়ে গৃহের প্রবেশদ্বারে পা রাখল। তার অদ্ভুত সৌন্দর্য ও স্নিগ্ধ ভাব দেখে মা যশোদা ও রোহিণী স্তব্ধ হয়ে দাঁড়িয়ে রইলেন। সনাতন বৈদিক শিষ্টাচার অনুসারে কোনো সম্মানিতা অতিথি বা পদ্মহস্তা নারীকে গৃহে আসতে দেখলে কেউ বাধা দেয় না। তাই তাঁরা তাকে বাধা দিলেন না।

পূতনা কালবিলম্ব না করে সরাসরি সেই প্রকোষ্ঠে চলে গেল যেখানে শয্যায় পরমেশ্বর ভগবান শ্রীকৃষ্ণ শায়িত ছিলেন।

### বিষাক্ত স্তনদুগ্ধ ও সর্বজ্ঞ ভগবানের দৃষ্টি

মেঘশ্যাম বর্ণের সেই দিব্য শিশু কমলনয়ন মেলে শয্যায় শয়ান ছিলেন। তাঁর শ্রীঅঙ্গ থেকে এক জ্যোতি বিচ্ছুরিত হচ্ছিল।

পূতনার হৃদয়ে ছিল তীব্র নরহত্যার বাসনা, কিন্তু মুখে ছিল কপট বাৎসল্য। সে তার স্তনে *কালকূট* নামক তীব্র প্রাণঘাতী বিষ লেপন করে এনেছিল, যার এক ফোঁটা স্পর্শেই মানুষ তৎক্ষণাৎ ভস্মীভূত হয়ে যায়। তার উদ্দেশ্য ছিল স্তনদুগ্ধ পানের ছলে শিশুকে সেই কালকূট বিষ পান করিয়ে হত্যা করা।

কিন্তু অন্তর্যামী ভগবান শ্রীকৃষ্ণ তার মনের সব কুৎসিত উদ্দেশ্য জানতেন। তিনি জানতেন যে এই নারী কংসের পাঠানো রাক্ষসী। তথাপি পূতনাকে নিজের ধাত্রী ও মায়ের সমান গতি প্রদান করার উদ্দেশ্যে, পূতনা যখন তাঁকে কোলে তুলতে হাত বাড়াল, তখন পরমেশ্বর ভগবান শ্রীকৃষ্ণ তাঁর দুটি কমল আঁখি মুদ্রিত করলেন!""",
                "questions": [
                    {
                        "question": "শিশুদের হত্যা করার জন্য কংস কোন রাক্ষসীকে পাঠিয়েছিল?",
                        "options": [
                            {"text": "পূতনা", "is_correct": True},
                            {"text": "শূর্পণখা", "is_correct": False},
                            {"text": "তাড়কা", "is_correct": False},
                            {"text": "সিংহিকা", "is_correct": False}
                        ]
                    },
                    {
                        "question": "পূতনার আকাশে ওড়ার অলৌকিক সিদ্ধির নাম কী ছিল?",
                        "options": [
                            {"text": "খেচরী সিদ্ধি", "is_correct": True},
                            {"text": "অণিমা সিদ্ধি", "is_correct": False},
                            {"text": "প্রাপ্তি সিদ্ধি", "is_correct": False},
                            {"text": "গরিমা সিদ্ধি", "is_correct": False}
                        ]
                    },
                    {
                        "question": "গোকুলে প্রবেশের সময় পূতনা কার রূপ ধারণ করেছিল?",
                        "options": [
                            {"text": "সাক্ষাৎ লক্ষ্মীদেবীর মতো পরমাসুন্দরী রমণীর রূপ", "is_correct": True},
                            {"text": "এক বৃদ্ধা ভিক্ষুকের রূপ", "is_correct": False},
                            {"text": "এক বর্মধারী সৈন্যের রূপ", "is_correct": False},
                            {"text": "এক তপস্বী মুনির রূপ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "নিজের রূপকে আরও শুভ দেখাতে পূতনার হাতে কী ছিল?",
                        "options": [
                            {"text": "একটি পদ্মফুল", "is_correct": True},
                            {"text": "একটি তলোয়ার", "is_correct": False},
                            {"text": "একটি শঙ্খ", "is_correct": False},
                            {"text": "একটি ধনুক", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ব্রজবাসীরা পূতনাকে গোকুলে প্রবেশে বাধা দেননি কেন?",
                        "options": [
                            {"text": "তার দিব্য সৌন্দর্য দেখে তাকে লক্ষ্মীদেবী ভেবেছিলেন", "is_correct": True},
                            {"text": "সে অস্ত্র দেখিয়ে ভয় দেখিয়েছিল", "is_correct": False},
                            {"text": "সে কংসের রাজকীয় ফরমান দেখিয়েছিল", "is_correct": False},
                            {"text": "সবাই ঘুমিয়ে পড়েছিলেন", "is_correct": False}
                        ]
                    },
                    {
                        "question": "পূতনা যখন ঘরে ঢুকল, তখন শিশু শ্রীকৃষ্ণের পাশে কারা ছিলেন?",
                        "options": [
                            {"text": "মা যশোদা ও মা রোহিণী", "is_correct": True},
                            {"text": "নন্দ মহারাজ ও বসুদেব", "is_correct": False},
                            {"text": "গর্গমুনি ও সান্দীপনি মুনি", "is_correct": False},
                            {"text": "কংস ও চাণূর", "is_correct": False}
                        ]
                    },
                    {
                        "question": "পূতনা আসার সময় নন্দ মহারাজ কোথায় গিয়েছিলেন?",
                        "options": [
                            {"text": "মথুরায় কংসের রাজকর দিতে", "is_correct": True},
                            {"text": "বৃন্দাবনে ধেনু চরাতে", "is_correct": False},
                            {"text": "উঠোনে বিশ্রাম করতে", "is_correct": False},
                            {"text": "বনে শিকার করতে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "শিশু শ্রীকৃষ্ণকে মারার জন্য পূতনা তার স্তনে কী মেখে এনেছিল?",
                        "options": [
                            {"text": "ভয়ঙ্কর কালকূট বিষ", "is_correct": True},
                            {"text": "ঘুমের ওষুধ", "is_correct": False},
                            {"text": "উত্তপ্ত ঘি", "is_correct": False},
                            {"text": "তেতো নিমের রস", "is_correct": False}
                        ]
                    },
                    {
                        "question": "পূতনা যখন কোলে তুলতে গেল, তখন ভগবান শ্রীকৃষ্ণ কী করলেন?",
                        "options": [
                            {"text": "তার অসৎ উদ্দেশ্য জেনে নয়ন দুটি বন্ধ করে নিলেন", "is_correct": True},
                            {"text": "ভয়ে চিৎকার করে কাঁদলেন", "is_correct": False},
                            {"text": "অগ্নিমূর্তি ধারণ করলেন", "is_correct": False},
                            {"text": "শয্যা ছেড়ে পালিয়ে গেলেন", "is_correct": False}
                        ]
                    },
                    {
                        "question": "পূতনার এই লীলা শ্রীমদ্ভাগবতের দশম স্কন্ধের কোন অধ্যায়ে বর্ণিত হয়েছে?",
                        "options": [
                            {"text": "অধ্যায় ৬", "is_correct": True},
                            {"text": "অধ্যায় ৩", "is_correct": False},
                            {"text": "অধ্যায় ১", "is_correct": False},
                            {"text": "অধ্যায় ১০", "is_correct": False}
                        ]
                    }
                ]
            },
            "te": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "పూతన రాక్షసి గోకులంలో ప్రవేశించిన దివ్య లీల",
                "content": """### కంసుడు పూతన రాక్షసిని పంపడం

దుష్ట కంసుడు తన మంత్రుల కుటిల సలహాను అనుసరించి, శూరసేన రాజ్యంలోని పసిపిల్లలందరినీ వెతికి చంపడానికి తన అనుచరులను ఆదేశించాడు. ఆ రాక్షసులలో అత్యంత క్రూరురాలైన ఒక మాయావిని పూతన.

పూతనకు ఆకాశంలో స్వేచ్ఛగా ఎగరగల *ఖేచరీ సిద్ధి* అనే అలౌకిక విద్య ఉంది. ప్రపంచంలోని పసిబిడ్డలను దయలేకుండా సంహరించడమే ఆమె నిత్యకృత్యం:

> **శ్రీమద్ భాగవతం, స్కంధం 10, అధ్యాయం 6, శ్లోకం 4**
> 
> *సా ఖేచర్యేకదోత్పత్య పూతనా లోకబాలఘాతినీ ।*  
> *పురాన్ జనపదాన్ గ్రామాన్ బభ్రామ శిశూన్ ఘ్నతీ ॥*  
> 
> **తాత్పర్యం:** "ఆకాశంలో ఎగిరే ఖేచరీ విద్యను కలిగి, లోకంలోని పసిపిల్లలను చంపడమే వృత్తిగా చేసుకున్న పూతన అనే రాక్షసి, నగరాలు, గ్రామాలు మరియు పల్లెలలో తిరుగుతూ అమాయక శిశువులను నిర్దాక్షిణ్యంగా చంపసాగింది."

విధివశాత్తు పూతన గోకులానికి చేరుకుంది. అక్కడ సాక్షాత్ భగవాన్ శ్రీకృష్ణుడు నందమహారాజు, యశోదామాతల ముద్దుల బిడ్డగా అవతరించి ఉన్నాడు. నిరంతరం భగవన్నామ సంకీర్తన జరిగే పవిత్ర గోకులంలోకి సాధారణ రాక్షసులు అడుగుపెట్టలేరు. కానీ భగవంతుడు తన బాల్య లీలలను ప్రదర్శించడానికి మరియు పూతనకు ముక్తిని ప్రసాదించడానికి ఆమె ప్రవేశాన్ని అనుమతించాడు.

### లక్ష్మీదేవి వంటి మనోహర రూపం

తన అసలైన భయంకర రాక్షసి రూపంతో గోకులానికి వెళితే గోపాలురు తనను వెంటనే సంహరిస్తారని పూతనకు తెలుసు. అందుకే ఆమె తన మాయాశక్తితో అత్యంత సౌందర్యవతియైన ఒక దేవకన్య రూపాన్ని ధరించింది:

> **శ్రీమద్ భాగవతం, స్కంధం 10, అధ్యాయం 6, శ్లోకాలు 7–9**
> 
> *తాం ప్రేక్ష్య తన్వీం తరుణీం సులక్షణాం*  
> *రంగద్వలగ్నాం సుకుచోన్నతిం స్త్రియమ్ ।*  
> *సువాససం కాంచనకుండలోల్లసత్-*  
> *కపోలచామీకరకర్ణవేష్టితామ్ ॥*  
> 
> **తాత్పర్యం:** "సన్నని నడుము, నవయవ్వనం, ఆభరణాలతో అలంకరించబడిన ముంగురులు, మెరిసే బంగారు కుండలాలు మరియు పట్టు వస్త్రాలు ధరించిన ఆమెను చూసి గోపికలు ఆశ్చర్యపోయారు. చేతిలో పద్మాన్ని ధరించి వచ్చిన ఆమెను చూసి సాక్షాత్ లక్ష్మీదేవియే నందభవనానికి విచ్చేసిందని భావించారు."

పూతన రూపం ఎంతో ఆకర్షణీయంగా ఉంది. ఆమె నల్లని కురులలో మల్లెపూలు గుబాళిస్తున్నాయి. ఆమె శరీరం నుండి సుగంధ పరిమళాలు వెదజల్లుతున్నాయి. చేతిలో కమలాన్ని పట్టుకుని, నేలపై పాదాలు మోపకుండా గాలిలో తేలుతున్నట్లుగా ఆమె గోకులంలోకి ప్రవేశించింది.

గోకులంలోని అమాయక గోపికలకు ఏమాత్రం అనుమానం రాలేదు. సాక్షాత్ భాగ్యదేవతయైన శ్రీ మహాలక్ష్మియే చిన్నారి కృష్ణుడిని ఆశీర్వదించడానికి వచ్చిందని అందరూ సంభ్రమాశ్చర్యాలతో తిలకించారు.

### నందభవనంలోకి నిరాటంకంగా ప్రవేశం

పూతన నేరుగా నందమహారాజు భవనంలోకి నడిచింది. ఆ సమయంలో నందమహారాజు వార్షిక పన్ను చెల్లించడానికి మథురకు వెళ్లి ఉన్నాడు. గృహంలో యశోదాదేవి, రోహిణీదేవి పసికందు శ్రీకృష్ణుడిని ప్రేమతో లాలిస్తున్నారు.

పూతన ఎంతో మధురమైన మాతృవాత్సల్య నవ్వుతో లోపలికి అడుగుపెట్టింది. ఆమె అపురూప సౌందర్యాన్ని చూసి యశోద, రోహిణి ఇద్దరూ ముగ్ధులయ్యారు. చేతిలో కమలంతో వచ్చిన పుణ్యస్త్రీని అతిథిగా ఆదరించడం వైదిక ధర్మం కనుక, ఆమెను ఎవరూ అడ్డుకోలేదు.

పూతన ఏమాత్రం సంకోచించకుండా పసికృష్ణుడు పడుకున్న గదిలోకి నేరుగా వెళ్లింది.

### కాలకూట విషం మరియు సర్వజ్ఞుడైన భగవానుడు

చిన్ని కృష్ణుడు మేఘశ్యామల వర్ణంతో, పట్టు వస్త్రాలలో పవళించి ఉన్నాడు. ఆయన పాదపద్మాలు, చేతులు దివ్య కాంతులను వెదజల్లుతున్నాయి.

పూతన హృదయంలో భయంకరమైన హత్యాకాండ ఆలోచన ఉంది, కానీ ముఖంపై మాత్రం అమాయక ప్రేమను ప్రదర్శించింది. ఆమె తన స్తనాలపై *కాలకూటం* అనే అత్యంత భయంకరమైన ప్రాణాంతక విషాన్ని పూసుకుని వచ్చింది. ఆ విషం తగిలితే ఎంతటి బలవంతుడైనా క్షణాల్లో భస్మమైపోతాడు. పాలు ఇచ్చే నెపంతో ఆ భయంకర విషాన్ని తాగించి బిడ్డను చంపాలన్నది ఆమె దుష్ట పన్నాగం.

కానీ సర్వజ్ఞుడైన భగవాన్ శ్రీకృష్ణుడికి ఆమె కపటత్వం అంతా తెలుసు. ఆమె కంసుడు పంపిన రాక్షసి అని, ఆమె స్తనాలలో కాలకూట విషం దాగి ఉందని భగవంతుడికి స్పష్టంగా తెలుసు. అయినప్పటికీ ఆమెకు తల్లి వంటి ఉత్తమ గతిని కల్పించేందుకు, పూతన తనను ఎత్తుకోవడానికి చేతులు చాచినప్పుడు, నల్లనయ్య తన పద్మనయనాలను మెల్లగా మూసుకున్నాడు!""",
                "questions": [
                    {
                        "question": "పసిపిల్లలను సంహరించడానికి కంసుడు పంపిన క్రూర రాక్షసి ఎవరు?",
                        "options": [
                            {"text": "పూతన", "is_correct": True},
                            {"text": "శూర్పణఖ", "is_correct": False},
                            {"text": "తాటక", "is_correct": False},
                            {"text": "సింహిక", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పూతనకు ఆకాశంలో ప్రయాణించడానికి సహాయపడిన అలౌకిక సిద్ధి ఏది?",
                        "options": [
                            {"text": "ఖేచరీ సిద్ధి", "is_correct": True},
                            {"text": "అణిమా సిద్ధి", "is_correct": False},
                            {"text": "ప్రాప్తి సిద్ధి", "is_correct": False},
                            {"text": "గరిమా సిద్ధి", "is_correct": False}
                        ]
                    },
                    {
                        "question": "గోకులంలో ప్రవేశించేటప్పుడు పూతన ఎవరి రూపాన్ని ధరించింది?",
                        "options": [
                            {"text": "సాక్షాత్ లక్ష్మీదేవి వంటి అద్భుత సౌందర్యవతియైన దేవకన్య రూపాన్ని", "is_correct": True},
                            {"text": "ఒక ముసలి బిచ్చగత్తె రూపాన్ని", "is_correct": False},
                            {"text": "కవచం ధరించిన యోధుడి రూపాన్ని", "is_correct": False},
                            {"text": "ఒక జటాధారి ముని రూపాన్ని", "is_correct": False}
                        ]
                    },
                    {
                        "question": "తన రూపాన్ని మరింత మంగళకరంగా చూపించడానికి పూతన చేతిలో ఏమి పట్టుకుంది?",
                        "options": [
                            {"text": "కమల పుష్పం", "is_correct": True},
                            {"text": "బంగారు ఖడ్గం", "is_correct": False},
                            {"text": "శంఖం", "is_correct": False},
                            {"text": "వెండి విల్లు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "గోకుల వాసులు పూతనను అడ్డుకోకపోవడానికి కారణం ఏమిటి?",
                        "options": [
                            {"text": "ఆమె సౌందర్యాన్ని చూసి సాక్షాత్ లక్ష్మీదేవియే వచ్చిందని భావించారు", "is_correct": True},
                            {"text": "ఆమె ఆయుధాలతో బెదిరించింది", "is_correct": False},
                            {"text": "ఆమె కంసుడి రాజముద్ర పత్రాన్ని చూపించింది", "is_correct": False},
                            {"text": "అందరూ నిద్రపోతున్నారు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పూతన ఇంటికి వచ్చినప్పుడు బాలకృష్ణుడి వద్ద ఎవరు ఉన్నారు?",
                        "options": [
                            {"text": "యశోదామాత మరియు రోహిణీమాత", "is_correct": True},
                            {"text": "నందమహారాజు మరియు వసుదేవుడు", "is_correct": False},
                            {"text": "గర్గముని మరియు సాందీపని ముని", "is_correct": False},
                            {"text": "కంసుడు మరియు చాణూరుడు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పూతన గోకులానికి వచ్చిన సమయంలో నందమహారాజు ఎక్కడికి వెళ్లారు?",
                        "options": [
                            {"text": "మథురకు కంసుడికి వార్షిక పన్ను చెల్లించడానికి", "is_correct": True},
                            {"text": "బృందావనంలో గోవులను మేపడానికి", "is_correct": False},
                            {"text": "పొలంలో విశ్రమించడానికి", "is_correct": False},
                            {"text": "అడవిలో వేటాడటానికి", "is_correct": False}
                        ]
                    },
                    {
                        "question": "బాలకృష్ణుడిని సంహరించడానికి పూతన తన స్తనాలకు ఏమి పూసుకుని వచ్చింది?",
                        "options": [
                            {"text": "భయంకరమైన కాలకూట విషం", "is_correct": True},
                            {"text": "నిద్ర మందు", "is_correct": False},
                            {"text": "వేడి నూనె", "is_correct": False},
                            {"text": "చేదు వేప రసం", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పూతన తనను ఎత్తుకోవడానికి వచ్చినప్పుడు బాలకృష్ణుడు ఏమి చేశాడు?",
                        "options": [
                            {"text": "ఆమె కపటాన్ని గ్రహించి కన్నులు మూసుకున్నాడు", "is_correct": True},
                            {"text": "భయంతో ఏడవడం ప్రారంభించాడు", "is_correct": False},
                            {"text": "అగ్ని రూపం ధరించాడు", "is_correct": False},
                            {"text": "మంచం పైనుంచి పారిపోయాడు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పూతన వధ లీల శ్రీమద్ భాగవతం దశమ స్కంధంలోని ఏ అధ్యాయంలో వర్ణించబడింది?",
                        "options": [
                            {"text": "అధ్యాయం 6", "is_correct": True},
                            {"text": "అధ్యాయం 3", "is_correct": False},
                            {"text": "అధ్యాయం 1", "is_correct": False},
                            {"text": "అధ్యాయం 10", "is_correct": False}
                        ]
                    }
                ]
            },
            "kn": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "ಪೂತನಾ ರಾಕ್ಷಸಿಯ ಗೋಕುಲ ಪ್ರವೇಶ ಲೀಲೆ",
                "content": """### ಕಂಸನಿಂದ ಪೂತನಾ ರಾಕ್ಷಸಿಯ ನಿಯೋಜನೆ

ದುಷ್ಟ ಕಂಸನು ತನ್ನ ಮಂತ್ರಿಗಳ ದುಷ್ಟ ಸಲಹೆಯಂತೆ, ಶೂರಸೇನ ರಾಜ್ಯದ ನವಜಾತ ಶಿಶುಗಳನ್ನು ಹುಡುಕಿ ಕೊಲ್ಲಲು ತನ್ನ ಕ್ರೂರ ಅಸುರರನ್ನು ಕಳುಹಿಸಿದನು. ಆ ಎಲ್ಲಾ ರಾಕ್ಷಸರಲ್ಲಿ ಅತ್ಯಂತ ನಿರ್ದಯಳೂ ಕುಖ್ಯಾತಳೂ ಆದವಳು ಪೂತನಾ ಎಂಬ ರಾಕ್ಷಸಿ.

ಪೂತನಾಗೆ ಆಕಾಶದಲ್ಲಿ ಹಾರಾಡುವ *ಖೇಚರೀ ಸಿದ್ಧಿ* ಎಂಬ ಮಾಂತ್ರಿಕ ಶಕ್ತಿಯಿತ್ತು. ಮುಗ್ಧ ನಸುಗೂಸುಗಳನ್ನು ನಿರ್ದಯವಾಗಿ ಕೊಲ್ಲುವುದೇ ಅವಳ ಕ್ರೂರ ಕಾಯಕವಾಗಿತ್ತು:

> **ಶ್ರೀಮದ್ ಭಾಗವತಂ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 6, ಶ್ಲೋಕ 4**
> 
> *ಸಾ ಖೇಚರ್ಯೇಕದೋತ್ಪತ್ಯ ಪೂತನಾ ಲೋಕಬಾಲಘಾತಿನೀ ।*  
> *ಪುರಾನ್ ಜನಪದಾನ್ ಗ್ರಾಮಾನ್ ಬಭ್ರಾಮ ಶಿಶೂನ್ ಘ್ನತೀ ॥*  
> 
> **ಭಾವಾರ್ಥ:** "ಆಕಾಶದಲ್ಲಿ ಹಾರುವ ಖೇಚರೀ ಶಕ್ತಿಯುಳ್ಳವಳೂ, ಜಗತ್ತಿನ ಹಸುಗೂಸುಗಳನ್ನು ಕೊಲ್ಲುವುದೇ ಕಾಯಕವಾಗಿ ಉಳ್ಳವಳೂ ಆದ ಪೂತನಾ ಎಂಬ ರಾಕ್ಷಸಿಯು ನಗರ, ಪಟ್ಟಣ ಮತ್ತು ಹಳ್ಳಿಗಳಲ್ಲಿ ಸಂಚರಿಸುತ್ತಾ ಮುಗ್ಧ ಶಿಶುಗಳನ್ನು ಸಂಹರಿಸತೊಡಗಿದಳು."

ದೈವಯೋಗದಿಂದ ಆ ಪೂತನೆ ಗೋಕುಲದ ಗಡಿಗೆ ಬಂದು ತಲುಪಿದಳು. ಅಲ್ಲಿ ಸಾಕ್ಷಾತ್ ಭಗವಾನ್ ಶ್ರೀಕೃಷ್ಣನು ನಂದಮಹಾರಾಜ ಮತ್ತು ಯಶೋದೆಯರ ಕಂದನಾಗಿ ನೆಲೆಸಿದ್ದನು. ಸದಾ ಹರಿನಾಮ ಸಂಕೀರ್ತನೆ ಮೊಳಗುವ ಗೋಕುಲದ ಪವಿತ್ರ ಕ್ಷೇತ್ರಕ್ಕೆ ಸಾಮಾನ್ಯ ಅಸುರರು ಕಾಲಿಡಲು ಸಾಧ್ಯವಿರಲಿಲ್ಲ. ಆದರೆ ಭಗವಂತನು ತನ್ನ ಬಾಲಲೀಲೆಗಳನ್ನು ಪ್ರಕಟಿಸಲು ಮತ್ತು ಪೂತನೆಗೆ ಮುಕ್ತಿ ನೀಡಲು ಸಂಕಲ್ಪಿಸಿದ್ದರಿಂದ ಅವಳಿಗೆ ಪ್ರವೇಶ ಸಿಕ್ಕಿತು.

### ಸಾಕ್ಷಾತ್ ಲಕ್ಷ್ಮೀದೇವಿಯಂತಹ ಮೋಹಕ ರೂಪ

ತನ್ನ ನೈಜ ರಾಕ್ಷಸಿ ರೂಪದಲ್ಲಿ ಗೋಕುಲಕ್ಕೆ ಹೋದರೆ ಗೋಪಾಲಕರು ತನ್ನನ್ನು ತಕ್ಷಣ ಕೊಲ್ಲುತ್ತಾರೆಂದು ಪೂತನೆಗೆ ತಿಳಿದಿತ್ತು. ಆದ್ದರಿಂದ ಅವಳು ತನ್ನ ಮಾಯಾಶಕ್ತಿಯಿಂದ ಅದ್ಭುತ ಸುಂದರಿಯಾದ ದೇವಕನ್ಯೆಯ ವೇಷವನ್ನು ಧರಿಸಿದಳು:

> **ಶ್ರೀಮದ್ ಭಾಗವತಂ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 6, ಶ್ಲೋಕಗಳು 7–9**
> 
> *ತಾಂ ಪ್ರೇಕ್ಷ್ಯ ತನ್ವೀಂ ತರುಣೀಂ ಸುಲಕ್ಷಣಾಂ*  
> *ರಂಗದ್ವಲಗ್ನಾಂ ಸುಕುಚೋನ್ನತಿಂ ಸ್ತ್ರಿಯಮ್ ।*  
> *ಸುವಾಸಸಂ ಕಾಂಚನಕುಂಡಲೋಲ್ಲಸತ್-*  
> *ಕಪೋಲಚಾಮೀಕರಕರ್ಣವೇಷ್ಟಿತಾಮ್ ॥*  
> 
> **ಭಾವಾರ್ಥ:** "ಅವಳ ತೆಳುವಾದ ನಡು, ನವಯೌವನ, ತೇಜಸ್ಸು, ಕಿವಿಯ ಚಿನ್ನದ ಓಲೆಗಳು ಮತ್ತು ದಿವ್ಯ ರೇಷ್ಮೆ ವಸ್ತ್ರಗಳನ್ನು ಕಂಡು ಗೋಪಿಯರು ವಿಸ್ಮಯಗೊಂಡರು. ಕೈಯಲ್ಲಿ ಕಮಲದ ಹೂವನ್ನು ಹಿಡಿದು ಬಂದ ಅವಳನ್ನು ಕಂಡು ಸಾಕ್ಷಾತ್ ಲಕ್ಷ್ಮೀದೇವಿಯೇ ನಂದಭವನಕ್ಕೆ ಬಂದಿದ್ದಾಳೆಂದು ಎಲ್ಲರೂ ಭಾವಿಸಿದರು."

ಪೂತನೆಯ ಆ ವೇಷವು ಅತ್ಯಂತ ಮನಮೋಹಕವಾಗಿತ್ತು. ಅವಳ ಮುಡಿಯಲ್ಲಿ ಪರಿಮಳಯುಕ್ತ ಮಲ್ಲಿಗೆ ಹೂಗಳು ಶೋಭಿಸುತ್ತಿದ್ದವು. ಕೈಯಲ್ಲಿ ಕಮಲದ ಹೂವನ್ನು ಹಿಡಿದು ನೆಲದ ಮೇಲೆ ಹೆಜ್ಜೆಯಿಡದೆ ತೇಲುತ್ತಿರುವಂತೆ ಅವಳು ಮುನ್ನಡೆದಳು.

ಗೋಕುಲದ ಮುಗ್ಧ ಗೋಪ-ಗೋಪಿಯರಿಗೆ ಕಿಂಚಿತ್ತೂ ಅನುಮಾನ ಬರಲಿಲ್ಲ. ಶ್ರೀಕೃಷ್ಣನಿಗೆ ಶುಭ ಹಾರೈಸಲು ಸಾಕ್ಷಾತ್ ಅದೃಷ್ಟದ ದೇವತೆ ಲಕ್ಷ್ಮಿಯೇ ಬಂದಿದ್ದಾಳೆಂದು ಎಲ್ಲರೂ ನಂಬಿದರು!

### ನಂದಭವನಕ್ಕೆ ಮುಕ್ತ ಪ್ರವೇಶ

ಪೂತನೆ ನೇರವಾಗಿ ನಂದಮಹಾರಾಜರ ಭವನದ ಒಳಗೆ ಪ್ರವೇಶಿಸಿದಳು. ಆ ಸಮಯದಲ್ಲಿ ನಂದಮಹಾರಾಜರು ವಾರ್ಷಿಕ ಕಂದಾಯ ಸಲ್ಲಿಸಲು ಮಥುರೆಗೆ ತೆರಳಿದ್ದರು. ಮನೆಯೊಳಗೆ ತಾಯಿ ಯಶೋದಾ ಮತ್ತು ತಾಯಿ ರೋಹಿಣಿ ಮುದ್ದು ಕೃಷ್ಣನ ಲಾಲನೆ ಪಾಲನೆಯಲ್ಲಿ ತೊಡಗಿದ್ದರು.

ಪೂತನೆ ಮುಖದಲ್ಲಿ ವಾತ್ಸಲ್ಯದ ಕಪಟ ನಗೆಯೊಂದಿಗೆ ಮನೆಯ ಹೊಸ್ತಿಲನ್ನು ದಾಟಿದಳು. ಅವಳ ದಿವ್ಯ ಸೌಂದರ್ಯವನ್ನು ಕಂಡು ಯಶೋದಾ ಮತ್ತು ರೋಹಿಣಿ ಬೆರಗಾದರು. ಕೈಯಲ್ಲಿ ಕಮಲದೊಂದಿಗೆ ಬಂದ ದೇವತೆಯಂತಹ ಹೆಣ್ಣುಮಗಳನ್ನು ವೈದಿಕ ಸಂಪ್ರದಾಯದಂತೆ ಆತಿಥ್ಯದಿಂದ ಸ್ವಾಗತಿಸಬೇಕೆಂಬ ಭಾವನೆಯಿಂದ ಯಾರೂ ಅವಳನ್ನು ತಡೆಯಲಿಲ್ಲ.

ಪೂತನೆ ಯಾವುದೇ ಅಡೆತಡೆಯಿಲ್ಲದೆ ಬಾಲಕೃಷ್ಣ ಮಲಗಿದ್ದ ಕೋಣೆಗೆ ಸರಸರನೆ ಹೆಜ್ಜೆಯಿಟ್ಟಳು.

### ಕಾಲಕೂಟ ವಿಷ ಮತ್ತು ಸರ್ವಜ್ಞ ಭಗವಂತನ ದೃಷ್ಟಿ

ಮೇಘಶ್ಯಾಮಲ ವರ್ಣದ ಮುದ್ದು ಕೃಷ್ಣನು ಮೃದುವಾದ ಹಾಸಿಗೆಯ ಮೇಲೆ ಮಲಗಿದ್ದನು. ಆತನ ಪುಟ್ಟ ಪಾದಕಮಲಗಳು ಮತ್ತು ಕೈಗಳು ದಿವ್ಯ ಕಾಂತಿಯನ್ನು ಬೀರುತ್ತಿದ್ದವು.

ಪೂತನೆಯ ಮನಸ್ಸಿನಲ್ಲಿ ಕೊಲೆಗಡುಕತನ ತುಂಬಿದ್ದರೂ, ಮುಖದಲ್ಲಿ ಮಾತ್ರ ಮಾತೃಪ್ರೇಮದ ನಾಟಕವಾಡುತ್ತಿದ್ದಳು. ಅವಳು ತನ್ನ ಸ್ತನಗಳಿಗೆ *ಕಾಲಕೂಟ* ಎಂಬ ಭಯಂಕರ ಹಾಲಾಹಲ ವಿಷವನ್ನು ಸವರಿಕೊಂಡು ಬಂದಿದ್ದಳು. ಆ ವಿಷದ ಒಂದು ಹನಿಯೂ ಯಾವುದೇ ಜೀವಿಯನ್ನು ಕ್ಷಣಾರ್ಧದಲ್ಲಿ ಭಸ್ಮ ಮಾಡಬಲ್ಲದ್ದಾಗಿತ್ತು. ಎದೆಹಾಲು ಕೊಡುವ ನೆಪದಲ್ಲಿ ವಿಷವುಣಿಸಿ ಮಗುವನ್ನು ಕೊಲ್ಲುವುದೇ ಅವಳ ಕ್ರೂರ ತಂತ್ರವಾಗಿತ್ತು.

ಆದರೆ ಸರ್ವಜ್ಞನಾದ ಭಗವಾನ್ ಶ್ರೀಕೃಷ್ಣನಿಗೆ ಆಕೆಯ ದುರುದ್ದೇಶ ತಿಳಿದಿತ್ತು. ಈಕೆ ಕಂಸನಿಂದ ಕಳುಹಿಸಲ್ಪಟ್ಟ ರಾಕ್ಷಸಿ ಮತ್ತು ಇವಳ ಸ್ತನಗಳಲ್ಲಿ ಹಾಲಾಹಲ ವಿಷವಿದೆ ಎಂಬುದನ್ನು ಭಗವಂತನು ಸಂಪೂರ್ಣವಾಗಿ ಅರಿತಿದ್ದನು. ಆದರೂ ಆಕೆಗೆ ತಾಯಿಯಂತಹ ಪರಮ ಗತಿಯನ್ನು ಕರುಣಿಸಲು ನಿಶ್ಚಯಿಸಿದ ಭಗವಂತನು, ಪೂತನೆ ತನ್ನನ್ನು ಎತ್ತಿಕೊಳ್ಳಲು ಮುಂದಾದಾಗ ತನ್ನ ಕಮಲ ನೇತ್ರಗಳನ್ನು ಮೆಲ್ಲನೆ ಮುಚ್ಚಿಕೊಂಡನು!""",
                "questions": [
                    {
                        "question": "ಹಸುಗೂಸುಗಳನ್ನು ಕೊಲ್ಲಲು ಕಂಸನಿಂದ ಕಳುಹಿಸಲ್ಪಟ್ಟ ಕ್ರೂರ ರಾಕ್ಷಸಿ ಯಾರು?",
                        "options": [
                            {"text": "ಪೂತನಾ", "is_correct": True},
                            {"text": "ಶೂರ್ಪಣಖಿ", "is_correct": False},
                            {"text": "ತಾಟಕಿ", "is_correct": False},
                            {"text": "ಸಿಂಹಿಕೆ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಆಕಾಶದಲ್ಲಿ ಹಾರಾಡಲು ಪೂತನೆ ಹೊಂದಿದ್ದ ಅದ್ಭುತ ಸಿದ್ಧಿ ಯಾವುದು?",
                        "options": [
                            {"text": "ಖೇಚರೀ ಸಿದ್ಧಿ", "is_correct": True},
                            {"text": "ಅಣಿಮಾ ಸಿದ್ಧಿ", "is_correct": False},
                            {"text": "ಪ್ರಾಪ್ತಿ ಸಿದ್ಧಿ", "is_correct": False},
                            {"text": "ಗರಿಮಾ ಸಿದ್ಧಿ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಗೋಕುಲಕ್ಕೆ ಪ್ರವೇಶಿಸುವಾಗ ಪೂತನೆ ಯಾರ ವೇಷವನ್ನು ಧರಿಸಿದ್ದಳು?",
                        "options": [
                            {"text": "ಸಾಕ್ಷಾತ್ ಲಕ್ಷ್ಮೀದೇವಿಯಂತಹ ಪರಮ ಸುಂದರಿಯಾದ ದೇವಕನ್ಯೆಯ ವೇಷ", "is_correct": True},
                            {"text": "ಒಬ್ಬ ವೃದ್ಧ ಭಿಕ್ಷುಕಿಯ ವೇಷ", "is_correct": False},
                            {"text": "ಕವಚ ಧರಿಸಿದ ಯೋಧನ ವೇಷ", "is_correct": False},
                            {"text": "ಜಟಾಧಾರಿ ಮುನಿಯ ವೇಷ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ತನ್ನ ವೇಷವನ್ನು ಮಂಗಳಕರವಾಗಿ ತೋರಲು ಪೂತನೆಯ ಕೈಯಲ್ಲಿ ಏನಿತ್ತು?",
                        "options": [
                            {"text": "ಕಮಲದ ಹೂವು", "is_correct": True},
                            {"text": "ಚಿನ್ನದ ಖಡ್ಗ", "is_correct": False},
                            {"text": "ಶಂಖ", "is_correct": False},
                            {"text": "ಬೆಳ್ಳಿಯ ಬಿಲ್ಲು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಗೋಕುಲದ ಜನರು ಪೂತನೆಯನ್ನು ತಡೆಯದೆ ಬಿಡಲು ಕಾರಣವೇನು?",
                        "options": [
                            {"text": "ಅವಳ ದಿವ್ಯ ಸೌಂದರ್ಯವನ್ನು ಕಂಡು ಸಾಕ್ಷಾತ್ ಲಕ್ಷ್ಮೀದೇವಿಯೆಂದು ಭಾವಿಸಿದರು", "is_correct": True},
                            {"text": "ಅವಳು ಆಯುಧಗಳನ್ನು ತೋರಿಸಿ ಹೆದರಿಸಿದಳು", "is_correct": False},
                            {"text": "ಅವಳು ಕಂಸನ ರಾಜಾಜ್ಞೆಯನ್ನು ತೋರಿಸಿದಳು", "is_correct": False},
                            {"text": "ಎಲ್ಲರೂ ಗಾಢ ನಿದ್ರೆಯಲ್ಲಿದ್ದರು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಪೂತನೆ ಮನೆಗೆ ಬಂದಾಗ ಬಾಲಕೃಷ್ಣನ ಬಳಿ ಯಾರೆಲ್ಲ ಇದ್ದರು?",
                        "options": [
                            {"text": "ತಾಯಿ ಯಶೋದಾ ಮತ್ತು ತಾಯಿ ರೋಹಿಣಿ", "is_correct": True},
                            {"text": "ನಂದಮಹಾರಾಜ ಮತ್ತು ವಸುದೇವ", "is_correct": False},
                            {"text": "ಗರ್ಗಮುನಿ ಮತ್ತು ಸಾಂದೀಪನಿ ಮುನಿ", "is_correct": False},
                            {"text": "ಕಂಸ ಮತ್ತು ಚಾಣೂರ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಪೂತನೆ ಗೋಕುಲಕ್ಕೆ ಬಂದಾಗ ನಂದಮಹಾರಾಜರು ಎಲ್ಲಿಗೆ ಹೋಗಿದ್ದರು?",
                        "options": [
                            {"text": "ಮಥುರೆಗೆ ಕಂಸನಿಗೆ ಕಂದಾಯ ಪಾವತಿಸಲು", "is_correct": True},
                            {"text": "ಬೃಂದಾವನದಲ್ಲಿ ಗೋವುಗಳನ್ನು ಮೇಯಿಸಲು", "is_correct": False},
                            {"text": "ಅಂಗಳದಲ್ಲಿ ವಿಶ್ರಾಂತಿ ಪಡೆಯಲು", "is_correct": False},
                            {"text": "ಕಾಡಿನಲ್ಲಿ ಬೇಟೆಯಾಡಲು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಶ್ರೀಕೃಷ್ಣನನ್ನು ಕೊಲ್ಲಲು ಪೂತನೆ ತನ್ನ ಸ್ತನಗಳಿಗೆ ಸವರಿಕೊಂಡಿದ್ದ ವಿಷ ಯಾವುದು?",
                        "options": [
                            {"text": "ಭಯಂಕರ ಕಾಲಕೂಟ ವಿಷ", "is_correct": True},
                            {"text": "ನಿದ್ರೆಯ ಔಷಧಿ", "is_correct": False},
                            {"text": "ಕುದಿಯುವ ಎಣ್ಣೆ", "is_correct": False},
                            {"text": "ಬೇವಿನ ರಸ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಪೂತನೆ ತನ್ನನ್ನು ಎತ್ತಿಕೊಳ್ಳಲು ಬಂದಾಗ ಬಾಲಕೃಷ್ಣನು ಏನು ಮಾಡಿದನು?",
                        "options": [
                            {"text": "ಅವಳ ದುರುದ್ದೇಶವನ್ನರಿತು ಕಣ್ಣುಗಳನ್ನು ಮುಚ್ಚಿಕೊಂಡನು", "is_correct": True},
                            {"text": "ಭಯದಿಂದ ಕಿರುಚುತ್ತಾ ಅತ್ತನು", "is_correct": False},
                            {"text": "ಅಗ್ನಿರೂಪ ತಾಳಿದನು", "is_correct": False},
                            {"text": "ಹಾಸಿಗೆಯಿಂದ ಎದ್ದು ಓಡಿದನು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಪೂತನೆಯ ಈ ಲೀಲೆಯು ಶ್ರೀಮದ್ ಭಾಗವತದ 10ನೇ ಸ್ಕಂಧದ ಯಾವ ಅಧ್ಯಾಯದಲ್ಲಿದೆ?",
                        "options": [
                            {"text": "ಅಧ್ಯಾಯ 6", "is_correct": True},
                            {"text": "ಅಧ್ಯಾಯ 3", "is_correct": False},
                            {"text": "ಅಧ್ಯಾಯ 1", "is_correct": False},
                            {"text": "ಅಧ್ಯಾಯ 10", "is_correct": False}
                        ]
                    }
                ]
            },
            "ml": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "പൂതന എന്ന രാക്ഷസി ഗോകൂലത്തിൽ എത്തിയ ലീല",
                "content": """### കംസൻ പൂതനയെ നിയോഗിക്കുന്നു

ദുഷ്ടനായ കംസരാജാവ് തന്റെ മന്ത്രിമാരുടെ ഉപദേശപ്രകാരം, ശൂരസേന രാജ്യത്തെ എല്ലാ നവജാതശിശുക്കളെയും കൊന്നൊടുക്കാൻ തന്റെ ക്രൂരരായ അസുരന്മാരെ അയച്ചു. അവരിൽ ഏറ്റവും ഭയങ്കരിയും ക്രൂരയുമായ ഒരു രാക്ഷസിയായിരുന്നു പൂതന.

ആകാശത്തിലൂടെ പറന്നുയരാൻ കഴിയുന്ന *ഖേചരീ സിദ്ധി* എന്ന മാന്ത്രിക ശക്തി പൂതനയ്ക്കുണ്ടായിരുന്നു. നിഷ്കളങ്കരായ കൊച്ചുകുഞ്ഞുങ്ങളെ ദാക്ഷിണ്യമില്ലാതെ കൊല്ലുകയായിരുന്നു അവളുടെ ദുഷ്ട കർമ്മം:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അധ്യായം 6, ശ്ലോകം 4**
> 
> *സാ ഖേചര്യേകദോത്പത്യ പൂതനാ ലോകബാലഘാതിനീ ।*  
> *പുരാൻ ജനപദാൻ ഗ്രാമാൻ ബഭ്രാമ ശിശൂൻ ഘ്നതീ ॥*  
> 
> **അർത്ഥം:** "ആകാശത്തിലൂടെ സഞ്ചരിക്കുന്ന ഖേചരീ സിദ്ധിയുള്ളവളും, കുഞ്ഞുങ്ങളെ കൊല്ലുന്നതുതന്നെ തൊഴിലാക്കിയവളുമായ പൂതന എന്ന രാക്ഷസി, നഗരങ്ങളിലും ഗ്രാമങ്ങളിലും ജനപദങ്ങളിലും ചുറ്റിനടന്ന് നിഷ്കളങ്കരായ കുഞ്ഞുങ്ങളെ കൊന്നൊടുക്കാൻ തുടങ്ങി."

ദൈവനിയോഗത്താൽ പൂതന ഗോകൂലത്തിന്റെ അതിർത്തിയിലെത്തി. അവിടെ ഭഗവാൻ ശ്രീകൃഷ്ണൻ നന്ദഗോപരുടെയും യശോദ അമ്മയുടെയും ഓമനപ്പുത്രനായി അവതരിച്ചിരുന്നു. സദാ ഹരിനാമകീർത്തനം മുഴങ്ങുന്ന പവിത്രമായ ഗോകൂലത്തിലേക്ക് സാധാരണ അസുരന്മാർക്ക് കടക്കാനാകുമായിരുന്നില്ല. എന്നാൽ ഭഗവാൻ തന്റെ ബാലലീലകൾ പ്രകടമാക്കാനും പൂതനയ്ക്ക് മോക്ഷം നൽകാനും തിരുമനസ്സായതിനാൽ അവൾക്ക് പ്രവേശനം സാധ്യമായി.

### ലക്ഷ്മീദേവിയെപ്പോലെ സുന്ദരരൂപം ധരിക്കുന്നു

തന്റെ ഭീകരമായ രാക്ഷസി രൂപത്തിൽ ചെന്നാൽ ഗോപന്മാർ തന്നെ വധിക്കുമെന്ന് പൂതനയ്ക്കറിയാമായിരുന്നു. അതിനാൽ അവൾ തന്റെ മായാശക്തിയാൽ അതീവ സുന്ദരിയായ ഒരു ദേവസ്ത്രീയുടെ രൂപം സ്വീകരിച്ചു:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അധ്യായം 6, ശ്ലോകങ്ങൾ 7–9**
> 
> *താം പ്രേക്ഷ്യ തന്വീം തരുണീം സുലക്ഷണാം*  
> *രംഗദ്വലഗ്നാം സുകുചോന്നതിം സ്ത്രിയം ।*  
> *സുവാസസം കാഞ്ചനകുണ്ഡലോല്ലസത്-*  
> *കപോലചാമീകരകർണ്ണവേഷ്ടിതാം ॥*  
> 
> **അർത്ഥം:** "മെലിഞ്ഞ ഇടയും, നവയൗവനവും, ചെവികളിൽ തിളങ്ങുന്ന സ്വർണ്ണക്കമ്മലുകളും, വിശേഷപ്പെട്ട പട്ടുചേലയും ധരിച്ച അവളെക്കണ്ട് ഗോപികമാർ അത്ഭുതസ്തബ്ധരായി. കയ്യിൽ ഒരു താമരപ്പൂവുമായി നന്ദഭവനത്തിലേക്ക് പ്രവേശിക്കുന്ന അവളെക്കണ്ട് സാക്ഷാൽ ലക്ഷ്മീദേവി തന്നെയാണെന്ന് എല്ലാവരും വിചാരിച്ചു."

പൂതനയുടെ വേഷം അത്യന്തം ആകർഷകമായിരുന്നു. മുടിയിൽ മുല്ലപ്പൂക്കൾ ചൂടി, ദേഹത്തുനിന്നും സുഗന്ധം പരത്തി, നിലത്തു കാലുറപ്പിക്കാതെ കാറ്റിൽ ഒഴുകി നടക്കുന്നതുപോലെ അവൾ നടന്നുനീങ്ങി.

ഗോകൂലത്തിലെ നിഷ്കളങ്കരായ ഗോപന്മാരും ഗോപികമാരും അവളെ തെല്ലും സംശയിച്ചില്ല. ഉണ്ണിക്കണ്ണനെ അനുഗ്രഹിക്കാൻ ഭാഗ്യദേവതയായ സാക്ഷാൽ മഹാലക്ഷ്മി തന്നെ വന്നതാണെന്ന് അവർ വിശ്വസിച്ചു.

### നന്ദഭവനത്തിലേക്ക് തടസ്സമില്ലാതെ പ്രവേശിക്കുന്നു

പൂതന നേരെ നന്ദഗോപരുടെ ഭവനത്തിലേക്ക് കടന്നുചെന്നു. ആ സമയത്ത് നന്ദഗോപർ കംസന് കപ്പം കൊടുക്കാനായി മഥുരയിൽ പോയിരിക്കുകയായിരുന്നു. ഭവനത്തിൽ യശോദ അമ്മയും രോഹിണി അമ്മയും ഉണ്ണിക്കണ്ണനെ സ്നേഹത്തോടെ പരിചരിച്ചുകൊണ്ടിരിക്കുകയായിരുന്നു.

പൂതന മുഖത്ത് മാതൃവാത്സല്യത്തിന്റെ ചിരിയോടെ വാതിൽപടി കടന്നു. അവളുടെ രൂപലാവണ്യം കണ്ട് യശോദയും രോഹിണിയും അത്ഭുതപ്പെട്ടു. കയ്യിൽ താമരപ്പൂവുമായി വന്ന അതിഥിയെ ആദരിക്കേണ്ടത് ധർമ്മമായതിനാലും, സ്നേഹസമ്പന്നയായ ഒരു പുണ്യവതിയാണെന്ന് തോന്നിയതിനാലും ആരും അവളെ തടഞ്ഞില്ല.

പൂതന ഒട്ടും അമാന്തിക്കാതെ ഉണ്ണിക്കണ്ണൻ കിടക്കുന്ന മുറിയിലേക്ക് വേഗത്തിൽ നടന്നുചെന്നു.

### കാളകൂടവിഷവും സർവ്വജ്ഞനായ ഭഗവാനും

പട്ടുവിരിപ്പിൽ കിടക്കുന്ന ഉണ്ണിക്കണ്ണൻ കാർമേഘവർണ്ണത്തോടെ ശോഭിക്കുകയായിരുന്നു. ആ താമരക്കണ്ണുകളും കൈകാലുകളും അതിദിവ്യമായ പ്രകാശം ചൊരിഞ്ഞു.

പൂതനയുടെ ഉള്ളിൽ കൊലപാതക ചിന്തയായിരുന്നു, എങ്കിലും മുഖത്ത് വാത്സല്യത്തിന്റെ നാടകം അവൾ തുടർന്നു. ആരെയും ഞൊടിയിടയിൽ ചാരമാക്കാൻ ശേഷിയുള്ള *കാളകൂടം* എന്ന മാരകവിഷം അവൾ തന്റെ മുലകളിൽ പുരട്ടിയിരുന്നു. മുലപ്പാൽ കൊടുക്കുന്ന വ്യാജേന ആ കാളകൂടവിഷം കുടിപ്പിച്ചു കുഞ്ഞിനെ കൊല്ലുകയായിരുന്നു അവളുടെ ക്രൂരമായ തന്ത്രം.

എന്നാൽ സർവ്വജ്ഞനായ ഭഗവാൻ ശ്രീകൃഷ്ണൻ അവളുടെ എല്ലാ കപടതകളും അറിഞ്ഞു. അവൾ കംസൻ അയച്ച രാക്ഷസിയാണെന്നും, അവളുടെ മുലകളിൽ കാളകൂടവിഷം പുരട്ടിയിട്ടുണ്ടെന്നും ഭഗവാനറിയാമായിരുന്നു. എങ്കിലും അവൾക്ക് ഒരു അമ്മയുടെ ഉന്നതമായ മോക്ഷപദം നൽകാൻ നിശ്ചയിച്ച ഭഗവാൻ, അവൾ തന്നെ എടുക്കാൻ കൈനീട്ടിയപ്പോൾ തന്റെ താമരക്കണ്ണുകൾ മെല്ലെ അടച്ചു!""",
                "questions": [
                    {
                        "question": "പിഞ്ചുകുഞ്ഞുങ്ങളെ കൊന്നൊടുക്കാൻ കംസൻ അയച്ച ക്രൂരയായ രാക്ഷസി ആരായിരുന്നു?",
                        "options": [
                            {"text": "പൂതന", "is_correct": True},
                            {"text": "ശൂർപ്പണഖ", "is_correct": False},
                            {"text": "താടക", "is_correct": False},
                            {"text": "സിംഹിക", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ആകാശത്തിലൂടെ സഞ്ചരിക്കാൻ പൂതനയ്ക്കുണ്ടായിരുന്ന അപൂർവ്വ സിദ്ധി ഏതായിരുന്നു?",
                        "options": [
                            {"text": "ഖേചരീ സിദ്ധി", "is_correct": True},
                            {"text": "അണിമാ സിദ്ധി", "is_correct": False},
                            {"text": "പ്രാപ്തി സിദ്ധി", "is_correct": False},
                            {"text": "ഗരിമാ സിദ്ധി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഗോകൂലത്തിൽ പ്രവേശിക്കുമ്പോൾ പൂതന ആരുടെ രൂപമാണ് ധരിച്ചിരുന്നത്?",
                        "options": [
                            {"text": "സാക്ഷാൽ ലക്ഷ്മീദേവിയെപ്പോലെ സുന്ദരിയായ ഒരു ദേവസ്ത്രീയുടെ രൂപം", "is_correct": True},
                            {"text": "ഒരു വൃദ്ധയായ ഭിക്ഷക്കാരിയുടെ രൂപം", "is_correct": False},
                            {"text": "പടച്ചട്ട ധരിച്ച ഒരു പടയാളിയുടെ രൂപം", "is_correct": False},
                            {"text": "ജട ധരിച്ച ഒരു മുനിയുടെ രൂപം", "is_correct": False}
                        ]
                    },
                    {
                        "question": "തന്റെ രൂപം മംഗളകരമായി കാണിക്കാൻ പൂതന കയ്യിൽ കരുതിയിരുന്നത് എന്തായിരുന്നു?",
                        "options": [
                            {"text": "ഒരു താമരപ്പൂവ്", "is_correct": True},
                            {"text": "ഒരു വാൾ", "is_correct": False},
                            {"text": "ഒരു ശംഖ്", "is_correct": False},
                            {"text": "ഒരു വെള്ളി വില്ല്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഗോകൂലവാസികൾ പൂതനയെ തടയാതിരുന്നത് എന്തുകൊണ്ടായിരുന്നു?",
                        "options": [
                            {"text": "അവളുടെ സൗന്ദര്യം കണ്ട് സാക്ഷാൽ ലക്ഷ്മീദേവി തന്നെയാണെന്ന് അവർ കരുതി", "is_correct": True},
                            {"text": "അവൾ ആയുധം കാട്ടി ഭയപ്പെടുത്തി", "is_correct": False},
                            {"text": "അവൾ കംസന്റെ രാജകീയ ഉത്തരവ് കാട്ടി", "is_correct": False},
                            {"text": "എല്ലാവരും ഉറക്കത്തിലായിരുന്നു", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പൂതന ഭവനത്തിൽ പ്രവേശിച്ചപ്പോൾ ഉണ്ണിക്കണ്ണന്റെ അടുത്ത് ആരെല്ലാമാണ് ഉണ്ടായിരുന്നത്?",
                        "options": [
                            {"text": "യശോദ അമ്മയും രോഹിണി അമ്മയും", "is_correct": True},
                            {"text": "നന്ദഗോപരും വസുദേവരും", "is_correct": False},
                            {"text": "ഗർഗ്ഗമുനിയും സാന്ദീപനി മുനിയും", "is_correct": False},
                            {"text": "കംസനും ചാണൂരനും", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പൂതന ഗോകൂലത്തിൽ എത്തിയ സമയം നന്ദഗോപർ എവിടെയായിരുന്നു?",
                        "options": [
                            {"text": "കംസന് കപ്പം നൽകാനായി മഥുരയിൽ", "is_correct": True},
                            {"text": "വൃന്ദാവനത്തിൽ പശുക്കളെ മേയ്ക്കാൻ", "is_correct": False},
                            {"text": "മുറ്റത്ത് വിശ്രമിക്കാൻ", "is_correct": False},
                            {"text": "കാട്ടിൽ നായാട്ടിന്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഉണ്ണിക്കണ്ണനെ കൊല്ലാനായി പൂതന മുലകളിൽ പുരട്ടിയിരുന്ന മാരക വിഷമേതായിരുന്നു?",
                        "options": [
                            {"text": "കാളകൂടവിഷം", "is_correct": True},
                            {"text": "മയക്കുമരുന്ന്", "is_correct": False},
                            {"text": "തിളച്ച എണ്ണ", "is_correct": False},
                            {"text": "കയ്പുള്ള വേപ്പുവെള്ളം", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പൂതന തന്നെ എടുക്കാൻ അടുത്തുവന്നപ്പോൾ ഭഗവാൻ ശ്രീകൃഷ്ണൻ എന്താണ് ചെയ്തത്?",
                        "options": [
                            {"text": "അവളുടെ ദുഷ്ട ഉദ്ദേശ്യമറിഞ്ഞ് കണ്ണുകൾ മെല്ലെ അടച്ചു", "is_correct": True},
                            {"text": "പേടിച്ച് ഉറക്കെ കരഞ്ഞു", "is_correct": False},
                            {"text": "തീജ്വാലയായി മാറി", "is_correct": False},
                            {"text": "കിടക്കയിൽ നിന്ന് ഓടിപ്പോയി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പൂതനാമോക്ഷം ശ്രീമദ് ഭാഗവതം പത്താം സ്കന്ധത്തിലെ ഏത് അധ്യായത്തിലാണ് വിവരിക്കുന്നത്?",
                        "options": [
                            {"text": "അധ്യായം 6", "is_correct": True},
                            {"text": "അധ്യായം 3", "is_correct": False},
                            {"text": "അധ്യായം 1", "is_correct": False},
                            {"text": "അധ്യായം 10", "is_correct": False}
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

        self.stdout.write(self.style.SUCCESS(f"Successfully populated Story 15 (ID: {story.id}) across all 7 languages!"))
