import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askharekrishna_backend.settings')
django.setup()

from django.core.management.base import BaseCommand
from stories.models import StoryMainTopic, Story, StoryTranslation, StoryQuestion, StoryQuestionOption

class Command(BaseCommand):
    help = "Populate Story 17: The Purification of Putana and the Gopis' Protective Mantras across 7 languages"

    def handle(self, *args, **options):
        topic = StoryMainTopic.objects.get(name="Krishna Pastimes")

        story_slug = "krishna-pastimes-the-purification-of-putana-and-the-gopis-protective-mantras"
        image_path = "stories/images/putana_purification_gopis_mantras.jpg"

        story, created = Story.objects.get_or_create(
            slug=story_slug,
            defaults={
                "topic": topic,
                "order": 16,
                "imagePath": image_path,
            }
        )
        if not created:
            story.topic = topic
            story.order = 16
            story.imagePath = image_path
            story.save()

        stories_data = {
            "en": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "The Purification of Putana and the Gopīs' Protective Mantras",
                "content": """### The Gopīs Perform Sacred Go-rakṣā Rites

After rescuing baby Krishna from the mountainous chest of the dead witch Putana, Mother Yashoda, Mother Rohini, and the elderly cowherd women carried the child safely home to their courtyard. Although the divine infant was smiling happily and showed no sign of harm, the loving gopīs were trembling with anxiety. To counteract any lingering occult poison or demonic contamination, they immediately performed ancient Vedic protective rites centered upon the sacred cow (*Go-rakṣā*):

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 6, Verses 20–21**
> 
> *gomūtreṇa snāpayitvā go-rajasy avadhūlitam*  
> *rakṣāṁ cakrus tanau gopyaḥ śākiny-ādibhya ādṛtāḥ*  
> 
> **Translation:** "The cowherd women lovingly bathed baby Krishna in sacred cow urine, sprinkled His divine body with the auspicious dust raised from the cows' hooves, and carefully protected Him against evil spirits and witches by anointing His twelve limbs with the holy names of Lord Vishnu."

One gopi took the brush of a soft cow’s tail and waved it gently over baby Krishna to sweep away malevolent subtle energies. Mother Yashoda and Rohini bathed Him with cow urine, smeared His forehead and chest with cow dung, and sprinkled Him with sacred *go-dhūli* (dust raised by cow hooves).

Then, with hearts brimming with pure maternal devotion, the gopīs chanted the twelve transcendental names of Lord Vishnu to guard every limb of the child: "May Lord Keshava protect His legs; may Lord Govinda protect His knees; may Lord Madhava protect His thighs; may Lord Vaikuntha protect His belly; may Lord Madhusudana protect His heart; may Lord Hrishikesha protect His senses; and may Lord Damodara protect His entire divine body!"

Though baby Krishna is Himself the Supreme Personality of Godhead, the protector and sustainer of all cosmic universes, He happily submitted to the loving ministrations of His devotees. Mother Yashoda then took Him onto her lap and offered Him her own pure, nectarine breast milk, which the Lord drank with boundless joy.

### The Cremation of Putana's Colossal Corpse

Meanwhile, the cowherd men of Gokula assembled around the gigantic carcass of the demoness. Spanning twelve miles across pastures and forests, the enormous corpse could not easily be transported or buried. 

Armed with sharp axes and saws, the strong cowherd men chopped the monstrous corpse into pieces:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 6, Verses 34–35**
> 
> *kalevaraṁ paraśubhiś chittvā dāru-sañcayaiḥ*  
> *dāhayām āsuḥ sa-roṣā dūre gokula-vāsinaḥ*  
> 
> **Translation:** "Chopping her enormous body into pieces with axes, the residents of Gokula, filled with wrath, piled heaps of firewood upon the severed limbs and cremated the corpse far away in the distant pastures."

They gathered vast stacks of dry timber, placed the massive limbs of the demoness upon the funeral pyre, and set it ablaze.

### The Miracle of Fragrant Aguru Incense Smoke

As the pyre caught fire, an astonishing, mind-boggling miracle occurred. Normally, when the body of a demon, witch, or carnivore is cremated, the smoke emits a nauseating, foul stench. But as Putana’s body was consumed by flames, something completely transcendental took place:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 6, Verses 37–38**
> 
> *dagdhasyāpi śarīrasya dhūmaḥ saurabhyam uttamam*  
> *vavāha sarvato dikṣu sarva-loka-mano-haraḥ*  
> *pūtanā loka-bāla-ghnī rākṣasī rudhirāśanā*  
> *jighāṁsayāpi haraye stanaṁ dattvāpa sad-gatim*  
> 
> **Translation:** "As her body burned, thick plumes of smoke arose that emitted an exquisite, heavenly fragrance like the burning of aguru incense, charming everyone in every direction! Putana was a murderous witch and blood-drinking demoness; yet, because she offered her breast milk to Lord Hari—even with the evil intention to kill Him—she was cleansed of all sins and achieved the highest spiritual liberation!"

The entire atmosphere of Gokula and the surrounding forests became saturated with the sweet, divine aroma of burning aguru and sandalwood incense. The cowherds smelled the air in disbelief, looking at one another in sheer wonder.

### Nanda Maharaja's Return and the Lord's Boundless Mercy

Just at that moment, Nanda Maharaja and his cowherd companions returned from Mathura in their bullock carts. Approaching Gokula, they smelled the sweet aguru fragrance in the breeze and saw the gigantic remnants of the demoness lying in the pastures. 

When the cowherds related the entire harrowing pastime, Nanda Maharaja was spellbound. He immediately remembered the urgent, prophetic words that Sri Vasudeva had spoken to him in Mathura: *"Return to Gokula without delay, for great disasters are about to strike your son!"* With tears of gratitude streaming down his cheeks, Nanda praised Vasudeva’s spiritual vision and rushed to embrace his darling child.

Śrīla Prabhupāda explains the profound philosophical essence of this pastime: Putana was an envious, child-killing witch who came with deadly poison to murder the infant Lord. Yet, because she outwardly acted like a mother by offering her breast milk, the Supreme Personality of Godhead accepted only her external maternal service, completely disregarding her murderous intention. The Lord elevated her soul to Goloka Vrindavana to serve as an eternal nurse and foster mother!

If the Supreme Lord is so infinitely merciful that He grants the highest liberation to an envious witch who offered Him poison, what boundless spiritual reward will He bestow upon a sincere devotee who offers Him loving devotion with a pure heart?""",
                "questions": [
                    {
                        "question": "What sacred rites did the gopis perform to protect baby Krishna from demonic contamination?",
                        "options": [
                            {"text": "Go-raksa rites using sacred cow urine, cow dung, dust of cow hooves, and waving a cow's tail", "is_correct": True},
                            {"text": "Military weapon drills", "is_correct": False},
                            {"text": "Hiding Him inside an iron chest", "is_correct": False},
                            {"text": "Taking Him to a doctor in Mathura", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Whose sacred names did the gopis chant to protect each limb of baby Krishna's body?",
                        "options": [
                            {"text": "The transcendental names of Lord Vishnu (Kesava, Narayana, Madhava, Govinda, etc.)", "is_correct": True},
                            {"text": "The names of demigods like Indra and Agni", "is_correct": False},
                            {"text": "The names of royal kings of Mathura", "is_correct": False},
                            {"text": "The names of stars and planets", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How did the cowherds dispose of Putana's colossal twelve-mile corpse?",
                        "options": [
                            {"text": "They chopped it into pieces with axes and cremated it with firewood", "is_correct": True},
                            {"text": "They pushed it into the ocean", "is_correct": False},
                            {"text": "They buried it whole beneath a mountain", "is_correct": False},
                            {"text": "They left it in the village street", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What miraculous aroma arose from the smoke when Putana's body was cremated?",
                        "options": [
                            {"text": "The sweet, heavenly fragrance of aguru and sandalwood incense", "is_correct": True},
                            {"text": "A foul, poisonous sulfuric stench", "is_correct": False},
                            {"text": "The smell of burnt iron", "is_correct": False},
                            {"text": "No smoke or odor arose at all", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Why did Putana's cremation smoke smell sweetly like divine aguru incense?",
                        "options": [
                            {"text": "Because baby Krishna sucked her breast milk, purifying all her sins and sanctifying her body", "is_correct": True},
                            {"text": "Because the wood was soaked in perfume", "is_correct": False},
                            {"text": "Because the demigods sprayed rosewater from heaven", "is_correct": False},
                            {"text": "Because Putana had eaten sweet flowers before dying", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What exalted spiritual position did the Supreme Lord grant to Putana?",
                        "options": [
                            {"text": "The eternal position of a nurse and foster mother in the spiritual world", "is_correct": True},
                            {"text": "The post of King Indra in heaven", "is_correct": False},
                            {"text": "Rebirth as an earthly queen", "is_correct": False},
                            {"text": "She was sent to the darkest hell", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Even though Putana intended to kill Him, what aspect did the Lord mercifully accept?",
                        "options": [
                            {"text": "Her offering of breast milk, accepting her as an affectionate mother", "is_correct": True},
                            {"text": "Her magical disguise", "is_correct": False},
                            {"text": "Her relationship with King Kamsa", "is_correct": False},
                            {"text": "Her physical strength", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Who arrived in Gokula from Mathura just as the demoness's body was being cremated?",
                        "options": [
                            {"text": "Nanda Maharaja and his cowherd companions", "is_correct": True},
                            {"text": "King Kamsa and his army", "is_correct": False},
                            {"text": "Sage Narada Muni", "is_correct": False},
                            {"text": "Vasudeva and Devaki", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What did Nanda Maharaja recall upon seeing the gigantic fallen demoness?",
                        "options": [
                            {"text": "Vasudeva's urgent warning in Mathura that great calamities would strike Gokula", "is_correct": True},
                            {"text": "A dream he had seen years ago", "is_correct": False},
                            {"text": "The tax receipt from Kamsa", "is_correct": False},
                            {"text": "A folk tale told by village elders", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Which verses of Srimad-Bhagavatam Canto 10 Chapter 6 describe the sweet aguru fragrance of Putana's funeral pyre?",
                        "options": [
                            {"text": "Verses 37–38", "is_correct": True},
                            {"text": "Verses 1–2", "is_correct": False},
                            {"text": "Verses 15–16", "is_correct": False},
                            {"text": "Verses 43–44", "is_correct": False}
                        ]
                    }
                ]
            },
            "ta": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "பூதனையின் முக்தி மற்றும் கோபியரின் ரக்ஷா மந்திரங்கள்",
                "content": """### கோபியர் நிகழ்த்திய திவ்யமான கோ-ரக்ஷா வழிபாடு

பூதனையின் மலை போன்ற மார்பகத்திலிருந்து பால கிருஷ்ணரை மீட்டெடுத்த அன்னை யசோதையும், ரோஹிணியும், கோகுலத்துப் பெண்களும் குழந்தையைத் தங்கள் வீட்டு முற்றத்திற்குப் பாசத்தோடு தூக்கி வந்தனர். அந்தத் தெய்வக் குழந்தை புன்னகை பூத்த முகத்தோடு, எந்தத் தீங்கும் இன்றி விளங்கிய போதிலும், அன்னை யசோதையின் தாய் மனம் பதறியது. கொடிய அசுர நஞ்சும், தீய சக்திகளும் குழந்தையை அணுகாமல் இருப்பதற்காக, புனிதமான பசுவை மையமாகக் கொண்ட தொன்மையான *கோ-ரக்ஷா* சடங்குகளை அவர்கள் உடனடியாகச் செய்தனர்:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 6, சுலோகங்கள் 20–21**
> 
> *கோமூத்ரேண ஸ்நாபயித்வா கோ-ரஜஸ்ய அவதூலிதம்*  
> *ரக்ஷாம் சக்ருஸ் தனௌ கோப்ய: சாகின்ய-ஆதிப்ய ஆத்ருதா:*  
> 
> **பொருள்:** "கோபியர் பால கிருஷ்ணரை புனிதமான பசுவின் கோமியத்தால் நீராட்டி, பசுக்களின் குளம்புகளிலிருந்து கிளம்பிய மங்களகரமான கோதூளிப் புழுதியை அவரது திருமேனியில் தூவி, விஷ்ணு பகவானின் திருநாமங்களைக் கூறி குழந்தையின் பன்னிரண்டு அங்கங்களையும் பாதுகாக்கும் ரக்ஷா சடங்கினைச் செய்தனர்."

ஒரு மூதாட்டி பசுவின் மென்மையான வாலை எடுத்து, திருஷ்டிகளையும் தீய சக்திகளையும் போக்க பால கிருஷ்ணர் மீது வீசி ஆசீர்வதித்தாள். அன்னை யசோதையும் ரோஹிணியும் பசுஞ்சாணத்தை குழந்தையின் நெற்றியிலும் மார்பிலும் திலகமாக இட்டனர்; பசுக்களின் பாதத் தூசியை அவர் மீது தெளித்தனர்.

பின்னர், தூய தாய்மைப் பக்தியோடு அவர்கள் பகவான் ஸ்ரீ விஷ்ணுவின் பன்னிரண்டு திருநாமங்களை உச்சரித்து ரக்ஷா செய்தனர்: "கேசவ பகவான் குழந்தையின் கால்களைக் காப்பாராக; கோவிந்த பகவான் முழங்கால்களைக் காப்பாராக; மாதவ பகவான் தொடைகளைக் காப்பாராக; வைகுண்ட பகவான் வயிற்றைக் காப்பாராக; மதுசூதன பகவான் இதயத்தைக் காப்பாராக; ஹ்ருஷீகேச பகவான் புலன்களைக் காப்பாராக; தாமோதர பகவான் குழந்தையின் முழுத் திருமேனியையும் காப்பாராக!"

அனைத்து உலகங்களையும் காத்து ரட்சிக்கும் முழுமுதற் கடவுளான பகவான் கிருஷ்ணர், தம் தூய பக்தர்களின் தாய்மைப் பாசத்திற்குப் பணிந்து அனைத்தையும் அமைதியாக ஏற்றுக்கொண்டார். பின்னர் அன்னை யசோதை பால கிருஷ்ணரைத் தன் மடியில் கிடத்தி, அமிர்தம் போன்ற தன் தாய்ப்பாலைப் புகட்டினாள்; பகவானும் பேரானந்தத்தோடு அதைப் பருகினார்.

### பன்னிரண்டு மைல் பிரம்மாண்ட உடலைத் தீயிலிடுதல்

இதற்கிடையில், கோகுலத்து ஆயர்கள் பூதனையின் மாபெரும் சடலத்தின் அருகே கூடினர். பன்னிரண்டு மைல் தூரம் பரவிக் கிடந்த அந்த பிரம்மாண்ட உடலை எவராலும் எளிதில் புதைக்கவோ, அப்புறப்படுத்தவோ முடியவில்லை.

எனவே, ஆயர்கள் கூரிய கோடாரிகளையும் ரம்பங்களையும் கொண்டு அந்த அரக்கியின் சடலத்தைத் துண்டு துண்டாக வெட்டினர்:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 6, சுலோகங்கள் 34–35**
> 
> *கலேவரம் பரசுபி: சித்த்வா தாரு-ஸஞ்சயை:*  
> *தாஹயாம் ஆஸு: ஸ-ரோஷா தூரே கோகுல-வாஸின:*  
> 
> **பொருள்:** "கோபமுற்ற கோகுலத்து மக்கள் கோடாரிகளைக் கொண்டு பூதனையின் பிரம்மாண்டமான உடலைத் துண்டு துண்டாக வெட்டி, விறகுக் கட்டைகளைக் குவித்து, ஊருக்கு அப்பால் உள்ள மேய்ச்சல் நிலத்தில் வைத்து அவளைத் தகனம் செய்தனர்."

அவர்கள் ஏராளமான காய்ந்த மரக்கட்டைகளைக் குவித்து, அந்த அரக்கியின் உடற்பாகங்களை அதன் மீது அடுக்கித் தீ மூட்டினர்.

### அகில் மற்றும் சந்தன நறுமணம் கமழ்ந்த அற்புதம்

பூதனையின் சிதை எரியத் தொடங்கியபோது, காண்போரை மெய்சிலிர்க்க வைக்கும் ஒரு மாபெரும் அற்புதம் நிகழ்ந்தது. சாதாரணமாக ஒரு கொடிய அரக்கியின் சடலம் எரியும்போது தாங்க முடியாத பிண நாற்றமும், துர்நாற்றமுமே வீச வேண்டும். ஆனால், பூதனையின் உடல் எரிந்தபோது எங்கும் நிகழாத தெய்வீக அற்புதம் நிகழ்ந்தது:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 6, சுலோகங்கள் 37–38**
> 
> *தக்தஸ்யாபி சரீரஸ்ய தூம: ஸௌரப்யம் உத்தமம்*  
> *வவாஹ ஸர்வதோ திக்ஷு ஸர்வ-லோக-மனோ-ஹர:*  
> *பூதனா லோக-பால-க்னீ ராக்ஷஸீ ருதிராஸனா*  
> *ஜிகாம்ஸயாபி ஹரயே ஸ்தனம் தத்த்வாப ஸத்-கதிம்*  
> 
> **பொருள்:** "எரியும் அவளுடைய உடலிலிருந்து கிளம்பிய அடர்ந்த புகையானது, அகில் மற்றும் சந்தன நறுமணத்தைப் பரப்பி அனைத்து திசைகளிலும் உள்ளோரின் மனதை மயக்கியது! பூதனை குழந்தைகளைக் கொல்லும் இரத்த வெறி பிடித்த அரக்கியாக இருந்தபோதிலும், கொலை செய்யும் வஞ்சக நோக்கத்தோடு வந்திருந்தாலும், பகவான் ஸ்ரீ ஹரிக்குத் தன் தாய்ப்பாலை அளித்த காரணத்தினால், அவள் அனைத்துப் பாவங்களும் நீங்கி உன்னதமான முக்தியை அடைந்தாள்!"

கோகுலமும் அதைச் சுற்றியுள்ள காடுகளும் முழுவதும் அகில், சாம்பிராணி மற்றும் சந்தன நறுமணத்தால் நிறைந்தது. அந்த நறுமணத்தை நுகர்ந்த ஆயர்கள் ஆச்சரியத்தில் திளைத்து ஒருவரை ஒருவர் பார்த்தனர்.

### நந்த மகாராஜரின் வருகையும் பகவானின் எல்லையற்ற கருணையும்

சரியாக அந்த நேரத்தில், மதுராவில் வரி செலுத்தி முடித்த நந்த மகாராஜர் தம் ஆயர்களுடன் மாட்டு வண்டிகளில் கோகுலத்திற்குத் திரும்பினார். காற்றில் கமழ்ந்த அகில் நறுமணத்தையும், மேய்ச்சல் நிலத்தில் கிடந்த அரக்கியின் மாபெரும் உடலையும் கண்டு அவர் திகைத்தார்.

நடந்த விபரீதங்களை மக்கள் விவரித்த போது, நந்த மகாராஜர் வசுதேவர் மதுராவில் தன்னிடம் கூறிய தீர்க்கதரிசன எச்சரிக்கையை நினைவுகூர்ந்தார்: *"கோகுலத்திற்கு உடனே புறப்படுங்கள்; உங்கள் குழந்தைக்குப் பெரும் ஆபத்து வரக்கூடும்!"* வசுதேவரின் தெய்வீக ஞானத்தை எண்ணி ஆனந்தக் கண்ணீர் வடித்த நந்தர், ஓடிவந்து தம் செல்வக் குழந்தையைக் கட்டித் தழுவிக்கொண்டார்.

ஸ்ரீல பிரபுபாதர் விளக்குகிறார்: பூதனை பச்சிளங்குழந்தைகளைக் கொல்லும் அரக்கி; பகவானைக் கொல்ல நஞ்சோடு வந்தவள். ஆயினும், அவள் ஒரு தாய் போல நடித்துப் பாலூட்டிய ஒரே ஒரு பாவனையை மட்டுமே பகவான் கருத்தில் கொண்டார்! அவளது கொலைவெறியைப் புறந்தள்ளி, அவளுக்குத் தன் ஆன்மீக லோகமான கோலோக பிருந்தாவனத்தில் நிரந்தர செவிலித்தாய் மற்றும் அன்னையின் ஸ்தானத்தை பகவான் வழங்கிவிட்டார்!

கொலை செய்யும் நோக்கோடு நஞ்சூட்டிய அரக்கிக்கே பகவான் இத்தகைய உன்னத முக்தியைத் தருகிறார் என்றால், தூய அன்போடு பகவானை வணங்கும் உண்மை பக்தர்களுக்கு அவர் எத்தகைய பேரின்பத்தை அருள்வார்!""",
                "questions": [
                    {
                        "question": "பூதனையின் உடலிலிருந்து குழந்தையை மீட்ட பின் கோபியர் செய்த ரக்ஷா சடங்கு எது?",
                        "options": [
                            {"text": "பசுவின் கோமியம், சாணம், கோதூளிப் புழுதி மற்றும் பசுவின் வால் கொண்டு செய்த கோ-ரக்ஷா வழிபாடு", "is_correct": True},
                            {"text": "ஆயுதப் பயிற்சி", "is_correct": False},
                            {"text": "இரும்புப் பெட்டியில் பூட்டி வைத்தல்", "is_correct": False},
                            {"text": "மதுராவில் உள்ள மருத்துவரிடம் அழைத்துச் செல்லுதல்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பால கிருஷ்ணரின் உடற்பாகங்களைப் பாதுகாக்க கோபியர் யாருடைய திருநாமங்களை உச்சரித்தனர்?",
                        "options": [
                            {"text": "விஷ்ணு பகவானின் திருநாமங்களை (கேசவ, நாராயண, மாதவ, கோவிந்த)", "is_correct": True},
                            {"text": "இந்திரன் மற்றும் அக்னியின் பெயர்களை", "is_correct": False},
                            {"text": "மதுரா நாட்டு அரசர்களின் பெயர்களை", "is_correct": False},
                            {"text": "நட்சத்திரங்களின் பெயர்களை", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பன்னிரண்டு மைல் நீளமுள்ள பூதனையின் சடலத்தை ஆயர்கள் என்ன செய்தனர்?",
                        "options": [
                            {"text": "கோடாரிகளால் துண்டு துண்டாக வெட்டி விறகுகளைக் குவித்துத் தகனம் செய்தனர்", "is_correct": True},
                            {"text": "கடலில் வீசினர்", "is_correct": False},
                            {"text": "மலையடிவாரத்தில் முழுமையாகப் புதைத்தனர்", "is_correct": False},
                            {"text": "தெருவிலேயே விட்டுவிட்டனர்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பூதனையின் சிதை எரிந்த போது எத்தகைய நறுமணம் கிளம்பியது?",
                        "options": [
                            {"text": "அகில் மற்றும் சந்தனம் போன்ற தெய்வீக நறுமணம்", "is_correct": True},
                            {"text": "தாங்க முடியாத துர்நாற்றம்", "is_correct": False},
                            {"text": "இரும்பு எரியும் வாசனை", "is_correct": False},
                            {"text": "புகையோ வாசனையோ வரவில்லை", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பூதனையின் உடல் எரிந்த போது அகில் நறுமணம் வீசியதற்குக் காரணம் என்ன?",
                        "options": [
                            {"text": "பகவான் கிருஷ்ணர் அவளது பாலைக் குடித்ததால் அவளது பாவங்கள் நீங்கி உடல் புனிதமானது", "is_correct": True},
                            {"text": "விறகுகளில் நறுமணத் தைலம் ஊற்றப்பட்டிருந்தது", "is_correct": False},
                            {"text": "தேவர்கள் பன்னீர் தெளித்தனர்", "is_correct": False},
                            {"text": "பூதனை மலர்களை உண்டிருந்தாள்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பூதனைக்கு பகவான் கிருஷ்ணர் எத்தகைய உன்னத ஆன்மீக ஸ்தானத்தை வழங்கினார்?",
                        "options": [
                            {"text": "ஆன்மீக லோகத்தில் தாய் மற்றும் செவிலித்தாய் என்னும் நிரந்தர ஸ்தானம்", "is_correct": True},
                            {"text": "சுவர்க்கத்தில் இந்திர பதவி", "is_correct": False},
                            {"text": "பூலோகத்தில் ஒரு ராணியாகப் பிறக்கும் வரம்", "is_correct": False},
                            {"text": "அவளை நரகத்திற்கு அனுப்பினார்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பூதனை கொல்லும் நோக்கோடு வந்த போதிலும் பகவான் எதை மட்டுமே கருத்தில் கொண்டார்?",
                        "options": [
                            {"text": "அவள் ஒரு தாய் போலப் பாலூட்டிய சேவையை மட்டுமே", "is_correct": True},
                            {"text": "அவளது அழகிய மாறுவேடத்தை", "is_correct": False},
                            {"text": "கம்சனுடனான அவளது உறவை", "is_correct": False},
                            {"text": "அவளது உடல் வலிமையை", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பூதனையின் உடல் தகனம் செய்யப்படும் போது மதுராவிலிருந்து கோகுலத்திற்குத் திரும்பியவர் யார்?",
                        "options": [
                            {"text": "நந்த மகாராஜர் மற்றும் ஆயர்கள்", "is_correct": True},
                            {"text": "கம்சனும் அவனது படைகளும்", "is_correct": False},
                            {"text": "நாரத முனிவர்", "is_correct": False},
                            {"text": "வசுதேவரும் தேவகியும்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "அரக்கியின் சடலத்தைக் கண்ட நந்த மகாராஜர் யாருடைய எச்சரிக்கையை நினைவுகூர்ந்தார்?",
                        "options": [
                            {"text": "மதுராவில் வசுதேவர் கூறிய தீர்க்கதரிசன எச்சரிக்கையை", "is_correct": True},
                            {"text": "முன்னொரு காலத்தில் கண்ட கனவை", "is_correct": False},
                            {"text": "கம்சன் அளித்த வரி ரசீதை", "is_correct": False},
                            {"text": "கிராமத்துப் பெரியவர்களின் கதையை", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பூதனையின் உடலிலிருந்து அகில் நறுமணம் கிளம்பியதை விவரிக்கும் பாகவத சுலோகங்கள் எவை?",
                        "options": [
                            {"text": "சுலோகங்கள் 37–38", "is_correct": True},
                            {"text": "சுலோகங்கள் 1–2", "is_correct": False},
                            {"text": "சுலோகங்கள் 15–16", "is_correct": False},
                            {"text": "சுலோகங்கள் 43–44", "is_correct": False}
                        ]
                    }
                ]
            },
            "hi": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "पूतना की मुक्ति और गोपियों द्वारा रक्षा-विधान",
                "content": """### गोपियों द्वारा पवित्र गो-रक्षा विधान

पूतना की छाती से बालकृष्ण को उठाकर माता यशोदा, रोहिणी और वृद्ध गोपियां बालक को तुरंत घर के आंगन में ले आईं। यद्यपि बालकृष्ण मंद-मंद मुस्कुरा रहे थे और उन्हें कोई चोट नहीं पहुंची थी, फिर भी वात्सल्यमयी माताओं का हृदय कांप रहा था। किसी भी आसुरी अमंगल को दूर करने के लिए गोपियों ने तुरंत पवित्र गाय से जुड़े वैदिक रक्षा-विधान (*गो-रक्षा*) संपन्न किए:

> **श्रीमद्-भागवतम, स्कंध 10, अध्याय 6, श्लोक 20–21**
> 
> *गोमूत्रेण स्नापयित्वा गोरजस्य अवधूलितम्*  
> *रक्षां चक्रुस्तनौ गोप्यः शाकिन्यादिभ्य आदृताः*  
> 
> **भावार्थ:** "गोपियों ने बालकृष्ण को पवित्र गोमूत्र से स्नान कराया, गायों के खुरों से उड़ी गोधूलि से उनके श्रीअंग को पवित्र किया और भगवान विष्णु के पवित्र नामों का उच्चारण करते हुए उनके बारह अंगों की रक्षा की।"

एक गोपी ने गाय की पूंछ का चंवर बनाकर बालक के ऊपर फेरा ताकि सारी बुरी दृष्टि दूर हो जाए। माता यशोदा ने गोमय (गोबर) से बालक के ललाट और वक्ष पर तिलक लगाया और गोधूलि से उनका अभिषेक किया।

इसके बाद गोपियों ने परम वात्सल्य भाव से भगवान विष्णु के बारह नामों का उच्चारण करते हुए अंग-रक्षा की: "भगवान केशव पैरों की रक्षा करें, गोविंद घुटनों की रक्षा करें, माधव जांघों की रक्षा करें, वैकुंठ उदर की रक्षा करें, मधुसूदन हृदय की रक्षा करें, हृषीकेश इंद्रियों की रक्षा करें और दामोदर बालक के संपूर्ण शरीर की रक्षा करें!"

समस्त ब्रह्मांडों के पालनहार भगवान श्रीकृष्ण ने अपनी माताओं के इस वात्सल्य प्रेम को बड़े आदर से स्वीकार किया। इसके बाद माता यशोदा ने बालक को अपनी गोद में लेकर अपना अमृतमय स्तनपान कराया, जिसे भगवान ने परम आनंद से पिया।

### पूतना के बारह मील लंबे शव का दाह-संस्कार

इधर गोकुल के ग्वाले पूतना के उस विशालकाय शव के पास एकत्र हुए। बारह मील लंबे उस पर्वताकार शव को न तो दबाया जा सकता था और न ही कहीं ले जाया जा सकता था। 

अतः ग्वालों ने कुल्हाड़ियों और आ Tapi से उस विशाल शरीर के टुकड़े-टुकड़े कर दिए:

> **श्रीमद्-भागवतम, स्कंध 10, अध्याय 6, श्लोक 34–35**
> 
> *कलेवरं परशुभिश्छित्त्वा दारुसञ्चयैः*  
> *दाहयामासुः सरोषा दूरे गोकुलवासिनः*  
> 
> **भावार्थ:** "क्रोधित गोकुलवासियों ने कुल्हाड़ियों से पूतना के विशाल शरीर के टुकड़े किए और लकड़ियों का ढेर लगाकर बस्ती से दूर उस शव का दाह-संस्कार किया।"

उन्होंने प्रचुर मात्रा में लकड़ियां एकत्र करके उस चिता में अग्नि प्रज्वलित की।

### अगरु और चंदन की अलौकिक सुगंध का चमत्कार

जैसे ही चिता में अग्नि धधकी, एक अभूतपूर्व चमत्कार हुआ। साधारणतः किसी राक्षसी या हिंसक प्राणी के शव के जलने पर अत्यंत असह्य दुर्गंध फैलती है। किंतु पूतना की चिता से जो धुआं उठा, वह सर्वथा दिव्य था:

> **श्रीमद्-भागवतम, स्कंध 10, अध्याय 6, श्लोक 37–38**
> 
> *दग्धस्यापि शरीरस्य धूमः सौरभ्यमुत्तमम्*  
> *ववाह सर्वतो दिक्षु सर्वलोकमनोहरः*  
> *पूतना लोकबालघ्नी राक्षसी रुधिराशना*  
> *जिघांसयापि हरये स्तनं दत्त्वाप सद्गतिम्*  
> 
> **भावार्थ:** "उसके जलते हुए शरीर से उठने वाला धुआं अगरु और चंदन जैसी सर्वोत्तम सुगंध से महक उठा, जिसने दसों दिशाओं के लोगों को मुग्ध कर दिया! पूतना बालघातिनी और रक्त पीने वाली राक्षसी थी; फिर भी, केवल भगवान को स्तनपान कराने के कारण—यद्यपि वह मारने आई थी—उसे परम गति (मुक्ति) प्राप्त हो गई!"

समस्त गोकुल और आसपास के वन अगरु और चंदन की सुगंध से सुवासित हो उठे। ग्वाले चकित होकर उस सुगंध को सूंघने लगे।

### नंद महाराज का आगमन और भगवान की अहैतुकी कृपा

उसी समय नंद महाराज मथुरा से कर चुकाकर अपनी गाड़ियों के साथ गोकुल लौटे। उन्होंने मार्ग में ही अगरु की दिव्य सुगंध का अनुभव किया और चारागाह में विशाल शव को देखा।

जब लोगों ने पूरी घटना सुनाई, तो नंद महाराज स्तब्ध रह गए। उन्हें तुरंत मथुरा में वसुदेव जी द्वारा दी गई चेतावनी स्मरण हो आई: *"गोकुल तुरंत लौट जाओ, क्योंकि वहां अनिष्ट होने वाला है!"* वसुदेव जी की दिव्य दृष्टि की सराहना करते हुए नंद महाराज दौड़कर आए और बालक कृष्ण को गले से लगा लिया।

श्रील प्रभुपाद समझाते हैं: पूतना कालकूट विष देकर बालक की हत्या करने आई थी। किंतु क्योंकि उसने बाहर से माता का रूप धरकर स्तनपान कराया था, भगवान ने उसके कपट को भुलाकर केवल उसकी उस मातृवत सेवा को स्वीकार किया और उसे गोलोक वृंदावन में धात्री (माता) का नित्य पद प्रदान किया!

यदि विष पिलाने वाली राक्षसी को भगवान परम गति दे सकते हैं, तो शुद्ध भाव से प्रेम करने वाले निष्कपट भक्त को भगवान क्या कुछ नहीं देंगे!""",
                "questions": [
                    {
                        "question": "पूतना के शरीर से बालक को लाने के बाद गोपियों ने कौन सा रक्षा-विधान किया?",
                        "options": [
                            {"text": "गोमूत्र, गोबर, गोधूलि और गाय की पूंछ से गो-रक्षा विधान", "is_correct": True},
                            {"text": "शस्त्र अभ्यास", "is_correct": False},
                            {"text": "लोहे के बक्से में बंद करना", "is_correct": False},
                            {"text": "मथुरा के वैद्य के पास ले जाना", "is_correct": False}
                        ]
                    },
                    {
                        "question": "बालकृष्ण के अंगों की रक्षा के लिए गोपियों ने किनके नामों का उच्चारण किया?",
                        "options": [
                            {"text": "भगवान विष्णु के नामों का (केशव, नारायण, माधव, गोविंद)", "is_correct": True},
                            {"text": "इंद्र और अग्नि के नामों का", "is_correct": False},
                            {"text": "मथुरा के राजाओं के नामों का", "is_correct": False},
                            {"text": "नक्षत्रों के नामों का", "is_correct": False}
                        ]
                    },
                    {
                        "question": "पूतना के बारह मील लंबे शव का ग्वालों ने क्या किया?",
                        "options": [
                            {"text": "कुल्हाड़ियों से टुकड़े करके लकड़ियों पर जला दिया", "is_correct": True},
                            {"text": "समुद्र में बहा दिया", "is_correct": False},
                            {"text": "पहाड़ के नीचे दबा दिया", "is_correct": False},
                            {"text": "गली में छोड़ दिया", "is_correct": False}
                        ]
                    },
                    {
                        "question": "पूतना के जलते शरीर के धुएं से कैसी सुगंध निकली?",
                        "options": [
                            {"text": "अगरु और चंदन जैसी दिव्य सुगंध", "is_correct": True},
                            {"text": "असह्य दुर्गंध", "is_correct": False},
                            {"text": "लोहे के जलने की गंध", "is_correct": False},
                            {"text": "कोई गंध नहीं निकली", "is_correct": False}
                        ]
                    },
                    {
                        "question": "पूतना के शव से अगरु की सुगंध क्यों निकली?",
                        "options": [
                            {"text": "क्योंकि भगवान कृष्ण ने उसका स्तनपान करके उसके समस्त पाप धो दिए थे", "is_correct": True},
                            {"text": "क्योंकि लकड़ियों पर इत्र डाला गया था", "is_correct": False},
                            {"text": "क्योंकि देवताओं ने गुलाब जल छिड़का था", "is_correct": False},
                            {"text": "क्योंकि पूतना ने फूल खाए थे", "is_correct": False}
                        ]
                    },
                    {
                        "question": "भगवान श्रीकृष्ण ने पूतना को कौन सा आध्यात्मिक पद प्रदान किया?",
                        "options": [
                            {"text": "गोलोक में धात्री (माता) का नित्य पद", "is_correct": True},
                            {"text": "स्वर्ग में इंद्राणी का पद", "is_correct": False},
                            {"text": "पृथ्वी पर रानी बनने का वरदान", "is_correct": False},
                            {"text": "घोर नर्क भेजा", "is_correct": False}
                        ]
                    },
                    {
                        "question": "पूतना के मारने आने पर भी भगवान ने उसकी किस बात को स्वीकार किया?",
                        "options": [
                            {"text": "माता के समान स्तनपान कराने की बाह्य सेवा को", "is_correct": True},
                            {"text": "उसके सुंदर रूप को", "is_correct": False},
                            {"text": "कंस से उसकी मित्रता को", "is_correct": False},
                            {"text": "उसकी शारीरिक शक्ति को", "is_correct": False}
                        ]
                    },
                    {
                        "question": "पूतना के दाह-संस्कार के समय मथुरा से गोकुल कौन लौटा?",
                        "options": [
                            {"text": "नंद महाराज और उनके साथी ग्वाले", "is_correct": True},
                            {"text": "कंस और उसकी सेना", "is_correct": False},
                            {"text": "नारद मुनि", "is_correct": False},
                            {"text": "वसुदेव और देवकी", "is_correct": False}
                        ]
                    },
                    {
                        "question": "शव देखकर नंद महाराज को किसकी चेतावनी याद आई?",
                        "options": [
                            {"text": "मथुरा में वसुदेव जी द्वारा दी गई चेतावनी", "is_correct": True},
                            {"text": "एक पुराने सपने की बात", "is_correct": False},
                            {"text": "कंस की कर रसीद", "is_correct": False},
                            {"text": "गांव के वृद्धों की बात", "is_correct": False}
                        ]
                    },
                    {
                        "question": "पूतना की चिता से अगरु की सुगंध का वर्णन भागवतम के किन श्लोकों में है?",
                        "options": [
                            {"text": "श्लोक 37–38", "is_correct": True},
                            {"text": "श्लोक 1–2", "is_correct": False},
                            {"text": "श्लोक 15–16", "is_correct": False},
                            {"text": "श्लोक 43–44", "is_correct": False}
                        ]
                    }
                ]
            },
            "bn": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "পূতনার মুক্তি ও গোপীদের গো-রক্ষা মন্ত্র",
                "content": """### গোপীদের গো-রক্ষা ও বিষ্ণুর নাম-সুরক্ষা

পূতনার বিশাল বক্ষস্থল থেকে শ্রীকৃষ্ণকে উদ্ধার করে মা যশোদা, রোহিণী এবং বৃদ্ধা গোপীগণ শিশুকে ঘরের আঙিনায় নিয়ে এলেন। শিশু কৃষ্ণ হাসিমুখে থাকলেও মাতৃহৃদয় আশঙ্কায় কাঁপছিল। কোনো অপদেবতা বা আসুরিক প্রভাব যাতে শিশুকে স্পর্শ করতে না পারে, সেজন্য তাঁরা অবিলম্বে পবিত্র গাভীকে কেন্দ্র করে বৈদিক *গো-রক্ষা* বিধান সম্পন্ন করলেন:

> **শ্রীমদ্ভাগবতম, স্কন্ধ ১০, অধ্যায় ৬, শ্লোক ২০–২১**
> 
> *গোমূত্রেণ স্নাপয়িত্বা গোরজস্য অবধূলিতম্*  
> *রক্ষাং চক্রুস্তনৌ গোপ্যঃ শাকিন্যাদিভ্য আদৃতাঃ*  
> 
> **অনুবাদ:** "গোপীগণ শিশু শ্রীকৃষ্ণকে পবিত্র গোমূত্র দ্বারা স্নান করালেন, গাভীদের খুরোত্থিত গোরেণু দ্বারা তাঁর অঙ্গ মার্জনা করলেন এবং ভগবান বিষ্ণুর দ্বাদশ নাম উচ্চারণ করে তাঁর অঙ্গসমূহ রক্ষা করলেন।"

এক বৃদ্ধা গোপী গাভীর নরম লেজের চামর বুলিয়ে শিশুর সমস্ত অমঙ্গল দূর করলেন। মা যশোদা গোময় দ্বারা তাঁর কপালে তিলক আঁকলেন।

অতঃপর গোপীগণ বাৎসল্য প্রেমে ভগবান বিষ্ণুর বারোটি নাম উচ্চারণ করে অঙ্গরক্ষা করলেন: "কেশব চরণে রক্ষা করুন, গোবিন্দ জানুদ্বয় রক্ষা করুন, মাধব ঊরু রক্ষা করুন, বৈকুণ্ঠ উদর রক্ষা করুন, মধুসূদন হৃদয় রক্ষা করুন, হৃষীকেশ ইন্দ্রিয় রক্ষা করুন এবং দামোদর সমগ্র শরীর রক্ষা করুন!"

সমগ্র সৃষ্টির অধিপতি শ্রীকৃষ্ণ তাঁর ভক্তিমতী মায়েদের এই সরল ভালোবাসা মাথা পেতে নিলেন। এরপর মা যশোদা তাঁকে কোলে তুলে অমৃতসমান স্তনদুগ্ধ পান করালেন।

### বারো মাইল দীর্ঘ দানবীয় দেহের সৎকার

এদিকে ব্রজবাসীরা পূতনার বারো মাইল দীর্ঘ পর্বতপ্রমাণ শবদেহের কাছে সমবেত হলেন। এত বিশাল দেহ সমাধি দেওয়া অসম্ভব ছিল। 

তাই ব্রজবাসীরা কুঠার দ্বারা সেই বিশাল শরীর খণ্ড খণ্ড করে কেটে ফেললেন:

> **শ্রীমদ্ভাগবতম, স্কন্ধ ১০, অধ্যায় ৬, শ্লোক ৩৪–৩৫**
> 
> *কলেবরং পরশুভিশ্ছিত্ত্বা দারুসঞ্চয়ৈঃ*  
> *দাহয়ামাসুঃ সরোষা দূরে গোকুলবাসিনঃ*  
> 
> **অনুবাদ:** "ক্রোধোন্মত্ত গোকুলবাসীরা কুঠার দিয়ে পূতনার বিশাল দেহ খণ্ড খণ্ড করে কাটলেন এবং দূরে প্রান্তরে কাষ্ঠের স্তূপ তৈরি করে সেই দেহ দাহ করলেন।"

তাঁরা বিপুল পরিমাণ কাষ্ঠ স্তূপীকৃত করে সেই চিতায় অগ্নিসংযোগ করলেন।

### অগুরু ও চন্দনের দিব্য সুবাসের অলৌকিক ঘটনা

চিতায় অগ্নি প্রজ্বলিত হতেই এক অচিন্ত্যনীয় অলৌকিক ঘটনা ঘটল। সাধারণত কোনো রাক্ষসী বা পশুর মৃতদেহ দগ্ধ হলে বিকট দুর্গন্ধ ছড়ায়। কিন্তু পূতনার চিতা থেকে যে ধোঁয়া উঠল, তা ছিল সম্পূর্ণ অপ্রাকৃত:

> **শ্রীমদ্ভাগবতম, স্কন্ধ ১০, অধ্যায় ৬, শ্লোক ৩৭–৩৮**
> 
> *দগ্ধস্যাপি শরীরস্য ধূমঃ সৌরভ্যমুত্তমম্*  
> *ববাহ সর্বতো दिक्ষু সর্বলোকমোহরঃ*  
> *পূতনা লোকবালঘ্নী রাক্ষসী রুধিরাশনা*  
> *জিঘাংসয়াপি হরয়ে স্তনং দত্ত্বাপ সদ্গতিম্*  
> 
> **অনুবাদ:** "তার জ্বলন্ত দেহ থেকে উত্থিত ধোঁয়া অগুরু ও চন্দনের ন্যায় দিব্য সুবাসে চতুর্দিক আমোদিত করে তুলল! পূতনা ছিল রক্তপায়ী নরঘাতিনী রাক্ষসী; তথাপি শ্রীহরিকে স্তনদুগ্ধ দানের কারণে—যদিও সে মারার জন্যই এসেছিল—সে পরম গতি (মুক্তি) লাভ করল!"

সমগ্র গোকুল অগুরু ও চন্দনের স্নিগ্ধ সুগন্ধে ভরে গেল। ব্রজবাসীরা বিস্মিত নয়নে পরস্পরকে দেখতে লাগলেন।

### নন্দ মহারাজের প্রত্যাবর্তন ও ভগবানের অহৈতুকী কৃপা

ঠিক সেই সময় নন্দ মহারাজ মথুরায় কর প্রদান করে গোকুলে ফিরলেন। বাতাসে সেই দিব্য অগুরু সুবাস এবং প্রান্তরে সেই বিশাল শবের অংশ দেখে তিনি বিস্মিত হলেন।

গ্রামবাসীদের মুখে সমস্ত ঘটনা শুনে নন্দ মহারাজ স্তব্ধ হয়ে গেলেন। তাঁর মনে পড়ল মথুরায় বসুদেবের সেই সতর্কবাণী: *"গোকুলে দ্রুত ফিরে যাও, কারণ সেখানে অমঙ্গল দেখা দিতে পারে!"* বসুদেবের আধ্যাত্মিক দূরদর্শিতার প্রশংসা করে নন্দ মহারাজ ছুটে এসে শিশু কৃষ্ণকে বুকে জড়িয়ে নিলেন।

শ্রীল প্রভুপাদ ব্যাখ্যা করেছেন: পূতনা এসেছিল কালকূট বিষ দিয়ে শিশুকে হত্যা করতে। কিন্তু সে মাতার বেশে স্তনদান করেছিল বলে দয়ালু শ্রীকৃষ্ণ তার কুৎসিত অভিপ্রায় ভুলে গিয়ে কেবল তার স্তনদানটুকুই গ্রহণ করলেন এবং তাকে নিত্য বৈকুণ্ঠধামে জননীর সমান ধাত্রী পদ দান করলেন!

যে ভগবান বিষদানকারী রাক্ষসীকেও পরম মুক্তি দেন, সেই প্রেমময় ভগবানকে যদি কেউ ভক্তিভরে ভালোবাসে, তবে তিনি তাকে কী না দেবেন!""",
                "questions": [
                    {
                        "question": "পূতনার বক্ষ থেকে উদ্ধারের পর গোপীরা কোন রক্ষা-বিধান করেছিলেন?",
                        "options": [
                            {"text": "গোমূত্র, গোময়, গোরেণু ও গাভীর লেজ দিয়ে গো-রক্ষা বিধান", "is_correct": True},
                            {"text": "অস্ত্র চালনা", "is_correct": False},
                            {"text": "বাক্সে বন্দি করা", "is_correct": False},
                            {"text": "মথুরার চিকিৎসকের কাছে নিয়ে যাওয়া", "is_correct": False}
                        ]
                    },
                    {
                        "question": "শ্রীকৃষ্ণের অঙ্গ রক্ষার জন্য গোপীরা কার নাম উচ্চারণ করেছিলেন?",
                        "options": [
                            {"text": "ভগবান বিষ্ণুর নাম (কেশব, নারায়ণ, মাধব, গোবিন্দ)", "is_correct": True},
                            {"text": "ইন্দ্র ও অগ্নির নাম", "is_correct": False},
                            {"text": "মথুরার রাজাদের নাম", "is_correct": False},
                            {"text": "গ্রহ-নক্ষত্রের নাম", "is_correct": False}
                        ]
                    },
                    {
                        "question": "পূতনার বারো মাইল দীর্ঘ দেহের কী ব্যবস্থা করা হয়েছিল?",
                        "options": [
                            {"text": "কুঠার দিয়ে কেটে কাষ্ঠের চিতায় দাহ করা হয়েছিল", "is_correct": True},
                            {"text": "সমুদ্রে ভাসিয়ে দেওয়া হয়েছিল", "is_correct": False},
                            {"text": "মাটিতে পুঁতে ফেলা হয়েছিল", "is_correct": False},
                            {"text": "রাস্তায় ফেলে রাখা হয়েছিল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "পূতনার চিতাগ্নি থেকে কেমন সুবাস নির্গত হয়েছিল?",
                        "options": [
                            {"text": "অগুরু ও চন্দনের মতো দিব্য সুবাস", "is_correct": True},
                            {"text": "তীব্র দুর্গন্ধ", "is_correct": False},
                            {"text": "লোহা পোড়ার গন্ধ", "is_correct": False},
                            {"text": "কোনো গন্ধ বের হয়নি", "is_correct": False}
                        ]
                    },
                    {
                        "question": "পূতনার শরীর থেকে অগুরু সুবাস নির্গত হওয়ার কারণ কী ছিল?",
                        "options": [
                            {"text": "শ্রীকৃষ্ণ স্তনপান করে তার সমস্ত পাপ ধৌত করে দিয়েছিলেন", "is_correct": True},
                            {"text": "কাঠে সুগন্ধি তেল দেওয়া হয়েছিল", "is_correct": False},
                            {"text": "দেবতারা গোলাপজল ছিটিয়েছিলেন", "is_correct": False},
                            {"text": "পূতনা সুগন্ধি ফুল খেয়েছিল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ভগবান শ্রীকৃষ্ণ পূতনাকে কোন আধ্যাত্মিক স্থান দান করলেন?",
                        "options": [
                            {"text": "গোলোকে চিরন্তন ধাত্রী মাতার স্থান", "is_correct": True},
                            {"text": "স্বর্গের ইন্দ্রাণী পদ", "is_correct": False},
                            {"text": "পৃথিবীর রানি হওয়ার বর", "is_correct": False},
                            {"text": "নরকে নিক্ষেপ করলেন", "is_correct": False}
                        ]
                    },
                    {
                        "question": "পূতনার অসৎ উদ্দেশ্য সত্ত্বেও ভগবান তার কোন বিষয়টিকে গ্রহণ করেছিলেন?",
                        "options": [
                            {"text": "মাতার মতো স্তনদানের বাহ্যিক সেবাকে", "is_correct": True},
                            {"text": "তার সুন্দর রূপকে", "is_correct": False},
                            {"text": "কংসের সাথে তার বন্ধুত্বকে", "is_correct": False},
                            {"text": "তার শারীরিক বলকে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "পূতনার সৎকারকালে মথুরা থেকে কে ফিরেছিলেন?",
                        "options": [
                            {"text": "নন্দ মহারাজ ও ব্রজবাসীরা", "is_correct": True},
                            {"text": "কংস ও তার বাহিনী", "is_correct": False},
                            {"text": "নারদ মুনি", "is_correct": False},
                            {"text": "বসুদেব ও দেবকী", "is_correct": False}
                        ]
                    },
                    {
                        "question": "মৃতদেহ দেখে নন্দ মহারাজের কার সতর্কবাণী মনে পড়েছিল?",
                        "options": [
                            {"text": "মথুরায় বসুদেবের সতর্কবাণী", "is_correct": True},
                            {"text": "একটি স্বপ্নের কথা", "is_correct": False},
                            {"text": "কংসের কর রসিদ", "is_correct": False},
                            {"text": "গ্রামের প্রবীণদের কথা", "is_correct": False}
                        ]
                    },
                    {
                        "question": "পূতনার চিতা থেকে অগুরু সুবাসের বিবরণ ভাগবতের কোন শ্লোকে আছে?",
                        "options": [
                            {"text": "শ্লোক ৩৭–৩৮", "is_correct": True},
                            {"text": "শ্লোক ১–২", "is_correct": False},
                            {"text": "শ্লোক ১৫–১৬", "is_correct": False},
                            {"text": "শ্লোক ৪৩–৪৪", "is_correct": False}
                        ]
                    }
                ]
            },
            "te": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "పూతనకు మోక్షం మరియు గోపికల రక్షా మంత్రాలు",
                "content": """### గోపికల గో-రక్షా విధానం

పూతన భయంకర వక్షస్థలంపై నుండి చిన్ని కృష్ణుడిని ఎత్తుకుని యశోద, రోహిణి, వృద్ధ గోపికలు ఇంటి ప్రాంగణానికి తీసుకువచ్చారు. ఆ పరమాత్ముడు నవ్వుతూ నిక్షేపంగా ఉన్నప్పటికీ, మాతృహృదయం భయంతో వణికిపోయింది. ఎలాంటి ఆసురీ శక్తులు బిడ్డను తాకకుండా ఉండేందుకు గోమాతను ఆశ్రయించి పవిత్రమైన *గో-రక్షా* సంప్రదాయాన్ని నిర్వహించారు:

> **శ్రీమద్ భాగవతం, స్కంధం 10, అధ్యాయం 6, శ్లోకాలు 20–21**
> 
> *గోమూత్రేణ స్నాపయిత్వా గోరజస్య అవధూలితమ్*  
> *రక్షాం చక్రుస్తనౌ గోప్యః శాకిన్యాదిభ్య ఆదృతాః*  
> 
> **తాత్పర్యం:** "గోపికలు బాలకృష్ణుడికి పవిత్ర గోమూత్రంతో స్నానం చేయించి, ఆవుల గిట్టల నుండి లేచిన గోధూళితో శ్రీఅంగాన్ని పవిత్రం చేసి, శ్రీమహావిష్ణువు ద్వాదశ నామాలను ఉచ్చరిస్తూ రక్షా బంధనం చేశారు."

ఒక వృద్ధ గోపిక గోతోకతో చామరంలా వీచి దిష్టి తీసింది. యశోదాదేవి ఆవుపేడతో నుదుటిపై తిలకం దిద్దింది.

తరువాత గోపికలు భగవాన్ శ్రీమహావిష్ణువు పన్నెండు నామాలతో అంగరక్ష చేశారు: "కేశవుడు పాదాలను, గోవిందుడు మోకాళ్ళను, మాధవుడు తొడలను, వైకుంఠుడు ఉదరాన్ని, మధుసూదనుడు హృదయాన్ని, హృషీకేశుడు ఇంద్రియాలను, దామోదరుడు సమస్త శరీరాన్ని రక్షించుగాక!"

అఖిలాండకోటి బ్రహ్మాండ నాయకుడైన శ్రీకృష్ణుడు తన భక్తులైన తల్లుల అమాయక ప్రేమను ఆనందంగా స్వీకరించాడు. ఆ తర్వాత యశోదమ్మ తన అమృతతుల్యమైన స్తన్యమివ్వగా, బాలకృష్ణుడు పరమానందంతో తాగాడు.

### పన్నెండు మైళ్ల పూతన దేహ దహనం

ఇంతలో గోపాలురు పూతన పన్నెండు మైళ్ల వికృత శరీరం వద్దకు చేరారు. అంత పెద్ద దేహాన్ని పూడ్చిపెట్టడం అసాధ్యం. 

అందువల్ల గోపాలురు గొడ్డళ్ళతో ఆ భారీ శరీరాన్ని ముక్కలు ముక్కలుగా నరికారు:

> **శ్రీమద్ భాగవతం, స్కంధం 10, అధ్యాయం 6, శ్లోకాలు 34–35**
> 
> *కలేవరం పరశుభిశ్ఛిత్త్వా దారుసంచయైః*  
> *దాహయామాసుః సరోషా దూరే గోకులవాసినః*  
> 
> **తాత్పర్యం:** "కోపోద్రిక్తులైన గోకులవాసులు గొడ్డళ్ళతో పూతన శరీరాన్ని ముక్కలుగా నరికి, దూరంగా కట్టెల మోపులు పేర్చి దహనం చేశారు."

వారు పెద్దఎత్తున కలపను తెచ్చి చితిపై ఆ శరీర భాగాలను పేర్చి నిప్పంటించారు.

### అగరు, చందన సుగంధాల అద్భుతం

చితాగ్ని రగులుకోగానే ఒక ఊహించని అద్భుతం జరిగింది. సాధారణంగా రాక్షస శరీరం కాలినప్పుడు భరించలేని దుర్గంధం వస్తుంది. కానీ పూతన చితి నుండి లేచిన పొగ అద్భుతమైన సువాసనను వెదజల్లింది:

> **శ్రీమద్ భాగవతం, స్కంధం 10, అధ్యాయం 6, శ్లోకాలు 37–38**
> 
> *దగ్ధస్యాపి శరీరస్య ధూమః సౌరభ్యముత్తమమ్*  
> *వవాహ సర్వతో దిక్షు సర్వలోకమనోహరః*  
> *పూతనా లోకబాలఘ్నీ రాక్షసీ రుధిరాశనా*  
> *జిఘాంసయాపి హరయే స్తనం దత్త్వాప సద్గతిమ్*  
> 
> **తాత్పర్యం:** "ఆమె కాలుతున్న శరీరం నుండి లేచిన పొగ అగరు, చందనం వంటి పరమ పవిత్ర దివ్య సుగంధాన్ని నలుదిక్కులా వ్యాపింపజేసింది! పూతన రక్తపిపాసియైన రాక్షసి; అయినప్పటికీ చంపే ఉద్దేశంతోనైనా శ్రీహరికి స్తన్యమిచ్చిన పుణ్యం వల్ల ఆమె సమస్త పాపాలు నశించి పరమగతిని పొందింది!"

గోకులమంతా అగరు ధూప పరిమళాలతో నిండిపోయింది. గోపాలురు ఆశ్చర్యంతో ఆ సుగంధాన్ని ఆఘ్రాణించారు.

### నందమహారాజు రాక మరియు భగవంతుని అపార కరుణ

సరిగ్గా అదే సమయానికి నందమహారాజు మథుర నుండి గోకులానికి తిరిగి వచ్చారు. గాలిలో అగరు సుగంధాన్ని, నేలకూలిన రాక్షసి శవాన్ని చూసి ఆయన విస్తుపోయారు.

ప్రజలు జరిగిన కథంతా చెప్పినప్పుడు, నందమహారాజుకు మథురలో వసుదేవుడు చెప్పిన హెచ్చరిక గుర్తొచ్చింది: *"గోకులానికి వెంటనే వెళ్ళండి, అక్కడ ముప్పు పొంచి ఉంది!"* వసుదేవుని దివ్యదృష్టిని కొనియాడుతూ నందమహారాజు పరుగున వచ్చి చిన్ని కృష్ణుడిని గుండెలకు హత్తుకున్నారు.

శ్రీల ప్రభుపాదుల వివరణ: పూతన విషమిచ్చి చంపడానికి వచ్చింది. కానీ తల్లి రూపంలో పాలిచ్చిన ఆ బాహ్య సేవను మాత్రమే భగవంతుడు స్వీకరించి, ఆమెకు గోలోక బృందావనంలో నిత్యధాత్రి (తల్లి) స్థానాన్ని ప్రసాదించాడు!

విషమిచ్చిన రాక్షసికే భగవంతుడు ఇంతటి ముక్తిని ఇస్తే, స్వచ్ఛమైన ప్రేమతో సేవించే భక్తునికి ఇంకెంతటి పరమ పదాన్ని ప్రసాదిస్తాడో కదా!""",
                "questions": [
                    {
                        "question": "పూతన వక్షస్థలం నుండి తెచ్చిన తర్వాత గోపికలు ఏ రక్షా విధానాన్ని చేశారు?",
                        "options": [
                            {"text": "గోమూత్రం, గోమయం, గోధూళి మరియు ఆవు తోకతో గో-రక్షా విధానం", "is_correct": True},
                            {"text": "ఆయుధ విన్యాసాలు", "is_correct": False},
                            {"text": "ఇనుప పెట్టెలో దాచడం", "is_correct": False},
                            {"text": "మథుర వైద్యుడి వద్దకు తీసుకెళ్ళడం", "is_correct": False}
                        ]
                    },
                    {
                        "question": "కృష్ణుడి అంగరక్ష కోసం గోపికలు ఎవరి నామాలను పఠించారు?",
                        "options": [
                            {"text": "శ్రీమహావిష్ణువు నామాలను (కేశవ, నారాయణ, మాధవ, గోవింద)", "is_correct": True},
                            {"text": "ఇంద్రుడు మరియు అగ్నిదేవుని పేర్లను", "is_correct": False},
                            {"text": "మథుర రాజుల పేర్లను", "is_correct": False},
                            {"text": "గ్రహాల పేర్లను", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పన్నెండు మైళ్ల పూతన శవాన్ని గోపాలురు ఏమి చేశారు?",
                        "options": [
                            {"text": "గొడ్డళ్ళతో ముక్కలుగా నరికి కట్టెలపై దహనం చేశారు", "is_correct": True},
                            {"text": "సముద్రంలో పడేశారు", "is_correct": False},
                            {"text": "మట్టిలో పూడ్చిపెట్టారు", "is_correct": False},
                            {"text": "వీధిలోనే వదిలేశారు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పూతన చితి నుండి ఎలాంటి సువాసన వెలువడింది?",
                        "options": [
                            {"text": "అగరు మరియు చందనం వంటి దివ్య సుగంధం", "is_correct": True},
                            {"text": "భరించలేని దుర్గంధం", "is_correct": False},
                            {"text": "ఇనుము కాలిన వాసన", "is_correct": False},
                            {"text": "ఎలాంటి వాసనా రాలేదు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పూతన చితి నుండి అగరు సువాసన రావడానికి కారణం ఏమిటి?",
                        "options": [
                            {"text": "శ్రీకృష్ణుడు పాలు తాగడం వల్ల ఆమె పాపాలన్నీ నశించి శరీరం పవిత్రమైంది", "is_correct": True},
                            {"text": "కట్టెలపై అత్తరు చల్లారు", "is_correct": False},
                            {"text": "దేవతలు పన్నీరు చల్లారు", "is_correct": False},
                            {"text": "పూతన పువ్వులు తిని ఉంది", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పూతనకు భగవాన్ శ్రీకృష్ణుడు ఏ ఆధ్యాత్మిక స్థానాన్ని ఇచ్చాడు?",
                        "options": [
                            {"text": "గోలోకంలో నిత్యధాత్రి (తల్లి) స్థానాన్ని", "is_correct": True},
                            {"text": "స్వర్గంలో ఇంద్రాణి పదవిని", "is_correct": False},
                            {"text": "భూమిపై రాణిగా పుట్టే వరాన్ని", "is_correct": False},
                            {"text": "నరకానికి పంపాడు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పూతన చంపడానికి వచ్చినప్పటికీ భగవంతుడు ఆమెలోని దేనిని పరిగణనలోకి తీసుకున్నాడు?",
                        "options": [
                            {"text": "తల్లిలా స్తన్యమిచ్చిన సేవను మాత్రమే", "is_correct": True},
                            {"text": "ఆమె అందమైన రూపాన్ని", "is_correct": False},
                            {"text": "కంసుడితో ఆమెకున్న సంబంధాన్ని", "is_correct": False},
                            {"text": "ఆమె శారీరక బలాన్ని", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పూతన దహన సమయంలో మథుర నుండి ఎవరు వచ్చారు?",
                        "options": [
                            {"text": "నందమహారాజు మరియు గోపాలురు", "is_correct": True},
                            {"text": "కంసుడు మరియు సైన్యం", "is_correct": False},
                            {"text": "నారద మహర్షి", "is_correct": False},
                            {"text": "వసుదేవుడు మరియు దేవకి", "is_correct": False}
                        ]
                    },
                    {
                        "question": "రాక్షసి శవాన్ని చూసిన నందమహారాజుకు ఎవరి హెచ్చరిక గుర్తొచ్చింది?",
                        "options": [
                            {"text": "మథురలో వసుదేవుడు చేసిన హెచ్చరిక", "is_correct": True},
                            {"text": "ఒక పాత కల", "is_correct": False},
                            {"text": "కంసుడి పన్ను రశీదు", "is_correct": False},
                            {"text": "గ్రామ పెద్దల మాటలు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పూతన చితి నుండి అగరు సువాసన రావడాన్ని భాగవతంలోని ఏ శ్లోకాలు వర్ణిస్తాయి?",
                        "options": [
                            {"text": "శ్లోకాలు 37–38", "is_correct": True},
                            {"text": "శ్లోకాలు 1–2", "is_correct": False},
                            {"text": "శ్లోకాలు 15–16", "is_correct": False},
                            {"text": "శ్లోకాలు 43–44", "is_correct": False}
                        ]
                    }
                ]
            },
            "kn": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "ಪೂತನಾ ಮೋಕ್ಷ ಮತ್ತು ಗೋಪಿಯರ ಗೋ-ರಕ್ಷಾ ಮಂತ್ರಗಳು",
                "content": """### ಗೋಪಿಯರ ಗೋ-ರಕ್ಷಾ ವಿಧಾನ

ಪೂತನೆಯ ವಿಶಾಲ ಶವದಿಂದ ಮುದ್ದು ಕೃಷ್ಣನನ್ನು ಎತ್ತಿಕೊಂಡ ಯಶೋದಾ, ರೋಹಿಣಿ ಮತ್ತು ಹಿರಿಯ ಗೋಪಿಯರು ಮಗುವನ್ನು ಮನೆಯ ಅಂಗಳಕ್ಕೆ ಕರೆತಂದರು. ಕೃಷ್ಣನು ಮಂದಹಾಸ ಬೀರುತ್ತಿದ್ದರೂ, ತಾಯಿಯ ಹೃದಯವು ಭಯದಿಂದ ತತ್ತರಿಸಿತ್ತು. ಯಾವುದೇ ಅಸುರೀ ಶಕ್ತಿ ಮಗುವನ್ನು ಬಾಧಿಸಬಾರದೆಂದು ಗೋಮಾತೆಯನ್ನು ಆಶ್ರಯಿಸಿ ಪವಿತ್ರವಾದ *ಗೋ-ರಕ್ಷಾ* ವಿಧಿಗಳನ್ನು ನೆರವೇರಿಸಿದರು:

> **ಶ್ರೀಮದ್ ಭಾಗವತಂ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 6, ಶ್ಲೋಕಗಳು 20–21**
> 
> *ಗೋಮೂತ್ರೇಣ ಸ್ನಾಪಯಿತ್ವಾ ಗೋರಜಸ್ಯ ಅವಧೂಲಿತಮ್*  
> *ರಕ್ಷಾಂ ಚಕ್ರುಸ್ತನೌ ಗೋಪ್ಯಃ ಶಾಕಿನ್ಯಾದಿಭ್ಯ ಆದೃತಾಃ*  
> 
> **ಭಾವಾರ್ಥ:** "ಗೋಪಿಯರು ಬಾಲಕೃಷ್ಣನಿಗೆ ಪವಿತ್ರ ಗೋಮೂತ್ರದಿಂದ ಸ್ನಾನ ಮಾಡಿಸಿದರು, ಆಕಳುಗಳ ಗೊರಸುಗಳಿಂದ ಎದ್ದ ಗೋಧೂಳಿಯನ್ನು ಶ್ರೀಅಂಗಕ್ಕೆ ಲೇಪಿಸಿದರು ಮತ್ತು ವಿಷ್ಣು ಭಗವಂತನ ದ್ವಾದಶ ನಾಮಗಳನ್ನು ಹೇಳುತ್ತಾ ಮಗುವಿನ ಹನ್ನೆರಡು ಅಂಗಗಳಿಗೆ ರಕ್ಷೆ ಕಟ್ಟಿದರು."

ಒಬ್ಬ ಹಿರಿಯ ಗೋಪಿಯು ಹಸುವಿನ ಬಾಲದ ಚಾಮರದಿಂದ ದೃಷ್ಟಿ ತೆಗೆದಳು. ಯಶೋದೆಯು ಗೋಮಯದಿಂದ ಮಗುವಿನ ಹಣೆಗೆ ತಿಲಕವಿಟ್ಟು ಆಶೀರ್ವದಿಸಿದಳು.

ನಂತರ ಭಗವಾನ್ ವಿಷ್ಣುವಿನ ಹನ್ನೆರಡು ನಾಮಗಳಿಂದ ಅಂಗರಕ್ಷೆ ಮಾಡಿದರು: "ಕೇಶವನು ಪಾದಗಳನ್ನು, ಗೋವಿಂದನು ಮೊಣಕಾಲುಗಳನ್ನು, ಮಾಧವನು ತೊಡೆಗಳನ್ನು, ವೈಕುಂಠನು ಉದರವನ್ನು, ಮಧುಸೂದನನು ಹೃದಯವನ್ನು, ಹೃಷೀಕೇಶನು ಇಂದ್ರಿಯಗಳನ್ನು ಮತ್ತು ದಾಮೋದರನು ಸಮಸ್ತ ಶರೀರವನ್ನು ರಕ್ಷಿಸಲಿ!"

ಜಗತ್ತನ್ನೇ ರಕ್ಷಿಸುವ ಶ್ರೀಕೃಷ್ಣನು ತಾಯಂದಿರ ಮುಗ್ಧ ಪ್ರೀತಿಗೆ ಶರಣಾಗಿ ಎಲ್ಲವನ್ನೂ ಸ್ವೀಕರಿಸಿದನು. ನಂತರ ಯಶೋದೆಯು ಅಮೃತದಂತಹ ಎದೆಹಾಲುಣಿಸಿದಾಗ ಕೃಷ್ಣನು ಪರಮಾನಂದದಿಂದ ಕುಡಿದನು.

### ಹನ್ನೆರಡು ಮೈಲಿ ಉದ್ದದ ಶವದ ದಹನ

ಇತ್ತ ಗೋಪಾಲಕರು ಪೂತನೆಯ ಹನ್ನೆರಡು ಮೈಲಿ ಉದ್ದದ ಶವದ ಬಳಿ ಜಮಾಯಿಸಿದರು. ಅಷ್ಟು ಬೃಹತ್ ಶರೀರವನ್ನು ಹೂಳಲು ಸಾಧ್ಯವಿರಲಿಲ್ಲ. 

ಆದ್ದರಿಂದ ಕೊಡಲಿಗಳಿಂದ ಆ ಶರೀರವನ್ನು ತುಂಡುತುಂಡಾಗಿ ಕತ್ತರಿಸಿದರು:

> **ಶ್ರೀಮದ್ ಭಾಗವತಂ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 6, ಶ್ಲೋಕಗಳು 34–35**
> 
> *ಕಲೇವರಂ ಪರಶುಭಿಶ್ಛಿತ್ತ್ವಾ ದಾರುಸಂಚಯೈಃ*  
> *ದಾಹಯಾಮಾಸುಃ ಸರೋಷಾ ದೂರೇ ಗೋಕುಲವಾಸಿನಃ*  
> 
> **ಭಾವಾರ್ಥ:** "ಕೋಪಗೊಂಡ ಗೋಕುಲವಾಸಿಗಳು ಕೊಡಲಿಗಳಿಂದ ಪೂತನೆಯ ಬೃಹತ್ ಶರೀರವನ್ನು ತುಂಡುಗಳಾಗಿ ಕತ್ತರಿಸಿ, ಊರಿನಿಂದ ದೂರದಲ್ಲಿ ಕಟ್ಟಿಗೆಯ ರಾಶಿಯನ್ನಿಟ್ಟು ಆ ಶವವನ್ನು ದಹಿಸಿದರು."

ಅವರು ಕಾಡಿನಿಂದ ಕಟ್ಟಿಗೆಯನ್ನು ತಂದು ದೊಡ್ಡ ಚಿತೆಯನ್ನು ನಿರ್ಮಿಸಿ ಅಗ್ನಿಸ್ಪರ್ಶ ಮಾಡಿದರು.

### ಅಗರು ಮತ್ತು ಶ್ರೀಗಂಧದ ಪರಿಮಳದ ಪವಾಡ

ಚಿತೆಗೆ ಬೆಂಕಿ ಹೊತ್ತಿಕೊಂಡಾಗ ಒಂದು ಮಹಾ ಅದ್ಭುತ ನಡೆಯಿತು. ಸಾಮಾನ್ಯ ರಾಕ್ಷಸಿ ಶವ ಉರಿಯುವಾಗ ಅಸಹ್ಯ ದುರ್ನಾತ ಬರುತ್ತದೆ. ಆದರೆ ಪೂತನೆಯ ಚಿತೆಯಿಂದ ಎದ್ದ ಹೊಗೆಯು ದಿವ್ಯ ಪರಿಮಳವನ್ನು ಬೀರಿತು:

> **ಶ್ರೀಮದ್ ಭಾಗವತಂ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 6, ಶ್ಲೋಕಗಳು 37–38**
> 
> *ದಗ್ಧಸ್ಯಾಪಿ ಶರೀರಸ್ಯ ಧೂಮಃ ಸೌರಭ್ಯಮುತ್ತಮಮ್*  
> *ವವಾಹ ಸರ್ವತೋ ದಿಕ್ಷು ಸರ್ವಲೋಕಮನೋಹರಃ*  
> *ಪೂತನಾ ಲೋಕಬಾಲಘ್ನೀ ರಾಕ್ಷಸೀ ರುಧಿರGradಾ*  
> *ಜಿಘಾಂಸಯಾಪಿ ಹರಯೇ ಸ್ತನಂ ದತ್ತ್ವಾಪ ಸದ್ಗತಿಮ್*  
> 
> **ಭಾವಾರ್ಥ:** "ಆಕೆಯ ಉರಿಯುವ ಶರೀರದಿಂದ ಎದ್ದ ಹೊಗೆಯು ಅಗರು ಮತ್ತು ಶ್ರೀಗಂಧದಂತಹ ಅತ್ಯುತ್ತಮ ಸುಗಂಧವನ್ನು ಎಲ್ಲ ದಿಕ್ಕುಗಳಿಗೂ ಪಸರಿಸಿತು! ಪೂತನೆಯು ಹಸುಗೂಸುಗಳನ್ನು ಕೊಲ್ಲುವ ರಕ್ತಪಿಪಾಸಿ ರಾಕ್ಷಸಿಯಾಗಿದ್ದರೂ, ಕೊಲ್ಲುವ ಉದ್ದೇಶದಿಂದಲಾದರೂ ಶ್ರೀಹರಿಗೆ ಮೊಲೆಹಾಲುಣಿಸಿದ್ದರಿಂದ ಆಕೆಯ ಎಲ್ಲ ಪಾಪಗಳು ತೊಳೆದು ಪರಮ ಗತಿಯನ್ನು ಪಡೆದಳು!"

ಗೋಕುಲವೆಲ್ಲವೂ ಶ್ರೀಗಂಧದ ಪರಿಮಳದಿಂದ ತುಂಬಿಹೋಯಿತು. ಗೋಪಾಲಕರು ವಿಸ್ಮಯದಿಂದ ಮೂಗಿಗೆ ಬೆರಳಿಟ್ಟುಕೊಂಡರು.

### ನಂದಮಹಾರಾಜರ ಆಗಮನ ಮತ್ತು ಭಗವಂತನ ಅಪಾರ ಕೃಪೆ

ಅದೇ ಸಮಯಕ್ಕೆ ನಂದಮಹಾರಾಜರು ಮಥುರೆಯಿಂದ ಗೋಕುಲಕ್ಕೆ ಮರಳಿದರು. ಗಾಳಿಯಲ್ಲಿ ಅಗರು ಪರಿಮಳವನ್ನು, ಅಂಗಳದಲ್ಲಿ ಬಿದ್ದಿದ್ದ ರಾಕ್ಷಸಿಯ ಶರೀರವನ್ನು ಕಂಡು ಆಶ್ಚರ್ಯಚಕಿತರಾದರು.

ನಡೆದ ಘಟನೆಯನ್ನು ಕೇಳಿದಾಗ, ನಂದರಿಗೆ ಮಥುರೆಯಲ್ಲಿ ವಸುದೇವನು ನೀಡಿದ ಎಚ್ಚರಿಕೆ ನೆನಪಾಯಿತು: *"ಗೋಕುಲಕ್ಕೆ ತಕ್ಷಣ ಮರಳಿ, ಅಲ್ಲಿ ಅಪಾಯವಿದೆ!"* ವಸುದೇವನ ದಿವ್ಯದೃಷ್ಟಿಯನ್ನು ಕೊಂಡಾಡುತ್ತಾ ನಂದಮಹಾರಾಜರು ಓಡಿಬಂದು ಮುದ್ದು ಕೃಷ್ಣನನ್ನು ಆಲಂಗಿಸಿಕೊಂಡರು.

ಶ್ರೀಲ ಪ್ರಭುಪಾದರು ವಿವರಿಸುತ್ತಾರೆ: ಪೂತನೆಯು ವಿಷವಿಟ್ಟು ಕೊಲ್ಲಲು ಬಂದವಳು. ಆದರೆ ತಾಯಿಯಂತೆ ಮೊಲೆಹಾಲುಣಿಸಿದ ಆ ಬಾಹ್ಯ ಸೇವೆಯನ್ನು ಮಾತ್ರವೇ ಭಗವಂತನು ಪರಿಗಣಿಸಿ, ಆಕೆಗೆ ಗೋಲೋಕದಲ್ಲಿ ನಿತ್ಯ ತಾಯಿಯ ಸ್ಥಾನವನ್ನು ಕರುಣಿಸಿದನು!

ವಿಷವಿಕ್ಕಿದ ರಾಕ್ಷಸಿಗೇ ಇಂತಹ ಪರಮ ಮೋಕ್ಷವನ್ನು ನೀಡುವ ಭಗವಂತನು, ನಿಷ್ಕಲ್ಮಷ ಭಕ್ತಿಯಿಂದ ಪ್ರೀತಿಸುವ ಸಜ್ಜನ ಭಕ್ತರಿಗೆ ಇನ್ನೇನನ್ನು ತಾನೇ ಕರುಣಿಸುವುದಿಲ್ಲ!""",
                "questions": [
                    {
                        "question": "ಪೂತನೆಯ ಶವದಿಂದ ತಂದ ನಂತರ ಗೋಪಿಯರು ಬಾಲಕೃಷ್ಣನಿಗೆ ಯಾವ ರಕ್ಷಾ ವಿಧಿ ಮಾಡಿದರು?",
                        "options": [
                            {"text": "ಗೋಮೂತ್ರ, ಗೋಮಯ, ಗೋಧೂಳಿ ಮತ್ತು ಹಸುವಿನ ಬಾಲದಿಂದ ಗೋ-ರಕ್ಷಾ ವಿಧಿ", "is_correct": True},
                            {"text": "ಆಯುಧ ತಾಲೀಮು", "is_correct": False},
                            {"text": "ಪೆಟ್ಟಿಗೆಯಲ್ಲಿ ಕೂಡಿ ಹಾಕುವುದು", "is_correct": False},
                            {"text": "ಮಥುರೆಯ ವೈದ್ಯರ ಬಳಿಗೆ ಕೊಂಡೊಯ್ಯುವುದು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಬಾಲಕೃಷ್ಣನ ಅಂಗರಕ್ಷೆಗಾಗಿ ಗೋಪಿಯರು ಯಾರ ನಾಮಗಳನ್ನು ಜಪಿಸಿದರು?",
                        "options": [
                            {"text": "ವಿಷ್ಣು ಭಗವಂತನ ನಾಮಗಳನ್ನು (ಕೇಶವ, ನಾರಾಯಣ, ಮಾಧವ, ಗೋವಿಂದ)", "is_correct": True},
                            {"text": "ಇಂದ್ರ ಮತ್ತು ಅಗ್ನಿಯ ಹೆಸರುಗಳನ್ನು", "is_correct": False},
                            {"text": "ಮಥುರೆಯ ರಾಜರ ಹೆಸರುಗಳನ್ನು", "is_correct": False},
                            {"text": "ಗ್ರಹಗಳ ಹೆಸರುಗಳನ್ನು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಹನ್ನೆರಡು ಮೈಲಿ ಉದ್ದದ ಪೂತನೆಯ ಶವವನ್ನು ಗೋಪಾಲಕರು ಏನು ಮಾಡಿದರು?",
                        "options": [
                            {"text": "ಕೊಡಲಿಗಳಿಂದ ತುಂಡರಿಸಿ ಕಟ್ಟಿಗೆಯ ಮೇಲೆ ದಹಿಸಿದರು", "is_correct": True},
                            {"text": "ಸಮುದ್ರಕ್ಕೆ ಎಸೆದರು", "is_correct": False},
                            {"text": "ಮಣ್ಣಿನಲ್ಲಿ ಹೂತರು", "is_correct": False},
                            {"text": "ದಾರಿಯಲ್ಲೇ ಬಿಟ್ಟರು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಪೂತನೆಯ ಚಿತೆಯಿಂದ ಎದ್ದ ಹೊಗೆಯಿಂದ ಎಂತಹ ಪರಿಮಳ ಬಂದಿತು?",
                        "options": [
                            {"text": "ಅಗರು ಮತ್ತು ಶ್ರೀಗಂಧದಂತಹ ದಿವ್ಯ ಪರಿಮಳ", "is_correct": True},
                            {"text": "ತಡೆಯಲಾರದ ದುರ್ನಾತ", "is_correct": False},
                            {"text": "ಕಬ್ಬಿಣ ಸುಟ್ಟ ವಾಸನೆ", "is_correct": False},
                            {"text": "ಯಾವ ವಾಸನೆಯೂ ಬರಲಿಲ್ಲ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಪೂತನೆಯ ಚಿತೆಯಿಂದ ಅಗರು ಪರಿಮಳ ಬರಲು ಕಾರಣವೇನು?",
                        "options": [
                            {"text": "ಶ್ರೀಕೃಷ್ಣನು ಹಾಲು ಕುಡಿದಿದ್ದರಿಂದ ಆಕೆಯ ಪಾಪಗಳು ಕರಗಿ ಶರೀರ ಪವಿತ್ರವಾಯಿತು", "is_correct": True},
                            {"text": "ಕಟ್ಟಿಗೆಗೆ ಸುಗಂಧ ದ್ರವ್ಯ ಸುರಿಯಲಾಗಿತ್ತು", "is_correct": False},
                            {"text": "ದೇವತೆಗಳು ಪನ್ನೀರು ಚಿಮುಕಿಸಿದರು", "is_correct": False},
                            {"text": "ಪೂತನೆ ಹೂವುಗಳನ್ನು ತಿಂದಿದ್ದಳು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಶ್ರೀಕೃಷ್ಣನು ಪೂತನಿಗೆ ಯಾವ ಆಧ್ಯಾತ್ಮಿಕ ಸ್ಥಾನವನ್ನು ಕರುಣಿಸಿದನು?",
                        "options": [
                            {"text": "ಗೋಲೋಕದಲ್ಲಿ ನಿತ್ಯ ತಾಯಿಯ (ಧಾತ್ರಿ) ಸ್ಥಾನವನ್ನು", "is_correct": True},
                            {"text": "ಸ್ವರ್ಗದಲ್ಲಿ ಇಂದ್ರಾಣಿ ಪದವಿಯನ್ನು", "is_correct": False},
                            {"text": "ಭೂಮಿಯಲ್ಲಿ ರಾಣಿಯಾಗುವ ವರವನ್ನು", "is_correct": False},
                            {"text": "ನರಕಕ್ಕೆ ತಳ್ಳಿದನು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಪೂತನೆ ಕೊಲ್ಲಲು ಬಂದಿದ್ದರೂ ಭಗವಂತನು ಆಕೆಯ ಯಾವ ವಿಷಯವನ್ನು ಸ್ವೀಕರಿಸಿದನು?",
                        "options": [
                            {"text": "ತಾಯಿಯಂತೆ ಹಾಲುಣಿಸಿದ ಸೇವೆಯನ್ನು ಮಾತ್ರ", "is_correct": True},
                            {"text": "ಆಕೆಯ ಸುಂದರ ರೂಪವನ್ನು", "is_correct": False},
                            {"text": "ಕಂಸನ ಜೊತೆಗಿನ ಸ್ನೇಹವನ್ನು", "is_correct": False},
                            {"text": "ಆಕೆಯ ಶಕ್ತಿಯನ್ನು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಶವದ ದಹನದ ವೇಳೆಗೆ ಮಥುರೆಯಿಂದ ಯಾರು ಹಿಂದಿರುಗಿದರು?",
                        "options": [
                            {"text": "ನಂದಮಹಾರಾಜರು ಮತ್ತು ಗೋಪಾಲಕರು", "is_correct": True},
                            {"text": "ಕಂಸ ಮತ್ತು ಆತನ ಸೈನ್ಯ", "is_correct": False},
                            {"text": "ನಾರದ ಮುನಿಗಳು", "is_correct": False},
                            {"text": "ವಸುದೇವ ಮತ್ತು ದೇವಕಿ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಶವವನ್ನು ಕಂಡು ನಂದರಿಗೆ ಯಾರ ಎಚ್ಚರಿಕೆ ನೆನಪಾಯಿತು?",
                        "options": [
                            {"text": "ಮಥುರೆಯಲ್ಲಿ ವಸುದೇವನು ನೀಡಿದ ಎಚ್ಚರಿಕೆ", "is_correct": True},
                            {"text": "ಹಳೆಯ ಕನಸಿನ ಮಾತು", "is_correct": False},
                            {"text": "ಕಂಸನ ಕಂದಾಯ ರಶೀದಿ", "is_correct": False},
                            {"text": "ಹಳ್ಳಿಯ ಹಿರಿಯರ ಮಾತು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಪೂತನೆಯ ಚಿತೆಯಿಂದ ಅಗರು ಪರಿಮಳ ಬರುವುದನ್ನು ವಿವರಿಸುವ ಭಾಗವತದ ಶ್ಲೋಕಗಳು ಯಾವುವು?",
                        "options": [
                            {"text": "ಶ್ಲೋಕ 37–38", "is_correct": True},
                            {"text": "ಶ್ಲೋಕ 1–2", "is_correct": False},
                            {"text": "ಶ್ಲೋಕ 15–16", "is_correct": False},
                            {"text": "ಶ್ಲೋಕ 43–44", "is_correct": False}
                        ]
                    }
                ]
            },
            "ml": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "പൂതനയ്ക്ക് മോക്ഷപ്രാപ്തിയും ഗോപികമാരുടെ രക്ഷാമന്ത്രങ്ങളും",
                "content": """### ഗോപികമാർ നടത്തിയ ഗോ-രക്ഷാ ചടങ്ങുകൾ

പൂതനയുടെ പടുകൂറ്റൻ നെഞ്ചിൽനിന്ന് ഉണ്ണിക്കണ്ണനെ എടുത്തുയർത്തിയ യശോദ അമ്മയും രോഹിണി അമ്മയും ഗോപികമാരും ചേർന്ന് കുഞ്ഞിനെ വീട്ടുമുറ്റത്തേക്ക് കൊണ്ടുവന്നു. ഉണ്ണിക്കണ്ണൻ യാതൊരു പരിക്കുമേൽക്കാതെ പുഞ്ചിരിതൂകി നിൽക്കുകയായിരുന്നെങ്കിലും, മാതൃഹൃദയങ്ങൾ ആശങ്കയാൽ വിറച്ചു. ആസുരബാധകളെ അകറ്റാൻ പവിത്രമായ പശുവിനെ കേന്ദ്രീകരിച്ചുള്ള വൈദികമായ *ഗോ-രക്ഷാ* ചടങ്ങുകൾ അവർ ഉടൻ നടത്തി:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അധ്യായം 6, ശ്ലോകങ്ങൾ 20–21**
> 
> *ഗോമൂത്രേണ സ്നാപയിത്വാ ഗോരജസ്യ അവധൂലിതമ്*  
> *രക്ഷാം ചക്രുസ്തനൗ ഗോപ്യഃ ശാകിന്യാദിഭ്യ ആദൃതാഃ*  
> 
> **അർത്ഥം:** "ഗോപികമാർ ഉണ്ണിക്കണ്ണനെ വിശുദ്ധ ഗോമൂത്രത്താൽ സ്നാനം ചെയ്യിക്കുകയും, പശുക്കളുടെ കുളമ്പുകളിൽനിന്നുയർന്ന ഗോരേണു വിതറി അവിടുത്തെ തിരുമേനി ശുദ്ധീകരിക്കുകയും, ഭഗവാൻ വിഷ്ണുവിന്റെ പവിത്ര നാമങ്ങൾ ചൊല്ലി പന്ത്രണ്ട് അംഗങ്ങളിലും രക്ഷാബന്ധനം നടത്തുകയും ചെയ്തു."

ഒരു മുതിർന്ന ഗോപിക പശുവിന്റെ വാൽക്കൊണ്ട് കുഞ്ഞിന് ഉഴിച്ചിൽ നടത്തി ദൃഷ്ടിദോഷങ്ങളെ അകറ്റി. യശോദ അമ്മ ചാണകം കൊണ്ട് നെറ്റിയിൽ തിലകം ചാർത്തി.

തുടർന്ന് ഗോപികമാർ പരമഭക്തിയോടെ ഭഗവാൻ വിഷ്ണുവിന്റെ പന്ത്രണ്ട് നാമങ്ങൾ ചൊല്ലി അംഗരക്ഷ ചെയ്തു: "കേശവൻ കാൽപ്പാദങ്ങളെ കാക്കട്ടെ; ഗോവിന്ദൻ കാൽമുട്ടുകളെ കാക്കട്ടെ; മാധവൻ തുടകളെ കാക്കട്ടെ; വൈകുണ്ഠൻ ഉദരത്തെ കാക്കട്ടെ; മധുസൂദനൻ ഹൃദയത്തെ കാക്കട്ടെ; ഹൃഷീകേശൻ ഇന്ദ്രിയങ്ങളെ കാക്കട്ടെ; ദാമോദരൻ സമസ്ത ശരീരത്തെയും കാക്കട്ടെ!"

പ്രപഞ്ചനാഥനായ ശ്രീകൃഷ്ണൻ തന്റെ അമ്മമാരുടെ സ്നേഹവാത്സല്യങ്ങളെ ആദരവോടെ സ്വീകരിച്ചു. തുടർന്ന് യശോദ അമ്മ ഉണ്ണിയെ മടിയിലിരുത്തി അമൃതതുല്യമായ മുലപ്പാൽ കൊടുത്തു; ഭഗവാൻ ആനന്ദത്തോടെ അത് കുടിച്ചു.

### പന്ത്രണ്ട് മൈൽ നീളമുള്ള രാക്ഷസിയുടെ ശവദാഹം

ഇതിനിടയിൽ ഗോപന്മാർ പൂതനയുടെ പന്ത്രണ്ട് മൈൽ നീളമുള്ള കൂറ്റൻ ശരീരത്തിനടുത്തേക്ക് ഒത്തുചേർന്നു. അത്രയും വലിയ ശരീരം കുഴിച്ചുമൂടുക അസാധ്യമായിരുന്നു. 

അതുകൊണ്ട് ഗോപന്മാർ കോടാലികൾ കൊണ്ട് ആ ഭീമാകാര ശരീരം കഷണങ്ങളാക്കി മുറിച്ചു:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അധ്യായം 6, ശ്ലോകങ്ങൾ 34–35**
> 
> *കലേവരം പരശുഭിശ്ഛിത്ത്വാ ദാരുസഞ്ചയൈഃ*  
> *ദാഹയാമാസുഃ സരോഷാ ദൂരേ ഗോകൂലവാസിനഃ*  
> 
> **അർത്ഥം:** "കോപിഷ്ടരായ ഗോകൂലവാസികൾ കോടാലികൾ കൊണ്ട് പൂതനയുടെ ശരീരം തുണ്ടംതുണ്ടമായി വെട്ടിമുറിക്കുകയും, നാട്ടിൽനിന്ന് ദൂരെ കാട്ടിൽ വിറകുകൂട്ടി ആ ശരീരം ദഹിപ്പിക്കുകയും ചെയ്തു."

അവർ ധാരാളം വിറകുകൂട്ടി വലിയ ചിതയൊരുക്കി തീ കൊടുത്തു.

### അഗരുവിന്റെയും ചന്ദനത്തിന്റെയും ദിവ്യ സുഗന്ധം

ചിത കത്തിയപ്പോൾ അത്യത്ഭുതകരമായ ഒരു പ്രതിഭാസമുണ്ടായി. സാധാരണ ഒരു രാക്ഷസിയുടെ ശരീരം കത്തുമ്പോൾ അസഹനീയമായ ദുർഗന്ധമാണ് ഉണ്ടാകേണ്ടത്. എന്നാൽ പൂതനയുടെ ചിതയിൽനിന്ന് ഉയർന്ന പുക ദിവ്യമായ സുഗന്ധം പരത്തി:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അധ്യായം 6, ശ്ലോകങ്ങൾ 37–38**
> 
> *ദഗ്ദ്ധസ്യാപി ശരീരസ്യ ധൂമഃ സൗരഭ്യമുത്തമമ്*  
> *വവാഹ സർവ്വതോ ദിക്ഷു സർവ്വലോകമനോഹരഃ*  
> *പൂതനാ ലോകബാലഘ്നീ രാക്ഷസീ രുധിരാശനാ*  
> *ജിഘാംസയാപി ഹരയേ സ്തനം ദത്ത്വാപ സദ്ഗതിമ്*  
> 
> **അർത്ഥം:** "കത്തിയെരിയുന്ന ആ ശരീരത്തിൽനിന്നുയർന്ന പുക അഗരുവിന്റെയും ചന്ദനത്തിന്റെയും ദിവ്യസുഗന്ധം നാനാദിക്കുകളിലും പരത്തി എല്ലാവരുടെയും മനസ്സിനെ ആകർഷിച്ചു! പൂതന കുഞ്ഞുങ്ങളെ കൊല്ലുന്ന രക്തദാഹിയായ രാക്ഷസിയായിരുന്നു; എന്നിട്ടും വധിക്കാൻ വേണ്ടിയാണെങ്കിലും ഭഗവാന് മുലപ്പാൽ കൊടുത്തതുകൊണ്ട് അവൾക്ക് പരമമായ മോക്ഷപദം ലഭിച്ചു!"

ഗോകൂലവും കാടുകളും അഗരുസുഗന്ധത്താൽ നിറഞ്ഞു. ഗോപന്മാർ അത്ഭുതസ്തബ്ധരായി പരസ്പരം നോക്കി.

### നന്ദഗോപരുടെ തിരിച്ചുവരവും ഭഗവാന്റെ അളവറ്റ കാരുണ്യവും

ആ സമയത്ത് നന്ദഗോപർ മഥുരയിൽ കപ്പം നൽകി ഗോകൂലത്തിൽ തിരിച്ചെത്തി. കാറ്റിൽ പരന്ന അഗരുസുഗന്ധവും കാട്ടിൽ കിടക്കുന്ന കൂറ്റൻ അസ്ഥികളും കണ്ട് അദ്ദേഹം അമ്പരന്നു.

നടന്ന സംഭവങ്ങളെല്ലാം കേട്ടപ്പോൾ, മഥുരയിൽ വസുദേവർ നൽകിയ മുന്നറിയിപ്പ് നന്ദഗോപർ ഓർത്തു: *"ഗോകൂലത്തിലേക്ക് ഉടൻ മടങ്ങുക, അവിടെ ആപത്ത് വരാൻ പോകുന്നു!"* വസുദേവരുടെ ദിവ്യദൃഷ്ടിയെ വാഴ്ത്തി നന്ദഗോപർ ഓടിയെത്തി ഉണ്ണിക്കണ്ണനെ മാറോടണച്ചു.

ശ്രീല പ്രഭുപാദർ വ്യക്തമാക്കുന്നു: പൂതന വിഷം നൽകി കൊല്ലാൻ വന്ന രാക്ഷസിയാണ്. എന്നാൽ അവൾ ഒരു അമ്മയെപ്പോലെ മുലപ്പാൽ തന്ന ആ ബാഹ്യസേവയെ മാത്രം ഭഗവാൻ സ്വീകരിച്ച്, അവളുടെ എല്ലാ ദ്രോഹങ്ങളെയും വിസ്മരിച്ച്, ഗോലോകത്തിൽ നിത്യമായ അമ്മയുടെ (ധാത്രി) പദവി നൽകി അനുഗ്രഹിച്ചു!

കൊല്ലാൻ വന്ന രാക്ഷസിക്കുപോലും ഭഗവാൻ ഇത്രയും ഉന്നതമായ മോക്ഷം നൽകിയെങ്കിൽ, നിർമ്മലമായ ഭക്തിയോടെ ഭഗവാനെ സ്നേഹിക്കുന്ന ഭക്തർക്ക് അവിടുന്ന് എന്താണ് നൽകാതിരിക്കുക!""",
                "questions": [
                    {
                        "question": "പൂതനയുടെ മാറത്തുനിന്ന് എടുത്ത ശേഷം ഗോപികമാർ ഉണ്ണിക്കണ്ണന് എന്ത് രക്ഷാചടങ്ങാണ് ചെയ്തത്?",
                        "options": [
                            {"text": "ഗോമൂത്രം, ചാണകം, ഗോരേണു, പശുവിന്റെ വാൽ എന്നിവ കൊണ്ടുള്ള ഗോ-രക്ഷാ ചടങ്ങ്", "is_correct": True},
                            {"text": "ആയുധ പരിശീലനം", "is_correct": False},
                            {"text": "പെട്ടിയിൽ പൂട്ടിയിടൽ", "is_correct": False},
                            {"text": "മഥുരയിലെ വൈദ്യന്റെ അടുത്ത് കൊണ്ടുപോകൽ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഉണ്ണിക്കണ്ണന്റെ അംഗരക്ഷയ്ക്കായി ഗോപികമാർ ആരുടെ നാമങ്ങളാണ് ചൊല്ലിയത്?",
                        "options": [
                            {"text": "ഭഗവാൻ വിഷ്ണുവിന്റെ നാമങ്ങൾ (കേശവ, നാരായണ, മാധവ, ഗോവിന്ദ)", "is_correct": True},
                            {"text": "ഇന്ദ്രന്റെയും അഗ്നിയുടെയും പേരുകൾ", "is_correct": False},
                            {"text": "മഥുരയിലെ രാജാക്കന്മാരുടെ പേരുകൾ", "is_correct": False},
                            {"text": "നക്ഷത്രങ്ങളുടെ പേരുകൾ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പന്ത്രണ്ട് മൈൽ നീളമുള്ള പൂതനയുടെ ശരീരം ഗോപന്മാർ എന്തുചെയ്തു?",
                        "options": [
                            {"text": "കോടാലികൾ കൊണ്ട് കഷണങ്ങളാക്കി ചിതയൊരുക്കി ദഹിപ്പിച്ചു", "is_correct": True},
                            {"text": "കടലിൽ തള്ളി", "is_correct": False},
                            {"text": "മണ്ണിൽ കുഴിച്ചുമൂടി", "is_correct": False},
                            {"text": "വഴിയിൽ ഉപേക്ഷിച്ചു", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പൂതനയുടെ ചിതയിൽനിന്ന് എന്തുതരം സുഗന്ധമാണ് ഉയർന്നത്?",
                        "options": [
                            {"text": "അഗരുവിന്റെയും ചന്ദനത്തിന്റെയും ദിവ്യ സുഗന്ധം", "is_correct": True},
                            {"text": "അസഹനീയമായ ദുർഗന്ധം", "is_correct": False},
                            {"text": "ഇരുമ്പ് കത്തിയ മണം", "is_correct": False},
                            {"text": "യാതൊരു മണവുമുണ്ടായില്ല", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പൂതനയുടെ ചിതയിൽനിന്ന് അഗരുസുഗന്ധം വരാൻ കാരണമെന്തായിരുന്നു?",
                        "options": [
                            {"text": "ശ്രീകൃഷ്ണൻ മുലപ്പാൽ കുടിച്ചതോടെ അവളുടെ പാപങ്ങൾ തീർന്ന് ശരീരം പവിത്രമായി", "is_correct": True},
                            {"text": "വിറകിൽ അത്തർ ഒഴിച്ചിരുന്നു", "is_correct": False},
                            {"text": "ദേവന്മാർ പനിനീർ തളിച്ചു", "is_correct": False},
                            {"text": "പൂതന പൂക്കൾ തിന്നിരുന്നു", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ശ്രീകൃഷ്ണൻ പൂതനയ്ക്ക് നൽകിയ ആധ്യാത്മിക പദവി എന്തായിരുന്നു?",
                        "options": [
                            {"text": "ഗോലോകത്തിൽ നിത്യമായ ധാത്രി അമ്മയുടെ പദവി", "is_correct": True},
                            {"text": "സ്വർഗ്ഗത്തിൽ ഇന്ദ്രാണി പദവി", "is_correct": False},
                            {"text": "ഭൂമിയിൽ രാജ്ഞിയാകാനുള്ള വരം", "is_correct": False},
                            {"text": "നരകത്തിലേക്ക് അയച്ചു", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പൂതന കൊല്ലാൻ വന്നതാണെങ്കിലും ഭഗവാൻ അവളുടെ ഏതു കാര്യമാണ് സ്വീകരിച്ചത്?",
                        "options": [
                            {"text": "അമ്മയെപ്പോലെ മുലപ്പാൽ തന്ന ആ ബാഹ്യസേവയെ മാത്രം", "is_correct": True},
                            {"text": "അവളുടെ സുന്ദര രൂപത്തെ", "is_correct": False},
                            {"text": "കംസനുമായുള്ള ബന്ധത്തെ", "is_correct": False},
                            {"text": "അവളുടെ ശരീരബലത്തെ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പൂതനയുടെ ശവദാഹ സമയത്ത് മഥുരയിൽനിന്ന് തിരിച്ചെത്തിയത് ആരായിരുന്നു?",
                        "options": [
                            {"text": "നന്ദഗോപരും സംഘവും", "is_correct": True},
                            {"text": "കംസനും സൈന്യവും", "is_correct": False},
                            {"text": "നാരദമുനി", "is_correct": False},
                            {"text": "വസുദേവരും ദേവകിയും", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ശവം കണ്ട നന്ദഗോപർക്ക് ആരുടെ മുന്നറിയിപ്പാണ് ഓർമ്മ വന്നത്?",
                        "options": [
                            {"text": "മഥുരയിൽ വസുദേവർ നൽകിയ മുന്നറിയിപ്പ്", "is_correct": True},
                            {"text": "ഒരു പഴയ സ്വപ്നം", "is_correct": False},
                            {"text": "കംസന്റെ കപ്പച്ചീട്ട്", "is_correct": False},
                            {"text": "നാട്ടിലെ മുതിർന്നവരുടെ വാക്ക്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പൂതനയുടെ ചിതയിൽനിന്ന് അഗരുസുഗന്ധം ഉയർന്നതിനെ വർണ്ണിക്കുന്ന ഭാഗവത ശ്ലോകങ്ങൾ ഏവ?",
                        "options": [
                            {"text": "ശ്ലോകങ്ങൾ 37–38", "is_correct": True},
                            {"text": "ശ്ലോകങ്ങൾ 1–2", "is_correct": False},
                            {"text": "ശ്ലോകങ്ങൾ 15–16", "is_correct": False},
                            {"text": "ശ്ലോകങ്ങൾ 43–44", "is_correct": False}
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

        self.stdout.write(self.style.SUCCESS(f"Successfully populated Story 17 (ID: {story.id}) across all 7 languages!"))
