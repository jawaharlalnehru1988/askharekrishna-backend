from django.db import migrations


def populate_topics_and_link_stories(apps, schema_editor):
    StoryMainTopic = apps.get_model('stories', 'StoryMainTopic')
    Story = apps.get_model('stories', 'Story')
    StoryTranslation = apps.get_model('stories', 'StoryTranslation')

    canonical_topics_config = {
        'Devotee Pastimes': {
            'order': 1,
            'description': 'This section contains number of devotees story',
            'image': 'stories/main-topic/shyamanda_prabhu.jpg',
            'name_translations': {
                'ta': 'பக்தர்களுடனான லீலைகள்',
                'hi': 'भक्तों की दिव्य लीलाएँ',
                'kn': 'ಭಕ್ತರ ಲೀಲೆಗಳು',
                'te': 'భక్తుల దివ్య లీలలు',
            },
            'keywords': ['devotee', 'பக்தர்', 'भक्त', 'ಭಕ್ತ', 'భక్తుల'],
        },
        'Krishna Pastimes': {
            'order': 2,
            'description': 'This section tells about pastimes of Lord krishna as said in Srimad Bhagavatam',
            'image': 'stories/main-topic/balakrishna.jpg',
            'name_translations': {
                'ta': 'கிருஷ்ண லீலைகள்',
                'hi': 'श्रीकृष्ण की दिव्य लीलाएँ',
                'kn': 'ಶ್ರೀಕೃಷ್ಣ ಲೀಲೆಗಳು',
                'te': 'శ్రీకృష్ణుని దివ్య లీలలు',
            },
            'keywords': ['krishna', 'கிருஷ்ண', 'श्रीकृष्ण', 'ಶ್ರೀಕೃಷ್ಣ', 'శ్రీకృష్ణ'],
        },
        'Preaching Stories': {
            'order': 3,
            'description': 'This section gives real time stories of devotees who preaches',
            'image': 'stories/main-topic/debate.jpg',
            'name_translations': {
                'ta': 'பிரச்சாரத்தின் போதான கதைகள்',
                'hi': 'प्रचार की प्रेरणादायक कहानियाँ',
                'kn': 'ಪ್ರಚಾರದ ಪ್ರೇರಣಾದಾಯಕ ಕಥೆಗಳು',
                'te': 'ప్రచార ప్రేరణాత్మక కథలు',
            },
            'keywords': ['preaching', 'பிரச்சார', 'प्रचार', 'ಪ್ರಚಾರ', 'ప్రచార'],
        },
        'Ekadasi Stories and Process': {
            'order': 4,
            'description': 'Only Ekadasi Stories',
            'image': 'stories/main-topic/rishi_and_lord_vishnu_1_CHzhnaQ.jpg',
            'name_translations': {
                'ta': 'ஏகாதசி மஹிமை வரலாற்று கதைகள்',
                'hi': 'एकादशी महिमा और इतिहास',
                'kn': 'ಏಕಾದಶಿ ಮಹಿಮೆ ಮತ್ತು ಇತಿಹಾಸ',
                'te': 'ఏకాదశి మహిమ మరియు చరిత్ర',
            },
            'keywords': ['ekadasi', 'ekadashi', 'ஏகாதசி', 'एकादशी', 'ಏಕಾದಶಿ', 'ఏకాదశి'],
        },
    }

    # Step 1: Ensure canonical topics exist with their config
    topic_instances = {}
    canonical_pks = set()
    for name, cfg in canonical_topics_config.items():
        topic, created = StoryMainTopic.objects.get_or_create(
            name=name,
            defaults={
                'order': cfg['order'],
                'description': cfg['description'],
                'name_translations': cfg['name_translations'],
                'is_active': True,
            }
        )
        if not created:
            topic.order = cfg['order']
            if not topic.description and cfg['description']:
                topic.description = cfg['description']
            if not topic.image and cfg['image']:
                topic.image = cfg['image']
            topic.name_translations = cfg['name_translations']
            topic.is_active = True
            topic.save()

        topic_instances[name] = topic
        canonical_pks.add(topic.pk)

    # Step 2: Link all stories to the proper canonical topic
    for story in Story.objects.all():
        topics_in_story = set(StoryTranslation.objects.filter(story=story).values_list('mainTopic', flat=True))
        matched_canonical_name = None

        for t_name, cfg in canonical_topics_config.items():
            for topic_str in topics_in_story:
                t_low = (topic_str or '').lower()
                if any(k in t_low or k in topic_str for k in cfg['keywords']):
                    matched_canonical_name = t_name
                    break
            if matched_canonical_name:
                break

        if not matched_canonical_name:
            matched_canonical_name = 'Devotee Pastimes'

        canonical_topic = topic_instances[matched_canonical_name]
        story.topic = canonical_topic
        story.save(update_fields=['topic'])

        # Step 3: Normalize translation mainTopic strings to match canonical / localized names
        for trans in StoryTranslation.objects.filter(story=story):
            lang = (trans.language_code or 'en').lower()
            if lang == 'en':
                canonical_str = matched_canonical_name
            else:
                canonical_str = canonical_topic.name_translations.get(lang, matched_canonical_name)
            if trans.mainTopic != canonical_str:
                trans.mainTopic = canonical_str
                trans.save(update_fields=['mainTopic'])

    # Step 4: Deactivate / clean up duplicate non-canonical topic records
    StoryMainTopic.objects.exclude(pk__in=canonical_pks).update(is_active=False)


def reverse_populate_topics(apps, schema_editor):
    Story = apps.get_model('stories', 'Story')
    Story.objects.update(topic=None)


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0014_story_topic_storymaintopic_name_translations'),
    ]

    operations = [
        migrations.RunPython(populate_topics_and_link_stories, reverse_populate_topics),
    ]
