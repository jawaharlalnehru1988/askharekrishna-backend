import logging
from django.core.management.base import BaseCommand
from vaishnava_calendar.models import CalendarObservance, CalendarObservanceTranslation

logger = logging.getLogger(__name__)

ACHARYA_STORIES = {
    'Madhavendra Puri': {
        'title': 'Sri Madhavendra Puri',
        'story': """### Sri Madhavendra Puri: Root of Gaura-Prema

#### 1. Eternal Identity & Lineage
In the Gaudiya Vaishnava lineage, Sri Madhavendra Puri (14th–15th century) is glorified as the **root sprout of the desire tree of devotional love** (*bhakti-kalpataru-mūla*). He was an exalted sannyasi in the Madhva Sampradaya, and the grand-spiritual master (*parama-guru*) of Lord Sri Caitanya Mahaprabhu (initiator of Sri Advaita Acarya, Lord Nityananda Prabhu, and Sri Ishvara Puri). He introduced the confidential mood of **Vrajabhava / Madhurya-rasa** into the Brahma-Madhva Sampradaya.

---

#### 2. Sacred Pastimes from Sri Caitanya-caritamrta (Madhya Lila 4)

##### Pastime 1: Unearthing Sri Gopala at Govardhana Hill
While circumambulating Govardhana Hill, Madhavendra Puri rested under a tree near Govinda Kunda. A young cowherd boy brought him a pot of milk, saying: *"Nobody starves in My village."* 

That night, the boy appeared in a dream, revealed Himself as **Sri Gopala**, and said: *"I am buried under a thicket of bushes on top of Govardhana Hill. Please excavate Me and install Me atop the hill!"* Madhavendra Puri excavated the ancient Deity of Lord Gopala (Sri Nathji) and celebrated a colossal **Annakuta festival**, feeding thousands of villagers.

##### Pastime 2: Walking 1,000 Miles for Sandalwood
Sri Gopala appeared in a dream to Madhavendra Puri, complaining of burning heat and requesting cool sandalwood pulp (*candana*) from the Malaya hills in Jagannath Puri. 

Despite advanced old age, Madhavendra Puri walked barefoot over 1,000 miles from Vrindavan to Jagannath Puri to fetch the sandalwood for his Beloved Lord!

##### Pastime 3: Lord Gopinatha Stealing Sweet Rice (Kshira-Chora Gopinatha at Remuna)
Stopping at the Gopinatha Temple in Remuna (Odisha), Madhavendra Puri saw twelve pots of condensed sweet rice (*amṛta-keli kṣīra*) offered to the Lord. He thought: *"If I could taste a tiny drop of this sweet rice, I could offer sweet rice to my Gopala in Vrindavan."* Instantly feeling ashamed of desiring food before it was offered, he left to sleep in the vacant marketplace. 

That night, Lord Gopinatha stole a pot of sweet rice, hid it under His garment, and instructed the priest in a dream: *"Wake up! Take this pot of sweet rice hidden under My skirt and give it to My devotee Madhavendra Puri!"* From that day, the Lord became famous as **Kṣīra-corā Gopīnātha**.

##### Pastime 4: The Ultimate Sloka of Separation (Ayikheta-Dinadayana)
On his deathbed, Sri Madhavendra Puri continuously recited the ultimate verse of separation (*vipralambha-bhāva*), weeping floods of ecstatic tears:
> *ayi dīna-dayārdranātha he mathurānātha kadāvalokyase*  
> *hṛdayaṁ tvad-aloka-kātaraṁ dayita bhrāmyati kiṁ karomy aham*  
>  
> *"O My Lord! O compassionate Master of Mathura! When will I see You? My heart is broken in separation without Your sight. O Beloved, my mind wanders in agony! What shall I do now?"*

---

#### 3. Spiritual Significance & Observance Guidelines
Sri Madhavendra Puri planted the seed of pure conjugal love of Godhead that bloomed in Lord Sri Caitanya Mahaprabhu.

- **Fasting Rules:** Fasting is observed until noon (12:00 PM).
- **Festival Activities:** Reading *Caitanya-caritamrta* Madhya Lila Chapter 4, offering sweet rice (*kṣīra*), sandalwood pulp (*candana*), and singing devotional kirtana.
- **Noon Parana:** Feast offering presented at noon, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Sri Madhavendra Puri on his Disappearance day for unalloyed devotion and a drop of *vipralambha-bhāva*.

**Pranama Mantra:**
> *namo gaura-prema-mūlāya mādhavendra-purī-bhūte*  
> *kṣīra-chora-gopīnātha-kṛpā-pātrāya te namaḥ*  
>  
> *"I offer my respectful obeisances unto Sri Madhavendra Puri, the root of Gaura-prema and the favored recipient of Sri Kshira-Chora Gopinatha's mercy."*
"""
    },
    'Ramanuja': {
        'title': 'Sri Ramanujacarya',
        'story': """### Sri Ramanujacarya: Incarnation of Ananta Shesha & Founder of Sri Sampradaya

#### 1. Eternal Identity & Lineage
Sri Ramanujacarya (1017–1137 CE) is recognized as an incarnation of **Ananta Shesha** (and Lakshmana). He is the founder-acharya of the **Śrī Sampradāya** (*Viśiṣṭādvaita-vāda* / Qualified Non-Dualism). Born in Sriperumbudur (Tamil Nadu) to Kesava Somayaji and Kantimathi, he dedicated his life to establishing Lord Sriman Narayana and Goddess Lakshmi as the Supreme Absolute Truth across Bharatvarsha.

---

#### 2. Sacred Pastimes from Prapannamrtam & Sri Sampradaya History

##### Pastime 1: Shouting the Secret Mantra from the Temple Tower (Tirukostiyur)
Ramanujacarya walked 18 times on foot to Tirukostiyur to receive initiation into the sacred 8-syllable mantra (*oṁ namo nārāyaṇāya*) from Gosthipurna. 

Gosthipurna strictly warned him: *"If you reveal this mantra to anyone, you will suffer in hell!"* 

Instantly, out of boundless compassion for suffering souls, Ramanujacarya climbed atop the high gate-tower (*gopuram*) of the Tirukostiyur Vishnu Temple, called out to all men, women, and children of the village, and loudly chanted the **Om Namo Narayanaya** mantra for everyone to hear! When Gosthipurna confronted him in anger, Ramanujacarya bowed and said: *"If my going to hell saves millions of souls, I accept hell gladly!"* Gosthipurna wept, embraced Ramanujacarya, and named him **Emberumanar** ("our superior Lord").

##### Pastime 2: Defeating Impersonalists & Reclaiming Sacred Temples
Ramanujacarya systematically defeated Mayavada impersonalists in philosophical debates throughout South India. He renovated and established the rigorous Deity worship standards at **Sri Ranganathaswamy Temple** in Sri Rangam, **Tirumala Venkateswara Temple** in Tirupati, and **Kanchipuram**.

##### Pastime 3: Recovering the Cheluvanarayana Swamy Deity at Melkote
When religious persecution forced Ramanujacarya to move to Melkote (Karnataka), he discovered the lost Deity of **Sri Cheluvanarayana Swamy**. 

Learning that the processional Deity (*Utsava-murti* Sampat Kumara) was kept in the palace of the Sultan of Delhi, 80-year-old Ramanujacarya traveled all the way to Delhi. 

When he stood in the Sultan's court and called: *"Come to me, My child!"*, the golden Deity of Sampat Kumara walked out of the Princess's room and sat in Ramanujacarya's lap!

##### Pastime 4: Writing the Sri Bhasya
Fulfilling his vow to Yamunacarya, Ramanujacarya authored the **Śrī-bhāṣya**, the monumental commentary on the *Brahma-sūtras*, refuting Shankara's Mayavada and establishing pure devotion to Sriman Narayana.

---

#### 3. Major Literary Contributions
- **Śrī-bhāṣya:** Monumental commentary on Vedanta-sutras.
- **Gītā-bhāṣya, Vedārtha-saṅgraha, Vedānta-dīpa, Vedānta-sāra, Saranagati Gadyam.**

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Sri Ramanujacarya on his Appearance day (Chaitra Sukla Shashthi) for absolute surrender to Sriman Narayana (*śaraṇāgati*) and Vaishnava compassion.

**Pranama Mantra:**
> *yo nityam acyuta-padāmbuja-yugma-rukma-*  
> *vyāmohatas tad-iterāṇi tṛṇāya mene*  
> *asmad-guroḥ bhagavato 'sya dayaika-sindhoḥ*  
> *rāmānujasya caraṇau śaraṇaṁ prapadye*  
>  
> *"I take shelter at the lotus feet of our spiritual master, Sri Ramanujacarya, an ocean of mercy who deemed everything other than the lotus feet of the infallible Lord Acyuta to be like dry straw."*
"""
    },
    'Nimbarka': {
        'title': 'Sri Nimbarkacarya',
        'story': """### Sri Nimbarkacarya: Incarnation of Sudarshana Chakra & Founder of Nimbarka Sampradaya

#### 1. Eternal Identity & Lineage
Sri Nimbarkacarya (11th–12th century CE) is recognized as the incarnation of **Sudarshana Chakra** (the divine discus of Lord Vishnu). He is the founder-acharya of the **Nimbārka Sampradāya** (Kumāra Sampradāya / *Dvaitādvaita-vāda* — Dualistic Non-Dualism). Born in Vaiduryapattanam (Nimbapuri, Andhra Pradesh) to Aruni Rishi and Jayanti Devi, he established his main ashram at Neemgaon (Govardhan, Vrindavan).

---

#### 2. Sacred Pastimes from Nimbarka Charitamrta & Vaishnava History

##### Pastime 1: Stopping the Sun on the Neem Tree (Origin of the Name Nimbarka)
While living at his ashram near Govardhana, an ascetic follower of Brahma visited Nimbarkacarya (then known as Niyamananda). They discussed philosophy until sunset. Nimbarkacarya invited the ascetic for dinner, but the ascetic declined, saying: *"I am a strict renunciate who never eats after sunset."* 

Distressed that a guest would leave his ashram unfed, Niyamananda placed a portion of his spiritual radiance onto a **Neem tree** (*nimba*), causing the glowing sun (*arka*) to reappear and remain frozen above the Neem tree until the guest finished his evening meal! From that miraculous day, he was glorified as **Nimbārka** ("the one who brought the sun onto the Neem tree").

##### Pastime 2: Direct Initiation from Sanat-Kumara
Nimbarkacarya received direct transcendental knowledge and initiation into the Radha-Krishna Yugala mantra from **Sanat-Kumara** (one of the Four Kumaras), tracing the lineage back to Lord Hansa (the Swan incarnation of Lord Vishnu).

##### Pastime 3: Establishing Radha-Krishna Yugala-Upasana
Centuries before other Acharyas in Vrindavan, Sri Nimbarkacarya was the pioneer who formally established the supreme worship of **Sri Radha and Sri Krishna together** (*Yugala-Upāsanā*) as the inseparable Absolute Truth, declaring Srimati Radharani to be the eternal consort and supreme potency of Sri Krishna.

##### Pastime 4: Writing the Vedanta-Parijata-Saurabha
Authoring his famous commentary on the *Brahma-sūtras* titled **Vedānta-Pārijāta-Saurabha**, Sri Nimbarkacarya established *Dvaitādvaita* (simultaneous duality and non-duality), refuting Mayavada impersonaliasm and proving that individual souls (*jīvas*) are eternally distinct yet qualitatively one with Supreme Lord Krishna.

---

#### 3. Major Literary Contributions
- **Vedānta-Pārijāta-Saurabha:** Masterpiece commentary on Vedanta-sutras.
- **Daśa-ślokī:** Ten nectarine verses on Radha-Krishna worship.
- **Rādha-aṣṭakam** and **Kṛṣṇa-stotram**.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Sri Nimbarkacarya on Kartika Purnima for unwavering devotion to Sri Radha-Krishna Yugala and freedom from philosophical illusion.

**Pranama Mantra:**
> *namo 'stu nimbārkāya sudarśanāvtāriṇe*  
> *rādhā-kṛṣṇa-yugala-bhakti-pradāyine mahātmane*  
>  
> *"I offer my respectful obeisances unto Sri Nimbarkacarya, the incarnation of Sudarshana Chakra, who bestowed the supreme worship of Sri Radha-Krishna Yugala upon the world."*
"""
    },
    'Jagannatha Dasa Babaji': {
        'title': 'Srila Jagannatha Dasa Babaji',
        'story': """### Srila Jagannatha Dasa Babaji: Pitamaha of Gaudiya Vaishnavas

#### 1. Eternal Identity & Lineage
Srila Jagannatha Dasa Babaji Maharaj (1776–1894 CE) is revered throughout the Gaudiya sampradaya as **Vaiṣṇava-sārvabhauma** and **Pitāmaha** (Grandfather) of all Gaudiya Vaishnavas. Living for over 120 years, he served as the *śikṣā-guru* of Srila Bhaktivinoda Thakura and *parama-guru* of Srila Bhaktisiddhanta Sarasvati Thakura.

---

#### 2. Sacred Pastimes from Gaudiya History & Life of Bhaktivinoda Thakura

##### Pastime 1: Identifying the Birthplace of Lord Caitanya (Yoga-Pitha, Mayapur)
In 1888, when Srila Bhaktivinoda Thakura discovered the ancient site of Yoga-Pitha in Mayapur, he requested Babaji Maharaj (then 112 years old and unable to walk, carried in a wicker basket by his disciple Bihari) to verify the location. 

The moment the basket touched the soil of Yoga-Pitha, Babaji Maharaj, though frail and bent with age, leaped high into the air out of his basket and danced in weeping ecstasy, shouting: *"Ei to Nimāi Janma-bhūmi!"* ("This indeed is the divine birthplace of Lord Nimai!"). His ecstasy confirmed the authenticity of Mayapur Yoga-Pitha.

##### Pastime 2: Living in a Wicker Basket at Surya Kunda
In Vrindavan, Babaji Maharaj resided at Surya Kunda performing intense bhayana. Because of extreme old age, his eyelids drooped over his eyes, requiring him to lift his eyelids with his fingers to see. He lived inside a small bamboo wicker basket (*jhāḍā*), absorbed 24 hours a day in Harinama.

##### Pastime 3: Feeding the Monkeys of Vrindavan
While living at Vrindavan, wild monkeys would jump into his hut and eat his offered prasadam. Disciples tried to drive the monkeys away, but Babaji Maharaj stopped them, saying: *"Do not disturb the sacred residents of Vraja! These monkeys are exalted associates of Lord Ramacandra and Sri Krishna."* He personally shared his daily prasadam with them.

##### Pastime 4: Directing Bhaktivinoda Thakura's Preaching Mission
Babaji Maharaj gave direct spiritual direction to Srila Bhaktivinoda Thakura, commanding him to build a temple at Yoga-Pitha Mayapur and publish Vaishnava literature for worldwide distribution.

---

#### 3. Spiritual Significance & Observance Guidelines
Srila Jagannatha Dasa Babaji exemplifies absolute absorption in Harinama and veneration of the Holy Dham.

- **Fasting Rules:** Fasting is observed until noon (12:00 PM).
- **Festival Activities:** Reading pastimes of Srila Jagannatha Dasa Babaji, chanting extra rounds of Harinama, and offering prasadam.
- **Noon Parana:** Feast offering presented at noon, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Jagannatha Dasa Babaji on his Disappearance day for unyielding faith in Navadvipa-Mayapur Dham and pure Harinama.

**Pranama Mantra:**
> *gaurāvirbhāva-bhūmes tvaṁ nirdeṣṭā saj-janapriyaḥ*  
> *vaiṣṇava-sārvabhaumaḥ śrī-jagannāthāya te namaḥ*  
>  
> *"I offer my respectful obeisances unto Srila Jagannatha Dasa Babaji Maharaja, the monarch among Vaishnavas (*Vaiṣṇava-sārvabhauma*), who revealed the authentic birthplace of Lord Gauranga."*
"""
    },
    'Gaura Kisora': {
        'title': 'Srila Gaura Kishora Dasa Babaji',
        'story': """### Srila Gaura Kishora Dasa Babaji: Incarnation of Guna Manjari

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srila Gaura Kishora Dasa Babaji (1846–1915 CE) is **Guna Manjari**. Born in Tepakhola (Faridpur, Bangladesh) into a merchant family, he received *babaji-vesha* from Srila Bhagavata Dasa Babaji (disciple of Srila Jagannatha Dasa Babaji). He was the direct initiating spiritual master (*dīkṣā-guru*) of **Srila Bhaktisiddhanta Sarasvati Thakura**.

---

#### 2. Sacred Pastimes from Life of Srila Bhaktisiddhanta Sarasvati & Gaudiya History

##### Pastime 1: Extreme Renunciation & Hiding in Abandoned Latrines
Living in Navadvipa and Vrindavan, Babaji Maharaj wore cast-away cloths from cremation grounds, washed them in Ganges water, and tied knot-beads to count his Holy Names. 

To escape insincere materialists seeking wealth blessings, Babaji Maharaj spent nights inside abandoned public latrines, chanting Harinama uninterruptedly! When visitors complained about the foul smell, Babaji replied: *"The scent of worldly fame (*pratiṣṭhā*) is millions of times fouler than nightsoil!"*

##### Pastime 2: The Fasting Test for Bimal Prasad (Srila Bhaktisiddhanta)
Srila Bhaktivinoda Thakura sent his brilliant scholar son Bimal Prasad (later Srila Bhaktisiddhanta Sarasvati) to take initiation from Babaji Maharaj. Babaji initially refused, saying: *"I am an illiterate, foolish old man. How can I initiate a scholar?"* 

Bimal Prasad returned to his room, locked the door, and began fasting unto death, declaring: *"If Babaji Maharaj does not initiate me, I shall give up my life!"* Seeing his absolute determination, Babaji Maharaj embraced Bimal Prasad, placed his lotus feet upon his head, and gave him *dīkṣā*.

##### Pastime 3: Rejecting Material Wealth
A wealthy zamindar offered to build a grand stone temple for Babaji Maharaj. Babaji Maharaj replied: *"If you truly wish to serve me, give me your palace and money, and live here under a tree with a rag around your waist!"* The zamindar fled, realizing Babaji's unyielding renunciation.

##### Pastime 4: Glorious Samadhi at Navadvipa
When Babaji Maharaj entered Samadhi on Utthan Ekadasi in 1915, rival babajis fought to claim his body for public fundraising. Srila Bhaktisiddhanta Sarasvati stood firm as a celibate *brahmacari*, declaring: *"Only one who has never committed any immoral act in his life may touch Babaji Maharaj's body!"* Everyone stepped back in awe. Srila Bhaktisiddhanta personally carried his guru's body across the Ganges and placed him in Samadhi at Sri Mayapur Yoga-Pitha!

---

#### 3. Spiritual Significance & Observance Guidelines
Srila Gaura Kishora Dasa Babaji is renunciation personified (*sakṣād-vairāgya-mūrti*).

- **Fasting Rules:** Fasting is observed on Utthan Ekadasi (complete fast from grains).
- **Festival Activities:** Reading *Life of Srila Gaura Kishora Dasa Babaji*, chanting extra rounds of Harinama, and studying *Upadeśāmṛta*.
- **Dwadasi Parana:** Taking *prasādam* break-fast on Dwadasi morning.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Gaura Kishora Dasa Babaji on his Disappearance day for complete freedom from desire for fame (*pratiṣṭhā*) and pure attraction to Harinama.

**Pranama Mantra:**
> *namo gaura-kiśorāya sakṣād-vairāgya-mūrtaye*  
> *vipralambha-rasāmbhodhe pādāmbhojāya te namaḥ*  
>  
> *"I offer my respectful obeisances unto Srila Gaura Kishora Dasa Babaji Maharaja, who is renunciation personified (*sakṣād-vairāgya-mūrti*) and an ocean of vipralambha-rasa."*
"""
    },
    'Visvanatha Cakravarti': {
        'title': 'Srila Visvanatha Cakravarti Thakura',
        'story': """### Srila Visvanatha Cakravarti Thakura: Vinoda Manjari & King of Vaishnava Poets

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srila Visvanatha Cakravarti Thakura (1626–1708 CE) is **Vinoda Manjari**. Born in Devagrama (Nadia, Bengal) into a Rarhiya Brahmana family, he was initiated by Sri Radha-Ramana Dasa (disciple of Sri Rasikananda). He lived at Radha-kunda and the Sri Sri Radha-Gokulananda Temple in Vrindavan. He is revered as the king (*Cakravartī*) of Gaudiya poets and philosophers, author of **Śrī Śrī Gurv-aṣṭakam** and **Sārārtha-Darśinī**.

---

#### 2. Sacred Pastimes from Gaudiya History & Bhakti-ratnakara

##### Pastime 1: Composing the Sri Sri Gurvashtakam
While absorbed in deep meditation on his guru and the Six Gosvamis at Radha-kunda, Srila Visvanatha Cakravarti Thakura composed the world-famous eight-verse prayer **Śrī Śrī Gurv-aṣṭakam** (*saṁsāra-dāvānala-liḍha-loka-trāṇāya kāruṇya-ghanāghanatvam...*). This prayer is sung every single morning at Mangala Arati in temples worldwide!

##### Pastime 2: Defeating the Opponents of Parakiya-rasa at Jaipur
When scholars in Jaipur challenged the authenticity of *Parakīyā-rasa* (conjugal love in paramour mood) and questioned the lineage of Gaudiya Vaishnavism, Srila Visvanatha Cakravarti (in extreme old age) dispatched his brilliant young student **Srila Baladeva Vidyabhushana** to Jaipur to present the arguments and compose the *Govinda-bhāṣya*.

##### Pastime 3: Srimati Radharani Protecting Him from Assassins
Furious at Visvanatha's unbending refutation of non-bona-fide sects, an envious gang hired assassins to kill him in the dark forests of Radha-kunda. 

As the assassins approached him in the dark, they suddenly saw a four-year-old girl (Srimati Radharani) protecting Visvanatha with glowing light and holding a fierce trident. The assassins fell at Visvanatha's feet, confessed their plot, and surrendered as his disciples!

##### Pastime 4: Writing the Sarartha-Darsini Commentary
Sitting at the Radha-Gokulananda Temple in Vrindavan, Visvanatha wrote **Sārārtha-Darśinī**, his sublime Sanskrit commentary on *Śrīmad-Bhāgavatam*, elucidating the Tenth Canto Vraja-lila with unmatched sweet poetic realization.

---

#### 3. Major Literary Contributions
- **Śrī Śrī Gurv-aṣṭakam:** The universal eight prayers to the Spiritual Master.
- **Sārārtha-Darśinī:** Sanskrit commentary on *Śrīmad-Bhāgavatam*.
- **Mādhurya-kādambinī:** The step-by-step ladder of devotional progress (*Śraddhā* to *Prema*).
- **Bhakti-rasāmṛta-sindhu-bindu**, **Ujjvala-nīlamaṇi-kiraṇa**, **Caitanya-caritāmṛta-ṭīkā**.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Visvanatha Cakravarti Thakura on his Disappearance day for unwavering faith in the Spiritual Master (*guru-nisṭhā*) and relish of Bhagavata-rasa.

**Pranama Mantra:**
> *namo bhakti-vinodāya śrī-visvanātha-rūpiṇe*  
> *vinoda-mañjarī-dhāmne gaura-bhakti-pradāyine*  
>  
> *"I offer my respectful obeisances unto Srila Visvanatha Cakravarti Thakura, who is Vinoda Manjari in Vraja-lila, the crown jewel of scholars, and the author of Sri Gurvashtakam."*
"""
    },
    'Baladeva Vidyabhusana': {
        'title': 'Srila Baladeva Vidyabhushana',
        'story': """### Srila Baladeva Vidyabhushana: Vedanta-Acharya of Gaudiya Sampradaya

#### 1. Eternal Identity & Lineage
Srila Baladeva Vidyabhushana (1700–1768 CE) is glorified as the **Vedāntācārya** of the Gaudiya Vaishnava Sampradaya. Born in Remuna (Balasore, Odisha), he studied Nyaya and Vedanta in Mysore and accepted Madhva sannyasa. Later, he surrendered at the lotus feet of Srila Visvanatha Cakravarti Thakura in Vrindavan, becoming his foremost disciple.

---

#### 2. Sacred Pastimes from Gaudiya History & Vedanta-Pith

##### Pastime 1: The Historical Jaipur Debate & Sri Govinda-bhasya (1718 CE)
Scholars in the Galta assembly at Jaipur challenged the Gaudiya Vaishnavas, claiming: *"You do not have your own commentary on the Brahma-sūtras! Therefore, you are not an authentic Vedantic sampradaya, and your Deity Sri Govindaji cannot be worshiped with Srimati Radharani!"* 

Dispatched by Srila Visvanatha Cakravarti Thakura, young Baladeva Vidyabhushana arrived at Galta Jaipur, declaring: *"Lord Caitanya Mahaprabhu accepted Srimad-Bhagavatam as the natural commentary on Brahma-sutras. But I shall write a direct commentary under Sri Govindaji's command!"*

##### Pastime 2: Direct Dictation by Sri Govindaji in a Dream
Prone before the Deity of **Sri Govindaji** in Jaipur, Baladeva prayed for guidance. Sri Govindaji appeared in his dream, embraced him, and said: *"Write the commentary! I shall dictate every word into your heart!"* 

Within a few days, Baladeva authored the flawless commentary on all four chapters of Vedanta-sutras. He named it **Śrī Govinda-bhāṣya** ("The commentary authored by Sri Govindaji Himself").

##### Pastime 3: Conquering the Jaipur Scholars & Awarded 'Vidyabhushana'
When Baladeva presented the *Govinda-bhāṣya* in the royal assembly, all scholars were stunned by its logical brilliance and devotion. They unanimously conferred upon him the title **Vidyābhūṣaṇa** ("one whose ornament is knowledge") and acknowledged Gaudiya Vaishnavism as the authentic fifth Vaishnava sampradaya!

##### Pastime 4: Protecting the Worship of Sri Sri Radha-Govindaji
Through his victory, the worship of Sri Govindaji along with Srimati Radharani was permanently restored and glorified across Bharatvarsha.

---

#### 3. Major Literary Contributions
- **Śrī Govinda-bhāṣya:** The definitive Gaudiya commentary on *Brahma-sūtras*.
- **Prameya-ratnāvalī:** Nine fundamental truths (*nava-prameya*) of Gaudiya theology.
- **Siddhānta-ratnam**, **Kāvya-kaustubha**, and commentaries on *Srimad-Bhagavatam*, *Bhagavad-gita*, and *Tattva-Sandarbha*.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Baladeva Vidyabhushana on his Disappearance day for deep intellectual clarity, mastery of Vedantic philosophy, and unswerving devotion to Sri Govindaji.

**Pranama Mantra:**
> *namo baladevāya vidyābhūṣaṇa-saṁjñine*  
> *govinda-bhāṣya-kāreṇa caitanya-mata-sthāpine*  
>  
> *"I offer my respectful obeisances unto Srila Baladeva Vidyabhushana, who established the doctrine of Lord Caitanya across the world by writing the divine Govinda-bhasya commentary."*
"""
    }
}


def populate_acharyas_descriptions():
    updated_count = 0
    for key_name, data in ACHARYA_STORIES.items():
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
    help = 'Populate detailed scriptural stories for Revered Acharyas observances.'

    def handle(self, *args, **options):
        count = populate_acharyas_descriptions()
        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated stories for {count} Acharya observances in Vaishnava Calendar.")
        )
