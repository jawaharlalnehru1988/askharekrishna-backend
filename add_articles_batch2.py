import os
import django

print("Setting DJANGO_SETTINGS_MODULE...")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askharekrishna_backend.settings')
print("Running django.setup()...")
django.setup()
print("Finished django.setup().")

from chanting.models import ChantingArticle

def get_next_order(main_topic):
    last_article = ChantingArticle.objects.filter(mainTopic=main_topic).order_by('-order').first()
    if last_article:
        return last_article.order + 1
    return 1

articles_data = [
    {
        "mainTopic": "Foundations of Hare Krishna Chanting",
        "subTopic": "Why Anyone Can Chant Hare Krishna",
        "article": """One of the most extraordinary features of chanting the Hare Krishna mahāmantra is that there are no hard and fast rules for its recitation. In many traditional Vedic rituals or yogic practices, one must adhere to strict regulations regarding time, place, cleanliness, and even one's birth or caste. However, Sri Caitanya Mahaprabhu, out of His supreme compassion, removed all such barriers for the chanting of the holy name.

In His *Sikshashtakam* (Verse 2), Lord Caitanya states: *namnam akari bahudha nija-sarva-shaktis / tatrarpita niyamitah smarane na kalah*. "O my Lord, Your holy name alone can render all benediction to living beings, and thus You have hundreds and millions of names... You have invested all Your transcendental energies in them, and there are no hard and fast rules for chanting these names." This means that one can chant whether sitting, walking, cooking, or resting, and regardless of whether one is physically clean or unclean.

Srila Haridasa Thakura, the *namacharya* (the authority on chanting the holy name), demonstrated that the holy name does not consider one's material background. Whether one is born in a highly educated family or a socially marginalized one, the holy name acts universally to purify the chanter. Because the soul is pure spirit and eternal servant of Krishna, the practice of chanting bypasses the external bodily coverings and directly connects the individual soul with the Supreme Lord. Therefore, anyone, anywhere, can chant and attain the highest perfection of life."""
    },
    {
        "mainTopic": "Foundations of Hare Krishna Chanting",
        "subTopic": "Why Chanting Is the Universal Religion of the Soul",
        "article": """When people hear about the chanting of Hare Krishna, they sometimes mistake it for a sectarian Hindu practice or a regional religion. However, Srila Prabhupada often emphasized that the chanting of God's holy names is *sanatana-dharma*, the eternal, universal religion of the soul. The word "religion" often implies a faith that one can change, but *dharma* refers to the inherent, unchangeable characteristic of a living entity—which is to serve the Supreme Lord.

Every living entity is originally a spiritual being, fragmental and eternally connected to the Supreme Spirit, Krishna. Due to contact with material nature, we have temporarily forgotten this relationship and identified with various temporary designations such as our nationality, race, gender, or sectarian belief system. Chanting the mahāmantra is the spiritual medicine that cures this amnesia.

Because God is the father of all living entities, calling out His names—whether as Krishna, Allah, or Jehovah—is a universal principle of spiritual awakening. The Hare Krishna mantra is particularly potent because it directly addresses the Supreme Lord and His spiritual energy, pleading for engagement in His service. Thus, it transcends all bodily and geographical boundaries, acting as the true, inclusive religion of the soul that unites everyone on the spiritual platform of loving devotion."""
    },
    {
        "mainTopic": "Foundations of Hare Krishna Chanting",
        "subTopic": "The Spiritual Science of Mantra Meditation",
        "article": """The practice of chanting Hare Krishna is not merely a blind exercise of faith; it is a profound spiritual science based on the principle of transcendental sound vibration. In physics, we learn that sound waves can shatter glass, penetrate walls, and alter our brain waves. If subtle material sound has such power, we can understand that spiritual sound, which descends from beyond the material universe, has immense transformative capabilities.

The mind is compared to a mirror that has gathered the dust of countless lifetimes of material desires, anxieties, and misconceptions. The chanting of the mahāmantra is the scientific process of *ceto-darpaṇa-mārjanam*—cleansing the mirror of the mind. By absorbing the consciousness in the sound vibration of Krishna's names, the mind is gradually cleared of its material impurities and is brought to a state of absolute tranquility and focus.

Unlike mechanical forms of meditation which try to force the mind into a void or blank state—a nearly impossible feat for the active mind—mantra meditation gives the mind a positive, highly purifying focal point. As the chanter focuses on the sound *Hare*, *Krishna*, and *Rama*, the dormant spiritual consciousness is systematically awakened, allowing the practitioner to directly experience spiritual pleasure and enlightenment beyond the limitations of the physical senses."""
    },
    {
        "mainTopic": "Foundations of Hare Krishna Chanting",
        "subTopic": "How Chanting Connects the Soul to God",
        "article": """In our conditioned state, the Supreme Lord seems far away, imperceptible to our blunt material senses. We cannot see Him with our earthly eyes or touch Him with our hands. However, the Vedic scriptures reveal a deep esoteric truth: in the absolute realm, there is no difference between the Supreme Lord and His holy name.

The *Brhan-naradiya Purana* and other *shastras* confirm that God being Absolute, His name, form, qualities, and pastimes are identical to Him. In the material world, if you are thirsty and chant "water, water," your thirst will not be quenched because the word and the substance are different. But because Krishna is fully spiritual, when you chant "Krishna," He is personally present dancing on your tongue.

Through chanting, the soul is directly associating with the Supreme Personality of Godhead. Over time, as the offenses in chanting diminish and the practitioner's devotion grows, this connection becomes a tangible, localized experience. The veil of *maya* (illusion) is lifted, and the soul realizes its eternal relationship with God. Thus, the holy name acts as a direct, unbreakable telephone line connecting the wandering soul back to its supreme source."""
    },
    {
        "mainTopic": "Foundations of Hare Krishna Chanting",
        "subTopic": "Why the Holy Name Is the Most Merciful Process",
        "article": """Throughout the history of the universe, various methods of spiritual realization have been prescribed corresponding to different epochs (*yugas*). In Satya-yuga, people attained perfection by prolonged mystic meditation; in Treta-yuga, by performing grand sacrifices; and in Dvapara-yuga, by opulent temple worship. But in the current age of Kali-yuga—an age characterized by short lifespans, diminished intelligence, and continuous disturbances—these arduous methods are practically impossible to execute properly.

Recognizing the fallen condition of the souls in this age, the Supreme Lord incarnated as Sri Caitanya Mahaprabhu to distribute the most potent and easiest spiritual practice: the congregational chanting of the holy names (*sankirtana*). What previously took thousands of years of breath control and rigid asceticism to achieve can now be attained simply by sincerely vibrating the Hare Krishna mahāmantra.

This extreme accessibility is why chanting is considered the most merciful process. It requires no previous qualifications, no elaborate wealth, and no immense physical stamina. Whether one is deeply entangled in sinful life, suffering from mental distress, or completely ignorant of the Vedas, the holy name eagerly lifts the practitioner out of the material mire. It is the special concession for the modern age, proving that Krishna's mercy is far greater than our disqualifications."""
    },
    {
        "mainTopic": "Foundations of Hare Krishna Chanting",
        "subTopic": "The Importance of Chanting in the Age of Kali",
        "article": """The *Srimad-Bhagavatam* (12.3.51) gives a definitive verdict on the spiritual practice for the present age: *kaler doṣa-nidhe rājann asti hy eko mahān guṇaḥ / kīrtanād eva kṛṣṇasya mukta-saṅgaḥ paraṁ vrajet*. "My dear King, although Kali-yuga is an ocean of faults, there is still one good quality about this age: Simply by chanting the Hare Krishna mahāmantra, one can become free from material bondage and be promoted to the transcendental kingdom."

Kali-yuga is described as an ocean of faults because quarrel, hypocrisy, disease, and anxiety are rampant. Attempting to cross this ocean by our own strength or by inventing new spiritual methods is futile. The authorized scriptures repeatedly stress that in this turbulent age, the only viable lifeboat is the holy name. 

The *Brhan-naradiya Purana* emphatically repeats this injunction to remove all doubt: *harer nama harer nama harer namaiva kevalam / kalau nasty eva nasty eva nasty eva gatir anyatha*. "In this age of quarrel and hypocrisy, the only means of deliverance is the chanting of the holy names of the Lord. There is no other way. There is no other way. There is no other way." For anyone serious about spiritual progress in the modern world, making the chanting of Hare Krishna the center of one's life is not just an option; it is an absolute necessity."""
    },
    {
        "mainTopic": "Foundations of Hare Krishna Chanting",
        "subTopic": "Why Chanting Is the Heart of Devotional Service",
        "article": """Within the path of Bhakti Yoga, the *shastras* outline nine primary processes of devotional service, starting with *śravaṇaṁ* (hearing), *kīrtanaṁ* (chanting), and *smaraṇaṁ* (remembering the Lord). Among these, *kīrtanaṁ*—specifically the chanting of the Lord's holy names—is declared by the previous *acharyas* (spiritual masters) to be the most important and the root of all other devotional activities.

Srila Jiva Goswami explains that while there are other powerful processes of bhakti, such as deity worship or rendering physical service, their effectiveness in the current age is heavily dependent on being accompanied by the chanting of the holy name. Chanting nourishes all other limbs of devotional service. When we chant, we are simultaneously hearing (*śravaṇaṁ*), vibrating the name (*kīrtanaṁ*), and naturally remembering the Lord (*smaraṇaṁ*).

Sri Caitanya Mahaprabhu focused His entire movement on *nama-sankirtana* (the congregational chanting of the holy names) because it acts as the lifeblood of a devotee. Just as watering the root of a tree automatically nourishes the branches, leaves, and flowers, pouring one’s energy into sincerely chanting the Hare Krishna mahāmantra automatically awakens all good qualities and brings success in every other aspect of one's spiritual life."""
    },
    {
        "mainTopic": "Foundations of Hare Krishna Chanting",
        "subTopic": "The Philosophy Behind the Mahāmantra",
        "article": """To derive the maximum benefit from chanting, it is helpful to understand the deep philosophical meaning behind the specific words of the Hare Krishna mahāmantra. The mantra is composed of three primary Sanskrit words: *Hare*, *Krishna*, and *Rama*.

*Krishna* means "the all-attractive Supreme Personality of Godhead." God, being the origin of all beauty, power, knowledge, and opulence, is naturally the most attractive person. *Rama* means "the reservoir of all transcendental pleasure." This indicates that the Lord is completely full of spiritual bliss and imparts that bliss to His devotees. The word *Hare* (the vocative form of *Hara*) refers to the supreme spiritual energy of the Lord, personified as Srimati Radharani, who represents the compassionate, devotional aspect of God.

Therefore, when we chant the mahāmantra, we are addressing the Lord and His internal energy. Srila Prabhupada beautifully translated the mood of the mantra: "O spiritual energy of the Lord, O Supreme Personality of Godhead, please engage me in Your pure devotional service." Unlike mundane prayers that ask for material boons, the mahāmantra is a pure, unalloyed cry of the soul begging to be reinstated in its eternal constitutional position as a loving servant of God."""
    },
    {
        "mainTopic": "Foundations of Hare Krishna Chanting",
        "subTopic": "The Relationship Between Krishna and His Name",
        "article": """A core tenet of Gaudiya Vaishnava philosophy is the doctrine of *nama-tattva*—the truth that the Supreme Lord is non-different from His holy name. In the material world, duality exists. The word "fire" cannot burn you, and the word "mango" cannot satisfy your hunger, because the designation and the object are entirely separate.

However, in the absolute spiritual realm, there is no duality. The *shastras* declare *abhinnatvān nāma-nāminoḥ*: the name of the Lord and the Lord Himself are identical. When we utter the word "Krishna," Krishna is personally manifesting before us in the form of sound vibration. The holy name contains all of Krishna's potencies, His forms, His qualities, and His pastimes fully intact.

For a neophyte practitioner, this truth may seem theoretical because the heart is covered by material illusions, preventing the direct perception of the Lord in His name. But as the chanting continues and the heart becomes purified, the devotee progressively realizes that the holy name is a living, breathing reality. Ultimately, for a pure devotee, chanting the name of Krishna is an experience of intense spiritual ecstasy, identical to seeing Him face-to-face."""
    },
    {
        "mainTopic": "Foundations of Hare Krishna Chanting",
        "subTopic": "Why the Holy Name Is the Supreme Spiritual Practice",
        "article": """Many spiritual seekers ask: "If there are so many paths of yoga, meditation, and charity, why is the chanting of Hare Krishna considered the supreme practice?" The answer lies in both the ease of the process and the unmatched elevation of the goal it achieves.

Most spiritual practices aim at lower spiritual goals. Karma-yoga aims at material elevation or pious credits; Jnana-yoga aims at impersonal liberation (merging into the Brahman effulgence); and Ashtanga-yoga aims at mystic perfections (*siddhis*). But the chanting of the Hare Krishna mahāmantra aims directly at *krishna-prema*, the highest, unalloyed love for the Supreme Personality of Godhead, which immerses the soul in eternal service in the spiritual world of Goloka Vrindavana.

Sri Narottama Dasa Thakura sings, *golokera prema-dhana, hari-nāma-saṅkīrtana*—"The chanting of the holy name is the treasure of love of God that has descended directly from the spiritual world." It is unparalleled because it instantly grants what other processes cannot achieve even after lifetimes of striving: the pure, spontaneous affection of the soul for its eternal Lord, making it the undeniable king of all spiritual practices."""
    },
    {
        "mainTopic": "Foundations of Hare Krishna Chanting",
        "subTopic": "Why Chanting Is Recommended for Everyone",
        "article": """One of the greatest testaments to the authenticity of the Hare Krishna chanting process is its universal applicability and immediate practical benefits for people in every station of life. To practice it, one does not need to abandon their family, move to a Himalayan cave, or adopt an austere monastic lifestyle.

For the anxious professional, chanting reduces stress and clarifies the mind, providing a peaceful anchor amidst modern worldly turbulence. For the student, it sharpens memory and focus by purifying the intelligence. For those suffering emotionally or physically, it provides deep internal solace, reminding the soul that it transcends the temporary miseries of the material body.

Because the process simply requires moving the lips and hearing the sound, it is accessible to the elderly who can no longer perform strenuous physical yoga, to the poor who cannot afford elaborate rituals, and to children whose hearts are naturally receptive to joyful musical vibration (*kirtan*). The Hare Krishna mantra is the perfect spiritual medicine precisely because it is universally prescribed and completely safe, ensuring spiritual progression for absolutely anyone who takes it up."""
    },
    {
        "mainTopic": "Foundations of Hare Krishna Chanting",
        "subTopic": "The Timeless Tradition of Chanting the Holy Name",
        "article": """A common misconception is that the chanting of Hare Krishna is a modern invention or a new religious movement started in the 20th century. In truth, the chanting of the holy names is an ancient, timeless tradition deeply rooted in the oldest scriptures known to humanity, the Vedas.

The chanting of the mahāmantra has been practiced continuously through an unbroken chain of spiritual teachers (*parampara*) descending from antiquity. The mantra itself is explicitly listed in the *Kali-santarana Upanishad*, a prominent Vedic text, which recommends it above all other mantras for liberation in the current age. Over five hundred years ago, Sri Caitanya Mahaprabhu actively popularized this chanting across the Indian subcontinent.

When Srila Prabhupada brought the chanting of Hare Krishna to the West in 1965, he did not invent a new religion or alter the mantra to fit modern tastes. He simply presented this pure, undiluted spiritual tradition as he received it from his spiritual master, establishing it globally according to scriptural prophecy. Therefore, when one chants Hare Krishna, they are plugging into a timeless, fully authorized, and supremely potent spiritual lifeline that has successfully delivered countless souls for millennia."""
    }
]

for idx, data in enumerate(articles_data):
    # Determine the order
    order = get_next_order(data['mainTopic'])
    
    # Create the article
    from django.db import IntegrityError, transaction
    try:
        with transaction.atomic():
            article = ChantingArticle.objects.create(
                mainTopic=data['mainTopic'],
                subTopic=data['subTopic'],
                article=data['article'],
                order=order
            )
            print(f"Added article: {article.mainTopic} - {article.subTopic} (Order: {article.order})")
    except IntegrityError:
        print(f"Article already exists (slug conflict): {data['mainTopic']} - {data['subTopic']}")


print("Finished adding bulk articles.")
