# Generated manually for CarnaticSyllabus model
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carnatic_questions', '0002_alter_carnaticquestion_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarnaticSyllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(max_length=255)),
                ('topic', models.CharField(max_length=255)),
                ('lesson', models.CharField(max_length=255)),
                ('audioPath', models.FileField(blank=True, max_length=500, null=True, upload_to='carnatic_syllabus/audio/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Carnatic Syllabus',
                'verbose_name_plural': 'Carnatic Syllabus',
                'ordering': ['division', 'topic', 'lesson'],
            },
        ),
    ]
