import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askharekrishna_backend.settings')
django.setup()

from django.core.management.base import BaseCommand
from stories.models import StoryMainTopic, Story, StoryTranslation, StoryQuestion, StoryQuestionOption

class Command(BaseCommand):
    help = "Populate Story 7: The Transcendental Appearance of Lord Krishna at Midnight across 7 languages"

    def handle(self, *args, **options):
        topic = StoryMainTopic.objects.get(name="Krishna Pastimes")

        story_slug = "krishna-pastimes-the-transcendental-appearance-of-lord-krishna-at-midnight"
        image_path = "stories/images/transcendental_appearance_midnight.jpg"

        story, created = Story.objects.get_or_create(
            slug=story_slug,
            defaults={
                "topic": topic,
                "order": 6,
                "imagePath": image_path,
            }
        )
        if not created:
            story.topic = topic
            story.order = 6
            story.imagePath = image_path
            story.save()

        # Story content across 7 languages
        stories_data = {
            "en": {
                "mainTopic": "Krishna Pastimes",
                "subTopic": "The Transcendental Appearance of Lord Krishna at Midnight",
                "content": """### Auspicious Signs of the Lord's Descent

When the supreme hour of the Lord's appearance arrived, all planetary systems became calm, joyful, and auspicious. The constellation of Rohini was dominant, and the astrological configuration was filled with auspicious celestial influences. In the directions, everywhere on earth, in the sky, and in the celestial heavens, a divine peace descended. 

Clear stars twinkled brightly in the sky, and gentle, fragrant breezes carried the sweet aroma of various seasonal flowers. Clear water flowed gracefully in all the rivers, and serene lakes were adorned with beautiful lotus and lily flowers. The singing birds chirped melodiously in the forest trees, and peacocks danced in joy. The pious brāhmaṇas, whose sacred fires had previously been disturbed by the cruel edicts of King Kamsa, found their sacrificial fires blazing brightly of their own accord. Even within the fearful minds of the saintly persons who were terrified of Kamsa's tyrannies, an overwhelming wave of transcendental bliss arose.

In the upper planetary realms, celestial drums sounded in the sky. Kinnaras and Gandharvas sang melodious songs of praise, Siddhas and Cāraṇas offered heartfelt prayers, and Vidyādharas and celestial Apsarās danced with ecstasy. Heavenly clouds gathered softly in the sky, rumbling gently like the sweet murmuring of the ocean and showering sweet showers of flowers upon the earth.

### The Lord Appears Like the Full Moon

Then, at the stroke of midnight, in the dense darkness of the dungeon of Mathura, the Supreme Personality of Godhead, who resides in the hearts of all living beings, manifested Himself before Devaki and Vasudeva. He appeared exactly like the brilliant full moon rising majestically over the eastern horizon to dispel the gloom of the entire universe.

Vasudeva looked upon the newly born child with absolute wonder and unblinking eyes. To his great astonishment, the child was not an ordinary human infant crying helplessly. Instead, before them stood the magnificent four-armed Lord Nārāyaṇa, Vasudeva-Krishna!

### The Divine Four-Armed Form

Śrīmad-Bhāgavatam describes this breathtaking sight:

> **Śrīmad-Bhāgavatam, Canto 10, Chapter 3, Verses 9–10**
> 
> *tam adbhutaṁ bālakam ambujekṣaṇaṁ*  
> *catur-bhujaṁ śaṅkha-gadāry-udāyudham*  
> *śrīvatsa-lakṣmaṁ gala-śobhi-kaustubhaṁ*  
> *pītāmbaraṁ sāndra-payoda-saubhagam*  
> 
> *mahārha-vaiḍūrya-kirīṭa-kuṇḍala-*  
> *tviṣā pariṣvakta-sahasra-kuntalam*  
> *uddāma-kāñcy-aṅgada-kaṅkaṇādibhir*  
> *virocamānaṁ vasudeva aikṣata*  
> 
> **Translation:** Vasudeva saw that wonderful child born with lotus-like eyes, four arms, holding a conchshell, club, disc, and lotus flower, marked with the sign of Śrīvatsa on His chest, bearing the effulgent Kaustubha gem upon His neck, dressed in yellow pitāmbara silks, and possessing a transcendental bodily hue like a fresh dark monsoon cloud. The child's abundant dark curls were encircled by the effulgence of a precious jeweled helmet and earrings made of vaiḍūrya stone, and He was gorgeously decorated with a brilliant belt around His waist and radiant armlets and bangles on His arms.

The dark prison dungeon was suddenly illuminated by the blinding golden-blue effulgence emanating from the Lord's transcendental body. He stood adorned with a fresh forest flower garland (*vana-mālā*), surrounded by a sweet heavenly fragrance that filled the entire stone cell.

### Vasudeva's Transcendent Realization

Upon beholding his newborn child in this opulent, four-armed form of Lord Viṣṇu, Vasudeva was struck with profound awe and devotion. All his fear of King Kamsa vanished immediately from his heart. He realized with complete certainty that this was not a mundane child born of material nature, but the Original Supreme Personality of Godhead Himself, descended to protect the devotees and vanquish the burden of demonic rulers.

Vasudeva felt an overwhelming desire to celebrate the appearance of the Supreme Lord by donating vast quantities of cows in charity to the brāhmaṇas, as was traditional for an honorable kṣatriya king at the birth of a prince. Because he was locked inside Kamsa's iron-bound prison and had no physical possessions at hand, Vasudeva meditated deeply in his mind, giving thousands of well-decorated, milk-laden cows away in transcendental charity to the brāhmaṇas.

Overcome with reverence, Vasudeva folded his hands in humble prayer (*añjali mudrā*), fell flat upon the stone floor in prostrated obeisances, and prepared to offer his heartfelt philosophical prayers unto the Supreme Personality of Godhead.""",
                "questions": [
                    {
                        "question": "Which astrological constellation (nakshatra) was dominant at the midnight appearance of Lord Krishna?",
                        "options": [
                            {"text": "Rohini", "is_correct": True},
                            {"text": "Ashwini", "is_correct": False},
                            {"text": "Magha", "is_correct": False},
                            {"text": "Bharani", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What natural sign occurred in the sacred fires of the brahmanas when Lord Krishna appeared?",
                        "options": [
                            {"text": "The sacrificial fires blazed brightly of their own accord without effort", "is_correct": True},
                            {"text": "They were completely extinguished", "is_correct": False},
                            {"text": "They turned cold like ice", "is_correct": False},
                            {"text": "They emitted thick dark smoke", "is_correct": False}
                        ]
                    },
                    {
                        "question": "To what celestial body does the scripture compare Lord Krishna's appearance from Devaki?",
                        "options": [
                            {"text": "The full moon rising on the eastern horizon", "is_correct": True},
                            {"text": "A blazing midday summer sun", "is_correct": False},
                            {"text": "A shooting meteor", "is_correct": False},
                            {"text": "A passing lightning strike", "is_correct": False}
                        ]
                    },
                    {
                        "question": "How did Lord Krishna first manifest Himself to Vasudeva and Devaki?",
                        "options": [
                            {"text": "As the magnificent four-armed Lord Vishnu holding conch, disc, club, and lotus", "is_correct": True},
                            {"text": "As a crying two-armed helpless infant", "is_correct": False},
                            {"text": "As an invisible disembodied voice", "is_correct": False},
                            {"text": "As a blazing column of fire", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What color was Lord Krishna's transcendental pitambara garment?",
                        "options": [
                            {"text": "Golden-yellow", "is_correct": True},
                            {"text": "Deep red", "is_correct": False},
                            {"text": "Pure white", "is_correct": False},
                            {"text": "Jet black", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What sacred jewel and mark adorned the chest and neck of Lord Krishna?",
                        "options": [
                            {"text": "The Kaustubha gem and the mark of Shrivatsa", "is_correct": True},
                            {"text": "The Syamantaka jewel and ruby ring", "is_correct": False},
                            {"text": "A gold locket and diamond chain", "is_correct": False},
                            {"text": "A silver medallion and pearl crescent", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What is the complexion of Lord Krishna's transcendental body compared to?",
                        "options": [
                            {"text": "A fresh dark monsoon cloud (sandra-payoda)", "is_correct": True},
                            {"text": "A pale white snowfield", "is_correct": False},
                            {"text": "Molten gold", "is_correct": False},
                            {"text": "Crimson clay", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What happened to the dark prison cell when the Lord manifested?",
                        "options": [
                            {"text": "It was flooded with brilliant golden-blue celestial radiance and sweet fragrance", "is_correct": True},
                            {"text": "It remained pitch black and freezing cold", "is_correct": False},
                            {"text": "It collapsed under an earthquake", "is_correct": False},
                            {"text": "It filled with heavy smoke", "is_correct": False}
                        ]
                    },
                    {
                        "question": "What did Vasudeva do mentally while locked inside Kamsa's prison?",
                        "options": [
                            {"text": "He donated thousands of decorated, milk-laden cows in charity to the brahmanas", "is_correct": True},
                            {"text": "He planned a violent jailbreak with hidden weapons", "is_correct": False},
                            {"text": "He wept bitterly in despair", "is_correct": False},
                            {"text": "He demanded gold coins from King Kamsa", "is_correct": False}
                        ]
                    },
                    {
                        "question": "In which chapter of Srimad-Bhagavatam Canto 10 is Lord Krishna's transcendental birth described?",
                        "options": [
                            {"text": "Chapter 3", "is_correct": True},
                            {"text": "Chapter 1", "is_correct": False},
                            {"text": "Chapter 12", "is_correct": False},
                            {"text": "Chapter 20", "is_correct": False}
                        ]
                    }
                ]
            },
            "ta": {
                "mainTopic": "கிருஷ்ண லீலைகள்",
                "subTopic": "நள்ளிரவில் பகவான் ஸ்ரீ கிருஷ்ணரின் திவ்ய அவதாரம்",
                "content": """### பகவானின் அவதாரத்தின் மங்களகரமான அறிகுறிகள்

பகவானின் அவதார நன்னேரம் நெருங்கியபோது, அண்ட சராசரங்களின் அனைத்து கிரக நிலைகளும் அமைதியும் ஆனந்தமும் மங்களமும் நிறைந்தவையாக மாறின. ரோகிணி நட்சத்திரம் முதன்மையாக விளங்கியது. அனைத்து திசைகளிலும், பூலோகத்திலும், ஆகாயத்திலும், தேவலோகத்திலும் திவ்ய அமைதி நிலவியது.

வானில் விண்மீன்கள் பிரகாசமாக மின்னின; பருவகால மலர்களின் நறுமணத்தை ஏந்தியபடி இதமான தென்றல் வீசியது. நதிகளில் தெளிந்த நன்னீர் அமைதியாகப் பாய்ந்தது; தாமரைகளும் அல்லி மலர்களும் தடாகங்களில் மலர்ந்து மணம் பரப்பின. மரங்களில் பறவைகள் இன்னிசை பாடின; மயில்கள் மகிழ்ச்சியில் தோகைய விரித்து ஆடின. கம்சனால் தடுத்து வைக்கப்பட்டிருந்த பிராமணர்களின் யாகத் தீ, எவ்வித முயற்சியும் இன்றி தாமாகவே பிரகாசமாக கொழுந்துவிட்டு எரிந்தது. கம்சனின் கொடுமைகளால் பயந்து நடுங்கிக் கொண்டிருந்த சாதுக்களின் உள்ளங்களில் சொல்லொணாத பரமானந்த அலை எழுந்தது.

தேவலோகத்தில் துந்துபி முரசுகள் முழங்கின. கந்தர்வர்களும் கின்னரர்களும் இன்னிசை பாடினர்; சித்தர்களும் சாரணர்களும் திவ்ய ஸ்தோத்திரங்களைப் பாடினர்; வித்யாதரர்களும் அப்சரசுகளும் ஆனந்தக் கூத்தாடினர். ஆகாயத்தில் மேகங்கள் திரண்டு சமுத்திரத்தின் ரீங்காரம் போல மெல்ல முழங்கி, பூமியின் மீது சுகந்த மலர் மழையைப் பொழிந்தன.

### பூரண சந்திரனைப் போன்ற பகவானின் அவதாரம்

அப்போது, நள்ளிரவு வேளையில், மதுராவின் காரிருள் சூழ்ந்த சிறைச்சாலையில், அனைத்து ஜீவராசிகளின் இதயங்களிலும் உறையும் முழுமுதற் கடவுளான பகவான் ஸ்ரீ கிருஷ்ணர், தேவகி மற்றும் வசுதேவர் முன்னே அவதரித்தார். உலகெங்கும் சூழ்ந்திருந்த அஞ்ஞான இருளைப் போக்க, கிழக்கு திசைக் கடலில் கம்பீரமாக உதயமாகும் முழு பூரண சந்திரனைப் போல பகவான் தோன்றினார்.

வசுதேவர் தமது புதிதாகப் பிறந்த குழந்தையைக் கண்கொட்டாமல் ஆச்சரியத்துடன் பார்த்தார். தமக்கு முன்னே தோன்றிய குழந்தை எவ்வித பலமுமின்றி அழுதுகொண்டிருக்கும் சாதாரண மானிடக் குழந்தை அல்ல என்பதைக் கண்டு அவர் வியந்தார். மாறாக, நான்கு கரங்களுடன் சங்க, சக்கர, கதாயுதங்களை ஏந்திய திவ்ய நாராயணராக, வசுதேவ-கிருஷ்ணராக பகவான் காட்சியளித்தார்!

### பகவானின் நான்கு கர திவ்ய ரூபம்

ஸ்ரீமத் பாகவதம் இந்த அற்புதக் காட்சியை விவரிக்கிறது:

> **ஸ்ரீமத் பாகவதம், ஸ்கந்தம் 10, அத்தியாயம் 3, சுலோகங்கள் 9–10**
> 
> *தம் அத்புதம் பாலகம் அம்புஜேக்ஷணம்*  
> *சதுர்-புஜம் சங்க-கதார்யுதாயுதம் |*  
> *ஸ்ரீவத்ஸ-லக்ஷ்மம் கல-ஶோபி-கௌஸ்துபம்*  
> *பீதாம்பரம் ஸாந்த்ர-பயோத-ஸௌபகம் ||*  
> 
> *மஹார்ஹ-வைடூர்ய-கிரீட-குண்டல-*  
> *த்விஷா பரிஷ்வக்த-ஸஹஸ்ர-குந்தலம் |*  
> *உத்தாம-காஞ்ச்யங்கத-கங்கணாதிபிர்*  
> *விரோசமானம் வஸுதேவ ஐக்ஷத ||*  
> 
> **பொருள்:** தாமரை மலர் போன்ற கண்களுடனும், நான்கு கரங்களில் சங்கு, கதை, சக்கரம், தாமரை மலரை ஏந்தியவராகவும், மார்பில் ஸ்ரீவத்ஸ மறுவையும், கழுத்தில் பிரகாசிக்கும் கௌஸ்துப மணியையும் தாங்கியவராக வசுதேவர் அந்த அற்புதக் குழந்தையைக் கண்டார். புது கார்மேகம் போன்ற சியாமள வர்ண உடலையும், பொன்னிற பீதாம்பர ஆடைகளையும் அணிந்திருந்த அக்குழந்தையின் தலைமுடி, ரத்தின கிரீடம் மற்றும் வைடூரிய குண்டலங்களின் ஒளியால் சூழப்பட்டிருந்தது. இடுப்பில் மணி மேகலையும், கரங்களில் தோள்வளை மற்றும் வளையல்களாலும் அலங்கரிக்கப்பட்டு பிரகாசித்த அந்த திவ்ய குழந்தையை வசுதேவர் தரிசித்தார்.

பகவானின் திவ்ய திருமேனியிலிருந்து வெளிப்பட்ட தங்க-நீல நிற திவ்ய ஒளி, இருண்ட சிறைக் கொட்டடியை சுடர்விட்டுப் பிரகாசிக்கச் செய்தது. நறுமண வனமாலையோடு பகவான் காட்சியளித்தார்; சிறைச்சாலை முழுவதும் திவ்ய சுகந்த நறுமணம் நிரம்பியது.

### வசுதேவரின் திவ்ய மெய்யுணர்வு

பகவான் ஸ்ரீ விஷ்ணுவின் இந்த நான்கு கர ரூபத்தைக் கண்டவுடன் வசுதேவருக்கு கம்சனைக் குறித்த சகல பயங்களும் உடனே மறைந்தன. இக்குழந்தை பௌதிக உலகிற்குரிய சாதாரண குழந்தை அல்ல; பக்தர்களைக் காக்கவும் அசுரர்களின் பாரத்தைத் தணிக்கவும் அவதரித்த முழுமுதற் கடவுளான பகவானே இவர் என்பதை வசுதேவர் திடமாக உணர்ந்தார்.

ஒரு இளவரசன் அவதரிக்கும் நன்னாளில் சத்திரிய மன்னர்கள் பிராமணர்களுக்கு எண்ணற்ற தானங்களை வழங்குவது மரபாகும். ஆனால், கம்சனின் இரும்புச் சிறையில் அடைபட்டிருந்த வசுதேவரிடம் எந்த பௌதிகப் பொருளும் இருக்கவில்லை. எனவே, வசுதேவர் தமது உள்ளத்தில் பக்தி பூர்வமாக தியானித்து, நற்பண்புகள் கொண்ட பிராமணர்களுக்கு ஆயிரக்கணக்கான அலங்கரிக்கப்பட்ட பால்சுரக்கும் பசுக்களை மனதார தானமாக வழங்கினார்.

பகவானின் மீது கொண்ட எல்லையற்ற பக்தியால் வசுதேவர் கைகூப்பி (*அஞ்சலி முத்திரை*), தரையில் வீழ்ந்து தண்டனிட்டு வணங்கி, பகவானை துதிக்கும் திவ்ய பிரார்த்தனைகளை சமர்ப்பிக்கத் தொடங்கினார்.""",
                "questions": [
                    {
                        "question": "பகவான் ஸ்ரீ கிருஷ்ணர் நள்ளிரவில் அவதரித்தபோது நிலவிய நட்சத்திரம் எது?",
                        "options": [
                            {"text": "ரோகிணி", "is_correct": True},
                            {"text": "அஸ்வினி", "is_correct": False},
                            {"text": "மகம்", "is_correct": False},
                            {"text": "பரணி", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பகவான் அவதரித்தபோது பிராமணர்களின் யாகத் தீயில் என்ன அற்புதம் நிகழ்ந்தது?",
                        "options": [
                            {"text": "எவ்வித முயற்சியும் இன்றி தீ தாமாகவே பிரகாசமாக கொழுந்துவிட்டு எரிந்தது", "is_correct": True},
                            {"text": "தீ முற்றிலும் அணைந்தது", "is_correct": False},
                            {"text": "பனிபோல குளிர்ந்து போனது", "is_correct": False},
                            {"text": "கரிய புகையாக மாறியது", "is_correct": False}
                        ]
                    },
                    {
                        "question": "தேவகிக்கு பகவான் அவதரித்ததை சாஸ்திரம் எதனுடன் ஒப்பிடுகிறது?",
                        "options": [
                            {"text": "கிழக்கு திசையில் உதயமாகும் முழு பூரண சந்திரன்", "is_correct": True},
                            {"text": "நண்பகல் வெயில்", "is_correct": False},
                            {"text": "எரிநட்சத்திரம்", "is_correct": False},
                            {"text": "மின்னல் கீற்று", "is_correct": False}
                        ]
                    },
                    {
                        "question": "வசுதேவர் மற்றும் தேவகிக்கு பகவான் முதலில் எந்த ரூபத்தில் காட்சியளித்தார்?",
                        "options": [
                            {"text": "சங்கு, சக்கரம், கதை, தாமரை ஏந்திய நான்கு கர திவ்ய நாராயண ரூபம்", "is_correct": True},
                            {"text": "அழுதுகொண்டிருக்கும் சாதாரண இரண்டுகை குழந்தை", "is_correct": False},
                            {"text": "உருவமற்ற அசரீரி குரல்", "is_correct": False},
                            {"text": "நெருப்புப் பிழம்பு", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பகவான் ஸ்ரீ கிருஷ்ணர் அணிந்திருந்த பீதாம்பர ஆடையின் நிறம் என்ன?",
                        "options": [
                            {"text": "பொன்னிற மஞ்சள்", "is_correct": True},
                            {"text": "அடர் சிவப்பு", "is_correct": False},
                            {"text": "வெள்ளை", "is_correct": False},
                            {"text": "கருப்பு", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பகவான் ஸ்ரீ கிருஷ்ணரின் மார்பிலும் கழுத்திலும் விளங்கிய ஆபரணங்கள் யாவை?",
                        "options": [
                            {"text": "கௌஸ்துப மணி மற்றும் ஸ்ரீவத்ஸ மறு", "is_correct": True},
                            {"text": "சியமந்தக மணி", "is_correct": False},
                            {"text": "வைர மாலை", "is_correct": False},
                            {"text": "முத்து சங்கிலி", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பகவான் ஸ்ரீ கிருஷ்ணரின் திருமேனி வர்ணம் எதற்கு ஒப்பிடப்படுகிறது?",
                        "options": [
                            {"text": "மழைக்கால புது கார்மேகம்", "is_correct": True},
                            {"text": "வெண்பனி", "is_correct": False},
                            {"text": "தங்கம்", "is_correct": False},
                            {"text": "செம்மண்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பகவான் தோன்றியபோது இருண்ட சிறைச்சாலை என்னவானது?",
                        "options": [
                            {"text": "தங்க-நீல திவ்ய ஒளியாலும் திவ்ய நறுமணத்தாலும் நிரம்பியது", "is_correct": True},
                            {"text": "மேலும் இருண்டது", "is_correct": False},
                            {"text": "பூகம்பத்தால் இடிந்து விழுந்தது", "is_correct": False},
                            {"text": "கரும்புகை சூழ்ந்தது", "is_correct": False}
                        ]
                    },
                    {
                        "question": "சிறையில் இருந்த வசுதேவர் பகவானின் அவதாரத்தின்போது மனதால் என்ன தானம் செய்தார்?",
                        "options": [
                            {"text": "பிராமணர்களுக்கு ஆயிரக்கணக்கான கறவை பசுக்களை மனதால் தானம் செய்தார்", "is_correct": True},
                            {"text": "ஆயுதங்களை சேகரித்தார்", "is_correct": False},
                            {"text": "கண்ணீர் வடித்து அழுது புலம்பினார்", "is_correct": False},
                            {"text": "கம்சனிடம் பொற்காசுகளைக் கேட்டார்", "is_correct": False}
                        ]
                    },
                    {
                        "question": "பகவான் ஸ்ரீ கிருஷ்ணரின் திவ்ய அவதாரம் ஸ்ரீமத் பாகவதம் பத்தாம் ஸ்கந்தத்தில் எந்த அத்தியாயத்தில் விவரிக்கப்படுகிறது?",
                        "options": [
                            {"text": "அத்தியாயம் 3", "is_correct": True},
                            {"text": "அத்தியாயம் 1", "is_correct": False},
                            {"text": "அத்தியாயம் 10", "is_correct": False},
                            {"text": "அத்தியாயம் 15", "is_correct": False}
                        ]
                    }
                ]
            },
            "hi": {
                "mainTopic": "कृष्ण लीलाएं",
                "subTopic": "मध्यरात्रि में भगवान श्री कृष्ण का दिव्य प्राकट्य",
                "content": """### भगवान के अवतरण के मंगलमय लक्षण

जब भगवान के प्राकट्य का परम पावन समय आया, तो समस्त ग्रह-नक्षत्र शांत, आनंदित और मंगलमय हो गए। रोहिणी नक्षत्र प्रमुख था और संपूर्ण खगोलीय वातावरण अत्यंत शुभ लक्षणों से युक्त था। चारों दिशाओं में, पृथ्वी पर, आकाश में और स्वर्गलोक में एक दिव्य शांति छा गई।

आकाश में तारे अत्यंत उज्ज्वल चमक रहे थे, और ऋतुओं के पुष्पों की मधुर सुगंध को लेकर शीतल-मंद-सुगंधित वायु बह रही थी। नदियों में निर्मल जल प्रवाहित हो रहा था और सरोवरों में कमल तथा कुमुदिनी के पुष्प प्रफुल्लित होकर महक रहे थे। वनों में पक्षी मधुर गान कर रहे थे और मयूर आनंद में नृत्य कर रहे थे। पापी कंस के अत्याचारों से पूर्व में पीड़ित ब्राह्मणों की यज्ञ-अग्नि बिना किसी प्रयास के स्वतः ही प्रज्वलित हो उठी। कंस के भय से त्रस्त साधु-महात्माओं के हृदयों में भी परमानंद की तरंगें उमड़ने लगीं।

स्वर्गलोक में देव-दुंदुभियां बज उठीं। किन्नर और गंधर्व मधुर गान गाने लगे, सिद्ध और चारण स्तुतियां करने लगे तथा विद्याधर और अप्सराएं आनंदमग्न होकर नृत्य करने लगीं। आकाश में मेघ समुद्र की गंभीर ध्वनि के समान गर्जना करते हुए पृथ्वी पर पुष्पों की वर्षा करने लगे।

### पूर्णिमा के चंद्रमा के समान प्राकट्य

तभी, भाद्रपद मास की कृष्णपक्षीय अष्टमी की मध्यरात्रि के घोर अंधकार में, मथुरा के कारागार में, समस्त जीवों के हृदय में निवास करने वाले श्री भगवान्, देवकी और वसुदेव के समक्ष प्रकट हुए। जैसे पूर्व दिशा में पूर्ण चंद्रमा उदित होकर संपूर्ण जगत के अंधकार को मिटा देता है, उसी प्रकार भगवान् अवतरित हुए।

वसुदेव ने अपने नवजात शिशु को अपलक नेत्रों से विस्मयपूर्वक देखा। वह कोई साधारण रोता हुआ अबोध बालक नहीं था, अपितु उनके सम्मुख साक्षात् चतुर्भुज भगवान श्री विष्णु, वासुदेव-कृष्ण के रूप में विराजमान थे!

### भगवान का अद्भुत चतुर्भुज स्वरूप

श्रीमद्भागवतम् में इस मनोहारी दृश्य का वर्णन आता है:

> **श्रीमद्भागवतम्, स्कंध 10, अध्याय 3, श्लोक 9–10**
> 
> *तं अद्भुतं बालकम् अम्बुजेक्षणं*  
> *चतुर्भुजं शङ्खगदार्युदायुधम् ।*  
> *श्रीवत्सलक्ष्मं गलशोभिकौस्तुभं*  
> *पीताम्बरं सान्द्रपयोदसौभगम् ॥*  
> 
> *महार्हवैडूर्यकिरीटकुण्डलट्विषा*  
> *परिष्वक्तसहस्रकुन्तलम् ।*  
> *उद्दामकाञ्च्यङ्गदकङ्कणादिभिर्*  
> *विरोचमानं वसुदेव ऐक्षत ॥*  
> 
> **भावार्थ:** वसुदेव ने देखा कि वह अद्भुत बालक कमल के समान विशाल नेत्रों वाला है, उसकी चार भुजाओं में शंख, चक्र, गदा और पद्म सुशोभित हैं। उनके वक्षःस्थल पर श्रीवत्स का चिन्ह है, गले में कौस्तुभ मणि शोभा पा रही है, उन्होंने पीतांबर धारण कर रखा है और उनके शरीर की कांति नवीन श्याम मेघ के समान मनोहर है। बहुमूल्य वैडूर्यमणि-जड़ित मुकुट और कुण्डलों की प्रभा से उनके घुंघराले बाल चमक रहे हैं तथा वे करधनी, बाजूबंद और कंकणों से सुसज्जित होकर अत्यंत दीप्तिमान लग रहे हैं।

भगवान के दिव्य विग्रह से निकलती स्वर्णिम-नीलमणि आभा ने उस अंधकारमय कारागार को आलोकित कर दिया। उनके गले में वनमाला सुशोभित थी और संपूर्ण कक्ष दिव्य सुगंध से भर गया।

### वसुदेव जी की दिव्य अनुभूति

भगवान श्री विष्णु के इस दिव्य चतुर्भुज रूप को देखकर वसुदेव के मन से कंस का सारा भय तत्काल समाप्त हो गया। वे समझ गए कि यह कोई सामान्य बालक नहीं, बल्कि साक्षात् पूर्ण पुरुषोत्तम भगवान् हैं जो भक्तों की रक्षा और असुरों के भार को हरने के लिए अवतरित हुए हैं।

पुत्र के जन्म पर ब्राह्मणों को गायों का दान देना क्षत्रियों की परंपरा थी। परंतु कारागार में बंद वसुदेव के पास कोई भौतिक साधन नहीं था। अतः उन्होंने अपने मन में ही ध्यान करते हुए ब्राह्मणों को हजारों अलंकृत, दुग्धवती गौएं दान में अर्पित कर दीं।

फिर अत्यंत विनीत भाव से हाथ जोड़कर (अंजलि मुद्रा में), वसुदेव ने दंडवत प्रणाम किया और भगवान की स्तुति करने लगे।""",
                "questions": [
                    {
                        "question": "भगवान श्री कृष्ण के अवतरण के समय कौन सा नक्षत्र उदित था?",
                        "options": [
                            {"text": "रोहिणी", "is_correct": True},
                            {"text": "अश्विनी", "is_correct": False},
                            {"text": "मघा", "is_correct": False},
                            {"text": "भरणी", "is_correct": False}
                        ]
                    },
                    {
                        "question": "भगवान के प्राकट्य पर ब्राह्मणों की यज्ञ-अग्नि में क्या चमत्कार हुआ?",
                        "options": [
                            {"text": "यज्ञ-अग्नि स्वतः ही प्रज्वलित हो उठी", "is_correct": True},
                            {"text": "अग्नि बुझ गई", "is_correct": False},
                            {"text": "अग्नि ठंडी हो गई", "is_correct": False},
                            {"text": "धुआं भर गया", "is_correct": False}
                        ]
                    },
                    {
                        "question": "देवकी से भगवान के प्राकट्य की उपमा शास्त्रों में किससे दी गई है?",
                        "options": [
                            {"text": "पूर्व दिशा में उदित होते पूर्ण चंद्रमा से", "is_correct": True},
                            {"text": "दोपहर के तपते सूर्य से", "is_correct": False},
                            {"text": "टूटते तारे से", "is_correct": False},
                            {"text": "बिजली की चमक से", "is_correct": False}
                        ]
                    },
                    {
                        "question": "भगवान श्री कृष्ण वसुदेव और देवकी के सम्मुख पहले किस स्वरूप में प्रकट हुए?",
                        "options": [
                            {"text": "शंख, चक्र, गदा, पद्म धारण किए चतुर्भुज रूप में", "is_correct": True},
                            {"text": "रोते हुए असहाय द्विभुज शिशु रूप में", "is_correct": False},
                            {"text": "अदृश्य आकाशवाणी के रूप में", "is_correct": False},
                            {"text": "अग्नि स्तंभ के रूप में", "is_correct": False}
                        ]
                    },
                    {
                        "question": "भगवान श्री कृष्ण के दिव्य पीतांबर का रंग कैसा था?",
                        "options": [
                            {"text": "सुनहरा पीला", "is_correct": True},
                            {"text": "लाल", "is_correct": False},
                            {"text": "श्वेत", "is_correct": False},
                            {"text": "काला", "is_correct": False}
                        ]
                    },
                    {
                        "question": "भगवान के वक्षःस्थल और गले में कौन से आभूषण सुशोभित थे?",
                        "options": [
                            {"text": "कौस्तुभ मणि और श्रीवत्स का चिन्ह", "is_correct": True},
                            {"text": "स्यमंतक मणि", "is_correct": False},
                            {"text": "हीरों का हार", "is_correct": False},
                            {"text": "मोतियों की माला", "is_correct": False}
                        ]
                    },
                    {
                        "question": "भगवान श्री कृष्ण के अंगों की कांति की तुलना किससे की गई है?",
                        "options": [
                            {"text": "नवीन श्याम मेघ (सांद्र-पयोद)", "is_correct": True},
                            {"text": "श्वेत हिम", "is_correct": False},
                            {"text": "सोना", "is_correct": False},
                            {"text": "लाल मिट्टी", "is_correct": False}
                        ]
                    },
                    {
                        "question": "भगवान के प्रकट होते ही अंधकारमय कारागार में क्या परिवर्तन हुआ?",
                        "options": [
                            {"text": "कारागार दिव्य स्वर्णिम-नीलमणि प्रकाश और सुगंध से भर गया", "is_correct": True},
                            {"text": "वहां घोर अंधकार छा गया", "is_correct": False},
                            {"text": "भूकंप से कारागार गिर गया", "is_correct": False},
                            {"text": "वहां धुआं फैल गया", "is_correct": False}
                        ]
                    },
                    {
                        "question": "कारागार में बंद वसुदेव जी ने मन ही मन क्या दान किया?",
                        "options": [
                            {"text": "ब्राह्मणों को हजारों अलंकृत दुग्धवती गायें दान कीं", "is_correct": True},
                            {"text": "कंस से युद्ध की योजना बनाई", "is_correct": False},
                            {"text": "निराशा में विलाप किया", "is_correct": False},
                            {"text": "कंस से धन मांगा", "is_correct": False}
                        ]
                    },
                    {
                        "question": "श्रीमद्भागवतम् के दसवें स्कंध के किस अध्याय में भगवान श्री कृष्ण का प्राकट्य वर्णित है?",
                        "options": [
                            {"text": "अध्याय 3", "is_correct": True},
                            {"text": "अध्याय 1", "is_correct": False},
                            {"text": "अध्याय 7", "is_correct": False},
                            {"text": "अध्याय 10", "is_correct": False}
                        ]
                    }
                ]
            },
            "ml": {
                "mainTopic": "കൃഷ്ണ ലീലകൾ",
                "subTopic": "അർദ്ധരാത്രിയിൽ ഭഗവാൻ ശ്രീകഷ്ണന്റെ ദിവ്യമായ അവതാരം",
                "content": """### ഭഗവാന്റെ അവതാരത്തിന്റെ മംഗളകരമായ ലക്ഷണങ്ങൾ

ഭഗവാന്റെ അവതാര സമയം അടുത്തപ്പോൾ പ്രപഞ്ചത്തിലെ സർവ്വ ഗ്രഹങ്ങളും ശാന്തവും മംഗളകരവുമായിത്തീർന്നു. രോഹിണി നക്ഷത്രം ഉദിച്ചുനിന്നു. ഭൂമിയിലും ആകാശത്തിലും സ്വർഗ്ഗത്തിലും പരമമായ ശാന്തിയും ആനന്ദവും നിറഞ്ഞു.

ആകാശത്തിൽ നക്ഷത്രങ്ങൾ തിളങ്ങിവിളങ്ങി; പൂക്കളുടെ സുഗന്ധം വഹിച്ചുകൊണ്ട് തണുത്ത ഇളംകാറ്റ് വീശി. നദികളിൽ തെളിഞ്ഞ ജലം ഒഴുകി; താമരപ്പൂക്കളും ആമ്പലുകളും ജലാശയങ്ങളിൽ വിരിഞ്ഞുനിന്നു. വനങ്ങളിൽ പക്ഷികൾ മധുരമായി പാടുകയും മയിലുകൾ നൃത്തം ചെയ്യുകയും ചെയ്തു. കംസന്റെ ഉപദ്രവം കാരണം അണഞ്ഞുപോയിരുന്ന ബ്രാഹ്മണരുടെ യാഗാഗ്നികൾ യാതൊരു പ്രയത്നവുമില്ലാതെ സ്വയം ജ്വലിച്ചുയർന്നു. ഭക്തന്മാരുടെ ഹൃദയങ്ങളിൽ പറഞ്ഞറിയിക്കാനാവാത്ത ദിവ്യാനന്ദം അലയടിച്ചു.

സ്വർഗ്ഗത്തിൽ ദേവദുന്ദുഭികൾ മുഴങ്ങി. ഗന്ധർവ്വന്മാരും കിന്നരന്മാരും മനോഹരമായി പാടുകയും സിദ്ധന്മാരും ചാരണന്മാരും സ്തുതികൾ അർപ്പിക്കുകയും ചെയ്തു. ആകാശത്തിൽ മേഘങ്ങൾ സാന്ദ്രമായി ഉരുണ്ടുകൂടി പുഷ്പവൃഷ്ടി ചൊരിഞ്ഞു.

### പൂർണ്ണചന്ദ്രനെപ്പോലെ ഭഗവാന്റെ ആവിർഭാവം

അങ്ങനെ, അർദ്ധരാത്രിയിലെ കൊടും ഇരുട്ടിൽ, മഥുരയിലെ കാരാഗൃഹത്തിൽ, സർവ്വചരാചരങ്ങളുടെയും ഹൃദയങ്ങളിൽ വസിക്കുന്ന സാക്ഷാൽ ഭഗവാൻ ശ്രീകൃഷ്ണൻ ദേവകിയുടെയും വസുദേവരുടെയും മുൻപിൽ ആവിർഭവിച്ചു. അജ്ഞാനത്തിന്റെ ഇരുൾ നീക്കിക്കൊണ്ട് കിഴക്കുദിക്കുന്ന പൂർണ്ണചന്ദ്രനെപ്പോലെ ഭഗവാൻ പ്രകാശിച്ചു.

തന്റെ മുൻപിൽ നിൽക്കുന്ന ദിവ്യബാലനെ കണ്ട് വസുദേവർ വിസ്മയിച്ചുപോയി. അവൻ കരയുന്ന ഒരു സാധാരണ കുഞ്ഞായിരുന്നില്ല; മറിച്ച്, ശംഖ്, ചക്രം, ഗദ, താമര എന്നിവ ധരിച്ച സാക്ഷാൽ ചതുർബാഹുവായ ഭഗവാൻ വിഷ്ണു തന്നെയായിരുന്നു!

### ഭഗവാന്റെ ദിവ്യമായ ചതുർഭുജ രൂപം

ശ്രീമദ് ഭാഗവതം ഈ ദിവ്യദർശനത്തെ ഇപ്രകാരം വർണ്ണിക്കുന്നു:

> **ശ്രീമദ് ഭാഗവതം, സ്കന്ധം 10, അദ്ധ്യായം 3, ശ്ലോകങ്ങൾ 9–10**
> 
> *തം അദ്ഭുതം ബാലകം അമ്ബുജേക്ഷണം*  
> *ചതുർ-ഭുജം ശങ്ഖഗദാര്യുദായുധമ് |*  
> *ശ്രീവത്സലക്ഷ്മം ഗലശോഭികൗസ്തുഭം*  
> *പീതാംബരം സാന്ദ്രപയോദസൗഭഗമ് ||*  
> 
> *മഹാർഹവൈഡൂര്യകിരീടകുണ്ഡല-*  
> *ത്വിഷാ പരിഷ്വക്തസഹസ്രകുന്തലമ് |*  
> *ഉദ്ദാമകാഞ്ച്യങ്ഗദകങ്കണാദിഭിർ*  
> *വിരോചമാനം വസുദേവ ഐക്ഷത ||*  
> 
> **അർത്ഥം:** താമരയിതൾ പോലെയുള്ള കണ്ണുകളോടും, നാലു തൃക്കൈകളിൽ ശംഖ്, ചക്രം, ഗദ, പത്മം എന്നിവയോടും കൂടിയ ആ ദിവ്യബാലനെ വസുദേവർ ദർശിച്ചു. മാറിൽ ശ്രീവത്സചിഹ്നവും കഴുത്തിൽ കൗസ്തുഭമണിയും തിളങ്ങിനിന്നു. കാർമേഘവർണ്ണമുള്ള തിരുമേനിയിൽ മഞ്ഞപ്പട്ടു വസ്ത്രങ്ങൾ അണിഞ്ഞിരുന്നു. വൈഡൂര്യ രത്നങ്ങൾ പതിപ്പിച്ച കിരീടത്തിന്റെയും കുണ്ഡലങ്ങളുടെയും പ്രഭയിൽ അവിടുത്തെ ചുരുണ്ട കാർകൂന്തൽ തിളങ്ങിവിളങ്ങി.

ഭഗവാന്റെ ദിവ്യശരീരത്തിൽ നിന്നുമുയർന്ന പ്രഭാപൂരത്താൽ ആ കാരാഗൃഹം മുഴുവൻ പ്രകാശമാനമായിത്തീർന്നു. വനമാലയുടെയും ദിവ്യപുഷ്പങ്ങളുടെയും സുഗന്ധം അവിടെയെങ്ങും നിറഞ്ഞു.

### വസുദേവരുടെ ദിവ്യമായ തിരിച്ചറിവ്

ഈ ചതുർഭുജ വിഷ്ണുരൂപം കണ്ടതോടെ വസുദേവരുടെ മനസ്സിൽ നിന്നും കംസനെക്കുറിച്ചുള്ള സകല ഭയങ്ങളും അപ്രത്യക്ഷമായി. ഇത് ഒരു സാധാരണ കുഞ്ഞല്ല, മറിച്ച് ഭക്തരെ രക്ഷിക്കാൻ അവതരിച്ച സാക്ഷാൽ പരമപുരുഷനായ ഭഗവാൻ തന്നെയാണെന്ന് അദ്ദേഹം പൂർണ്ണമായി തിരിച്ചറിഞ്ഞു.

ഒരു രാജകുമാരൻ ജനിക്കുമ്പോൾ ബ്രാഹ്മണർക്ക് ദാനം നൽകുന്നത് ക്ഷത്രിയരുടെ ധർമ്മമാണ്. എന്നാൽ കാരാഗൃഹത്തിൽ ബന്ധിതനായിരുന്ന വസുദേവരുടെ പക്കൽ യാതൊന്നുമില്ലായിരുന്നു. അതിനാൽ അദ്ദേഹം മനസ്സുകൊണ്ട് ആയിരക്കണക്കിന് അലങ്കരിച്ച കറവപ്പശുക്കളെ ബ്രാഹ്മണർക്ക് സങ്കല്പത്തിൽ ദാനം ചെയ്തു.

അനന്തരം, അത്യധികം വിനയത്തോടെ കൈകൂപ്പി വസുദേവർ സാഷ്ടാംഗം പ്രണമിച്ച് ഭഗവാനെ സ്തുതിക്കുവാൻ തുടങ്ങി.""",
                "questions": [
                    {
                        "question": "ഭഗവാൻ ശ്രീകൃഷ്ണന്റെ അവതാര സമയത്ത് ഏത് നക്ഷത്രമാണ് ഉദിച്ചുനിന്നിരുന്നത്?",
                        "options": [
                            {"text": "രോഹിണി", "is_correct": True},
                            {"text": "അശ്വതി", "is_correct": False},
                            {"text": "മകം", "is_correct": False},
                            {"text": "ഭരണി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഭഗവാൻ അവതരിച്ചപ്പോൾ ബ്രാഹ്മണരുടെ യാഗാഗ്നിയിൽ എന്തു സംഭവിച്ചു?",
                        "options": [
                            {"text": "യാഗാഗ്നി യാതൊരു പ്രയത്നവുമില്ലാതെ തനിയെ ജ്വലിച്ചുയർന്നു", "is_correct": True},
                            {"text": "തീ പൂർണ്ണമായി അണഞ്ഞുപോയി", "is_correct": False},
                            {"text": "മഞ്ഞുപോലെ തണുത്തുപോയി", "is_correct": False},
                            {"text": "പുക നിറഞ്ഞു", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ദേവകിയിൽ നിന്നുള്ള ഭഗവാന്റെ അവതാരത്തെ ശാസ്ത്രങ്ങളിൽ എന്തിനോടാണ് ഉപമിച്ചിരിക്കുന്നത്?",
                        "options": [
                            {"text": "കിഴക്കുദിക്കുന്ന പൂർണ്ണചന്ദ്രനോട്", "is_correct": True},
                            {"text": "ഉച്ചസൂര്യനോട്", "is_correct": False},
                            {"text": "കൊള്ളിമീനിനോട്", "is_correct": False},
                            {"text": "മിന്നലിനോട്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഭഗവാൻ ആദ്യം ഏതു രൂപത്തിലാണ് മാതാപിതാക്കളുടെ മുന്നിൽ പ്രത്യക്ഷനായത്?",
                        "options": [
                            {"text": "ശംഖ്, ചക്രം, ഗദ, താമര ധരിച്ച ചതുർഭുജ വിഷ്ണുരൂപത്തിൽ", "is_correct": True},
                            {"text": "കരയുന്ന സാധാരണ ശിശുരൂപത്തിൽ", "is_correct": False},
                            {"text": "അശരീരി ശബ്ദമായി", "is_correct": False},
                            {"text": "അഗ്നിസ്തംഭമായി", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഭഗവാന്റെ പീതാംബര വസ്ത്രത്തിന്റെ നിറം എന്തായിരുന്നു?",
                        "options": [
                            {"text": "സ്വർണ്ണമഞ്ഞ", "is_correct": True},
                            {"text": "ചുവപ്പ്", "is_correct": False},
                            {"text": "വെള്ള", "is_correct": False},
                            {"text": "കറുപ്പ്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഭഗവാന്റെ മാറിലും കഴുത്തിലും ശോഭിച്ചിരുന്ന ചിഹ്നങ്ങളും ആഭരണങ്ങളും ഏവ?",
                        "options": [
                            {"text": "കൗസ്തുഭമണിയും ശ്രീവത്സചിഹ്നവും", "is_correct": True},
                            {"text": "ശ്യമന്തക രത്നം", "is_correct": False},
                            {"text": "വൈരമാല", "is_correct": False},
                            {"text": "മുത്തുമാല", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഭഗവാന്റെ തിരുമേനിയുടെ വർണ്ണം എന്തിനോടാണ് ഉപമിച്ചിരിക്കുന്നത്?",
                        "options": [
                            {"text": "പുതിയ മഴക്കാറിനോട് (സാന്ദ്ര-പയോദം)", "is_correct": True},
                            {"text": "വെൺമഞ്ഞിനോട്", "is_correct": False},
                            {"text": "സ്വർണ്ണത്തോട്", "is_correct": False},
                            {"text": "ചെമ്മണ്ണിനോട്", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ഭഗവാൻ പ്രത്യക്ഷനായപ്പോൾ ഇരുണ്ട കാരാഗൃഹത്തിന് എന്തു സംഭവിച്ചു?",
                        "options": [
                            {"text": "ദിവ്യപ്രകാശത്താലും സുഗന്ധത്താലും നിറഞ്ഞു", "is_correct": True},
                            {"text": "കൂടുതൽ ഇരുണ്ടുപോയി", "is_correct": False},
                            {"text": "ഭൂകമ്പത്തിൽ തകർന്നു", "is_correct": False},
                            {"text": "പുക നിറഞ്ഞു", "is_correct": False}
                        ]
                    },
                    {
                        "question": "കാരാഗൃഹത്തിൽ വച്ച് വസുദേവർ മനസ്സുകൊണ്ട് എന്തു ദാനം ചെയ്തു?",
                        "options": [
                            {"text": "ആയിരക്കണക്കിന് കറവപ്പശുക്കളെ ബ്രാഹ്മണർക്ക് സങ്കല്പത്തിൽ ദാനം ചെയ്തു", "is_correct": True},
                            {"text": "ആയുധങ്ങൾ ശേഖരിച്ചു", "is_correct": False},
                            {"text": "കരഞ്ഞു വിലപിച്ചു", "is_correct": False},
                            {"text": "കംസനോട് ധനം ചോദിച്ചു", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ശ്രീമദ് ഭാഗവതം പത്താം സ്കന്ധത്തിലെ ഏത് അദ്ധ്യായത്തിലാണ് ഭഗവാന്റെ ജനനം വിവരിച്ചിരിക്കുന്നത്?",
                        "options": [
                            {"text": "അദ്ധ്യായം 3", "is_correct": True},
                            {"text": "അദ്ധ്യായം 1", "is_correct": False},
                            {"text": "അദ്ധ്യായം 6", "is_correct": False},
                            {"text": "അദ്ധ്യായം 11", "is_correct": False}
                        ]
                    }
                ]
            },
            "bn": {
                "mainTopic": "কৃষ্ণ লীলা",
                "subTopic": "অর্ধরাত্রে ভগবান শ্রীকৃষ্ণের দিব্য আবির্ভাব",
                "content": """### ভগবানের আবির্ভাবের পরম মঙ্গলময় লক্ষণ

ভগবানের আবির্ভাবের পরম পবিত্র লগ্ন যখন সমুপস্থিত হলো, তখন নিখিল ব্রহ্মাণ্ডের সকল গ্রহ-নক্ষত্র শান্ত, প্রসন্ন ও পরম মঙ্গলময় হয়ে উঠল। রোহিণী নক্ষত্র উদিত ছিল এবং সমস্ত জ্যোতির্বলয় কল্যাণকর প্রভাবে পূর্ণ ছিল। চতুর্দিকে, ভূলোকে, অন্তরীক্ষে এবং দেবলোকে দিব্য শান্তি নেমে এলো।

আকাশে তারকারাজি উজ্জ্বলভাবে জ্বলতে লাগল; ঋতুকালীন পুষ্পের সুবাস বহন করে শীতল-মন্দ-সুগন্ধি সমীরণ বইতে শুরু করল। নদীসমূহে নির্মল জলধারা প্রবাহিত হতে লাগল এবং সরোবরে প্রস্ফুটিত পদ্ম ও শালুক শোভা পেতে লাগল। বনে বনে পক্ষীরা সুমধুর কলতান করতে লাগল এবং ময়ূরেরা পরমানন্দে নৃত্য করতে লাগল। পূর্বে কংসের অত্যাচারে নিভে যাওয়া ব্রাহ্মণগণের যজ্ঞাগ্নি কোনো প্রকার চেষ্টা ব্যতিরেকেই স্বয়ং প্রজ্বলিত হয়ে উঠল। কংসের ভয়ে সন্ত্রস্ত সাধু-মহাত্মাদের হৃদয়ে এক অভূতপূর্ব আনন্দের হিল্লোল বয়ে গেল।

স্বর্গলোকে দেবদুন্দুভি বেজে উঠল। কিন্নর ও গন্ধর্বগণ মধুর গান গাইতে লাগলেন, সিদ্ধ ও চারণগণ স্তব নিবেদন করতে লাগলেন এবং বিদ্যাধর ও অপ্সরাগণ আনন্দে নৃত্য করতে লাগলেন। আকাশে মেঘমালা সমুদ্রের গম্ভীরা ধ্বনির ন্যায় গর্জন করে পুষ্পবৃষ্টি বর্ষণ করতে লাগল।

### পূর্ণচন্দ্রের ন্যায় ভগবানের আবির্ভাব

তখন ভাদ্রমাসের কৃষ্ণাষ্টমীর নিশীথ অন্ধকারে, মথুরার নিভৃত কারাগারে, সর্বভূতের অন্তর্যামী পূর্ণ পুরুষোত্তম শ্রীভগবান দেবকী ও বসুদেবের সম্মুখে আবির্ভূত হলেন। যেমন পূর্ব দিগন্তে পূর্ণচন্দ্র উদিত হয়ে জগতের অন্ধকার দূরীভূত করে, তদ্রূপ ভগবান আবির্ভূত হলেন।

বসুদেব অপলক দৃষ্টিতে বিস্ময়ে সেই নবজাত শিশুর দিকে তাকিয়ে রইলেন। তিনি দেখলেন, এ কোনো ক্রন্দনরত সাধারণ মানবশিশু নয়; বরং তাঁর সম্মুখে চতুর্ভুজ শঙ্খ-চক্র-গদা-পদ্মধারী সাক্ষাৎ পরমেশ্বর ভগবান নারায়ণ, বাসুদেব-কৃষ্ণরূপে দাঁড়িয়ে আছেন!

### ভগবানের অপ্রাকৃত চতুর্ভুজ রূপ

শ্রীমদ্ভাগবতে এই পরম অপ্রাকৃত রূপের অপূর্ব বর্ণনা রয়েছে:

> **শ্রীমদ্ভাগবত, স্কন্ধ ১০, অধ্যায় ৩, শ্লোক ৯–১০**
> 
> *তং অদ্ভুতং বালকং অম্বুজেক্ষণং*  
> *চতুর্ভুজং শঙ্খগদার্যুদাযুধম্ ।*  
> *শ্রীবৎসলক্ষ্মং গলশোভিকৌস্তুভং*  
> *পীতাম্বরং সান্দ্রপয়োদসৌভগম্ ॥*  
> 
> *মহার্হবৈডূর্যকিরীটকুন্ডল-*  
> *ত্বিষা পরিষ্বক্তসহস্রকুন্তলম্ ।*  
> *উদ্দামাকান্যঙ্গদকঙ্কণাদিভির্*  
> *বিরোচমানং বসুদেব ঐক্ষত ॥*  
> 
> **অনুবাদ:** বসুদেব দেখলেন যে সেই অদ্ভুত বালক পদ্মের ন্যায় বিশাল নয়নযুক্ত, চতুর্ভুজ, হস্তে শঙ্খ, চক্র, গদা ও পদ্ম ধারণ করে আছেন। বক্ষে শ্রীবৎস চিহ্ন, কণ্ঠে উজ্জ্বল কৌস্তুভ মণি, পরিধানে পীতাম্বর এবং গাত্রবর্ণ নবীন সজল মেঘের ন্যায় মনোহর। বহুমূল্য বৈদূর্যমণি-খচিত মুকুট ও কুণ্ডলের দ্যুতিতে তাঁর কুঞ্চিত অলকদাম শোভা পাচ্ছে এবং তিনি কটিভূষণ ও বলয়াদির দ্বারা পরম দীপ্তিমান হয়ে বিরাজ করছেন।

ভগবানের শ্রীঅঙ্গ হতে বিচ্ছুরিত স্বর্ণ-নীলিম প্রভায় সেই অন্ধকার কারাগার দিব্য আলোকে উদ্ভাসিত হয়ে উঠল। তাঁর বক্ষে সুগন্ধি বনমালা শোভা পাচ্ছিল এবং কারাগৃহ পরম অপ্রাকৃত সুবাসে ভরে উঠল।

### বসুদেবের দিব্য উপলব্ধি

ভগবান শ্রীবিষ্ণুর এই চতুর্ভুজ রূপ প্রত্যক্ষ করে বসুদেবের মন থেকে কংসের সকল ভয় মুহূর্তে অপসৃত হলো। তিনি নিশ্চিতভাবে উপলব্ধি করলেন যে, ইনি কোনো প্রাকৃত শিশু নন, স্বয়ং পরম পুরুষোত্তম ভগবান, যিনি ভক্তদের রক্ষা করতে এবং অসুরদের বিনাশ করতে অবতীর্ণ হয়েছেন।

রাজকুমারের জন্মে ব্রাহ্মণদের গোদান করা ক্ষত্রিয় রাজাদের কর্তব্য। কিন্তু কারাগারে বন্দী বসুদেবের নিকটে কোনো পার্থিব সম্পদ ছিল না। তাই তিনি মনে মনেই ব্রাহ্মণদের উদ্দেশ্যে সহস্র সহস্র অলঙ্কৃত পয়স্বিনী গাভী দান করলেন।

অতঃপর কৃতাঞ্জলিপুটে পরম ভক্তিভরে ভূমিতে সাষ্টাঙ্গ প্রণাম করে বসুদেব ভগবানের স্তুতি করতে শুরু করলেন।""",
                "questions": [
                    {
                        "question": "ভগবান শ্রীকৃষ্ণের আবির্ভাবের সময় কোন নক্ষত্র উদিত ছিল?",
                        "options": [
                            {"text": "রোহিণী", "is_correct": True},
                            {"text": "অশ্বিনী", "is_correct": False},
                            {"text": "মঘা", "is_correct": False},
                            {"text": "ভরণী", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ভগবানের আবির্ভাবে ব্রাহ্মণদের যজ্ঞাগ্নিতে কি অলৌকিক ঘটনা ঘটেছিল?",
                        "options": [
                            {"text": "যজ্ঞাগ্নি বিনা চেষ্টায় স্বয়ং প্রজ্বলিত হয়ে উঠেছিল", "is_correct": True},
                            {"text": "অগ্নি নিভে গিয়েছিল", "is_correct": False},
                            {"text": "বরফের মত ঠাণ্ডা হয়ে গিয়েছিল", "is_correct": False},
                            {"text": "ধোঁয়ায় ভরে গিয়েছিল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "শাস্ত্রে দেবকীর উদরে ভগবানের আবির্ভাবকে কার সাথে তুলনা করা হয়েছে?",
                        "options": [
                            {"text": "পূর্ব দিগন্তে উদিত পূর্ণচন্দ্রের সাথে", "is_correct": True},
                            {"text": "মধ্যাহ্নের প্রখর সূর্যের সাথে", "is_correct": False},
                            {"text": "উল্কাপাতের সাথে", "is_correct": False},
                            {"text": "বিদ্যুৎ চমকের সাথে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ভগবান শ্রীকৃষ্ণ প্রথমে মাতা-পিতার সম্মুখে কোন রূপে আবির্ভূত হন?",
                        "options": [
                            {"text": "শঙ্খ-চক্র-গদা-পদ্মধারী চতুর্ভুজ বিষ্ণুরূপে", "is_correct": True},
                            {"text": "ক্রন্দনরত অসহায় দ্বিভুজ শিশুরূপে", "is_correct": False},
                            {"text": "অশরীরী দৈববাণীরূপে", "is_correct": False},
                            {"text": "অগ্নিশিখারূপে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ভগবান শ্রীকৃষ্ণের পীতাম্বর বস্ত্রের বর্ণ কেমন ছিল?",
                        "options": [
                            {"text": "স্বর্ণালী হলুদ", "is_correct": True},
                            {"text": "লাল", "is_correct": False},
                            {"text": "সাদা", "is_correct": False},
                            {"text": "কালো", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ভগবানের বক্ষে ও কণ্ঠে কোন চিহ্ন ও রত্ন শোভা পাচ্ছিল?",
                        "options": [
                            {"text": "শ্রীবৎস চিহ্ন ও কৌস্তুভ মণি", "is_correct": True},
                            {"text": "স্যমন্তক মণি", "is_correct": False},
                            {"text": "হীরার মালা", "is_correct": False},
                            {"text": "মুক্তার হার", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ভগবানের অপ্রাকৃত গাত্রবর্ণ কিসের সাথে তুলনীয়?",
                        "options": [
                            {"text": "নবীন সজল শ্যামল মেঘের সাথে", "is_correct": True},
                            {"text": "শ্বেত তুষারের সাথে", "is_correct": False},
                            {"text": "স্বর্ণের সাথে", "is_correct": False},
                            {"text": "লাল মাটির সাথে", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ভগবান আবির্ভূত হলে অন্ধকার কারাগৃহে কি পরিবর্তন ঘটেছিল?",
                        "options": [
                            {"text": "কারাগার দিব্য স্বর্ণ-নীলিম আলো এবং মনোহর সুবাসে ভরে উঠেছিল", "is_correct": True},
                            {"text": "আরও অন্ধকার হয়ে গিয়েছিল", "is_correct": False},
                            {"text": "ভূমিকম্পে ভেঙে পড়েছিল", "is_correct": False},
                            {"text": "ধোঁয়ায় ভরে গিয়েছিল", "is_correct": False}
                        ]
                    },
                    {
                        "question": "কারাগারে বন্দী বসুদেব মনে মনে কি দান করেছিলেন?",
                        "options": [
                            {"text": "ব্রাহ্মণদের উদ্দেশ্যে সহস্র সহস্র পয়স্বিনী গাভী দান করেছিলেন", "is_correct": True},
                            {"text": "অস্ত্র সংগ্রহ করেছিলেন", "is_correct": False},
                            {"text": "হতাশায় কেঁদেছিলেন", "is_correct": False},
                            {"text": "কংসের কাছে ধন প্রার্থনা করেছিলেন", "is_correct": False}
                        ]
                    },
                    {
                        "question": "শ্রীমদ্ভাগবতের দশম স্কন্ধের কোন অধ্যায়ে শ্রীকৃষ্ণের আবির্ভাব বর্ণিত হয়েছে?",
                        "options": [
                            {"text": "অধ্যায় ৩", "is_correct": True},
                            {"text": "অধ্যায় ১", "is_correct": False},
                            {"text": "অধ্যায় ৭", "is_correct": False},
                            {"text": "অধ্যায় ১২", "is_correct": False}
                        ]
                    }
                ]
            },
            "te": {
                "mainTopic": "కృష్ణ లీలలు",
                "subTopic": "అర్ధరాత్రి వేళ భగవాన్ శ్రీకృష్ణుని దివ్య ఆవిర్భావం",
                "content": """### భగవంతుని ఆవిర్భావ సమయమున శుభ శకునాలు

భగవంతుని అవతార సమయం సమీపించినప్పుడు, సకల లోకాలలోని గ్రహాలన్నీ శాంతించి శుభప్రదంగా మారాయి. రోహిణి నక్షత్రం ఆకాశంలో శోభాయమానంగా వెలిగింది. భూమిపై, ఆకాశంలో, స్వర్గంలో దివ్యమైన శాంతి మరియు ఆనందం నెలకొన్నాయి.

ఆకాశంలో నక్షత్రాలు దేదీప్యమానంగా మెరిశాయి; ఋతువుల పుష్పాల పరిమళాన్ని మోసుకొస్తూ చల్లని మందమారుతం వీచింది. నదులలో నిర్మల జలాలు ప్రవహించాయి; సరస్సులలో పద్మాలు వికసించాయి. వనాలలో పక్షులు మధురంగా గానం చేశాయి, నెమళ్ళు ఆనందంతో నాట్యమాడాయి. కంసుని ఆగడాల వల్ల ఆగిపోయిన బ్రాహ్మణుల యజ్ఞాగ్నులు ఎటువంటి ప్రయత్నం లేకుండానే స్వయంగా ప్రజ్వరిల్లాయి. భక్తుల హృదయాలలో వర్ణనాతీతమైన పరమానందం వెల్లివిరిసింది.

స్వర్గలోకంలో దేవదుందుభులు మోగాయి. గంధర్వులు, కిన్నరులు మధురంగా గానం చేశారు; సిద్ధులు, చారణులు స్తుతులు సమర్పించారు. ఆకాశంలో మేఘాలు సాంద్రంగా కమ్ముకొని సుగంధ పుష్పవృష్టిని కురిపించాయి.

### పూర్ణచంద్రుని వలె భగవానుని ఆవిర్భావం

అప్పుడు, అర్ధరాత్రి వేళ, మథుర చెరసాలలోని గాఢాంధకారంలో, సర్వభూతాంతర్యామి అయిన భగవాన్ శ్రీకృష్ణుడు దేవకీ వసుదేవుల ఎదుట ప్రత్యక్షమయ్యాడు. తూర్పు దిక్కున పూర్ణచంద్రుడు ఉదయించి లోకంలోని చీకట్లను పారద్రోలినట్లు భగవంతుడు ఆవిర్భవించాడు.

వసుదేవుడు తన ముద్దుల బిడ్డను ఆశ్చర్యంతో చూశాడు. ఆయన ఎదుట ఉన్నది ఏడ్చే సాధారణ శిశువు కాదు; సాక్షాత్తు శంఖ, చక్ర, గదా, పద్మాలను ధరించిన చతుర్భుజ విష్ణుమూర్తి, వాసుదేవ-కృష్ణుడు!

### భగవంతుని అద్భుత చతుర్భుజ రూపం

శ్రీమద్భాగవతంలో ఈ దివ్య రూపం ఇలా వర్ణించబడింది:

> **శ్రీమద్భాగవతం, స్కంధం 10, అధ్యాయం 3, శ్లోకాలు 9–10**
> 
> *తం అద్భుతం బాలకం అంబుజేక్షణం*  
> *చతుర్భుజం శంఖగదార్యుదాయుధమ్ |*  
> *శ్రీవత్సలక్ష్మం గలశోభికౌస్తుభం*  
> *పీతాంబరం సాంద్రపయోదసౌభగమ్ ||*  
> 
> *మహార్హవైడూర్యకిరీటకుండల-*  
> *త్విషా పరిష్వక్తసహస్రకుంతలమ్ |*  
> *ఉద్దామకాంచ్యంగదకంకణాదిభిర్*  
> *విరోచమానం వసుదేవ ఐక్షత ||*  
> 
> **తాత్పర్యం:** కమలాల వంటి నేత్రాలు, నాలుగు బాహువులలో శంఖం, చక్రం, గద, పద్మాలను ధరించి, వక్షస్థలమున శ్రీవత్స చిహ్నము, కంఠమున కౌస్తుభమణి మెరుస్తుండగా, పీతాంబరమును ధరించి, వర్షాకాలపు నీలిమేఘ ఛాయతో శోభిల్లుతున్న ఆ దివ్య బాలుడిని వసుదేవుడు దర్శించాడు. వైడూర్య రత్నాలు పొదిగిన కిరీటం, కుండలాల కాంతితో ఆయన ముంగురులు ప్రకాశిస్తున్నాయి.

ఆ చీకటి చెరసాల భగవంతుని దివ్య శరీర కాంతితో ప్రకాశవంతమైంది. పరిమళభరితమైన వనమాలతో అలరారిన భగవంతుని దివ్య సుగంధం ఆ గది అంతటా నిండిపోయింది.

### వసుదేవుని దివ్య అనుభూతి

ఈ చతుర్భుజ విష్ణు రూపాన్ని చూడగానే వసుదేవుని మనసులోని కంసుని భయమంతా పటాపంచలైంది. ఈయన సాధారణ బాలుడు కాదని, భక్తులను రక్షించడానికి అవతరించిన సాక్షాత్ పూర్ణ పురుషోత్తముడేనని ఆయన గ్రహించాడు.

రాజకుమారుడు జన్మించినప్పుడు గోదానం చేయడం క్షత్రియ ధర్మం. కానీ బందీగా ఉన్న వసుదేవుని వద్ద ఏమీ లేదు. కావున ఆయన తన మనస్సులోనే వేలాది అలంకరించిన పాడి ఆవులను బ్రాహ్మణులకు దానం చేశాడు.

అనంతరం చేతులు జోడించి (అంజలి ముద్రతో) సాష్టాంగ నమస్కారాలు ఆచరించి, భగవంతుని స్తుతించడం ప్రారంభించాడు.""",
                "questions": [
                    {
                        "question": "భగవాన్ శ్రీకృష్ణుడు జన్మించినప్పుడు ఏ నక్షత్రం ఉదయించింది?",
                        "options": [
                            {"text": "రోహిణి", "is_correct": True},
                            {"text": "అశ్విని", "is_correct": False},
                            {"text": "మఖ", "is_correct": False},
                            {"text": "భరణి", "is_correct": False}
                        ]
                    },
                    {
                        "question": "భగవంతుడు ఆవిర్భవించినప్పుడు బ్రాహ్మణుల యజ్ఞాగ్నులలో జరిగిన అద్భుతం ఏమిటి?",
                        "options": [
                            {"text": "యజ్ఞాగ్నులు స్వయంగా ప్రజ్వరిల్లాయి", "is_correct": True},
                            {"text": "అగ్ని ఆరిపోయింది", "is_correct": False},
                            {"text": "మంచులా చల్లబడింది", "is_correct": False},
                            {"text": "పొగ నిండిపోయింది", "is_correct": False}
                        ]
                    },
                    {
                        "question": "శాస్త్రాలలో శ్రీకృష్ణుని ఆవిర్భావాన్ని దేనితో పోల్చారు?",
                        "options": [
                            {"text": "తూర్పున ఉదయించే పూర్ణచంద్రునితో", "is_correct": True},
                            {"text": "మధ్యాహ్న సూర్యునితో", "is_correct": False},
                            {"text": "తోకచుక్కతో", "is_correct": False},
                            {"text": "మెరుపుతో", "is_correct": False}
                        ]
                    },
                    {
                        "question": "శ్రీకృష్ణుడు మొదట తల్లిదండ్రుల ఎదుట ఏ రూపంలో ప్రత్యక్షమయ్యాడు?",
                        "options": [
                            {"text": "శంఖ, చక్ర, గదా, పద్మాలను ధరించిన చతుర్భుజ రూపంలో", "is_correct": True},
                            {"text": "సాధారణ ఏడ్చే శిశువుగా", "is_correct": False},
                            {"text": "ఆకాశవాణిగా", "is_correct": False},
                            {"text": "అగ్ని స్తంభంగా", "is_correct": False}
                        ]
                    },
                    {
                        "question": "శ్రీకృష్ణుని పీతాంబర వస్త్రం ఏ రంగులో ఉంది?",
                        "options": [
                            {"text": "బంగారు పసుపు", "is_correct": True},
                            {"text": "ఎరుపు", "is_correct": False},
                            {"text": "తెలుపు", "is_correct": False},
                            {"text": "నలుపు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "భగవంతుని వక్షస్థలంలో మరియు కంఠంలో వెలిగిన ఆభరణాలు ఏవి?",
                        "options": [
                            {"text": "శ్రీవత్స చిహ్నం మరియు కౌస్తుభమణి", "is_correct": True},
                            {"text": "శ్యమంతకమణి", "is_correct": False},
                            {"text": "వజ్రాల హారం", "is_correct": False},
                            {"text": "ముత్యాల దండ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "భగవానుని శరీర వర్ణం దేనితో పోల్చబడింది?",
                        "options": [
                            {"text": "వర్షాకాలపు నీలిమేఘంతో (సాంద్ర-పయోదం)", "is_correct": True},
                            {"text": "మంచుతో", "is_correct": False},
                            {"text": "బంగారంతో", "is_correct": False},
                            {"text": "ఎర్రమట్టితో", "is_correct": False}
                        ]
                    },
                    {
                        "question": "భగవంతుడు ప్రత్యక్షమైనప్పుడు చీకటి చెరసాలలో ఏమి జరిగింది?",
                        "options": [
                            {"text": "చెరసాల అంతా దివ్యకాంతి మరియు సుగంధంతో నిండిపోయింది", "is_correct": True},
                            {"text": "మరింత చీకటైంది", "is_correct": False},
                            {"text": "భూకంపంతో కూలిపోయింది", "is_correct": False},
                            {"text": "పొగ నిండింది", "is_correct": False}
                        ]
                    },
                    {
                        "question": "చెరసాలలో ఉన్న వసుదేవుడు మనస్సులో ఏమి దానం చేశాడు?",
                        "options": [
                            {"text": "వేలాది పాడి ఆవులను బ్రాహ్మణులకు దానం చేశాడు", "is_correct": True},
                            {"text": "ఆయుధాలు సేకరించాడు", "is_correct": False},
                            {"text": "విలపించాడు", "is_correct": False},
                            {"text": "కంసుడిని ధనం కోరాడు", "is_correct": False}
                        ]
                    },
                    {
                        "question": "శ్రీమద్భాగవతము పదవ స్కంధంలో ఏ అధ్యాయంలో కృష్ణుని జన్మ వర్ణించబడింది?",
                        "options": [
                            {"text": "అధ్యాయం 3", "is_correct": True},
                            {"text": "అధ్యాయం 1", "is_correct": False},
                            {"text": "అధ్యాయం 5", "is_correct": False},
                            {"text": "అధ్యాయం 10", "is_correct": False}
                        ]
                    }
                ]
            },
            "kn": {
                "mainTopic": "ಕೃಷ್ಣ ಲೀಲೆಗಳು",
                "subTopic": "ಮಧ್ಯರಾತ್ರಿಯಲ್ಲಿ ಭಗವಾನ್ ಶ್ರೀಕೃಷ್ಣನ ದಿವ್ಯ ಆವಿರ್ಭಾವ",
                "content": """### ಭಗವಂತನ ಆವಿರ್ಭಾವದ ಮಂಗಳಕರ ಲಕ್ಷಣಗಳು

ಭಗವಂತನ ಆವಿರ್ಭಾವದ ಪರಮ ಪವಿತ್ರ ಸಮಯ ಬಂದಾಗ, ಸಮಸ್ತ ವಿಶ್ವದ ಗ್ರಹ ನಕ್ಷತ್ರಗಳು ಶಾಂತ ಮತ್ತು ಮಂಗಳಮಯವಾದವು. ರೋಹಿಣಿ ನಕ್ಷತ್ರವು ಪ್ರಕಾಶಮಾನವಾಗಿ ಬೆಳಗಿತು. ಭೂಮಿ, ಆಕಾಶ ಮತ್ತು ದೇವಲೋಕಗಳಲ್ಲಿ ದಿವ್ಯ ಶಾಂತಿ ನೆಲೆಸಿತು.

ಆಕಾಶದಲ್ಲಿ ನಕ್ಷತ್ರಗಳು ಹೊಳೆಯುತ್ತಿದ್ದವು; ಋತುಮಾನದ ಹೂವುಗಳ ಸುವಾಸನೆಯನ್ನು ಹೊತ್ತು ತಂಪಾದ ಮಂದಮಾರುತವು ಬೀಸಿತು. ನದಿಗಳಲ್ಲಿ ನಿರ್ಮಲವಾದ ನೀರು ಹರಿಯಿತು; ಸರೋವರಗಳಲ್ಲಿ ಕಮಲಗಳು ಅರಳಿದವು. ಕಾಡುಗಳಲ್ಲಿ ಪಕ್ಷಿಗಳು ಮಧುರವಾಗಿ ಹಾಡಿದವು, ನವಿಲುಗಳು ಆನಂದದಿಂದ ನರ್ತಿಸಿದವು. ಕಂಸನ ದೌರ್ಜನ್ಯದಿಂದ ನಂದಿಹೋಗಿದ್ದ ಬ್ರಾಹ್ಮಣರ ಯಜ್ಞಾಗ್ನಿಗಳು ತಾವಾಗಿಯೇ ಪ್ರಜ್ವಲಿಸಿದವು. ಭಕ್ತರ ಹೃದಯಗಳಲ್ಲಿ ಅಪಾರವಾದ ಆನಂದದ ಅಲೆಗಳು ಮೂಡಿದವು.

ದೇವಲೋಕದಲ್ಲಿ ದೇವದುಂದುಭಿಗಳು ಮೊಳಗಿದವು. ಗಂಧರ್ವರು, ಕಿನ್ನರರು ಹಾಡಿದರು; ಸಿದ್ಧರು, ಚಾರಣರು ಸ್ತುತಿಸಿದರು. ಆಕಾಶದಲ್ಲಿ ಮೇಘಗಳು ಗಂಭೀರವಾಗಿ ಗರ್ಜಿಸುತ್ತಾ ಹೂಮಳೆಯನ್ನು ಸುರಿಸಿದವು.

### ಪೂರ್ಣಚಂದ್ರನಂತೆ ಭಗವಂತನ ಆಗಮನ

ಆಗ, ಮಧ್ಯರಾತ್ರಿಯ ಕತ್ತಲೆಯಲ್ಲಿ, ಮಥುರೆಯ ಸೆರೆಮನೆಯಲ್ಲಿ, ಸರ್ವಭೂತಾಂತರ್ಯಾಮಿಯಾದ ಭಗವಾನ್ ಶ್ರೀಕೃಷ್ಣನು ದೇವಕಿ ಮತ್ತು ವಸುದೇವರ ಮುಂದೆ ಆವಿರ್ಭವಿಸಿದನು. ಪೂರ್ವದಿಕ್ಕಿನಲ್ಲಿ ಪೂರ್ಣಚಂದ್ರನು ಉದಯಿಸಿ ಜಗತ್ತಿನ ಕತ್ತಲೆಯನ್ನು ನೀಗಿಸುವಂತೆ ಭಗವಂತನು ಪ್ರಕಟನಾದನು.

ವಸುದೇವರು ತಮ್ಮ ನವಜಾತ ಶಿಶುವನ್ನು ವಿಸ್ಮಯದಿಂದ ನೋಡಿದರು. ಆತನು ಅಳುವ ಸಾಮಾನ್ಯ ಮಗುವಾಗಿರಲಿಲ್ಲ; ಶಂಖ, ಚಕ್ರ, ಗದಾ, ಪದ್ಮಗಳನ್ನು ಧರಿಸಿದ ಸಾಕ್ಷಾತ್ ಚತುರ್ಭುಜ ವಿಷ್ಣುಸ್ವರೂಪಿಯಾಗಿದ್ದನು!

### ಭಗವಂತನ ದಿವ್ಯ ಚತುರ್ಭುಜ ರೂಪ

ಶ್ರೀಮದ್ಭಾಗವತದಲ್ಲಿ ಈ ಅದ್ಭುತ ರೂಪವನ್ನು ಹೀಗೆ ವರ್ಣಿಸಲಾಗಿದೆ:

> **ಶ್ರೀಮದ್ಭಾಗವತ, ಸ್ಕಂಧ 10, ಅಧ್ಯಾಯ 3, ಶ್ಲೋಕಗಳು 9–10**
> 
> *ತಂ ಅದ್ಭುತಂ ಬಾಲಕಂ ಅಂಬುಜೇಕ್ಷಣಂ*  
> *ಚತುರ್ಭುಜಂ ಶಂಖಗದಾರ್ಯುದಾಯುಧಮ್ |*  
> *ಶ್ರೀವತ್ಸಲಕ್ಷ್ಮಂ ಗಲಶೋಭಿಕೌಸ್ತುಭಂ*  
> *ಪೀತಾಂಬರಂ ಸಾಂದ್ರಪಯೋದಸೌಭಗಮ್ ||*  
> 
> *ಮಹಾರ್ಹವೈಡೂರ್ಯಕಿರೀಟಕುಂಡಲ-*  
> *ತ್ವಿಷಾ ಪರಿಷ್ವಕ್ತಸಹಸ್ರಕುಂತಲಮ್ |*  
> *ಉದ್ದಾಮಕಾಂಚ್ಯಂಗದಕಂಕಣಾದಿಭಿರ್*  
> *ವಿರೋಚಮಾನಂ ವಸುದೇವ ಐಕ್ಷತ ||*  
> 
> **ಭಾವಾರ್ಥ:** ಕಮಲದಂತಹ ವಿಶಾಲ ಕಣ್ಣುಗಳುಳ್ಳ, ನಾಲ್ಕು ಕೈಗಳಲ್ಲಿ ಶಂಖ, ಚಕ್ರ, ಗದೆ ಮತ್ತು ಕಮಲವನ್ನು ಧರಿಸಿದ, ಎದೆಯ ಮೇಲೆ ಶ್ರೀವತ್ಸ ಚಿಹ್ನೆ, ಕೊರಳಿನಲ್ಲಿ ಹೊಳೆಯುವ ಕೌಸ್ತುಭ ಮಣಿ, ಮೈಮೇಲೆ ಪೀತಾಂಬರವನ್ನು ಧರಿಸಿ, ನೀಲಿಮೇಘಶ್ಯಾಮಲ ವರ್ಣದಿಂದ ಕಂಗೊಳಿಸುತ್ತಿದ್ದ ಆ ದಿವ್ಯ ಬಾಲಕನನ್ನು ವಸುದೇವರು ದರ್ಶಿಸಿದರು. ವೈಡೂರ್ಯ ರತ್ನಖಚಿತ ಕಿರೀಟ ಮತ್ತು ಕುಂಡಲಗಳ ಕಾಂತಿಯಿಂದ ಆತನ ಗುಂಗುರು ಕೂದಲು ಕಂಗೊಳಿಸುತ್ತಿತ್ತು.

ಆ ಕತ್ತಲೆಯ ಸೆರೆಮನೆಯು ಭಗವಂತನ ದಿವ್ಯ ತೇಜಸ್ಸಿನಿಂದ ಬೆಳಗಿತು. ದಿವ್ಯ ವನಮಾಲೆಯ ಸುಗಂಧವು ಎಲ್ಲೆಡೆ ಪಸರಿಸಿತು.

### ವಸುದೇವರ ದಿವ್ಯ ಸಾಕ್ಷಾತ್ಕಾರ

ಈ ಚತುರ್ಭುಜ ರೂಪವನ್ನು ನೋಡಿದ ವಸುದೇವರಿಗೆ ಕಂಸನ ಭಯವೆಲ್ಲಾ ಮಾಯವಾಯಿತು. ಈತನು ಸಾಮಾನ್ಯ ಮಗುವಲ್ಲ, ಭಕ್ತರನ್ನು ರಕ್ಷಿಸಲು ಬಂದ ಪರಮ ಪುರುಷೋತ್ತಮ ಭಗವಂತನೇ ಎಂದು ಅವರು ಅರಿತರು.

ರಾಜಕುಮಾರನ ಜನನದ ಸಮಯದಲ್ಲಿ ಬ್ರಾಹ್ಮಣರಿಗೆ ಗೋವುಗಳನ್ನು ದಾನ ಮಾಡುವುದು ಕ್ಷತ್ರಿಯ ಧರ್ಮ. ಆದರೆ ಸೆರೆಮನೆಯಲ್ಲಿದ್ದ ವಸುದೇವರ ಬಳಿ ಏನೂ ಇರಲಿಲ್ಲ. ಆದ್ದರಿಂದ ಅವರು ಮನಸ್ಸಿನಲ್ಲಿಯೇ ಸಾವಿರಾರು ಹಾಲುಕರೆಯುವ ಹಸುಗಳನ್ನು ಬ್ರಾಹ್ಮಣರಿಗೆ ದಾನ ಮಾಡಿದರು.

ನಂತರ ಕೈಮುಗಿದು ಸಾಷ್ಟಾಂಗ ಪ್ರಣಾಮಗಳನ್ನು ಅರ್ಪಿಸಿ, ಭಗವಂತನನ್ನು ಸ್ತುತಿಸಲು ಪ್ರಾರಂಭಿಸಿದರು.""",
                "questions": [
                    {
                        "question": "ಶ್ರೀಕೃಷ್ಣನ ಆವಿರ್ಭಾವದ ಸಮಯದಲ್ಲಿ ಯಾವ ನಕ್ಷತ್ರವು ಪ್ರಧಾನವಾಗಿತ್ತು?",
                        "options": [
                            {"text": "ರೋಹಿಣಿ", "is_correct": True},
                            {"text": "ಅಶ್ವಿನಿ", "is_correct": False},
                            {"text": "ಮಘಾ", "is_correct": False},
                            {"text": "ಭರಣಿ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಭಗವಂತನ ಆವಿರ್ಭಾವದ ಸಮಯದಲ್ಲಿ ಬ್ರಾಹ್ಮಣರ ಯಜ್ಞಾಗ್ನಿಯಲ್ಲಿ ಆದ ಪವಾಡವೇನು?",
                        "options": [
                            {"text": "ಯಜ್ಞಾಗ್ನಿಗಳು ತಾವಾಗಿಯೇ ಪ್ರಜ್ವಲಿಸಿದವು", "is_correct": True},
                            {"text": "ಅಗ್ನಿ ಆರಿಹೋಯಿತು", "is_correct": False},
                            {"text": "ಹಿಮದಂತೆ ತಣ್ಣಗಾಯಿತು", "is_correct": False},
                            {"text": "ಹೊಗೆ ತುಂಬಿಕೊಂಡಿತು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ದೇವಕಿಯ ಗರ್ಭದಿಂದ ಭಗವಂತನ ಜನನವನ್ನು ಶಾಸ್ತ್ರಗಳಲ್ಲಿ ಯಾವುದಕ್ಕೆ ಹೋಲಿಸಲಾಗಿದೆ?",
                        "options": [
                            {"text": "ಪೂರ್ವದಿಕ್ಕಿನಲ್ಲಿ ಉದಯಿಸುವ ಪೂರ್ಣಚಂದ್ರನಿಗೆ", "is_correct": True},
                            {"text": "ಮಧ್ಯಾಹ್ನದ ಸೂರ್ಯನಿಗೆ", "is_correct": False},
                            {"text": "ಉಲ್ಕೆಗೆ", "is_correct": False},
                            {"text": "ಮಿಂಚಿಗೆ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಭಗವಾನ್ ಶ್ರೀಕೃಷ್ಣನು ತಂದೆ-ತಾಯಿಯರ ಮುಂದೆ ಮೊದಲು ಯಾವ ರೂಪದಲ್ಲಿ ಪ್ರಕಟನಾದನು?",
                        "options": [
                            {"text": "ಶಂಖ, ಚಕ್ರ, ಗದಾ, ಪದ್ಮಧಾರಿ ಚತುರ್ಭುಜ ರೂಪದಲ್ಲಿ", "is_correct": True},
                            {"text": "ಅಳುವ ಸಾಮಾನ್ಯ ಮಗುವಿನ ರೂಪದಲ್ಲಿ", "is_correct": False},
                            {"text": "ಅಶರೀರವಾಣಿಯಾಗಿ", "is_correct": False},
                            {"text": "ಅಗ್ನಿಸ್ತಂಭವಾಗಿ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಶ್ರೀಕೃಷ್ಣನು ಧರಿಸಿದ್ದ ಪೀತಾಂಬರದ ಬಣ್ಣ ಯಾವುದು?",
                        "options": [
                            {"text": "ಚಿನ್ನದ ಹಳದಿ", "is_correct": True},
                            {"text": "ಕೆಂಪು", "is_correct": False},
                            {"text": "ಬಿಳಿ", "is_correct": False},
                            {"text": "ಕಪ್ಪು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಭಗವಂತನ ಎದೆ ಮತ್ತು ಕೊರಳಿನಲ್ಲಿ ಶೋಭಿಸುತ್ತಿದ್ದ ಆಭರಣಗಳು ಯಾವುವು?",
                        "options": [
                            {"text": "ಕೌಸ್ತುಭ ಮಣಿ ಮತ್ತು ಶ್ರೀವತ್ಸ ಚಿಹ್ನೆ", "is_correct": True},
                            {"text": "ಸ್ಯಮಂತಕ ಮಣಿ", "is_correct": False},
                            {"text": "ವಜ್ರದ ಹಾರ", "is_correct": False},
                            {"text": "ಮುತ್ತಿನ ಮಾಲೆ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಭಗವಂತನ ಮೈಬಣ್ಣವನ್ನು ಯಾವುದಕ್ಕೆ ಹೋಲಿಸಲಾಗಿದೆ?",
                        "options": [
                            {"text": "ಮಳೆಗಾಲದ ನೀಲಿ ಮೇಘಕ್ಕೆ (ಸಾಂದ್ರ-ಪಯೋದ)", "is_correct": True},
                            {"text": "ಬಿಳಿ ಹಿಮಕ್ಕೆ", "is_correct": False},
                            {"text": "ಚಿನ್ನಕ್ಕೆ", "is_correct": False},
                            {"text": "ಕೆಮ್ಮಣ್ಣಿಗೆ", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಭಗವಂತನು ಪ್ರಕಟವಾದಾಗ ಕತ್ತಲೆಯ ಸೆರೆಮನೆಗೆ ಏನಾಯಿತು?",
                        "options": [
                            {"text": "ಸೆರೆಮನೆಯು ದಿವ್ಯ ಬೆಳಕು ಮತ್ತು ಸುವಾಸನೆಯಿಂದ ತುಂಬಿಹೋಯಿತು", "is_correct": True},
                            {"text": "ಇನ್ನಷ್ಟು ಕತ್ತಲಾಯಿತು", "is_correct": False},
                            {"text": "ಭೂಕಂಪದಿಂದ ಕುಸಿದುಹೋಯಿತು", "is_correct": False},
                            {"text": "ಹೊಗೆ ತುಂಬಿಕೊಂಡಿತು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಸೆರೆಮನೆಯಲ್ಲಿದ್ದ ವಸುದೇವರು ಮನಸ್ಸಿನಲ್ಲಿಯೇ ಏನನ್ನು ದಾನ ಮಾಡಿದರು?",
                        "options": [
                            {"text": "ಸಾವಿರಾರು ಹಾಲುಕರೆಯುವ ಹಸುಗಳನ್ನು ಬ್ರಾಹ್ಮಣರಿಗೆ ದಾನ ಮಾಡಿದರು", "is_correct": True},
                            {"text": "ಆಯುಧಗಳನ್ನು ಸಂಗ್ರಹಿಸಿದರು", "is_correct": False},
                            {"text": "ಅತ್ತು ಗೋಳಾಡಿದರು", "is_correct": False},
                            {"text": "ಕಂಸನ ಬಳಿ ಹಣ ಕೇಳಿದರು", "is_correct": False}
                        ]
                    },
                    {
                        "question": "ಶ್ರೀಮದ್ಭಾಗವತದ ಹತ್ತನೇ ಸ್ಕಂಧದ ಯಾವ ಅಧ್ಯಾಯದಲ್ಲಿ ಶ್ರೀಕೃಷ್ಣನ ಜನ್ಮವನ್ನು ವರ್ಣಿಸಲಾಗಿದೆ?",
                        "options": [
                            {"text": "ಅಧ್ಯಾಯ 3", "is_correct": True},
                            {"text": "ಅಧ್ಯಾಯ 1", "is_correct": False},
                            {"text": "ಅಧ್ಯಾಯ 6", "is_correct": False},
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

        self.stdout.write(self.style.SUCCESS(f"Successfully populated Story 7 (ID: {story.id}) across all 7 languages!"))
