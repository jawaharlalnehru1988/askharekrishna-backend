from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stories", "0002_story_audiopath"),
    ]

    operations = [
        migrations.AlterField(
            model_name="story",
            name="slug",
            field=models.SlugField(allow_unicode=True, blank=True, max_length=280, unique=True),
        ),
    ]
