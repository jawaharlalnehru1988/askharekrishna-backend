from django.db import migrations, models


def backfill_kacheri_titles(apps, schema_editor):
    CarnaticKacheri = apps.get_model('carnatic_questions', 'CarnaticKacheri')

    for kacheri in CarnaticKacheri.objects.all():
        singer = (kacheri.singer or '').strip()
        ragam = (kacheri.ragam or '').strip()

        if singer and ragam:
            title = f"{singer} - {ragam}"
        else:
            title = singer or ragam or 'Untitled Kacheri'

        kacheri.title = title
        kacheri.save(update_fields=['title'])


class Migration(migrations.Migration):

    dependencies = [
        ('carnatic_questions', '0012_carnatickacheri'),
    ]

    operations = [
        migrations.AddField(
            model_name='carnatickacheri',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.RunPython(backfill_kacheri_titles, migrations.RunPython.noop),
        migrations.AlterModelOptions(
            name='carnatickacheri',
            options={
                'ordering': ['title', 'singer', 'ragam', '-created_at'],
                'verbose_name': 'Carnatic Kacheri',
                'verbose_name_plural': 'Carnatic Kacheri',
            },
        ),
    ]