from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carnatic_questions', '0003_carnaticsyllabus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carnaticsyllabus',
            name='lesson',
            field=models.CharField(max_length=3000),
        ),
    ]
