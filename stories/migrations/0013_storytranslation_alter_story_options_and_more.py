import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0012_story_source_story_and_unique_source_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(choices=[('en', 'English'), ('ta', 'Tamil'), ('kn', 'Kannada'), ('te', 'Telugu'), ('hi', 'Hindi'), ('ml', 'Malayalam'), ('bn', 'Bengali'), ('mr', 'Marathi'), ('gu', 'Gujarati'), ('or', 'Odia'), ('pa', 'Punjabi'), ('sa', 'Sanskrit')], default='en', max_length=10)),
                ('mainTopic', models.CharField(max_length=255)),
                ('subTopic', models.CharField(max_length=255)),
                ('article', models.TextField()),
                ('audioPath', models.FileField(blank=True, max_length=500, null=True, upload_to='stories/audio/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='stories.story')),
            ],
            options={
                'verbose_name': 'Story Translation',
                'verbose_name_plural': 'Story Translations',
                'ordering': ['story_id', 'language_code'],
            },
        ),
        migrations.AlterModelOptions(
            name='story',
            options={'ordering': ['order', 'id'], 'verbose_name': 'Story', 'verbose_name_plural': 'Stories'},
        ),
        migrations.AlterModelOptions(
            name='storymaintopic',
            options={'ordering': ['order', 'name'], 'verbose_name': 'Story Main Topic', 'verbose_name_plural': 'Story Main Topics'},
        ),
        migrations.AlterModelOptions(
            name='storyquestion',
            options={'ordering': ['translation_id', 'order', 'id'], 'verbose_name': 'Story MCQ Question', 'verbose_name_plural': 'Story MCQ Questions'},
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveConstraint(
                    model_name='story',
                    name='uq_story_source_language',
                ),
                migrations.RemoveConstraint(
                    model_name='storyquestion',
                    name='uq_story_question_order',
                ),
                migrations.RemoveConstraint(
                    model_name='storyquestionoption',
                    name='uq_story_option_order',
                ),
                migrations.RemoveIndex(
                    model_name='story',
                    name='story_topic_lang_ord_idx',
                ),
                migrations.RemoveIndex(
                    model_name='story',
                    name='story_topic_id_idx',
                ),
                migrations.AddField(
                    model_name='storymaintopic',
                    name='created_at',
                    field=models.DateTimeField(default=django.utils.timezone.now),
                ),
                migrations.AddField(
                    model_name='storymaintopic',
                    name='is_active',
                    field=models.BooleanField(default=True),
                ),
                migrations.AddField(
                    model_name='storymaintopic',
                    name='order',
                    field=models.PositiveIntegerField(default=0),
                ),
                migrations.AddField(
                    model_name='storymaintopic',
                    name='updated_at',
                    field=models.DateTimeField(auto_now=True),
                ),
                migrations.AddField(
                    model_name='storyquestion',
                    name='translation',
                    field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='stories.storytranslation'),
                ),
                migrations.RemoveField(
                    model_name='storyquestion',
                    name='story',
                ),
                migrations.RemoveField(
                    model_name='story',
                    name='article',
                ),
                migrations.RemoveField(
                    model_name='story',
                    name='audioPath',
                ),
                migrations.RemoveField(
                    model_name='story',
                    name='language',
                ),
                migrations.RemoveField(
                    model_name='story',
                    name='mainTopic',
                ),
                migrations.RemoveField(
                    model_name='story',
                    name='source_story',
                ),
                migrations.RemoveField(
                    model_name='story',
                    name='subTopic',
                ),
            ],
            database_operations=[
                migrations.RunSQL(
                    sql="""
                    ALTER TABLE stories_storymaintopic ADD COLUMN IF NOT EXISTS created_at timestamp with time zone DEFAULT NOW();
                    ALTER TABLE stories_storymaintopic ADD COLUMN IF NOT EXISTS updated_at timestamp with time zone DEFAULT NOW();
                    ALTER TABLE stories_storymaintopic ADD COLUMN IF NOT EXISTS is_active boolean DEFAULT TRUE;
                    ALTER TABLE stories_storymaintopic ADD COLUMN IF NOT EXISTS "order" integer DEFAULT 0;

                    ALTER TABLE stories_storyquestion ADD COLUMN IF NOT EXISTS translation_id bigint REFERENCES stories_storytranslation(id) ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;
                    
                    -- Drop old constraints/indexes if they exist
                    ALTER TABLE stories_story DROP CONSTRAINT IF EXISTS uq_story_source_language;
                    ALTER TABLE stories_storyquestion DROP CONSTRAINT IF EXISTS uq_story_question_order;
                    ALTER TABLE stories_storyquestionoption DROP CONSTRAINT IF EXISTS uq_story_option_order;
                    DROP INDEX IF EXISTS story_topic_lang_ord_idx;
                    DROP INDEX IF EXISTS story_topic_id_idx;

                    -- Drop old columns on stories_story
                    ALTER TABLE stories_story DROP COLUMN IF EXISTS article CASCADE;
                    ALTER TABLE stories_story DROP COLUMN IF EXISTS "audioPath" CASCADE;
                    ALTER TABLE stories_story DROP COLUMN IF EXISTS language_id CASCADE;
                    ALTER TABLE stories_story DROP COLUMN IF EXISTS "mainTopic_id" CASCADE;
                    ALTER TABLE stories_story DROP COLUMN IF EXISTS source_story_id CASCADE;
                    ALTER TABLE stories_story DROP COLUMN IF EXISTS translated_from_id CASCADE;
                    ALTER TABLE stories_story DROP COLUMN IF EXISTS "subTopic" CASCADE;

                    -- Drop old story_id column from stories_storyquestion
                    ALTER TABLE stories_storyquestion DROP COLUMN IF EXISTS story_id CASCADE;
                    """,
                    reverse_sql=""
                )
            ]
        ),
        migrations.AddConstraint(
            model_name='storytranslation',
            constraint=models.UniqueConstraint(fields=('story', 'language_code'), name='uq_story_translation_language'),
        ),
        migrations.AddConstraint(
            model_name='storyquestion',
            constraint=models.UniqueConstraint(fields=('translation', 'order'), name='uq_story_translation_question_order'),
        ),
        migrations.AddConstraint(
            model_name='storyquestionoption',
            constraint=models.UniqueConstraint(fields=('question', 'order'), name='uq_story_translation_option_order'),
        ),
    ]
