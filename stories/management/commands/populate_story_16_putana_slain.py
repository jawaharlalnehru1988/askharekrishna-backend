import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askharekrishna_backend.settings')
django.setup()

from django.core.management.base import BaseCommand
from stories.models import StoryMainTopic, Story, StoryTranslation, StoryQuestion, StoryQuestionOption

class Command(BaseCommand):
    help = "Populate Story 16: The Slaying of Putana and Her Gigantic Fall across 7 languages"

    def handle(self, *args, **options):
        topic = StoryMainTopic.objects.get(name="Krishna Pastimes")

        story_slug = "krishna-pastimes-the-slaying-of-putana-and-her-gigantic-fall"
        image_path = "stories/images/putana_slain_gigantic_fall.jpg"

        story, created = Story.objects.get_or_create(
            slug=story_slug,
            defaults={
                "topic": topic,
                "order": 15,
                "imagePath": image_path,
            }
        )
        if not created:
            story.topic = topic
            story.order = 15
            story.imagePath = image_path
            story.save()

        stories_data = {
            "en": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "The Slaying of Putana and Her Gigantic Fall",
                "content": """### Baby Krishna Seizes the Poisoned Breast

Having entered the bedchamber of Mother Yashoda without hindrance, the demonic witch Putana bent over the cradle. In her mind was cold, calculating malice, but on her face she wore the warm, alluring smile of an affectionate mother. 

With deceptive gentleness, Putana lifted the infant Lord onto her lap. She exposed her breast, which had been smeared with the virulent *kālakūṭa* poison—a lethal venom so powerful that even a trace could incinerate a living being. Thinking her foul plot was foolproof, she offered her poisoned nipple to baby Krishna's mouth.

The infant Lord, the Supreme Personality of Godhead, was fully aware of her demonic identity and intentions. Grasping her breast firmly with both of His tiny lotus hands, the Lord began to suck:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 6, Verse 10**
> 
> *tad aṅkam āruhya gadāgrajo 'lpakaḥ*  
> *pragṛhya dorbhyāṁ prapibant stanaṁ balāt*  
> *sa-pūtanāyāḥ sa-viṣaṁ sa-jīvitam*  
> *prapīḍya gāḍhaṁ karayoḥ sa-roṣam*  
> 
> **Translation:** "Climbing onto her lap, baby Krishna seized her breast firmly with both hands as if angry. He pressed it tightly and sucked out not only the deadly poison, but along with it, the very life-air of the witch Putana."

The Supreme Lord is all-attractive and all-purifying. When the poison entered His divine mouth, it could not harm Him in the slightest, just as darkness cannot touch the blazing sun. Instead, the Lord pressed her breast with unbreakable force, drawing forth the poisonous milk together with the witch's vital life energy (*prāṇa*).

### The Agonizing Screams of Putana

As the Lord’s tiny lips drew out her life-air, Putana felt an unbearable, burning agony shooting through every nerve and vital organ of her body. Her mystic powers deserted her. The excruciating pain made her feel as though all the joints and bones in her skeleton were being ground to fine dust.

Writhing in desperate torment, the demoness lost all control:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 6, Verse 11**
> 
> *sā muñca muñcālam iti prabhāṣiṇī*  
> *niṣpīḍyamānākhila-marma-bandhanā*  
> *nyamīlayad dṛṣṭim udasya bāhukau*  
> *prasvedavat-kāya-rujo 'vacālatā*  
> 
> **Translation:** "Screaming desperately, 'Leave me! Leave me! It is enough!', feeling all the vital points of her body crushed, she threw her arms wide into the sky, perspiration poured from her thrashing body, and her eyes rolled in unbearable agony."

Her ear-splitting shrieks shook the earth and sky. Birds dropped from the trees, and pregnant women in the surrounding districts trembled in dread. The demoness flailed her arms, kicked her legs, and struggled with all her demonic might to push the tiny baby away. But Krishna’s grip was unbreakable. The Supreme Lord held fast to her breast like a thunderbolt, drinking until her last breath was drawn from her chest.

### The Shattering of the Illusion and the Colossal Fall

With her life-air completely extinguished, Putana’s mystic disguise disintegrated. Her body began to expand rapidly, returning to its natural, horrifying, mountainous form:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 6, Verse 14**
> 
> *patamānaḥ śarīreṇa drumāñ cakṣoditān bahūn*  
> *pātitavān mahān āśu śailād iva patan drumān*  
> *ṣaṭ-krośāyatam aṅgaṁ tat patitaṁ bhuvi dāruṇam*  
> 
> **Translation:** "As her gigantic corpse fell to the earth, it smashed numerous large trees into splinters, like a collapsing mountain crashing down. Her terrifying body stretched across a full six krośas (twelve miles) upon the ground."

The sound of her mountainous fall was like a cosmic thunderclap. Her lifeless body measured six *krośas* (twelve miles) in length. Her mouth was wide open like an immense cavern, her teeth resembled giant plows, her nostrils were like deep mountain caves, and her tangled hair spread across the earth like a burning forest. Huge trees were crushed into matchwood beneath her massive weight.

### The Fearless Lord on the Demoness's Chest

Hearing the earth-shattering crash and Putana’s bloodcurdling screams, Mother Yashoda, Mother Rohini, and all the cowherd men and women rushed toward the pastures in absolute terror. They feared the worst for baby Krishna.

When they arrived at the clearing, they stopped dead in their tracks, paralyzed by the sight of the colossal demoness stretched across the fields. But when their eyes traveled to her massive chest, their dread turned to boundless joy and astonishing wonder:

There, seated happily and fearlessly upon the mountainous corpse of the witch, was baby Krishna! The divine child was smiling sweetly, playing with His lotus toes and laughing innocently, completely undisturbed by the monstrous demoness beneath Him. Overcome with maternal love and ecstatic relief, Mother Yashoda and Rohini rushed forward, climbed upon the giant carcass, and scooped the radiant child into their trembling, loving arms!""",
                "questions": [
                    {
                        "question": "How did baby Krishna hold Putana when she offered her poisoned breast?",
                        "options": [
                            {"text": "He seized her breast firmly with both of His lotus hands", "is_correct": True},
                            {"text": "He pushed her away with a stick", "is_correct": False},
                            {"text": "He hid His face in a blanket", "is_correct": False},
                            {"text": "He called out for Vasudeva", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Along with the virulent poison, what else did baby Krishna suck from Putana?",
                        "options": [
                            {"text": "Her very life-air (prana)", "is_correct": True},
                            {"text": "Her golden ornaments", "is_correct": False},
                            {"text": "Her silken garments", "is_correct": False},
                            {"text": "Her celestial chariot", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What desperate words did Putana scream out in agony as the Lord drained her life?",
                        "options": [
                            {"text": "'Munca, munca, alam!' ('Leave me, leave me, it is enough!')", "is_correct": True},
                            {"text": "'Kamsa, come save me!'", "is_correct": False},
                            {"text": "'Drink more milk!'", "is_correct": False},
                            {"text": "'Where is Nanda Maharaja?'", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What happened to Putana's beautiful disguise when her life-air was sucked out?",
                        "options": [
                            {"text": "It shattered and revealed her true, monstrous mountainous form", "is_correct": True},
                            {"text": "It turned into pure gold", "is_correct": False},
                            {"text": "It vanished into water", "is_correct": False},
                            {"text": "It transformed into a flock of white birds", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How large was Putana's colossal corpse when it crashed to the ground?",
                        "options": [
                            {"text": "Six krosas (twelve miles) long", "is_correct": True},
                            {"text": "One hundred yards", "is_correct": False},
                            {"text": "Ten feet", "is_correct": False},
                            {"text": "Fifty miles", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What happened to the trees when Putana's colossal body fell?",
                        "options": [
                            {"text": "Numerous huge trees were crushed into splinters beneath her weight", "is_correct": True},
                            {"text": "The trees caught fire and vanished", "is_correct": False},
                            {"text": "The trees bore golden fruits immediately", "is_correct": False},
                            {"text": "The trees remained completely untouched", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Where was baby Krishna found by the cowherds after Putana collapsed?",
                        "options": [
                            {"text": "Playing and crawling fearlessly upon her gigantic chest", "is_correct": True},
                            {"text": "Hidden under a large rock", "is_correct": False},
                            {"text": "Floating in the Yamuna River", "is_correct": False},
                            {"text": "Sleeping in Nanda's bedchamber", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Why couldn't the deadly kalakuta poison harm baby Krishna?",
                        "options": [
                            {"text": "Because He is the all-pure Supreme Lord; poison cannot affect Him just as darkness cannot touch the sun", "is_correct": True},
                            {"text": "Because He had drunk an herbal antidote", "is_correct": False},
                            {"text": "Because the poison had expired", "is_correct": False},
                            {"text": "Because Putana forgot to smear it", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How did Mother Yashoda and Rohini react upon seeing baby Krishna on the demoness's body?",
                        "options": [
                            {"text": "Overwhelmed with relief and love, they rushed forward and scooped Him into their arms", "is_correct": True},
                            {"text": "They fainted and ran away in fear", "is_correct": False},
                            {"text": "They scolded the child", "is_correct": False},
                            {"text": "They called for the royal army", "is_correct": False}
                        ]
                    },
                    {
                        "question": "Which verse of Srimad-Bhagavatam describes Putana's colossal corpse spanning six krosas?",
                        "options": [
                            {"text": "Canto 10, Chapter 6, Verse 14", "is_correct": True},
                            {"text": "Canto 10, Chapter 6, Verse 1", "is_correct": False},
                            {"text": "Canto 10, Chapter 1, Verse 10", "is_correct": False},
                            {"text": "Canto 10, Chapter 3, Verse 25", "is_correct": False}
                        ]
                    }
                ]
            },
            "ta": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "பூதனை வதம் மற்றும் அவளது பிரம்மாண்ட வீழ்ச்சி",
                "content": """### நஞ்சு பூசிய மார்பகத்தைப் பற்றிப் பிடித்த பால கிருஷ்ணர்

அன்னை யசோதையின் அந்தரங்க அறைக்குள் எவ்விதத் தடையுமின்றி நுழைந்த பூதனை, பால கிருஷ்ணர் படுத்திருந்த தொட்டிலின் அருகே குனிந்தாள். அவளுடைய உள்ளத்தில் கொலைவெறி தாண்டவமாடிய போதிலும், முகத்தில் வாஞ்சையான பாசப் புன்னகையைத் தவழவிட்டாள்.

வஞ்சகமான பாசத்தோடு அந்தத் தெய்வக் குழந்தையைத் தன் மடியில் தூக்கி வைத்துக்கொண்டாள். தன் மார்பில் பூசப்பட்டிருந்த *காலகூடம்* என்னும் கொடிய ஆலகால விஷத்தை ஊட்டிவிட அவள் முனைந்தாள். அந்த விஷத்தின் ஒரு சிறு துளி கூட எந்த ஒரு உயிரையும் அடுத்த கணமே சாம்பலாக்கிவிடும் தன்மை கொண்டது. தன் திட்டம் வெற்றி பெற்றுவிட்டதாக மமதையோடு அவள் பால கிருஷ்ணரின் வாயருகே தன் நஞ்சு நிறைந்த முலையை வைத்தாள்.

முழுமுதற் கடவுளான பால கிருஷ்ணர் அவளுடைய அசுரத் தன்மையையும் கொடிய நோக்கத்தையும் முழுமையாக அறிந்திருந்தார். தம்முடைய தாமரை மலர் போன்ற இரு சிறிய கரங்களாலும் அவளது மார்பகத்தை இறுகப் பற்றிப் பிடித்துக்கொண்டு, பகவான் பாலூட்டத் தொடங்கினார்:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 6, சுலோகம் 10**
> 
> *தத் அங்கமாருஹ்ய கதாஹ்ரஜோ ல்பக:*  
> *ப்ரஹ்ருஹ்ய தோர்ப்யாம் ப்ரபிபந்த் ஸ்தனம் பலாத்*  
> *ஸ-பூதனாயா: ஸ-விஷம் ஸ-ஜீவிதம்*  
> *ப்ரபீட்ய காடம் கரயோ: ஸ-ரோஷம்*  
> 
> **பொருள்:** "பால கிருஷ்ணர் கோபங்கொண்டவரைப் போல அவளது மடியில் ஏறி, தம் இரு திருக்கரங்களாலும் அவளது மார்பை பலமாகப் பற்றிக்கொண்டார். அந்த மார்பகத்தை இறுகப் பிழிந்து, கொடிய விஷத்தோடு சேர்த்து பூதனையின் பிராண வாயுவையும் பகவான் உறிஞ்சி குடிக்கத் தொடங்கினார்."

சூரியனை எந்த இருளும் தீண்ட முடியாதது போல, சர்வ வல்லமை படைத்த முழுமுதற் கடவுளான பகவானை எந்த ஒரு கொடிய விஷமும் சிறிதும் பாதிக்க முடியாது. பகவான் தம் திருக்கரங்களால் அவளுடைய மார்பை வஜ்ராயுதம் போல இறுகப் பிடித்து, நச்சுப் பாலுடன் சேர்த்து அவளுடைய உயிர் மூச்சையும் வேகமாக உள்ளிழுக்கலானார்.

### பூதனையின் மரண ஓலமும் அலறலும்

பகவான் அவளுடைய பிராண வாயுவை உறிஞ்சத் தொடங்கியதும், பூதனையின் நரம்புகளிலும், உயிர் நாடிகளிலும் தாங்க முடியாத பேரெரிச்சல் பரவியது. அவளுடைய மாயாஜால சக்திகள் யாவும் அவளைக் கைவிட்டன. அவளது உடலின் எலும்புகளும் மூட்டுகளும் மாவாக அரைக்கப்படுவது போன்ற தாங்கவொண்ணாத வேதனையை அவள் அனுபவித்தாள்.

கடுமையான வேதனையால் துடித்த பூதனை, தன் சுயநினைவை இழந்து அலறினாள்:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 6, சுலோகம் 11**
> 
> *ஸா முஞ்ச முஞ்சாலம் இதி ப்ரபாஷிணீ*  
> *நிஷ்பீட்யமானாகில-மர்ம-பந்தனா*  
> *ந்யமீலயத் த்ருஷ்டிம் உதஸ்ய பாஹுகௌ*  
> *ப்ரஸ்வேதவத்-காய-ருஜோ வசாலதா*  
> 
> **பொருள்:** "'என்னை விட்டுவிடு! என்னை விட்டுவிடு! இதுவே போதும்!' என்று பயங்கரமாகக் கூச்சலிட்டாள். தன் உடல் உறுப்புகள் யாவும் நொறுக்கப்படுவதை உணர்ந்த அவள், வானை நோக்கித் தன் கைகளை வீசினாள்; உடல் முழுவதும் வியர்வை வெள்ளமாய் ஓட, தாங்க முடியாத வலியால் அவள் துடிதுடித்தாள்."

பூதனையின் மரண அலறல் விண்ணையும் மண்ணையும் அதிரச் செய்தது. வானில் பறந்த பறவைகள் பயந்து கீழே விழுந்தன. திசைகளெல்லாம் எதிரொலித்த அந்தப் பேரொலியைக் கேட்டு கர்ப்பிணிப் பெண்கள் நடுங்கினர். அந்த அரக்கி தன் கைகளையும் கால்களையும் உதைத்துக்கொண்டு, அந்தச் சிறிய குழந்தையைத் தள்ளிவிடப் போராடினாள். ஆனால் பகவானின் பிடி வஜ்ரத்தை விடக் கடினமாக இருந்தது. அவளுடைய இறுதி மூச்சு அடங்கும் வரை பகவான் அவளை விடாமல் உறிஞ்சிக் குடித்தார்.

### மாயை கலைந்து விழுந்த பன்னிரண்டு மைல் பிரம்மாண்ட உடல்

உயிர் பிரிந்த அடுத்த கணமே, பூதனையின் மோகன தேவலோக மாறுவேடம் முற்றிலும் மறைந்துபோனது. அவளுடைய உடல் மலை போலப் பிரம்மாண்டமாகப் பெருகி, அவளது உண்மையான கோர அரக்கி ரூபம் வெளிப்பட்டது:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 6, சுலோகம் 14**
> 
> *பதமான: சரீரேண த்ருமான் சக்ஷோதிதான் பஹூன்*  
> *பாதிதவான் மஹான் ஆசு சைலாத் இவ பதன் த்ருமான்*  
> *ஷட்-க்ரோசாயதம் அங்கம் தத் பதிதம் புவி தாருணம்*  
> 
> **பொருள்:** "ஒரு மாபெரும் மலை சரிந்து விழுவது போல, அவளது பிரம்மாண்ட உடல் கீழே விழுந்தபோது எண்ணற்ற பெருமரங்கள் நொறுங்கித் துகள்களாயின. ஆறு குரோசங்கள் (பன்னிரண்டு மைல்கள்) நீளமுள்ள அவளது பயங்கரமான சடலம் பூமியின் மீது சரிந்து விழுந்தது."

அவள் விழுந்த சத்தம் பிரபஞ்ச இடி முழக்கம் போல இருந்தது. அவளது உடல் பன்னிரண்டு மைல் நீளத்திற்குப் பரவிக் கிடந்தது. அவளுடைய வாய் ஒரு பெரிய குகை போலத் திறந்திருந்தது; அவளது கோரைப் பற்கள் ஏர்க்கலப்பைகள் போல நீட்டிக்கொண்டிருந்தன; அவளது தலைமுடி எரியும் காடு போல விரிந்து கிடந்தது. அவளுடைய பாரமான உடல் பட்ட மரங்கள் அனைத்தும் சுக்குநூறாக உடைந்து விழுந்தன.

### அரக்கியின் மார்பில் அச்சமின்றி விளையாடிய பகவான்

பூமியை உலுக்கிய அந்தப் பயங்கரமான சத்தத்தைக் கேட்டு, அன்னை யசோதை, ரோஹிணி மற்றும் கோகுலத்து மக்கள் அனைவரும் குழந்தைக்கு என்ன நேர்ந்ததோ என்று பதறியடித்துக்கொண்டு ஓடிவந்தனர்.

மேய்ச்சல் நிலத்தில் ஒரு மாபெரும் மலை சரிந்து கிடப்பது போலக் கிடந்த பூதனையின் சடலத்தைக் கண்டு அவர்கள் திகைத்து நின்றனர். ஆனால், அவளது பிரம்மாண்டமான மார்பகத்தின் மீது தங்கள் பார்வையைச் செலுத்தியபோது, அவர்களின் பயமெல்லாம் எல்லைയിல்லாத ஆனந்தமாக மாறியது!

அங்கே, மரணமடைந்த அந்த அரக்கியின் மார்பின் மீது பால கிருஷ்ணர் அச்சமின்றி அமர்ந்து புன்னகைத்துக் கொண்டிருந்தார்! கார்மேக வண்ணனான அந்தத் தெய்வக் குழந்தை, தன் தாமரை மலர்ப் பாதங்களை அசைத்து ஆனந்தமாக விளையாடிக் கொண்டிருந்தார். தாய்மைப் பாசமும் எல்லையற்ற நிம்மதியும் பொங்கி வழிய, அன்னை யசோதையும் ரோஹிணியும் விரைந்து சென்று, அந்த மாபெரும் உடலின் மீது ஏறி பால கிருஷ்ணரை வாரியெடுத்துத் தழுவிக்கொண்டனர்!""",
                "questions": [
                    {
                        "question": "பூதனை நஞ்சு தடவிய முலையை வாயருகே வைத்த போது பால கிருஷ்ணர் என்ன செய்தார்?",
                        "options": [
                            {"text": "தம் இரு தாமரைக் கரங்களாலும் அவளது மார்பை இறுகப் பற்றிப் பிடித்தார்", "is_correct": True},
                            {"text": "அவளை ஒரு குச்சியால் அடித்தார்", "is_correct": False},
                            {"text": "போர்வையால் முகத்தை மூடிக்கொண்டார்", "is_correct": False},
                            {"text": "வசுதேவரைக் கூப்பிட்டார்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "கொடிய நஞ்சுடன் சேர்த்து பூதனையிடமிருந்து பால கிருஷ்ணர் எதை உறிஞ்சி எடுத்தார்?",
                        "options": [
                            {"text": "அவளுடைய பிராண வாயுவை (உயிர் மூச்சை)", "is_correct": True},
                            {"text": "அவளது தங்க நகைகளை", "is_correct": False},
                            {"text": "அவளது பட்டு ஆடைகளை", "is_correct": False},
                            {"text": "அவளது தேரை", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பகவான் பிராணனை உறிஞ்சிய போது தாங்க முடியாத வேதனையில் பூதனை என்ன கூச்சலிட்டாள்?",
                        "options": [
                            {"text": "'முஞ்ச, முஞ்ச, ஆலம்!' ('என்னை விட்டுவிடு! விட்டுவிடு! இதுவே போதும்!')", "is_correct": True},
                            {"text": "'கம்சா, என்னைக் காப்பாற்று!'", "is_correct": False},
                            {"text": "'இன்னும் பால் குடி!'", "is_correct": False},
                            {"text": "'நந்த மகாராஜர் எங்கே?'", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பிராணன் பிரிந்ததும் பூதனையின் மோகன தேவலோக வேடம் என்னவாயிற்று?",
                        "options": [
                            {"text": "மாயை கலைந்து அவளது பிரம்மாண்ட கோர அரக்கி ரூபம் வெளிப்பட்டது", "is_correct": True},
                            {"text": "அது தங்கமாக மாறியது", "is_correct": False},
                            {"text": "அது தண்ணீராகக் கரைந்தது", "is_correct": False},
                            {"text": "அது வெள்ளைப் புறாக்களாக மாறியது", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பூமி மீது விழுந்து கிடந்த பூதனையின் சடலம் எத்தனை நீளம் கொண்டதாக இருந்தது?",
                        "options": [
                            {"text": "ஆறு குரோசங்கள் (பன்னிரண்டு மைல்கள்) நீளம்", "is_correct": True},
                            {"text": "நூறு அடிகள்", "is_correct": False},
                            {"text": "பத்து அடிகள்", "is_correct": False},
                            {"text": "ஐம்பது மைல்கள்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பூதனையின் பிரம்மாண்ட உடல் சரிந்து விழுந்த போது மரங்களுக்கு என்ன நேர்ந்தது?",
                        "options": [
                            {"text": "எண்ணற்ற பெருமரங்கள் நொறுங்கி சுக்குநூறாக விழுந்தன", "is_correct": True},
                            {"text": "மரங்கள் தீப்பற்றி எரிந்தன", "is_correct": False},
                            {"text": "மரங்கள் உடனடியாக தங்கக் கனிகளைத் தந்தன", "is_correct": False},
                            {"text": "மரங்களுக்கு எதுவுமே ஆகவில்லை", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பூதனை வீழ்ந்த பிறகு பால கிருஷ்ணர் எங்கே காணப்பட்டார்?",
                        "options": [
                            {"text": "அரக்கியின் பிரம்மாண்ட மார்பின் மீது அச்சமின்றி விளையாடிக் கொண்டிருந்தார்", "is_correct": True},
                            {"text": "ஒரு பெரிய பாறையின் அடியில்", "is_correct": False},
                            {"text": "யமுனை நதியில் மிதந்து கொண்டிருந்தார்", "is_correct": False},
                            {"text": "நந்தரின் படுக்கையறையில் உறங்கிக் கொண்டிருந்தார்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "கொடிய காலகூட விஷம் ஏன் பகவான் கிருஷ்ணரைச் சிறிதும் பாதிக்கவில்லை?",
                        "options": [
                            {"text": "பகவான் முழுமுதற் கடவுள்; சூரியனை இருள் தீண்ட முடியாதது போல நஞ்சு பகவானைப் பாதிக்காது", "is_correct": True},
                            {"text": "பகவான் மூலிகை மருந்து குடித்திருந்தார்", "is_correct": False},
                            {"text": "விஷத்தின் வீரியம் குறைந்திருந்தது", "is_correct": False},
                            {"text": "பூதனை விஷம் தடவ மறந்துவிட்டாள்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "அரக்கியின் மார்பில் பால கிருஷ்ணரைக் கண்ட அன்னை யசோதையும் ரோஹிணியும் என்ன செய்தனர்?",
                        "options": [
                            {"text": "ஆனந்தக் கண்ணீருடன் விரைந்து சென்று குழந்தையை வாரி அணைத்துக்கொண்டனர்", "is_correct": True},
                            {"text": "பயந்து மயங்கி விழுந்தனர்", "is_correct": False},
                            {"text": "குழந்தையைக் கடிந்துகொண்டனர்", "is_correct": False},
                            {"text": "ராணுவத்தை அழைத்தனர்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பூதனையின் சடலம் ஆறு குரோசங்கள் நீளம் கொண்டதாக விவரிக்கும் ஸ்ரீமத் பாகவத சுலோகம் எது?",
                        "options": [
                            {"text": "ஸ்கந்தம் 10, அத்தியாயம் 6, சுலோகம் 14", "is_correct": True},
                            {"text": "ஸ்கந்தம் 10, அத்தியாயம் 6, சுலோகம் 1", "is_correct": False},
                            {"text": "ஸ்கந்தம் 10, அத்தியாயம் 1, சுலோகம் 10", "is_correct": False},
                            {"text": "ஸ்கந்தம் 10, அத்தியாயம் 3, சுலோகம் 25", "is_correct": False}
                        ]
                    }
                ]
            },
            "hi": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "पूतना वध और उसका विशालकाय पतन",
                "content": """### विषैले स्तनों को भगवान द्वारा दृढ़ता से पकड़ना

माता यशोदा के शयनकक्ष में निर्बाध प्रवेश पाकर पूतना पालने के पास पहुंची। उसके मन में हत्यारी क्रूरता थी, किंतु मुख पर उसने वात्सल्य का ढोंग रच रखा था।

उसने छलपूर्वक बालकृष्ण को अपनी गोद में उठा लिया। उसने अपने स्तनों पर लगा *कालकूट* विष उनके मुख के समीप किया। यह विष इतना भयंकर था कि उसकी एक बूंद भी किसी भी प्राणी को तुरंत भस्म कर सकती थी। अपनी योजना को सफल मानते हुए उसने विषैला स्तन भगवान के मुख में दे दिया।

पूर्ण पुरुषोत्तम भगवान श्रीकृष्ण उसके समस्त कपट और राक्षसी स्वभाव को भली-भांति जानते थे। अपने दोनों नन्हे चरणकमल सदृश करकमलों से उसके स्तन को दृढ़तापूर्वक पकड़कर भगवान दूध पीने लगे:

> **श्रीमद्-भागवतम, स्कंध 10, अध्याय 6, श्लोक 10**
> 
> *तदङ्कमा hisa गदाग्रजोऽल्पकः*  
> *प्रगृह्य दोर्भ्यां प्रपिबन् स्तनं बलात्*  
> *सपूतनायाः सविषं सजीवितम्*  
> *प्रपीड्य गाढं करयोः सरोषम्*  
> 
> **भावार्थ:** "बालकृष्ण मानो क्रोधित होकर उसकी गोद में चढ़ गए और अपने दोनों हाथों से उसके स्तन को कसकर पकड़ लिया। उन्होंने उस स्तन को जोर से दबाकर विष के साथ-साथ पूतना के प्राणों को भी खींचना आरंभ कर दिया।"

जैसे प्रज्वलित सूर्य को अंधकार स्पर्श नहीं कर सकता, वैसे ही परम पवित्र भगवान श्रीकृष्ण को कालकूट विष तनिक भी प्रभावित नहीं कर सका। इसके विपरीत, भगवान ने वज्र के समान दृढ़ता से उसके प्राणों को सोखना शुरू किया।

### पूतना का चीत्कार और तड़प

जैसे ही भगवान ने उसके प्राण खींचने शुरू किए, पूतना के शरीर की प्रत्येक नाड़ी और मर्मस्थान में असह्य जलन होने लगी। उसकी सारी आसुरी माया नष्ट हो गई। उसे लगा मानो उसकी हड्डियां और जोड़ चूर्ण-विशूर्ण हो रहे हों।

असह्य पीड़ा से छटपटाती हुई राक्षसी चिल्लाने लगी:

> **श्रीमद्-भागवतम, स्कंध 10, अध्याय 6, श्लोक 11**
> 
> *सा मुञ्च मुञ्चालमिति प्रभाषिणी*  
> *निष्पीड्यमानाखिलमर्मबन्धना*  
> *न्यमीलयद् दृष्टिम उदस्य बाहुकौ*  
> *प्रस्वेदवत्काय रुजोऽवचालता*  
> 
> **भावार्थ:** "'मुझे छोड़ दो! मुझे छोड़ दो! बस करो!' ऐसा बार-बार चिल्लाती हुई, अपने समस्त मर्मस्थानों के कुचले जाने की असह्य वेदना से वह आकाश की ओर भुजाएं फेंककर पसीने से लथपथ होकर तड़पने लगी।"

उसकी भयंकर चीत्कार से आकाश और पृथ्वी कांप उठे। पेड़ों से पक्षी नीचे गिर पड़े और आसपास की गर्भवती स्त्रियां भय से कांपने लगीं। वह बालक को दूर फेंकने के लिए हाथ-पैर पटकने लगी, किंतु भगवान की पकड़ वज्रवत थी। जब तक उसके शरीर से अंतिम श्वास नहीं निकल गई, तब तक भगवान ने उसे नहीं छोड़ा।

### माया का टूटना और बारह मील लंबा विशाल पतन

प्राण निकलते ही पूतना का सुंदर रूप लुप्त हो गया और उसका वास्तविक, पर्वताकार राक्षसी शरीर प्रकट हो गया:

> **श्रीमद्-भागवतम, स्कंध 10, अध्याय 6, श्लोक 14**
> 
> *पतमानः शरीरेण द्रुमांश्चक्षोदितान् बहून्*  
> *पातितवान् महान् आशु शैलादिव पतन् द्रुमान्*  
> *षट्क्रोशायतम् अङ्गं तत् पतितं भुवि दारुणम्*  
> 
> **भावार्थ:** "जैसे कोई विशाल पर्वत गिरता है, वैसे ही जब उसका विशालकाय शरीर धरती पर गिरा, तो उसने अनेक बड़े-बड़े वृक्षों को चूर-चूर कर दिया। उसका भयानक शव छह क्रोश (बारह मील) लंबा था।"

पूतना के गिरने की ध्वनि ब्रह्मांडीय वज्रपात जैसी थी। उसका मुंह किसी विशाल गुफा जैसा खुला था, दांत हल के फाल जैसे थे और बाल जलते हुए वन के समान फैले थे। उसके भारी शरीर के नीचे दबकर अनेक विशाल वृक्ष तिनकों की भांति टूट गए।

### राक्षसी की छाती पर बालकृष्ण की क्रीड़ा

उस भयानक गड़गड़ाहट और चीत्कार को सुनकर माता यशोदा, माता रोहिणी और सभी ग्वाल-बाल भयभीत होकर दौड़ पड़े। उन्हें बालक कृष्ण की चिंता सता रही थी।

जब वे घटनास्थल पर पहुंचे, तो छह क्रोश लंबे उस विशाल शव को देखकर स्तब्ध रह गए। परंतु जब उनकी दृष्टि उस राक्षसी की विशाल छाती पर पड़ी, तो उनका सारा भय असीम आनंद में बदल गया:

वहां भगवान श्रीकृष्ण उस राक्षसी की छाती पर निर्भय होकर क्रीड़ा कर रहे थे! वे मंद-मंद मुस्कुरा रहे थे और अपने नन्हे चरणकमलों को हिलाकर हंस रहे थे। वात्सल्य प्रेम से गद्गद होकर माता यशोदा और रोहिणी ने उस विशाल शरीर पर चढ़कर अपने लाडले को तुरंत अपनी गोद में भर लिया!""",
                "questions": [
                    {
                        "question": "विषैला स्तन सामने आने पर बालकृष्ण ने क्या किया?",
                        "options": [
                            {"text": "अपने दोनों हाथों से उसके स्तन को कसकर पकड़ लिया", "is_correct": True},
                            {"text": "लाठी से प्रहार किया", "is_correct": False},
                            {"text": "चादर में मुंह छिपा लिया", "is_correct": False},
                            {"text": "वसुदेव को पुकारा", "is_correct": False}
                        ]
                    },
                    {
                        "question": "विष के साथ-साथ भगवान श्रीकृष्ण ने पूतना का क्या खींचा?",
                        "options": [
                            {"text": "उसके प्राण (जीवन-वायु)", "is_correct": True},
                            {"text": "उसके सोने के आभूषण", "is_correct": False},
                            {"text": "उसके रेशमी वस्त्र", "is_correct": False},
                            {"text": "उसका रथ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "प्राण खिंचते समय पूतना तड़पकर क्या चिल्लाई?",
                        "options": [
                            {"text": "'मुञ्च, मुञ्च, अलम्!' ('मुझे छोड़ दो, छोड़ दो, बस करो!')", "is_correct": True},
                            {"text": "'कंस मुझे बचाओ!'", "is_correct": False},
                            {"text": "'और दूध पियो!'", "is_correct": False},
                            {"text": "'नंद महाराज कहां हैं?'", "is_correct": False}
                        ]
                    },
                    {
                        "question": "प्राण निकलते ही पूतना के सुंदर रूप का क्या हुआ?",
                        "options": [
                            {"text": "माया नष्ट हो गई और उसका बारह मील लंबा राक्षसी रूप प्रकट हो गया", "is_correct": True},
                            {"text": "वह सोने में बदल गया", "is_correct": False},
                            {"text": "वह पानी बनकर बह गया", "is_correct": False},
                            {"text": "वह कबूतर बन गई", "is_correct": False}
                        ]
                    },
                    {
                        "question": "धरती पर गिरे पूतना के शव की लंबाई कितनी थी?",
                        "options": [
                            {"text": "छह क्रोश (बारह मील)", "is_correct": True},
                            {"text": "सौ गज", "is_correct": False},
                            {"text": "दस फीट", "is_correct": False},
                            {"text": "पचास मील", "is_correct": False}
                        ]
                    },
                    {
                        "question": "पूतना के शरीर के गिरने से वृक्षों का क्या हुआ?",
                        "options": [
                            {"text": "अनेक बड़े-बड़े वृक्ष चूर-चूर होकर गिर पड़े", "is_correct": True},
                            {"text": "वृक्ष जल गए", "is_correct": False},
                            {"text": "वृक्षों पर सोने के फल लग गए", "is_correct": False},
                            {"text": "वृक्षों को कुछ नहीं हुआ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "पूतना के गिरने के बाद बालकृष्ण कहां मिले?",
                        "options": [
                            {"text": "राक्षसी की विशाल छाती पर निर्भय होकर खेलते हुए", "is_correct": True},
                            {"text": "एक बड़ी चट्टान के नीचे", "is_correct": False},
                            {"text": "यमुना में तैरते हुए", "is_correct": False},
                            {"text": "नंदभवन में सोते हुए", "is_correct": False}
                        ]
                    },
                    {
                        "question": "कालकूट विष बालकृष्ण को क्यों हानि नहीं पहुंचा सका?",
                        "options": [
                            {"text": "क्योंकि वे परम पवित्र पूर्ण पुरुषोत्तम भगवान हैं; विष उन्हें स्पर्श भी नहीं कर सकता", "is_correct": True},
                            {"text": "उन्होंने दवा पी रखी थी", "is_correct": False},
                            {"text": "विष पुराना हो चुका था", "is_correct": False},
                            {"text": "पूतना विष लगाना भूल गई थी", "is_correct": False}
                        ]
                    },
                    {
                        "question": "बालकृष्ण को राक्षसी की छाती पर सुरक्षित देखकर माताओं ने क्या किया?",
                        "options": [
                            {"text": "दौड़कर उस विशाल शरीर पर चढ़ीं और बालक को गले से लगा लिया", "is_correct": True},
                            {"text": "भय से मूर्छित होकर भाग गईं", "is_correct": False},
                            {"text": "बालक को डांटने लगीं", "is_correct": False},
                            {"text": "सैनिकों को बुलाया", "is_correct": False}
                        ]
                    },
                    {
                        "question": "पूतना के छह क्रोश लंबे शरीर का वर्णन किस श्लोक में मिलता है?",
                        "options": [
                            {"text": "स्कंध 10, अध्याय 6, श्लोक 14", "is_correct": True},
                            {"text": "स्कंध 10, अध्याय 6, श्लोक 1", "is_correct": False},
                            {"text": "स्कंध 10, अध्याय 1, श्लोक 10", "is_correct": False},
                            {"text": "स्कंध 10, अध्याय 3, श्लोक 25", "is_correct": False}
                        ]
                    }
                ]
            },
            "bn": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "পূতনা বধ ও তার দানবীয় পতন",
                "content": """### বিষাক্ত স্তন ধারণ ও শ্রীকৃষ্ণের সংহারক রূপ

মা যশোদার কক্ষে প্রবেশ করে মায়াবিনী পূতনা শ্রীকৃষ্ণের পালঙ্কের কাছে গিয়ে দাঁড়াল। হৃদয়ে ছিল নারকীয় বিষ, কিন্তু মুখে ছিল কপট স্নেহের আভা।

সে কপট বাৎসল্যে শিশু শ্রীকৃষ্ণকে কোলে তুলে নিল। স্তনে মাখানো ছিল ভয়ানক *কালকূট* বিষ, যার এক ফোঁটাও যে কোনো প্রাণীকে মুহূর্তেই ভস্ম করতে পারে। নিজের কুচক্র সফল মনে করে সে বিষাক্ত স্তন শ্রীকৃষ্ণের মুখে তুলে দিল।

পূর্ণ ভগবান শ্রীকৃষ্ণ তার সমস্ত কুটিল অভিপ্রায় জানতেন। তিনি তাঁর দুটি কোমল করপল্লব দিয়ে তার স্তন দৃঢ়ভাবে আঁকড়ে ধরলেন এবং দুধ পান করতে লাগলেন:

> **শ্রীমদ্ভাগবতম, স্কন্ধ ১০, অধ্যায় ৬, শ্লোক ১০**
> 
> *তদঙ্কমারুহ্য গদাগ্রজোঽল্পকঃ*  
> *প্রগৃহ্য দোর্ভ্যাং প্রপিবন্ স্তনং বলাৎ*  
> *সপূতনায়াঃ সবিষং সজীবিতম্*  
> *প্রপীড্য গাঢং করয়োঃ সরোষম্*  
> 
> **অনুবাদ:** "শিশু কৃষ্ণ ক্রোধের ছলে তার কোলে আরোহণ করলেন এবং উভয় হস্ত দ্বারা তার স্তন দৃঢ়ভাবে চেপে ধরে বিষাক্ত দুগ্ধের সাথে সাথে পূতনার প্রাণবায়ুও পান করতে লাগলেন।"

সূর্যকে যেমন অন্ধকার স্পর্শ করতে পারে না, তেমনই পূর্ণব্রহ্ম ভগবান শ্রীকৃষ্ণকে কোনো বিষই বিন্দুমাত্র স্পর্শ করতে পারেনি। বরং শ্রীকৃষ্ণের বজ্রকঠিন আকর্ষণে পূতনার জীবনীশক্তি নিঃশেষ হতে লাগল।

### পূতনার আর্তনাদ ও যন্ত্রণার ছটফটানি

প্রাণবায়ু নিঃশেষিত হতে থাকলে পূতনার সর্বাঙ্গে এক ভয়াবহ দাহ উপস্থিত হলো। সমস্ত মণি-মানিক্য ও মায়াবী রূপ অন্তর্হিত হলো। তার মনে হতে লাগল যেন শরীরের সমস্ত অস্থিসন্ধি চূর্ণবিচূর্ণ হয়ে যাচ্ছে।

যন্ত্রণায় পাগলপ্রায় হয়ে রাক্ষসী বিকট চিৎকার করে উঠল:

> **শ্রীমদ্ভাগবতম, স্কন্ধ ১০, অধ্যায় ৬, শ্লোক ১১**
> 
> *সা মুঞ্চ মুঞ্চালমিতি প্রভাষিণী*  
> *নিষ্পীড্যমানাখিলমর্মবন্ধনা*  
> *ন্যমীলয়দ্ দৃষ্টিমুদস্য বাহুকৌ*  
> *প্রস্বেদবৎকায় রুজোঽবচালতা*  
> 
> **অনুবাদ:** "'আমাকে ছেড়ে দাও! ছেড়ে দাও! যথেষ্ট হয়েছে!'—এইভাবে আর্তনাদ করে সর্বাঙ্গের অসহ্য যন্ত্রণায় সে হাত-পা ছুড়তে লাগল এবং ঘর্মাক্ত শরীরে ছটফট করতে লাগল।"

তার সেই ভয়াল চিৎকারে আকাশ-বাতাস প্রকম্পিত হলো। বৃক্ষ থেকে পাখিরা খসে পড়ল। দিগ্বিদিক কাঁপিয়ে সে শিশুকে শরীর থেকে দূরে নিক্ষেপ করার চেষ্টা করল, কিন্তু শ্রীকৃষ্ণের বজ্রমুষ্টি ছিল অটল। তাঁর আকর্ষণে পূতনার শেষ নিঃশ্বাসও স্তব্ধ হয়ে গেল।

### মায়ার অবসান ও বিশাল দেহের পতন

প্রাণ নিঃশেষিত হওয়ার সাথে সাথে পূতনার রূপ অন্তর্হিত হলো এবং তার আসল পর্বতপ্রমাণ রাক্ষসী শরীর প্রকট হলো:

> **শ্রীমদ্ভাগবতম, স্কন্ধ ১০, অধ্যায় ৬, শ্লোক ১৪**
> 
> *পতমানঃ শরীরেণ দ্রুমাংশ্চক্ষোদিতাং বহুন্*  
> *পাতিতবান্ মহান্ আশু শৈলাদিব পতন্ দ্রুমান্*  
> *ষট্ক্রোশায়তম্ অঙ্গং তৎ পতিতং ভুবি দারুণম্*  
> 
> **অনুবাদ:** "একটি বিশাল পর্বত ভেঙে পড়ার মতো তার বিরাট শরীর যখন ভূমিতে আছড়ে পড়ল, তখন বহু বৃহদাকার বৃক্ষ চূর্ণবিচূর্ণ হয়ে গেল। তার সেই ভয়ানক শরীর ভূমিতে ছয় ক্রোশ (বারো মাইল) বিস্তৃত হয়ে পতিত হলো।"

তার পতনের শব্দ ছিল এক মহাপ্রলয়ঙ্কর বজ্রপাতের মতো। তার মুখ ছিল এক বিশাল গুহার মতো, দাঁত ছিল লাঙ্গলের ফালের ন্যায়। তার বিশাল দেহের চাপে বহু প্রাচীন বৃক্ষ ধূলিসাৎ হয়ে গেল।

### রাক্ষসীর বক্ষে নির্ভীক শ্রীকৃষ্ণ

সেই প্রলয়ঙ্কর শব্দ শুনে মা যশোদা, মা রোহিণী এবং ব্রজবাসীরা আতঙ্কে ছুটে এলেন। 

সেখানে পৌঁছে বারো মাইল দীর্ঘ সেই দানবীয় শবদেহ দেখে সবাই স্তম্ভিত হলেন। কিন্তু সেই রাক্ষসীর বিশাল বক্ষের দিকে দৃষ্টি যেতেই তাঁদের সমস্ত ভয় পরম আনন্দে রূপান্তরিত হলো:

সেখানে ছোট্ট শ্রীকৃষ্ণ নির্ভয়ে বসে তাঁর চরণকমল নাড়াচাড়া করে খেলা করছিলেন এবং মিষ্টি হাসছিলেন! মা যশোদা ও মা রোহিণী অশ্রুপূর্ণ নয়নে সেই বিশাল দেহে উঠে পরম স্নেহে গোপালকে বুকে জড়িয়ে নিলেন!""",
                "questions": [
                    {
                        "question": "বিষাক্ত স্তন মুখে দেওয়ার সময় শিশু শ্রীকৃষ্ণ কী করলেন?",
                        "options": [
                            {"text": "উভয় হস্ত দিয়ে স্তন দৃঢ়ভাবে চেপে ধরলেন", "is_correct": True},
                            {"text": "লাঠি দিয়ে আঘাত করলেন", "is_correct": False},
                            {"text": "মুখ ঢেকে নিলেন", "is_correct": False},
                            {"text": "বসুদেবকে ডাকলেন", "is_correct": False}
                        ]
                    },
                    {
                        "question": "বিষের সাথে সাথে শ্রীকৃষ্ণ পূতনার আর কী পান করলেন?",
                        "options": [
                            {"text": "তার প্রাণবায়ু (জীবনশক্তি)", "is_correct": True},
                            {"text": "তার স্বর্ণালঙ্কার", "is_correct": False},
                            {"text": "তার পট্টবস্ত্র", "is_correct": False},
                            {"text": "তার রথ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "প্রাণ নিঃশেষিত হওয়ার সময় যন্ত্রণায় পূতনা কী চিৎকার করেছিল?",
                        "options": [
                            {"text": "'মুঞ্চ মুঞ্চ অলম্!' ('ছেড়ে দাও, ছেড়ে দাও, যথেষ্ট হয়েছে!')", "is_correct": True},
                            {"text": "'কংস বাঁচাও!'", "is_correct": False},
                            {"text": "'আরও দুধ খাও!'", "is_correct": False},
                            {"text": "'নন্দ মহারাজ কোথায়?'", "is_correct": False}
                        ]
                    },
                    {
                        "question": "প্রাণবায়ু স্তব্ধ হওয়ার পর পূতনার সুন্দর রূপের কী হলো?",
                        "options": [
                            {"text": "মায়া দূর হলো এবং বারো মাইল দীর্ঘ রাক্ষসী রূপ প্রকাশ পেল", "is_correct": True},
                            {"text": "তা সোনায় পরিণত হলো", "is_correct": False},
                            {"text": "তা জলে পরিণত হলো", "is_correct": False},
                            {"text": "তা পায়রা হয়ে উড়ে গেল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ভূমিতে পতিত পূতনার মৃতদেহটি কত দীর্ঘ ছিল?",
                        "options": [
                            {"text": "ছয় ক্রোশ (বারো মাইল)", "is_correct": True},
                            {"text": "একশো গজ", "is_correct": False},
                            {"text": "দশ ফুট", "is_correct": False},
                            {"text": "পঞ্চাশ মাইল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "পূতনার বিশাল শরীর পতিত হওয়ায় বৃক্ষদের কী হয়েছিল?",
                        "options": [
                            {"text": "অসংখ্য বিশাল বৃক্ষ চূর্ণবিচূর্ণ হয়ে গেল", "is_correct": True},
                            {"text": "গাছে আগুন লেগে গেল", "is_correct": False},
                            {"text": "গাছে সোনার ফল ধরল", "is_correct": False},
                            {"text": "গাছের কোনো ক্ষতি হয়নি", "is_correct": False}
                        ]
                    },
                    {
                        "question": "পূতনা পতনের পর শিশু শ্রীকৃষ্ণকে কোথায় পাওয়া গেল?",
                        "options": [
                            {"text": "রাক্ষসীর বিশাল বক্ষে নির্ভয়ে খেলতে দেখা গেল", "is_correct": True},
                            {"text": "একটি বড় পাথরের নিচে", "is_correct": False},
                            {"text": "যমুনায় ভাসমান অবস্থায়", "is_correct": False},
                            {"text": "শয়নকক্ষে ঘুমন্ত অবস্থায়", "is_correct": False}
                        ]
                    },
                    {
                        "question": "কালকূট বিষ কেন ভগবান শ্রীকৃষ্ণের কোনো ক্ষতি করতে পারেনি?",
                        "options": [
                            {"text": "কারণ তিনি পরমেশ্বর ভগবান; সূর্যের কাছে অন্ধকার যেমন টিকতে পারে না, বিষও তাঁর কোনো ক্ষতি করতে পারে না", "is_correct": True},
                            {"text": "তিনি ওষুধ খেয়েছিলেন", "is_correct": False},
                            {"text": "বিষের মেয়াদ উত্তীর্ণ ছিল", "is_correct": False},
                            {"text": "পূতনা বিষ মাখতে ভুলে গিয়েছিল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "শ্রীকৃষ্ণকে অক্ষত দেখে যশোদা ও রোহিণী কী করলেন?",
                        "options": [
                            {"text": "ছুটে গিয়ে সেই বিশাল শরীরে উঠে সন্তানকে কোলে জড়িয়ে নিলেন", "is_correct": True},
                            {"text": "ভয়ে পালিয়ে গেলেন", "is_correct": False},
                            {"text": "শিশুকে বকাঝকা করলেন", "is_correct": False},
                            {"text": "সৈন্য ডাকলেন", "is_correct": False}
                        ]
                    },
                    {
                        "question": "পূতনার ছয় ক্রোশ দীর্ঘ শরীরের বিবরণ কোন শ্লোকে রয়েছে?",
                        "options": [
                            {"text": "স্কন্ধ ১০, অধ্যায় ৬, শ্লোক ১৪", "is_correct": True},
                            {"text": "স্কন্ধ ১০, অধ্যায় ৬, শ্লোক ১", "is_correct": False},
                            {"text": "স্কন্ধ ১০, অধ্যায় ১, শ্লোক ১০", "is_correct": False},
                            {"text": "স্কন্ধ ১০, অধ্যায় ৩, শ্লোক ২৫", "is_correct": False}
                        ]
                    }
                ]
            },
            "te": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "పూతనా సంహారం మరియు ఆమె బ్రహ్మాండమైన పతనం",
                "content": """### విషపూరితమైన స్తనాన్ని బాలకృష్ణుడు దృఢంగా పట్టడం

యశోదాదేవి శయనమందిరంలోకి ప్రవేశించిన పూతన చిన్ని కృష్ణుడి ఊయల వద్దకు చేరింది. హృదయంలో విషపు ఆలోచనలు ఉన్నా, ముఖంపై మాత్రం తీయని నవ్వును ప్రదర్శించింది.

ఆమె బాలకృష్ణుడిని ఎత్తుకుని తన ఒడిలో కూర్చోబెట్టుకుంది. ఆమె తన స్తనాలకు ప్రాణాంతకమైన *కాలకూట* విషాన్ని పూసి ఉంది. ఆ విషం యొక్క ఒక చిన్న బిందువైనా ఎంతటి వారినైనా క్షణాల్లో భస్మం చేయగలదు. తన కుట్ర ఫలించిందని భావిస్తూ ఆ విషపూరిత స్తనాన్ని కృష్ణుడి నోటికి అందించింది.

సర్వేశ్వరుడైన భగవాన్ శ్రీకృష్ణుడికి ఆమె కపటత్వం మొత్తం తెలుసు. తన చిన్నారి కరపద్మాలతో ఆమె స్తనాన్ని గట్టిగా ఒడిసిపట్టి, భగవానుడు పాలు తాగడం ప్రారంభించాడు:

> **శ్రీమద్ భాగవతం, స్కంధం 10, అధ్యాయం 6, శ్లోకం 10**
> 
> *తదంకమారుహ్య గదాగ్రజోల్పకః*  
> *ప్రగృహ్య దోర్భ్యాం ప్రపిబన్ స్తనం బలాత్*  
> *సపూతనాయాః సవిషం సజీవితమ్*  
> *ప్రపీడ్య గాఢం కరయోః సరోషమ్*  
> 
> **తాత్పర్యం:** "బాలకృష్ణుడు కోపగించినట్లుగా ఆమె ఒడిలోకి ఎక్కి, తన రెండు చేతులతో ఆమె స్తనాన్ని గట్టిగా పట్టుకుని, విషంతో పాటు పూతన ప్రాణవాయువులను కూడా బలంగా తాగడం ప్రారంభించాడు."

వెలుగులీనే సూర్యుడిని చీకటి ఎలా తాకలేదో, అలాగే పరమ పవిత్రుడైన శ్రీకృష్ణుడిని ఆ కాలకూట విషం ఏమాత్రం ప్రభావితం చేయలేకపోయింది. పైగా భగవంతుడి వజ్రసంకల్ప పట్టుతో పూతన శరీరంలోని సమస్త ప్రాణాలు వేగంగా కరిగిపోసాగాయి.

### పూతన భీకర ఆర్తనాదాలు

భగవంతుడు ఆమె ప్రాణాలను పీల్చడం ప్రారంభించగానే, పూతన శరీరంలోని నరనరాల్లో విపరీతమైన మంటలు చెలరేగాయి. ఆమె మాయాశక్తులన్నీ నశించాయి. ఎముకలు పిండిపిండి అయిపోతున్నంత భరించలేని నరకయాతనను ఆమె అనుభవించింది.

ఆ భయంకర వేదనను తట్టుకోలేక ఆ రాక్షసి గిలగిలా కొట్టుకుంటూ కేకలు వేసింది:

> **శ్రీమద్ భాగవతం, స్కంధం 10, అధ్యాయం 6, శ్లోకం 11**
> 
> *సా ముంచ ముంచాలమితి ప్రభాషిణీ*  
> *నిష్పీడ్యమానాఖిలమర్మబంధనా*  
> *న్యమీలయద్ దృష్టిముదస్య బాహుకౌ*  
> *ప్రస్వేదవత్కాయ రుజోవచాలతా*  
> 
> **తాత్పర్యం:** "'నన్ను వదిలేయ్! వదిలేయ్! ఇక చాలు!' అని భయంకరంగా అరుస్తూ, సర్వాంగాలు నుజ్జునుజ్జవుతున్న బాధతో చేతులు ఆకాశం వైపు విసురుతూ, చెమటతో తడిసి ముద్దవుతూ నేలపై గిలగిలా కొట్టుకుంది."

ఆమె ఆర్తనాదాలకు ఆకాశం, భూమి కంపించాయి. చెట్లపైనున్న పక్షులు కిందపడిపోయాయి. చుట్టుపక్కల గర్భిణీ స్త్రీలు భయంతో వణికిపోయారు. ఆ బిడ్డను విదిలించి కొట్టడానికి ఆమె చేయని ప్రయత్నం లేదు, కానీ శ్రీకృష్ణుడి పట్టు వజ్రాయుధం కన్నా కఠినమైనది. ఆమెలో చివరి ప్రాణపు బొట్టు పోయేంతవరకు భగవంతుడు ఆమెను విడిచిపెట్టలేదు.

### మాయా వినాశనం మరియు పన్నెండు మైళ్ల వికృత శరీరం

ప్రాణం పోయిన వెంటనే పూతన ధరించిన అందమైన దేవకన్య రూపం మాయమై, ఆమె నిజమైన పర్వతాకార భయంకర రాక్షసి శరీరం ప్రత్యక్షమైంది:

> **శ్రీమద్ భాగవతం, స్కంధం 10, అధ్యాయం 6, శ్లోకం 14**
> 
> *పతమానః శరీరేణ ద్రుమాంశ్చక్షోదితాన్ బహూన్*  
> *పాతితవాన్ మహాన్ ఆశు శైలాదివ పతన్ ద్రుమాన్*  
> *షట్క్రోశాయతం అంగం తత్ పతితం భువి దారుణమ్*  
> 
> **తాత్పర్యం:** "ఒక పెద్ద పర్వతం కూలిపడినట్లుగా ఆమె భారీ దేహం నేలకూలినప్పుడు ఎన్నో మహావృక్షాలు తునాతునకలయ్యాయి. ఆమె భయంకర శరీరం ఆరు క్రోశాల (పన్నెండు మైళ్ల) మేర నేలపై విస్తరించి పడిపోయింది."

ఆమె నేలకూలిన శబ్దం ప్రళయ గర్జనలా ఉంది. ఆమె నోరు ఒక పెద్ద గుహలా తెరుచుకుని ఉంది, పళ్ళు నాగలి కర్రల్లా ఉన్నాయి. ఆమె బరువుకు ఎన్నో వృక్షాలు పిండిపిండైపోయాయి.

### రాక్షసి వక్షస్థలంపై చిన్ని కృష్ణుడి ఆటలు

ఆ భయంకర శబ్దాలను విని యశోద, రోహిణి, సమస్త గోపాలురు పరుగుపరుగున వచ్చారు. 

అక్కడ పన్నెండు మైళ్ల విస్తీర్ణంలో పడివున్న వికృత రాక్షసి శవాన్ని చూసి అందరూ నిశ్చేష్టులయ్యారు. కానీ వారి చూపు ఆ రాక్షసి విశాల వక్షస్థలంపై పడగానే వారి భయమంతా పరమానందంగా మారింది:

అక్కడ చిన్ని కృష్ణుడు ఏ భయమూ లేకుండా నవ్వుతూ, తన ముద్దుముద్దు పాదాలను ఆడిస్తూ ఆడుకుంటున్నాడు! అది చూసి యశోదా రోహిణులు ఆనందబాష్పాలతో ఆ భారీ శవంపైకి ఎక్కి, కన్నబిడ్డను ప్రేమతో హృదయానికి హత్తుకున్నారు!""",
                "questions": [
                    {
                        "question": "విషపూరిత స్తనాన్ని అందించినప్పుడు బాలకృష్ణుడు ఏమి చేశాడు?",
                        "options": [
                            {"text": "తన రెండు చేతులతో ఆమె స్తనాన్ని గట్టిగా పట్టుకున్నాడు", "is_correct": True},
                            {"text": "కర్రతో కొట్టాడు", "is_correct": False},
                            {"text": "దుప్పటిలో ముఖం దాచుకున్నాడు", "is_correct": False},
                            {"text": "వసుదేవుడిని పిలిచాడు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "విషంతో పాటు శ్రీకృష్ణుడు పూతన నుండి దేనిని పీల్చివేశాడు?",
                        "options": [
                            {"text": "ఆమె ప్రాణవాయువులను", "is_correct": True},
                            {"text": "ఆమె బంగారు నగలను", "is_correct": False},
                            {"text": "ఆమె పట్టు వస్త్రాలను", "is_correct": False},
                            {"text": "ఆమె రథాన్ని", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ప్రాణాలు పోయే వేదనలో పూతన ఏమని అరిచింది?",
                        "options": [
                            {"text": "'ముంచ ముంచ అలమ్!' ('నన్ను వదిలేయ్, వదిలేయ్, ఇక చాలు!')", "is_correct": True},
                            {"text": "'కంసా నన్ను కాపాడు!'", "is_correct": False},
                            {"text": "'ఇంకా పాలు తాగు!'", "is_correct": False},
                            {"text": "'నందమహారాజు ఎక్కడ?'", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ప్రాణం పోయిన తర్వాత పూతన అందమైన రూపం ఏమైంది?",
                        "options": [
                            {"text": "మాయ తొలిగి పన్నెండు మైళ్ల భయంకర రాక్షసి రూపం వెలుగుచూసింది", "is_correct": True},
                            {"text": "బంగారంగా మారింది", "is_correct": False},
                            {"text": "నీరుగా కరిగిపోయింది", "is_correct": False},
                            {"text": "పావురంగా మారి ఎగిరిపోయింది", "is_correct": False}
                        ]
                    },
                    {
                        "question": "నేలకూలిన పూతన శవం ఎంత పొడవు విస్తరించి ఉంది?",
                        "options": [
                            {"text": "ఆరు క్రోశాలు (పన్నెండు మైళ్లు)", "is_correct": True},
                            {"text": "వంద గజాలు", "is_correct": False},
                            {"text": "పది అడుగులు", "is_correct": False},
                            {"text": "యాభై మైళ్లు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పూతన శరీరం పడినప్పుడు చెట్లకు ఏమైంది?",
                        "options": [
                            {"text": "అనేక మహావృక్షాలు తునాతునకలయ్యాయి", "is_correct": True},
                            {"text": "చెట్లు కాలిపోయాయి", "is_correct": False},
                            {"text": "చెట్లకు బంగారు కాయలు కాశాయి", "is_correct": False},
                            {"text": "చెట్లకు ఏమీ కాలేదు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పూతన కూలిన తర్వాత బాలకృష్ణుడు ఎక్కడ కనిపించాడు?",
                        "options": [
                            {"text": "రాక్షసి వక్షస్థలంపై నిర్భయంగా ఆడుకుంటూ కనిపించాడు", "is_correct": True},
                            {"text": "ఒక పెద్ద బండరాయి కింద", "is_correct": False},
                            {"text": "యమునా నదిలో ఈదుతూ", "is_correct": False},
                            {"text": "నందభవనంలో నిద్రిస్తూ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "కాలకూట విషం బాలకృష్ణుడికి ఎందుకు హాని చేయలేకపోయింది?",
                        "options": [
                            {"text": "ఆయన పరమ పవిత్రుడైన భగవంతుడు; సూర్యుడిని చీకటి తాకలేనట్లే విషం ఆయనను తాకలేదు", "is_correct": True},
                            {"text": "ఆయన ఔషధం తాగి ఉన్నాడు", "is_correct": False},
                            {"text": "విషం గడువు తీరిపోయింది", "is_correct": False},
                            {"text": "పూతన విషం పూయడం మరచిపోయింది", "is_correct": False}
                        ]
                    },
                    {
                        "question": "కృష్ణుడిని చూసిన యశోదా రోహిణులు ఏమి చేశారు?",
                        "options": [
                            {"text": "ఆ భారీ శరీరంపైకి ఎక్కి బిడ్డను ప్రేమతో హత్తుకున్నారు", "is_correct": True},
                            {"text": "భయంతో పారిపోయారు", "is_correct": False},
                            {"text": "బిడ్డను తిట్టారు", "is_correct": False},
                            {"text": "సైన్యాన్ని పిలిచారు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "పూతన ఆరు క్రోశాల శరీరాన్ని వర్ణించే శ్లోకం ఏది?",
                        "options": [
                            {"text": "స్కంధం 10, అధ్యాయం 6, శ్లోకం 14", "is_correct": True},
                            {"text": "స్కంధం 10, అధ్యాయం 6, శ్లోకం 1", "is_correct": False},
                            {"text": "స్కంధం 10, అధ్యాయం 1, శ్లోకం 10", "is_correct": False},
                            {"text": "స్కంధం 10, అధ్యాయం 3, శ్లోకం 25", "is_correct": False}
                        ]
                    }
                ]
            },
            "kn": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "ಪೂತನಾ ಸಂಹಾರ ಮತ್ತು ಆಕೆಯ ಬೃಹತ್ ಶರೀರದ ಪತನ ಲೀಲೆ",
                "content": """### ವಿಷಪೂರಿತ ಸ್ತನವನ್ನು ಬಾಲಕೃಷ್ಣನು ದೃಢವಾಗಿ ಹಿಡಿಯುವುದು

ತಾಯಿ ಯಶೋದೆಯ ಕೋಣೆಯೊಳಗೆ ನುಗ್ಗಿದ ಪೂತನೆ ಬಾಲಕೃಷ್ಣನ ತೊಟ್ಟಿಲ ಬಳಿ ಸಾಗಿದಳು. ಅವಳ ಮನಸ್ಸಿನಲ್ಲಿ ಕೊಲೆಯ ದುರುದ್ದೇಶವಿದ್ದರೂ, ಮುಖದಲ್ಲಿ ಪ್ರೀತಿಯ ನಗೆಯನ್ನು ಪ್ರದರ್ಶಿಸಿದಳು.

ಅವಳು ಮಗುವನ್ನು ತನ್ನ ಮಡಿಲಿಗೆತ್ತಿಕೊಂಡಳು. ಅವಳ ಸ್ತನಗಳಿಗೆ *ಕಾಲಕೂಟ* ಎಂಬ ಪ್ರಾಣಾಂತಕ ಹಾಲಾಹಲ ವಿಷವನ್ನು ಸವರಲಾಗಿತ್ತು. ಆ ವಿಷದ ಒಂದು ಸಣ್ಣ ಹನಿಯೂ ಯಾರನ್ನಾದರೂ ಕ್ಷಣಾರ್ಧದಲ್ಲಿ ಭಸ್ಮ ಮಾಡಬಲ್ಲದ್ದಾಗಿತ್ತು. ತನ್ನ ಯೋಜನೆ ಸಫಲವಾಯಿತೆಂದು ಭಾವಿಸಿ ಅವಳು ವಿಷದ ಮೊಲೆಯನ್ನು ಕೃಷ್ಣನ ಬಾಯಿಗೆ ನೀಡಿದಳು.

ಸರ್ವೇಶ್ವರನಾದ ಭಗವಾನ್ ಶ್ರೀಕೃಷ್ಣನಿಗೆ ಅವಳ ಎಲ್ಲ ಕಪಟವೂ ತಿಳಿದಿತ್ತು. ತನ್ನ ಪುಟ್ಟ ಕಮಲದಂತಹ ಎರಡು ಕೈಗಳಿಂದ ಅವಳ ಸ್ತನವನ್ನು ಗಟ್ಟಿಯಾಗಿ ಹಿಡಿದು, ಭಗವಂತನು ಹಾಲನ್ನು ಹೀರುತ್ತಾ ಸಾಗಿದನು:

> **ಶ್ರೀಮದ್ ಭಾಗವತಂ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 6, ಶ್ಲೋಕ 10**
> 
> *ತದಂಕಮಾರುಹ್ಯ ಗದಾಗ್ರಜೋಲ್ಪಕಃ*  
> *ಪ್ರಗೃಹ್ಯ ದೋರ್ಭ್ಯಾಂ ಪ್ರಪಿಬನ್ ಸ್ತನಂ ಬಲಾತ್*  
> *ಸಪೂತನಾಯಾಃ ಸವಿಷಂ ಸಜೀವಿತಮ್*  
> *ಪ್ರಪೀಡ್ಯ ಗಾಢಂ ಕರಯೋಃ ಸರೋಷಮ್*  
> 
> **ಭಾವಾರ್ಥ:** "ಬಾಲಕೃಷ್ಣನು ಕೋಪಗೊಂಡವನಂತೆ ಅವಳ ಮಡಿಲನ್ನೇರಿ, ಎರಡೂ ಕೈಗಳಿಂದ ಅವಳ ಸ್ತನವನ್ನು ಗಟ್ಟಿಯಾಗಿ ಅದುಮಿ, ವಿಷದ ಜೊತೆಗೆ ಪೂತನೆಯ ಪ್ರಾಣವಾಯುವನ್ನೇ ಹೀರಿಕೊಳ್ಳತೊಡಗಿದನು."

ಸೂರ್ಯನನ್ನು ಕತ್ತಲೆಯು ಮುಟ್ಟಲಾರದಂತೆ, ಪರಿಶುದ್ಧನಾದ ಭಗವಂತನಿಗೆ ಕಾಲಕೂಟ ವಿಷವು ಕಿಂಚಿತ್ತೂ ಹಾನಿ ಮಾಡಲಿಲ್ಲ. ಬದಲಾಗಿ, ಭಗವಂತನ ವಜ್ರದಂತಹ ಬಲವಾದ ಆಕರ್ಷಣೆಯಿಂದ ಆಕೆಯ ಜೀವವೇ ಬರಿದಾಗತೊಡಗಿತು.

### ಪೂತನೆಯ ಭೀಕರ ಚೀತ್ಕಾರ ಮತ್ತು ನರಳಾಟ

ಪ್ರಾಣವಾಯು ಹೀರುತ್ತಿದ್ದಂತೆ ಪೂತನೆಯ ಇಡೀ ದೇಹದಲ್ಲಿ ಅಸಹನೀಯ ಉರಿ ಆರಂಭವಾಯಿತು. ಆಕೆಯ ಸಮಸ್ತ ಮಾಯಾಶಕ್ತಿಯೂ ನಶಿಸಿತು. ಆಕೆಯ ಎಲುಬುಗಳೆಲ್ಲ ಪುಡಿಪುಡಿಯಾಗುತ್ತಿರುವಂತಹ ತೀವ್ರ ಯಾತನೆ ಅವಳಿಗೆ ಆಯಿತು.

ಆ ತೀವ್ರ ನೋವಿನಿಂದ ಆ ರಾಕ್ಷಸಿಯು ನರಳುತ್ತಾ ಕಿರುಚಿಕೊಂಡಳು:

> **ಶ್ರೀಮದ್ ಭಾಗವತಂ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 6, ಶ್ಲೋಕ 11**
> 
> *ಸಾ ಮುಂಚ ಮುಂಚಾಲಮಿತಿ ಪ್ರಭಾಷಿಣೀ*  
> *ನಿಷ್ಪೀಡ್ಯಮಾನಾಖಿಲಮರ್ಮಬಂಧನಾ*  
> *ನ್ಯಮೀಲಯದ್ ದೃಷ್ಟಿಮುದಸ್ಯ ಬಾಹುಕೌ*  
> *ಪ್ರಸ್ವೇದವತ್ಕಾಯ ರುಜೋವಚಾಲತಾ*  
> 
> **ಭಾವಾರ್ಥ:** "'ನನ್ನನ್ನು ಬಿಡು! ಬಿಡು! ಸಾಕು ಇಷ್ಟೇ!' ಎಂದು ಕಿರುಚುತ್ತಾ, ದೇಹದ ಎಲ್ಲಾ ಮರ್ಮಸ್ಥಾನಗಳು ಪುಡಿಯಾಗುವ ಯಾತನೆಯಿಂದ ಕೈಗಳನ್ನು ಆಕಾಶಕ್ಕೆ ಚಾಚಿ, ಬೆವರಿನಿಂದ ತೊಯ್ದು ನೆಲದ ಮೇಲೆ ಒದ್ದಾಡಿದಳು."

ಆಕೆಯ ಭೀಕರ ಚೀತ್ಕಾರಕ್ಕೆ ಆಕಾಶ, ಭೂಮಿ ನಡುಗಿದವು. ಗಿಡಗಳಿಂದ ಪಕ್ಷಿಗಳು ಉದುರಿದವು. ಆ ಮಗುವನ್ನು ಕಿತ್ತು ಎಸೆಯಲು ಅವಳು ಎಷ್ಟೇ ಪ್ರಯತ್ನಿಸಿದರೂ ಕೃಷ್ಣನ ಹಿಡಿತವು ಬಿಗಿಯಾಗಿಯೇ ಇತ್ತು. ಆಕೆಯ ಕೊನೆಯ ಉಸಿರು ಹೋಗುವವರೆಗೂ ಭಗವಂತನು ಬಿಡಲಿಲ್ಲ.

### ಮಾಯೆ ನಾಶವಾಗಿ ಬಿದ್ದ ಹನ್ನೆರಡು ಮೈಲಿ ಉದ್ದದ ಶವ

ಪ್ರಾಣ ಹೋದ ಕೂಡಲೇ ಪೂತನೆಯ ದೇವಕನ್ಯೆಯ ವೇಷ ಮರೆಯಾಗಿ, ಅವಳ ನಿಜವಾದ ಪರ್ವತಾಕಾರದ ರಾಕ್ಷಸಿ ಶರೀರ ಪ್ರಕಟವಾಯಿತು:

> **ಶ್ರೀಮದ್ ಭಾಗವತಂ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 6, ಶ್ಲೋಕ 14**
> 
> *ಪತಮಾನಃ ಶರೀರೇಣ ದ್ರುಮಾಂಶ್ಚಕ್ಷೋದಿತಾನ್ ಬಹೂನ್*  
> *ಪಾತಿತವಾನ್ ಮಹಾನ್ ಆಶು ಶೈಲಾದಿವ ಪತನ್ ದ್ರುಮಾನ್*  
> *ಷಟ್ಕ್ರೋಶಾಯತಮ್ ಅಂಗಂ ತತ್ ಪತಿತಂ ಭುವಿ ದಾರುಣಮ್*  
> 
> **ಭಾವಾರ್ಥ:** "ಒಂದು ದೊಡ್ಡ ಪರ್ವತವೇ ಉರುಳಿಬಿದ್ದಂತೆ ಆಕೆಯ ಭಾರೀ ಶರೀರವು ನೆಲಕ್ಕುರುಳಿದಾಗ ಅನೇಕ ಬೃಹತ್ ವೃಕ್ಷಗಳು ಪುಡಿಪುಡಿಯಾದವು. ಆಕೆಯ ಆರು ಕ್ರೋಶಗಳ (ಹನ್ನೆರಡು ಮೈಲಿಗಳ) ಭಯಾನಕ ಶವವು ನೆಲದ ಮೇಲೆ ಪಸರಿಸಿತು."

ಆಕೆ ನೆಲಕ್ಕುರುಳಿದ ಸದ್ದು ಭೀಕರ ಗುಡುಗಿನಂತಿತ್ತು. ಆಕೆಯ ಬಾಯಿ ದೊಡ್ಡ ಗುಹೆಯಂತಿತ್ತು, ಹಲ್ಲುಗಳು ನೇಗಿಲಿನ ಫಾಲಗಳಂತಿದ್ದವು. ಆಕೆಯ ಭಾರಕ್ಕೆ ಎಷ್ಟೋ ಮರಗಳು ಮುರಿದುಬಿದ್ದವು.

### ರಾಕ್ಷಸಿಯ ಎದೆಯ ಮೇಲೆ ಆಟವಾಡುತ್ತಿದ್ದ ಕೃಷ್ಣ

ಆ ಭೀಕರ ಶಬ್ದವನ್ನು ಕೇಳಿ ತಾಯಿ ಯಶೋದಾ, ರೋಹಿಣಿ ಮತ್ತು ಎಲ್ಲ ಗೋಪಾಲಕರು ಗಾಬರಿಯಿಂದ ಓಡಿಬಂದರು. 

ಅಲ್ಲಿ ಹನ್ನೆರಡು ಮೈಲಿ ಉದ್ದಕ್ಕೆ ಬಿದ್ದಿದ್ದ ಆ ರಾಕ್ಷಸಿಯ ಶವವನ್ನು ನೋಡಿ ಎಲ್ಲರೂ ದಂಗಾದರು. ಆದರೆ ಅವರ ದೃಷ್ಟಿ ಆಕೆಯ ಎದೆಯ ಮೇಲ್ಭಾಗಕ್ಕೆ ಹೋದಾಗ ಅವರ ಆತಂಕವೆಲ್ಲ ಪರಮಾನಂದವಾಯಿತು:

ಅಲ್ಲಿ ಪುಟ್ಟ ಬಾಲಕೃಷ್ಣನು ಯಾವುದೇ ಭಯವಿಲ್ಲದೆ ನಗುತ್ತಾ, ತನ್ನ ಕಾಲುಗಳನ್ನು ಆಡಿಸುತ್ತಾ ಆಟವಾಡುತ್ತಿದ್ದನು! ಅದನ್ನು ಕಂಡು ಯಶೋದಾ ಮತ್ತು ರೋಹಿಣಿ ಆ ಮಹಾಶರೀರದ ಮೇಲೆ ಹತ್ತಿ, ತಮ್ಮ ಮುದ್ದು ಕಂದನನ್ನು ಪ್ರೀತಿಯಿಂದ ಎತ್ತಿ ಮುದ್ದಾಡಿದರು!""",
                "questions": [
                    {
                        "question": "ವಿಷದ ಮೊಲೆಯನ್ನು ಮುಂದಿಟ್ಟಾಗ ಬಾಲಕೃಷ್ಣನು ಏನು ಮಾಡಿದನು?",
                        "options": [
                            {"text": "ಎರಡೂ ಕೈಗಳಿಂದ ಆಕೆಯ ಸ್ತನವನ್ನು ಗಟ್ಟಿಯಾಗಿ ಹಿಡಿದುಕೊಂಡನು", "is_correct": True},
                            {"text": "ಕೋಲಿನಿಂದ ಹೊಡೆದನು", "is_correct": False},
                            {"text": "ಮುಖ ಮುಚ್ಚಿಕೊಂಡನು", "is_correct": False},
                            {"text": "ವಸುದೇವನನ್ನು ಕರೆದನು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ವಿಷದ ಜೊತೆಗೆ ಶ್ರೀಕೃಷ್ಣನು ಪೂತನೆಯಿಂದ ಏನನ್ನು ಹೀರಿಕೊಂಡನು?",
                        "options": [
                            {"text": "ಆಕೆಯ ಪ್ರಾಣವಾಯುವನ್ನು", "is_correct": True},
                            {"text": "ಆಕೆಯ ಬಂಗಾರದ ಒಡವೆಗಳನ್ನು", "is_correct": False},
                            {"text": "ಆಕೆಯ ರೇಷ್ಮೆ ಸೀರೆಯನ್ನು", "is_correct": False},
                            {"text": "ಆಕೆಯ ರಥವನ್ನು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಪ್ರಾಣ ಹೋಗುವ ಯಾತನೆಯಲ್ಲಿ ಪೂತನೆ ಏನೆಂದು ಕಿರುಚಿದಳು?",
                        "options": [
                            {"text": "'ಮುಂಚ ಮುಂಚ ಅಲಮ್!' ('ನನ್ನನ್ನು ಬಿಡು, ಬಿಡು, ಸಾಕು!')", "is_correct": True},
                            {"text": "'ಕಂಸ ನನ್ನನ್ನು ಕಾಪಾಡು!'", "is_correct": False},
                            {"text": "'ಇನ್ನೂ ಹಾಲು ಕುಡಿ!'", "is_correct": False},
                            {"text": "'ನಂದಮಹಾರಾಜ ಎಲ್ಲಿ?'", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಪ್ರಾಣ ಹೋದ ನಂತರ ಪೂತನೆಯ ಸುಂದರ ವೇಷ ಏನಾಯಿತು?",
                        "options": [
                            {"text": "ಮಾಯೆ ಕರಗಿ ಹನ್ನೆರಡು ಮೈಲಿ ಉದ್ದದ ರಾಕ್ಷಸಿ ಶರೀರ ಪ್ರಕಟವಾಯಿತು", "is_correct": True},
                            {"text": "ಬಂಗಾರವಾಯಿತು", "is_correct": False},
                            {"text": "ನೀರಿನಂತೆ ಕರಗಿತು", "is_correct": False},
                            {"text": "ಪಾರಿವಾಳವಾಗಿ ಹಾರಿಹೋಯಿತು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ನೆಲಕ್ಕುರುಳಿದ ಪೂತನೆಯ ಶವದ ಉದ್ದವೆಷ್ಟಿತ್ತು?",
                        "options": [
                            {"text": "ಆರು ಕ್ರೋಶಗಳು (ಹನ್ನೆರಡು ಮೈಲಿಗಳು)", "is_correct": True},
                            {"text": "ನೂರು ಗಜಗಳು", "is_correct": False},
                            {"text": "ಹತ್ತು ಅಡಿಗಳು", "is_correct": False},
                            {"text": "ಐವತ್ತು ಮೈಲಿಗಳು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಪೂತನೆಯ ಶರೀರ ಬಿದ್ದಾಗ ಮರಗಳಿಗೆ ಏನಾಯಿತು?",
                        "options": [
                            {"text": "ಅನೇಕ ಬೃಹತ್ ಮರಗಳು ಪುಡಿಪುಡಿಯಾದವು", "is_correct": True},
                            {"text": "ಮರಗಳು ಸುಟ್ಟುಹೋದವು", "is_correct": False},
                            {"text": "ಮರಗಳಿಗೆ ಬಂಗಾರದ ಹಣ್ಣುಗಳು ಬಿಟ್ಟವು", "is_correct": False},
                            {"text": "ಮರಗಳಿಗೆ ಏನೂ ಆಗಲಿಲ್ಲ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಪೂತನೆ ಬಿದ್ದ ನಂತರ ಬಾಲಕೃಷ್ಣ ಎಲ್ಲಿ ಕಂಡುಬಂದನು?",
                        "options": [
                            {"text": "ರಾಕ್ಷಸಿಯ ಎದೆಯ ಮೇಲೆ ನಿರ್ಭಯವಾಗಿ ಆಟವಾಡುತ್ತಿದ್ದನು", "is_correct": True},
                            {"text": "ಒಂದು ಬಂಡೆಯ ಕೆಳಗೆ", "is_correct": False},
                            {"text": "ಯಮುನೆಯಲ್ಲಿ ತೇಲುತ್ತಿದ್ದನು", "is_correct": False},
                            {"text": "ಮನೆಯಲ್ಲಿ ಮಲಗಿದ್ದನು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಕಾಲಕೂಟ ವಿಷವು ಶ್ರೀಕೃಷ್ಣನಿಗೆ ಏಕೆ ಹಾನಿ ಮಾಡಲಿಲ್ಲ?",
                        "options": [
                            {"text": "ಆತನು ಪರಮ ಪವಿತ್ರ ಭಗವಂತ; ಸೂರ್ಯನನ್ನು ಕತ್ತಲೆ ಸೋಲಿಸಲಾರದಂತೆ ವಿಷ ಆತನನ್ನು ಬಾಧಿಸಲಾರದು", "is_correct": True},
                            {"text": "ಆತನು ಔಷಧಿ ಕುಡಿದಿದ್ದನು", "is_correct": False},
                            {"text": "ವಿಷದ ಶಕ್ತಿ ಕುಂದಿತ್ತು", "is_correct": False},
                            {"text": "ಪೂತನೆ ವಿಷ ಸವರಲು ಮರೆತಿದ್ದಳು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಕೃಷ್ಣನನ್ನು ಕಂಡ ತಾಯಂದಿರು ಏನು ಮಾಡಿದರು?",
                        "options": [
                            {"text": "ಆ ಬೃಹತ್ ಶರೀರದ ಮೇಲೆ ಹತ್ತಿ ಕಂದನನ್ನು ಎತ್ತಿಕೊಂಡರು", "is_correct": True},
                            {"text": "ಭಯದಿಂದ ಓಡಿಹೋದರು", "is_correct": False},
                            {"text": "ಮಗುವನ್ನು ಬೈದರು", "is_correct": False},
                            {"text": "ಸೈನ್ಯವನ್ನು ಕರೆದರು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಪೂತನೆಯ ಆರು ಕ್ರೋಶ ಉದ್ದದ ಶರೀರವನ್ನು ವಿವರಿಸುವ ಶ್ಲೋಕ ಯಾವುದು?",
                        "options": [
                            {"text": "ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 6, ಶ್ಲೋಕ 14", "is_correct": True},
                            {"text": "ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 6, ಶ್ಲೋಕ 1", "is_correct": False},
                            {"text": "ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 1, ಶ್ಲೋಕ 10", "is_correct": False},
                            {"text": "ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 3, ಶ್ಲೋಕ 25", "is_correct": False}
                        ]
                    }
                ]
            },
            "ml": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "പൂതനാമോക്ഷവും രാക്ഷസിയുടെ പടുകൂറ്റൻ പതനവും",
                "content": """### വിഷമുലയെ ഉറക്കെപ്പിടിച്ച് ഭഗവാൻ

യശോദ അമ്മയുടെ മുറിയിൽ കടന്നുകൂടിയ പൂതന ഉണ്ണിക്കണ്ണന്റെ തൊട്ടിലിനടുത്തേക്ക് ചെന്നു. മനസ്സിൽ വിഷപ്പുകയായിരുന്നെങ്കിലും മുഖത്ത് വാത്സല്യത്തിന്റെ ചിരി അവൾ കാട്ടി.

കപട സ്നേഹത്തോടെ അവൾ കുഞ്ഞിനെ മടിയിലെടുത്തു. ആരെയും ഞൊടിയിടയിൽ ചാരമാക്കാൻ ശേഷിയുള്ള *കാളകൂടവിഷം* പുരട്ടിയ മുല അവൾ കുഞ്ഞിന്റെ ചുണ്ടുകളിൽ വെച്ചുകൊടുത്തു. തന്റെ പദ്ധതി വിജയിച്ചെന്ന അഹങ്കാരത്തോടെ അവൾ പാലൂട്ടാൻ തുടങ്ങി.

എന്നാൽ സർവ്വജ്ഞനായ ഭഗവാൻ ശ്രീകൃഷ്ണൻ അവളുടെ ദുഷ്ടലക്ഷ്യം പൂർണ്ണമായും അറിഞ്ഞിരുന്നു. തന്റെ ചെറിയ താമരക്കൈകൾ കൊണ്ട് അവളുടെ മുലയെ ശക്തമായി അമർത്തിപ്പിടിച്ചുകൊണ്ട് ഭഗവാൻ പാലു കുടിക്കാൻ തുടങ്ങി:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അധ്യായം 6, ശ്ലോകം 10**
> 
> *തദങ്കമാരുഹ്യ ഗദാഗ്രജോല്പകഃ*  
> *പ്രഗൃഹ്യ ദോർഭ്യാം പ്രപിബൻ സ്തനം ബലാത്*  
> *സപൂതനായാഃ സവിഷം സജീവിതമ്*  
> *പ്രപീഡ്യ ഗാഢം കരയോഃ സരോഷമ്*  
> 
> **അർത്ഥം:** "ഉണ്ണിക്കണ്ണൻ കോപത്തോടെയെന്നപോലെ അവളുടെ മടിയിൽ കയറി, ഇരു കൈകളാലും അവളുടെ മുലയെ മുറുകെപ്പിടിച്ച്, വിഷത്തോടൊപ്പം പൂതനയുടെ പ്രാണവായുവിനെയും ഊറ്റിക്കുടിക്കാൻ തുടങ്ങി."

സൂര്യനെ അന്ധകാരത്തിന് സ്പർശിക്കാൻ കഴിയാത്തതുപോലെ, പരമപവിത്രനായ ഭഗവാനെ ആ കാളകൂടവിഷത്തിന് തൊടാൻ പോലുമായില്ല. മറിച്ച് ഭഗവാന്റെ ദിവ്യമായ ശക്തിയാൽ അവളുടെ ജീവശ്വാസം തന്നെ വലിഞ്ഞുപോയി.

### പൂതനയുടെ ഭീകര നിലവിളി

പ്രാണൻ ചോർന്നുപോയപ്പോൾ പൂതനയുടെ സർവ്വാംഗങ്ങളിലും അഗ്നിജ്വാല പടരുന്നതുപോലെ തോന്നി. അവളുടെ മായാശക്തികളെല്ലാം അസ്തമിച്ചു. അസ്ഥികളെല്ലാം തകർന്നുപോകുന്ന കഠിനമായ വേദന അവളനുഭവിച്ചു.

വേദന സഹിക്കാനാവാതെ ആ രാക്ഷസി അലറിവിളിച്ചു:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അധ്യായം 6, ശ്ലോകം 11**
> 
> *സാ മുഞ്ച മുഞ്ചാലമിതി പ്രഭാഷിണീ*  
> *നിഷ്പീഡ്യമാനാഖിലമർമ്മബന്ധനാ*  
> *ന്യമീലയദ് ദൃഷ്ടിമുദസ്യ ബാഹുകൗ*  
> *പ്രസ്വേദവത്കായ രുജോവചാലതാ*  
> 
> **അർത്ഥം:** "'എന്നെ വിടൂ! എന്നെ വിടൂ! മതിയായി!' എന്ന് ഉറക്കെ നിലവിളിച്ചുകൊണ്ട്, ശരീരത്തിലെ സർവ്വ മർമ്മങ്ങളും തകർന്നടിയുന്ന വേദനയാൽ അവൾ ആകാശത്തേക്ക് കൈകൾ വീശി നിലത്തുരുണ്ടു."

അവളുടെ അലർച്ചയിൽ ആകാശവും ഭൂമിയും വിറച്ചു. മരങ്ങളിൽനിന്ന് പക്ഷികൾ താഴെ വീണു. കുട്ടിയെ തള്ളിമാറ്റാൻ അവൾ പഠിച്ച പണി പതിനെട്ടും നോക്കി, പക്ഷെ ഭഗവാന്റെ പിടി വജ്രത്തേക്കാൾ ഉറച്ചതായിരുന്നു. അവളുടെ അവസാന ശ്വാസവും തീരുന്നതുവരെ ഭഗവാൻ വിട്ടില്ല.

### മായ നശിക്കുന്നു; പന്ത്രണ്ട് മൈൽ നീളമുള്ള പതനം

പ്രാണൻ വേർപെട്ട നിമിഷം പൂതനയുടെ ദേവസ്ത്രീ രൂപം അപ്രത്യക്ഷമായി, അവളുടെ പർവ്വതതുല്യമായ ഭീകര രൂപം പുറത്തുവന്നു:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അധ്യായം 6, ശ്ലോകം 14**
> 
> *പതമാനഃ ശരീരേണ ദ്രുമാംശ്ചക്ഷോദിതാൻ ബഹൂൻ*  
> *പാതിതവാൻ മഹാൻ ആശു ശൈലാദിവ പതൻ ദ്രുമാൻ*  
> *ഷട്ക്രോശായതമ് അംഗം തത് പതിതം ഭുവി ദാരുണമ്*  
> 
> **അർത്ഥം:** "ഒരു വലിയ പർവ്വതം ഇടിഞ്ഞുവീഴുന്നതുപോലെ അവളുടെ പടുകൂറ്റൻ ശരീരം നിലംപതിച്ചപ്പോൾ അനേകം വന്മരങ്ങൾ പൊടിപൊടിയായി. ആറ് ക്രോശം (പന്ത്രണ്ട് മൈൽ) നീളമുള്ള ആ ഭീകര ശരീരം ഭൂമിയിൽ വീണുകിടന്നു."

അവൾ വീണ ശബ്ദം ഇടിവെട്ടുപോലെയായിരുന്നു. ഗുഹപോലെ തുറന്ന വായയും, കലപ്പപോലെയുള്ള പല്ലുകളുമായി ആ ശരീരം കിടന്നു. അവളുടെ ശരീരഭാരത്താൽ കാടുകൾ തകർന്നുപോയി.

### രാക്ഷസിയുടെ മാറിലിരുന്ന് ഉണ്ണിക്കണ്ണന്റെ കളി

ഭയാനകമായ ആ ശബ്ദം കേട്ട് യശോദ അമ്മയും രോഹിണി അമ്മയും ഗോപന്മാരും അങ്ങോട്ടേക്ക് പാഞ്ഞെത്തി. 

പന്ത്രണ്ട് മൈൽ നീളത്തിൽ കിടക്കുന്ന ഭീകരരൂപം കണ്ട് എല്ലാവരും സ്തംഭിച്ചുപോയി. എന്നാൽ അവളുടെ വലിയ നെഞ്ചിലേക്ക് നോക്കിയപ്പോൾ അവരുടെ ഭയം ആനന്ദമായി മാറി:

അവിടെ ഉണ്ണിക്കണ്ണൻ യാതൊരു ഭയവുമില്ലാതെ ചിരിച്ചുകൊണ്ട്, കാൽവിരലുകൾ വായിലിട്ട് കളിക്കുകയായിരുന്നു! അത് കണ്ട് ആശ്വാസത്തോടെ യശോദയും രോഹിണിയും ആ പടുകൂറ്റൻ ശരീരത്തിൽ ഓടിക്കയറി ഉണ്ണിയെ വാരിപ്പുണർന്നു!""",
                "questions": [
                    {
                        "question": "വിഷമുല നൽകിയപ്പോൾ ഉണ്ണിക്കണ്ണൻ എന്താണ് ചെയ്തത്?",
                        "options": [
                            {"text": "ഇരുകൈകൾ കൊണ്ടും അവളുടെ മുലയെ അമർത്തിപ്പിടിച്ചു", "is_correct": True},
                            {"text": "വടികൊണ്ടടിച്ചു", "is_correct": False},
                            {"text": "പുതപ്പുകൊണ്ട് മുഖം മറച്ചു", "is_correct": False},
                            {"text": "വസുദേവരെ വിളിച്ചു", "is_correct": False}
                        ]
                    },
                    {
                        "question": "വിഷത്തോടൊപ്പം ഭഗവാൻ പൂതനയിൽ നിന്ന് എന്താണ് ഊറ്റിയെടുത്തത്?",
                        "options": [
                            {"text": "അവളുടെ പ്രാണവായുവിനെ", "is_correct": True},
                            {"text": "സ്വർണ്ണാഭരണങ്ങളെ", "is_correct": False},
                            {"text": "പട്ടുചേലകളെ", "is_correct": False},
                            {"text": "അവളുടെ രഥത്തെ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "വേദന സഹിക്കാനാവാതെ പൂതന എന്താണ് അലറിവിളിച്ചത്?",
                        "options": [
                            {"text": "'മുഞ്ച മുഞ്ച ആലം!' ('എന്നെ വിടൂ, വിടൂ, മതിയായി!')", "is_correct": True},
                            {"text": "'കംസാ എന്നെ രക്ഷിക്കൂ!'", "is_correct": False},
                            {"text": "'കൂടുതൽ പാലു കുടിക്കൂ!'", "is_correct": False},
                            {"text": "'നന്ദഗോപർ എവിടെ?'", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പ്രാണൻ പോയതോടെ പൂതനയുടെ സുന്ദര രൂപത്തിന് എന്തുപറ്റി?",
                        "options": [
                            {"text": "മായ നശിച്ചു പന്ത്രണ്ട് മൈൽ നീളമുള്ള ഭീകര രൂപം പുറത്തുവന്നു", "is_correct": True},
                            {"text": "അത് സ്വർണ്ണമായി മാറി", "is_correct": False},
                            {"text": "അത് വെള്ളമായി ഒഴുകിപ്പോയി", "is_correct": False},
                            {"text": "അതൊരു പ്രാവായി മാറി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "നിലംപതിച്ച പൂതനയുടെ ശരീരത്തിന് എത്ര നീളമുണ്ടായിരുന്നു?",
                        "options": [
                            {"text": "ആറ് ക്രോശം (പന്ത്രണ്ട് മൈൽ)", "is_correct": True},
                            {"text": "നൂറ് വാര", "is_correct": False},
                            {"text": "പത്തടി", "is_correct": False},
                            {"text": "അമ്പത് മൈൽ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പൂതനയുടെ ശരീരം വീണപ്പോൾ മരങ്ങൾക്ക് എന്തു സംഭവിച്ചു?",
                        "options": [
                            {"text": "അനേകം വന്മരങ്ങൾ പൊടിപൊടിയായി തകർന്നു", "is_correct": True},
                            {"text": "മരങ്ങൾക്ക് തീപിടിച്ചു", "is_correct": False},
                            {"text": "മരങ്ങളിൽ സ്വർണ്ണപ്പഴങ്ങൾ ഉണ്ടായി", "is_correct": False},
                            {"text": "മരങ്ങൾക്ക് ഒന്നും സംഭവിച്ചില്ല", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പൂതന വീണുകിടന്നപ്പോൾ ഉണ്ണിക്കണ്ണനെ എവിടെയാണ് കണ്ടത്?",
                        "options": [
                            {"text": "രാക്ഷസിയുടെ മാറിലിരുന്ന് നിർഭയമായി കളിക്കുന്നതായി", "is_correct": True},
                            {"text": "ഒരു പാറയുടെ അടിയിൽ", "is_correct": False},
                            {"text": "യമുനയിൽ നീന്തുന്നതായി", "is_correct": False},
                            {"text": "മുറിയിൽ ഉറങ്ങുന്നതായി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "കാളകൂടവിഷം ഭഗവാന് ദോഷം വരുത്താതിരുന്നത് എന്തുകൊണ്ട്?",
                        "options": [
                            {"text": "ഭഗവാൻ പരമപവിത്രനായ ഈശ്വരനാണ്; സൂര്യനെ ഇരുട്ടിന് തൊടാനാവാത്തതുപോലെ വിഷം ഭഗവാനെ ബാധിക്കില്ല", "is_correct": True},
                            {"text": "ഭഗവാൻ മരുന്ന് കുടിച്ചിരുന്നു", "is_correct": False},
                            {"text": "വിഷത്തിന്റെ വീര്യം പോയിരുന്നു", "is_correct": False},
                            {"text": "പൂതന വിഷം പുരട്ടാൻ മറന്നുപോയി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഉണ്ണിയെ സുരക്ഷിതനായി കണ്ട അമ്മമാർ എന്തുചെയ്തു?",
                        "options": [
                            {"text": "ആ ശരീരത്തിൽ ഓടിക്കയറി ഉണ്ണിയെ മാറോടണച്ചു", "is_correct": True},
                            {"text": "പേടിച്ചോടിപ്പോയി", "is_correct": False},
                            {"text": "കുഞ്ഞിനെ വഴക്കുപറഞ്ഞു", "is_correct": False},
                            {"text": "സൈന്യത്തെ വിളിച്ചു", "is_correct": False}
                        ]
                    },
                    {
                        "question": "പൂതനയുടെ ആറ് ക്രോശം നീളമുള്ള ശരീരത്തെ വർണ്ണിക്കുന്ന ശ്ലോകം ഏതാണ്?",
                        "options": [
                            {"text": "സ്കന്ധം 10, അധ്യായം 6, ശ്ലോകം 14", "is_correct": True},
                            {"text": "സ്കന്ധം 10, അധ്യായം 6, ശ്ലോകം 1", "is_correct": False},
                            {"text": "സ്കന്ധം 10, അധ്യായം 1, ശ്ലോകം 10", "is_correct": False},
                            {"text": "സ്കന്ധം 10, അധ്യായം 3, ശ്ലോകം 25", "is_correct": False}
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

        self.stdout.write(self.style.SUCCESS(f"Successfully populated Story 16 (ID: {story.id}) across all 7 languages!"))
