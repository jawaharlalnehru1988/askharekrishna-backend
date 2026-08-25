import logging
from django.core.management.base import BaseCommand
from vaishnava_calendar.models import CalendarObservance, CalendarObservanceTranslation

logger = logging.getLogger(__name__)

AVATAR_STORIES = {
    'Janmashtami': {
        'title': 'Sri Krsna Janmashtami',
        'story': """### Sri Krsna Janmashtami: The Divine Advent of the Supreme Personality of Godhead

#### 1. Eternal Identity & Tattva
Lord Sri Krishna is the Supreme Absolute Truth, the original Supreme Personality of Godhead (*kṛṣṇas tu bhagavān svayam* — *Srimad-Bhagavatam* 1.3.28), from whom all Vishnu incarnations, Vaikuntha planets, and cosmic universes emanate. He appears in His original two-armed *svayam-rūpa* form at the end of Dvapara-yuga on the eighth day of the dark fortnight (*Kṛṣṇa Aṣṭamī*) in the month of Sravana/Bhadra under the auspicious *Rohiṇī* star.

---

#### 2. Sacred Pastimes from Srimad-Bhagavatam (Canto 10, Chapters 1–3)

##### Pastime 1: Earth's Appeal & The Cosmic Prophecy
When demonic kings burdened Mother Earth (*Bhūmi-devī*) with massive military oppression, she assumed the form of a cow and wept on the shores of the milk ocean. Lord Brahma entered deep meditation and received the *Puruṣa-sūkta* message from Lord Vishnu: *"The Supreme Personality of Godhead will soon appear in the Yadu dynasty to relieve the burden of Earth."*

Meanwhile, in Mathura, King Kamsa drove the chariot for his newly wedded sister Devaki and her husband Vasudeva. Suddenly, a thunderous voice from the sky proclaimed: *"O foolish Kamsa! The eighth child born from Devaki's womb will slay you!"* Terrified, Kamsa threw Vasudeva and Devaki into a dark subterranean dungeon bound in heavy iron chains, killing their first six newborn infants.

##### Pastime 2: The Midnight Advent in Kamsa's Prison Cell
At midnight on Bhadra Krishna Ashtami, inside Kamsa's locked prison cell, Lord Sri Krishna appeared not as an ordinary human infant, but in His magnificent four-armed **Vasudeva-Vishnu form** (*caturbhuja*). He held the conch, discus, mace, and lotus flower, decorated with the Kaustubha jewel, Srivatsa mark, golden silk garments, and a blazing jeweled crown!

Vasudeva and Devaki folded their hands in awe and offered sublime prayers (*Srimad-Bhagavatam* 10.3.13–31). Fearing Kamsa's wrath, Devaki begged: *"O Lord of Vaikuntha! Please withdraw this four-armed divine form so my brother Kamsa cannot see You!"* Responding to Her maternal love, the Supreme Lord transformed Himself into a sweet, two-armed newborn infant.

##### Pastime 3: The Midnight Crossing of the Yamuna River
By the Lord's *Yogamāyā* potency, the heavy iron shackles fell from Vasudeva's wrists and feet, the massive locked iron doors swung wide open, and all of Kamsa's guards fell into deep hypnotic sleep. 

Vasudeva placed baby Krishna in a woven wicker basket upon his head and stepped into a roaring midnight thunderstorm. **Ananta Sesha** hovered behind Vasudeva, spreading His multi-hooded canopy over baby Krishna to shield Him from the torrential rain. 

When Vasudeva reached the swollen, churning Yamuna River, the river goddess parted her waters to create a dry path, allowing Vasudeva to cross safely to Gokula. Vasudeva placed baby Krishna beside sleeping Mother Yashoda, picked up Yashoda's newborn baby girl (Yogamaya), and returned to Kamsa's prison before dawn.

##### Pastime 4: Nandotsava — The Festival of Joy in Vraja
The following morning in Gokula, Nanda Maharaja and Yashoda Devi rejoiced over the birth of their dark, golden-eyed boy. The entire village of Vrindavan celebrated **Nandotsava**, singing *kīrtana*, dancing in joy, and tossing butter, yogurt, turmeric, and milk upon one another—a festival celebrated to this day across the world.

---

#### 3. Spiritual Significance & Observance Guidelines
Fasting on Sri Krishna Janmashtami cleanses a devotee of sins accumulated over millions of lifetimes (*Janmaṣṭamī-vrata*). 

- **Fasting Rules:** Devotees observe a complete fast (or water-only fast) until midnight.
- **Midnight Worship:** At midnight (the hour of Krishna's birth), elaborate *abhiṣeka* (bathing of Krishna with milk, honey, ghee, yogurt, fruit juices, and holy waters) is performed accompanied by ecstatic kirtana.
- **Offering & Parana:** 108 varieties of unoffered delicacies (*bhoga*) are offered to Lord Krishna, followed by midnight *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray on Janmashtami for pure *kṛṣṇa-bhakti*, freedom from material bondage, and the constant remembrance of Lord Sri Krishna's lotus feet.

**Pranama Mantra:**
> *he kṛṣṇa karuṇā-sindho dīna-bandho jagat-pate*  
> *gopeśa gopikā-kānta rādhā-kānta namo 'stu te*  
>  
> *"O my dear Krishna, You are the ocean of mercy, the friend of the distressed, and the Lord of creation. You are the master of the cowherds and the lover of the gopis, especially Srimati Radharani. I offer my respectful obeisances unto You."*
"""
    },
    'Gaura Purnima': {
        'title': 'Gaura Purnima',
        'story': """### Gaura Purnima: The Golden Advent of Sri Caitanya Mahaprabhu

#### 1. Eternal Identity & Tattva
Sri Caitanya Mahaprabhu is the Supreme Personality of Godhead, Lord Sri Krishna Himself, appearing in the golden color (*gaura-varṇa*) and ecstatic mood (*bhāva*) of Srimati Radharani (*kṛṣṇa-varṇaṁ tviṣākṛṣṇaṁ* — *Srimad-Bhagavatam* 11.5.32; *rādhā-bhāva-dyuti-suvalitaṁ naumi kṛṣṇa-svarūpam* — *Caitanya-caritamrta* Adi 1.5). He appeared in Kali-yuga to inaugurate the *Yuga-dharma* of Harinama Sankirtana and freely distribute the highest gift of *kṛṣṇa-prema*.

---

#### 2. Sacred Pastimes from Sri Caitanya-caritamrta & Sri Caitanya Bhagavata

##### Pastime 1: The Lunar Eclipse & Birth at Mayapur Yoga Pith (1486 CE)
On Phalguna Purnima in 1486 CE (under Phalguni constellation), during a total lunar eclipse (*grahaṇa*), Lord Caitanya appeared in Navadvipa (Mayapur) under a Neem tree in the courtyard of Sri Jagannatha Misra and Srimati Sachi Devi (hence named **Nimai**).

Because of the lunar eclipse, tens of thousands of people across Bengal stood waist-deep in the holy Ganges River, loudly chanting *Hari! Hari! Haribol!*, unknowingly welcoming the Supreme Lord with congregational chanting of the Holy Names!

##### Pastime 2: Childhood Miracles of Nimai Pandit
As a small child, Nimai would stop crying only when the women of Navadvipa clapped their hands and chanted *Hare Krishna!* 

Once, a poisonous cobra slithered into the room, and little Nimai lay down on its coils as if resting on Lord Ananta Sesha! On another occasion, two thieves kidnapped baby Nimai to steal his golden bangles, but Nimai mystically bewildered them, causing them to wander in circles and carry the child straight back to Jagannatha Misra's house.

##### Pastime 3: Sannyasa & Deliverance of Jagai and Madhai
At age 24, Nimai took *sannyāsa* from Keshava Bharati in Katwa, receiving the name **Sri Krishna Caitanya**. 

Before His sannyasa, Lord Caitanya and Lord Nityananda delivered the notorious, drunken brothers Jagai and Madhai. When Madhai struck Lord Nityananda with a broken clay pot, drawing blood, Mahaprabhu summoned His Sudarshana Chakra. But Lord Nityananda begged for their forgiveness, causing both brothers to weep in repentance, abandon their sinful ways, and become saintly devotees.

##### Pastime 4: The Gambhira Ecstasies in Jagannath Puri
Mahaprabhu spent His final 24 years in Jagannath Puri residing at Kasi Misra's house (Gambhira). Day and night, in the intimate company of Svarupa Damodara Gosvami and Ramananda Raya, He relished the deepest, most confidential mellows of love of Krishna in separation (*vipralambha-bhāva*), setting the ultimate standard of devotion for Gaudiya Vaishnavas.

---

#### 3. Spiritual Significance & Observance Guidelines
Gaura Purnima marks the beginning of the new year in the Gaudiya Vaishnava calendar.

- **Fasting Rules:** Devotees observe a strict fast from all food and water (or water-only) until moonrise.
- **Festival Activities:** Continuous *gaura-līlā* recitations, *nāma-saṅkīrtana*, and magnificent *māhā-abhiṣeka* of Sri Gauranga Deities with milk, fruit juices, and sacred waters.
- **Moonrise Fast Break:** At moonrise (approx. 6:00 PM), devotees break fast with *anukalpa-prasādam* (non-grain dishes), followed by a grand feast on the next day (Anandotsava).

---

#### 4. How to Pray & Seek Blessings
Devotees pray on Gaura Purnima for unwavering attachment to Harinama Sankirtana, liberation from spiritual pride, and shelter at Lord Gauranga's golden lotus feet.

**Pranama Mantra:**
> *namo mahā-vadānyāya kṛṣṇa-prema-pradāya te*  
> *kṛṣṇāya kṛṣṇa-caitanya-nāmne gaura-tviṣe namaḥ*  
>  
> *"O most munificent incarnation! You are Krishna Himself appearing as Sri Krishna Caitanya Mahaprabhu. You have assumed the golden color of Srimati Radharani, and You are freely distributing what no other incarnation has ever given: pure love of Krishna. I offer my respectful obeisances unto You."*
"""
    },
    'Nityananda Trayodasi': {
        'title': 'Nityananda Trayodasi',
        'story': """### Nityananda Trayodasi: Appearance of Lord Nityananda Prabhu

#### 1. Eternal Identity & Tattva
Lord Nityananda Prabhu is none other than **Lord Balarama** (Sri Ananta Sankarshana), the original plenary expansion of Lord Sri Krishna. In Gaura-lila, He appears as the primary embodiment of compassion (*prakāśa-vigraha*) and the original spiritual master (*ādi-guru*). He is the second personality of the Pancha-tattva, delivering the most fallen souls through Harinama Sankirtana.

---

#### 2. Sacred Pastimes from Sri Caitanya Bhagavata

##### Pastime 1: Birth in Ekachakra (1474 CE)
Lord Nityananda appeared on Magha Sukla Trayodasi in the village of Ekachakra (Rarh district, Bengal) as the son of Hadai Pandita and Srimati Padmavati Devi. 

As a child, Nitai organized village boys into theatrical plays re-enacting Vedic pastimes (such as Vamana, Nrisimha, Varaha, and Ramacandra). When a traveling sannyasi visited Hadai Pandita's house and requested young Nitai as his traveling companion (*bhikṣā*), Hadai Pandita surrendered his heart and gave Nitai away. Nityananda spent 20 years visiting holy pilgrimage sites across India awaiting Lord Caitanya's advent.

##### Pastime 2: Reunited with Lord Caitanya at Nandanacarya's House (1506 CE)
Arriving in Navadvipa in 1506 CE, Nityananda stayed secretly at Nandanacarya's house. Lord Caitanya told His associates: *"I saw a magnificent personality in My dream searching for My residence!"* 

Lord Caitanya led all the devotees to Nandanacarya's house, where Nityananda sat bathed in a radiant golden aura. The moment Nityananda saw Mahaprabhu, He collapsed in divine ecstasy. Mahaprabhu held Nityananda in His arms and declared: *"Nityananda is My elder brother Balarama!"*

##### Pastime 3: The Deliverance of Jagai and Madhai
When Lord Nityananda and Haridasa Thakura went door-to-door preaching Harinama in Navadvipa, they confronted the feared tyrants Jagai and Madhai. 

Madhai struck Nityananda on the forehead with a broken clay vessel, drawing blood. Instead of punishing them, Nityananda smiled with boundless mercy and pleaded: *"You may strike Me, but please chant the Holy Name of Krishna!"* Astonished by Nityananda's unbelievable forgiveness, Jagai and Madhai fell weeping at His feet, completely repenting and transforming into saintly devotees.

##### Pastime 4: Boundless Mercy Across Bengal
Lord Caitanya instructed Nityananda to return to Bengal and freely bestow *kṛṣṇa-prema* upon all living beings regardless of caste, creed, or qualifications. Nityananda flooded Bengal with *prema-saṅkīrtana*, liberating even bandits, outcasts, and fallen souls.

---

#### 3. Spiritual Significance & Observance Guidelines
Without the grace of Lord Nityananda Prabhu, no one can attain shelter at the lotus feet of Sri Gaura-Radha-Krishna (*nitāiyer karuṇā habe, braje rādhā-kṛṣṇa pābe*).

- **Fasting Rules:** Fasting is observed until noon (12:00 PM).
- **Worship:** Morning *abhiṣeka* of Sri Gaura-Nitai Deities accompanied by *nāma-saṅkīrtana*, followed by reading Nityananda-lila from *Caitanya Bhagavata*.
- **Noon Parana:** At noon, feast offerings (*bhoga*) are presented to Sri Gaura-Nitai, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Lord Nityananda Prabhu on Nityananda Trayodasi for spiritual strength (*bala*), freedom from pride and anger, and the mercy of Lord Caitanya Mahaprabhu.

**Pranama Mantra:**
> *saṅkarṣaṇaḥ kāraṇa-toya-śāyī*  
> *garbhododa-śāyī ca payobdhi-śāyī*  
> *śeṣaś ca yasyāṁśa-kalāḥ sa nityā-*  
> *nandākhya-rāmaḥ śaraṇaṁ mamāstu*  
>  
> *"May Lord Nityananda Rama be my eternal shelter. Sankarshana, Karanodakasayi Vishnu, Garbhodakasayi Vishnu, Kshirodakasayi Vishnu, and Sesha are all His plenary portions and portions of His plenary portions."*
"""
    },
    'Rama Navami': {
        'title': 'Sri Rama Navami',
        'story': """### Sri Rama Navami: Appearance of Lord Sri Ramacandra

#### 1. Eternal Identity & Tattva
Lord Sri Ramacandra is the Supreme Personality of Godhead, the Seventh Avatara of Lord Vishnu, appearing in Treta-yuga in the Ikshvaku dynasty (Surya-vamsa) as the ideal monarch (*Maryādā-Puruṣottama*). He embodies absolute truth (*satya*), righteousness (*dharma*), flawless chivalry, and boundless affection for His devotees.

---

#### 2. Sacred Pastimes from Valmiki Ramayana & Srimad-Bhagavatam (Canto 9, Chapters 10–11)

##### Pastime 1: Divine Birth in Ayodhya
On Chaitra Sukla Navami under the Punarvasu constellation at noon, Lord Ramacandra appeared in Ayodhya as the eldest son of King Dasharatha and Queen Kausalya, alongside His divine brothers Lakshmana (incarnation of Sesha), Bharata (incarnation of Sudarshana Chakra), and Shatrughna (incarnation of Panchajanya Conch).

##### Pastime 2: Protecting Visvamitra's Yajna & Breaking Shiva's Bow
As a youth, Lord Rama accompanied Sage Visvamitra into the forest, vanquishing the demons Tataka and Subahu. In Mithila, He effortlessly lifted, strung, and snapped the colossal iron bow of Lord Shiva (*Haradhanus*), winning the hand of Srimati Sita Devi (incarnation of Goddess Lakshmi).

##### Pastime 3: Forest Exile & Unswerving Truthfulness
On the eve of His coronation, to honor His father's royal promise to Queen Kaikeyi, Lord Rama cheerfully relinquished the empire of Ayodhya without a trace of sorrow, embarking on a 14-year forest exile to Dandakaranya with Sita Devi and Lakshmana.

##### Pastime 4: Slaying Ravana & Establishing Rama-rajya
When the demon king Ravana abducted Sita Devi, Lord Rama allied with Sugriva and Hanuman, built the miraculous stone bridge (**Rāma-setu**) across the ocean to Lanka, and annihilated Ravana's army. Returning in triumph to Ayodhya, Lord Rama established **Rāma-rājya**—an era of divine peace, perfection, and prosperity.

---

#### 3. Spiritual Significance & Observance Guidelines
Sri Rama Navami grants liberation, victory over unrighteousness, and protection to all who chant Lord Rama's Holy Name.

- **Fasting Rules:** Fasting is observed until sunset (or 12:00 PM depending on tradition).
- **Activities:** Recitation of *Valmiki Ramayana* or *Ramacharitamanasa*, chanting *Śrī Rāma Jaya Rāma Jaya Jaya Rāma*, and elaborate evening *kīrtana*.
- **Parana:** Breaking fast after sunset with cooling panakam, kosambari, and *prasādam*.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Lord Sri Ramacandra on Rama Navami for unswerving truthfulness, moral strength, and unconditional surrender at His lotus feet.

**Pranama Mantra:**
> *rāmāya rāmabhadrāya rāmacandrāya vedhase*  
> *raghunāthāya nāthāya sītāyāḥ pataye namaḥ*  
>  
> *"I offer my respectful obeisances unto Lord Ramacandra, the protector of all, the Lord of Raghu's dynasty, the Supreme Controller, and the beloved husband of Srimati Sita Devi."*
"""
    },
    'Radhastami': {
        'title': 'Radhastami',
        'story': """### Radhastami: The Divine Appearance of Srimati Radharani

#### 1. Eternal Identity & Tattva
Srimati Radharani is the supreme internal pleasure potency (*hlādinī-śakti*) of Lord Sri Krishna (*rādhā kṛṣṇa-praṇaya-vikṛtir hlādinī śaktir asmād* — *Caitanya-caritamrta* Adi 1.6). She is the Queen of Vrindavan (*Vṛndāvaneśvarī*), the origin of all Laxmis, and the fountainhead of pure devotional service (*bhakti-devī*). Lord Krishna is the attractor of all worlds (*madana-mohana*), but Srimati Radharani attracts even Lord Krishna Himself (*madana-mohana-mohinī*).

---

#### 2. Sacred Pastimes from Padma Purana, Brahma-vaivarta Purana & Vraja Tradition

##### Pastime 1: Golden Appearance in Raval
On Bhadra Sukla Ashtami under the Anuradha constellation at sunrise, Srimati Radharani appeared in Raval (near Gokula) on a golden lotus flower floating upon the Yamuna River. King Vrishabhanu and Queen Kirtida discovered the self-luminous baby girl floating upon the lotus and joyfully adopted Her as their daughter.

##### Pastime 2: Opening Her Eyes Only for Krishna
Baby Radharani kept Her eyes tightly closed from birth, refusing to look at anything in the material world. When Nanda Maharaja and Yashoda Devi arrived from Gokula to see the newborn girl, toddler Krishna stepped up to Radharani's cradle. 

The moment Krishna's sweet divine fragrance touched Radharani, She opened Her eyes for the very first time—beholding Her eternal Lord Sri Krishna as Her first vision!

##### Pastime 3: The Queen of Seva Kunj & Rasa-Lila
In Vrindavan, Srimati Radharani is the supreme embodiment of *Mahābhāva*—the zenith of divine love. Without Srimati Radharani's grace (*rādhā-kṛpā*), no soul can enter the *Rāsa-līlā* or attain pure *rāgānugā-bhakti*. Lord Krishna Himself bows His head to touch Srimati Radharani's lotus feet (*rādhā-caraṇam*).

##### Pastime 4: The Immortal Nectar Cook for Krishna
At Mother Yashoda's request and blessed by Sage Durvasa's boon (that any dish prepared by Radharani would taste like nectar and grant long life to the eater), Srimati Radharani cooked delicious milk preparations (*kṣīra*, *pāyasa*, sweets) for Lord Krishna every afternoon at Nandagram.

---

#### 3. Spiritual Significance & Observance Guidelines
Radhastami is the most sacred day for Gaudiya Vaishnavas, granting unconditional entrance into *kṛṣṇa-prema*.

- **Fasting Rules:** Fasting is observed until noon (12:00 PM).
- **Festival Activities:** Elaborate *māhā-abhiṣeka* of Srimati Radharani and Sri Krishna with milk, honey, fruit juices, and fragrant flowers, accompanied by *Rādhikā-ṣṭakam* recitations and kirtana.
- **Noon Parana:** At 12:00 PM, an extraordinary feast offering (*bhoga*) prepared with love is presented to Srimati Radharani, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srimati Radharani on Radhastami for Her compassionate glance (*kṛpā-kaṭākṣa*), pure maidservantship (*rādhā-dāsyam*), and eternal shelter at Her lotus feet.

**Pranama Mantra:**
> *tapta-kāñcana-gaurāṅgi rādhe vṛndāvaneśvari*  
> *vṛṣabhānu-sute devī praṇamāmi hari-priye*  
>  
> *"I offer my respectful obeisances unto Srimati Radharani, whose bodily complexion is like molten gold, who is the Queen of Vrindavan, the daughter of King Vrishabhanu, and immensely dear to Lord Hari."*
"""
    },
    'Balarama': {
        'title': 'Sri Balarama Purnima',
        'story': """### Sri Balarama Purnima: Appearance of Lord Balarama

#### 1. Eternal Identity & Tattva
Lord Balarama is the first direct plenary expansion (*prakāśa-mūrti*) of Lord Sri Krishna, the source of all Vishnu incarnations, Ananta Sesha, Sankarshana, and cosmic maintenance. He is the divine elder brother of Sri Krishna, embodying spiritual strength (*bala*), protection, and pure Mood of Service (*sevā-bhāva*).

---

#### 2. Sacred Pastimes from Srimad-Bhagavatam (Canto 10)

##### Pastime 1: Mystical Transfer from Devaki to Rohini
Lord Balarama first entered Devaki's womb as her seventh child in Kamsa's prison cell. By Lord Krishna's divine command, Yogamaya mystically transferred the embryo from Devaki's womb to the womb of Rohini Devi residing in Gokula at Nanda Maharaja's palace. Thus He was born on Sravana Purnima in Gokula and named **Sankarṣaṇa** (the transferred one) and **Balarāma**.

##### Pastime 2: Subduing Dhenukasura at Talavana
When young Krishna and Balarama were tending calves in Vrindavan, their cowherd friends begged to taste the ripe palm fruits of Talavana forest, guarded by the ferocious ass-demon Dhenukasura. 

Lord Balarama entered Talavana, grabbed Dhenukasura by his hind legs, twirled him around, and hurled him to the top of a giant palm tree, slaying the demon effortlessly and freeing Talavana for all cows and cowherds!

##### Pastime 3: Slaying Pralambasura
During a game of leap-frog, the demon Pralambasura disguised himself as a cowherd boy and carried Lord Balarama away on his shoulders. 

Realizing the demon's evil intent, Lord Balarama struck Pralambasura's head with His mighty fist, shattering his skull like a lightning bolt striking a mountain peak.

##### Pastime 4: Subduing Yamuna River with His Plow (*Hala*)
During the *Rāsa-yātrā* at Ramaghat, Lord Balarama desired to bathe in the Yamuna River and called her to come closer. When Yamuna River hesitated, Lord Balarama dragged her with His plow (*hala*), carving new channels through Vrindavan. The river goddess bowed in fear and surrendered at His lotus feet.

---

#### 3. Spiritual Significance & Observance Guidelines
Lord Balarama bestows spiritual strength (*spiritual energy*) needed to overcome material desires and serve Lord Krishna.

- **Fasting Rules:** Fasting is observed until noon (12:00 PM).
- **Festival Activities:** Abhisheka of Lord Balarama and Lord Krishna Deities, offering honey-infused beverages (*vāruṇī*), royal blue garments, and grand *kīrtana*.
- **Noon Parana:** Feast offering (*bhoga*) presented at noon, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Lord Balarama on Balarama Purnima for spiritual strength to destroy anarthas, protection against illusions, and devotion to Sri Krishna.

**Pranama Mantra:**
> *namas te halāyudhāya namas te musalāyudha*  
> *namas te revatī-kānta namas te bhakta-vatsala*  
>  
> *"I offer my respectful obeisances unto Lord Balarama, who holds the plow and mace weapons, who is the beloved husband of Srimati Revati Devi, and who is immensely compassionate toward His devotees."*
"""
    },
    'Nrisimhadeva': {
        'title': 'Nrisimha Caturdasi',
        'story': """### Nrisimha Caturdasi: Appearance of Lord Nrisimhadeva

#### 1. Eternal Identity & Tattva
Lord Nrisimhadeva is the half-man, half-lion incarnation (*Nara-hari*) of Lord Sri Vishnu, appearing specifically to protect His five-year-old pure devotee Prahlada Maharaja and destroy the tyrannical demon king Hiranyakashipu (*prahlāda-kleda-kāriṇe*). He represents the fierce protection of the Lord for His surrendered devotees.

---

#### 2. Sacred Pastimes from Srimad-Bhagavatam (Canto 7, Chapters 5–10)

##### Pastime 1: Hiranyakashipu's Boons & Tyranny
The demon king Hiranyakashipu performed extreme austerities on Mandara Mountain, securing boons from Lord Brahma that he could not be killed by any human or beast, inside or outside, during day or night, on land or in water/sky, nor by any manufactured weapon.

##### Pastime 2: Five-Year-Old Prahlada's Unflinching Devotion
While in his mother Kayadhu's womb, Prahlada heard Narada Muni's divine instructions. At age five in demonic school, Prahlada preached *Navadhā-Bhakti* to his schoolmates! Furious, Hiranyakashipu subjected Prahlada to horrific tortures—throwing him off cliffs, stepping on him with elephants, hurling him into snake pits, and feeding him deadly poison. But Lord Vishnu shielded Prahlada from every attempt!

##### Pastime 3: The Blazing Pillar & Emergence of Nrisimhadeva
Hiranyakashipu pointed to a golden pillar in his palace and demanded: *"Is your God inside this pillar?"* Prahlada answered calmly: *"Yes, my Lord is everywhere!"* 

Enraged, Hiranyakashipu struck the pillar with his heavy mace. Immediately, a thunderous roar reverberated through the universe, and Lord Nrisimhadeva emerged from the pillar in a terrifying half-man, half-lion form with eyes like molten gold, razor claws, and a roaring mane!

##### Pastime 4: Fulfilling All Boons & Pacification by Prahlada
Lord Nrisimhadeva caught Hiranyakashipu at dusk (*neither day nor night*), placed him on His lap (*neither land nor sky*), sat on the doorway threshold (*neither inside nor outside*), and ripped open his chest with His razor-sharp claws (*neither man nor beast, nor manufactured weapon*), impeccably preserving Lord Brahma's boons! 

Even Lord Brahma, Lord Shiva, and Goddess Lakshmi dared not approach Lord Nrisimhadeva's roaring anger. But when five-year-old Prahlada bowed down, Lord Nrisimhadeva licked the child with deep affection, placed His lotus hand on Prahlada's head, and granted him pure unalloyed love of God.

---

#### 3. Spiritual Significance & Observance Guidelines
Lord Nrisimhadeva destroys all obstacles (*vighna-vināśaka*) on the path of devotional service.

- **Fasting Rules:** Fasting is observed until dusk (sunset / 6:00 PM).
- **Festival Activities:** Abhisheka of Lord Nrisimhadeva, chanting *Sri Nrisimha Kavacha*, *Nrisimha Ashtakam*, and *Ugram Veeram Maha-Vishnum*.
- **Dusk Parana:** Breaking fast after dusk with non-grain / feast *prasādam*.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Lord Nrisimhadeva on Nrisimha Caturdasi for protection from internal enemies (lust, anger, greed, pride) and unshakeable shelter at His lotus feet.

**Pranama Mantra:**
> *namas te narasimhāya prahlādāhlāda-dāyine*  
> *hiraṇyakasipor vakṣah-śilā-ṭaṅka-nakhālaye*  
>  
> *ito nṛsiṁhaḥ parato nṛsiṁho yato yato yāmi tato nṛsiṁhaḥ*  
> *bahir nṛsiṁho hṛdaye nṛsiṁho nṛsiṁham ādiṁ śaraṇaṁ prapadye*  
>  
> *"I offer my respectful obeisances unto Lord Nrisimhadeva, who gives joy to Prahlada Maharaja and whose nails are like chisels on the stonelike chest of the demon Hiranyakashipu. Lord Nrisimha is here and He is there. Wherever I go, Lord Nrisimha is there. He is in the heart and He is outside as well. I surrender unto Lord Nrisimha, the origin of all things and the supreme refuge."*
"""
    },
    'Vamana Dvadasi': {
        'title': 'Sri Vamana Dvadasi',
        'story': """### Sri Vamana Dvadasi: Appearance of Lord Vamanadeva

#### 1. Eternal Identity & Tattva
Lord Vamanadeva is the fifth Avatara of Lord Vishnu, appearing in Treta-yuga as a dwarf brahmana (*brahmacāri-vaṭu*) to Sage Kashyapa and Mother Aditi. He appeared to restore Lord Indra's heavenly kingdom, subdue the pride of King Bali, and grant King Bali the highest perfection of total self-surrender (*ātma-nivedanam*).

---

#### 2. Sacred Pastimes from Srimad-Bhagavatam (Canto 8, Chapters 15–23)

##### Pastime 1: Birth from Aditi's Payovrata Vow
Mother Aditi performed the 12-day *Payovrata* (milk vow) to conceive a divine son to protect the demigods. On Bhadra Sukla Dvadasi under Shravana constellation at noon, Lord Vishnu appeared as a radiant dwarf brahmana boy holding an umbrella (*chattra*), staff (*daṇḍa*), and water pot (*kamaṇḍalu*).

##### Pastime 2: Arrival at King Bali's Yajna
King Bali (grandson of Prahlada Maharaja) was conducting his 100th *Ashvamedha Yajna* on the banks of the Narmada River. 

When young Vamanadeva entered the sacrificial arena, His divine effulgence stunned all present. King Bali rose, washed Vamanadeva's lotus feet, placed the water on his head, and offered Him any gift—gold, villages, or kingdoms.

##### Pastime 3: Asking for Three Steps of Land
Vamanadeva smiled gently and asked for only **three steps of land** measured by His small feet (*padāni trīṇi*). 

Guru Shukracharya recognized Vamanadeva as Lord Vishnu and warned Bali: *"Do not grant this request! He will take everything!"* But King Bali declared: *"If the Supreme Lord Himself begs at my door, I am blessed to surrender everything!"*

##### Pastime 4: Trivikrama Form & Total Surrender
As Bali poured holy water to seal the gift, Vamanadeva expanded into His cosmic form (**Trivikrama**). With His first step, He covered the Earth and lower planets. With His second step, He covered the celestial planets and pierced the universe's outer shell, causing the holy Ganges (*Ākāśa-gaṅgā*) to flow down from His big toe.

Finding no place left for the third step, Vamanadeva asked: *"Where shall I place My third step?"* 

King Bali bowed his head with ecstatic surrender: *"O Lord! Please place Your third step upon my head!"* 

Deeply pleased by Bali's total surrender (*ātma-nivedanam*), Lord Vamanadeva placed His foot on Bali's head, made him sovereign of Sutala-loka (a planet far superior to heaven), and personally became the eternal gatekeeper of Bali's palace!

---

#### 3. Spiritual Significance & Observance Guidelines
Lord Vamanadeva teaches total surrender of ego and worldly wealth (*ātma-nivedanam*).

- **Fasting Rules:** Fasting is observed until noon (12:00 PM).
- **Festival Activities:** Abhisheka of Lord Vamanadeva, reading *Srimad-Bhagavatam* Canto 8 (Bali-Vamana pastimes), and offering yellow silk garments, flowers, and sweet rice.
- **Noon Parana:** Feast offering presented at noon, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Lord Vamanadeva on Vamana Dvadasi for complete surrender of false pride and ego at His lotus feet.

**Pranama Mantra:**
> *namo brahmaṇya-devāya go-brāhmaṇa-hitāya ca*  
> *jagad-dhitāya kṛṣṇāya govindāya namo namaḥ*  
>  
> *chalayasi vikramate balim adbhuta-vāmana*  
> *naka-dharaṇa-vikramaṇena janāṁs tapayasi*  
> *kesava dhṛta-vāmana-rūpa jaya jagadīśa hare*  
>  
> *"O Keshava! O Lord of the Universe! O Lord Hari who have assumed the form of a dwarf brahmana! All glories to You! By Your wonderful steps You tricked King Bali, and by stepping across the universe You purified all living beings."*
"""
    },
    'Varaha Dvadasi': {
        'title': 'Varaha Dvadasi',
        'story': """### Varaha Dvadasi: Appearance of Lord Varahadeva

#### 1. Eternal Identity & Tattva
Lord Varahadeva is the Second Avatara of Lord Vishnu, appearing in Satya-yuga as a colossal boar incarnation (*Yajña-Varāha*). He emerged from Lord Brahma's nostril to rescue Mother Earth (*Bhūmi-devī*) from the depths of the Garbhodaka Ocean and slay the powerful demon Hiranyaksha.

---

#### 2. Sacred Pastimes from Srimad-Bhagavatam (Canto 3, Chapters 13–19)

##### Pastime 1: Emergence from Lord Brahma's Nostril
When the demon Hiranyaksha dragged Mother Earth into the dark abyss of the cosmic ocean, Lord Brahma fell into intense anxiety. As Brahma meditated on Lord Vishnu, a tiny white boar no larger than a thumb tip (*aṅguṣṭha-mātra*) emerged from Brahma's nostril. 

Within moments, before Lord Brahma and the assembled sages, the boar expanded into a colossal, mountain-sized entity with eyes like blazing lightning and a tusk like a gleaming white peak!

##### Pastime 2: Rescuing Mother Earth
Lord Varahadeva roared like thunder, dove deep into the Garbhodaka Ocean, located Mother Earth in the dark depths, and gently lifted her upon His white tusks (*daṁṣṭrā*). Swimming back to the cosmic surface, He placed Mother Earth upon the ocean waters, endowing her with gravitational stability.

##### Pastime 3: Battle with Hiranyaksha
The arrogant demon Hiranyaksha confronted Lord Varahadeva, hurling a heavy iron mace and launching fierce attacks. Lord Varahadeva parried every weapon with ease. Finally, Lord Varahadeva struck Hiranyaksha behind the ear with His forefoot, crushing the demon's life force and restoring peace to the universe.

##### Pastime 4: Glorification as Yajna-Varaha
The great rishis of Janaloka and Tapoloka offered majestic prayers (*Srimad-Bhagavatam* 3.13.25–45), worshiping Lord Varaha as **Yajña-Varāha**—the personification of all Vedic fire sacrifices, whose bristles are kusha grass, whose eyes are sacrificial ghee, and whose tusks are the altars.

---

#### 3. Spiritual Significance & Observance Guidelines
Lord Varahadeva rescues fallen souls drowning in the ocean of material existence.

- **Fasting Rules:** Fasting is observed until noon (12:00 PM).
- **Festival Activities:** Abhisheka of Lord Varahadeva, chanting *Varaha-kavacha* and *Dasavatara-stotra* (verse 2), and reading *Srimad-Bhagavatam* Canto 3.
- **Noon Parana:** Feast offering presented at noon, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Lord Varahadeva on Varaha Dvadasi to be rescued from the ocean of birth and death (*saṁsāra-sāgara*).

**Pranama Mantra:**
> *vasati śina-śikhare śaśini vimala-kalā*  
> *dharaṇi-dharaṇa-paṭatarasikare*  
> *keśava dhṛta-śūkara-rūpa jaya jagadīśa hare*  
>  
> *"O Keshava! O Lord of the Universe! O Lord Hari who have assumed the form of a Boar! All glories to You! The Earth rests securely upon the tip of Your tusk like a spot on the moon."*
"""
    },
    'Gita': {
        'title': 'Srimad Bhagavad Gita',
        'story': """### Srimad Bhagavad Gita Jayanti: Appearance of the Song Celestial

#### 1. Eternal Identity & Tattva
*Śrīmad Bhagavad-gītā* is the direct sound incarnation (*śabda-brahma*) of Lord Sri Krishna, spoken directly from His lotus mouth (*padmanābhasya mukha-padmād viniḥsṛtā*) to Arjuna at Kurukshetra. It contains the supreme quintessence of all Vedic scriptures (*gītopaniṣado gāvo dogdhā gopāla-nandanaḥ*), presenting 700 divine verses across 18 chapters covering five fundamental truths: *Īśvara* (Supreme Lord), *Jīva* (Living entity), *Prakṛti* (Material nature), *Kāla* (Time), and *Karma* (Action).

---

#### 2. Sacred Pastimes from Mahabharata & Gita Mahatmya

##### Pastime 1: The Battlefield of Kurukshetra & Arjuna's Bewilderment
On the battlefield of Kurukshetra at the dawn of the Mahabharata War, Arjuna instructed Krishna (acting as his chariot driver / *Pārtha-sārathi*) to drive his chariot between the two armies. 

Seeing his grandfathers, teachers, kinsmen, and friends arrayed on both sides, Arjuna's heart broke in material compassion and grief. He dropped his Gandiva bow, wept, and collapsed in his chariot, refusing to fight (*BG 1.46*).

##### Pastime 2: Spoken Directly by Lord Sri Krishna (18 Chapters)
Taking the position of spiritual master (*śiṣyas te 'haṁ śādhi māṁ tvāṁ prapannam* — *BG* 2.7), Lord Sri Krishna spoke the 700 verses of *Bhagavad-gītā*. 

He illuminated the eternal, indestructible nature of the soul (*BG 2.13, 2.20*), the science of selfless action (*Karma-yoga*), spiritual wisdom (*Jñāna-yoga*), and divine devotion (*Bhakti-yoga*). In Chapter 11, Lord Krishna revealed His stupendous **Viśvarūpa** (Universal Form) and four-armed Vasudeva form to Arjuna.

##### Pastime 3: The Supreme Instruction — Total Surrender (BG 18.66)
In the climax of *Bhagavad-gītā* (Chapter 18, verse 66), Lord Sri Krishna delivered the ultimate ultimate instruction (*carama-śloka*):

> *sarva-dharmān parityajya mām ekaṁ śaraṇaṁ vraja*  
> *ahaṁ tvāṁ sarva-pāpebhyo mokṣayiṣyāmi mā śucaḥ*  
>  
> *"Abandon all varieties of religion and just surrender unto Me. I shall deliver you from all sinful reactions. Do not fear."*

##### Pastime 4: The Glories of Bhagavad-gita (Gita Mahatmya)
In the *Varāha Purāṇa*, Lord Shiva reveals to Mother Parvati that one who reads *Bhagavad-gītā* with devotion is cleansed of all past sins (*samudbhavaṁ pāpaṁ naśyati*), as if bathing daily in the sacred Ganges River.

---

#### 3. Spiritual Significance & Observance Guidelines
Gita Jayanti coincides with Mokshada Ekadasi in the month of Margasirsha (December).

- **Observance Activities:** Sequential chanting of all 700 verses of *Bhagavad-gītā*, hosting *Gītā-pārāyaṇa* assemblies, and reading Srila Prabhupada's *Bhagavad-gītā As It Is*.
- **Book Distribution (Gita Dana):** Distributing copies of *Bhagavad-gītā* to homes, schools, libraries, and spiritual seekers around the globe.

---

#### 4. How to Pray & Seek Blessings
Devotees pray on Gita Jayanti for unwavering intelligence (*vyavasāyātmikā buddhiḥ*), total surrender to Krishna's divine will, and empowerment to distribute *Bhagavad-gītā*.

**Invocation & Glories Mantra:**
> *gītā sugītā kartavyā kim anyaiḥ śāstra-vistaraiḥ*  
> *yā svayaṁ padmanābhasya mukha-padmād viniḥsṛtā*  
>  
> *"Bhagavad-gita should be carefully sung and studied. What is the need of reading any other voluminous scriptures, when this song emanated directly from the lotus mouth of the Supreme Lord Padmanabha Himself?"*
"""
    }
}


def populate_avatar_descriptions():
    updated_count = 0
    for key_name, data in AVATAR_STORIES.items():
        observances = CalendarObservance.objects.filter(translations__title__icontains=key_name)
        for obs in observances:
            trans, created = CalendarObservanceTranslation.objects.get_or_create(
                observance=obs,
                language_code='en',
                defaults={
                    'title': obs.title,
                    'description': data['story']
                }
            )
            if not created:
                trans.description = data['story']
                trans.save()
            updated_count += 1
    return updated_count


class Command(BaseCommand):
    help = 'Populate detailed scriptural stories for Divine Avatars & Supreme Lord observances.'

    def handle(self, *args, **options):
        count = populate_avatar_descriptions()
        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated stories for {count} Avatar observances in Vaishnava Calendar.")
        )
