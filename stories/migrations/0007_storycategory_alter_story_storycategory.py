import django.db.models.deletion
from django.db import migrations, models


def copy_story_category_to_fk(apps, schema_editor):
    Story = apps.get_model("stories", "Story")
    StoryCategory = apps.get_model("stories", "StoryCategory")

    for story in Story.objects.all().only("id", "storyCategory"):
        raw_category = getattr(story, "storyCategory", None)
        if not raw_category:
            continue

        category_name = str(raw_category).strip()
        if not category_name:
            continue

        category, _ = StoryCategory.objects.get_or_create(name=category_name)
        story.storyCategory_ref = category
        story.save(update_fields=["storyCategory_ref"])


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_storymaintopic_refactor_main_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('description', models.CharField(blank=True, default='', max_length=200)),
                ('image', models.ImageField(blank=True, max_length=500, null=True, upload_to='stories/category/')),
            ],
            options={
                'verbose_name': 'Story Category',
                'verbose_name_plural': 'Story Categories',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='story',
            name='storyCategory_ref',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stories', to='stories.storycategory'),
        ),
        migrations.RunPython(copy_story_category_to_fk, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='story',
            name='storyCategory',
        ),
        migrations.RenameField(
            model_name='story',
            old_name='storyCategory_ref',
            new_name='storyCategory',
        ),
    ]
