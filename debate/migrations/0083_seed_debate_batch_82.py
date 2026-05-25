from django.db import migrations
from django.utils.text import slugify


DEBATE_DATA = [
    {
        "mainTopic": "Islamic Theological Challenges to Krishna Consciousness",
        "subTopic": "Why believe in reincarnation instead of a single life with judgment?",
        "article": (
            "This question goes straight to the heart of justice, mercy, and human destiny. From an Islamic viewpoint, one life followed by judgment is morally serious, clear, and urgent: life is a trust, actions matter, and accountability is real. That moral sharpness is deeply valuable, and a respectful conversation should acknowledge it immediately.\n\n"
            "Now the Vaishnava response asks a different but related question: does one short lifetime provide an equal moral arena for everyone? People are born into radically unequal conditions: geography, health, family stability, access to education, access to revelation, and psychological capacity. If judgment is final after one life, how is asymmetry fully resolved?\n\n"
            "Reincarnation in Vedic thought addresses this by extending the horizon of accountability. Karma means no act is lost, no intention disappears, and no growth is wasted. The soul continues through multiple births, carrying subtle impressions and consequences, until it reaches purification and liberation. So reincarnation is not moral leniency. It is expanded moral continuity.\n\n"
            "A modern analogy is education policy. Imagine evaluating all students by one single exam taken on one single day, regardless of background, disability, or opportunity. Many would call that unfair. A multi-stage evaluation across years, with cumulative record, often gives a fuller and fairer picture. Rebirth plus karma works similarly: cumulative moral history, not isolated snapshot.\n\n"
            "Bhagavad-gita supports this continuity: the soul changes bodies like garments (BG 2.22), and spiritual effort is never lost (BG 2.40). Even interrupted progress carries forward (BG 6.41-45). So rebirth is framed as a just and compassionate architecture for gradual awakening, not endless wandering without purpose.\n\n"
            "A Muslim friend may still answer: but God can judge perfectly even in one life. Vaishnava thought agrees God is perfectly just. The divergence is not about divine capability, but about revealed metaphysical design: one tradition teaches one earthly life then judgment; another teaches repeated embodied opportunities under law-like karmic causality.\n\n"
            "From the Vedic application side, reincarnation also explains experiential diversity without blaming God for arbitrary inequality. Different beginnings in life are linked to prior causation, and present practice can transform future trajectory. This gives both responsibility and hope.\n\n"
            "Srila Prabhupada repeatedly emphasized that understanding rebirth should increase seriousness, not complacency: do not delay spiritual life. Human birth is a rare chance to end the cycle through bhakti and return to Krishna.\n\n"
            "In conversation, a good response is: 'Single-life judgment gives urgency and moral clarity, and I respect that. Reincarnation, however, offers a broader framework of justice where moral development and consequence continue across lifetimes, so no sincere effort is wasted and no inequality is random. In Vedic understanding, this is not escape from accountability; it is accountability extended across a fuller timeline until liberation.'\n\n"
            "That keeps the dialogue respectful, fair, and philosophically grounded."
        ),
        "order": 242,
        "language": "en",
    },
    {
        "mainTopic": "Islamic Theological Challenges to Krishna Consciousness",
        "subTopic": "How does Krishna consciousness align with Islamic rejection of intermediaries between God and humans?",
        "article": (
            "This is a very important interfaith question. In Islamic theology, especially in its strict formulations, direct devotion to Allah is central and associating partners or dependency structures that replace direct reliance is strongly rejected. So when someone hears about gurus, deities, saints, and parampara in Krishna consciousness, they may worry: is this creating intermediaries that block direct relation with God?\n\n"
            "A Krishna-conscious response begins by clarifying purpose. In Vaishnava practice, guru and sadhu are not independent salvific powers. They are transparent guides, meant to connect the soul more directly to Bhagavan, not to themselves. Their authority is representative and service-based, not ontological competition with God.\n\n"
            "A modern analogy: a qualified doctor does not replace health itself; she helps you access it correctly. Or a language teacher does not replace truth; he helps you understand it accurately. In the same way, guru is a guide in method and realization, not a rival deity.\n\n"
            "From Vedic application, parampara is framed as epistemic humility: transcendental knowledge is received through disciplined transmission so it is not distorted by ego. Bhagavad-gita 4.2 speaks of this transmission chain. So disciplic guidance is about preserving fidelity to divine teaching, not inserting obstacles between soul and God.\n\n"
            "What about deity worship and saints? Vaishnava theology says all worship must culminate in Krishna, the Supreme source. Respect to saintly persons is gratitude for service, not deification of finite beings as independent absolutes. If that line is crossed, tradition itself calls it deviation.\n\n"
            "A Muslim interlocutor may still object: even representative structures can drift into excess. That concern is fair and historically real across traditions. Vaishnavism addresses this through scriptural criteria, ethical discipline, and the principle that genuine teacher directs all honor upward to Krishna, never hoards it personally.\n\n"
            "Another analogy from technology: secure systems often use trusted certificates and protocol chains. These do not replace the destination server; they verify authentic connection. Parampara functions similarly as trust architecture for spiritual transmission.\n\n"
            "Srila Prabhupada's emphasis was consistent: become servant of God, chant God's names, and avoid personality cultism divorced from siddhanta. He accepted discipleship as training in surrender to Krishna, not dependence on a human ego-center.\n\n"
            "In conversation, a balanced response is: 'I understand Islamic concern about intermediaries. In Krishna consciousness, guru and parampara are not partners to God but guides toward God. Their legitimacy lies in transparent representation, not independent divinity. The test is simple: does the structure increase direct surrender to the Supreme, or distract from it? Authentic bhakti insists on the former.'\n\n"
            "That framing preserves both respect for Tawheed concerns and fidelity to Vaishnava practice."
        ),
        "order": 243,
        "language": "en",
    },
    {
        "mainTopic": "Islamic Theological Challenges to Krishna Consciousness",
        "subTopic": "Isn't devotion to anyone but Allah considered shirk (polytheism)?",
        "article": (
            "From within Islamic theology, the concern is straightforward and serious: devotion directed to anyone besides Allah is shirk. So when Muslims see devotion to Krishna, they interpret it through that category. A meaningful response has to start by recognizing that this is not a casual accusation in Islam; it is a core theological boundary.\n\n"
            "The Krishna-conscious response is not to dismiss the concern, but to clarify identity claims. Vaishnavas are not saying: Krishna is someone other than the Supreme and we worship Him anyway. They are saying: Krishna is the Supreme source Himself. So from inside Vaishnava ontology, devotion to Krishna is devotion to the one ultimate God, not devotion to a second divine being.\n\n"
            "A modern analogy: if two traditions use different proper names for the ultimate, disagreement may concern identity-reference rather than number of ultimates. The real debate is not 'one versus many' but 'who is the one.'\n\n"
            "Bhagavad-gita presents Krishna with absolute claims of sourcehood and supremacy (BG 7.7, 10.8). Vaishnava theology interprets these claims literally: all energies and beings are dependent on Him. Therefore, bhakti to Krishna is monotheistic devotion within that revealed framework.\n\n"
            "A Muslim friend may reply: Islamic revelation identifies Allah in a way that excludes incarnational theology and image-mediated worship. That is a real doctrinal divergence, and honest dialogue should admit it. But divergence in revelation claims is not automatically logical polytheism. It is competing monotheistic theologies with different descriptions of the one Supreme.\n\n"
            "From Vedic application, bhakti also distinguishes clearly between Bhagavan and all finite beings. Worship of devas as independent absolutes is rejected in mature siddhanta. Respect may be offered, but ultimate surrender belongs only to the Supreme. That is structurally parallel to monotheistic exclusivity, though articulated differently.\n\n"
            "Think of constitutional law again: two legal systems can each claim one final court of appeal while defining that court differently. The conflict is over rightful final authority, not over whether final authority should exist.\n\n"
            "Srila Prabhupada often said that the practical test is this: are we living to please God, or to serve ego and material desire? He encouraged people from Abrahamic backgrounds to deepen God-centered life, then examine Krishna's identity through scripture and practice rather than through stereotype.\n\n"
            "In conversation, a precise response is: 'I understand why, within Islamic theology, devotion to other-than-Allah is shirk. Vaishnava theology, however, does not see Krishna as other-than-God; it identifies Him as the Supreme source. So this is not a defense of polytheism, but a difference over the identity and mode of revelation of the one God. The dialogue should focus there.'\n\n"
            "That keeps the exchange clear, respectful, and intellectually honest."
        ),
        "order": 244,
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
        ('debate', '0082_seed_debate_batch_81'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_code=unseed_data),
    ]
