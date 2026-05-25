from django.db import migrations
from django.utils.text import slugify


DEBATE_DATA = [
    {
        "mainTopic": "Islamic Theological Challenges to Krishna Consciousness",
        "subTopic": "How can Krishna be God when Islam affirms strict monotheism (Tawheed)?",
        "article": (
            "This is a powerful and sincere question, and the best way to answer it is with respect. When a Muslim says, 'How can Krishna be God when Islam teaches Tawheed?' they are not just making a logical objection. They are defending something sacred: Allah is one, without partner, without equal, beyond comparison. That commitment to divine unity is the beating heart of Islam. So the conversation has to begin with honor, not argument.\n\n"
            "Now here is an important first step: Krishna-conscious theology also affirms one ultimate Supreme Reality. So the core disagreement is usually not 'one God versus many gods' in a simplistic sense. The disagreement is about how that one Supreme Reality is understood and approached.\n\n"
            "A helpful modern analogy is language. One person says 'water,' another says 'maa,' another says 'pani.' Different words, same underlying reality. Of course theology is much deeper than vocabulary, but the analogy helps: different traditions may emphasize different divine attributes, forms of worship, and metaphysical structures while still trying to speak about the ultimate source.\n\n"
            "From the Vedic side, Krishna in Bhagavad-gita is not presented as one deity among competitors. He says, 'I am the source of all spiritual and material worlds. Everything emanates from Me.' (BG 10.8). He also says, 'There is no truth superior to Me.' (BG 7.7). So Vaishnava claim is radical monotheism in its own framework: one Supreme source, with many energies and manifestations, but not many independent gods fighting for cosmic sovereignty.\n\n"
            "A Muslim may still respond: 'But if God is one, why so many names and forms?' That is fair. Vaishnava response is that plurality of names does not mean plurality of ultimate beings. One person can be called father, teacher, judge, and friend in different relationships without becoming four different people. Similarly, the one Supreme can be addressed according to different revealed qualities and relationships.\n\n"
            "Now comes the delicate point: Islam strongly rejects associating partners with Allah (shirk). Vaishnava theology also rejects the idea that anyone is equal to the Supreme. Devas are empowered beings, not independent equals to Bhagavan. If someone treats finite beings as ultimate independent gods, Vaishnava siddhanta itself would call that misunderstanding.\n\n"
            "So where do we honestly differ? Islam generally emphasizes divine transcendence and formless incomparability in a very strict way. Krishna bhakti includes transcendence but also insists on divine personality and relational form. It says the Supreme is not less than personal; He is supremely personal. Form is not a limitation when the form is spiritual (sac-cid-ananda), self-existent, and beyond material composition.\n\n"
            "Think of another modern comparison: software in cloud architecture can appear through many interfaces without being divided into separate systems. The core remains one. Many access points do not imply many independent backends. In Vaishnava terms, the one Supreme can be approached through different revealed names and relationships while remaining absolutely one in ontological sourcehood.\n\n"
            "Srila Prabhupada often encouraged respectful dialogue with Muslims and Christians by emphasizing common ground first: God is supreme, we are servants of God, and life's purpose is to remember and serve Him. Then he would explain Krishna as the fullest revelation of that same Supreme Person, not as a rival tribal deity.\n\n"
            "In conversation, a strong response is: 'I deeply respect Tawheed. Krishna consciousness also teaches one ultimate Supreme source. The real discussion is not whether God is one, but whether that one Supreme is only approached as absolutely transcendent, or also as eternally personal and relational. Vaishnava theology says the one God can reveal unlimited names and forms without losing unity. That is not polytheistic rivalry. It is unified theism with relational depth.'\n\n"
            "That keeps the dialogue principled, respectful, and intellectually honest."
        ),
        "order": 233,
        "language": "en",
    },
    {
        "mainTopic": "Islamic Theological Challenges to Krishna Consciousness",
        "subTopic": "Doesn't polytheism contradict the concept of divine unity?",
        "article": (
            "This objection comes quickly in almost every Hindu-Muslim theological conversation: 'Doesn't polytheism contradict divine unity?' On the surface it seems decisive. If God is one, then worship of many forms appears logically incoherent. So let us slow it down and separate three things people often mix together: ontology, worship practice, and symbolism.\n\n"
            "Ontology asks: how many ultimate independent realities exist? Vaishnava answer: one. Worship practice asks: how many forms or names are used to approach that ultimate? Vaishnava answer: many. Symbolism asks: how does tradition communicate divine attributes? Vaishnava answer: through multiple narratives, forms, and lila contexts. Confusion begins when these three layers are collapsed into one.\n\n"
            "A modern parallel is white light through a prism. One beam enters, many colors appear. The many colors are not separate suns. They are differentiated expressions of one source interacting with conditions of perception. Vaishnava theology uses this kind of logic: one Supreme Reality, many energies, many manifestations, many relational entrances. Plural expression does not require plural ultimates.\n\n"
            "Bhagavad-gita supports this structure. Krishna says that even when people worship other deities with faith, that faith is ultimately sanctioned by Him (BG 7.21), and the fruits are also granted through Him (BG 9.23-24, interpreted through Vaishnava commentaries). In other words, all power remains sourced in one Supreme center. This is not metaphysical democracy of equal gods. It is hierarchical unity with delegated functions.\n\n"
            "A Muslim interlocutor may say, 'But practically people worship many gods as if they are separate.' That observation can be true at folk level in any religion. Popular religion often includes theological confusion. But in debate, we must engage the best doctrinal form of a tradition, not only its weakest popular distortions. Classical Vaishnava siddhanta is clear: Bhagavan is supreme; devas are dependent.\n\n"
            "From the Vedic application side, this is where achintya-bhedabheda helps. Reality includes simultaneous oneness and difference. Everything is one with the Supreme as His energy, yet different as distinct identities and functions. Divine unity is preserved at source level; diversity is preserved at relational and energetic level.\n\n"
            "Compare this to governance. One sovereign state has multiple ministries: education, health, finance, justice. Citizens interface with different ministries for different needs, but nobody concludes there are five independent sovereign states. Unity at the top, diversity in operation. Vaishnava theology often works like that metaphysically.\n\n"
            "Now does this fully satisfy strict Tawheed? Not always, because Islamic theology usually refuses mediated devotional plurality that might blur direct devotion to Allah alone. That is a real doctrinal divergence and should be admitted honestly. But divergence does not mean contradiction by default. It may mean different models of safeguarding divine unity: Islam safeguards by strict exclusion of devotional multiplicity, while Vaishnavism safeguards by ontological hierarchy and source-dependence.\n\n"
            "Srila Prabhupada's practical approach was to bring people back to the center: if God is one, then life should become God-centered, disciplined, and free from material egoism. He emphasized that mature theism means understanding who is supreme and acting accordingly.\n\n"
            "In conversation, a useful response is: 'If polytheism means many independent supreme beings, yes, that contradicts divine unity. But Vaishnava theology does not teach that. It teaches one Supreme source with many dependent manifestations and relational forms. The question is not unity versus plurality in the abstract; it is whether plurality is independent or sourced. In Krishna consciousness, it is always sourced in one Supreme Reality.'\n\n"
            "That keeps the answer logical, non-defensive, and faithful to siddhanta."
        ),
        "order": 234,
        "language": "en",
    },
    {
        "mainTopic": "Islamic Theological Challenges to Krishna Consciousness",
        "subTopic": "Why worship a human incarnation instead of the transcendent Creator?",
        "article": (
            "This is a profound question and many sincere Muslims ask it with real reverence: 'If God is transcendent and beyond all likeness, why worship a human incarnation?' From Islamic viewpoint, transcendence protects divine majesty. If the Creator is reduced to created form, worship risks confusion and idolatry. That concern is understandable and deserves a careful answer.\n\n"
            "A helpful starting point is this: Krishna bhakti does not deny transcendence. It says transcendence is complete enough to include immanence by choice. The Supreme is not forced into matter. The Supreme can reveal Himself personally without ceasing to be transcendent.\n\n"
            "In Bhagavad-gita Krishna says He appears by His own internal potency (BG 4.6): unborn, imperishable, yet manifesting in history. Vaishnava interpretation is that avatara is not karmic birth. It is voluntary descent. So the issue is not 'God trapped in flesh,' but 'God freely self-revealing in accessible form.'\n\n"
            "A modern analogy: a university professor teaching kindergarten for one hour does not lose her doctorate. She is not reduced by accessibility. Her willingness to enter the student's level is an expression of competence and care, not limitation. Similarly, avatara is interpreted as divine compassion: the Infinite meets finite beings where they can actually relate.\n\n"
            "Muslim critique may answer: 'God can guide without becoming embodied, through prophets and revelation.' Vaishnava tradition agrees that revelation and saintly teachers are valid channels. But it adds that direct divine descent is also possible and meaningful. If the Supreme is truly omnipotent, then self-manifestation in personal form cannot be ruled out a priori. Denying that possibility may itself limit divine freedom.\n\n"
            "From Vedic application, worship of Krishna is worship of the transcendent Creator Himself, not of a merely historical hero. His apparently human pastimes are understood as lila, transcendental acts performed in a humanly relatable mode. The form is spiritual (sac-cid-ananda-vigraha), not material like ours.\n\n"
            "There is also a relational dimension. Many people can respect a distant sovereign, but love deepens when there is personal reciprocity. Bhakti insists that the highest spiritual fulfillment is not only obedience before majesty, but loving exchange with the Supreme Person. The avatara principle serves that intimacy without denying sovereignty.\n\n"
            "Consider technology design: a powerful system with no user interface is theoretically impressive but practically inaccessible to most users. A well-designed interface does not diminish backend power; it allows relationship and use. In devotional terms, divine form is like a grace-filled interface that allows embodied souls to hear, remember, serve, and love.\n\n"
            "Srila Prabhupada repeatedly explained that Krishna's humanlike activities are the highest revelation of God's sweetness, not evidence of limitation. He would say that if God is truly great, He can be great in majesty and great in intimacy.\n\n"
            "In conversation, a strong response is: 'I honor the concern for divine transcendence. Krishna bhakti also affirms transcendence, but it adds that the transcendent Creator can freely reveal Himself in personal form without becoming materially limited. Avatara is not reduction of God; it is compassion of God. Worshiping Krishna is not preferring a human over the Creator, but worshiping the Creator who chose to become personally accessible.'\n\n"
            "That answer preserves respect, logic, and devotional depth all at once."
        ),
        "order": 235,
        "language": "en",
    },
]


def seed_data(apps, schema_editor):
    DebateArticle = apps.get_model('debate', 'DebateArticle')
    for entry in DEBATE_DATA:
        slug_value = slugify(f"{entry['mainTopic']} {entry['subTopic']}")[:280]
        DebateArticle.objects.update_or_create(
            mainTopic=entry['mainTopic'],
            subTopic=entry['subTopic'],
            defaults={
                'article': entry['article'],
                'slug': slug_value,
                'order': entry['order'],
                'language': entry['language'],
            },
        )


def unseed_data(apps, schema_editor):
    DebateArticle = apps.get_model('debate', 'DebateArticle')
    for entry in DEBATE_DATA:
        DebateArticle.objects.filter(
            mainTopic=entry['mainTopic'],
            subTopic=entry['subTopic'],
        ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('debate', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_code=unseed_data),
    ]
