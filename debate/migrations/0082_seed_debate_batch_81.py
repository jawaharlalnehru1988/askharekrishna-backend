from django.db import migrations
from django.utils.text import slugify


DEBATE_DATA = [
    {
        "mainTopic": "Islamic Theological Challenges to Krishna Consciousness",
        "subTopic": "Doesn't Islam's revelation (Quran) supersede older texts like the Vedas?",
        "article": (
            "This is one of the most important questions in Hindu-Muslim dialogue, and it deserves a respectful answer. From the Islamic viewpoint, the Quran is final revelation, preserved and complete, and therefore earlier revelations are either partial, historically limited, or superseded. So when a Muslim asks this, they are not attacking for sport. They are being consistent with their theology.\n\n"
            "A Krishna-conscious response should begin by honoring that sincerity. Then it can ask a deeper philosophical question: what does 'final' mean? Does final automatically mean earlier revelations are false? Or can it mean a later revelation for a specific community and historical mission, without erasing other authentic disclosures of the Divine?\n\n"
            "A modern analogy helps. In law, a new ruling may clarify application in one jurisdiction without nullifying every earlier legal principle from all civilizations. In science, a later paper can refine a model without proving that all prior observations were useless. Development does not always mean cancellation.\n\n"
            "From the Vedic side, revelation is often understood as recurring and multi-layered, not one-time and closed. Divine knowledge appears repeatedly across ages according to the needs and consciousness of people in different contexts. The Bhagavad-gita itself speaks of timeless wisdom being taught repeatedly across cycles (BG 4.1-3). So the Vedic framework is not threatened by chronology. It sees revelation as dynamic pedagogy.\n\n"
            "A Muslim friend may reply: 'But if revelations differ, they cannot all be equally true.' Fair point. Vaishnava response is that different revelations can vary in emphasis while converging on core theism: God is supreme, we are accountable, and human life should become surrendered and ethical. Differences in law, ritual, social order, and metaphysical detail may reflect historical mission rather than simple contradiction.\n\n"
            "From Vedic application, the question becomes practical: which text most fully explains the nature of the soul, karma, devotion, divine personality, and the path to sustained God-consciousness? Vaishnavas hold that the Vedic corpus, especially Bhagavad-gita and Bhagavata Purana, provides unmatched philosophical depth in these areas.\n\n"
            "This does not require insulting the Quran. It means evaluating traditions by scope and theological granularity. A text may be perfect for one revelatory purpose and still not claim to elaborate every metaphysical dimension another tradition develops.\n\n"
            "Srila Prabhupada's method was often to find common ground first: if a scripture teaches remembrance of God, moral discipline, and surrender to the Supreme, respect it. Then go deeper into the science of bhakti and the detailed ontology of Bhagavan, jiva, and prakriti.\n\n"
            "In conversation, a strong response is: 'I respect the Islamic belief in final revelation. From a Vedic standpoint, revelation is recurring and context-sensitive rather than closed in a single historical moment. Later does not automatically mean all earlier revelation is invalid. The meaningful comparison is: which scripture gives the most complete and transformative account of God, the soul, and loving service? Vaishnava tradition says the Vedic texts do that in exceptional depth.'\n\n"
            "That keeps the tone respectful, comparative, and serious."
        ),
        "order": 239,
        "language": "en",
    },
    {
        "mainTopic": "Islamic Theological Challenges to Krishna Consciousness",
        "subTopic": "How can idols represent the unseen, infinite divine reality?",
        "article": (
            "This question comes naturally from Islamic theology because Islam fiercely protects divine transcendence and rejects image-based worship. So when someone asks this, they are safeguarding tawheed, not merely criticizing another culture. A respectful answer must acknowledge that concern clearly.\n\n"
            "Now the Vaishnava clarification: deity worship is not the claim that stone is independently God. It is the claim that the infinite Lord can choose to be present and approachable through a consecrated form for the sake of embodied beings. The initiative is divine, not material.\n\n"
            "Think of a modern analogy from communications. A voice call comes through a tiny speaker in your phone. Nobody says your mother has been reduced to plastic and metal. The device is a medium of real presence in relationship. In the same way, murti in Vaishnava theology functions as an authorized medium of divine presence, not a replacement deity manufactured by human imagination.\n\n"
            "A Muslim may say: 'But God does not need images to be present.' Vaishnava agrees God does not need them. The point is that humans often need concrete focus for loving service. Bhagavad-gita 12.5 itself says progress on the unmanifest path is very difficult for embodied beings. The arcana form is a compassionate concession for relational practice, not a limitation imposed on God.\n\n"
            "From Vedic application, deity worship is governed by theology and discipline: consecration, mantra, purity, service standards, and scriptural guidelines from Pancharatra and bhakti texts. It is not arbitrary object attachment. The structure exists precisely to prevent reduction into superstition.\n\n"
            "There is also internal logic in avatara theology: if God can reveal Himself through sound (scripture), saintly persons, and historical descents, why can He not reveal Himself through consecrated form? Denying this possibility may unintentionally limit divine freedom.\n\n"
            "A modern design analogy: a complex operating system may be invisible in raw code, yet it offers a graphical interface so ordinary users can genuinely interact with it. The interface does not diminish the system's depth. It makes relationship possible. Arcana serves that devotional interface function.\n\n"
            "Srila Prabhupada consistently called deity worship arca-vigraha, not idol worship, and taught that sincere service before the deity purifies consciousness and awakens real God relationship.\n\n"
            "In conversation, a useful response is: 'I understand why image-worship seems problematic from Islamic monotheism. But Vaishnava deity worship is not worship of matter as God. It is worship of the one infinite Lord who, by His own will, becomes accessible through consecrated form for embodied devotees. The form is medium, not rival. The goal is remembrance, surrender, and love of the unseen Supreme.'\n\n"
            "That keeps both reverence and philosophical clarity intact."
        ),
        "order": 240,
        "language": "en",
    },
    {
        "mainTopic": "Islamic Theological Challenges to Krishna Consciousness",
        "subTopic": "Isn't idol worship prohibited in Islamic monotheism?",
        "article": (
            "Yes, within Islamic theology, idol worship is prohibited. That part should be acknowledged directly without argument games. The real interfaith discussion is not whether Islam prohibits it. It does. The discussion is whether Vaishnava deity worship is the same thing Islam means by idol worship.\n\n"
            "In Islamic usage, idolatry means assigning divinity to created objects or partners besides Allah. Vaishnava theology rejects that too. It does not say material objects are independent gods. It says the one Supreme Lord may accept service through a consecrated form He authorizes.\n\n"
            "So both traditions reject autonomous finite objects as ultimate. The divergence is in sacramental logic: Islam typically refuses visual mediation to prevent theological drift, while Vaishnavism allows controlled divine mediation through arcana to cultivate personal devotion.\n\n"
            "A modern analogy is policy design. Two safety systems may aim at the same outcome but use different mechanisms. One system bans all risky access paths. Another permits limited access through strict protocols and supervision. Same concern, different method.\n\n"
            "From the Vedic side, deity worship has strict protocol precisely so it does not become casual object worship: initiation, mantra, purity rules, daily seva, scriptural education, and philosophical grounding. Without this framework, Vaishnava teachers themselves would call the practice degraded.\n\n"
            "A Muslim friend might still say, 'Even with protocol, representation risks confusion.' That is a fair concern, and honest dialogue should admit this as a real doctrinal difference. But difference is not dishonesty. Each system tries to protect divine supremacy in its own coherent way.\n\n"
            "Bhagavad-gita repeatedly centers devotion on the Supreme source, not on independent finite powers. Vaishnava commentators emphasize that all worship must culminate in surrender to Bhagavan. The arcana process is meant to train that surrender, not replace it.\n\n"
            "Srila Prabhupada often explained with practical clarity: if one understands philosophy, deity worship deepens personal service to Krishna; if one does not, external ritual becomes mechanical. So education and siddhanta are essential companions of worship.\n\n"
            "In conversation, a balanced response is: 'You are right that Islam prohibits idol worship. Vaishnava tradition also rejects worship of independent material objects as ultimate. Our claim is different: the one Supreme can accept worship through consecrated form as an act of grace for embodied souls. So the issue is not lawlessness versus monotheism, but two different theological methods for protecting divine unity and cultivating devotion.'\n\n"
            "That answer remains respectful, exact, and debate-ready."
        ),
        "order": 241,
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
        ('debate', '0081_seed_debate_batch_80'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_code=unseed_data),
    ]
