from django.db import migrations
from django.utils.text import slugify


DEBATE_DATA = [
    {
        "mainTopic": "Islamic Theological Challenges to Krishna Consciousness",
        "subTopic": "Why practice rituals and idol worship when Islam emphasizes direct connection to God?",
        "article": (
            "This question is sincere and important. From an Islamic perspective, direct turning to God in prayer without images is a great strength. It protects divine transcendence, reduces confusion, and keeps worship focused. That concern deserves respect, not dismissal.\n\n"
            "A Krishna-conscious response starts by saying: direct connection to God is also central in bhakti. Chanting the holy name, hearing scripture, and heartfelt prayer are all direct practices. The difference is that Vaishnava tradition also uses ritual and deity worship as embodied aids for attention, remembrance, and loving service.\n\n"
            "Think of a modern analogy from learning science. You can understand physics through pure equations, but many students learn better with labs, models, and experiments. The labs are not a distraction from truth; they help embodiment of truth. In the same way, ritual in bhakti is meant to embody devotion, not replace it.\n\n"
            "A Muslim friend may ask: if God is near, why need ritual structure at all? Because human minds are unstable. Ritual creates rhythm, discipline, and repeated God-centered orientation through body, speech, and mind together. Without structure, many people drift into occasional emotion rather than sustained spiritual life.\n\n"
            "From Vedic application, arcana is not random ceremony. It is regulated worship with scriptural standards, purity disciplines, mantras, and service attitudes. The intent is inner transformation: humility, attention, gratitude, and surrender. If ritual becomes mechanical, tradition itself critiques it as shallow.\n\n"
            "A practical analogy: fitness goals are personal and inward, but many people succeed only with concrete routines, schedules, and guided forms. Routine does not negate authenticity; it stabilizes it. Ritual can function similarly in spiritual life.\n\n"
            "Bhagavad-gita's broader teaching supports this integration: remember God always, offer your work, mind, and devotion to Him. Ritual is one channel among several for this offering. It is not mandatory in one single uniform format for everyone, but it is deeply useful for many seekers.\n\n"
            "Srila Prabhupada emphasized both: the heart of practice is chanting and surrender to Krishna, while deity worship and temple ritual train the senses in personal service. He warned that external form without inner devotion is incomplete, but inner devotion without discipline often remains sentimental and unstable.\n\n"
            "In conversation, a balanced response is: 'I respect Islam's emphasis on direct devotion to God. Krishna consciousness also values direct connection deeply. Our tradition adds ritual and deity worship as disciplined embodied practices that help stabilize remembrance and loving service. For us, they are means of concentration and surrender, not substitutes for God.'\n\n"
            "That keeps the tone respectful, practical, and theologically clear."
        ),
        "order": 248,
        "language": "en",
    },
    {
        "mainTopic": "Islamic Theological Challenges to Krishna Consciousness",
        "subTopic": "Isn't the Islamic concept of prophethood different from Hindu avatars?",
        "article": (
            "Yes, the Islamic concept of prophethood and the Hindu concept of avatara are different, and it is better to admit that clearly than to force a false equivalence. In Islam, prophets are human messengers chosen by God to convey revelation and guidance. They are not God. In Vaishnava theology, avataras are divine descents of the Supreme Himself.\n\n"
            "So at the level of definition, difference is real. But dialogue can still ask a second question: are they completely unrelated, or do they play partly parallel roles in divine guidance?\n\n"
            "A modern analogy: in one system, the founder sends certified representatives with full instructions. In another system, the founder sometimes appears personally and sometimes sends representatives. Both systems involve guidance, authority, and transmission, but the mode differs.\n\n"
            "From Vedic application, both categories actually exist: there are avataras (divine descents) and there are empowered teachers and rishis who function as messengers. So Vaishnava framework can conceptually recognize something similar to prophetic function while still maintaining the unique avatara doctrine.\n\n"
            "A Muslim interlocutor may say: allowing divine incarnation compromises transcendence. Vaishnava reply is that divine freedom includes the freedom to self-manifest without losing transcendence. If God is truly sovereign, self-revelation in personal form cannot be ruled out in principle.\n\n"
            "Bhagavad-gita 4.7-8 describes descent when dharma declines. This is not karmic birth but purposeful intervention. Prophethood in Islam and avatara in Vaishnavism can thus be seen as two theological models of how God restores guidance: through chosen human messengers in one model, and through both messengers and divine descent in the other.\n\n"
            "A systems analogy helps: some organizations escalate all issues through delegated managers; others include rare direct intervention by the founder during crisis. Both aim at order restoration. The disagreement is over governance style, not over the need for guidance.\n\n"
            "Srila Prabhupada often took this approach in dialogue: appreciate prophets and saints who teach surrender to God, while explaining Krishna as the original Supreme Person who may appear directly and also send representatives.\n\n"
            "In conversation, a clear response is: 'You are right that Islamic prophethood and Hindu avatara are not identical. Prophets are divinely guided human messengers; avataras are divine descents. The shared ground is that both traditions affirm God does not abandon humanity and provides guidance in history. The real debate is about mode of guidance, not whether guidance exists.'\n\n"
            "That is honest, respectful, and precise."
        ),
        "order": 249,
        "language": "en",
    },
    {
        "mainTopic": "Islamic Theological Challenges to Krishna Consciousness",
        "subTopic": "How does Krishna consciousness address the Islamic prohibition against idolatry?",
        "article": (
            "This objection is central in Hindu-Muslim conversations and should be treated carefully. Islam prohibits idolatry to protect pure monotheism and prevent confusion between Creator and creation. Krishna consciousness can acknowledge that concern as a serious and valid theological safeguard.\n\n"
            "The key Vaishnava response is definitional: what Islam rejects as idolatry and what Vaishnavism practices as arcana are not claimed to be the same act. Vaishnavism does not teach that matter itself is independently divine. It teaches that the one Supreme can accept worship through consecrated form by divine sanction.\n\n"
            "A modern communication analogy: when you salute a national flag, you are not worshiping cloth fibers. You are honoring the reality symbolized and represented through the medium. Vaishnava arcana similarly treats form as authorized medium, not autonomous deity.\n\n"
            "A Muslim friend may still object: even symbolic mediation risks sliding into object fixation. That is a fair pastoral concern. Vaishnava tradition addresses it by strict theology, regulated practice, and constant scriptural reinforcement that Bhagavan is supreme, infinite, and never reducible to matter.\n\n"
            "From Vedic application, deity worship requires consecration, purity discipline, mantra, and service mentality. The process is pedagogical: train senses to serve God rather than exploit matter. If someone treats deity as mere object, that is considered ignorance within the tradition itself.\n\n"
            "Another analogy: in education, diagrams are not the reality itself but can give real access to understanding. A chemistry model is not a molecule, yet through the model students genuinely learn molecular behavior. Arcana operates similarly at devotional level: a spiritually authorized model of engagement with divine presence.\n\n"
            "Bhagavad-gita's center remains surrender to the Supreme source. Deity worship is one mode of cultivating that surrender, not a rival theology of multiple independent gods.\n\n"
            "Srila Prabhupada consistently used the term arca-vigraha and insisted this is not idol worship in the crude sense. He stressed philosophy plus practice: understand Krishna's supremacy, then engage senses in service through worship.\n\n"
            "In conversation, a balanced response is: 'I respect Islam's prohibition as a way to guard monotheism. Krishna consciousness addresses that concern by distinguishing idolization of matter from worship of the one Supreme through consecrated form. Arcana is not competition with God; it is disciplined training in remembrance and loving service to God.'\n\n"
            "That keeps dialogue calm, respectful, and conceptually accurate."
        ),
        "order": 250,
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
        ('debate', '0084_seed_debate_batch_83'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_code=unseed_data),
    ]
