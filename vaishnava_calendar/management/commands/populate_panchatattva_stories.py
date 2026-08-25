import logging
from django.core.management.base import BaseCommand
from vaishnava_calendar.models import CalendarObservance, CalendarObservanceTranslation

logger = logging.getLogger(__name__)

PANCHATTATVA_STORIES = {
    'Advaita': {
        'title': 'Sri Advaita Acarya',
        'story': """### Sri Advaita Acarya: Incarnation of Maha-Vishnu & Sada-Shiva

#### 1. Eternal Identity & Lineage
In the Pancha-tattva, Sri Advaita Acarya (1434–1559 CE) is the combined incarnation of **Maha-Vishnu** (the primary creator of the material universes) and **Sada-Shiva** (*advaitaṁ harinādvaitād ācāryaṁ bhakti-śaṁsanāt* — *Caitanya-caritamrta* Adi 1.12–13). He was born in Navagrama (Sunamganj, Bangladesh) to Kubera Pandita and Nabha Devi, and later lived in Shantipur and Navadvipa. He was married to Srimati Sita Thakurani and Srimati Sri Devi, and was initiated by **Srila Madhavendra Puri**.

---

#### 2. Sacred Pastimes from Sri Caitanya-caritamrta & Sri Caitanya Bhagavata

##### Pastime 1: Tulasi Worship & Calling Lord Caitanya to Earth
Grieved by the drowning of the world in Kali-yuga material illusion and atheism, Sri Advaita Acarya vowed to bring the Supreme Personality of Godhead Himself down to the Earth. 

Relying on the shastric verse from the *Gautamīya-tantra* (*tulasī-dala-mātreṇa jalasya cusukena vā...*), Advaita Acarya worshipped His Salagrama-sila every single day with fresh Ganges water and *Tulasī-mañjarīs*, crying out with thunderous roars of intense devotional sorrow. 

His roaring prayers pierced the outer shell of the universe and compelled Lord Sri Krishna to descend as **Sri Caitanya Mahaprabhu**!

##### Pastime 2: Testing Lord Caitanya's Anger at Shantipur (Madhya 10)
Advaita Acarya desired to experience Lord Caitanya's chastisement as a loving master. He began teaching subtle Mayavada (impersonalism) in Shantipur. 

Hearing this, Lord Caitanya stormed into Shantipur, pulled Advaita Acarya off his seat, and slapped his back in anger! 

Advaita Acarya began dancing in wild joy, shouting: *"Today my desire is fulfilled! My Lord has beaten me like a master chastises a servant!"* Lord Caitanya wept in love and embraced Advaita Acarya.

##### Pastime 3: The Universal Offerings at Advaita Bhavan
At Advaita Bhavan in Shantipur, Advaita Acarya hosted Sri Caitanya Mahaprabhu, Lord Nityananda, and all Navadvipa devotees after Mahaprabhu took *sannyāsa*, feeding thousands of devotees lavish prasadam for ten days in divine joy.

##### Pastime 4: Recognizing Mahaprabhu's Visvarupa in Navadvipa
Before Mahaprabhu revealed His identity to the world, Advaita Acarya offered full prostrated obeisances at young Nimai's feet in Srivasa Angan, proclaiming Him as the Supreme Absolute Truth.

---

#### 3. Spiritual Significance & Observance Guidelines
Without Advaita Acarya's roaring prayers, Lord Caitanya would not have descended to establish the Sankirtana movement.

- **Fasting Rules:** Fasting is observed until noon (12:00 PM).
- **Festival Activities:** Abhisheka of Sri Advaita Acarya / Sri Gaura-Nitai Deities, offering Tulasi leaves, Ganges water, and reading *Caitanya-caritamrta* Adi Lila Chapter 6.
- **Noon Parana:** Feast offering presented at noon, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Sri Advaita Acarya on his Appearance day for intense enthusiasm in calling upon the Supreme Lord through Harinama Sankirtana.

**Pranama Mantra:**
> *mahā-viṣṇur jagat-kartā māyayā yaḥ sṛjaty adaḥ*  
> *tasyāvtāra evāyam advaitācārya īśvaraḥ*  
>  
> *"Advaita Acarya is the incarnation of Maha-Vishnu, whose main function is to create the cosmic world through the actions of Maya. I offer my respectful obeisances unto Sri Advaita Acarya."*
"""
    },
    'Visnupriya': {
        'title': 'Srimati Visnupriya Devi',
        'story': """### Srimati Visnupriya Devi: Incarnation of Satyabhama & Lakshmi Devi

#### 1. Eternal Identity & Lineage
In Gaura-lila, Srimati Visnupriya Devi is **Satyabhama Devi** (and Bhu-devi / Lakshmi-devi). She is the second divine consort of Lord Sri Caitanya Mahaprabhu (Nimai Pandit) in Navadvipa. She was born on Vasanta Panchami in Navadvipa to the saintly royal physician **Sanatana Misra** and Srimati Mahamayi Devi.

---

#### 2. Sacred Pastimes from Sri Caitanya Bhagavata & Sri Caitanya Mangala

##### Pastime 1: Divine Marriage with Nimai Pandit
After Laksmipriya Devi passed away in separation, Sachi Mata arranged the divine marriage of Nimai Pandit with young Visnupriya Devi. 

The wealthy royal devotee Buddhimanta Khan hosted the wedding with breathtaking opulence, recreating the celestial splendor of Lord Krishna's marriage to Satyabhama in Dvaraka.

##### Pastime 2: The Agony of Separation on the Eve of Sannyasa
On the night before Nimai Pandit left home to accept *sannyāsa* at Katwa (at age 24), Srimati Visnupriya Devi sensed the impending separation. Falling at Nimai's lotus feet, she wept bitterly: *"My Lord, if You abandon me, I will drown myself in the Ganges!"* 

Lord Nimai gently placed His hand upon her head, revealed His transcendental four-armed Vishnu form, and instructed her: *"Do not grieve, My queen. I reside eternally in your heart, and Harinama Sankirtana is our unbroken bond."* Before departing into the night, He gave her His personal wooden sandals (*pādukā*) to worship.

##### Pastime 3: Extreme Tapasya & Rice Grain Chanting
After Lord Caitanya accepted sannyasa, Srimati Visnupriya Devi led a life of extreme, superhuman austerity (*tapasya*). 

Every morning, sitting in silent meditation, she chanted one round of the Hare Krishna Maha-Mantra and placed **one grain of raw rice** into a clay pot. She chanted continuously from dawn to dusk, and at the end of the day, she boiled only the few handfuls of rice accumulated from her rounds, offered them to Mahaprabhu, and ate only that tiny portion as her daily maintenance! Her golden complexion turned pale white from severe vows.

##### Pastime 4: Carving and Worshiping Sri Gauranga Wooden Deity
Srimati Visnupriya Devi commissioned the carving of the first wooden **Sri Gauranga Mahaprabhu Deity** in Navadvipa, worshipping Him alongside Mahaprabhu's wooden sandals (*pādukā*). That historic original Deity is worshipped to this day at the Dhameswar Mahaprabhu Temple in Navadvipa!

---

#### 3. Spiritual Significance & Observance Guidelines
Srimati Visnupriya Devi exemplifies the pinnacle of unalloyed devotion in separation (*vipralambha-bhāva*).

- **Fasting Rules:** Fasting is observed until noon (12:00 PM) on Vasanta Panchami.
- **Festival Activities:** Worshiping Srimati Visnupriya Devi and Sri Gauranga Mahaprabhu, offering yellow silk garments, flowers, and sweet rice.
- **Noon Parana:** Feast offering presented at noon, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srimati Visnupriya Devi on her Appearance day for unswerving attachment to Harinama Sankirtana and tolerance in times of trial.

**Pranama Mantra:**
> *namas te viṣṇupriyāyai gaura-prāṇādhikātmine*  
> *satyabhāmā-svarūpāyai rukmiṇy-ādi-gaṇātmine*  
>  
> *"I offer my respectful obeisances unto Srimati Visnupriya Devi, who is dearer to Lord Gauranga than His own life, and who is the incarnation of Satyabhama and Lakshmi Devi."*
"""
    },
    'Sita Thakurani': {
        'title': 'Srimati Sita Thakurani',
        'story': """### Srimati Sita Thakurani: Incarnation of Mother Yashoda

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srimati Sita Thakurani is **Mother Yashoda** (and Yogamaya / Paurnamasi). She is the revered divine consort of Sri Advaita Acarya, residing in Shantipur and Navadvipa. She was the daughter of Nrsimha Bhaduri. She showered young Nimai Pandit with maternal affection (*vātsalya-bhāva*).

---

#### 2. Sacred Pastimes from Sri Caitanya-caritamrta (Adi 13) & Sri Caitanya Bhagavata

##### Pastime 1: Visiting Newborn Nimai at Mayapur (Adi 13.112–123)
When Lord Caitanya appeared in Mayapur, Sri Advaita Acarya dispatched Srimati Sita Thakurani to Jagannatha Misra's house bearing auspicious gifts for the newborn baby. 

Sita Thakurani brought golden armlets, silver anklets, waist-bells, tiger-claws set in gold, fine silk garments, and sacred protective herbs.

##### Pastime 2: Naming the Divine Child "Nimai"
When Sita Thakurani beheld newborn Nimai, His golden beauty enchanted her heart. Fearing that evil spirits or envious eyes might harm such an extraordinarily beautiful child, Sita Thakurani lovingly named Him **Nimai**, praying that the natural bitterness of the Neem tree would ward off all evil influences! 

She bathed baby Nimai and Srimati Sachi Devi with holy water and paddy grains, blessing Nimai with long life and protection.

##### Pastime 3: Motherly Feeding at Shantipur
Whenever Lord Caitanya and Lord Nityananda visited Shantipur, Srimati Sita Thakurani personally cooked massive feasts of traditional Bengali delicacies—curries, sweet rice, pitha, and milk sweets—serving the two Lords with boundless maternal affection.

##### Pastime 4: Pillar of the Shantipur Lineage
Following Sri Advaita Acarya's physical disappearance, Srimati Sita Thakurani guided the Shantipur community, empowering disciples like Achyutananda and nurturing Gaura-bhakti across Bengal.

---

#### 3. Spiritual Significance & Observance Guidelines
Srimati Sita Thakurani exemplifies maternal love (*vātsalya-rasa*) in Gaura-lila.

- **Fasting Rules:** Fasting is observed until noon (12:00 PM).
- **Festival Activities:** Worshiping Sita-Advaita Deities and Sri Gaura-Nitai, offering maternal affection, sweet rice, and reading *Caitanya-caritamrta* Adi 13.
- **Noon Parana:** Feast offering presented at noon, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srimati Sita Thakurani on her Appearance day for maternal protection and pure affection for Lord Caitanya Mahaprabhu.

**Pranama Mantra:**
> *namas te sītā-ṭhākurāṇyai advaita-priya-gehinī*  
> *yaśodā-rūpiṇī devī gaura-vātsalya-kāriṇī*  
>  
> *"I offer my respectful obeisances unto Srimati Sita Thakurani, the beloved wife of Sri Advaita Acarya, who is Mother Yashoda in Vraja-lila and the embodiment of maternal affection for Lord Caitanya."*
"""
    },
    'Jahnava': {
        'title': 'Srimati Jahnava Devi',
        'story': """### Srimati Jahnava Devi: Incarnation of Ananga Manjari & Revati Devi

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srimati Jahnava Devi (Jahnava Mata) is **Ananga Manjari** (the younger sister of Srimati Radharani) and **Revati Devi** (consort of Lord Balarama). She is the revered primary divine consort of Lord Nityananda Prabhu, born in Borokhai (Bengal) to Suryadasa Sarakhela (brother of Gauridasa Pandita).

---

#### 2. Sacred Pastimes from Bhakti-ratnakara & Gaudiya History

##### Pastime 1: Presiding over the Historic Kheturi Maha-Festival
Following the physical disappearance of Lord Caitanya, Lord Nityananda, and Sri Advaita Acarya, Mother Jahnava Devi assumed supreme spiritual leadership of the Gaudiya Sampradaya. 

She presided over the monumental **Kheturi Festival** hosted by Narottama Dasa Thakura, seating thousands of Vaishnavas, establishing liturgical standards, and personally serving prasadam to all assembled acharyas.

##### Pastime 2: Cook and Mother to Thousands at Kheturi
During the Kheturi festival, Mother Jahnava Devi personally cooked in the kitchen for days, preparing dozens of delicacies for thousands of devotees. She served all the Vaishnavas with Her own hands, manifesting boundless maternal compassion.

##### Pastime 3: Pilgrimage to Vrindavan & Commissioning Sri Radharani Deity
Jahnava Mata traveled on foot to Vrindavan, visiting Seva Kunj, Radha-kunda, and Vrindavan's main temples. 

Srila Jiva Gosvami and the assembled Vrindavan acharyas welcomed her with highest honor as the embodiment of Lord Nityananda's mercy. She commissioned the Deity of **Sri Radharani** to be placed to the left of Sri Gopinatha in Vrindavan!

##### Pastime 4: Subduing Bandits with Compassion
While traveling through dense jungles inhabited by dangerous bandits, Jahnava Mata's divine radiance and ocean of compassion melted the hearts of thieves and robbers, converting them on the spot into pure Harinama devotees.

---

#### 3. Spiritual Significance & Observance Guidelines
Mother Jahnava Devi is worshiped as the universal mother of all Gaudiya Vaishnavas (*jāhnavā-mātā*).

- **Fasting Rules:** Fasting is observed until noon (12:00 PM).
- **Festival Activities:** Abhisheka of Sri Sri Gaura-Nitai / Jahnava Devi Deities, offering silk garments, flowers, and reading *Bhakti-ratnakara*.
- **Noon Parana:** Feast offering presented at noon, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srimati Jahnava Devi on her Appearance day for maternal shelter, spiritual strength, and entrance into *nāma-saṅkīrtana*.

**Pranama Mantra:**
> *namas te jāhnavā-devyai nityānanda-priyātmane*  
> *ananga-mañjarī-rūpā-kṛpā-sindho namo 'stu te*  
>  
> *"I offer my respectful obeisances unto Srimati Jahnava Devi, the beloved consort of Lord Nityananda Prabhu, who is Ananga Manjari in Vraja-lila and an ocean of mercy."*
"""
    },
    'Sita Devi': {
        'title': 'Srimati Sita Devi',
        'story': """### Srimati Sita Devi (Janaki Navami): Incarnation of Goddess Lakshmi

#### 1. Eternal Identity & Lineage
Srimati Sita Devi (Janaki) is the divine incarnation of **Goddess Lakshmi** (Sri-devi), the eternal pleasure potency and consort of Lord Sri Ramacandra. She appeared in Mithila as the self-manifested daughter of Saint-King Janaka (Videha), emerging from a golden furrow while King Janaka was plowing the sacred earth for a Yajna.

---

#### 2. Sacred Pastimes from Valmiki Ramayana & Srimad-Bhagavatam (Canto 9, Chapter 10)

##### Pastime 1: Self-Manifestation from the Sacred Furrow (Sita)
King Janaka was plowing the sacrificial ground with a golden plow. Suddenly, the tip of his plow touched a golden chest hidden in the soil. Opening the chest, King Janaka found an effulgent baby girl. A celestial voice proclaimed: *"She is your divine daughter!"* Because she emerged from the furrow (*sītā*), King Janaka named her **Sītā** and **Jānakī**.

##### Pastime 2: Swayamvara & Marriage with Lord Ramacandra
When Sita came of age, King Janaka declared that she would marry whoever could lift and string the colossal iron bow of Lord Shiva (*Pinaka*). Great kings and demons failed to even nudge the bow. 

Young Prince Ramacandra stepped forward, effortlessly picked up the bow with one hand, strung it, and snapped it in two! Sita Devi placed the golden wedding garland around Lord Rama's neck.

##### Pastime 3: Unswerving Chastity & Voluntary Forest Exile
When Lord Rama was exiled to the forest for 14 years, He urged Sita to remain comfortably in Ayodhya's palace. 

Sita Devi answered: *"Where Rama is, there is Ayodhya! Without Rama, heaven itself is hell!"* She gave up royal silks and jewelry to walk barefoot behind Lord Rama into the dangerous Dandakaranya forest, setting the supreme Vedic standard of chastity (*pātivratya-dharma*).

##### Pastime 4: Trial by Fire (Agni-Pariksha) & Return to Ayodhya
When Ravana abducted an illusory shadow form (*māyā-sītā*), Lord Rama waged war and destroyed Ravana. To prove Her unblemished purity to the world, Srimati Sita Devi entered a blazing fire. **Agni Deva** (the fire god) personally stepped out of the flames carrying Sita Devi untouched and spotless, handing Her back to Lord Rama! Returning to Ayodhya, Sita Devi was crowned Queen of Ayodhya alongside Lord Ramacandra.

---

#### 3. Spiritual Significance & Observance Guidelines
Janaki Navami grants prosperity, purity, and devotion to Lord Ramacandra.

- **Fasting Rules:** Fasting is observed until noon (12:00 PM).
- **Festival Activities:** Reading *Valmiki Ramayana* (Sita Kalyanam & Janaki Navami chapters), offering lotus flowers, red/yellow garments, and panakam.
- **Noon Parana:** Feast offering presented at noon, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srimati Sita Devi on Janaki Navami for purity, unswerving devotion, and shelter at Lord Ramacandra's lotus feet.

**Pranama Mantra:**
> *janaka-sutāyai namas te rāma-vallabhāyai*  
> *pātivratya-guṇottarāyai mahā-lakṣmyai namo 'stu te*  
>  
> *"I offer my respectful obeisances unto Srimati Sita Devi, the daughter of King Janaka, the beloved consort of Lord Ramacandra, the supreme embodiment of chastity, and Goddess Maha-Lakshmi Herself."*
"""
    },
    'Haridasa': {
        'title': 'Srila Haridasa Thakura',
        'story': """### Srila Haridasa Thakura: The Supreme Namacharya

#### 1. Eternal Identity & Lineage
In Gaura-lila, Srila Haridasa Thakura (1450–1534 CE) is recognized as the combined incarnation of **Lord Brahma** and **Prahlada Maharaja** (*Gaura-ganoddesa-dipika* verses 67–68). He was born in Buron village (Jessore, Bangladesh) into a Muslim family. Lord Caitanya Mahaprabhu Himself crowned him as the **Nāmācārya**—the supreme authority and master of chanting the Holy Names (*Hare Krishna Maha-Mantra*).

---

#### 2. Sacred Pastimes from Sri Caitanya-caritamrta (Antya 11) & Sri Caitanya Bhagavata

##### Pastime 1: Chanting 300,000 Holy Names Daily & Converting the Prostitute
Srila Haridasa Thakura chanted **300,000 Holy Names (192 rounds)** on his beads every single day without fail. 

When an envious landlord Ramachandra Khan sent a beautiful prostitute to tempt and disgrace Haridasa at night in Phulia, Haridasa politely told her: *"Please sit and wait until I finish my daily vow of 300,000 Holy Names."* 

He chanted all night through three consecutive nights. By listening to the Holy Name emanating from Haridasa's lips, the prostitute's mind was completely purified. She wept, fell at Haridasa's feet, shaved her head, surrendered all her wealth to the poor, and became a saintly Vaishnavi devotee!

##### Pastime 2: Surviving Beating in 22 Marketplaces (Caitanya Bhagavata Adi 16)
When the local Muslim ruler (Kazi) imprisoned Haridasa for chanting Hindu mantras, the Kazi ordered him to be beaten continuously across **22 marketplaces** until he died. 

As executioners struck his back with heavy whips, Haridasa felt no pain; instead, absorbed in samadhi, he prayed for the executioners: *"O my Lord Krishna! Please be merciful upon these poor men and do not hold them guilty for striking me!"* 

Stunned that Haridasa remained alive and smiling after 22 marketplaces of whip beatings, the executioners released him, recognizing him as a divine saint!

##### Pastime 3: Defeating the Venomous Snake at Benapole
While Haridasa lived in a cave at Benapole, a deadly black cobra resided in a hole inside the same cave. Visitors feared the snake, but Haridasa remained peaceful. Finally, to relieve the anxiety of his visitors, the giant cobra slithered out of its hole, bowed down to Haridasa Thakura, and departed from the cave forever.

##### Pastime 4: Glorious Disappearance in Jagannath Puri (Antya 11)
Feeling his advanced age, Haridasa expressed his final desire to pass away while gazing upon Lord Caitanya's lotus face. 

In Jagannath Puri, surrounded by Lord Caitanya, Lord Nityananda, Svarupa Damodara, and all Vaishnavas, Haridasa sat on the ground, placed Lord Caitanya's lotus feet upon his chest, stared directly into Mahaprabhu's golden face, and loudly chanted *"Sri Krsna Caitanya!"* as his life air departed from his body. 

Lord Caitanya picked up Haridasa's body in His arms and danced in wild, weeping ecstasy through Jagannath Puri, personally carrying Haridasa's body to the sea shore, burying him with His own hands, and distributing *maha-prasadam* to thousands!

---

#### 3. Spiritual Significance & Observance Guidelines
Srila Haridasa Thakura demonstrates that birth, caste, and social status are completely irrelevant in chanting the Holy Name.

- **Fasting Rules:** Fasting is observed until noon (12:00 PM).
- **Festival Activities:** Reading *Caitanya-caritamrta* Antya Lila Chapter 11 (Disappearance of Srila Haridasa Thakura), chanting 64 or 192 rounds of the Hare Krishna Maha-Mantra, and kirtana.
- **Noon Parana:** Feast offering presented at noon, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Haridasa Thakura on his Disappearance day for taste in chanting the Holy Name (*nāme ruci*) and freedom from offences (*nāmāparādha*).

**Pranama Mantra:**
> *namo namas te haridāsa-nāmnā*  
> *nāmācāryāya mahātmane*  
> *kṛṣṇa-nāma-sudhā-dhārā-pravāhāyātmabindune*  
>  
> *"I offer my respectful obeisances unto Srila Haridasa Thakura, the exalted Namacharya, who flooded the world with the nectarine stream of Krishna's Holy Name."*
"""
    },
    'Svarupa Damodara': {
        'title': 'Sri Svarupa Damodara Gosvami',
        'story': """### Sri Svarupa Damodara Gosvami: Incarnation of Lalita Sakhi

#### 1. Eternal Identity & Lineage
In Vraja-lila, Sri Svarupa Damodara Gosvami (Purushottama Acharya) is **Lalita Sakhi** (the chief intimate gopi associate of Srimati Radharani). He was the confidential personal secretary, alter-ego (*dvitīya-kalevara*), and constant companion of Lord Sri Caitanya Mahaprabhu in Jagannath Puri. He was born in Navadvipa.

---

#### 2. Sacred Pastimes from Sri Caitanya-caritamrta (Madhya & Antya Lila)

##### Pastime 1: Becoming Mahaprabhu's Second Body (Dvitiya-Kalevara)
When Svarupa Damodara accepted *sannyāsa* (without accepting the *tridaṇḍa* cloth or title, wearing simple *brahmacārī* white garments), he traveled directly to Jagannath Puri. 

The moment Lord Caitanya saw Svarupa Damodara, He embraced him in divine ecstasy, declaring: *"Svarupa Damodara is My second body! Whatever I feel in My heart, Svarupa Damodara understands instantly!"*

##### Pastime 2: Guardian of Gaudiya Siddhanta & Literature
No poet, scholar, or devotee could present any song, poem, or scripture to Lord Caitanya Mahaprabhu without Svarupa Damodara's strict prior examination. If a work contained the slightest trace of Mayavada (impersonalism), *rasābhāsa* (incompatible mellows), or philosophical error, Svarupa Damodara immediately rejected it to protect Mahaprabhu's delicate ecstatic moods.

##### Pastime 3: Singing Confidential Songs in the Gambhira
Night after night inside the Gambhira, as Lord Caitanya swooned in the unbearable agony of separation from Krishna (*vipralambha-bhāva*), Svarupa Damodara sang exquisite *padāvalī* songs from *Gīta-govinda*, *Kṛṣṇa-karṇāmṛta*, and the poems of Vidyapati and Chandidasa, soothing Mahaprabhu's heart.

##### Pastime 4: Authoring the Kadacha (Personal Diary)
Svarupa Damodara maintained a confidential personal diary (**Kaḍacā**), recording the most intimate, internal reasons for Lord Caitanya's advent and His Gambhira pastimes. This notebook served as the primary source text for Srila Rupa Gosvami, Srila Sanatana Gosvami, and Srila Krsnadasa Kaviraja Gosvami's *Caitanya-caritamrta*.

---

#### 3. Spiritual Significance & Observance Guidelines
Sri Svarupa Damodara Gosvami teaches the highest standard of pure Gaudiya *siddhānta* and *vipralambha-bhāva*.

- **Fasting Rules:** Fasting is observed until noon (12:00 PM).
- **Festival Activities:** Reading *Caitanya-caritamrta* Adi Lila 1.41–46 and Antya Lila, singing *padāvalī-kīrtana*, and studying Gaudiya philosophy.
- **Noon Parana:** Feast offering presented at noon, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Sri Svarupa Damodara Gosvami on his Disappearance day for razor-sharp fidelity to Srila Prabhupada's teachings, freedom from Mayavada contamination, and relish of Harinama.

**Pranama Mantra:**
> *namas te svarūpāya gaura-dvitīya-mūrtaye*  
> *lalitā-rūpa-dhāriṇe rasāmbho-nidhaye namaḥ*  
>  
> *"I offer my respectful obeisances unto Sri Svarupa Damodara Gosvami, the second body of Lord Caitanya, who is Lalita Sakhi in Vraja-lila and an ocean of divine rasa."*
"""
    },
    'Ramananda Raya': {
        'title': 'Sri Ramananda Raya',
        'story': """### Sri Ramananda Raya: Incarnation of Visakha Sakhi

#### 1. Eternal Identity & Lineage
In Vraja-lila, Sri Ramananda Raya is **Visakha Sakhi** (the intimate confidential sakhi of Srimati Radharani). He was a high minister (*Governor of Rajamahendri*) under Emperor Prataparudra of Orissa, residing on the banks of the Godavari River and later in Jagannath Puri. He is glorified as one of the two main pillars of Lord Caitanya's intimate pastimes in Puri (alongside Svarupa Damodara).

---

#### 2. Sacred Pastimes from Sri Caitanya-caritamrta (Madhya Lila 8 & Antya Lila)

##### Pastime 1: The Historical Meeting on the Godavari River (Rāmānanda-Saṁvāda)
When Lord Caitanya traveled to South India, He sought out Ramananda Raya at Vidyanagar on the banks of the Godavari River. 

Though Ramananda was a wealthy royal governor wearing fine silks, when he saw Lord Caitanya in sannyasi robes, he fell at Mahaprabhu's feet weeping. Mahaprabhu embraced him, and both swooned in torrential floods of ecstatic tears.

##### Pastime 2: The Progressive Truths of Devotion (Madhya 8)
Night after night, Mahaprabhu questioned Ramananda Raya: *"What is the goal of life? Speak further!"* 

Ramananda systematically elevated the definition of spiritual perfection: from varna-dharma to karma-tyaga, jnana-mishra bhakti, pure bhakti, dasya-rasa, sakhya-rasa, vatsalya-rasa, and finally to **madhurya-rasa** (conjugal love). 

When Mahaprabhu pressed further, Ramananda revealed the supreme pinnacle of devotion: **Radha-krsna-prema** and Srimati Radharani's unmatchable mood of service.

##### Pastime 3: Revealing the Combined Form of Sri Rasaraj-Mahabhava
Seeing Ramananda hesitating to speak higher truths, Lord Caitanya revealed His most confidential form to Ramananda Raya: the combined form of **Sri Krishna (Rasaraja)** and **Srimati Radharani (Mahabhava)**—blazing like molten gold and holding a flute! 

Seeing this vision, Ramananda Raya swooned in ecstasy. Mahaprabhu instructed him to keep this secret sealed from worldly eyes.

##### Pastime 4: Authoring Jagannatha-vallabha Nataka
Ramananda resigned from his royal governorship to live in Jagannath Puri as Mahaprabhu's constant companion. He composed the immortal Sanskrit drama **Jagannātha-vallabha-nāṭaka**, depicting the sweet pastimes of Radha and Krishna, which brought supreme joy to Lord Caitanya in the Gambhira.

---

#### 3. Spiritual Significance & Observance Guidelines
Sri Ramananda Raya teaches the ultimate zenith of *rāgānugā-bhakti* and *radha-dasyam*.

- **Fasting Rules:** Fasting is observed until noon (12:00 PM).
- **Festival Activities:** Reading *Caitanya-caritamrta* Madhya Lila Chapter 8 (*Rāmānanda-Saṁvāda*), singing *Jagannatha-vallabha* songs, and kirtana.
- **Noon Parana:** Feast offering presented at noon, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Sri Ramananda Raya on his Disappearance day for entrance into the confidential mellows of *radha-dasyam*.

**Pranama Mantra:**
> *namo rāmānandāya rāya-saṁjñakāya mahātmane*  
> *viśākhā-rūpa-dhāriṇe gaura-prema-rasābdhaye*  
>  
> *"I offer my respectful obeisances unto Sri Ramananda Raya, the great soul who is Visakha Sakhi in Vraja-lila, and an ocean of divine love for Sri Caitanya Mahaprabhu."*
"""
    },
    'Virabhadra': {
        'title': 'Sri Virabhadra',
        'story': """### Sri Virabhadra Gosvami: Incarnation of Kshirodakasayi Vishnu

#### 1. Eternal Identity & Lineage
In Vraja-lila, Sri Virabhadra Gosvami (Viracandra) is **Kshirodakasayi Vishnu** (and an expansion of Lord Balarama). Glorified in *Caitanya-caritamrta* (Adi 11.8–12) as the supreme branch of the desire tree of Lord Nityananda Prabhu (*śrī-vīrabhadra gosāñi -- nityānanda-skandha*), he was born in Khardaha (Bengal) as the divine son of **Lord Nityananda Prabhu** and Srimati Vasudha Devi (raised under Mother Jahnava Devi).

---

#### 2. Sacred Pastimes from Sri Caitanya-caritamrta (Adi 11) & Bhakti-ratnakara

##### Pastime 1: Glorification as the Crown Jewel of Nityananda's Lineage
Srila Krsnadasa Kaviraja Gosvami writes in *Caitanya-caritamrta* (Adi 11.8–9):  
*"Sri Virabhadra Gosani is the main trunk of the Nityananda branch. He is Lord Vishnu Himself (*kṣīrodakaśāyī*). Through his potency, Lord Caitanya's message flooded the entire universe!"*

##### Pastime 2: Converting 1,200 Buddhist Monks (Nera-Neris)
In Bengal, 1,200 vows-bound Buddhist tantric renunciates (**Neḍā-Neḍīs**) lived without authentic Vaishnava initiation. 

Virabhadra Gosvami blessed them all with Harinama initiation, integrated them into pure Gaudiya Vaishnavism, and empowered them as householders and kirtana singers, ending centuries of pseudo-monastic confusion.

##### Pastime 3: The Miracle of the Black Stone at Vrindavan
When Virabhadra Gosvami visited Vrindavan, he acquired a giant black stone from the King of Jaipur. By his divine touch, he carved the stone into two breathtaking Deities: **Sri Radharamana** and **Sri Syamasundara** (worshipped in Khardaha, Bengal).

##### Pastime 4: Unifying the Gaudiya Community
Alongside Mother Jahnava Devi, Virabhadra Gosvami organized regional kirtana conventions, establishing absolute harmony, pure liturgical standards, and devotion across Bengal and Odisha.

---

#### 3. Spiritual Significance & Observance Guidelines
Sri Virabhadra Gosvami is worshiped on his Appearance day for spiritual strength and freedom from spiritual confusion.

- **Fasting Rules:** Fasting is observed until noon (12:00 PM).
- **Festival Activities:** Abhisheka of Sri Sri Gaura-Nitai / Sri Virabhadra Deities, offering white/blue silk garments, flowers, and reading *Caitanya-caritamrta* Adi Lila Chapter 11.
- **Noon Parana:** Feast offering presented at noon, followed by taking *prasādam* break-fast (*pāraṇā*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Sri Virabhadra Gosvami on his Appearance day for total surrender to Lord Nityananda's lotus feet.

**Pranama Mantra:**
> *namas te vīrabhadrāya nityānanda-sutātmane*  
> *kṣīrodakaśāyī-rūpā-kṛpā-sindho namo 'stu te*  
>  
> *"I offer my respectful obeisances unto Sri Virabhadra Gosvami, the divine son of Lord Nityananda Prabhu, who is Kshirodakasayi Vishnu Himself and a boundless ocean of mercy."*
"""
    }
}


def populate_panchatattva_descriptions():
    updated_count = 0
    for key_name, data in PANCHATTATVA_STORIES.items():
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
    help = 'Populate detailed scriptural stories for Pancha-Tattva, Divine Consorts & Intimate Associates observances.'

    def handle(self, *args, **options):
        count = populate_panchatattva_descriptions()
        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated stories for {count} Pancha-Tattva / Associate observances in Vaishnava Calendar.")
        )
