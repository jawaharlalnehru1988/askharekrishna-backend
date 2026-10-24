import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askharekrishna_backend.settings')
django.setup()

from django.core.management.base import BaseCommand
from stories.models import StoryMainTopic, Story, StoryTranslation, StoryQuestion, StoryQuestionOption

class Command(BaseCommand):
    help = "Populate Story 18: The Shattering of the Hand-Cart (Sakatabhanjana) across 7 languages"

    def handle(self, *args, **options):
        topic = StoryMainTopic.objects.get(name="Krishna Pastimes")

        story_slug = "krishna-pastimes-the-shattering-of-the-hand-cart-sakatabhanjana"
        image_path = "stories/images/sakatabhanjana_shattering_cart.jpg"

        story, created = Story.objects.get_or_create(
            slug=story_slug,
            defaults={
                "topic": topic,
                "order": 17,
                "imagePath": image_path,
            }
        )
        if not created:
            story.topic = topic
            story.order = 17
            story.imagePath = image_path
            story.save()

        stories_data = {
            "en": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "The Shattering of the Hand-Cart (Śakaṭāsura-bhañjana)",
                "content": """### The Grand Utthāna-mahotsava in Gokula

When baby Krishna was approximately three months old, Mother Yashoda observed that the child was able to turn Himself over from His back to His belly for the very first time. In ancient Vedic culture, this developmental milestone is celebrated with immense joy through a sacred ritual called the *Utthāna-mahotsava* (the first-turning ceremony), combined with the observation of the child’s auspicious birth-star (*janma-nakṣatra*):

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 7, Verses 4–5**
> 
> *kadācid autthānika-kautukādṛtā*  
> *mahā-manās te prathame 'bda-pūraṇe*  
> *janmarṣa-patta-praśamāya mādhavaṁ*  
> *snāpya dvijaiḥ śasta-padaiḥ sa-maṅgalaiḥ*  
> 
> **Translation:** "When baby Krishna reached three months of age and could turn Himself over, Mother Yashoda joyfully arranged the Utthāna festival. Learned brāhmaṇas gathered to chant auspicious Vedic hymns, perform sacred oblations, and bathe the child in sanctified water for His long life and welfare."

Nanda Maharaja and Mother Yashoda generously distributed cows decorated with gold and silk, along with mountains of grain and sweets, to the venerable brāhmaṇas. Gokula was transformed into a paradise of music, laughter, and chanting. Singers sang melodious songs, mṛdaṅga drums resounded, and all the cowherd men and women gathered in high festive spirits.

### Baby Krishna Placed Beneath the Hand-Cart

After the sacred bath and chanting of Vedic mantras, baby Krishna felt weary from the festive excitement and fell into a peaceful slumber. Mother Yashoda gently swaddled the infant in soft silks. 

Looking for a quiet, shaded place where the loud festivities and courtyard traffic would not disturb the sleeping child, Yashoda placed baby Krishna beneath a large, two-wheeled wooden handcart (*śakaṭa*) parked in the courtyard. This heavy wagon was heavily loaded with large brass pots, copper jugs, and earthen jars filled with milk, yogurt, churned butter, and molasses.

Believing her darling boy was completely safe in the cool shade of the cart, Mother Yashoda hurried off to receive newly arrived guests, honor the brāhmaṇas, and oversee the feast.

### The Playful Kick and the Shattering of Śakaṭāsura

What no one in Gokula knew was that a terrible demon named Śakaṭāsura, dispatched by King Kamsa, had entered the heavy wooden cart! Taking subtle, disembodied possession of the wagon, the demon waited patiently for the right moment to collapse the massive weight of the vehicle and crush baby Krishna beneath its heavy wheels and brass pots.

While lying beneath the cart, baby Krishna woke up feeling hungry. Missing His mother's sweet breast milk, the infant Lord began to cry in mock distress, tossing His tiny arms and kicking His small lotus feet into the air:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 7, Verses 6–9**
> 
> *adhaḥ śayānaḥ śakaṭasya kṛṣṇaḥ*  
> *pranīta-pādo ru-rudan kṣut-tṛṣṇaḥ*  
> *pādābhighātena bibhebha tatra*  
> *pātena bhagno hita-dāru-saṅghaḥ*  
> 
> **Translation:** "Lying beneath the cart, baby Krishna cried out for His mother's breast milk in simulated anger. Tossing His tiny legs, His lotus foot playfully struck the wheel of the handcart. Immediately, the heavy wagon was violently overturned, its wooden axle snapped, wheels shattered into splinters, and all the brass and clay pots smashed to pieces, spilling milk and butter everywhere!"

The touch of the Supreme Lord’s lotus foot possesses infinite potency. Though baby Krishna seemed like a helpless three-month-old infant, His tiny heel struck the cart wheel with the force of a cosmic thunderbolt! 

The demon Śakaṭāsura was instantly slain, his subtle body crushed by the Lord’s divine touch. The heavy wagon violently overturned, spinning into the air and crashing down in ruin. Its heavy axle shattered, the thick wooden wheel hubs split into pieces, and dozens of brass pitchers and clay vessels smashed to fragments, sending rivers of white milk, churned butter, and creamy yogurt splashing across the sunny courtyard!

### The Innocent Eyewitnesses and the Vrajavasis' Wonder

The deafening crash of the shattering wagon sounded like a mountain collapsing, interrupting the festival. Terrified that a disaster had occurred, Mother Yashoda, Nanda Maharaja, the brāhmaṇas, and all the cowherds dropped what they were holding and rushed into the courtyard in sheer panic.

They were stunned to find the massive loaded wagon reduced to splinters. But amidst the broken pottery, scattered timber, and rivers of spilled milk, they saw baby Krishna lying peacefully upon His back, smiling enchantingly, sucking His lotus toe, and completely unharmed!

Relieved beyond words, Mother Yashoda scooped up her divine baby and held Him close to her pounding heart, while Nanda Maharaja and the elder cowherds looked at the wreckage in complete bewilderment: *"How could a stationary, sturdy wagon heavily laden with pots suddenly overturn and shatter without being drawn by bulls or pushed by men?"*

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 7, Verses 13–14**
> 
> *ūcur bālāś ca dṛṣṭveti caritram asureśvare*  
> *bālena hato 'yam iti na śraddadhur dāruṇam*  
> 
> **Translation:** "The young cowherd children playing nearby exclaimed: 'We saw it with our own eyes! This tiny baby began crying and kicked the wheel of the cart with His foot, and immediately the cart broke and flew into pieces!' But the adult cowherds could not believe that such an extraordinary feat could be performed by a fragile infant."

The simple-hearted cowherds could not fathom the supreme transcendental majesty of baby Krishna. They thought the children were simply speaking out of playful imagination. Attributing the baby’s miraculous survival to the divine protection of Lord Vishnu and the auspicious blessings of the brāhmaṇas, Nanda Maharaja immediately arranged for further Vedic sacrifices and gave more cows in charity, rejoicing in the safety of his beloved child!""",
                "questions": [
                    {
                        "question": "On which auspicious occasion did the pastime of shattering the handcart take place?",
                        "options": [
                            {"text": "During the Utthana-mahotsava (first-turning ceremony) at three months of age", "is_correct": True},
                            {"text": "During the Govardhana Puja", "is_correct": False},
                            {"text": "During the Rasa dance festival", "is_correct": False},
                            {"text": "During the marriage of Vasudeva", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Where did Mother Yashoda place baby Krishna to sleep while she attended to guests?",
                        "options": [
                            {"text": "Beneath a large, two-wheeled wooden handcart (sakata) in the shade", "is_correct": True},
                            {"text": "Inside a deep underground cave", "is_correct": False},
                            {"text": "On the roof of the palace", "is_correct": False},
                            {"text": "Inside a boat on the Yamuna River", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What was loaded upon the heavy wooden handcart?",
                        "options": [
                            {"text": "Heavy brass and clay vessels filled with milk, curd, butter, and molasses", "is_correct": True},
                            {"text": "Swords and iron shields", "is_correct": False},
                            {"text": "Gold bricks from Mathura", "is_correct": False},
                            {"text": "Dry firewood and stones", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Which demon sent by Kamsa had taken subtle possession of the wooden cart to crush Krishna?",
                        "options": [
                            {"text": "Sakatasura (the cart demon)", "is_correct": True},
                            {"text": "Trinavarta", "is_correct": False},
                            {"text": "Aghasura", "is_correct": False},
                            {"text": "Bakasura", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Why did baby Krishna begin to cry and kick His feet in the air?",
                        "options": [
                            {"text": "He woke up feeling hungry and wanted His mother's breast milk", "is_correct": True},
                            {"text": "He was bitten by an ant", "is_correct": False},
                            {"text": "He was terrified of the dark", "is_correct": False},
                            {"text": "He was calling for Balarama", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What happened when baby Krishna's tiny lotus foot struck the wheel of the cart?",
                        "options": [
                            {"text": "The cart violently overturned, the axle and wheels shattered into splinters, and the demon was slain", "is_correct": True},
                            {"text": "The wheel turned into solid gold", "is_correct": False},
                            {"text": "Nothing happened at all", "is_correct": False},
                            {"text": "The cart smoothly rolled into the forest", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Who witnessed the event and told the adult cowherds that baby Krishna kicked the cart?",
                        "options": [
                            {"text": "The small cowherd children playing nearby in the courtyard", "is_correct": True},
                            {"text": "King Kamsa's royal spies", "is_correct": False},
                            {"text": "Sage Narada Muni from the sky", "is_correct": False},
                            {"text": "The pet parrots of Yashoda", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Why did the adult cowherds find it difficult to believe the children's account?",
                        "options": [
                            {"text": "They thought it was impossible for a tiny three-month-old infant to shatter a massive loaded wagon", "is_correct": True},
                            {"text": "They believed the children were lying for fun", "is_correct": False},
                            {"text": "They were angry at the children", "is_correct": False},
                            {"text": "They thought a storm blew the cart away", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How was baby Krishna found by Mother Yashoda amidst the shattered wreckage?",
                        "options": [
                            {"text": "Lying peacefully upon His back, smiling happily and sucking His lotus toe, completely unharmed", "is_correct": True},
                            {"text": "Bleeding and weeping loudly", "is_correct": False},
                            {"text": "Hidden under a pile of butter", "is_correct": False},
                            {"text": "Trapped under the heavy wheel", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Which chapter of Srimad-Bhagavatam Canto 10 describes the pastime of Sakatabhanjana?",
                        "options": [
                            {"text": "Chapter 7", "is_correct": True},
                            {"text": "Chapter 2", "is_correct": False},
                            {"text": "Chapter 5", "is_correct": False},
                            {"text": "Chapter 12", "is_correct": False}
                        ]
                    }
                ]
            },
            "ta": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "சகடாசுர வதம் மற்றும் வண்டி உடைந்த லீலை",
                "content": """### கோகுலத்தில் நிகழ்ந்த திவ்யமான உத்தான மகோற்சவம்

பால கிருஷ்ணருக்கு சுமார் மூன்று மாதங்கள் நிரம்பிய போது, அவர் முதன்முதலாகப் படுக்கையிலிருந்து தன் முதுகைத் திருப்பி, குப்புறப் படுக்கும் திருப்புமுனையை அன்னை யசோதை கண்டாள். தொன்மையான வைதீகப் பண்பாட்டில், குழந்தையின் இந்த வளர்ச்சியை *உத்தான மகோற்சவம்* (குழந்தை திரும்பும் விழா) என்றும், குழந்தையின் ஜென்ம நட்சத்திர தின விழா என்றும் கோலாகலமாகக் கொண்டாடுவது மரபாகும்:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 7, சுலோகங்கள் 4–5**
> 
> *கதாசித் ஔத்தானிக-கௌதுகாத்ருதா*  
> *மஹா-மனாஸ் தே ப்ரதமே ப்த-பூரணே*  
> *ஜன்மர்ஷ-பத்த-ப்ரசமாய மாதவம்*  
> *ஸ்நாப்ய த்விஜை: சஸ்த-பதை: ஸ-மங்களை:*  
> 
> **பொருள்:** "பால கிருஷ்ணருக்கு மூன்று மாதங்கள் முடிந்து, குழந்தை தன் உடலைத் திருப்பிப் படுத்த உத்தான நன்னாளில், அன்னை யசோதை பெருமகிழ்ச்சியோடு விழாவை நடத்தினாள். வேதம் கற்ற பிராமணர்கள் மங்களகரமான மந்திரங்களை முழங்க, குழந்தையின் ஆயுளும் நன்மையும் பெருக திருமுழுக்காட்டுச் சடங்கினைச் செய்தனர்."

நந்த மகாராஜரும் அன்னை யசோதையும் பொன்னாலும் பட்டாலும் அலங்கரிக்கப்பட்ட பசுக்களையும், தானியக் குவியல்களையும் பிராமணர்களுக்கு வாரி வழங்கினர். இசை, மங்கல முழக்கம், நடனம் ஆகியவற்றால் கோகுலமே பரவசமடைந்தது.

### வண்டியின் நிழலில் உறங்க வைக்கப்பட்ட பால கிருஷ்ணர்

திருமுழுக்கு மற்றும் மங்கள வழிபாடுகள் முடிந்ததும், திருவிழாக் கொண்டாட்டங்களால் சோர்வடைந்த பால கிருஷ்ணர் இனிதாகக் கண்ணயர்ந்தார். அன்னை யசோதை அவரை மென்மையான பட்டுத் துணியில் பொதிந்து தூக்கினாள்.

முற்றத்தில் விருந்தினர்களின் நடமாட்டமும், மங்கள வாத்தியங்களின் பேரொலியும் குழந்தையின் உறக்கத்தைக் கலைத்துவிடக் கூடாது என்று கருதிய யசோதை, முற்றத்தின் ஓரத்தில் நின்றுகொண்டிருந்த ஒரு பெரிய மர மாட்டு வண்டியின் நிழலில் மெத்தையை விரித்து பால கிருஷ்ணரைப் படுக்க வைத்தாள். அந்த வண்டியில் பித்தளைப் பானைகள், வெண்கலக் குடங்கள், பால், தயிர், வெண்ணெய் நிரம்பிய பெரிய மண்பானைகள் ஆகியவை மிகக் கனமாக ஏற்றப்பட்டிருந்தன.

குழந்தை நிழலில் பாதுகாப்பாக உறங்குவதாகக் கருதிய அன்னை யசோதை, புதிதாக வந்த விருந்தினர்களை உபசரிக்கவும், பிராமணர்களுக்கு அன்னதானம் வழங்கவும் விரைந்து சென்றாள்.

### குழந்தையின் திருவடி பட்டதும் நொறுங்கிய சகடாசுரன்

ஆனால் கோகுலத்தில் யாருக்கும் தெரியாத ஒரு கொடிய உண்மை அங்கே மறைந்திருந்தது! கம்சனால் ஏவப்பட்ட சகடாசுரன் என்னும் அரக்கன், அந்தப் பாரமான மர வண்டியில் அரூபமாகப் புகுந்திருந்தான்! அந்த வண்டியின் மாபெரும் எடையை அப்படியே சரித்து, பால கிருஷ்ணரை அடியில் வைத்து நசுக்கிக் கொன்றுவிட வேண்டும் என்பதே அவனுடைய கொடிய திட்டம்.

வண்டியின் அடியில் படுத்திருந்த பால கிருஷ்ணர் பசியோடு விழித்தெழுந்தார். தாய்ப்பாலைக் காணாத பகவான், செல்லமாகக் கோபம் கொண்டவரைப் போல அழுதபடி, தன் தாமரை மலர்ப் பாதங்களை வானை நோக்கி உதைத்து விளையாடத் தொடங்கினார்:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 7, சுலோகங்கள் 6–9**
> 
> *அத: சயான: சகடஸ்ய க்ருஷ்ண:*  
> *ப்ரநீத-பாதோ ரு-ருதன் க்ஷுத்-த்ருஷ்ண:*  
> *பாதாபிகாதேன பிபேப தத்ர*  
> *பாதேன பக்னோ ஹித-தாரு-ஸங்க:*  
> 
> **பொருள்:** "வண்டியின் அடியில் படுத்திருந்த பால கிருஷ்ணர், தாய்ப்பால் அருந்தும் ஆசையோடு அழுதபடி தம் சிறு பாதங்களை அசைத்தார். விளையாட்டாக அவரது தாமரைத் திருவடி அந்த வண்டிச் சக்கரத்தைத் தீண்டியது. அடுத்த கணமே, அந்த மாபெரும் வண்டி தலைகீழாகப் புரண்டு, அச்சு முறிந்து, சக்கரங்கள் சுக்குநூறாக நொறுங்கின; வண்டியில் இருந்த பாண்டங்கள் அனைத்தும் உடைந்து, எங்கும் பாலும் வெண்ணெயும் ஆறாகப் பாய்ந்தது!"

முழுமுதற் கடவுளான பகவானின் தாமரை மலர்த் திருவடிகள் அளப்பரிய தெய்வீக சக்தி கொண்டவை. மூன்று மாதப் பச்சிளங்குழந்தையின் சிறிய குதிங்கால் பட்ட மாத்திரத்திலேயே, வஜ்ராயுதம் தாக்கியது போல வண்டி உருக்குலைந்தது!

சகடாசுரன் நொடிப்பொழுதில் உயிரிழந்து மடிந்தான். அந்தப் பிரம்மாண்ட வண்டி காற்றில் சுழன்று கீழே விழுந்தது. அதன் மரச்சக்கரங்கள் தூள்தூளாயின; இரும்பு அச்சுகள் முறிந்தன; வண்டியில் இருந்த வெண்கலப் பாத்திரங்களும், மண்பானைகளும் உடைந்து நொறுங்கி, முற்றமெங்கும் பாலும் நெய்யும் வெண்ணெயும் ஆறாக ஓடின!

### சிறுவர்கள் கூறிய உண்மையும் ஆயர்களின் திகைப்பும்

வண்டி வெடித்து நொறுங்கிய சத்தம் ஒரு மாபெரும் மலை சரிவது போலக் கேட்டது. பேரதிர்ச்சியடைந்த நந்த மகாராஜர், அன்னை யசோதை, பிராமணர்கள் மற்றும் கோகுலத்து மக்கள் அனைவரும் கைகளில் இருந்த தட்டுகளைப் போட்டுவிட்டுப் பதறியடித்துக் கொண்டு முற்றத்திற்கு ஓடிவந்தனர்.

அங்கே சுக்குநூறாக உடைந்த மரத்துண்டுகளையும், கொட்டிக் கிடந்த பால் தயிரையும் கண்டு அவர்கள் நடுங்கிப் போயினர். ஆனால், அந்த இடிபாடுகளுக்கு நடுவே, பால கிருஷ்ணர் எவ்வித காயமுமின்றி, தன் கால் கட்டைவிரலை வாயில் வைத்துச் சுவைத்தபடி, மல்லாந்து படுத்து ஆனந்தமாகச் சிரித்துக் கொண்டிருந்தார்!

அளவற்ற நிம்மதியோடும் தாய்மைப் பாசத்தோடும் அன்னை யசோதை குழந்தையை வாரி அணைத்துத் தன் மார்போடு சேர்த்துக்கொண்டாள். மாடுகளோ மனிதர்களோ இழுக்காமல், தானாகவே நின்றுகொண்டிருந்த ஒரு கனமான வண்டி எப்படித் திடீரெனச் சுக்குநூறாக நொறுங்கி விழுந்தது என்று நந்தரும் பெரியவர்களும் விழித்தனர்:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 7, சுலோகங்கள் 13–14**
> 
> *ஊசுர் பாலாஸ் ச த்ருஷ்ட்வேதி சரித்ரம் அஸுரேஸ்வரே*  
> *பாலேன ஹதோ யம் இதி ந ச்ரத்ததுர் தாருணம்*  
> 
> **பொருள்:** "அங்கே விளையாடிக்கொண்டிருந்த சிறுவர்கள், 'நாங்கள் எங்கள் கண்களால் பார்த்தோம்! இந்தக் குழந்தை அழுதபடி தன் காலால் உதைத்த உடனே இந்த வண்டி பறந்து போய் உடைந்தது!' என்று கூறினர். ஆனால், இவ்வளவு சிறிய பச்சிளங்குழந்தை இத்தகைய மாபெரும் வண்டியை உதைத்து உடைக்க முடியும் என்பதைப் பெரியவர்களால் நம்ப முடியவில்லை."

அப்பாவிகளான ஆயர்கள் பால கிருஷ்ணரின் பரத்துவத்தை முழுமையாக உணரவில்லை. சிறுவர்கள் விளையாட்டாகக் கூறுகிறார்கள் என்றே அவர்கள் கருதினர். விஷ்ணு பகவானின் திருவருளாலும், பிராமணர்களின் மங்கள ஆசிகளாலுமே குழந்தை உயிர் தப்பியது என்று நம்பிய நந்த மகாராஜர், மேலும் பல பசுக்களையும் தானங்களையும் வழங்கித் தன் பாசக் குழந்தையின் நல்வாழ்விற்காகப் பிரார்த்தித்தார்!""",
                "questions": [
                    {
                        "question": "வண்டி உடைந்த இந்த திவ்ய லீலை எந்த மங்களகரமான விழாவின் போது நிகழ்ந்தது?",
                        "options": [
                            {"text": "உத்தான மகோற்சவம் (குழந்தை திரும்பும் மூன்று மாத விழா)", "is_correct": True},
                            {"text": "கோவர்த்தன பூஜை", "is_correct": False},
                            {"text": "ராஸ லீலை விழா", "is_correct": False},
                            {"text": "வசுதேவரின் திருமண விழா", "is_correct": False}
                        ]
                    },
                    {
                        "question": "விருந்தினர்களை உபசரிக்கும் போது பால கிருஷ்ணரை யசோதை எங்கே படுக்க வைத்தாள்?",
                        "options": [
                            {"text": "முற்றத்தில் நின்றுகொண்டிருந்த ஒரு பெரிய மர மாட்டு வண்டியின் நிழலில்", "is_correct": True},
                            {"text": "ஒரு ஆழமான குகையில்", "is_correct": False},
                            {"text": "மாளிகையின் கூரையில்", "is_correct": False},
                            {"text": "யமுனை நதியில் உள்ள படகில்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "அந்தப் பாரமான மர வண்டியில் என்ன ஏற்றப்பட்டிருந்தது?",
                        "options": [
                            {"text": "பால், தயிர், வெண்ணெய் நிரம்பிய கனமான வெண்கலப் பாண்டங்களும் மண்பானைகளும்", "is_correct": True},
                            {"text": "போர்க்கருவிகளும் வாள்களும்", "is_correct": False},
                            {"text": "மதுராவிலிருந்து வந்த தங்கக் கட்டிகள்", "is_correct": False},
                            {"text": "விறகுக் கட்டைகளும் கற்களும்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "குழந்தையைக் கொல்வதற்காக அந்த வண்டியில் அரூபமாகப் புகுந்திருந்த அசுரன் யார்?",
                        "options": [
                            {"text": "சகடாசுரன்", "is_correct": True},
                            {"text": "திருணாவர்த்தன்", "is_correct": False},
                            {"text": "அகாசுரன்", "is_correct": False},
                            {"text": "பகாசுரன்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பால கிருஷ்ணர் ஏன் அழுதபடி தன் கால்களை வானை நோக்கி உதைத்தார்?",
                        "options": [
                            {"text": "பசியோடு விழித்தெழுந்து தாய்ப்பால் அருந்த விரும்பியதால்", "is_correct": True},
                            {"text": "எறும்பு கடித்ததால்", "is_correct": False},
                            {"text": "இருட்டைக் கண்டு பயந்ததால்", "is_correct": False},
                            {"text": "பலராமரைக் கூப்பிடுவதற்காக", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பால கிருஷ்ணரின் தாமரைத் திருவடி பட்டதும் வண்டிக்கு என்ன நேர்ந்தது?",
                        "options": [
                            {"text": "வண்டி தலைகீழாகப் புரண்டு, சக்கரங்களும் அச்சும் சுக்குநூறாக நொறுங்கி அசுரன் மடிந்தான்", "is_correct": True},
                            {"text": "வண்டி தங்கமாக மாறியது", "is_correct": False},
                            {"text": "வண்டிக்கு எதுவுமே ஆகவில்லை", "is_correct": False},
                            {"text": "வண்டி தானாகக் காட்டுக்குள் ஓடியது", "is_correct": False}
                        ]
                    },
                    {
                        "question": "குழந்தை காலால் உதைத்து வண்டியை உடைத்ததைக் கண்ணாரக் கண்ட சாட்சிகள் யார்?",
                        "options": [
                            {"text": "முற்றத்தில் விளையாடிக்கொண்டிருந்த சிறுவர்கள்", "is_correct": True},
                            {"text": "கம்சனின் ஒற்றர்கள்", "is_correct": False},
                            {"text": "வானில் இருந்த நாரத முனிவர்", "is_correct": False},
                            {"text": "யசோதையின் கிளிகள்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "சிறுவர்கள் கூறியதை ஆயர்களால் ஏன் எளிதில் நம்ப முடியவில்லை?",
                        "options": [
                            {"text": "மூன்று மாதக் குழந்தை இவ்வளவு பெரிய வண்டியை உடைக்க முடியாது என்று அவர்கள் எண்ணியதால்", "is_correct": True},
                            {"text": "சிறுவர்கள் பொய் சொல்கிறார்கள் என்று கோபப்பட்டதால்", "is_correct": False},
                            {"text": "புயல் காற்றால் வண்டி உடைந்ததாக நினைத்ததால்", "is_correct": False},
                            {"text": "அவர்கள் சிறுவர்களைப் புறக்கணித்ததால்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "இடிபாடுகளுக்கு நடுவே பால கிருஷ்ணர் எவ்வாறு காணப்பட்டார்?",
                        "options": [
                            {"text": "எந்தக் காயமுமின்றி, சிரித்தபடி தன் கால் கட்டைவிரலைச் சுவைத்துக்கொண்டிருந்தார்", "is_correct": True},
                            {"text": "ரத்தக் காயங்களோடு அழுதுகொண்டிருந்தார்", "is_correct": False},
                            {"text": "வெண்ணெய் பானைக்குள் ஒளிந்திருந்தார்", "is_correct": False},
                            {"text": "சக்கரத்தின் அடியில் மாட்டிக்கொண்டிருந்தார்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "சகடாசுர வதத்தை விவரிக்கும் ஸ்ரீமத் பாகவதம் பத்தாம் ஸ்கந்தத்தின் அத்தியாயம் எது?",
                        "options": [
                            {"text": "அத்தியாயம் 7", "is_correct": True},
                            {"text": "அத்தியாயம் 2", "is_correct": False},
                            {"text": "அத்தியாயம் 5", "is_correct": False},
                            {"text": "அத்தியாயம் 12", "is_correct": False}
                        ]
                    }
                ]
            },
            "hi": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "शकटासुर वध और छकड़े का टूटना",
                "content": """### गोकुल में भव्य उत्थान महोत्सव

जब बालकृष्ण लगभग तीन मास के हुए, तब माता यशोदा ने देखा कि बालक पहली बार पीठ के बल से पेट के बल उलटने लगा है। वैदिक संस्कृति में बालक के इस प्रथम करवट बदलने के अवसर को *उत्थान महोत्सव* के रूप में बड़े धूमधाम से मनाया जाता है, जो बालक के जन्म-नक्षत्र के दिन संपन्न किया गया:

> **श्रीमद्-भागवतम, स्कंध 10, अध्याय 7, श्लोक 4–5**
> 
> *कदाचिदौत्थानिककौतुकादृता*  
> *महामनास्ते प्रथमेऽब्दपूरणे*  
> *जन्मर्षपत्तप्रशमाय माधवं*  
> *स्नाप्य द्विजैः शस्तपदैः सुमङ्गलैः*  
> 
> **भावार्थ:** "जब बालकृष्ण तीन महीने के होकर पहली बार करवट बदलने लगे, तब माता यशोदा ने बड़े हर्षोल्लास से उत्थान महोत्सव का आयोजन किया। वेदपाठी ब्राह्मणों ने बालक के कल्याण और दीर्घायु के लिए मंगलमय मंत्रों के साथ उनका अभिषेक किया।"

नंद महाराज और माता यशोदा ने ब्राह्मणों को सुवर्ण और रेशम से सजी गौएं तथा प्रचुर अन्न-धन दान में दिया। गोकुल में मंगल गान, मृदंग की ध्वनि और आनंद का सागर उमड़ पड़ा।

### छकड़े (बैलगाड़ी) के नीचे बालकृष्ण का शयन

अभिषेक और वैदिक अनुष्ठानों के उपरांत, उत्सव के कोलाहल से थककर बालकृष्ण सो गए। माता यशोदा ने उन्हें कोमल रेशमी वस्त्र में लपेटा।

आंगन में अतिथियों की भीड़ और बाजों की ध्वनि से बालक की नींद न टूटे, इसलिए यशोदा ने उन्हें आंगन में खड़े एक बड़े छकड़े (गाड़ी) के नीचे सुला दिया। उस छकड़े पर दूध, दही, माखन और गुड़ से भरे भारी पीतल, तांबे और मिट्टी के विशाल घड़े लदे हुए थे।

बालक को छकड़े की शीतल छाया में सुरक्षित मानकर, माता यशोदा आए हुए अतिथियों के सत्कार और ब्राह्मणों को भोजन कराने में व्यस्त हो गईं।

### बालकृष्ण का चरण-प्रहार और शकटासुर का उद्धार

गोकुल में कोई नहीं जानता था कि कंस द्वारा भेजा गया शकटासुर नामक एक भयानक असुर उस छकड़े में अदृश्य रूप से प्रवेश कर चुका था! वह इसी ताक में था कि भारी छकड़े को उलटकर बालक कृष्ण को उसके नीचे कुचल डाले।

छकड़े के नीचे लेटे बालकृष्ण की नींद खुली और उन्हें भूख लगी। माता का स्तनपान न पाकर भगवान क्रोधित बालक की भांति रोने लगे और अपने नन्हे चरणकमलों को आकाश में उछालने लगे:

> **श्रीमद्-भागवतम, स्कंध 10, अध्याय 7, श्लोक 6–9**
> 
> *अधः शयानः शकटस्य कृष्णः*  
> *प्रणीतपादो रुरुदन् क्षुतृष्णः*  
> *पादाभिघातेन बिभेभ तत्र*  
> *पातेन भग्नोहिरदारुसङ्घः*  
> 
> **भावार्थ:** "छकड़े के नीचे लेटे बालकृष्ण भूख से व्याकुल होकर रोने लगे और अपने चरण उछालने लगे। खेलते-खेलते उनका चरणकमल छकड़े के पहिए से छू गया। तत्काल वह भारी छकड़ा उलट गया, उसकी धुरी टूट गई, पहिए चूर-चूर हो गए और समस्त बर्तन टूटकर चारों ओर दूध-दही की नदियां बह निकलीं!"

पूर्ण पुरुषोत्तम भगवान के चरणकमलों में अनंत सामर्थ्य है। यद्यपि बालकृष्ण केवल तीन महीने के अबोध शिशु दिख रहे थे, किंतु उनकी एड़ी का हल्का सा स्पर्श वज्रपात बन गया!

छकड़े में स्थित शकटासुर तत्काल मारा गया। वह विशाल छकड़ा हवा में उछलकर औंधे मुंह गिरा। उसकी धुरी टूट गई, पहियों के टुकड़े-टुकड़े हो गए और पीतल व मिट्टी के घड़े फूटकर आंगन में माखन-मिश्री और दूध की धाराएं बहने लगीं!

### बालकों की गवाही और ब्रजवासियों का विस्मय

छकड़े के टूटने का भयंकर शब्द सुनकर नंद महाराज, माता यशोदा और सभी गोप-गोपियां घबराकर आंगन की ओर दौड़े।

वहां छकड़े के टूटे हुए टुकड़ों और बिखरे हुए बर्तनों को देखकर सभी भयभीत हो गए। किंतु मलबे के बीच जब उन्होंने बालकृष्ण को सुरक्षित, हंसते हुए और अपने पैर का अंगूठा चूसते देखा, तो माताओं के प्राण लौट आए!

माता यशोदा ने बालक को तुरंत गोद में उठा लिया। नंद महाराज और वृद्ध गोप आश्चर्यचकित होकर सोचने लगे कि बिना किसी बैल या मनुष्य के खींचे यह भारी छकड़ा अपने आप कैसे टूट गया:

> **श्रीमद्-भागवतम, स्कंध 10, अध्याय 7, श्लोक 13–14**
> 
> *ऊचुर्बालाश्च दृष्ट्वेति चरित्रमसुरेश्वरे*  
> *बालेन हतोऽयमिति न श्रद्दधुर्दारुणम्*  
> 
> **भावार्थ:** "पास में खेल रहे ग्वाल-बालकों ने कहा: 'हमने अपनी आंखों से देखा है! इस नन्हे बालक ने रोते हुए अपने पैर से छकड़े को मारा और यह गाड़ी उड़कर टूट गई!' किंतु बड़े लोग विश्वास नहीं कर सके कि इतना छोटा बालक इतने भारी छकड़े को तोड़ सकता है।"

गोकुल के सरल हृदय गोप यह नहीं समझ सके कि यह स्वयं भगवान की लीला है। उन्होंने बालकों की बात को बाल-सुलभ कल्पना समझा और भगवान नारायण की कृपा मानकर नंद महाराज ने पुनः ब्राह्मणों को गौ-दान दिया और बालक के कल्याण की प्रार्थना की!""",
                "questions": [
                    {
                        "question": "छकड़ा टूटने की यह लीला किस उत्सव के दिन हुई?",
                        "options": [
                            {"text": "उत्थान महोत्सव (तीन महीने पर बालक के करवट बदलने का उत्सव)", "is_correct": True},
                            {"text": "गोवर्धन पूजा", "is_correct": False},
                            {"text": "रासलीला उत्सव", "is_correct": False},
                            {"text": "वसुदेव जी का विवाह", "is_correct": False}
                        ]
                    },
                    {
                        "question": "माता यशोदा ने बालकृष्ण को कहां सुलाया था?",
                        "options": [
                            {"text": "आंगन में खड़े एक भारी छकड़े (बैलगाड़ी) की छाया में", "is_correct": True},
                            {"text": "एक गहरी गुफा में", "is_correct": False},
                            {"text": "महल की छत पर", "is_correct": False},
                            {"text": "यमुना में नाव पर", "is_correct": False}
                        ]
                    },
                    {
                        "question": "उस भारी छकड़े पर क्या लदा हुआ था?",
                        "options": [
                            {"text": "दूध, दही, माखन और गुड़ से भरे भारी धातु व मिट्टी के घड़े", "is_correct": True},
                            {"text": "अस्त्र-शस्त्र और तलवारें", "is_correct": False},
                            {"text": "मथुरा का सोना", "is_correct": False},
                            {"text": "लकड़ी और पत्थर", "is_correct": False}
                        ]
                    },
                    {
                        "question": "छकड़े में कौन सा असुर छिपकर बैठा था?",
                        "options": [
                            {"text": "शकटासुर", "is_correct": True},
                            {"text": "तृणावर्त", "is_correct": False},
                            {"text": "अघासुर", "is_correct": False},
                            {"text": "बकासुर", "is_correct": False}
                        ]
                    },
                    {
                        "question": "बालकृष्ण रोते हुए पैर क्यों उछालने लगे?",
                        "options": [
                            {"text": "भूख लगने पर माता का दूध पीने के लिए", "is_correct": True},
                            {"text": "चींटी काटने के कारण", "is_correct": False},
                            {"text": "अंधेरे से डरकर", "is_correct": False},
                            {"text": "बलराम को बुलाने के लिए", "is_correct": False}
                        ]
                    },
                    {
                        "question": "बालकृष्ण के चरण का स्पर्श होते ही छकड़े का क्या हुआ?",
                        "options": [
                            {"text": "छकड़ा उलट गया, धुरी व पहिए टूटकर बिखर गए और असुर मारा गया", "is_correct": True},
                            {"text": "छकड़ा सोने का बन गया", "is_correct": False},
                            {"text": "छकड़े को कुछ नहीं हुआ", "is_correct": False},
                            {"text": "छकड़ा जंगल की ओर चल पड़ा", "is_correct": False}
                        ]
                    },
                    {
                        "question": "किसने देखा कि बालक के पैर से छकड़ा टूटा है?",
                        "options": [
                            {"text": "पास में खेल रहे नन्हे ग्वाल-बालकों ने", "is_correct": True},
                            {"text": "कंस के गुप्तचरों ने", "is_correct": False},
                            {"text": "नारद मुनि ने", "is_correct": False},
                            {"text": "यशोदा के तोते ने", "is_correct": False}
                        ]
                    },
                    {
                        "question": "बड़े गोपों ने बालकों की बात पर विश्वास क्यों नहीं किया?",
                        "options": [
                            {"text": "क्योंकि तीन महीने का नन्हा बालक भारी छकड़ा तोड़ दे, यह असंभव लगा", "is_correct": True},
                            {"text": "क्योंकि बालक झूठ बोल रहे थे", "is_correct": False},
                            {"text": "क्योंकि वे नाराज थे", "is_correct": False},
                            {"text": "क्योंकि आंधी आई थी", "is_correct": False}
                        ]
                    },
                    {
                        "question": "टूटे मलबे के बीच बालकृष्ण किस स्थिति में मिले?",
                        "options": [
                            {"text": "सुरक्षित हंसते हुए और पैर का अंगूठा चूसते हुए", "is_correct": True},
                            {"text": "रक्त से लथपथ होकर रोते हुए", "is_correct": False},
                            {"text": "माखन के मटके में छिपे हुए", "is_correct": False},
                            {"text": "पहिए के नीचे दबे हुए", "is_correct": False}
                        ]
                    },
                    {
                        "question": "शकटासुर वध की यह कथा श्रीमद्-भागवतम के किस अध्याय में आती है?",
                        "options": [
                            {"text": "अध्याय 7", "is_correct": True},
                            {"text": "अध्याय 2", "is_correct": False},
                            {"text": "अध्याय 5", "is_correct": False},
                            {"text": "अध्याय 12", "is_correct": False}
                        ]
                    }
                ]
            },
            "bn": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "শকটা সুর বধ ও শকট ভঞ্জন লীলা",
                "content": """### গোকুলে মহা উত্থান মহোৎসব

শ্রীকৃষ্ণের বয়স যখন প্রায় তিন মাস, তখন মা যশোদা লক্ষ্য করলেন যে শিশুটি প্রথমবার পিঠ থেকে উপুড় হয়ে পাশ ফিরে শোয়ার চেষ্টা করছে। সনাতন বৈদিক সংস্কৃতিতে শিশুর এই প্রথম পাশ ফেরার শুভ মুহূর্তকে *উত্থান মহোৎসব* বলা হয় এবং শিশুর জন্ম-নক্ষত্রের দিনে এই উৎসব আড়ম্বরের সাথে পালিত হলো:

> **শ্রীমদ্ভাগবতম, স্কন্ধ ১০, অধ্যায় ৭, শ্লোক ৪–৫**
> 
> *কদাচিদৌত্থানিককৌতুকাদৃতা*  
> *মহামনাস্তে প্রথমেঽব্দপূরণে*  
> *জন্মর্ষপত্তপ্রশমায় মাধবং*  
> *স্নাপ্য দ্বিজৈঃ শস্তপদৈঃ সুমঙ্গলৈঃ*  
> 
> **অনুবাদ:** "যখন শিশু কৃষ্ণ তিন মাস বয়সে প্রথম পাশ ফিরলেন, তখন মা যশোদা মহা আনন্দের সাথে উত্থান উৎসবের আয়োজন করলেন। বেদজ্ঞ ব্রাহ্মণগণ শিশুর দীর্ঘায়ু ও কল্যাণের জন্য শুভ বৈদিক মন্ত্রোচ্চারণ করে তাঁকে স্নান করালেন।"

নন্দ মহারাজ ও মা যশোদা ব্রাহ্মণদের স্বর্ণ ও রেশমে সুসজ্জিত বহু গাভী ও প্রচুর শস্য দান করলেন। গোকুল সঙ্গীত, আনন্দধ্বনি ও উল্লাসে মুখরিত হয়ে উঠল।

### মালবাহী শকটের (গাড়ির) নিচে শিশু কৃষ্ণের শয়ন

উৎসবের কোলাহলে ক্লান্ত হয়ে শিশু কৃষ্ণ ঘুমিয়ে পড়লেন। মা যশোদা তাঁকে নরম রেশমি কাপড়ে মুড়ে দিলেন।

আঙিনায় অতিথিদের ভিড়ে শিশুর নিদ্রায় ব্যাঘাত ঘটবে ভেবে, যশোদা তাঁকে আঙিনায় দাঁড়িয়ে থাকা একটি বিশাল দুই চাকার কাঠের মালবাহী গাড়ির (শকট) নিচে ছায়ায় শুইয়ে দিলেন। সেই শকটে দুধ, দই, মাখন ও গুড়ে ভরা ভারী পিতল, কাঁসা ও মাটির বড় বড় কলসি বোঝাই করা ছিল।

শিশু ছায়ায় নিরাপদে ঘুমোচ্ছে ভেবে মা যশোদা সমাগত অতিথিদের অভ্যর্থনা ও ব্রাহ্মণদের ভোজন পরিবেশনে ব্যস্ত হয়ে পড়লেন।

### চরণস্পর্শে শকটা সুরের ধ্বংস

গোকুলবাসীদের অজ্ঞাতসারে কংসের পাঠানো শকটা সুর নামক এক রাক্ষস সেই কাঠের গাড়ির মধ্যে অদৃশ্যভাবে আশ্রয় নিয়েছিল! তার কুচক্র ছিল ভারী গাড়িটি উল্টে ফেলে তার নিচে নিষ্পেষিত করে শিশু কৃষ্ণকে হত্যা করা।

শকটের নিচে শুয়ে থাকা শিশু কৃষ্ণ ক্ষুধা পেয়ে জেগে উঠলেন। স্তনদুগ্ধের আশায় তিনি কৃত্রিম ক্রোধ প্রকাশ করে কাঁদতে লাগলেন এবং তাঁর ক্ষুদ্র চরণকমল দুটি আকাশে ছুঁড়তে লাগলেন:

> **শ্রীমদ্ভাগবতম, স্কন্ধ ১০, অধ্যায় ৭, শ্লোক ৬–৯**
> 
> *অধঃ শয়ানঃ শকটস্য কৃষ্ণঃ*  
> *প্রণীতপাদো রুরুদন্ ক্ষুতৃষ্ণঃ*  
> *পাদাভিঘাতেন বিভেভ তত্র*  
> *পাতেন ভগ্নোহিরদারুসঙ্ঘঃ*  
> 
> **অনুবাদ:** "গাড়ির নিচে শয়ান শিশু কৃষ্ণ ক্ষুধার্ত হয়ে কাঁদতে লাগলেন এবং পা ছুঁড়তে লাগলেন। তাঁর কোমল চরণকমল অসাবধানতাবশত গাড়ির চাকায় স্পর্শ করল। তৎক্ষণাৎ সেই বিশাল শকট উল্টে গিয়ে চূর্ণবিচূর্ণ হলো, চাকা ও অক্ষদণ্ড ভেঙে টুকরো টুকরো হলো এবং সমস্ত পাত্র ভেঙে দুধ-দইয়ের নদী বয়ে গেল!"

পরমেশ্বর ভগবানের চরণকমলের শক্তি অসীম। তিন মাসের শিশুর সামান্য চরণের আঘাতে বজ্রপাতের মতো শব্দ হলো!

শকটা সুর তৎক্ষণাৎ নিহত হলো। বিশাল শকটটি শূন্যে উল্টে পড়ে ভেঙে গেল। ভারী কাঠের চাকা ও অক্ষদণ্ড ভেঙে টুকরো টুকরো হলো এবং শত শত মাটির ও ধাতুর কলসি ভেঙে আঙিনাময় দুধ, দই ও মাখনের স্রোত বইতে লাগল!

### শিশুদের প্রত্যক্ষ সাক্ষ্য ও ব্রজবাসীদের বিস্ময়

গাড়ি ভাঙার বজ্রসম শব্দ শুনে নন্দ মহারাজ, মা যশোদা ও ব্রজবাসীরা আতঙ্কিত হয়ে ছুটে এলেন।

সেখানে এসে গাড়ির ভগ্নাবশেষ দেখে সবার বুক কেঁপে উঠল। কিন্তু সেই ধ্বংসস্তূপের মাঝে যখন দেখলেন শিশু কৃষ্ণ সম্পূর্ণ অক্ষত অবস্থায় হাসিমুখে পায়ের আঙুল চুষছেন, তখন মা যশোদার আনন্দের সীমা রইল না!

মা যশোদা শিশুকে কোলে তুলে নিলেন। ব্রজবাসীরা বিস্মিত হয়ে ভাবলেন, কোনো বলদ বা মানুষ না থাকা সত্ত্বেও এত ভারী গাড়িটি কীভাবে একা একা উল্টে ভেঙে গেল:

> **শ্রীমদ্ভাগবতম, স্কন্ধ ১০, অধ্যায় ৭, শ্লোক ১৩–১৪**
> 
> *ঊচুর্বালাশ্চ দৃষ্ট্বেতি চরিত্রসুরেশ্বরে*  
> *বালেন হতোঽয়মিতি ন শ্রদ্ধধুর্দারুণম্*  
> 
> **অনুবাদ:** "পাশে খেলা করা রাখাল বালকেরা বলল: 'আমরা নিজেদের চোখে দেখেছি! এই ছোট্ট শিশুটি কেঁদে পা ছুঁড়ে চাকায় লাথি মারল, আর সাথে সাথেই গাড়িটি উড়ে গিয়ে ভেঙে গেল!' কিন্তু বড়রা বিশ্বাস করতে পারলেন না যে এত ছোট শিশু এমন ভারী গাড়ি ভাঙতে পারে।"

ব্রজবাসীরা শিশুদের কথাকে শিশুর কল্পনা মনে করলেন। শ্রীহরির কৃপায় শিশু রক্ষা পেয়েছে ভেবে নন্দ মহারাজ আবার ব্রাহ্মণদের গো-দান করলেন এবং সন্তানের দীর্ঘায়ু কামনা করলেন!""",
                "questions": [
                    {
                        "question": "শকট ভঞ্জনের এই লীলা কোন শুভ উৎসবে ঘটেছিল?",
                        "options": [
                            {"text": "উত্থান মহোৎসব (তিন মাস বয়সে শিশুর প্রথম পাশ ফেরার উৎসব)", "is_correct": True},
                            {"text": "গোবর্ধন পূজা", "is_correct": False},
                            {"text": "রাসলীলা উৎসব", "is_correct": False},
                            {"text": "বসুদেবের বিবাহ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "মা যশোদা শিশু কৃষ্ণকে কোথায় শুইয়ে রেখেছিলেন?",
                        "options": [
                            {"text": "আঙিনায় থাকা একটি বড় কাঠের মালবাহী গাড়ির (শকট) ছায়ায়", "is_correct": True},
                            {"text": "একটি গুহার ভেতর", "is_correct": False},
                            {"text": "বাড়ির ছাদে", "is_correct": False},
                            {"text": "যমুনার নৌকায়", "is_correct": False}
                        ]
                    },
                    {
                        "question": "সেই ভারী গাড়িতে কী বোঝাই করা ছিল?",
                        "options": [
                            {"text": "দুধ, দই, মাখন ও গুড়ে ভরা ভারী কলসি", "is_correct": True},
                            {"text": "অস্ত্রশস্ত্র ও তলোয়ার", "is_correct": False},
                            {"text": "মথুরার সোনাদানা", "is_correct": False},
                            {"text": "কাঠ ও পাথর", "is_correct": False}
                        ]
                    },
                    {
                        "question": "গাড়ির মধ্যে কোন অসুর গোপনে প্রবেশ করেছিল?",
                        "options": [
                            {"text": "শকটা সুর", "is_correct": True},
                            {"text": "তৃণাবর্ত", "is_correct": False},
                            {"text": "অঘাসুর", "is_correct": False},
                            {"text": "বকাসুর", "is_correct": False}
                        ]
                    },
                    {
                        "question": "শিশু কৃষ্ণ কেন কেঁদে পা ছুঁড়তে লাগলেন?",
                        "options": [
                            {"text": "ক্ষুধার্ত হয়ে মায়ের দুধ পান করার জন্য", "is_correct": True},
                            {"text": "পিঁপড়া কামড়ানোর জন্য", "is_correct": False},
                            {"text": "অন্ধকারে ভয় পেয়ে", "is_correct": False},
                            {"text": "বলরামকে ডাকার জন্য", "is_correct": False}
                        ]
                    },
                    {
                        "question": "শ্রীকৃষ্ণের চরণ স্পর্শ করতেই গাড়িটির কী হলো?",
                        "options": [
                            {"text": "গাড়িটি উল্টে ভেঙে চূর্ণবিচূর্ণ হলো এবং অসুর নিহত হলো", "is_correct": True},
                            {"text": "গাড়িটি সোনা হয়ে গেল", "is_correct": False},
                            {"text": "গাড়ির কিছুই হলো না", "is_correct": False},
                            {"text": "গাড়িটি বনে চলে গেল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "কে প্রত্যক্ষদর্শী হিসেবে বড়দের বলেছিল যে শিশুটি লাথি মেরেছে?",
                        "options": [
                            {"text": "পাশে খেলা করা রাখাল বালকেরা", "is_correct": True},
                            {"text": "কংসের চরেরা", "is_correct": False},
                            {"text": "নারদ মুনি", "is_correct": False},
                            {"text": "যশোদার পোষা তোতাপাখি", "is_correct": False}
                        ]
                    },
                    {
                        "question": "বড়রা কেন বালকদের কথায় সহজে বিশ্বাস করতে পারলেন না?",
                        "options": [
                            {"text": "কারণ তিন মাসের শিশুর পক্ষে এত বড় গাড়ি ভাঙা অসম্ভব মনে হয়েছিল", "is_correct": True},
                            {"text": "কারণ বালকেরা মিথ্যা বলছিল বলে ভেবেছিলেন", "is_correct": False},
                            {"text": "কারণ ঝড় উঠেছিল", "is_correct": False},
                            {"text": "কারণ তারা রেগে গিয়েছিলেন", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ভগ্নাবশেষের মাঝে শিশু কৃষ্ণকে কীভাবে পাওয়া গেল?",
                        "options": [
                            {"text": "সম্পূর্ণ অক্ষত অবস্থায় হাসিমুখে পায়ের আঙুল চুষতে দেখা গেল", "is_correct": True},
                            {"text": "রক্তাক্ত অবস্থায় কাঁদতে দেখা গেল", "is_correct": False},
                            {"text": "মাখনের হাঁড়িতে লুকিয়ে ছিলেন", "is_correct": False},
                            {"text": "চাকার নিচে চাপা পড়েছিলেন", "is_correct": False}
                        ]
                    },
                    {
                        "question": "শকটা সুর বধের কথা শ্রীমদ্ভাগবতের কোন অধ্যায়ে আছে?",
                        "options": [
                            {"text": "অধ্যায় ৭", "is_correct": True},
                            {"text": "অধ্যায় ২", "is_correct": False},
                            {"text": "অধ্যায় ৫", "is_correct": False},
                            {"text": "অধ্যায় ১২", "is_correct": False}
                        ]
                    }
                ]
            },
            "te": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "శకటాసుర భంజనం మరియు బండి విరిగిన దివ్య లీల",
                "content": """### గోకులంలో ఘనంగా జరిగిన ఉత్థాన మహోత్సవం

బాలకృష్ణుడికి సుమారు మూడు నెలల వయస్సు వచ్చినప్పుడు, ఆయన మొదటిసారి బోర్లా పడటం యశోదాదేవి గమనించింది. వైదిక సంస్కృతిలో పసిబిడ్డ మొదటిసారి తిరిగే ఈ శుభ ఘడియను *ఉత్థాన మహోత్సవం*గా, ఆ రోజు వచ్చే జన్మనక్షత్ర వేడుకగా ఎంతో వైభవంగా జరుపుకుంటారు:

> **శ్రీమద్ భాగవతం, స్కంధం 10, అధ్యాయం 7, శ్లోకాలు 4–5**
> 
> *కదాచిదౌత్థానికకౌతుకాదృతా*  
> *మహామనాస్తే ప్రథమేబ్దపూరణే*  
> *జన్మర్షపత్తప్రశమాయ మాధవం*  
> *స్నాప్య ద్విజైః శస్తపదైః సుమంగళైః*  
> 
> **తాత్పర్యం:** "బాలకృష్ణుడు మూడు నెలల ప్రాయంలో మొదటిసారి పక్కకు తిరిగినప్పుడు, యశోదాదేవి ఎంతో ఆనందంతో ఉత్థాన వేడుకను ఏర్పాటు చేసింది. వేద పండితులైన బ్రాహ్మణులు మంగళకరమైన వేద మంత్రాలతో ఆ పసికందు ఆయురారోగ్యాల కోసం అభిషేకం చేశారు."

నందమహారాజు, యశోదాదేవి బ్రాహ్మణులకు బంగారు ఆభరణాలతో అలంకరించిన గోవులను, అపారమైన ధాన్యాలను దానమిచ్చారు. గోకులమంతా మంగళ వాద్యాలు, నృత్యాలతో పరవశించిపోయింది.

### బండి కింద బాలకృష్ణుడి శయనం

అభిషేక వేడుకల అనంతరం అలసిపోయిన బాలకృష్ణుడు నిద్రలోకి జారుకున్నాడు. యశోదాదేవి ఆ పసిబిడ్డను మెత్తని పట్టు వస్త్రంలో చుట్టింది.

ఆవరణలో విచ్చేసిన అతిథుల కోలాహలం వల్ల బిడ్డ నిద్రకు భంగం కలగకూడదని భావించి, ప్రాంగణంలో నిలిపివుంచిన ఒక పెద్ద చెక్క ఎడ్లబండి (శకటం) నీడలో పరుండబెట్టింది. ఆ బండిపై పాలు, పెరుగు, వెన్న మరియు బెల్లంతో నిండిన పెద్ద పెద్ద కంచు, ఇత్తడి, మట్టి పాత్రలు ఎంతో బరువుగా పేర్చి ఉన్నాయి.

బిడ్డ చల్లని నీడలో సురక్షితంగా ఉన్నాడని భావించి, యశోదమ్మ అతిథులకు భోజనాలు వడ్డించడంలో నిమగ్నమైంది.

### చిన్ని కృష్ణుడి పాదతాడనం మరియు శకటాసుర సంహారం

అయితే కంసుడు పంపిన శకటాసురుడనే రాక్షసుడు ఆ బండిలో అదృశ్యంగా ప్రవేశించి ఉన్నాడని గోకులంలో ఎవరికీ తెలియదు! ఆ భారీ బండిని బిడ్డపై కూల్చి నలిపి చంపాలన్నదే ఆ రాక్షసుడి దుష్ట పన్నాగం.

బండి కింద పడుకున్న బాలకృష్ణుడికి మెలకువ వచ్చి ఆకలి వేసింది. తల్లి స్తన్యమివ్వడానికి రాలేదని కోపగించుకున్నట్లు ఏడుస్తూ, తన చిన్ని పాదపద్మాలను గాల్లోకి విసరడం మొదలుపెట్టాడు:

> **శ్రీమద్ భాగవతం, స్కంధం 10, అధ్యాయం 7, శ్లోకాలు 6–9**
> 
> *అధః శయానః శకటస్య కృష్ణః*  
> *ప్రణీతపాడో రురుదన్ క్షుతృష్ణః*  
> *పాదాభిఘాతేన బిభేభ తత్ర*  
> *పాతేన భగ్నోహిరదారుసఙ్ఘః*  
> 
> **తాత్పర్యం:** "బండి కింద పడుకున్న బాలకృష్ణుడు ఆకలితో ఏడుస్తూ తన కాళ్ళను ఆడిస్తూ, ఆడుకుంటూ తన పాదపద్మంతో బండి చక్రాన్ని తన్నాడు. వెంటనే ఆ బరువైన బండి గాల్లోకి లేచి తలకిందులుగా పడి, ఇరుసు విరిగి, చక్రాలు ముక్కలై, పాత్రలన్నీ పగిలి పాలు, పెరుగు వరదలై పారాయి!"

పరమేశ్వరుడైన శ్రీకృష్ణుడి పాదపద్మాలకు అపరిమితమైన శక్తి ఉంది. మూడు నెలల పసికందు పాదం తగిలినంత మాత్రాన వజ్రాయుధం తాకినట్లుగా ఆ బండి బద్దలైంది!

బండిలో దాగున్న శకటాసురుడు క్షణంలో ప్రాణాలు విడిచాడు. ఆ భారీ బండి ఆకాశంలోకి లేచి తునాతునకలై నేలకూలింది. ఇరుసులు విరిగిపోయాయి, చక్రాలు బద్దలయ్యాయి. వందలాది పాలు, పెరుగు కుండలు పగిలిపోయి ప్రాంగణమంతా వెన్న, పెరుగు నదుల్లా ప్రవహించాయి!

### పిల్లల సాక్ష్యం మరియు గోపాలుర ఆశ్చర్యం

పర్వతం కూలినంత శబ్దం రావడంతో నందమహారాజు, యశోదమ్మ, సమస్త గోపాలురు భయంతో పరుగుపరుగున వచ్చారు.

అక్కడ నుజ్జునుజ్జయిన బండిని చూసి అందరి గుండెలు ఆగిపోయినంత పనైంది. కానీ ఆ చెల్లాచెదురైన శిథిలాల మధ్య చిన్ని కృష్ణుడు ఏ గాయమూ లేకుండా, నవ్వుతూ తన కాలి బొటనవేలిని చీకుతూ ఆడుకోవడం చూసి యశోదమ్మ ప్రాణాలు తేటపడ్డాయి!

యశోదమ్మ బిడ్డను హృదయానికి హత్తుకుంది. ఎడ్లు లాగకుండా, మనుషులు నెట్టకుండా ఇంత పెద్ద బండి ఎలా కూలిపోయిందో ఎవరికీ అర్థం కాలేదు:

> **శ్రీమద్ భాగవతం, స్కంధం 10, అధ్యాయం 7, శ్లోకాలు 13–14**
> 
> *ఊచుర్బాలాశ్చ దృష్ట్వేతి చరిత్రమసురేశ్వరే*  
> *బాలేన హతోయమితి న శ్రద్దధుర్దారుణమ్*  
> 
> **తాత్పర్యం:** "అక్కడ ఆడుకుంటున్న చిన్నారులు, 'మేము కళ్ళారా చూశాము! ఈ చిన్నారి ఏడుస్తూ కాలుతో తన్నగానే బండి గాల్లోకి ఎగిరి ముక్కలైంది!' అని చెప్పారు. కానీ ఇంత చిన్న పసికందు అంత పెద్ద బండిని తన్ని విరగ్గొట్టగలడంటే పెద్దలెవరూ నమ్మలేకపోయారు."

గోకులవాసులు పిల్లల మాటలను చిన్నపిల్లల చేష్టలుగా భావించారు. శ్రీహరి రక్షణ వల్లే బిడ్డ బతికాడని నమ్మి, నందమహారాజు మళ్ళీ బ్రాహ్మణులకు గోదానాలు చేసి స్వస్తివాచకాలు పలికించాడు!""",
                "questions": [
                    {
                        "question": "శకటం విరిగిన ఈ లీల ఏ శుభ సందర్భంలో జరిగింది?",
                        "options": [
                            {"text": "ఉత్థాన మహోత్సవం (మూడు నెలల వయసులో బిడ్డ బోర్లా పడే వేడుక)", "is_correct": True},
                            {"text": "గోవర్ధన పూజ", "is_correct": False},
                            {"text": "రాసలీల ఉత్సవం", "is_correct": False},
                            {"text": "వసుదేవుడి వివాహం", "is_correct": False}
                        ]
                    },
                    {
                        "question": "యశోదాదేవి బాలకృష్ణుడిని ఎక్కడ పడుకోబెట్టింది?",
                        "options": [
                            {"text": "ప్రాంగణంలో నిలిపివుంచిన పెద్ద చెక్క బండి నీడలో", "is_correct": True},
                            {"text": "ఒక లోతైన గుహలో", "is_correct": False},
                            {"text": "భవనం పైకప్పు మీద", "is_correct": False},
                            {"text": "యమునా నదిలోని పడవలో", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ఆ బండిపై ఏమి పేర్చి ఉన్నాయి?",
                        "options": [
                            {"text": "పాలు, పెరుగు, వెన్న, బెల్లంతో నిండిన భారీ పాత్రలు", "is_correct": True},
                            {"text": "ఆయుధాలు మరియు కత్తులు", "is_correct": False},
                            {"text": "మథుర బంగారం", "is_correct": False},
                            {"text": "కట్టెలు మరియు రాళ్ళు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "బండిలో ఆవహించి ఉన్న రాక్షసుడు ఎవరు?",
                        "options": [
                            {"text": "శకటాసురుడు", "is_correct": True},
                            {"text": "తృణావర్తుడు", "is_correct": False},
                            {"text": "అఘాసురుడు", "is_correct": False},
                            {"text": "బకాసురుడు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "బాలకృష్ణుడు ఏడుస్తూ కాళ్ళు ఎందుకు ఆడించాడు?",
                        "options": [
                            {"text": "ఆకలి వేసి తల్లి పాలు తాగాలని", "is_correct": True},
                            {"text": "చీమ కుట్టినందుకు", "is_correct": False},
                            {"text": "చీకటికి భయపడి", "is_correct": False},
                            {"text": "బలరాముడిని పిలవడానికి", "is_correct": False}
                        ]
                    },
                    {
                        "question": "కృష్ణుడి పాదం తగలగానే బండికి ఏమైంది?",
                        "options": [
                            {"text": "బండి తలకిందులై తునాతునకలైంది మరియు రాక్షసుడు మరణించాడు", "is_correct": True},
                            {"text": "బంగారంగా మారింది", "is_correct": False},
                            {"text": "బండికి ఏమీ కాలేదు", "is_correct": False},
                            {"text": "అడవిలోకి వెళ్ళిపోయింది", "is_correct": False}
                        ]
                    },
                    {
                        "question": "కృష్ణుడు తన్నడం వల్లే బండి విరిగిందని ఎవరు చెప్పారు?",
                        "options": [
                            {"text": "అక్కడ ఆడుకుంటున్న చిన్నపిల్లలు", "is_correct": True},
                            {"text": "కంసుడి వేగులవారు", "is_correct": False},
                            {"text": "నారద మహర్షి", "is_correct": False},
                            {"text": "యశోదమ్మ చిలుక", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పెద్దలు పిల్లల మాటను ఎందుకు నమ్మలేకపోయారు?",
                        "options": [
                            {"text": "మూడు నెలల పసికందు అంత పెద్ద బండిని తన్ని విరగ్గొట్టడం అసాధ్యమని భావించారు", "is_correct": True},
                            {"text": "పిల్లలు అబద్ధం చెబుతున్నారని కోపగించారు", "is_correct": False},
                            {"text": "గాలివానకు విరిగిందని భావించారు", "is_correct": False},
                            {"text": "పిల్లలను పట్టించుకోలేదు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "శిథిలాల మధ్య బాలకృష్ణుడు ఎలా కనిపించాడు?",
                        "options": [
                            {"text": "సురక్షితంగా నవ్వుతూ కాలి బొటనవేలిని చీకుతూ కనిపించాడు", "is_correct": True},
                            {"text": "రక్తగాయాలతో ఏడుస్తూ", "is_correct": False},
                            {"text": "వెన్న కుండలో దాక్కుని", "is_correct": False},
                            {"text": "చక్రం కింద ఇరుక్కుని", "is_correct": False}
                        ]
                    },
                    {
                        "question": "శకటాసుర భంజనం లీల భాగవతంలోని ఏ అధ్యాయంలో ఉంది?",
                        "options": [
                            {"text": "అధ్యాయం 7", "is_correct": True},
                            {"text": "అధ్యాయం 2", "is_correct": False},
                            {"text": "అధ్యాయం 5", "is_correct": False},
                            {"text": "అధ్యాయం 12", "is_correct": False}
                        ]
                    }
                ]
            },
            "kn": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "ಶಕಟಾಸುರ ಭಂಜನ ಮತ್ತು ಬಂಡಿ ಮುರಿದ ಲೀಲೆ",
                "content": """### ಗೋಕುಲದಲ್ಲಿ ವೈಭವದ ಉತ್ಥಾನ ಮಹೋತ್ಸವ

ಬಾಲಕೃಷ್ಣನಿಗೆ ಸುಮಾರು ಮೂರು ತಿಂಗಳು ತುಂಬಿದಾಗ, ಕಂದನು ಮೊದಲ ಬಾರಿಗೆ ಬೆನ್ನಿನಿಂದ ಹೊಟ್ಟೆಯ ಮೇಲೆ ಹೊರಳಾಡುವುದನ್ನು ತಾಯಿ ಯಶೋದೆಯು ಕಂಡಳು. ವೈದಿಕ ಸಂಪ್ರದಾಯದಲ್ಲಿ ಮಗುವಿನ ಈ ಬೆಳವಣಿಗೆಯನ್ನು *ಉತ್ಥಾನ ಮಹೋತ್ಸವ*ವೆಂದು ಹಾಗೂ ಮಗುವಿನ ಜನ್ಮನಕ್ಷತ್ರದ ದಿನವೆಂದು ಅತ್ಯಂತ ಸಡಗರದಿಂದ ಆಚರಿಸಲಾಗುತ್ತದೆ:

> **ಶ್ರೀಮದ್ ಭಾಗವತಂ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 7, ಶ್ಲೋಕಗಳು 4–5**
> 
> *ಕದಾಚಿದೌತ್ಥಾನಿಕಕೌತುಕಾದೃತಾ*  
> *ಮಹಾಮನಾಸ್ತೇ ಪ್ರಥಮೇಬ್ದಪೂರಣೇ*  
> *ಜನ್ಮರ್ಷಪತ್ತಪ್ರಶಮಾಯ ಮಾಧವಂ*  
> *ಸ್ನಾಪ್ಯ ದ್ವಿಜೈಃ ಶಸ್ತಪದೈಃ ಸುಮಂಗಲೈಃ*  
> 
> **ಭಾವಾರ್ಥ:** "ಬಾಲಕೃಷ್ಣನು ಮೂರು ತಿಂಗಳ ಪ್ರಾಯದಲ್ಲಿ ಮೊದಲ ಬಾರಿಗೆ ಹೊರಳಾಡಿದಾಗ, ತಾಯಿ ಯಶೋದೆಯು ಸಂಭ್ರಮದಿಂದ ಉತ್ಥಾನ ಮಹೋತ್ಸವವನ್ನು ಆಚರಿಸಿದಳು. ಬ್ರಾಹ್ಮಣರು ಮಗುವಿನ ದೀರ್ಘಾಯುಷ್ಯ ಮತ್ತು ಕಲ್ಯಾಣಕ್ಕಾಗಿ ಮಂಗಳಕರ ವೇದ ಮಂತ್ರಗಳಿಂದ ಅಭಿಷೇಕ ಮಾಡಿದರು."

ನಂದಮಹಾರಾಜರು ಮತ್ತು ಯಶೋದೆಯು ಚಿನ್ನದ ಆಭರಣಗಳಿಂದ ಶೃಂಗರಿಸಿದ ಗೋವುಗಳನ್ನು, ರಾಶಿರಾಶಿ ಧಾನ್ಯಗಳನ್ನು ಬ್ರಾಹ್ಮಣರಿಗೆ ದಾನವಾಗಿ ನೀಡಿದರು. ಗೋಕುಲವೆಲ್ಲವೂ ಮಂಗಲ ಗಾನ ಮತ್ತು ಮೃದಂಗದ ನಿನಾದದಿಂದ ಸಂಭ್ರಮಿಸಿತು.

### ಬಂಡಿಯ ನೆರಳಿನಲ್ಲಿ ಬಾಲಕೃಷ್ಣನ ಶಯನ

ಅಭಿಷೇಕ ಮತ್ತು ಪೂಜೆಗಳ ನಂತರ ದಣಿದ ಬಾಲಕೃಷ್ಣನು ನಿದ್ರೆಗೆ ಜಾರಿದನು. ಯಶೋದೆಯು ಕಂದನನ್ನು ಮೃದುವಾದ ರೇಷ್ಮೆ ಬಟ್ಟೆಯಲ್ಲಿ ಸುತ್ತಿದಳು.

ಅಂಗಳದಲ್ಲಿ ಅತಿಥಿಗಳ ಗದ್ದಲದಿಂದ ಮಗುವಿನ ನಿದ್ರೆಗೆ ಭಂಗವಾಗಬಾರದೆಂದು, ಅಂಗಳದಲ್ಲಿದ್ದ ದೊಡ್ಡ ಭಾರೀ ಮರದ ಎತ್ತಿನ ಬಂಡಿಯ ನೆರಳಿನಲ್ಲಿ ಮಗುವನ್ನು ಮಲಗಿಸಿದಳು. ಆ ಬಂಡಿಯ ಮೇಲೆ ಹಾಲು, ಮೊಸರು, ಬೆಣ್ಣೆ ಮತ್ತು ಬೆಲ್ಲದಿಂದ ತುಂಬಿದ ಹಿತ್ತಾಳೆ, ತಾಮ್ರ ಮತ್ತು ಮಣ್ಣಿನ ದೊಡ್ಡ ದೊಡ್ಡ ಮಡಕೆಗಳನ್ನು ತುಂಬಲಾಗಿತ್ತು.

ಮಗು ನೆರಳಿನಲ್ಲಿ ಸುರಕ್ಷಿತವಾಗಿದೆಯೆಂದು ಭಾವಿಸಿ, ಯಶೋದೆಯು ಅತಿಥಿಗಳಿಗೆ ಸತ್ಕಾರ ಮಾಡಲು ಮತ್ತು ಬ್ರಾಹ್ಮಣರಿಗೆ ಭೋಜನ ಬಡಿಸಲು ತೆರಳಿದಳು.

### ಬಾಲಕೃಷ್ಣನ ಪುಟ್ಟ ಪಾದಸ್ಪರ್ಶ ಮತ್ತು ಶಕಟಾಸುರನ ಅಂತ್ಯ

ಆದರೆ ಕಂಸನಿಂದ ಕಳುಹಿಸಲ್ಪಟ್ಟ ಶಕಟಾಸುರನೆಂಬ ರಾಕ್ಷಸನು ಆ ಮರದ ಬಂಡಿಯಲ್ಲಿ ಅದೃಶ್ಯನಾಗಿ ಆವೇಶಿಸಿಕೊಂಡಿದ್ದನೆಂಬುದು ಯಾರಿಗೂ ತಿಳಿದಿರಲಿಲ್ಲ! ಆ ಭಾರೀ ಬಂಡಿಯನ್ನು ಮಗು ಕೃಷ್ಣನ ಮೇಲೆ ಉರುಳಿಸಿ, ಚಕ್ರಗಳ ಕೆಳಗೆ ಜಜ್ಜಿ ಕೊಲ್ಲುವುದೇ ಅವನ ದುಷ್ಟ ಸಂಚಾಗಿತ್ತು.

ಬಂಡಿಯ ಕೆಳಗೆ ಮಲಗಿದ್ದ ಕೃಷ್ಣನಿಗೆ ಎಚ್ಚರವಾಗಿ ಹಸಿವಾಯಿತು. ಎದೆಹಾಲು ಸಿಗದೆ ಕೋಪಗೊಂಡಂತೆ ನಟಿಸುತ್ತಾ, ಪುಟ್ಟ ಕಂದನು ತನ್ನ ಕಮಲದಂತಹ ಪಾದಗಳನ್ನು ಗಾಳಿಯಲ್ಲಿ ಆಡಿಸತೊಡಗಿದನು:

> **ಶ್ರೀಮದ್ ಭಾಗವತಂ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 7, ಶ್ಲೋಕಗಳು 6–9**
> 
> *ಅಧಃ ಶಯಾನಃ ಶಕಟಸ್ಯ ಕೃಷ್ಣಃ*  
> *ಪ್ರಣೀತಪಾದೋ ರುರುದನ್ ಕ್ಷುತೃಷ್ಣಃ*  
> *ಪಾದಾಭಿಘಾತೇನ ಬಿಭೇಭ ತತ್ರ*  
> *ಪಾತೇನ ಭಗ್ನೋಹಿರದಾರುಸಙ್ಘಃ*  
> 
> **ಭಾವಾರ್ಥ:** "ಬಂಡಿಯ ಕೆಳಗೆ ಮಲಗಿದ್ದ ಬಾಲಕೃಷ್ಣನು ಹಸಿವಿನಿಂದ ಅಳುತ್ತಾ ಕಾಲುಗಳನ್ನು ಒದೆಯತೊಡಗಿದನು. ಆಟವಾಡುತ್ತಾ ಆತನ ಪುಟ್ಟ ಪಾದಕಮಲವು ಬಂಡಿಯ ಚಕ್ರಕ್ಕೆ ತಗುಲಿತು. ತಕ್ಷಣವೇ ಆ ಭಾರೀ ಬಂಡಿಯು ತಲೆಕೆಳಗಾಗಿ ಉರುಳಿಬಿದ್ದಿತು, ಅದರ ಅಚ್ಚು ಮುರಿಯಿತು, ಚಕ್ರಗಳು ಚೂರುಚೂರಾದವು ಮತ್ತು ಎಲ್ಲಾ ಮಡಕೆಗಳು ಒಡೆದು ಹಾಲು-ಮೊಸರಿನ ಪ್ರವಾಹವೇ ಹರಿಯಿತು!"

ಪರಮೇಶ್ವರನ ಪಾದಕಮಲಗಳ ಶಕ್ತಿಯು ಅಪರಿಮಿತವಾದದ್ದು. ಮೂರು ತಿಂಗಳ ಪುಟ್ಟ ಮಗುವಿನ ಪಾದದ ಸ್ಪರ್ಶವು ವಜ್ರಾಯುಧದಂತೆ ಬಂಡಿಗೆ ಬಡಿಯಿತು!

ಶಕಟಾಸುರನು ಕ್ಷಣಾರ್ಧದಲ್ಲಿ ಕೊಲ್ಲಲ್ಪಟ್ಟನು. ಆ ಬೃಹತ್ ಬಂಡಿಯು ಆಕಾಶಕ್ಕೆ ಚಿಮ್ಮಿ ತುಂಡುತುಂಡಾಗಿ ನೆಲಕ್ಕುರುಳಿತು. ಅಚ್ಚುಗಳು ಮುರಿದವು, ಚಕ್ರಗಳು ನುಜ್ಜುಗುಜ್ಜಾದವು. ನೂರಾರು ಮಣ್ಣಿನ ಮತ್ತು ಹಿತ್ತಾಳೆಯ ಮಡಕೆಗಳು ಒಡೆದು ಅಂಗಳದಲ್ಲೆಲ್ಲಾ ಬೆಣ್ಣೆ ಮತ್ತು ಮೊಸರು ನದಿಯಂತೆ ಹರಿಯಿತು!

### ಮಕ್ಕಳ ಸಾಕ್ಷಿ ಮತ್ತು ಗೋಪಾಲಕರ ವಿಸ್ಮಯ

ಬಂಡಿ ಮುರಿದ ಭೀಕರ ಶಬ್ದವನ್ನು ಕೇಳಿ ನಂದಮಹಾರಾಜರು, ಯಶೋದಾ ಮತ್ತು ಸಮಸ್ತ ಗೋಪಾಲಕರು ಗಾಬರಿಯಿಂದ ಓಡಿಬಂದರು.

ಅಲ್ಲಿ ಬಂಡಿಯ ಚೂರುಗಳನ್ನು ನೋಡಿ ಎಲ್ಲರೂ ದಂಗಾದರು. ಆದರೆ ಆ ಅವಶೇಷಗಳ ನಡುವೆ ಮುದ್ದು ಕೃಷ್ಣನು ಯಾವ ಗಾಯವೂ ಇಲ್ಲದೆ, ನಗುತ್ತಾ ತನ್ನ ಕಾಲಿನ ಹೆಬ್ಬೆರಳನ್ನು ಚೀಪುತ್ತಾ ಆಟವಾಡುತ್ತಿರುವುದನ್ನು ಕಂಡು ಎಲ್ಲರ ಜೀವ ಮರಳಿ ಬಂದಂತಾಯಿತು!

ತಾಯಿ ಯಶೋದೆಯು ಮಗುವನ್ನು ಎತ್ತಿ ಮುದ್ದಾಡಿದಳು. ಎತ್ತುಗಳು ಎಳೆಯದೆ, ಮನುಷ್ಯರು ತಳ್ಳದೆ ಅಷ್ಟು ದೊಡ್ಡ ಬಂಡಿ ತಾನಾಗಿಯೇ ಹೇಗೆ ಉರುಳಿತು ಎಂದು ಹಿರಿಯರಿಗೆ ತಿಳಿಯಲಿಲ್ಲ:

> **ಶ್ರೀಮದ್ ಭಾಗವತಂ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 7, ಶ್ಲೋಕಗಳು 13–14**
> 
> *ಊಚುರ್ಬಾಲಾಶ್ಚ ದೃಷ್ಟ್ವೇತಿ ಚರಿತ್ರಮಸುರೇಶ್ವರೇ*  
> *ಬಾಲೇನ ಹತೋಯಮಿತಿ ನ ಶ್ರದ್ದಧುರ್ದಾರುಣಮ್*  
> 
> **ಭಾವಾರ್ಥ:** "ಅಲ್ಲಿ ಆಟವಾಡುತ್ತಿದ್ದ ಗೋಪಾಲಕ ಮಕ್ಕಳು, 'ನಾವು ಕಣ್ಣಾರೆ ನೋಡಿದ್ದೇವೆ! ಈ ಪುಟ್ಟ ಮಗು ಅಳುತ್ತಾ ಕಾಲಿನಿಂದ ಒದೆಯುತ್ತಿದ್ದಂತೆ ಬಂಡಿಯು ಹಾರಿ ಚೂರುಚೂರಾಯಿತು!' ಎಂದರು. ಆದರೆ ಇಷ್ಟು ಪುಟ್ಟ ಮಗು ಅಷ್ಟು ದೊಡ್ಡ ಬಂಡಿಯನ್ನು ಒಡೆದುಹಾಕಲು ಸಾಧ್ಯವೆಂದು ದೊಡ್ಡವರು ನಂಬಲಿಲ್ಲ."

ಮುಗ್ಧ ಗೋಪಾಲಕರು ಮಕ್ಕಳ ಮಾತನ್ನು ಕೇವಲ ಮಕ್ಕಳಾಟವೆಂದು ಭಾವಿಸಿದರು. ಶ್ರೀಹರಿಯ ಕೃಪೆಯಿಂದಲೇ ಮಗು ಉಳಿಯಿತೆಂದು ನಂಬಿ, ನಂದಮಹಾರಾಜರು ಮತ್ತೆ ಬ್ರಾಹ್ಮಣರಿಗೆ ಗೋವುಗಳನ್ನು ದಾನ ಮಾಡಿ ಮಗುವಿನ ರಕ್ಷಣೆಗಾಗಿ ಪ್ರಾರ್ಥಿಸಿದರು!""",
                "questions": [
                    {
                        "question": "ಬಂಡಿ ಮುರಿದ ಈ ಲೀಲೆಯು ಯಾವ ಮಂಗಳಕರ ಉತ್ಸವದಂದು ನಡೆಯಿತು?",
                        "options": [
                            {"text": "ಉತ್ಥಾನ ಮಹೋತ್ಸವ (ಮೂರು ತಿಂಗಳಿನಲ್ಲಿ ಮಗು ಹೊರಳಾಡುವ ಉತ್ಸವ)", "is_correct": True},
                            {"text": "ಗೋವರ್ಧನ ಪೂಜೆ", "is_correct": False},
                            {"text": "ರಾಸಲೀಲೆ ಉತ್ಸವ", "is_correct": False},
                            {"text": "ವಸುದೇವರ ವಿವಾಹ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ತಾಯಿ ಯಶೋದೆಯು ಬಾಲಕೃಷ್ಣನನ್ನು ಎಲ್ಲಿ ಮಲಗಿಸಿದಳು?",
                        "options": [
                            {"text": "ಅಂಗಳದಲ್ಲಿದ್ದ ದೊಡ್ಡ ಮರದ ಎತ್ತಿನ ಬಂಡಿಯ ನೆರಳಿನಲ್ಲಿ", "is_correct": True},
                            {"text": "ಒಂದು ಗುಹೆಯಲ್ಲಿ", "is_correct": False},
                            {"text": "ಮನೆಯ ಮಾಳಿಗೆಯ ಮೇಲೆ", "is_correct": False},
                            {"text": "ಯಮುನೆಯ ದೋಣಿಯಲ್ಲಿ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಆ ಭಾರೀ ಬಂಡಿಯ ಮೇಲೆ ಏನನ್ನು ತುಂಬಲಾಗಿತ್ತು?",
                        "options": [
                            {"text": "ಹಾಲು, ಮೊಸರು, ಬೆಣ್ಣೆ ಮತ್ತು ಬೆಲ್ಲದಿಂದ ತುಂಬಿದ ಹಿತ್ತಾಳೆ ಮತ್ತು ಮಣ್ಣಿನ ಮಡಕೆಗಳು", "is_correct": True},
                            {"text": "ಕತ್ತಿಗಳು ಮತ್ತು ಆಯುಧಗಳು", "is_correct": False},
                            {"text": "ಮಥುರೆಯ ಬಂಗಾರ", "is_correct": False},
                            {"text": "ಕಟ್ಟಿಗೆ ಮತ್ತು ಕಲ್ಲುಗಳು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಬಂಡಿಯಲ್ಲಿ ಆವೇಶಿಸಿಕೊಂಡಿದ್ದ ರಾಕ್ಷಸ ಯಾರು?",
                        "options": [
                            {"text": "ಶಕಟಾಸುರ", "is_correct": True},
                            {"text": "ತೃಣಾವರ್ತ", "is_correct": False},
                            {"text": "ಅಘಾಸುರ", "is_correct": False},
                            {"text": "ಬಕಾಸುರ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಬಾಲಕೃಷ್ಣನು ಅಳುತ್ತಾ ಕಾಲುಗಳನ್ನು ಏಕೆ ಒದೆಯತೊಡಗಿದನು?",
                        "options": [
                            {"text": "ಹಸಿವಾಗಿ ತಾಯಿಯ ಹಾಲು ಕುಡಿಯಲು", "is_correct": True},
                            {"text": "ಇರುವೆ ಕಚ್ಚಿದ್ದಕ್ಕೆ", "is_correct": False},
                            {"text": "ಕತ್ತಲೆಗೆ ಹೆದರಿ", "is_correct": False},
                            {"text": "ಬಲರಾಮನನ್ನು ಕರೆಯಲು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಕೃಷ್ಣನ ಪಾದ ತಗುಲಿದ ತಕ್ಷಣ ಬಂಡಿಗೆ ಏನಾಯಿತು?",
                        "options": [
                            {"text": "ಬಂಡಿಯು ತಲೆಕೆಳಗಾಗಿ ಚೂರುಚೂರಾಯಿತು ಮತ್ತು ರಾಕ್ಷಸನು ಸತ್ತನು", "is_correct": True},
                            {"text": "ಬಂಡಿಯು ಚಿನ್ನವಾಯಿತು", "is_correct": False},
                            {"text": "ಬಂಡಿಗೆ ಏನೂ ಆಗಲಿಲ್ಲ", "is_correct": False},
                            {"text": "ಬಂಡಿ ಕಾಡಿಗೆ ಓಡಿತು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಕೃಷ್ಣನ ಕಾಲೊದೆತದಿಂದಲೇ ಬಂಡಿ ಮುರಿಯಿತೆಂದು ಯಾರು ಹೇಳಿದರು?",
                        "options": [
                            {"text": "ಅಲ್ಲಿ ಆಟವಾಡುತ್ತಿದ್ದ ಪುಟ್ಟ ಮಕ್ಕಳು", "is_correct": True},
                            {"text": "ಕಂಸನ ಗೂಢಚಾರರು", "is_correct": False},
                            {"text": "ನಾರದ ಮುನಿಗಳು", "is_correct": False},
                            {"text": "ಯಶೋದೆಯ ಗಿಳಿ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ದೊಡ್ಡವರು ಮಕ್ಕಳ ಮಾತನ್ನು ಏಕೆ ನಂಬಲಿಲ್ಲ?",
                        "options": [
                            {"text": "ಮೂರು ತಿಂಗಳ ಮಗು ಅಷ್ಟು ದೊಡ್ಡ ಬಂಡಿಯನ್ನು ಒಡೆಯಲು ಸಾಧ್ಯವಿಲ್ಲವೆಂದು ಭಾವಿಸಿದರು", "is_correct": True},
                            {"text": "ಮಕ್ಕಳು ಸುಳ್ಳು ಹೇಳುತ್ತಿದ್ದಾರೆಂದು ಸಿಟ್ಟಾದರು", "is_correct": False},
                            {"text": "ಗಾಳಿಗೆ ಮುರಿಯಿತೆಂದು ಭಾವಿಸಿದರು", "is_correct": False},
                            {"text": "ಮಕ್ಕಳನ್ನು ಕಡೆಗಣಿಸಿದರು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಅವಶೇಷಗಳ ನಡುವೆ ಬಾಲಕೃಷ್ಣನು ಹೇಗೆ ಕಂಡುಬಂದನು?",
                        "options": [
                            {"text": "ಸುರಕ್ಷಿತವಾಗಿ ನಗುತ್ತಾ ಕಾಲಿನ ಹೆಬ್ಬೆರಳನ್ನು ಚೀಪುತ್ತಾ ಕಂಡುಬಂದನು", "is_correct": True},
                            {"text": "ರಕ್ತ ಸುರಿಸುತ್ತಾ ಅಳುತ್ತಿದ್ದನು", "is_correct": False},
                            {"text": "ಬೆಣ್ಣೆಯ ಮಡಕೆಯಲ್ಲಿ ಅಡಗಿದ್ದನು", "is_correct": False},
                            {"text": "ಚಕ್ರದ ಕೆಳಗೆ ಸಿಲುಕಿದ್ದನು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಶಕಟಾಸುರ ಭಂಜನದ ಲೀಲೆಯು ಭಾಗವತದ ಯಾವ ಅಧ್ಯಾಯದಲ್ಲಿದೆ?",
                        "options": [
                            {"text": "ಅಧ್ಯಾಯ 7", "is_correct": True},
                            {"text": "ಅಧ್ಯಾಯ 2", "is_correct": False},
                            {"text": "ಅಧ್ಯಾಯ 5", "is_correct": False},
                            {"text": "ಅಧ್ಯಾಯ 12", "is_correct": False}
                        ]
                    }
                ]
            },
            "ml": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "ശകടാസുര വധവും വണ്ടി തകർന്ന ലീലയും",
                "content": """### ഗോകൂലത്തിൽ നടന്ന ഉത്ഥാന മഹോത്സവം

ഉണ്ണിക്കണ്ണന് മൂന്നു മാസം പ്രായമായപ്പോൾ, കുഞ്ഞ് ആദ്യമായി മലർന്നു കിടപ്പിൽനിന്ന് കമിഴ്ന്നു വീഴാൻ ശ്രമിക്കുന്നത് യശോദ അമ്മ കണ്ടു. പുരാതന വൈദിക സംസ്കാരത്തിൽ ഈ സുപ്രധാന വളർച്ചാഘട്ടത്തെ *ഉത്ഥാന മഹോത്സവം* എന്ന പേരിൽ, കുഞ്ഞിന്റെ ജന്മനക്ഷത്ര ദിനത്തിൽ അതിഗംഭീരമായി ആഘോഷിക്കുന്നത് പതിവാണ്:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അധ്യായം 7, ശ്ലോകങ്ങൾ 4–5**
> 
> *കദാചിദൗത്ഥാനികകൗതുകാദൃതാ*  
> *മഹാമനാസ്തേ പ്രഥമേബ്ദപൂരണേ*  
> *ജന്മർഷപത്തപ്രശമായ മാധവം*  
> *സ്നാപ്യ ദ്വിജൈഃ ശസ്തപദൈഃ സുമംഗലൈഃ*  
> 
> **അർത്ഥം:** "ഉണ്ണിക്കണ്ണന് മൂന്നു മാസം തികഞ്ഞ് ആദ്യമായി കമിഴ്ന്നുവീണ ആ പുണ്യദിനത്തിൽ യശോദ അമ്മ വലിയ സന്തോഷത്തോടെ ഉത്ഥാനോത്സവം നടത്തി. ബ്രാഹ്മണർ മംഗളകരമായ മന്ത്രങ്ങൾ ചൊല്ലി ഉണ്ണിയുടെ ആയുസ്സിനും ക്ഷേമത്തിനുമായി പുണ്യാഹം നടത്തി."

നന്ദഗോപരും യശോദ അമ്മയും ബ്രാഹ്മണർക്ക് സ്വർണ്ണവും പട്ടുവസ്ത്രങ്ങളും അണിയിച്ച പശുക്കളെയും ധാന്യശേഖരങ്ങളും ദാനം ചെയ്തു. ഗോകൂലമാകെ പാട്ടും മേളവുമായി ഉത്സവലഹരിയിലായി.

### വണ്ടിയുടെ തണലിൽ ഉറങ്ങുന്ന ഉണ്ണിക്കണ്ണൻ

ചടങ്ങുകൾ കഴിഞ്ഞപ്പോൾ ക്ഷീണിതനായ ഉണ്ണിക്കണ്ണൻ നല്ല ഉറക്കത്തിലായി. യശോദ അമ്മ കുഞ്ഞിനെ മൃദുവായ പട്ടുവിരിപ്പിൽ കിടത്തി.

മുറ്റത്ത് അതിഥികളുടെ ബഹളത്താൽ കുഞ്ഞിന്റെ ഉറക്കം നഷ്ടപ്പെടാതിരിക്കാൻ, മുറ്റത്ത് നിർത്തിയിട്ടിരുന്ന ഒരു വലിയ കാളവണ്ടിയുടെ (ശകടം) തണലിൽ അമ്മ ഉണ്ണിയെ കിടത്തി. ആ വണ്ടിയിൽ പാൽ, തൈര്, വെണ്ണ, ശർക്കര എന്നിവ നിറഞ്ഞ വലിയ പിച്ചളപ്പാത്രങ്ങളും മൺകലങ്ങളും നിറച്ചിട്ടുണ്ടായിരുന്നു.

കുഞ്ഞ് തണലിൽ സുരക്ഷിതമായി ഉറങ്ങുകയാണെന്നു കരുതി, യശോദ അമ്മ അതിഥികളെ സൽക്കരിക്കാനും സദ്യ കൊടുക്കാനും പോയി.

### ഉണ്ണിക്കണ്ണന്റെ കാൽത്തല്ലും ശകടാസുരന്റെ നാശവും

എന്നാൽ കംസൻ അയച്ച ശകടാസുരൻ എന്ന അസുരൻ ആ കാളവണ്ടിയിൽ അദൃശ്യനായി പ്രവേശിച്ചിട്ടുണ്ടായിരുന്നു എന്ന കാര്യം ആരും അറിഞ്ഞില്ല! ആ വലിയ വണ്ടി മറിച്ചിട്ട് ഉണ്ണിക്കണ്ണനെ ചതച്ചുകൊല്ലുകയായിരുന്നു അവന്റെ ലക്ഷ്യം.

വണ്ടിയുടെ അടിയിൽ കിടന്ന ഉണ്ണിക്കണ്ണന് ഉണർന്നപ്പോൾ വിശന്നു. അമ്മയുടെ മുലപ്പാൽ കിട്ടാതെ കോപിച്ചതുപോലെ ഭാവച്ചു കുഞ്ഞ് കരയാൻ തുടങ്ങി, തന്റെ താമരക്കാലുകൾ ആകാശത്തേക്ക് ആഞ്ഞുതൊഴിച്ചു:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അധ്യായം 7, ശ്ലോകങ്ങൾ 6–9**
> 
> *അധഃ ശയാനഃ ശകടസ്യ കൃഷ്ണഃ*  
> *പ്രണീതപാദോ രുരുദൻ ക്ഷുതൃഷ്ണഃ*  
> *പാദാഭിഘാതേന ബിഭേഭ തത്ര*  
> *പാതേന ഭഗ്നോഹിരദാരുസങ്ഘഃ*  
> 
> **അർത്ഥം:** "വണ്ടിയുടെ അടിയിൽ കിടന്ന ഉണ്ണിക്കണ്ണൻ വിശപ്പുകൊണ്ട് കരഞ്ഞ് കാലിട്ടടിച്ചു. കളിക്കുന്നതിനിടയിൽ ആ താമരപ്പാദം വണ്ടിയുടെ ചക്രത്തിൽ തട്ടി. പെട്ടെന്ന് ആ വലിയ വണ്ടി തലകീഴായി മറിഞ്ഞു, അച്ചുതണ്ട് ഒടിഞ്ഞു, ചക്രങ്ങൾ തകർന്നു, എല്ലാ പാത്രങ്ങളും ഉടഞ്ഞ് പാലൊഴുകി!"

പരമേശ്വരനായ ഭഗവാന്റെ താമരപ്പാദങ്ങൾക്ക് അപാരമായ ശക്തിയുണ്ട്. മൂന്നു മാസം പ്രായമുള്ള ഒരു കുഞ്ഞിന്റെ കാൽത്തല്ല് ഒരു ഇടിമിന്നൽ പോലെയായിരുന്നു!

ശകടാസുരൻ തൽക്ഷണം കൊല്ലപ്പെട്ടു. ആ വലിയ വണ്ടി വായുവിൽ ഉയർന്നുപൊങ്ങി നിലംപതിച്ചു. അച്ചുതണ്ട് ഒടിഞ്ഞുനുറുങ്ങി, ചക്രങ്ങൾ തകർന്നു. നൂറുകണക്കിന് കലങ്ങൾ പൊട്ടി മുറ്റമാകെ പാലും തൈരും വെണ്ണയും പരന്നൊഴുകി!

### കുട്ടികളുടെ സാക്ഷ്യവും ഗോപന്മാരുടെ അത്ഭുതവും

പർവ്വതം തകർന്നുവീഴുന്നതുപോലെയുള്ള ശബ്ദം കേട്ട് നന്ദഗോപരും യശോദ അമ്മയും നാട്ടുകാരും ഭയന്നോടിയെത്തി.

തകർന്നുകിടക്കുന്ന വണ്ടി കണ്ട് എല്ലാവരുടെയും ചങ്ക് തകർന്നു. എന്നാൽ ആ അവശിഷ്ടങ്ങൾക്കിടയിൽ ഉണ്ണിക്കണ്ണൻ യാതൊരു പോറലുമേൽക്കാതെ പുഞ്ചിരിച്ചുകൊണ്ട് കാൽവിരൽ കുടിക്കുന്നത് കണ്ടപ്പോൾ അമ്മയുടെ ശ്വാസം നേരെ വീണു!

യശോദ അമ്മ ഉണ്ണിയെ മാറോടണച്ചു. കാളകളോ മനുഷ്യരോ തൊടാതെ ഇത്രയും വലിയൊരു വണ്ടി എങ്ങനെ താനേ തകർന്നു എന്നോർത്ത് മുതിർന്നവർ അത്ഭുതപ്പെട്ടു:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അധ്യായം 7, ശ്ലോകങ്ങൾ 13–14**
> 
> *ഊചുർബാലാശ്ച ദൃഷ്ട്വേതി ചരിത്രമസുരേശ്വരേ*  
> *ബാലേന ഹതോയമിതി ന ശ്രദ്ധധുർദാരുണമ്*  
> 
> **അർത്ഥം:** "അവിടെ കളിച്ചുകൊണ്ടിരുന്ന കുട്ടികൾ പറഞ്ഞു: 'ഞങ്ങൾ കണ്ണുകൊണ്ട് കണ്ടതാണ്! ഈ ഉണ്ണിക്കണ്ണൻ കരഞ്ഞുകൊണ്ട് കാലുകൊണ്ട് വണ്ടിയിൽ തൊഴിച്ചപ്പോഴാണ് വണ്ടി പൊട്ടിത്തെറിച്ചത്!' എന്നാൽ ഇത്രയും ചെറിയൊരു കുഞ്ഞ് വലിയൊരു വണ്ടി തകർക്കുമെന്ന് മുതിർന്നവർക്ക് വിശ്വസിക്കാനായില്ല."

മുതിർന്ന ഗോപന്മാർ അത് കുട്ടിക്കളിയായി തള്ളിക്കളഞ്ഞു. മഹാവിഷ്ണുവിന്റെ കാരുണ്യം കൊണ്ടാണ് കുഞ്ഞ് രക്ഷപ്പെട്ടതെന്നു കരുതി നന്ദഗോപർ വീണ്ടും ബ്രാഹ്മണർക്ക് പശുക്കളെ ദാനം നൽകി!""",
                "questions": [
                    {
                        "question": "വണ്ടി തകർന്ന ഈ ലീല ഏത് മംഗളകരമായ ചടങ്ങിലാണ് സംഭവിച്ചത്?",
                        "options": [
                            {"text": "ഉത്ഥാന മഹോത്സവം (മൂന്നു മാസം പ്രായത്തിൽ കുഞ്ഞ് കമിഴ്ന്നുവീഴുന്ന ചടങ്ങ്)", "is_correct": True},
                            {"text": "ഗോവർദ്ധന പൂജ", "is_correct": False},
                            {"text": "രാസലീല", "is_correct": False},
                            {"text": "വസുദേവരുടെ കല്യാണം", "is_correct": False}
                        ]
                    },
                    {
                        "question": "യശോദ അമ്മ ഉണ്ണിക്കണ്ണനെ എവിടെയാണ് ഉറക്കിക്കിടത്തിയത്?",
                        "options": [
                            {"text": "മുറ്റത്തുണ്ടായിരുന്ന വലിയൊരു കാളവണ്ടിയുടെ തണലിൽ", "is_correct": True},
                            {"text": "ഒരു ഗുഹയിൽ", "is_correct": False},
                            {"text": "വീടിന്റെ മട്ടുപ്പാവിൽ", "is_correct": False},
                            {"text": "യമുനയിലെ തോണിയിൽ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ആ വലിയ വണ്ടിയിൽ എന്തെല്ലാമാണ് നിറച്ചിരുന്നത്?",
                        "options": [
                            {"text": "പാൽ, തൈര്, വെണ്ണ എന്നിവ നിറഞ്ഞ വലിയ പിച്ചളപ്പാത്രങ്ങളും മൺകലങ്ങളും", "is_correct": True},
                            {"text": "വാളും പരിചയും", "is_correct": False},
                            {"text": "മഥുരയിലെ സ്വർണ്ണം", "is_correct": False},
                            {"text": "വിറകും കല്ലും", "is_correct": False}
                        ]
                    },
                    {
                        "question": "വണ്ടിയിൽ പ്രവേശിച്ചിരുന്ന അസുരൻ ആരായിരുന്നു?",
                        "options": [
                            {"text": "ശകടാസുരൻ", "is_correct": True},
                            {"text": "തൃണാവർത്തൻ", "is_correct": False},
                            {"text": "അഘാസുരൻ", "is_correct": False},
                            {"text": "ബകാസുരൻ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഉണ്ണിക്കണ്ണൻ കരഞ്ഞുകൊണ്ട് കാലിട്ടടിച്ചത് എന്തുകൊണ്ടായിരുന്നു?",
                        "options": [
                            {"text": "വിശന്നിട്ട് അമ്മയുടെ മുലപ്പാൽ കുടിക്കാൻ", "is_correct": True},
                            {"text": "ഉറുമ്പ് കടിച്ചതുകൊണ്ട്", "is_correct": False},
                            {"text": "ഇരുട്ടിനെ പേടിച്ചിട്ട്", "is_correct": False},
                            {"text": "ബലരാമനെ വിളിക്കാൻ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഉണ്ണിക്കണ്ണന്റെ കാൽത്തല്ലേറ്റപ്പോൾ വണ്ടിക്ക് എന്തു സംഭവിച്ചു?",
                        "options": [
                            {"text": "വണ്ടി തലകീഴായി മറിഞ്ഞു പൊടിപൊടിയായി, അസുരൻ കൊല്ലപ്പെട്ടു", "is_correct": True},
                            {"text": "വണ്ടി സ്വർണ്ണമായി മാറി", "is_correct": False},
                            {"text": "വണ്ടിക്ക് ഒന്നും സംഭവിച്ചില്ല", "is_correct": False},
                            {"text": "വണ്ടി കാട്ടിലേക്ക് ഓടിപ്പോയി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "കുഞ്ഞ് തൊഴിച്ചപ്പോഴാണ് വണ്ടി തകർന്നതെന്ന് ആരാണ് മുതിർന്നവരോട് പറഞ്ഞത്?",
                        "options": [
                            {"text": "അവിടെ കളിച്ചുകൊണ്ടിരുന്ന കുട്ടികൾ", "is_correct": True},
                            {"text": "കംസന്റെ ചാരന്മാർ", "is_correct": False},
                            {"text": "നാരദമുനി", "is_correct": False},
                            {"text": "യശോദയുടെ തത്ത", "is_correct": False}
                        ]
                    },
                    {
                        "question": "മുതിർന്നവർ കുട്ടികളുടെ വാക്ക് വിശ്വസിക്കാതിരുന്നത് എന്തുകൊണ്ടായിരുന്നു?",
                        "options": [
                            {"text": "മൂന്നു മാസമുള്ള കുഞ്ഞിന് ഇത്ര വലിയ വണ്ടി തകർക്കാൻ കഴിയില്ലെന്ന് കരുതിയതുകൊണ്ട്", "is_correct": True},
                            {"text": "കുട്ടികൾ കള്ളം പറയുകയാണെന്ന് കരുതിയതുകൊണ്ട്", "is_correct": False},
                            {"text": "കാറ്റടിച്ചാണ് വണ്ടി വീണതെന്ന് കരുതിയതുകൊണ്ട്", "is_correct": False},
                            {"text": "കുട്ടികളോട് ദേഷ്യമായതുകൊണ്ട്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "തകർന്ന വണ്ടിക്കിടയിൽ ഉണ്ണിക്കണ്ണനെ എങ്ങനെയാണ് കണ്ടത്?",
                        "options": [
                            {"text": "യാതൊരു പരിക്കുമേൽക്കാതെ ചിരിച്ചുകൊണ്ട് കാൽവിരൽ കുടിക്കുന്നതായി", "is_correct": True},
                            {"text": "രക്തം വാർന്നു കരയുന്നതായി", "is_correct": False},
                            {"text": "വെണ്ണക്കലത്തിൽ ഒളിച്ചിരിക്കുന്നതായി", "is_correct": False},
                            {"text": "ചക്രത്തിനടിയിൽ കുടുങ്ങിക്കിടക്കുന്നതായി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ശകടാസുരവധം ഭാഗവതത്തിലെ ഏത് അധ്യായത്തിലാണ് വിവരിക്കുന്നത്?",
                        "options": [
                            {"text": "അധ്യായം 7", "is_correct": True},
                            {"text": "അധ്യായം 2", "is_correct": False},
                            {"text": "അധ്യായം 5", "is_correct": False},
                            {"text": "അധ്യായം 12", "is_correct": False}
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

        self.stdout.write(self.style.SUCCESS(f"Successfully populated Story 18 (ID: {story.id}) across all 7 languages!"))
