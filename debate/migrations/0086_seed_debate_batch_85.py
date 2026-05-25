from django.db import migrations
from django.utils.text import slugify


DEBATE_DATA = [
    {
        "mainTopic": "Islamic Theological Challenges to Krishna Consciousness",
        "subTopic": "Why should modern Muslims consider Krishna relevant when Islam is complete?",
        "article": (
            "This is a fair and deeply identity-level question. If Islam is complete and final, why should a modern Muslim engage Krishna at all? The concern is understandable: many fear that engagement means compromise, dilution, or confusion. So the first respectful answer is this: sincere engagement does not require disloyalty. Understanding another tradition is not the same as abandoning your own.\n\n"
            "From a Krishna-conscious perspective, the relevance of Krishna can be presented in two ways: theological and civilizational. Theological relevance asks whether Krishna discourse can deepen conversation on divine personhood, love, surrender, and metaphysics. Civilizational relevance asks how billions of people can coexist with dignity in plural societies without reducing each other to stereotypes.\n\n"
            "A modern analogy: medical specialists in different systems may disagree on foundational models, yet still study each other's methods to improve understanding and outcomes. Engagement does not erase differences; it clarifies them and often improves practice.\n\n"
            "A Muslim interlocutor may say: but if revelation is complete, additional frameworks are unnecessary. Vaishnava reply can be: necessity and relevance are not identical. You may not need another scripture for your own covenantal path, yet still find relevance in comparative theology, ethical dialogue, and shared God-centered values that reduce conflict and increase wisdom.\n\n"
            "From Vedic application, Krishna is presented as the Supreme source of all beings (BG 10.8), and all authentic spiritual striving is seen as ultimately connected to the one Supreme Reality. So Vaishnava tradition naturally invites dialogue rather than isolation. It argues that hearing about Krishna can illuminate universal theistic questions even for those committed to other lineages.\n\n"
            "There is also practical relevance in social ethics. Krishna bhakti emphasizes disciplined living, remembrance of God, self-control, compassion, and service. These values overlap with many Islamic moral commitments. Shared ethical space can become a foundation for cooperation without forced theological merger.\n\n"
            "A technology analogy helps: different operating systems can run different interfaces but still communicate through shared protocols. Interoperability does not require identical architecture. Likewise, traditions can remain doctrinally distinct while cultivating spiritual interoperability in humility, justice, and God-conscious conduct.\n\n"
            "Srila Prabhupada often encouraged respectful dialogue with Muslims and Christians by emphasizing common submission to God and reform of materialistic life. He argued that real religion is not sectarian competition but awakening love and obedience to the Supreme.\n\n"
            "In conversation, a balanced response is: 'If you are a committed Muslim, engagement with Krishna need not mean replacing Islam. It can mean deepening your understanding of how other theistic traditions approach God, personhood, and devotion, while strengthening peaceful coexistence. From the bhakti side, Krishna is relevant because He is understood as universally related to all souls, not confined to one ethnicity or era.'\n\n"
            "That response preserves identity, respect, and intellectual seriousness."
        ),
        "order": 251,
        "language": "en",
    },
    {
        "mainTopic": "Islamic Theological Challenges to Krishna Consciousness",
        "subTopic": "Doesn't Islamic theology better explain divine justice and human responsibility?",
        "article": (
            "This is one of the strongest comparative questions because it deals with real moral pain: suffering, accountability, fairness, and final judgment. Islamic theology offers a compelling structure: one life, clear moral law, divine omniscience, final judgment, and proportional recompense. Many people experience that framework as morally clean and existentially serious.\n\n"
            "A Krishna-conscious response should begin by acknowledging that strength honestly. Then it can ask whether clarity alone resolves all justice questions, especially those involving unequal life conditions and developmental asymmetry.\n\n"
            "In Vedic thought, justice is extended through karma across multiple births. Responsibility is not removed; it is expanded over time. Every action has consequence, every intention leaves imprint, and moral causality is continuous. The system aims to answer why people begin life with radically different circumstances without assigning arbitrariness to God.\n\n"
            "A modern analogy: imagine judging athletes from different backgrounds after one race without accounting for lifelong training conditions, injuries, or access disparities. A multi-stage evaluation across a longer horizon may appear less simple, but can be more distributively fair. Karma-rebirth framework operates similarly at metaphysical scale.\n\n"
            "A Muslim friend may respond: God can judge perfectly even with one life. Vaishnava thought agrees God can. The divergence is not divine competence, but revealed cosmic structure. One model emphasizes linear historical judgment; another emphasizes cyclical moral development culminating in liberation.\n\n"
            "From Vedic application, human responsibility remains intense: present choices shape future births and spiritual trajectory. Bhagavad-gita teaches no sincere effort is lost (BG 2.40), but also insists on disciplined action, self-control, and surrender. So karma is not fatalism; it is accountability with hope.\n\n"
            "Another practical analogy is rehabilitation justice versus purely punitive justice. A system can punish wrongdoing, or it can include pathways for transformation and reintegration. Vedic cosmology leans strongly toward transformative justice across lifetimes while preserving causal accountability.\n\n"
            "Srila Prabhupada often emphasized personal responsibility: stop sinful habits, chant, serve, and reform consciousness now. He rejected passive karma excuses and taught that bhakti can rapidly alter karmic trajectory through surrender to Krishna.\n\n"
            "In conversation, a strong response is: 'Islamic theology provides powerful moral clarity and accountability, and I respect that. Vedic theology offers a different justice architecture: karmic continuity across lifetimes, where no action is lost and no inequality is random. Human responsibility remains central, but divine justice is worked out over a broader temporal horizon aimed at transformation and liberation.'\n\n"
            "That keeps the comparison fair and philosophically robust."
        ),
        "order": 252,
        "language": "en",
    },
    {
        "mainTopic": "Islamic Theological Challenges to Krishna Consciousness",
        "subTopic": "How can Hinduism's caste system coexist with Islamic principles of human equality?",
        "article": (
            "This is a critical question, especially in South Asian contexts where social wounds are real. From Islamic teaching, human equality before God is foundational: no inherent superiority by birth, race, or lineage, only moral and spiritual excellence. So when caste oppression is associated with Hindu society, the critique is morally serious and cannot be brushed aside.\n\n"
            "A responsible Krishna-conscious response starts with honesty: birth-based discrimination and humiliation are wrong, and whenever they occur, they violate genuine spiritual principles. Defensive denial helps no one.\n\n"
            "Then comes the doctrinal distinction. Classical Vedic teaching of varna is based on guna (qualities) and karma (work), not janma (birth). Bhagavad-gita 4.13 explicitly frames social classification by qualities and actions. So hereditary caste absolutism is better understood as historical social distortion than theological ideal.\n\n"
            "A modern analogy: a constitution may guarantee equality while social institutions still practice discrimination. The failure belongs to distorted implementation, not to the ethical core of the constitution itself. Similarly, caste abuse reflects social degeneration, not the highest siddhanta.\n\n"
            "A Muslim interlocutor may still respond: but the distortion became entrenched for centuries. That criticism is valid and must be acknowledged. Vaishnava reform movements, including many bhakti traditions, historically challenged caste exclusivism by centering devotion over birth and opening spiritual access widely.\n\n"
            "From Vedic application, Krishna bhakti is radically inclusive at the spiritual level: any person who takes shelter of bhakti can attain the highest destination regardless of social background (see BG 9.32 in Vaishnava interpretation). Spiritual identity as jiva transcends caste labels.\n\n"
            "A workplace analogy helps: organizations once dominated by legacy networks can be restructured around competence and integrity. Reform is real when evaluation criteria shift from inherited status to demonstrated quality. Bhakti does something similar spiritually: from birth privilege to devotion qualification.\n\n"
            "Srila Prabhupada repeatedly emphasized that Krishna consciousness is for everyone, not one caste. He initiated disciples globally across races and backgrounds, directly contesting the idea that access to God is birth-restricted.\n\n"
            "In conversation, a balanced response is: 'Islamic equality critique is morally important and should be heard. Birth-based caste discrimination is a social wrong, not a spiritual ideal. Vedic texts define social function by qualities and work, and bhakti traditions emphasize universal access to God beyond birth identity. The right comparison is between Islamic equality principles and reformed, scripturally grounded bhakti practice, not between ideals and historical abuses alone.'\n\n"
            "That response is honest, accountable, and constructive."
        ),
        "order": 253,
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
        ('debate', '0085_seed_debate_batch_84'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_code=unseed_data),
    ]
