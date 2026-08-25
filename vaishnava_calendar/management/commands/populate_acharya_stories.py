import logging
from django.core.management.base import BaseCommand
from vaishnava_calendar.models import CalendarObservance, CalendarObservanceTranslation

logger = logging.getLogger(__name__)

ACHARYA_STORIES = {
    'Sri Gadadhara Pandita': {
        'title': 'Sri Gadadhara Pandita',
        'story': """### Sri Gadadhara Pandita: The Incarnation of Srimati Radharani

#### 1. Eternal Identity & Lineage
In the *Gaura-ganoddesa-dipika* (verses 147–153), Srila Kavi-karnapura reveals that Sri Gadadhara Pandita is none other than Srimati Radharani, the internal pleasure potency (*hlādinī-śakti*) of Lord Sri Krishna, appearing in Gaura-lila. Just as Srimati Radharani is the ultimate shelter of devotion in Vrindavan, Sri Gadadhara Pandita is the chief associate of Lord Caitanya Mahaprabhu in Navadvipa and Jagannath Puri. He was born in Chatra (Chittagong) to Madhava Nayaka and Ratnavati Devi, and grew up as an intimate childhood companion of Nimai Pandit in Navadvipa.

---

#### 2. Sacred Life & Inspiring Pastimes from Sri Caitanya-caritamrta

##### Pastime 1: Meeting Srila Pundarika Vidyanidhi (Caitanya-caritamrta Madhya 16)
When Sri Mukunda Datta took young Gadadhara Pandita to meet Srila Pundarika Vidyanidhi in Navadvipa, Gadadhara saw Pundarika sitting on a luxurious silk bed, wearing fine perfumed garments and smoking an ornate pipe. Gadadhara initially doubted whether such a worldly-looking person could be a pure devotee.

Sensing Gadadhara's mind, Mukunda Datta began reciting a famous verse from *Srimad-Bhagavatam* (3.2.23) describing Krishna's mercy to the demoness Putana (*aho bakī yaṁ stana-kāla-kūṭaṁ...*). 

Hearing Krishna's magnanimity, Pundarika Vidyanidhi was instantly seized by intense divine ecstasy. Tears flooded from his eyes like torrents of rain, his hair stood on end, he tore his fine silk clothes, smashed the brass lampstand, and fell unconscious onto the floor! Seeing this matchless exhibition of *kṛṣṇa-prema*, Gadadhara Pandita wept in deep repentance for having judged Pundarika externally. To erase his offense, Gadadhara immediately surrendered to Pundarika Vidyanidhi and accepted him as his spiritual master.

##### Pastime 2: The Loving Obstinacy of Kshetra-Sannyasa (Caitanya-caritamrta Madhya 16.130–149)
After Sri Caitanya Mahaprabhu took *sannyasa* and resided in Jagannath Puri, Gadadhara Pandita took *kṣetra-sannyasa*—a sacred vow never to step outside the holy limits of Puri. At the Tota-Gopinatha temple, Gadadhara installed and lovingly served the Deity of Sri Tota-Gopinatha.

When Lord Caitanya prepared to journey to Vrindavan, Gadadhara Pandita insisted on giving up his *kṣetra-sannyasa* vow to accompany Mahaprabhu. 
Lord Caitanya pleaded with him: *"Giving up your vow of kshetra-sannyasa to follow Me is a great offense to Lord Jagannath. You must stay here and serve Tota-Gopinatha."*

Gadadhara Pandita answered with profound, emotional surrender:  
*"Wherever You are, my Lord, is Jagannath Puri! My kshetra-sannyasa and my Gopinatha worship are wherever Your lotus feet abide. Let all offenses fall upon me, but I cannot leave Your side!"*

Seeing Gadadhara's unyielding affection, Mahaprabhu took his hands and said: *"If you abandon Gopinatha, it will break My heart and destroy My mission. If you truly love Me, return to Nilacala and serve Gopinatha."* Hearing these loving, firm words, Gadadhara collapsed unconscious in separation as Mahaprabhu boarded the boat.

##### Pastime 3: Tota-Gopinatha Kneels for His Devotee
As the years passed, Gadadhara Pandita grew weak from separation and aging, making it very difficult for him to reach up and place flower garlands around the neck of the tall Deity of Sri Tota-Gopinatha. 

Understanding the agony of His beloved servant, Sri Tota-Gopinatha performed a sweet miracle: the Deity sat down in a kneeling position (*padmāsana*) so that Gadadhara Pandita could easily dress and garland Him every day! To this day in Jagannath Puri, Sri Tota-Gopinatha remains the only sitting Deity of Lord Krishna in the world, standing as eternal proof of the Lord's affection for Gadadhara Pandita.

##### Pastime 4: Dissolving the Pages of Srimad-Bhagavatam
Every afternoon at Tota-Gopinatha temple, Lord Caitanya Mahaprabhu came to listen to Gadadhara Pandita recite *Srimad-Bhagavatam*, particularly the stories of Dhruva Maharaja and Prahlada Maharaja. As Gadadhara recited, torrents of tears flowed from his eyes onto the pages of the scripture, washing away the ink. Lord Caitanya would hold Gadadhara in His arms, both of them submerged in an ocean of divine ecstatic love.

---

#### 3. Major Contributions to Vaishnavism
- **Establishment of Sri Tota-Gopinatha Temple:** Left an immortal center of pure Deity worship and *rāgānugā-bhakti* in Jagannath Puri.
- **Ultimate Paragon of Radharani's Mood:** Taught the world the deepest mood of divine love in separation (*vipralambha-bhava*).
- **Master Class in Bhagavatam Recitation:** Demonstrated that *Srimad-Bhagavatam* is not an intellectual text, but a living stream of divine affection to be relished with tears of love.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Sri Gadadhara Pandita on both his Appearance day (Vaisakha Sukla Dwitiya) and Disappearance day (Jyeshtha Amavasya) for gaining a deep, unshakeable taste for *Srimad-Bhagavatam* and pure attachment to the lotus feet of Sri Caitanya Mahaprabhu.

**Pranama Mantra:**
> *vande śrī-gadādhara-gaura-pādābja-sevinam*  
> *bhaktimantaṁ mahā-bhāgaṁ gaura-kīrtana-nartanam*  
>  
> *"I offer my respectful obeisances unto Sri Gadadhara Pandita, who is constantly engaged in serving the lotus feet of Sri Gaurasundara with deep devotion, absorbed in the ecstatic chanting and dancing of Gaura-kirtana."*
"""
    },
    'Sri Madhavendra Puri': {
        'title': 'Sri Madhavendra Puri',
        'story': """### Sri Madhavendra Puri: The Root of the Tree of Divine Love

#### 1. Eternal Identity & Lineage
Srila Krsnadasa Kaviraja Gosvami glorifies Srila Madhavendra Puri in *Sri Caitanya-caritamrta* (Adi 9.10) as the sprout and original root of the devotional desire tree of pure love of Godhead (*prema-kalpataru*). He belonged to the Brahma-Madhva Sampradaya as the disciple of Srila Lakshmipati Tirtha, and became the grand-spiritual master (*parama-guru*) of Sri Caitanya Mahaprabhu through his initiated disciple, Srila Isvara Puri. He also initiated Sri Advaita Acarya. Madhavendra Puri was the first Great Acarya in the Madhva line to openly manifest the confidential mellows of conjugal love (*mādhurya-rasa*) and intense separation (*vipralambha-bhava*).

---

#### 2. Inspiring Pastimes from Sri Caitanya-caritamrta (Madhya Lila, Chapter 4)

##### Pastime 1: Unearthing Sri Gopalaji on Govardhana Hill
While performing *parikramā* of Vrindavan, Madhavendra Puri reached Govardhana Hill. Taking bath at Govinda-kunda, he sat under a tree to perform his evening worship without asking anyone for food (*ayācaka-vṛtti*). 

Suddenly, a beautiful dark cowherd boy came carrying a pot of milk, smiled gently, and handed it to Madhavendra Puri, saying: *"Drink this milk, Swamiji. In My village, no one goes hungry."* When Madhavendra Puri asked who he was, the boy replied: *"I am a cowherd boy of this village. I will return later to fetch the pot."*

That night in a dream, the same boy took Madhavendra Puri by the hand to a nearby thicket and revealed: *"I am Sri Gopala, the lifter of Govardhana Hill! My priest hid Me in this bush during a Turkish invasion. I have been burning in heat and cold here for a long time. Please excavate Me and install Me on top of the hill!"*

The next morning, Madhavendra Puri assembled the villagers, cleared the thickets, and unearthed the heavy golden-black Deity of Sri Gopalaji. They triumphantly carried Gopalaji to the top of Govardhana Hill, performed an elaborate *abhiṣeka*, and held a monumental **Annakuta Festival** with mountains of rice, vegetables, and sweets—re-enacting Lord Krishna's original pastime!

##### Pastime 2: Ksiracora Gopinatha — The Lord Who Stole Condensed Milk
To cool Sri Gopalaji with sandalwood paste, Madhavendra Puri traveled on foot toward Jagannath Puri. En route, he stopped at Remuna in Odisha to see Sri Gopinatha Deity. Seeing twelve pots of sweet condensed milk (*kṣīra*) offered to Gopinatha every evening, Madhavendra Puri thought in his mind: *"If I could taste just a drop of this milk, I could learn how to prepare it to offer to my Gopalaji."* 

Immediately, he felt deeply ashamed for harboring a desire to taste food before it was officially offered to the Lord. Condemning himself, he left the temple without asking anyone for food and slept under a tree in the vacant village market.

That night, Lord Gopinatha appeared in a dream to the head pujari of the temple and said: *"Wake up, pujari! I have hidden a pot of milk under My lower garment! Take it immediately and give it to My devotee Madhavendra Puri, who is sleeping in the marketplace."*

The priest rushed into the sanctum, found the pot of sweet milk behind Gopinatha's garment, and ran through the streets shouting: *"Take this milk! Whosoever is named Madhavendra Puri, come forward! For your sake, Gopinatha has stolen a pot of milk!"* Madhavendra Puri drank the stolen milk with tears of ecstasy. From that historic night, the Deity became immortalized as **Ksira-cora Gopinatha** (Gopinatha who stole milk).

##### Pastime 3: Sandalwood for Gopalaji
Continuing to Jagannath Puri, Madhavendra Puri obtained one maund (approx. 40 kg) of precious sandalwood and camphor from the King of Orissa. On his return journey through Remuna, Sri Gopalaji appeared to him again in a dream, saying: *"My dear Puri, I have already received all the sandalwood you gathered. Gopinatha's body and My body are non-different. If you grind this sandalwood paste and smear it on Gopinatha's body in Remuna, My burning sensation will be relieved."* Madhavendra Puri joyously spent the entire hot summer season in Remuna grinding sandalwood for Gopinatha.

##### Pastime 4: The Ultimate Verse of Separation (*Ayi Dīna-Dayādrta-Nātha He*)
During his final days in Remuna, Madhavendra Puri was submerged in agonizing love of separation from Lord Krishna. He constantly chanted a verse (*Caitanya-caritamrta Madhya 4.197*) that later became the foundational jewel of Gaudiya philosophy:

> *ayi dīna-dayārdrta-nātha he*  
> *mathurā-nātha kadāvalokyase*  
> *hṛdayaṁ tvad-aloka-kātaraṁ*  
> *dayita bhrāmyati kiṁ karomy aham*  
>  
> *"O Lord whose heart is melted with mercy for the helpless! O Lord of Mathura! When will I see You again? My heart is tormented in Your absence! O Beloved, I am wandering in distress—what shall I do now?"*

Srila Krsnadasa Kaviraja Gosvami declares that Sri Caitanya Mahaprabhu Himself would recite this very verse in Jagannath Puri, swooning in divine ecstasy.

---

#### 3. Major Contributions to Vaishnavism
- **Unearthing Sri Gopalaji:** Established the Deity of Sri Nathji / Gopalaji on Govardhana Hill.
- **Cornerstone of Gaudiya Sampradaya:** Transfused *mādhurya-rasa* and *vipralambha* into the Madhva lineage, paving the way for Sri Caitanya Mahaprabhu's advent.
- **Ksiracora Gopinatha Leela:** Demonstrated the supreme truth that Lord Krishna breaks His own rules to serve and fulfill the pure desires of His unalloyed devotee.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Madhavendra Puri on his Disappearance day (Phalguna Krishna Dwadasi) and Appearance day (Vaisakha Sukla Saptami) for *ayācaka-vṛtti* (complete faith in Krishna's maintenance) and for gaining the ultimate gift of *kṛṣṇa-prema* in separation.

**Pranama Mantra:**
> *śrīmad-rāsarasāmboji-janārka-kula-bhāskaram*  
> *vande mādhavapurīṁ śrīmad-īśvara-pūri-gurum*  
>  
> *"I offer my respectful obeisances unto Srila Madhavendra Puri, the spiritual master of Sri Isvara Puri, who shines like the sun in the sky of unalloyed devotional love, revealing the sweetness of the rasa-lila."*
"""
    },
    'Sri Madhvacarya': {
        'title': 'Sri Madhvacarya',
        'story': """### Sri Madhvacarya: The Founder of Tattvavada (Brahma-Madhva Sampradaya)

#### 1. Eternal Identity & Lineage
Sri Madhvacarya (1238–1317 CE) is recognized in scriptural tradition as the third incarnation of Mukhyaprana (Vayu Deva)—the first being Sri Hanuman in Treta-yuga, the second being Sri Bhimasena in Dvapara-yuga, and the third being Sri Madhvacarya in Kali-yuga. He established the **Tattvavada** (Dvaita Vedanta) school within the Brahma Sampradaya. He was born on Vijaya Dasami in Pajaka village near Udupi, Karnataka, to Madhyageha Bhatta and Vedavati Devi, and was named Vasudeva at birth.

---

#### 2. Sacred Life & Inspiring Pastimes

##### Pastime 1: Childhood Miracles of Young Vasudeva
From early childhood, Vasudeva manifested superhuman intellect and divine strength. Once, when his father was burdened by heavy debts to a ruthless creditor, young Vasudeva gave the creditor a handful of tamarind seeds. The moment the seeds touched the creditor's hands, they miraculously turned into solid gold coins, completely liquidating his father's debt! 

On another occasion, when a cobra attacked him in the forest, young Vasudeva crushed the deadly serpent beneath his big toe without any effort. At age five, he effortlessly digested a giant basket of boiled horse-grams (*kollu*) intended for an ox, showing his identity as Vayu Deva.

##### Pastime 2: Defeating Mayavada and Establishing Tattvavada
At age sixteen, Vasudeva took *sannyāsa* from Achyutapreksha Tirtha and was named **Purna-prajna** (and later Anandatirtha / Madhvacarya). When his guru began lecturing on Mayavada (impersonalism), Madhvacarya immediately pointed out thirty-two fundamental fallacies in Adi Shankara's commentary on the spot! 

He established *Tattvavada*, proving through Vedic sound revelation that Lord Sri Vishnu is the Supreme Absolute Truth (*sarvottama*), eternally personal, possessor of all infinite auspicious qualities (*sakala-guṇa-pūrṇa*), and eternally distinct from the individual jiva souls (*bheda*).

##### Pastime 3: Pilgrimage to Badarikashrama and Meeting Srila Vyasadeva
Madhvacarya journeyed on foot to the high Himalayas to Badarikashrama. Crossing impassable snowy cliffs, he entered the hidden hermitage of **Srila Veda Vyasa** (Vyasadeva). Vyasadeva affectionately embraced Madhvacarya as His eternal servant Vayu, blessed him, and presented him with eight sacred Salagrama-silas (including Kalingamardana and Hayagriva). Vyasadeva instructed Madhvacarya to write commentaries (*Brahma-sūtra Bhāṣya*) to establish pure dualistic devotion across India.

##### Pastime 4: Unearthing Udupi Sri Krishna from Gopi-Chandana
While sitting in deep meditation on the seashore at Malpe (near Udupi), Madhvacarya foresaw through divine vision a merchant ship from Dvaraka caught in a violent storm. Waving his saffron cloth, Madhvacarya calmed the churning ocean waves and safely guided the ship to shore.

The overjoyed captain offered Madhvacarya any precious cargo from the ship. Madhvacarya asked only for a heavy block of *gopī-candana* clay used as ballast in the ship's hold. When Madhvacarya washed away the clay, he revealed the breathtaking Deity of **Udupi Sri Krishna** holding a churning rod (*manthana-koḷu*) and rope—the exact Deity carved by Vishvakarma and worshipped by Srimati Rukmini Devi in Dvaraka! 

Madhvacarya carried the Deity on his shoulders to Udupi while spontaneously composing the famous *Dvādaśa-stotra*. He installed Sri Krishna in Udupi and established eight monastic orders (**Ashta Mathas**) with eight sannyasi disciples to conduct unbroken daily worship.

---

#### 3. Major Contributions to Vaishnavism
- **Establishment of Tattvavada (Dvaita Vedanta):** Refuted Mayavada impersonalism and firmly established the eternal supremacy and personality of Lord Vishnu.
- **Installation of Udupi Sri Krishna & Ashta Mathas:** Formed the spiritual capital of Karnataka at Udupi with 24x7 unbroken Deity worship.
- **Sarvamoola Granthas:** Authored 37 landmark commentaries on Brahma Sutras, Bhagavad Gita, Upanishads, and Bhagavata Tatparya Nirnaya.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Sri Madhvacarya on his Disappearance day (Magha Sukla Navami) and Appearance day (Vijaya Dasami) for gaining razor-sharp clarity in Vaishnava philosophy, protection from impersonal philosophy, and unalloyed devotion unto Lord Sri Krishna.

**Pranama Mantra:**
> *namaste prāṇanāthāya viṣṇu-pādābja-bhānave*  
> *namo mādhavacāryāya mahā-kāruṇikātmane*  
>  
> *"I bow down to Sri Madhvacarya, the Lord of life energy (Vayu), who is like the blazing sun shining upon the lotus feet of Lord Vishnu, and whose heart is filled with supreme compassion for all living beings."*
"""
    },
    'Sri Raghunandana Thakura': {
        'title': 'Sri Raghunandana Thakura',
        'story': """### Sri Raghunandana Thakura: The Child Devotee Who Fed Sri Gopinatha

#### 1. Eternal Identity & Lineage
In the *Gaura-ganoddesa-dipika* (verse 176), Srila Kavi-karnapura reveals that Sri Raghunandana Thakura is **Kandarpa Manjari** (and an incarnation of Pradyumna) in Vraja-lila. He was born in Srikhanda village (Bengal) into the noble physician family of Sri Mukunda Dasa, who was a premier intimate associate of Lord Sri Caitanya Mahaprabhu.

---

#### 2. Inspiring Pastimes from Sri Caitanya-caritamrta & Bhakti-ratnakara

##### Pastime 1: The Child Who Compelled Sri Gopinatha to Eat (Caitanya-caritamrta Madhya 15.112–117)
When Raghunandana was just five years old, his father Mukunda Dasa had to leave home urgently on medical duties. Before leaving, Mukunda instructed young Raghunandana: *"My dear son, today you offer the bhoga to our family Deity, Sri Gopinatha. Make sure He eats everything."*

Child Raghunandana placed the plate of fresh sweet *laddus* before Sri Gopinatha, sat down, and waited for the Deity to eat. When Gopinatha remained motionlessly smiling on the altar, little Raghunandana began crying uncontrollably, pleading: *"My father told me You must eat this food! Why are You not eating? If You don't eat, my father will be very angry with me!"*

Moved by the innocent, intense, unalloyed affection of the five-year-old boy, the Deity of Sri Gopinatha personally reached out His hand, picked up every single *laddu*, and ate the entire offering! 

When Mukunda returned and asked for Gopinatha's *prasādam*, Raghunandana innocently answered: *"Father, Gopinatha ate everything!"* Astonished and bewildered, Mukunda placed another *laddu* behind a door to test the boy. Watching secretly through a crack in the door, Mukunda saw Sri Gopinatha personally take the *laddu*, bite off half, and hold the remaining half in His hand! Mukunda broke down in weeping ecstasy, embracing his extraordinary son.

##### Pastime 2: Who is the Father and Who is the Son?
In Jagannath Puri, Lord Caitanya Mahaprabhu once lovingly questioned Mukunda Dasa in front of all the devotees: *"Mukunda, tell Me: between you and Raghunandana, who is the father and who is the son?"*

Mukunda Dasa folded his hands in humility and replied: *"My Lord, Raghunandana is my father, and I am his son! Because Raghunandana has awakened pure Krishna-prema in my heart and brought Gopinatha into our life, he is my spiritual father."* 

Lord Caitanya smiled joyously and declared: *"Whoever awakens our Krishna-bhakti is indeed our father and spiritual guide!"*

##### Pastime 3: The Daily Kadamba Flowers of Srikhanda
At the bathing pond in Srikhanda where Raghunandana performed his daily ablutions, a miracle occurred every single day: two fresh Kadamba flowers bloomed on a tree year-round, regardless of season, solely for Raghunandana to pick and offer to Sri Gopinatha!

##### Pastime 4: The Flying Anklet (Nupura-Kunda)
When the formidable cowherd associate Sri Abhirama Thakura visited Srikhanda, he bowed to young Raghunandana to test his spiritual potency. Raghunandana remained untouched by Abhirama's intense power and began dancing in wild *gaura-kīrtana*. During his ecstatic dance, one of Raghunandana's silver anklets (*nūpura*) flew off his foot and landed miles away in Akaihat, creating a holy pond known to this day as **Nupura-kunda**.

---

#### 3. Major Contributions to Vaishnavism
- **Pioneer of Srikhanda Sampradaya:** Established Srikhanda as one of the premier centers of Gaudiya kirtana and sweet Gopinatha worship.
- **Embodiment of Pure Vatsalya-Sakhya Bhava:** Taught humanity that childlike, uncalculating love (*viśvāsa*) has the power to compel the Supreme Absolute Truth to break all Deity worship barriers.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Sri Raghunandana Thakura on his Appearance day (Magha Sukla Dwitiya) and Disappearance day (Sravana Sukla Dwitiya) for childlike, unwavering faith that melts the heart of Lord Sri Krishna and Sri Gopinatha.

**Pranama Mantra:**
> *namas te śrī-raghunandanāya kṛpā-sindhave*  
> *gopīnātha-mukha-prema-bhojana-kāriṇe*  
>  
> *"I offer my respectful obeisances unto Sri Raghunandana Thakura, an ocean of mercy, whose innocent love compelled Lord Sri Gopinatha to eat directly from his hand."*
"""
    },
    'Sri Ramanujacarya': {
        'title': 'Sri Ramanujacarya',
        'story': """### Sri Ramanujacarya: The Incarnation of Sri Ananta Sesha (Sri Sampradaya)

#### 1. Eternal Identity & Lineage
Scriptural tradition recognizes Sri Ramanujacarya (1017–1137 CE) as the incarnation of Sri Ananta Sesha (and Lakshmana), appearing to preserve and spread the **Sri Sampradaya** (descending from Srimati Lakshmi Devi). He established the **Viśiṣṭādvaita** (Qualified Non-Dualism) philosophy. He was born in Sriperumbudur, Tamil Nadu, to Asuri Kesava Somayaji and Kanthimathi Ammal, and was named Ilaya Perumal (Ramanuja).

---

#### 2. Sacred Life & Inspiring Pastimes from Prapannamritam

##### Pastime 1: Shouting the Secret Ashtakshari Mantra from the Temple Tower
Determined to receive sacred initiation into the eight-syllable *Aṣṭākṣarī Mantra* (*Om Namo Narayanaya*), Ramanujacarya walked on foot eighteen times from Srirangam to Thirukoshtiyur to beg his guru, Srila Goshthipurna (Thirukoshtiyur Nambi). 

Goshthipurna finally revealed the mantra under strict vow: *"This mantra is so powerful that whoever hears it will immediately be freed from all sins and attain Vaikuntha. If you reveal it to anyone, you will suffer eternal damnation in hell."*

The very next hour, Ramanujacarya climbed to the top of the massive *gopuram* tower of the Thirukoshtiyur temple. He called out to all the townspeople—regardless of caste, age, or status—and shouted the sacred *Aṣṭākṣarī Mantra* at the top of his lungs for everyone to hear!

Goshthipurna rushed up the tower in fury: *"You have disobeyed your Guru! You will go to hell!"* 
Ramanujacarya bowed at his guru's feet with tearful humility: *"My lord, if millions of fallen souls are liberated from material suffering by hearing this mantra, I will gladly suffer in hell for eternity!"* Overwhelmed by Ramanuja's boundless compassion, Goshthipurna embraced him weeping and bestowed upon him the title **Emberumanar** ("My Superior Lord").

##### Pastime 2: Rescuing Sampat-Kumara (Chella Pillai) from Delhi
When invaders raided the sacred temple of Thiru Narayanapuram (Melukote, Karnataka) and carried off the processional Deity of Sampat-kumara to Delhi, Ramanujacarya walked all the way to Delhi to retrieve Him. 

The Sultan's young daughter (Bibi Lachhi) had taken the Deity into her bedchamber, treating Him as her beloved friend. Ramanujacarya stood at the palace door and called out with parental affection: *"Come, my dear child (Chella Pillai), come to your father!"*

Miraculously, the metallic Deity of Sampat-kumara stepped off the princess's bed, walked through the palace, jumped onto Ramanujacarya's lap, and embraced him! Ramanuja lovingly carried Chella Pillai back to Melukote.

##### Pastime 3: Defeating Impersonalism & Fulfilling Yamunacarya's Vows
Ramanujacarya traveled across the length and breadth of India, defeating impersonal Mayavada scholars and establishing *Viśiṣṭādvaita*. He proved that Lord Sriman Narayana and His consort Lakshmi Devi are the Supreme Absolute Reality, that individual souls (*jīvas*) are eternally distinct servants of the Lord, and that total surrender (*prapatti*) is the highest path. He fulfilled the three sacred vows of Srila Yamunacarya by authoring the masterwork commentary on Brahma Sutras (**Sri Bhashya**).

##### Pastime 4: Standardizing Temple Administration & Inclusion
Ramanujacarya restructured the administration of major holy places including Srirangam, Tirupati, and Melukote. He established the *Pancharatra* system of worship and created the **Thirukulathar** initiative at Melukote, granting temple entry and spiritual initiation to oppressed communities centuries ahead of his time.

---

#### 3. Major Contributions to Vaishnavism
- **Establishment of Visishtadvaita Vedanta:** Systematized the philosophical foundation of the Sri Sampradaya.
- **Prapatti & Universal Inclusion:** Opened the doors of unconditional surrender (*śaraṇāgati*) and sacred mantras to all humanity.
- **Literary Masterpieces:** Authored nine monumental texts (*Navaratnas*), including *Sri Bhashya*, *Gita Bhashya*, and *Gadya Trayam*.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Sri Ramanujacarya on his Disappearance day (Magha Sukla Dashami) and Appearance day (Chithirai Thiruvadhirai / Chaitra Sukla Shasthi) for acquiring complete surrender (*prapatti*) at the feet of Sriman Narayana and freedom from pride.

**Pranama Mantra:**
> *yo nityam acyuta-padāmbuja-yugma-rukma-*  
> *vyāmohatas tad-iterāṇi tṛṇāya mene*  
> *asmad-guroḥ bhagavato 'sya dayaikasindhoḥ*  
> *rāmānujasya caraṇau śaraṇaṁ prapadye*  
>  
> *"I take shelter at the lotus feet of our divine spiritual master, Sri Ramanujacarya, an ocean of compassion, who out of intense love for the golden lotus feet of Lord Acyuta considered all worldly objects as insignificant straw."*
"""
    },
    'Sri Rasikananda': {
        'title': 'Sri Rasikananda',
        'story': """### Sri Rasikananda Deva Gosvami: The Great Preacher of Utkala

#### 1. Eternal Identity & Lineage
In the *Gaura-ganoddesa-dipika* and Gaudiya paddhati texts, Sri Rasikananda Deva Gosvami (Rasika Murari) is recognized as **Kanaka Manjari** in Vraja-lila. He was born on Kartik Purnima in 1590 CE in Rohini village (Midnapore, near the Bengal-Odisha border) to King Achyutananda and Rani Bhavani Devi. He was the foremost empowered disciple of **Sri Syamananda Prabhu**.

---

#### 2. Sacred Life & Inspiring Pastimes from Rasika-mangala

##### Pastime 1: Taming the Mad Man-Eating Elephant (Gopaladasa)
While Rasikananda was preaching Krishna-bhakti in the kingdom of Mayurbhanj, the hostile local king Baidyanath Bhanja sought to destroy him. The king released a rogue, man-eating elephant named Gopaladasa that had killed scores of people, directing it toward Rasikananda.

As the wild elephant charged with raised trunk and terrifying trumpets, Rasikananda stood motionless in serene ecstatic trance, softly singing: *"Kṛṣṇa! Kṛṣṇa! Kṛṣṇa! Kṛṣṇa! Kṛṣṇa! Kṛṣṇa! Kṛṣṇa! he!"*

The moment Rasikananda looked into the elephant's eyes with divine compassion, the fierce beast abruptly stopped. It fell to its knees, bowed its head to the ground, tears streaming from its eyes, and placed its trunk at Rasikananda's lotus feet! Rasikananda leaned down and whispered the holy *Harināma* into the elephant's ear. From that day forward, the elephant Gopaladasa refused meat and alcohol, ate only *kṛṣṇa-prasādam*, and bowed down to every Vaishnava it met!

##### Pastime 2: Converting the Tyrannical Subahdar (Ahmed Beg)
The tyrannical Mughal governor (*Subahdar*) of Odisha, Ahmed Beg, ordered the destruction of temples and set out with soldiers to arrest Rasikananda. Undeterred, Rasikananda walked straight into Ahmed Beg's court chanting *gaura-kīrtana*.

When Ahmed Beg looked at Rasikananda, he saw a blinding golden radiance surrounding him and beheld a terrifying four-armed form of Lord Vishnu holding discus and mace standing behind Rasikananda as his protector! Trembling violently in fear, Ahmed Beg fell at Rasikananda's feet, begged for forgiveness, accepted him as his spiritual guardian, and issued royal decrees protecting all Vaishnavas and temples across Odisha.

##### Pastime 3: Establishing Sri Sri Radha-Madanamohana at Gopiballabhpur
Sri Rasikananda established the famous holy sanctuary of **Gopiballabhpur** on the banks of the Subarnarekha River. Installing the captivating Deities of Sri Sri Radha-Madanamohana, he transformed a dense, dangerous jungle inhabited by wild beasts and ruthless bandits into a radiant town of perpetual *nāma-saṅkīrtana*.

##### Pastime 4: Merging into Sri Ksira-cora Gopinatha at Remuna
On Phalguna Krishna Dwadasi in 1652 CE, Sri Rasikananda assembled his disciples at the Ksira-cora Gopinatha temple in Remuna. After singing ecstatic kirtana, he walked directly into the inner sanctum, embraced the Deity of Sri Gopinatha, and merged his physical form into the Deity before the eyes of all present!

---

#### 3. Major Contributions to Vaishnavism
- **Mass Preaching in Odisha & Bengal:** Converted royal dynasties, tribal communities, and ruthless invaders to pure Gaudiya Vaishnavism.
- **Founding of Gopiballabhpur:** Built a major seat of the Syamanandi lineage that remains a vibrant pilgrimage center.
- **Literary & Musical Compositions:** Composed devotional works including *Śyāma-rasakaḍamvadinī* and numerous *padāvalī* songs.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Sri Rasikananda Deva Gosvami on his Disappearance day (Phalguna Krishna Dwadasi) and Appearance day (Kartika Purnima) for fearless preaching potency, spiritual protection against all dangers, and unswerving attachment to Sri Sri Radha-Madanamohana.

**Pranama Mantra:**
> *śrī-śyāmānanda-priya-dāsaṁ rasikānanda-saṁjñakam*  
> *dīna-kṛpā-laṁkāra-bhūṣitaṁ taṁ namāmy aham*  
>  
> *"I offer my respectful obeisances unto Sri Rasikananda, the beloved disciple of Sri Syamananda Prabhu, who is decorated with the supreme ornament of compassion for the fallen souls."*
"""
    },
    'Sri Srinivasa Acarya': {
        'title': 'Sri Srinivasa Acarya',
        'story': """### Sri Srinivasa Acarya: The Embodiment of Gaura-Prema-Shakti

#### 1. Eternal Identity & Lineage
In the *Gaura-ganoddesa-dipika* (verse 204), Srila Kavi-karnapura reveals that Sri Srinivasa Acarya is **Mani Manjari** in Vraja-lila. He was born on Vaisakha Purnima in Chakhandi village (Bengal) to Gangadhara Bhattacarya (Chaitanya Dasa) and Lakshmipriya Devi. Before Srinivasa's birth, Lord Caitanya Mahaprabhu appeared in a dream to Gangadhara, promising that a son would be born to him who would be the personal embodiment of Lord Caitanya's divine mercy (*gaura-kāruṇya-śakti*). He was the prized student of **Srila Jiva Gosvami** in Vrindavan and initiated by **Srila Gopala Bhatta Gosvami**.

---

#### 2. Sacred Life & Inspiring Pastimes from Bhakti-ratnakara

##### Pastime 1: The Sacred Mission to Transport the Vrindavan Scriptures
Recognizing the genius and spiritual potency of Srinivasa Acarya, Narottama Dasa Thakura, and Syamananda Prabhu, Srila Jiva Gosvami entrusted them with the supreme mission of transporting the original handwritten manuscripts of the Six Gosvamis (*Sri Caitanya-caritamrta*, *Bhakti-rasamrita-sindhu*, *Ujjvala-nilamani*, etc.) from Vrindavan to Bengal and Odisha.

Jiva Gosvami packed the priceless scriptures into heavy iron-bound wooden chests and placed them on a large bullock cart guarded by ten armed guards. As the cart traveled through the kingdom of Vanavishnupur (Bengal), royal astrologers informed the robber-king **Birhambir** that a cart carrying immense, priceless treasure was passing through his land. That night, King Birhambir's bandits ambushed the guards and stole the iron chests, hiding them in the royal treasury!

##### Pastime 2: Converting King Birhambir and Retrieving the Scriptures
Heartbroken by the theft, Srinivasa sent Narottama to Kheturi and Syamananda to Odisha, vowing to remain alone in Vishnupur until the sacred scriptures were recovered. Disguised as a brahmana scholar, Srinivasa entered King Birhambir's court, where the royal priest Vyasacarya was attempting to explain *Srimad-Bhagavatam*. 

With supreme humility and razor-sharp scriptural wisdom, Srinivasa began explaining the *Rāsa-pañcādhyāyī* (Five Chapters of Rasa-lila). As Srinivasa spoke, streams of ecstatic tears flooded from his eyes, and his voice choked with divine love. 

Listening to Srinivasa's divine discourse, King Birhambir broke down in uncontrollable weeping, realized his grave crime, fell at Srinivasa's feet, and produced the stolen iron chests from his secret vault! King Birhambir surrendered his kingdom, accepted initiation from Srinivasa Acarya, and transformed the bandit region of Vishnupur into **Gupta Vrindavan**—the cultural center of terracotta Vaishnava temples.

##### Pastime 3: Composing the Immortal Sad-Gosvamy-Astaka
Absorbed in deep meditation on the Six Gosvamis of Vrindavan, Sri Srinivasa Acarya composed the world-famous eight-verse prayer, the **Ṣaḍ-gosvāmy-aṣṭakam**:

> *kṛṣṇotkīrtana-gāna-nartana-parau premāmṛtāmbho-nidhī*  
> *dhīrādhīra-jana-priyau tri-bhuvane mānyau śaraṇyākarau*  
> *rādhā-kṛṣṇa-padāravinda-bhajanānandena mattālikau*  
> *vande rūpa-sanātanau raghu-yugau śrī-jīva-gopālakau*  
>  
> *"I offer my respectful obeisances unto the Six Gosvamis—Sri Rupa, Sri Sanatana, Sri Raghunatha Dasa, Sri Raghunatha Bhatta, Sri Jiva, and Sri Gopala Bhatta—who are always engaged in chanting the holy name of Krishna and dancing in ecstasy..."*

---

#### 3. Major Contributions to Vaishnavism
- **Preservation & Distribution of Gosvami Literature:** Saved and disseminated the core written works of Vrindavan Vaishnavism throughout Bengal and Odisha.
- **Transformation of Vishnupur:** Converted a kingdom of plunderers into a sanctuary of classic Vaishnava music, arts, and terracotta temples.
- **Composition of Sad-Gosvamy-Astaka:** Authored the definitive hymn celebrating the mood and activities of the Six Gosvamis.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Sri Srinivasa Acarya on his Appearance day (Vaisakha Purnima) and Disappearance day (Kartika Krishna Tritiya) for acquiring unshakeable faith in the books of the Six Gosvamis and the empowerment to preach Krishna consciousness.

**Pranama Mantra:**
> *gaura-kāruṇya-śaktiṁ taṁ gaura-bhakta-jana-priyam*  
> *śrī-śrīnivāsam ācāryaṁ vande gaura-kṛpā-bharam*  
>  
> *"I offer my respectful obeisances unto Sri Srinivasa Acarya, the embodiment of Lord Caitanya's mercy potency, who is immensely dear to all the devotees of Sri Gaura and laden with the compassionate grace of Gaurasundara."*
"""
    },
    'Sri Srivasa Pandita': {
        'title': 'Sri Srivasa Pandita',
        'story': """### Sri Srivasa Pandita: The Incarnation of Sri Narada Muni

#### 1. Eternal Identity & Lineage
In the *Gaura-ganoddesa-dipika* (verse 90), Srila Kavi-karnapura reveals that Sri Srivasa Pandita (Srivasa Thakura) is none other than **Narada Muni** in Gaura-lila. He was born in Sylhet (Hatta) and later moved to Navadvipa (Mayapur). He was the eldest of four devoted brothers (Srivasa, Rama, Pati, and Srimana) and was married to Malini Devi (incarnation of Nurse Ambika in Krishna-lila).

---

#### 2. Sacred Life & Inspiring Pastimes from Sri Caitanya Bhagavata

##### Pastime 1: Nocturnal Sankirtana Pastimes at Srivasa Angan
Srivasa Angan (the house of Srivasa Pandita in Mayapur) was the birthplace and headquarters of Lord Caitanya's nocturnal *saṅkīrtana-līlā*. Every night behind closed doors, Lord Caitanya and Lord Nityananda danced in ecstatic love with Srivasa Pandita, Advaita Acarya, Gadadhara Pandita, and Haridasa Thakura. 

Celestial demigods including Lord Brahma and Lord Shiva disguised themselves as human brahmanas and stood outside Srivasa Angan, weeping in gratitude for being allowed to witness the supreme nocturnal kirtanas.

##### Pastime 2: The Death of Srivasa's Son During Kirtana (Caitanya Bhagavata Madhya 25)
While Lord Caitanya was dancing in wild ecstatic kirtana at Srivasa Angan, Srivasa's young son suddenly died of a high fever inside the house. The women in the inner quarters began weeping loudly.

Hearing the crying, Srivasa rushed inside and pleaded with tears in his eyes: *"Please stop crying! Lord Gaurasundara is dancing in divine ecstasy in our courtyard. If His joy is disturbed by your lamentation, I will drown myself in the Ganges this very moment!"*

Srivasa calmly covered the dead boy's body with a white cloth, walked back outside, and rejoined Mahaprabhu's kirtana, dancing with even greater joy as if nothing had happened!

Hours later, Lord Caitanya stopped dancing and asked: *"Why does My heart feel heavy today? Has some sorrow occurred in this home?"* The devotees tearfully revealed that Srivasa's son had passed away hours earlier.

Mahaprabhu rushed into the room, touched the dead boy, and commanded: *"My child, why are you leaving Srivasa Pandita?"*

By Mahaprabhu's divine potency, the dead child sat up and spoke words of high spiritual wisdom: *"O Supreme Lord! No one is anyone's father or son. My appointed duration in this physical body has ended according to my past karma, and I am now moving on to my next destination. Please bless me that I may never forget Your lotus feet!"*

Hearing the dead boy speak, all present were stunned. Lord Caitanya turned to Srivasa Pandita with tears streaming down His golden face and declared: *"Srivasa, you have lost one son, but Nityananda and I will forever be your two sons! We will never abandon your house!"*

##### Pastime 3: Defying the Chand Kazi
When the Mughal magistrate Chand Kazi broke the sacred *mṛdaṅga* drums at Srivasa Angan and issued a ban on Harinama Sankirtana, Srivasa Pandita remained completely fearless. Inspired by Lord Caitanya, Srivasa hosted the grand torchlight civil disobedience march that led to Chand Kazi's spiritual conversion.

##### Pastime 4: Complete Faith in Maintenance (Clapping Three Times)
When Lord Caitanya once asked Srivasa how he would support his large family without accepting employment or begging, Srivasa clapped his hands three times: *"One, two, three!"*

Mahaprabhu asked what he meant. Srivasa replied: *"If no food arrives at my home for one day, I will fast. If no food arrives for two days, I will fast. If no food arrives for three days, I will jump into the Ganges and end my life!"*

Lord Caitanya embraced Srivasa in deep emotion, proclaiming: *"Even if Goddess Lakshmi herself becomes a beggar, poverty will never enter the home of Srivasa Pandita! Whatever My pure devotee needs, I will personally carry it on My own shoulders to his door!"*

---

#### 3. Major Contributions to Vaishnavism
- **Birthplace of Sankirtana Movement:** Srivasa Angan stands as the eternal epicenter where the congregational chanting of the Holy Names was inaugurated.
- **Paramount Model of Unflinching Devotion (*Ananya-Bhakti*):** Demonstrated that love for Lord Caitanya transcends all worldly loss, grief, and attachment.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Sri Srivasa Pandita on his Appearance day (Phalguna Krishna Navami) and Disappearance day (Ashadha Sukla Chaturdasi) for absolute faith in the Holy Name, freedom from worldly grief, and unshakeable shelter at Srivasa Angan.

**Pranama Mantra:**
> *namas te śrīvāsāpaṇḍitāya mahātmane*  
> *gaura-kīrtana-līlāyāḥ prāṇadātre kṛpātmane*  
>  
> *"I offer my respectful obeisances unto the great soul Sri Srivasa Pandita, the ocean of mercy, who is the very life and soul of Lord Caitanya's ecstatic kirtana pastimes."*
"""
    },
    'Sri Syamananda Prabhu': {
        'title': 'Sri Syamananda Prabhu',
        'story': """### Sri Syamananda Prabhu: Kanaka Manjari & The Sacred Nupura

#### 1. Eternal Identity & Lineage
In Vraja-lila, Sri Syamananda Prabhu (originally named Dukhi Krishna Dasa) is **Kanaka Manjari**, the eternal maidservant of Srimati Radharani. He was born on Chaitra Purnima in Dharenda Bahadurpur (Odisha/Bengal border) to Krishna Dasa and Durika Devi. He was initiated into the Gaudiya tradition by **Sri Hridaya Chaitanya** (disciple of Gauridasa Pandita in Ambika Kalna), and was later sent to Vrindavan to study Gosvami scriptures under **Srila Jiva Gosvami**.

---

#### 2. Sacred Life & Inspiring Pastimes from Bhakti-ratnakara

##### Pastime 1: Finding Radharani's Golden Anklet at Seva Kunj
While living in Vrindavan, Dukhi Krishna Dasa volunteered for the humble service of sweeping the pathways of Seva Kunj every morning before dawn so that Srimati Radharani and Lord Krishna's lotus feet would not be hurt by thorns or pebbles.

One morning, while sweeping under a kanana tree, Dukhi Krishna found a brilliant, self-luminous golden anklet (*nūpura*) lying in the dust—dropped by Srimati Radharani during the previous night's *Rāsa-līlā*! 

Soon, Lalita Sakhi appeared disguised as an old brahmana woman searching for the lost anklet. Dukhi Krishna recognized her divine nature and declared: *"I will hand this sacred anklet only to the original owner with my own hands."* 

Srimati Radharani personally manifested before Dukhi Krishna Dasa in Her breathtaking divine form. Filled with infinite affection for His humble sweeping service, Srimati Radharani took the golden anklet, touched it to his forehead, and bestowed upon him a unique crescent-shaped tilaka mark (**Nūpura Tilaka**). She renamed him **Śyāmānanda**—"he who gives joy to Srimati Radharani and Syamasundara."

##### Pastime 2: The Tilaka Test and Guru-Bhakti
When Syamananda returned to Bengal wearing the new Nupura-tilaka given directly by Srimati Radharani, envious critics complained to his guru Hridaya Chaitanya that Syamananda had abandoned his original sampradaya tilaka. To test his disciple's humility in public, Hridaya Chaitanya struck Syamananda with a stick. 

Syamananda did not feel any anger or pain; instead, he fell at his guru's feet weeping bitterly for having caused anxiety to his spiritual master! That night, Srimati Radharani appeared in Hridaya Chaitanya's dream, showed the golden mark on Her own foot, and declared: *"I Myself gave Syamananda this tilaka mark!"* Hridaya Chaitanya broke down in weeping joy and embraced Syamananda as his most exalted disciple.

##### Pastime 3: Preaching in Odisha & Initiating Rasikananda
Syamananda Prabhu traveled throughout Odisha, Bengal, and Chota Nagpur, spreading the congregational chanting of Harinama. He initiated Sri Rasikananda Deva Gosvami and established the famous Deity of **Sri Sri Radha-Shyamsundar** in Vrindavan, which remains one of the seven main Deities of Vrindavan.

---

#### 3. Major Contributions to Vaishnavism
- **Founding the Syamanandi Lineage:** Introduced the **Nupura Tilaka** and created a major branch of Gaudiya Vaishnavism across Eastern India.
- **Installing Sri Sri Radha-Shyamsundar:** Established Radha-Shyamsundar in Vrindavan.
- **Trio of Scripture Distribution:** Co-led the historic mission with Srinivasa Acarya and Narottama Dasa Thakura to transport the Vrindavan Gosvami texts.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Sri Syamananda Prabhu on his Appearance day (Chaitra Sukla Purnima) and Disappearance day (Ashadha Krishna Saptami) for humble, unpretentious service (*sevanāmṛta*), deep guru-bhakti, and the grace of Srimati Radharani.

**Pranama Mantra:**
> *he śyāmānanda rādhikā-charaṇābjātma-dāsa*  
> *kanaka-mañjarī-rūpeṇa sevana-parāyaṇā*  
> *namas te śrī-śyāmānandāya gaura-bhakta-priyātmane*  
>  
> *"I offer my respectful obeisances unto Sri Syamananda Prabhu, who is Kanaka Manjari in Vraja-lila, dedicated to the confidential service of Srimati Radharani's lotus feet, and immensely dear to all devotees of Lord Caitanya."*
"""
    },
    'Sri Vakresvara Pandita': {
        'title': 'Sri Vakresvara Pandita',
        'story': """### Sri Vakresvara Pandita: Ananga Manjari & The Ecstatic Dancer

#### 1. Eternal Identity & Lineage
In the *Gaura-ganoddesa-dipika* (verse 71), Srila Kavi-karnapura reveals that Sri Vakresvara Pandita is **Ananga Manjari** (the younger sister of Srimati Radharani) in Vraja-lila, and also an incarnation of Tungavidya Sakhi. He was born in Guptipara / Triveni (Bengal). He was an intimate associate of Lord Caitanya Mahaprabhu in both Navadvipa and Jagannath Puri.

---

#### 2. Sacred Life & Inspiring Pastimes from Sri Caitanya Bhagavata

##### Pastime 1: Continuous Dancing for 72 Hours (Three Days & Nights)
Sri Vakresvara Pandita was the most phenomenal dancer in Lord Caitanya's kirtana assembly. Once, in the courtyard of Srivasa Angan, Vakresvara Pandita began dancing in divine ecstasy. He danced continuously for **72 hours (three full days and nights)** without stopping for food, water, or rest! 

Lord Caitanya Himself personally sang kirtana for Vakresvara's dancing. When Vakresvara finally stopped and bowed at Mahaprabhu's lotus feet, Lord Caitanya embraced him tearfully, declaring: *"Vakresvara, I have only one wing of devotional love. By your matchless dancing, you have given Me a second wing! If I had one more devotee like you, I could fly and submerge the entire universe in kirtana!"*

##### Pastime 2: The Deliverance of Devananda Pandita (Caitanya Bhagavata Madhya 21)
Devananda Pandita was a famous scholar of *Srimad-Bhagavatam* in Navadvipa who taught the scripture intellectually without understanding *prema-bhakti*. Once, when Srivasa Pandita wept in tears of love listening to Devananda's class, Devananda's ignorant students forcibly dragged Srivasa out of the assembly. Devananda did not stop them, committing a grave *vaiṣṇava-aparādha*.

Later, when Sri Vakresvara Pandita visited Kulia (Navadvipa) and danced in wild ecstatic love outside Devananda's house, Devananda observed Vakresvara's pure, divine ecstasy. Transformed, Devananda spent the entire night holding a fan over Vakresvara, wiping the dust and sweat off Vakresvara's body with his own garments.

Impressed by Devananda's selfless service to Vakresvara Pandita, Lord Caitanya forgave Devananda's offense and bestowed pure *kṛṣṇa-prema* upon him, declaring: *"Because Devananda served Vakresvara Pandita, I am now pleased with him!"*

##### Pastime 3: Establishing Sri Sri Radha-Kanta at Jagannath Puri
When Lord Caitanya moved to Jagannath Puri, Vakresvara Pandita accompanied Him and resided at Kasi Misra's house (Gambhira). He installed the breathtaking Deities of **Sri Sri Radha-Kanta** at Kasi Misra's residence, creating a holy sanctuary of devotion in Puri.

##### Pastime 4: Empowering Sri Gopal Guru Gosvami
Vakresvara Pandita initiated Sri Gopal Guru Gosvami (who served Mahaprabhu as a young boy in Puri) and established the Radha-Kanta Matha lineage, continuing the confidential worship of *ananga-mañjarī-upāsanā*.

---

#### 3. Major Contributions to Vaishnavism
- **Immortality of Gaura-Nrktya:** Demonstrated the supreme power of ecstatic dancing in Harinama Sankirtana.
- **Deliverance of Devananda Pandita:** Proved that serving a pure Vaishnava (*vaiṣṇava-sevā*) erases all offenses against the Holy Name.
- **Founding Radha-Kanta Matha:** Established a major center of Gaudiya worship in Jagannath Puri.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Sri Vakresvara Pandita on his Appearance day (Ashadha Sukla Tritiya) and Disappearance day (Ashadha Krishna Navami) for unflagging enthusiasm in kirtana-dancing, freedom from Vaishnava offenses, and internal service under Ananga Manjari.

**Pranama Mantra:**
> *namas te gaura-nṛtyāṅga-vakreśvara-mahātmane*  
> *ananga-mañjarī-rūpa-kṛpā-sindho namo 'stu te*  
>  
> *"I offer my respectful obeisances unto the great soul Sri Vakresvara Pandita, the dancing limb of Lord Caitanya, who is Ananga Manjari in Vraja-lila and an endless ocean of mercy."*
"""
    },
    'Srila Bhaktisiddhanta Sarasvati Thakura': {
        'title': 'Srila Bhaktisiddhanta Sarasvati Thakura',
        'story': """### Srila Bhaktisiddhanta Sarasvati Thakura: Nayana Manjari & The Lion Guru

#### 1. Eternal Identity & Lineage
In Gaudiya parampara tradition, Srila Bhaktisiddhanta Sarasvati Thakura Prabhupada (1874–1936 CE) is **Nayana Manjari** in Vraja-lila. He was born on February 6, 1874 in Jagannath Puri (near Sri Jagannath Temple) to **Srila Bhaktivinoda Thakura** and Srimati Bhagavati Devi, and was named Bimala Prasada at birth. He was initiated by the renowned paramahamsa saint **Srila Gaura Kisora Dasa Babaji Maharaja**.

---

#### 2. Sacred Life & Inspiring Pastimes

##### Pastime 1: The Lifetime Mango Vow (Anarpita-Phala-Tyaga)
When Bimala Prasada was four years old, his father Bhaktivinoda Thakura brought home fresh mangoes. Before the fruits were officially offered on the altar to Lord Jagannath, young Bimala Prasada picked up one mango and ate it. 

Bhaktivinoda Thakura gently corrected him: *"My dear child, unoffered food is impure and should never be eaten. We must always offer everything to Lord Sri Krishna first."*

Taking his father's words deeply to heart, young Bimala Prasada felt immense remorse and vowed: *"Because I greedily ate an unoffered mango, I promise never to eat a mango again in my life!"* Throughout his entire 62 years of life, despite being offered mangoes by kings and disciples across India, he strictly maintained this vow, exemplifying unwavering self-control (*tapasya*).

##### Pastime 2: The One Billion Holy Names Vow (100 Crore Harinama Vrata)
From 1905 to 1914, residing in a small grass hut at Mayapur Yoga Pith (Lord Caitanya's birthplace), he undertook a monumental vow of chanting **100 crore (one billion) Holy Names** of Sri Krishna. 

He chanted 300,000 Holy Names (192 rounds on beads) every single day for nine consecutive years! Sleeping on the floor and eating simple boiled rice watered down with rain water, he accumulated immense spiritual potency to launch a worldwide revival of Gaudiya Vaishnavism.

##### Pastime 3: The Lion Guru (Simha-Guru) Defeating Caste Prides
In 1911 at Balighai (Midnapore), during a famous nationwide convention organized by caste-brahmanas and smarta scholars, Srila Bhaktisiddhanta presented his landmark thesis *Brāhmaṇa o Vaiṣṇava*. He proved from Vedic scriptures that a person born in any family who becomes a pure Vaishnava is far superior to a caste-born brahmana. His razor-sharp logic silenced all opponents, earning him the title **Simha-Guru** (Lion Guru).

##### Pastime 4: The Brihat-Mridanga & Modern Technology in Preaching
Srila Bhaktisiddhanta revolutionized Vaishnava preaching by defining the printing press as the **Bṛhat-Mṛdaṅga** (the Great Clay Drum). He explained: *"A clay mridanga played in a kirtana can be heard for a few hundred feet, but the printing press—publishing books and periodicals—can resound across oceans and endure for generations!"* 

He established the **Gaudiya Math** (64 monastic centers), introduced *tridaṇḍi-sannyāsa*, utilized motorcars and printing presses for preaching (*yukta-vairāgya*), and instructed his beloved disciple, Srila A.C. Bhaktivedanta Swami Prabhupada: *"If you ever get money, print books and preach in the English language!"*

---

#### 3. Major Contributions to Vaishnavism
- **Founding of Gaudiya Math:** Opened 64 centers across India, Myanmar, and Europe to propagate Lord Caitanya's message.
- **The Brihat-Mridanga Strategy:** Established major publishing houses printing journals (*The Harmonist*, *Nadiya Prakasa*) and scriptural editions.
- **Re-establishing Pure Gaudiya Siddhanta:** Cleansed Vaishnavism of Sahajiya and caste distortions, establishing *yukta-vairāgya* and *tridandi-sannyasa*.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Bhaktisiddhanta Sarasvati Thakura on his Appearance day (Panchami after Magha Purnima) and Disappearance day (Pausha Krishna Dwadasi) for fearless preaching boldness, uncompromising fidelity to Srila Prabhupada's books, and victory over material illusions.

**Pranama Mantra:**
> *nama oṁ viṣṇu-pādāya kṛṣṇa-preṣṭhāya bhū-tale*  
> *śrīmate bhaktisiddhānta-sarasvatīti nāmine*  
>  
> *śrī-vārṣabhānavī-devī-dayitāya kṛpābdhaye*  
> *kṛṣṇa-sambandha-vijñāna-dāyine prabhave namaḥ*  
>  
> *"I offer my respectful obeisances unto Srila Bhaktisiddhanta Sarasvati Thakura, who is very dear to Lord Krishna, having taken shelter at His lotus feet. I offer my obeisances unto him who is dear to Srimati Radharani, who is an ocean of mercy, and who imparts the science of relationship with Krishna."*
"""
    },
    'Srila Bhaktivinoda Thakura': {
        'title': 'Srila Bhaktivinoda Thakura',
        'story': """### Srila Bhaktivinoda Thakura: Kamala Manjari & The Seventh Gosvami

#### 1. Eternal Identity & Lineage
In Gaudiya Vaishnava parampara, Srila Bhaktivinoda Thakura (1838–1914 CE) is recognized as **Kamala Manjari** in Vraja-lila. He is celebrated as the **Seventh Gosvami** for single-handedly reviving pure Gaudiya Vaishnavism during a dark era when it was corrupted by pseudo-devotional sects. He was born on September 2, 1838 in Ula Birnagar (Nadia, Bengal) to Ananda Chandra Datta and Jaganmohini Devi, and was named Kedaranatha Datta at birth. He was initiated by **Srila Vipina Vihari Gosvami** and accepted **Srila Jagannath Dasa Babaji Maharaja** as his siksha-guru.

---

#### 2. Sacred Life & Inspiring Pastimes

##### Pastime 1: The Golden Light & Rediscovery of Mayapur Yoga Pith
While serving as a high-ranking Magistrate in Krishnanagar, Bhaktivinoda Thakura spent his evenings gazing across the Jalangi River toward Navadvipa. One night from his terrace, he beheld a magnificent, blinding pillar of golden light shining across the river in the village of Miyapur.

Guided by inner realization and ancient manuscripts (*Navadvipa-dhāma-māhātmya*), he brought the venerated 140-year-old saint **Srila Jagannath Dasa Babaji Maharaja** to the spot in a basket. The moment they arrived under a jackfruit tree, old Babaji Maharaja suddenly leaped out of his basket and danced in wild ecstatic love, shouting: *"Ei to Nimai-janma-bhūmi!"* ("This indeed is the birth-site of Nimai!"). Thus, Bhaktivinoda Thakura rediscovered Lord Caitanya's actual birth-site at **Mayapur Yoga Pith**.

##### Pastime 2: Subduing the Mystical Pretender Bisakhena
While Magistrate of Jagannath Puri, a tantric pretender named Bisakhena claimed to be an incarnation of Maha-Vishnu, terrorizing villages with mystic powers and demanding royal women. When others feared his black magic, Bhaktivinoda Thakura fearlessly investigated, tried him in court, and sentenced him to prison. 

When Bisakhena cast black-magic curses threatening to kill Bhaktivinoda's family, Bhaktivinoda remained completely unmoved, relying solely on the Holy Name. A doctor shaved off Bisakhena's long hair (the source of his tantric power), breaking his spell and causing him to poison himself in jail.

##### Pastime 3: Preaching to the West (1896)
In 1896 (the birth year of Srila Prabhupada), Bhaktivinoda Thakura published a Sanskrit and English treatise entitled *Sri Chaitanya Mahaprabhu: His Life and Precepts*, sending copies to McGill University in Canada, the Royal Asiatic Society in London, and major universities across the West, planting the seeds of global Harinama.

##### Pastime 4: Prophesying the Adbhuta Mandir & ISKCON
Bhaktivinoda Thakura published a prophecy in *Sajjana-toṣaṇī*: *"Very soon a day will come when foreign devotees from America, England, France, and Russia will link arms with Bengali devotees and dance in wild Harinama Sankirtana in Mayapur!"* He also envisioned a grand **Adbhuta Mandir** (Wondrous Temple) rising in Mayapur—fulfilled today by the Temple of the Vedic Planetarium (TOVP).

---

#### 3. Major Contributions to Vaishnavism
- **Rediscovery of Mayapur Yoga Pith:** Located and restored Lord Caitanya's birthplace.
- **Prolific Literary Legacy:** Authored over 100 texts including *Jaiva-dharma*, *Sri Chaitanya Shikshamrita*, *Saranagati*, *Gitavali*, and *Kalyana-kalpataru*.
- **Pioneer of Global Preaching:** First Acarya to send English Vaishnava literature to Western universities.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Bhaktivinoda Thakura on his Appearance day (Bhadra Sukla Ekadasi) and Disappearance day (Jyeshtha Amavasya) for unconditional surrender (*śaraṇāgati*), deep relish for Vaishnava songs, and entrance into Mayapur-dhama.

**Pranama Mantra:**
> *namo bhaktivinodāya sac-cid-ānanda-nāmine*  
> *gaura-śakti-svarūpāya rūpānuga-varāya te*  
>  
> *"I offer my respectful obeisances unto Saccidananda Bhaktivinoda Thakura, who is the embodiment of Lord Caitanya's transcendental potency and the foremost follower of Srila Rupa Gosvami."*
"""
    },
    'Srila Gopala Bhatta Gosvami': {
        'title': 'Srila Gopala Bhatta Gosvami',
        'story': """### Srila Gopala Bhatta Gosvami: Guna Manjari & The Self-Manifested Radha-Ramana

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srila Gopala Bhatta Gosvami (1503–1578 CE) is **Guna Manjari**. He is one of the revered Six Gosvamis of Vrindavan. He was born in Srirangam, Tamil Nadu, into a high Sri Sampradaya family as the son of Venkata Bhatta (the chief priest of Srirangam temple) and nephew of Srila Prabodhananda Sarasvati.

---

#### 2. Sacred Life & Inspiring Pastimes from Sri Caitanya-caritamrta (Madhya 9)

##### Pastime 1: Serving Lord Caitanya During Chaturmasya at Srirangam
When Lord Caitanya Mahaprabhu stayed at Venkata Bhatta's house in Srirangam for the four months of the rainy season (*chāturmāsya*) in 1511 CE, young Gopala Bhatta served Mahaprabhu with boundless affection, washing His feet and partaking of His prasadam remnants. 

Before departing, Lord Caitanya embraced young Gopala Bhatta, gave him His personal loincloth (*kaupīna*), wooden seat (*āsana*), and black wooden rosary beads, and instructed him to later join Rupa and Sanatana Gosvamis in Vrindavan.

##### Pastime 2: Self-Manifestation of Sri Sri Radha-Ramana Devaji (1542 CE)
While on pilgrimage to the Gandaki River in Nepal, twelve sacred Salagrama-silas jumped into Gopala Bhatta's water pot (*kamaṇḍalu*). He brought them back to Vrindavan and worshipped them lovingly.

On Nrisimha Caturdasi in 1542 CE, a wealthy merchant donated exquisite silk garments, golden crowns, and ornaments for Deities. Gopala Bhatta placed them before his Salagrama-silas, feeling intense sorrow in his heart: *"Alas, my Salagramas have no arms or legs for Me to ornament and crown!"*

That night, Gopala Bhatta wept in fervent prayer. At sunrise on Nrisimha Caturdasi morning, when he opened the altar curtain, he was amazed to find that one of his Salagrama-silas (the **Damodara-sila**) had self-manifested into the breathtaking Deity of **Sri Radha-Ramana Devaji**! 

The Deity was perfectly formed with Krishna's three-fold bending posture (*tri-bhaṅga*), possessing the smiling face of Sri Govindadev, chest of Sri Gopinath, and feet of Sri Madanamohan. To this day in Vrindavan, Sri Radha-Ramana Devaji's 500-year-old unbroken worship continues.

##### Pastime 3: Compiling Hari-Bhakti-Vilasa
Under Lord Caitanya's direct direction and with Sanatana Gosvami's assistance, Srila Gopala Bhatta Gosvami compiled **Hari-bhakti-vilāsa**—the monumental 20-chapter encyclopedia of Vaishnava rituals, Deity worship standards (*arcana-paddhati*), and devotional ethics.

##### Pastime 4: Initiating Srila Srinivasa Acarya
Recognizing the divine empowerment of young Srinivasa, Gopala Bhatta Gosvami accepted him as his initiated disciple in Vrindavan, empowering him to spread Gosvami literature throughout Bengal.

---

#### 3. Major Contributions to Vaishnavism
- **Deity of Sri Radha-Ramana:** Revealed the self-manifested Deity of Sri Radha-Ramana in Vrindavan.
- **Hari-bhakti-vilasa:** Created the definitive liturgical manual for the entire Gaudiya Sampradaya.
- **Sat-Kriya-Sara-Dipika:** Authored the manual for Vaishnava lifecycle rites (*saṁskāras*).

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Gopala Bhatta Gosvami on his Appearance day (Pousha Sukla Paurnami/Navami) and Disappearance day (Sravana Krishna Panchami) for unblemished Deity worship standards, pure *rāgānugā-bhakti*, and intense love for Sri Radha-Ramana Devaji.

**Pranama Mantra:**
> *gaura-kāruṇya-śaktimantaṁ guṇa-mañjarī-rūpiṇam*  
> *rādhā-ramaṇa-devanga-sevā-saṅkīrtanotsavam*  
> *śrīmad-gopāla-bhaṭṭākhyaṁ vande rūpānuga-priyam*  
>  
> *"I offer my respectful obeisances unto Srila Gopala Bhatta Gosvami, the embodiment of Lord Caitanya's mercy, who is Guna Manjari in Vraja-lila, the beloved worshipper of Sri Radha-Ramana Devaji, and extremely dear to the followers of Srila Rupa Gosvami."*
"""
    },
    'Srila Narottama Dasa Thakura': {
        'title': 'Srila Narottama Dasa Thakura',
        'story': """### Srila Narottama Dasa Thakura: Champaka Manjari & Thakura Mahasaya

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srila Narottama Dasa Thakura is **Champaka Manjari**. He was born on Maghi Purnima in Kheturi (Rajshahi district, modern Bangladesh) to King Raja Krishnananda Datta and Queen Narayani Devi. He was the sole initiated disciple of **Srila Lokanatha Gosvami** in Vrindavan, and studied Gosvami scriptures under **Srila Jiva Gosvami**.

---

#### 2. Sacred Life & Inspiring Pastimes from Bhakti-ratnakara & Narottama-vilasa

##### Pastime 1: Receiving Lord Caitanya's Prema at the Padma River
Years before Narottama's birth, while Lord Caitanya Mahaprabhu was traveling through Kanair Natshala along the banks of the Padma River, Mahaprabhu called out: *"O River Padmavati! Keep My love of Godhead (prema) in safekeeping! When a prince named Narottama comes here, hand My prema over to him!"*

When young Prince Narottama bathed in the Padma River years later, the waters of the river turned golden, and Goddess Padmavati personally presented Lord Caitanya's *prema* to Narottama, transforming his complexion into molten gold!

##### Pastime 2: Winning Lokanatha Gosvami's Grace through Secret Tapasya
When Narottama arrived in Vrindavan, he begged Srila Lokanatha Gosvami for initiation. Lokanatha, having vowed never to take disciples, refused. 

Undeterred, Prince Narottama quietly went to Lokanatha's latrine area every night at midnight, cleaned the area with his own clothes, and washed it with water for over a year! When Lokanatha discovered who was performing this humble service, he wept, embraced Narottama, and initiated him.

##### Pastime 3: The Historic Kheturi Maha-Festival
At Kheturi on Gaura Purnima, Narottama Dasa Thakura hosted the largest festival in post-Caitanya history, installing six sets of Deities (Sri Gauranga, Sri Vallabhikanta, Sri Vrajamohan, Sri Radhakanta, Sri Radharamana, and Sri Gopalaji). Mother Jahnava Devi (consort of Lord Nityananda) presided over the assembly.

During Narottama's ecstatic kirtana (*Garanhati tune*), Lord Caitanya, Lord Nityananda, and all Their departed associates supernaturally reappeared on the kirtana stage and danced among the weeping devotees!

##### Pastime 4: Merging into the Holy Milk-White Ganges (Ganga-Jala)
When envious caste-brahmanas criticized Narottama for initiating non-brahmanas, Narottama entered the Ganges at Budhuri Ghat and instructed his disciples to rub his body. As Ramachandra Kaviraja and Ganga-narayana Chakravarti rubbed his body, Narottama's physical form melted into liquid milk and merged into the Ganges before all eyes!

---

#### 3. Major Contributions to Vaishnavism
- **Prarthana & Prema-Bhakti-Candrika:** Authored the two immortal songbooks considered the "Veda of Gaudiya Vaishnavas."
- **Kheturi Maha-Festival:** United the post-Caitanya Gaudiya Sampradaya under a unified liturgical standard.
- **Garanhati Kirtana:** Pioneered classical Gaudiya kirtana melodies.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Narottama Dasa Thakura on his Appearance day (Maghi Purnima) and Disappearance day (Kartika Krishna Panchami) for absolute humility, freedom from spiritual pride (*pratiṣṭhā*), and shelter at Sri Rupa Manjari's lotus feet (*śrī-rūpa-mañjarī-pada, sei mora sampada*).

**Pranama Mantra:**
> *namo narottama-padābja-sevinām*  
> *śrī-lokanātha-priya-dāsātmane*  
> *prema-bhakti-candrikā-kāriṇe*  
> *śrī-champaka-mañjarī-rūpiṇe namaḥ*  
>  
> *"I offer my respectful obeisances unto Srila Narottama Dasa Thakura, the beloved disciple of Srila Lokanatha Gosvami, who is Champaka Manjari in Vraja-lila, and the author of the nectarine Prema-bhakti-candrika."*
"""
    },
    'Srila Prabhupada': {
        'title': 'Srila Prabhupada',
        'story': """### Srila A.C. Bhaktivedanta Swami Prabhupada: Founder-Acharya of ISKCON

#### 1. Eternal Identity & Lineage
In Gaudiya parampara tradition, Srila A.C. Bhaktivedanta Swami Prabhupada (1896–1977 CE) is recognized as an empowered *śaktyāveśa-avatāra* specifically sent by Lord Sri Krishna to fulfill Sri Caitanya Mahaprabhu's prophecy (*pṛthivīte āche yata nagarādi grāma / sarvatra pracāra hoibe mora nāma*). He was born on September 1, 1896 (Nandotsava day) in Kolkata to Gour Mohan De and Rajani Devi, and was named Abhay Charan De at birth. He was initiated by **Srila Bhaktisiddhanta Sarasvati Thakura Prabhupada** in 1933 at Allahabad.

---

#### 2. Sacred Life & Inspiring Pastimes

##### Pastime 1: The Divine Order (1922)
At their very first meeting in 1922 at Ultadanga Junction Road in Kolkata, Srila Bhaktisiddhanta Sarasvati Thakura issued his legendary instruction to young Abhay Charan: *"You are educated young men. Why don't you preach Lord Caitanya's message throughout the whole world in the English language?"* Abhay accepted this instruction as his life's sole mission.

##### Pastime 2: The Historic Voyage of the Jaladuta (1965)
In August 1965, at the age of 69, with no financial backing, possessing only 40 rupees ($7 USD), an umbrella, and trunk boxes of his translated *Srimad-Bhagavatam* volumes, Srila Prabhupada boarded a cargo ship named the **Jaladuta** bound for New York.

During thirty days at sea, he suffered two massive heart attacks. Facing death on the Atlantic Ocean, he wrote his historic poem *Mārkine Bhāgavata-Dharma*, praying: *"O Lord Krishna, how will I make them understand Your message? I am a very unfortunate, fallen beggar. But if You make me dance, I will dance as You desire!"*

##### Pastime 3: Tompkins Square Park & The Birth of ISKCON (1966)
Arriving in New York City, Srila Prabhupada sat under a tree in Tompkins Square Park in the East Village, playing a small pair of hand cymbals (*karātalas*) and chanting *Hare Krishna Hare Krishna Krishna Krishna Hare Hare / Hare Rama Hare Rama Rama Rama Hare Hare*. Youths and seekers joined him in weeping ecstasy. In July 1966, he legally incorporated the **International Society for Krishna Consciousness (ISKCON)**.

##### Pastime 4: Global Revolution & Translating Scriptures
Over the next 12 years (1965–1977), Srila Prabhupada traveled around the world **14 times**, opened over **100 temples**, established farm communities and gurukulas, and founded the **Bhaktivedanta Book Trust (BBT)**. Working late into the night between 1:00 AM and 4:00 AM, he translated over 80 canonical volumes of Vedic scriptures—including *Bhagavad-gītā As It Is*, *Śrīmad-Bhāgavatam* (12 Cantoes), and *Śrī Caitanya-caritāmṛta*.

---

#### 3. Major Contributions to Vaishnavism
- **Founding ISKCON & BBT:** Built a worldwide spiritual movement spanning every continent, publishing over 500 million books in 80+ languages.
- **Globalizing Harinama & Ratha Yatra:** Took Harinama Sankirtana and Jagannath Ratha Yatra to major cities (London, New York, Tokyo, Paris, Sydney).
- **Pure Sraddha & Prasadam Distribution:** Distributed billions of plates of pure *kṛṣṇa-prasādam* worldwide.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Prabhupada on his Appearance day (Nandotsava tithi) and Disappearance day (Kartika Sukla Chaturthi) for unshakeable faith in his books, daily chanting of 16 rounds of the Hare Krishna Maha-Mantra, adherence to the 4 regulative principles, and total surrender to preaching.

**Pranama Mantra:**
> *nama oṁ viṣṇu-pādāya kṛṣṇa-preṣṭhāya bhū-tale*  
> *śrīmate bhaktisiddhānta-svāmin iti nāmine*  
>  
> *namas te sārasvate deve gaura-vāṇī-pracāriṇe*  
> *nirviśeṣa-śūnyavādi-pāścātya-deśa-tāriṇe*  
>  
> *"I offer my respectful obeisances unto His Divine Grace A.C. Bhaktivedanta Swami Prabhupada, who is very dear to Lord Krishna, having taken shelter at His lotus feet. Our respectful obeisances are unto you, O servant of Sarasvati Gosvami. You are kindly preaching the message of Lord Caitanyadeva and liberating the Western countries, which are filled with impersonalism and voidism."*
"""
    },
    'Srila Raghunatha Dasa Gosvami': {
        'title': 'Srila Raghunatha Dasa Gosvami',
        'story': """### Srila Raghunatha Dasa Gosvami: Rasa Manjari & Prayojana-Acharya

#### 1. Eternal Identity & Lineage
In Vraja-lila, Srila Raghunatha Dasa Gosvami (1495–1571 CE) is **Rasa Manjari** (and Bhanumati). He is one of the revered Six Gosvamis of Vrindavan, glorified as the **Prayojana-Acharya**—the teacher who exemplifies the ultimate goal of unalloyed love of Godhead (*kṛṣṇa-prema*). He was born in Saptagram (Bengal) into an immensely wealthy landlord family (son of Govardhana Majumdar and nephew of Hiranya Majumdar) possessing an annual income of 1.2 million gold coins (*twelve lakh rupees*). He was initiated by **Srila Yadunandana Acarya** and surrendered at the feet of **Lord Caitanya Mahaprabhu** and **Srila Svarupa Damodara Gosvami**.

---

#### 2. Sacred Life & Inspiring Pastimes from Sri Caitanya-caritamrta (Antya Lila)

##### Pastime 1: The Chida-Dahi Mahotsava at Panihati (Antya 6)
Young Raghunatha repeatedly ran away from home to join Lord Caitanya, but his wealthy parents caught him every time and kept him under heavy guard. When Lord Nityananda Prabhu came to Panihati on the banks of the Ganges, Raghunatha Dasa fell at Lord Nityananda's feet from a distance.

Lord Nityananda laughed, placed His lotus foot on Raghunatha's head, and affectionately teased him: *"You try to see Me like a thief from afar! Now I will punish you: feed all My associates chipped rice and yogurt!"*

Raghunatha joyfully bought thousands of clay pots of chipped rice, condensed milk, bananas, and yogurt, feeding thousands of devotees in two sacred pots (**Chida-Dahi Mahotsava**). Lord Nityananda blessed him: *"Very soon Lord Caitanya Mahaprabhu will release you from material bondage and accept you at His lotus feet!"*

##### Pastime 2: Escape to Jagannath Puri & Sixteen Days on Foot
Following Lord Nityananda's blessing, Raghunatha slipped past his guards before dawn, traveling secret jungle paths on foot for 12 days to reach Jagannath Puri, eating only three times. 

When he arrived, Lord Caitanya placed him under the direct spiritual guidance of **Svarupa Damodara Gosvami**, naming him "Svarupa's Raghunatha." Mahaprabhu presented Raghunatha with His own personal **Goverdhana-sila** and **Gunja-mala**, which Raghunatha worshipped with tears of love every day.

##### Pastime 3: Extreme Renunciation at Radha-kunda
After Lord Caitanya and Svarupa Damodara passed away, Raghunatha went to Vrindavan planning to throw himself off Govardhana Hill. Rupa and Sanatana Gosvamis embraced him as their third brother and instructed him to live at **Radha-kunda**.

Raghunatha Dasa performed astounding, superhuman *tapasya*: he chanted 100,000 Holy Names (64 rounds) daily, offered 1,000 prostrated obeisances, offered 2,000 obeisances to Vaishnavas, and remembered Krishna's pastimes for 3 hours daily. He drank only a small cup of buttermilk every two or three days!

##### Pastime 4: Srimati Radharani Shields Her Devotee
While Raghunatha Dasa sat on the banks of Radha-kunda in the blazing midday summer sun absorbed in trance, Srimati Radharani Herself stood behind him, using Her own silk garment (*āñcala*) to shade him from the sun, sweat pouring from Her divine body! Sanatana Gosvami witnessed this miracle and tearfully built a small cottage (*bhajana-kuṭīra*) for Raghunatha to protect Radharani from the exertion of shading him.

---

#### 3. Major Contributions to Vaishnavism
- **Literary Masterpieces:** Authored **Vilāpa-kusumāñjali**, **Stavāvalī**, **Mānaḥ-śikṣā**, and **Raghunātha-dāsa-gaṇoddeśa-dīpikā**.
- **Radha-Dasyam:** Taught the ultimate perfection of Gaudiya Vaishnavism—unconditional maidservantship under Srimati Radharani.
- **Sanctification of Radha-kunda & Shyama-kunda:** Developed and sanctified Radha-kunda as the holiest place in the universe.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Raghunatha Dasa Gosvami on his Appearance day (Vaisakha Krishna Radhashtami/Magha Sukla Navami) and Disappearance day (Ashvina Sukla Dvadasi) for ultimate renunciation (*vairāgya*), *radha-dasyam*, and unswerving love for Radha-kunda.

**Pranama Mantra:**
> *nama oṁ viṣṇu-pādāya rūpānuga-varāya te*  
> *śrī-raghunātha-dāsāya rādhā-kuṇḍa-nivāsine*  
>  
> *vairāgya-yug-bhakti-rasaṁ prayatnair*  
> *apāyayan mām anabhīpsum api*  
> *kṛpāmbudhir yaḥ para-duḥkha-duḥkhī*  
> *sanātanaṁ taṁ prabhum āśrayāmi*  
>  
> *"I offer my respectful obeisances unto Srila Raghunatha Dasa Gosvami, the foremost follower of Srila Rupa Gosvami, who resides eternally at Radha-kunda and who generously made me drink the nectar of devotional service coupled with renunciation."*
"""
    },
    'Srila Vrndavana Dasa Thakura': {
        'title': 'Srila Vrndavana Dasa Thakura',
        'story': """### Srila Vrndavana Dasa Thakura: Vyasadeva of Gaura-Lila

#### 1. Eternal Identity & Lineage
In Gaudiya Vaishnava theology, Srila Vrndavana Dasa Thakura (1507–1589 CE) is recognized as **Srila Veda Vyasa** (the author of *Srimad-Bhagavatam*), appearing as the **Vyāsadeva of Gaura-līlā**. He was born in Mamgachi (Modadrumadvipa, Navadvipa) to **Srimati Narayani Devi**—the blessed four-year-old niece of Srivasa Pandita who received Lord Caitanya's personal betel leaf remnant and wept in divine ecstasy. He was the foremost disciple of **Lord Nityananda Prabhu**.

---

#### 2. Sacred Life & Inspiring Pastimes from Sri Caitanya Bhagavata & Bhakti-ratnakara

##### Pastime 1: The Divine Blessing of Narayani Devi
When Narayani Devi was a four-year-old girl playing at Srivasa Angan, Lord Caitanya Mahaprabhu held out a betel leaf (*tāmbūla*) and prasadam from His lotus mouth and gave it to her, calling out: *"Narayani! Chant Krishna's Holy Name and weep in love!"* 

The small child instantly swooned in divine love, tears flowing down her cheeks like rivers. Srila Vrndavana Dasa Thakura took birth in the womb of this exalted, sanctified soul Narayani Devi.

##### Pastime 2: Authoring Sri Caitanya Bhagavata (Originally Caitanya Mangala)
Empowered directly by Lord Nityananda Prabhu, Vrndavana Dasa Thakura sat in Denur (Burdwan) and composed **Śrī Caitanya Bhāgavata**—the first authentic biography of Sri Caitanya Mahaprabhu written in the Bengali language. 

He depicted the early pastimes (*Ādi-līlā*) and Navadvipa *saṅkīrtana* with unmatched sweetness, authority, and scriptural fidelity. Srila Krsnadasa Kaviraja Gosvami glorifies him in *Caitanya-caritamrta* (Adi 8.39):  
*"Vrndavana Dasa Thakura is the Vyasadeva of Lord Caitanya's pastimes. Hearing his book removes all spiritual obstacles and awakens pure love for Lord Caitanya."*

##### Pastime 3: Traveling with Lord Nityananda Prabhu
Vrndavana Dasa Thakura accompanied Lord Nityananda Prabhu across Bengal, witnessing Nityananda's ocean of mercy that delivered even the most fallen souls, thieves, and outcasts through Harinama Sankirtana.

##### Pastime 4: Establishing Denur Sri Gauranga Temple
He spent his final years in Denur village, where he installed the captivating Deity of **Sri Gauranga** and continued writing devotional works until his physical disappearance on Vaisakha Krishna Parva.

---

#### 3. Major Contributions to Vaishnavism
- **Śrī Caitanya Bhāgavata:** Authored the foundational, immortal biography of Lord Caitanya Mahaprabhu.
- **Śrī Nityānanda-caritāmṛta:** Authored the canonical biography of Lord Nityananda Prabhu.
- **Veda Vyasa of Gaura-Lila:** Established the scriptural authenticity of Gaura-tattva and Nityananda-tattva.

---

#### 4. How to Pray & Seek Blessings
Devotees pray to Srila Vrndavana Dasa Thakura on his Disappearance day (Vaisakha Krishna Krsna-Paksha) and Appearance day for deep relish of *Caitanya Bhagavata*, unflinching shelter at Lord Nityananda's lotus feet, and total freedom from Vaishnava-aparadha.

**Pranama Mantra:**
> *namo 'stu te gaura-līlā-vyāsāya karuṇātmane*  
> *nityānanda-priyāṅgāya śrī-vṛndāvana-dāsine*  
>  
> *"I offer my respectful obeisances unto Srila Vrndavana Dasa Thakura, the Vyasadeva of Gauranga's pastimes, the embodiment of compassion, and the beloved associate of Lord Nityananda Prabhu."*
"""
    }
}


def populate_acharya_descriptions():
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
    help = 'Populate detailed scriptural stories for the 17 core Vaishnava Acharyas in the calendar.'

    def handle(self, *args, **options):
        count = populate_acharya_descriptions()
        self.stdout.write(
            self.style.SUCCESS(f"Successfully populated stories for {count} Acharya observances in Vaishnava Calendar.")
        )
