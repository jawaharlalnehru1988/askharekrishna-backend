import logging
from django.core.management.base import BaseCommand
from vaishnava_calendar.models import CalendarObservance, CalendarObservanceTranslation

logger = logging.getLogger(__name__)

GOSVAMI_STORIES = {
    'Rupa Gosvami': {
        'title': 'Srila Rupa Gosvami',
        'story': """### Srila Rupa Gosvami: Rupa Manjari & Bhakti-Rasa-Acharya

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srila Rupa Gosvami (1489–1564 CE) is **Rupa Manjari**, the leader of all maidservants of Srimati Radharani (*śrī-rūpa-mañjarī-pada, sei mora sampada*). He is glorified as the **Bhakti-Rasa-Acharya**—the foundational architect of Gaudiya Vaishnava theology. Born in Ramakeli (Bengal) into a high Sarasvata brahmana lineage as Dabir Khas (Prime Minister under Nawab Hussain Shah), he surrendered at the lotus feet of Lord Caitanya Mahaprabhu at Prayagraj.

---

#### 2. Sacred Pastimes from Sri Caitanya-caritamrta (Madhya 19 & Antya Lila)

##### Pastime 1: Ten Days of Divine Instruction at Prayagraj (Dasasvamedha Ghat)
At Dasasvamedha Ghat in Prayagraj, Lord Caitanya Mahaprabhu empowered Srila Rupa Gosvami for ten consecutive days, infusing His divine potency into Rupa's heart (*hṛdi rūpe brahma-vidyā-sukha-dā*). 

Mahaprabhu taught Rupa Gosvami the entire science of *Bhakti-rasa*, comparing the spirit soul to an infinitesimal particle wandering the universe, and describing the growth of the devotional creeper (*bhakti-latā-bīja*).

##### Pastime 2: Unearthing Sri Govindadeva on Gomati Tila
Fulfilling Lord Caitanya's order to rediscover lost holy places in Vrindavan, Srila Rupa Gosvami searched intensely for the lost Deity of **Sri Govindadev**. 

A beautiful cowherd boy appeared and led Rupa Gosvami to Gomati Tila, saying: *"A cow comes here every afternoon and bathes this hillock in milk. Your lost Deity is buried underneath!"* Rupa Gosvami excavated Gomati Tila and revealed the breathtaking self-manifested Deity of Sri Govindadev!

##### Pastime 3: Composing Vidagdha-Madhava & Lalita-Madhava
In Jagannath Puri, Srila Rupa Gosvami read his Sanskrit dramas *Vidagdha-Mādhava* and *Lalitā-Mādhava* before Lord Caitanya, Svarupa Damodara, and Ramananda Raya. 

Hearing Rupa's poetic verses describing Srimati Radharani's love in separation, Lord Caitanya wept in ecstasy, and Ramananda Raya declared: *"Rupa's poetry is not composed by human intellect; it is the direct sound representation of Mahaprabhu's own heart!"*

##### Pastime 4: Srimati Radharani Cooks Sweet Rice for Sanatana
When Srila Sanatana Gosvami wished to feed Rupa Gosvami sweet rice (*kṣīra*), Rupa Gosvami felt sad that he had no ingredients in his hut. 

Srimati Radharani disguised Herself as a young gopi maiden, brought rice, milk, and sugar to Rupa's hut, and instructed him to cook. When Sanatana ate the sweet rice, he swooned in divine ecstasy, realizing that Srimati Radharani Herself had supplied the ingredients!

---

#### 3. Major Literary Contributions
- **Bhakti-rasāmṛta-sindhu:** The definitive encyclopedia of devotional service (translated as *The Nectar of Devotion*).
- **Ujjvala-nīlamaṇi:** The science of *mādhurya-rasa* and Srimati Radharani's *Mahābhāva*.
- **Upadeśāmṛta:** Eleven foundational verses of instruction for all practitioners (*The Nectar of Instruction*).
- **Laghu-bhāgavatāmṛta, Padyāvalī, Stavamālā, Vidagdha-Mādhava, Lalitā-Mādhava.**

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Rupa Gosvami on his Disappearance day (Sravana Purnima) for shelter under his lotus feet (*rūpānuga-bhakti*), purity of intention, and relish of *Bhagavata-rasa*.

**Pranama Mantras:**
> *śrī-caitanya-mano-'bhīṣṭaṁ sthāpitaṁ yena bhū-tale*  
> *svayaṁ rūpaḥ kadā mahyaṁ dadāti sva-padāntikam*  
>  
> *"When will Srila Rupa Gosvami Prabhupada, who has established within this material world the desire of Lord Caitanya's heart, give me shelter under his lotus feet?"*
"""
    },
    'Sanatana Gosvami': {
        'title': 'Srila Sanatana Gosvami',
        'story': """### Srila Sanatana Gosvami: Lavanga Manjari & Sambandha-Acharya

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srila Sanatana Gosvami (1488–1558 CE) is **Lavanga Manjari** (and Rati Manjari). He is glorified as the **Sambandha-Acharya**—the senior-most Vrindavan Gosvami who establishes our eternal relationship with Sri Madana-Mohana and Lord Krishna. Born in Ramakeli as Sakara Mallik (Finance Minister under Nawab Hussain Shah), he escaped prison to surrender at Lord Caitanya Mahaprabhu's lotus feet at Varanasi.

---

#### 2. Sacred Pastimes from Sri Caitanya-caritamrta (Madhya 20–25)

##### Pastime 1: Two Months of Divine Instruction at Varanasi (Sambandha-tattva)
At Varanasi, Lord Caitanya instructed Srila Sanatana Gosvami for two solid months, revealing the absolute science of *Jīva-tattva*, *Sambandha-tattva*, *Bhakti-yoga*, and explaining the confidential meanings of the *Ātmārāma* verse (SB 1.7.10) in 61 different ways!

##### Pastime 2: Installing Sri Madana-Mohana & The Salt Bread Pastime
While wandering in Vrindavan, Srila Sanatana Gosvami discovered the self-manifested Deity of **Sri Madana-Mohana** kept by a poor brahmana in Mathura. Sanatana installed Him atop Dvadasaditya Tila near the Yamuna. 

When Sanatana offered dry baked bread without salt, Madana-Mohana playfully demanded: *"Sanatana! At least give Me some salt with this dry bread!"* Sanatana replied: *"O Lord, today You ask for salt, tomorrow You will ask for sweetmeats! Where will this poor beggar get it?"* Later, a wealthy merchant Ramadasa Kapoor's stranded salt boat was freed by Sanatana's blessing, and the merchant built the magnificent Madana-Mohana Temple!

##### Pastime 3: Govardhana Parikrama & Lord Krishna's Footprint Sila
Even in advanced old age, Srila Sanatana Gosvami performed daily **24-mile Parikrama around Govardhana Hill**. 

Seeing His elderly servant sweating and exhausted, Lord Krishna appeared as a young cowherd boy, stood on a Govardhana-sila, played His flute, and pressed His lotus footprint into the stone. Handing the **Govardhana-sila with Krishna's footprint** to Sanatana, Krishna said: *"Baba! Circumambulating this single Sila four times equals circumambulating all of Govardhana Hill!"*

##### Pastime 4: Converting the Mayavadi Sannyasis of Varanasi
Through Sanatana Gosvami's deep humility and Lord Caitanya's divine potency, thousands of Mayavadi sannyasis of Varanasi led by Prakasananda Sarasvati surrendered at Lord Caitanya's lotus feet.

---

#### 3. Major Literary Contributions
- **Bṛhad-bhāgavatāmṛta:** The supreme spiritual epic detailing Gopa-kumara's journey across cosmic realms to Goloka Vrindavan.
- **Hari-bhakti-vilāsa:** The comprehensive guidebook of Vaishnava rituals, Deity worship, and daily conduct (*sada-ācāra*).
- **Bṛhad-vaiṣṇava-toṣaṇī:** The deep Sanskrit commentary on the Tenth Canto of Srimad-Bhagavatam.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Sanatana Gosvami on Guru Purnima (Ashadha Purnima) for firm establishing of *sambandha-jñāna* and shelter under Sri Madana-Mohana.

**Pranama Mantra:**
> *vande rūpa-sanātanau raghu-yugau śrī-jīva-gopālakau*  
> *sanātana-samīkṣante madanecchā-vaśaṁ gataḥ*  
>  
> *"I offer my respectful obeisances unto Srila Sanatana Gosvami, the Sambandha-Acharya, who binds us eternally to the lotus feet of Sri Madana-Mohana."*
"""
    },
    'Jiva Gosvami': {
        'title': 'Srila Jiva Gosvami',
        'story': """### Srila Jiva Gosvami: Vilasa Manjari & Tattva-Acharya

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srila Jiva Gosvami (1513–1598 CE) is **Vilasa Manjari**. He is glorified as the **Tattva-Acharya**—the unmatched philosophical genius who systematically formulated **Acintya-Bhedābheda-Tattva** (inconceivable simultaneous oneness and difference). He was the nephew of Srila Rupa Gosvami and Srila Sanatana Gosvami (son of Anupama/Vallabha).

---

#### 2. Sacred Pastimes from Sri Caitanya-caritamrta & Bhakti-ratnakara

##### Pastime 1: Vision of Lord Nityananda at Navadvipa
As a young boy in Bakla Chandradvip, Jiva dreamed of Lord Caitanya dancing. Leaving home for Navadvipa, he met **Lord Nityananda Prabhu**, who placed His lotus feet upon Jiva's head, toured Navadvipa Dham with him, and commanded him: *"Go to Varanasi to study Sanskrit grammar, and then reside under Rupa and Sanatana in Vrindavan!"*

##### Pastime 2: Defeating Rupa Narayana & Sanatana's Chastisement
An arrogant scholar named Rupa Narayana came to Vrindavan demanding a debate victory certificate from Rupa and Sanatana, who signed it without argument. 

Young Jiva Gosvami, unable to tolerate an arrogant scholar disrespecting his gurus, challenged Rupa Narayana on the banks of the Yamuna and thoroughly defeated him in Sanskrit logic! 

When Sanatana Gosvami learned that Jiva had shown a trace of pride, Sanatana banished Jiva from Vrindavan. Jiva fasted in a crocodile-infested cave at Nanda Ghat until Rupa Gosvami interceded, bringing Jiva back to Radha-Damodara.

##### Pastime 3: Serving Sri Sri Radha-Damodara & Writing the Sat-Sandarbhas
Srila Rupa Gosvami personally carved and gifted the Deity of **Sri Sri Radha-Damodara** to Jiva Gosvami. At the Radha-Damodara Temple in Vrindavan, Jiva Gosvami spent decades authoring the **Ṣaṭ-Sandarbhas**, defining the absolute philosophy of Gaudiya Vaishnavism.

##### Pastime 4: Dispatching the First Book Distribution Caravan to Bengal
Recognizing the urgent need to spread the Gosvamis' writings across India, Srila Jiva Gosvami organized a bullock-cart caravan carrying all manuscripts of the Six Gosvamis. He dispatched his top three brilliant disciples—**Srinivasa Acarya, Narottama Dasa Thakura, and Syamananda Prabhu**—to carry these sacred texts to Bengal and Odisha!

---

#### 3. Major Literary Contributions
- **Ṣaṭ-Sandarbhas:** The six philosophical treatises (Tattva, Bhagavata, Paramatma, Krishna, Bhakti, and Priti Sandarbha).
- **Gopāla-campū:** Epic poetic narration of Lord Krishna's Vraja and Dvaraka pastimes.
- **Harināmāmṛta-vyākaraṇa:** Sanskrit grammar taught entirely through Krishna's Holy Names.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Jiva Gosvami on his Disappearance day (Pausha Tritiya) for philosophical clarity, allegiance to Gaudiya *siddhānta*, and service to Sri Sri Radha-Damodara.

**Pranama Mantra:**
> *nāma-śreṣṭhaṁ manu-mapi śacī-putram atra svarūpaṁ*  
> *rūpaṁ tasyāgrajam uru-purīṁ māthurīṁ goṣṭhavāṭīm*  
> *kṛṣṇākhyāṁ tat-prakaṭa-saraḥ rādhikā-kuṇḍam etāt*  
> *gīrvāṇābhir drakṣyati yaḥ śrī-jīvo namāmi*  
>  
> *"I offer my respectful obeisances unto Srila Jiva Gosvami, who protects and illuminates the sublime teachings of Lord Caitanya Mahaprabhu and the Six Gosvamis."*
"""
    },
    'Raghunatha Dasa': {
        'title': 'Srila Raghunatha Dasa Gosvami',
        'story': """### Srila Raghunatha Dasa Gosvami: Rasa Manjari & Prayojana-Acharya

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srila Raghunatha Dasa Gosvami (1494–1586 CE) is **Rasa Manjari** (and Tulasi Manjari). He is glorified as the **Prayojana-Acharya**—the supreme exemplar of unalloyed *radha-dasyam* and extreme detachment. Born in Saptagram (Bengal) as the multi-millionaire prince son of landlord Govardhana Majumdar, he renounced princely wealth to surrender at Katwa, Puri, and Radha-kunda.

---

#### 2. Sacred Pastimes from Sri Caitanya-caritamrta (Antya 6 & 16)

##### Pastime 1: The Chida-Dahi Mahotsava at Panihati (Antya 6)
Endlessly trying to escape his family guard to join Lord Caitanya, Raghunatha Dasa met Lord Nityananda at Panihati under a banyan tree. 

Lord Nityananda jokingly called him a thief and commanded: *"You are trying to reach Lord Caitanya without My mercy! Pay a fine by feeding all My associates chipped rice and yogurt!"* Raghunatha joyfully hosted the famous **Chida-Dahi Festival**, feeding thousands of devotees. Lord Nityananda placed His lotus feet upon Raghunatha's head, blessing him: *"Your family bondage is shattered! You will soon reach Lord Caitanya's lotus feet!"*

##### Pastime 2: Escaping to Jagannath Puri & Sixteen Years of Personal Service
Sprinting on foot through jungle paths for twelve days while dodging guards, Raghunatha arrived in Jagannath Puri eating only thrice on the way. 

Lord Caitanya entrusted him to **Svarupa Damodara Gosvami** as his personal assistant. Mahaprabhu gifted Raghunatha His own personal **Govardhana-sila** and **Gunja-mala**, which Raghunatha bathed in his tears every day.

##### Pastime 3: Extreme Austerity at Radha-kunda
After Lord Caitanya and Svarupa Damodara passed away, Raghunatha went to Vrindavan planning to throw himself off Govardhana Hill. Rupa and Sanatana embraced him and requested him to stay at **Radha-kunda**. 

There, Raghunatha offered 1,000 prostrated obeisances daily, chanted 100,000 Holy Names (64 rounds), offered 2,000 obeisances to Vaishnavas, and slept less than 1.5 hours daily! For food, he drank only a small cup of buttermilk (*thañch*) every two days.

##### Pastime 4: Srimati Radharani Shields Him from the Sun
While Raghunatha Dasa sat out in the open sun on the banks of Radha-kunda absorbed in writing *Vraja-vilāsa-stava*, Srimati Radharani Herself appeared behind him, shielding him from the fierce sun with her veil while sweet perspiration dripped from her forehead!

---

#### 3. Major Literary Contributions
- **Vilāpa-kusumāñjali:** Heart-wrenching prayers of unalloyed *radha-dasyam*.
- **Manāḥ-śikṣā:** Eleven foundational instructions to the mind.
- **Stavāvalī, Muktā-carita, Sva-niyama-daśakam.**

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Raghunatha Dasa Gosvami on his Disappearance day for ultimate renunciation (*vairāgya*) and entrance into *radha-dasyam*.

**Pranama Mantra:**
> *vairāgya-yug-bhakti-rasaṁ prayatnair apāyayan mām anabhipsu-mandam*  
> *kṛpāmbur yaḥ prapadadyato 'smin śrī-rūpa-dāmau raghunātham īḍe*  
>  
> *"I offer my respectful obeisances unto Srila Raghunatha Dasa Gosvami, the ocean of mercy who fed me the nectar of devotional service coupled with detachment."*
"""
    },
    'Raghunatha Bhatta': {
        'title': 'Srila Raghunatha Bhatta Gosvami',
        'story': """### Srila Raghunatha Bhatta Gosvami: Incarnation of Raga Manjari

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srila Raghunatha Bhatta Gosvami (1505–1579 CE) is **Raga Manjari**. He was the divine son of the great South Indian saint **Tapan Misra** (in whose house Lord Caitanya stayed for two months in Varanasi).

---

#### 2. Sacred Pastimes from Sri Caitanya-caritamrta (Antya 13)

##### Pastime 1: Cooking and Serving Lord Caitanya at Varanasi (Antya 13)
When Lord Caitanya stayed at Tapan Misra's house in Varanasi, young Raghunatha Bhatta washed Mahaprabhu's lotus feet, massaged His legs, and served Him prasadam with intense love. Mahaprabhu affectionately called him "Bhatta" and blessed him.

##### Pastime 2: Eight Months in Jagannath Puri & Mahaprabhu's Sacred Gifts
When Raghunatha Bhatta grew up, he traveled to Jagannath Puri and spent eight months in Mahaprabhu's personal service. 

Before sending him to Vrindavan, Lord Caitanya gifted Raghunatha Bhatta His own 14-foot **Tulasi garland** (*tulasī-mālā*) and **betel nut remnants**, instructing him: *"Do not marry, do not talk worldly topics, worship Radha-Krishna constantly, and recite Srimad-Bhagavatam under the Six Gosvamis in Vrindavan!"*

##### Pastime 3: Melodious Recitation of Srimad-Bhagavatam at Govindadeva Temple
In Vrindavan, Raghunatha Bhatta Gosvami joined Rupa and Sanatana. Sitting at the Sri Govindadeva Temple, he recited *Śrīmad-Bhāgavatam* in a voice so sweet, melodious, and choked with tears of ecstasy that tears flowed like rivers from the eyes of all listeners! 

He sang each verse in three or four different ragas (tunes), weeping continuously in divine love.

##### Pastime 4: Pure Devotional Outlook (Adosha-darshi)
Srila Raghunatha Bhatta Gosvami never listened to blasphemy or criticism of any Vaishnava. He believed that every Vaishnava was serving Krishna according to their capacity, refusing to see any faults in others (*adoṣa-darśī*).

---

#### 3. Major Contributions
- Inspired his wealthy royal disciple to build the magnificent **Sri Govindadeva Temple** in Vrindavan for Srila Rupa Gosvami.
- Gifted sacred jewels and royal crowns for Sri Govindadeva's worship.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Raghunatha Bhatta Gosvami on his Disappearance day for a melodious voice in reciting Srimad-Bhagavatam and freedom from criticizing Vaishnavas (*vaiṣṇava-nindā*).

**Pranama Mantra:**
> *namo raghunāthāya bhattākhyāya mahātmane*  
> *rāga-mañjarī-rūpāya gaura-kṛpā-mūrtaye*  
>  
> *"I offer my respectful obeisances unto Srila Raghunatha Bhatta Gosvami, who is Raga Manjari in Vraja-lila, the master reciter of Srimad-Bhagavatam, and the embodiment of Lord Caitanya's mercy."*
"""
    },
    'Gopala Bhatta': {
        'title': 'Srila Gopala Bhatta Gosvami',
        'story': """### Srila Gopala Bhatta Gosvami: Incarnation of Guna Manjari

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srila Gopala Bhatta Gosvami (1503–1578 CE) is **Guna Manjari** (and Ananga Manjari). He was born in Sri Rangam (Tamil Nadu) as the son of the head priest **Venkata Bhatta** (Sri Sampradaya). During Lord Caitanya's Chaturmasya stay at Sri Rangam in 1510, young Gopala Bhatta served Mahaprabhu with supreme love and received His direct mercy.

---

#### 2. Sacred Pastimes from Sri Caitanya-caritamrta (Madhya 9) & Bhakti-ratnakara

##### Pastime 1: Serving Lord Caitanya During Chaturmasya at Sri Rangam
For four months during the rainy season, Lord Caitanya stayed at Venkata Bhatta's house in Sri Rangam. 

Seven-year-old Gopala Bhatta massaged Mahaprabhu's lotus feet, brought Him water, and wept tears of grief when Mahaprabhu departed. Lord Caitanya embraced him, gave him His personal *kaupīna* (loincloth) and wooden seat (*āsana*), instructing him to worship Salagrama-silas in Vrindavan after his parents' departure.

##### Pastime 2: Bringing Twelve Damodara Salagrama-Silas from Gandaki River
While on pilgrimage to Nepal, Gopala Bhatta bathed in the sacred Kali-Gandaki River. When he dipped his brass water pot (*loṭā*) into the water, **twelve Damodara Salagrama-silas** entered his pot by their own accord! He brought them back to Vrindavan and worshiped them with unswerving devotion.

##### Pastime 3: Self-Manifestation of Sri Radha-Ramanaji (1542 CE)
On Narasimha Caturdasi night, a wealthy merchant gifted Gopala Bhatta fine silks, crowns, and gold ornaments. 

Feeling sad that he could only offer ornaments to a Deity with hands and feet, not to rounded Salagrama-silas, Gopala Bhatta wept all night in front of his Damodara-sila. 

The next morning, when he uncovered his Silas, one of the Damodara-silas had self-manifested into the breathtaking 12-inch Deity of **Sri Radha-Ramana**, complete with three curves (*tri-bhaṅga-lalita*), lotus eyes, and a smiling face! (The original self-manifested Sila is still visible on Radha-Ramana's back to this day).

##### Pastime 4: Authoring Hari-bhakti-vilasa & Initiating Srinivasa Acarya
Under Srila Sanatana Gosvami's guidance, Gopala Bhatta compiled the authoritative manual of Vaishnava Deity worship and archana (**Hari-bhakti-vilāsa**). He also initiated **Srinivasa Acarya** into Gaudiya Vaishnavism.

---

#### 3. Major Literary & Cultural Legacy
- **Sri Radha-Ramana Temple:** Established the unceasing 500-year-old worship of Sri Radha-Ramana in Vrindavan without any idol replacement (*Sri Radha-Ramana has never left Vrindavan since 1542*).
- **Hari-bhakti-vilāsa** and **Sat-kriyā-sāra-dīpikā**.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Gopala Bhatta Gosvami on his Disappearance day for Deity worship purity (*arcana-mārga*) and shelter under Sri Radha-Ramanaji.

**Pranama Mantra:**
> *namo gaura-kṛpā-mūrte gopāla-bhaṭṭa-saṁjñaka*  
> *guṇa-mañjarī-rūpāya rādhā-ramaṇa-dāyine*  
>  
> *"I offer my respectful obeisances unto Srila Gopala Bhatta Gosvami, the embodiment of Lord Caitanya's mercy, who is Guna Manjari in Vraja-lila and the revealer of Sri Radha-Ramanaji."*
"""
    },
    'Lokanatha': {
        'title': 'Srila Lokanatha Gosvami',
        'story': """### Srila Lokanatha Gosvami: Incarnation of Manjulali Manjari

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srila Lokanatha Gosvami (1483–1588 CE) is **Manjulali Manjari** (Lila Manjari). Born in Talkhari (Jessore, Bangladesh) to Padmanabha Chakravarti and Sita Devi, he was dispatched to Vrindavan by Lord Caitanya Mahaprabhu *even before* Rupa and Sanatana arrived, making him one of the pioneer Gosvamis of Vraja.

---

#### 2. Sacred Pastimes from Bhakti-ratnakara & Gaudiya History

##### Pastime 1: Dispatched to Vrindavan by Lord Caitanya
Embracing Lokanatha in Navadvipa, Lord Caitanya instructed him: *"Go immediately to Vrindavan and rediscover the lost holy places. I shall join you there after I accept sannyasa."* 

Lokanatha traveled with his dear lifelong friend **Bhugarbha Gosvami**. When Lord Caitanya later visited Vrindavan for a short time, He secretly met Lokanatha under a banyan tree, instructing him to remain in Vrindavan perpetually.

##### Pastime 2: Worshiping Sri Radha-Vinodaji in a Canvas Bag
Wandering through the forests of Vrindavan, Srila Lokanatha Gosvami desired a Deity to worship. 

Lord Krishna self-manifested as the exquisite small Deity of **Sri Radha-Vinoda** and handed Himself to Lokanatha in Kishorivana! 

Lokanatha carried Sri Radha-Vinodaji in a cloth bag hung around his neck wherever he walked, serving Him with intense love and weeping tears of joy.

##### Pastime 3: Extraordinary Humility & Refusing Disciples
Out of profound humility, Srila Lokanatha Gosvami resolved never to accept any disciples or fame, living in complete seclusion at Kishorivana.

##### Pastime 4: Accepting Srila Narottama Dasa Thakura as His Only Disciple
Prince Narottama Dasa Thakura ran away from his kingdom to Vrindavan, longing for Lokanatha Gosvami's initiation. Lokanatha refused to accept him. 

Determined to serve, Narottama began secretly cleaning Lokanatha's latrine area every night at midnight, carrying away nightsoil and sweeping the path with his hair! 

After one year of secret service, Lokanatha caught Narottama in the act, wept in awe at his humility, embraced him, and gave him initiation as his **one and only disciple**!

---

#### 3. Spiritual Significance & Observance Guidelines
Srila Lokanatha Gosvami teaches supreme detachment, humility, and single-minded devotion to Sri Radha-Vinodaji.

- **Fasting Rules:** Fasting is observed until noon (12:00 PM).
- **Festival Activities:** Reading *Bhakti-ratnakara* (pastimes of Lokanatha Gosvami and Narottama Dasa Thakura), offering flowers and sweet rice to Sri Radha-Vinodaji.
- **Noon Parana:** Feast offering presented at noon, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Lokanatha Gosvami on his Disappearance day for genuine humility (*tṛṇād api sunīcena*) and shelter in Vraja-bhumi.

**Pranama Mantra:**
> *śrīmāl-lokanātha-prabhuṁ vande karuṇāmṛta-sāgaram*  
> *mañjulālī-rūpābhidhaṁ gaura-priya-janaṁ sadā*  
>  
> *"I offer my respectful obeisances unto Srila Lokanatha Gosvami Prabhupada, an ocean of nectarine mercy who is Manjulali Manjari in Vraja-lila and eternally dear to Lord Caitanya."*
"""
    },
    'Krsnadasa Kaviraja': {
        'title': 'Srila Krishnadasa Kaviraja Gosvami',
        'story': """### Srila Krishnadasa Kaviraja Gosvami: Kasturi Manjari & Biographer-Acharya

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srila Krishnadasa Kaviraja Gosvami (1496–1588 CE) is **Kasturi Manjari**. He was born in Jhamatpur (Katwa, Bengal) to Bhagiratha and Sunanda. He is glorified as the **Biographer-Acharya** of Lord Sri Caitanya Mahaprabhu and author of the crown jewel of Gaudiya literature: **Śrī Caitanya-caritāmṛta**.

---

#### 2. Sacred Pastimes from Sri Caitanya-caritamrta (Adi 5) & Gaudiya History

##### Pastime 1: Vision of Lord Nityananda at Jhamatpur (Adi 5.181–232)
When a visiting scholar insulted Srila Nityananda Prabhu at Krishnadasa's family home, Krishnadasa's brother remained silent. Furious at his brother's tolerance of *Nityānanda-nindā*, Krishnadasa left home. 

That night, Lord Nityananda appeared to Krishnadasa in a dream, surrounded by cowherd boys and holding a golden rod. Lord Nityananda smiled and commanded him: *"O Krishnadasa! Fear not. Arise and go immediately to Vrindavan! In Vrindavan you will attain all desires!"*

##### Pastime 2: Writing Sri Caitanya-caritamrta at Radha-kunda
In extreme old age (over 80 years old), almost blind, deaf, and trembling with age, Srila Krishnadasa Kaviraja Gosvami sat under the trees of **Radha-kunda**. 

All senior Vrindavan Gosvamis—Srila Jiva Gosvami, Lokanatha, Gopala Bhatta, and Raghunatha Dasa—unanimously requested him to write the definitive biography of Lord Caitanya's life and philosophy. 

Deeply praying at the lotus feet of **Sri Madana-Mohana**, Madana-Mohana's floral garland fell from the Deity's neck as a divine command!

##### Pastime 3: Extraordinary Humility in Writing
Throughout *Caitanya-caritamrta*, Srila Krishnadasa Kaviraja displays unmatched, weeping humility:
> *purīṣera kīṭa haite mui se laghiṣṭha*  
> *jagāi mādhāi haite mui se pāpiṣṭha*  
> *"I am lower than a worm in stool, more sinful than Jagai and Madhai. Anyone who hears my name loses all his pious merit!"*

##### Pastime 4: The Theft of the Manuscripts & Disappearance
When the bullock-cart carrying the original manuscript of *Caitanya-caritamrta* was stolen by King Birhambir's bandits in Vana-Vishnupur, Krishnadasa Kaviraja was heartbroken. Entering samadhi in separation from Radha-kunda, he entered the eternal pastimes of Srimati Radharani.

---

#### 3. Major Literary Contributions
- **Śrī Caitanya-caritāmṛta:** The unmatched magnum opus of Gaudiya Vaishnavism.
- **Govinda-līlāmṛta:** 25 chapters detailing Radha-Krishna's eight-fold daily pastimes (*aṣṭa-kālīya-līlā*).
- **Sāraṅga-raṅgadā:** Sanskrit commentary on Bilvamangala Thakura's *Kṛṣṇa-karṇāmṛta*.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Krishnadasa Kaviraja Gosvami on his Disappearance day for genuine humility and deep attachment to reading *Sri Caitanya-caritamrta*.

**Pranama Mantra:**
> *vande rūpa-sanātana-raghunātha-śrī-jīva-gopāla-bhaṭṭa-dāsas*  
> *caitanya-caritāmṛta-kāraṁ kastūrī-mañjarī-svarūpam*  
>  
> *"I offer my respectful obeisances unto Srila Krishnadasa Kaviraja Gosvami, who is Kasturi Manjari in Vraja-lila and the author of Sri Caitanya-caritamrta."*
"""
    },
    'Vrndavana Dasa': {
        'title': 'Srila Vrndavana Dasa Thakura',
        'story': """### Srila Vrndavana Dasa Thakura: Incarnation of Srila Vyasadeva

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srila Vrndavana Dasa Thakura (1507–1589 CE) is **Vedavyasa** (Srila Vyasadeva). He was born in Mamgachi (Navadvipa) to **Narayani Devi** (the four-year-old niece of Srivasa Pandita who received Lord Caitanya's prasadam remnants). He is glorified throughout Gaudiya literature as the **Vyāsadeva of Gaura-līlā** and author of **Śrī Caitanya-bhāgavata**.

---

#### 2. Sacred Pastimes from Sri Caitanya Bhagavata & Sri Caitanya-caritamrta (Adi 11)

##### Pastime 1: Narayani Receiving Mahaprabhu's Direct Remnants
When Lord Caitanya revealed His *Mahā-prakāśa-līlā* in Srivasa Angan, He called four-year-old Narayani, gave her His chewed betel remnants (*tāmbūla*), and commanded her: *"Chant Krishna's Holy Name and weep!"* 

The small child instantly swooned in divine love, tears cascading down her cheeks. Srila Vrndavana Dasa Thakura was born from her womb as an incarnation of Srila Vyasadeva.

##### Pastime 2: Personal Servant of Lord Nityananda Prabhu
Lord Nityananda Prabhu took young Vrndavana Dasa under His personal shelter. Vrndavana Dasa accompanied Lord Nityananda on His sankirtana tours across Bengal, witnessing Nityananda's wild ecstatic dancing and torrential distribution of Krishna-prema to the most fallen souls.

##### Pastime 3: Authoring Sri Caitanya-bhagavata at Denur
Empowered by Lord Nityananda, Vrndavana Dasa Thakura retired to the peaceful village of Denur (Bardhaman) and composed **Śrī Caitanya-bhāgavata** (originally named *Caitanya-maṅgala*). 

He vividly recorded the childhood, youth (*Ādi-khaṇḍa*), and Navadvipa pastimes (*Madhya-khaṇḍa*) of Nimai Pandit, capturing the roaring sankirtana in Srivasa Angan and the surrender of Chand Kazi.

##### Pastime 4: Glorification by Krishnadasa Kaviraja Gosvami
In *Caitanya-caritamrta* (Adi 11.55), Srila Krishnadasa Kaviraja writes:  
*"Srila Vyasadeva described Krishna-lila in Srimad-Bhagavatam. The Vyasadeva of Caitanya-lila is none other than Vrndavana Dasa Thakura!"*

---

#### 3. Major Literary Contributions
- **Śrī Caitanya-bhāgavata:** The primary nectarine chronicle of Lord Caitanya's early life and Navadvipa Sankirtana.
- **Nityānanda-guṇavaṇam** and **Śrī Navadvīpa-mahātmyam**.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Vrndavana Dasa Thakura on his Disappearance day for attachment to hearing Gaura-lila and unswerving faith in Lord Nityananda Prabhu.

**Pranama Mantra:**
> *namo 'stu vṛndāvana-dāsa-nāmne*  
> *caitanya-līlāmṛta-kārakāya*  
> *vedavyāsāvtārāya narāyaṇī-sutāya ca*  
>  
> *"I offer my respectful obeisances unto Srila Vrndavana Dasa Thakura, the son of Narayani Devi, who is the incarnation of Srila Vyasadeva and author of the nectarine Sri Caitanya-bhagavata."*
"""
    },
    'Narottama Dasa': {
        'title': 'Srila Narottama Dasa Thakura',
        'story': """### Srila Narottama Dasa Thakura: Champaka Manjari & Thakura Mahasaya

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srila Narottama Dasa Thakura (1520–1611 CE) is **Champaka Manjari**. Born as the royal prince of Kheturi (Garanhati, Rajshahi, Bangladesh) to King Krishnananda Datta and Narayani Devi, he renounced royal luxury to seek initiation under Srila Lokanatha Gosvami in Vrindavan. He is glorified as **Thakura Mahasaya**—the crown jewel of Gaudiya kirtaniyas and author of *Prārthanā* and *Prema-bhakti-candrikā*.

---

#### 2. Sacred Pastimes from Bhakti-ratnakara, Narottama-vilasa & Prema-vilasa

##### Pastime 1: Lord Caitanya Depositing Prema in the Padma River
When Lord Caitanya traveled through East Bengal years before Narottama's birth, He deposited His divine love (*prema*) in the waters of the Padma River at Kanair Natshala, crying: *"Padma! Keep this prema safe for My Narottama when he comes to bathe here!"* 

When young Narottama entered the Padma River years later, the river surged with golden light, and the prema of Lord Caitanya entered Narottama's body, turning his skin into molten gold!

##### Pastime 2: Nighttime Latrine Cleaning for Lokanatha Gosvami
Determined to receive initiation from Srila Lokanatha Gosvami (who had sworn never to accept disciples), Prince Narottama quietly sneaked out of his residence at midnight every night for a full year, cleaning Lokanatha's latrine area and sweeping the forest path with his own hair! 

When Lokanatha caught Narottama in the dark and realized the prince's incredible humility, Lokanatha wept, embraced him, and initiated him as his sole disciple.

##### Pastime 3: Hosting the Historic Kheturi Maha-Festival
Narottama established six grand Deities in Kheturi (Sri Gauranga, Vallabhikanta, Sri Vrajamohana, Sri Radhakanta, Sri Radharamana, and Sri Gopalaji). 

He organized the first nationwide **Kheturi Festival**, bringing together Mother Jahnava Devi, Srinivasa Acarya, Syamananda Prabhu, and thousands of devotees from Bengal, Odisha, and Vrindavan, introducing the unique *Padāvalī-kīrtana* style.

##### Pastime 4: Disappearance into Milk in the Ganges
Feeling the end of his earthly pastimes at Garanhati, Narottama instructed his disciples Ramachandra Kaviraja and Narasimha to carry him to the banks of the Ganges. 

As his disciples massaged his body with Ganges water while singing kirtana, Narottama's body melted directly into pure liquid white milk (*kṣīra*) and merged into the sacred waters of Mother Ganges!

---

#### 3. Major Literary Contributions
- **Prārthanā:** Immortal devotional songs of prayer, humble lamentation, and aspiration (*"Śrī-kṛṣṇa-caitanya prabhu doyā koro more"*, *"Gaurāṅga bolite habe pulaka śarīra"*).
- **Prema-bhakti-candrikā:** The moonlight of spontaneous love of Godhead (*Rāgānugā-bhakti*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Narottama Dasa Thakura on his Disappearance day for weeping affection in chanting the Holy Name and genuine Vaishnava humility.

**Pranama Mantra:**
> *namo narottamāya eva rādhā-kṛṣṇa-padātmine*  
> *caṁpaka-mañjarī-rūpāya kṛpā-sindho namo 'stu te*  
>  
> *"I offer my respectful obeisances unto Srila Narottama Dasa Thakura, who is Champaka Manjari in Vraja-lila, the supreme singer of Gaura-kirtana, and an ocean of mercy."*
"""
    },
    'Srinivasa Acarya': {
        'title': 'Srila Srinivasa Acarya',
        'story': """### Srila Srinivasa Acarya: Incarnation of Mani Manjari

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srila Srinivasa Acarya (1520–1610 CE) is **Mani Manjari**. Born in Chakhandi (Bengal) to the saintly brahmana Gangadhara Bhattacharya (Chaitanyadasa) and Lakshmipriya Devi. He was initiated into Gaudiya Vaishnavism by **Srila Gopala Bhatta Gosvami** and studied all Six Gosvamis' scriptures under **Srila Jiva Gosvami** in Vrindavan. He is famous as the author of the immortal **Ṣaṭ-Gosvāmy-aṣṭakam**.

---

#### 2. Sacred Pastimes from Bhakti-ratnakara & Anuraga-valli

##### Pastime 1: Conception Blessed by Lord Caitanya
When Gangadhara Bhattacharya visited Jagannath Puri during Lord Caitanya's pastimes, Lord Caitanya repeatedly called out *"Jagannatha! Jagannatha!"* with such ecstatic love that Gangadhara came to be known as Chaitanyadasa. Lord Caitanya blessed him that a divine son would be born to him who would preach Gaudiya Vaishnavism across Bengal.

##### Pastime 2: Arriving at Katwa and Puri Just After Disappearance
When young Srinivasa traveled to Katwa to meet Lord Caitanya, Mahaprabhu accepted sannyasa. Later, when Srinivasa traveled on foot to Puri to see Mahaprabhu, Lord Caitanya had just completed His unmanifest pastimes! 

Weeping in agony, Srinivasa was instructed in a dream by Lord Caitanya to travel to Vrindavan and take shelter of Rupa, Sanatana, Jiva, and Gopala Bhatta.

##### Pastime 3: The Caravan of Books & Converting King Birhambir
Srila Jiva Gosvami entrusted Srinivasa Acarya, Narottama Dasa Thakura, and Syamananda Prabhu with a bullock cart containing the sole original manuscripts of the Six Gosvamis to carry to Bengal. 

In Vana-Vishnupur, royal astrologers informed the robber-king **Birhambir** that a priceless treasure cart was passing through. The King's bandits stole the trunk of books! 

Srinivasa stayed behind in Vishnupur, entered the King's court, recited *Śrīmad-Bhāgavatam* with such celestial devotion that King Birhambir wept, fell at Srinivasa's feet, confessed the theft, returned all the sacred manuscripts intact, and became Srinivasa's surrendered disciple along with his entire royal kingdom!

##### Pastime 4: Composing the Shad-Gosvami-Ashtaka
Absorbed in profound separation from the Six Gosvamis of Vrindavan, Srila Srinivasa Acarya composed the world-famous eight-verse prayer **Ṣaṭ-Gosvāmy-aṣṭakam** (*kṛṣṇotkīrtana-gāna-nartana-parau premāmṛtāmbho-nidhī...*), glorifying their activities at Radha-kunda.

---

#### 3. Major Literary Contributions
- **Ṣaṭ-Gosvāmy-aṣṭakam:** The foundational eight prayers glorifying the Six Gosvamis.
- **Gaurāṅga-mahātmyam** and commentaries on *Hari-bhakti-vilāsa*.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Srinivasa Acarya on his Disappearance day for deep appreciation of the Six Gosvamis' scriptures and enthusiasm in preaching.

**Pranama Mantra:**
> *namo gaura-kṛpā-dāmne śrīnivāsāyātma-mūrtaye*  
> *maṇi-mañjarī-rūpāya sat-sampradāya-dāyine*  
>  
> *"I offer my respectful obeisances unto Srila Srinivasa Acarya, who is Mani Manjari in Vraja-lila, the recipient of Lord Caitanya's direct mercy, and the restorer of the Gosvami literature."*
"""
    },
    'Syamananda': {
        'title': 'Srila Syamananda Prabhu',
        'story': """### Srila Syamananda Prabhu: Incarnation of Kanakamanjari

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srila Syamananda Prabhu (Dukhi Krishna Dasa) is **Kanakamanjari**. Born in Dharenda-Bahadulpur (Utkala/Odisha) to Krishna Mandal and Durika Devi. He was initiated into Gaudiya Vaishnavism by **Sri Hridaya Chaitanya** (disciple of Gauridasa Pandita). He studied under **Srila Jiva Gosvami** in Vrindavan and was assigned the daily service of sweeping **Seva Kunj**.

---

#### 2. Sacred Pastimes from Syamananda-prakasa & Bhakti-ratnakara

##### Pastime 1: Finding Srimati Radharani's Golden Anklet (Nupura)
While sweeping the groves of Seva Kunj early one morning, Dukhi Krishna Dasa found a divine golden anklet (*nūpura*) shining under a tree. 

Soon, Subala-gopi (Lalita Sakhi in disguise) returned searching for Srimati Radharani's lost anklet. Recognizing her divine nature, Dukhi Krishna requested Radharani's darshana. 

Srimati Radharani appeared before him, pressed the anklet against Dukhi Krishna's forehead, leaving a golden tilaka mark (*tilaka* shaped like an anklet with a dot), and renamed him **Śyāmānanda** ("one who gives pleasure to Syama")!

##### Pastime 2: Resolving the Tilaka Controversy with Hridaya Chaitanya
When Syamananda returned to his guru Hridaya Chaitanya wearing the new golden tilaka mark given by Radharani, Hridaya Chaitanya tested him, becoming outwardly angry and beating him for changing his sampradaya tilaka. 

Syamananda bore the beatings patiently without anger. That night, Srimati Radharani appeared in Hridaya Chaitanya's dream, showing Her original anklet mark and explaining that She Herself had placed the tilaka on Syamananda. Hridaya Chaitanya wept in joy and embraced Syamananda as his exalted disciple.

##### Pastime 3: Preaching in Odisha & Converting Rasikananda
Returned to Odisha with the Gosvami manuscripts, Srila Syamananda Prabhu preached Harinama Sankirtana across Midnapore and Odisha, converting the noble prince **Sri Rasikananda Deva Gosvami** into his chief disciple.

##### Pastime 4: Subduing Mad Wild Elephants
When a mad wild elephant charged toward Syamananda's kirtana party in the Odisha jungles, Syamananda simply raised his arms, chanted *"Hare Krishna!"*, and touched the elephant's forehead. The wild elephant bowed its knees, wept tears of devotion, and became a gentle devotee!

---

#### 3. Spiritual Significance & Observance Guidelines
Srila Syamananda Prabhu exemplifies the highest perfection of *sevan-mārga* and Radharani's direct mercy.

- **Fasting Rules:** Fasting is observed until noon (12:00 PM).
- **Festival Activities:** Reading *Bhakti-ratnakara* (pastimes of Syamananda Prabhu at Seva Kunj), offering yellow silk garments, flowers, and kirtana.
- **Noon Parana:** Feast offering presented at noon, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Syamananda Prabhu on his Disappearance day for eager enthusiasm in humble devotional service.

**Pranama Mantra:**
> *namo 'stu śyāmānandāya rādhikā-charaṇābji-sevine*  
> *kanaka-mañjarī-rūpāya gaura-bhakti-pradāyine*  
>  
> *"I offer my respectful obeisances unto Srila Syamananda Prabhu, who is Kanakamanjari in Vraja-lila, the blessed sweeper of Seva Kunj who received Srimati Radharani's divine anklet."*
"""
    }
}


def populate_gosvami_descriptions():
    updated_count = 0
    for key_name, data in GOSVAMI_STORIES.items():
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
    help = 'Populate detailed scriptural stories for Vrindavan Six Gosvamis & Paramount Acharyas observances.'

    def handle(self, *args, **options):
        count = populate_gosvami_descriptions()
        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated stories for {count} Gosvami / Acharya observances in Vaishnava Calendar.")
        )
