# Generated migration to remove DebateMainTopic and add topic field

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debate', '0096_debatemaintopic_debatecategory'),
    ]

    operations = [
        # Add topic field to DebateArticle
        migrations.AddField(
            model_name='debatearticle',
            name='topic',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        # Data migration: copy mainTopic name to topic field
        migrations.RunPython(
            code=lambda apps, schema_editor: copy_maintopic_to_topic(apps, schema_editor),
            reverse_code=lambda apps, schema_editor: None,
        ),
        # Remove mainTopic FK
        migrations.RemoveField(
            model_name='debatearticle',
            name='mainTopic',
        ),
        # Delete DebateMainTopic model
        migrations.DeleteModel(
            name='DebateMainTopic',
        ),
    ]


def copy_maintopic_to_topic(apps, schema_editor):
    """Copy mainTopic.name to topic field for all articles"""
    DebateArticle = apps.get_model('debate', 'DebateArticle')
    
    for article in DebateArticle.objects.exclude(mainTopic__isnull=True):
        article.topic = article.mainTopic.name
        article.save(update_fields=['topic'])
