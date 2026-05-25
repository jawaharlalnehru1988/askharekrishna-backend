from django.db import migrations, models
import django.db.models.deletion


def copy_main_topic_to_fk(apps, schema_editor):
    Story = apps.get_model("stories", "Story")
    StoryMainTopic = apps.get_model("stories", "StoryMainTopic")

    for story in Story.objects.all().only("id", "mainTopic"):
        raw_main_topic = getattr(story, "mainTopic", None)
        if not raw_main_topic:
            continue

        topic_name = str(raw_main_topic).strip()
        if not topic_name:
            continue

        topic, _ = StoryMainTopic.objects.get_or_create(name=topic_name)
        story.mainTopic_ref = topic
        story.save(update_fields=["mainTopic_ref"])


class Migration(migrations.Migration):

    dependencies = [
        ("stories", "0005_alter_story_language_alter_story_storycategory_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="StoryMainTopic",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(db_index=True, max_length=255, unique=True)),
                ("description", models.CharField(blank=True, default="", max_length=200)),
                ("image", models.ImageField(blank=True, max_length=500, null=True, upload_to="stories/main-topic/")),
            ],
            options={
                "verbose_name": "Story Main Topic",
                "verbose_name_plural": "Story Main Topics",
                "ordering": ["name"],
            },
        ),
        migrations.AddField(
            model_name="story",
            name="mainTopic_ref",
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="stories", to="stories.storymaintopic"),
        ),
        migrations.RunPython(copy_main_topic_to_fk, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name="story",
            name="mainTopic",
        ),
        migrations.RenameField(
            model_name="story",
            old_name="mainTopic_ref",
            new_name="mainTopic",
        ),
        migrations.AlterModelOptions(
            name="story",
            options={"ordering": ["order", "mainTopic__name", "subTopic"], "verbose_name": "Story", "verbose_name_plural": "Stories"},
        ),
    ]
