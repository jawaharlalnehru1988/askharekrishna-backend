from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0007_storycategory_alter_story_storycategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='imagePath',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='stories/images/'),
        ),
    ]
