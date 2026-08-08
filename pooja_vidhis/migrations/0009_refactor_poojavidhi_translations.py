from django.db import migrations, models
import django.db.models.deletion

LANGUAGE_CHOICES = [
    ('en', 'English'),
    ('ta', 'Tamil'),
    ('kn', 'Kannada'),
    ('te', 'Telugu'),
    ('hi', 'Hindi'),
    ('ml', 'Malayalam'),
    ('bn', 'Bengali'),
]


def migrate_pooja_vidhi_data(apps, schema_editor):
    PoojaVidhiTranslation = apps.get_model('pooja_vidhis', 'PoojaVidhiTranslation')
    PoojaVidhiQuestion = apps.get_model('pooja_vidhis', 'PoojaVidhiQuestion')

    with schema_editor.connection.cursor() as cursor:
        cursor.execute(
            'SELECT id, "mainTopic", "subTopic", article, language_id, source_vidhi_id, "audioPath", "articleImage" '
            'FROM pooja_vidhis_poojavidhi ORDER BY id'
        )
        rows = cursor.fetchall()

    pv_dict = {}
    for r in rows:
        pv_dict[r[0]] = {
            'id': r[0],
            'mainTopic': r[1] or '',
            'subTopic': r[2] or '',
            'article': r[3] or '',
            'language_id': r[4] or 'en',
            'source_vidhi_id': r[5],
            'audioPath': r[6] or '',
            'articleImage': r[7] or '',
        }

    vidhi_to_root = {}
    for pv_id, pv in pv_dict.items():
        curr = pv
        visited = set()
        while curr['source_vidhi_id'] and curr['id'] not in visited:
            visited.add(curr['id'])
            parent = pv_dict.get(curr['source_vidhi_id'])
            if parent:
                curr = parent
            else:
                break
        vidhi_to_root[pv_id] = curr['id']

    # Clear self-referential foreign keys to allow deleting merged rows without FK violation
    with schema_editor.connection.cursor() as cursor:
        cursor.execute('UPDATE pooja_vidhis_poojavidhi SET source_vidhi_id = NULL')

    created_keys = set()
    to_delete_ids = set()

    for pv_id, pv in pv_dict.items():
        root_id = vidhi_to_root[pv_id]
        lang_code = pv['language_id']
        key = (root_id, lang_code)

        if key in created_keys:
            existing = PoojaVidhiTranslation.objects.filter(pooja_vidhi_id=root_id, language_code=lang_code).first()
            if existing and existing.subTopic != pv['subTopic']:
                root_id = pv_id
                vidhi_to_root[pv_id] = pv_id
                key = (pv_id, lang_code)

        PoojaVidhiTranslation.objects.get_or_create(
            pooja_vidhi_id=root_id,
            language_code=lang_code,
            defaults={
                'mainTopic': pv['mainTopic'],
                'subTopic': pv['subTopic'],
                'article': pv['article'],
            }
        )
        created_keys.add(key)

        root_pv_data = pv_dict[root_id]
        if pv['audioPath'] and not root_pv_data['audioPath']:
            with schema_editor.connection.cursor() as cursor:
                cursor.execute('UPDATE pooja_vidhis_poojavidhi SET "audioPath" = %s WHERE id = %s', [pv['audioPath'], root_id])
            root_pv_data['audioPath'] = pv['audioPath']

        if pv['articleImage'] and not root_pv_data['articleImage']:
            with schema_editor.connection.cursor() as cursor:
                cursor.execute('UPDATE pooja_vidhis_poojavidhi SET "articleImage" = %s WHERE id = %s', [pv['articleImage'], root_id])
            root_pv_data['articleImage'] = pv['articleImage']

        PoojaVidhiQuestion.objects.filter(pooja_vidhi_id=pv_id).update(
            pooja_vidhi_id=root_id,
            language_code=lang_code,
        )

        if pv_id != root_id:
            to_delete_ids.add(pv_id)

    if to_delete_ids:
        with schema_editor.connection.cursor() as cursor:
            cursor.execute('DELETE FROM pooja_vidhis_poojavidhi WHERE id IN %s', [tuple(to_delete_ids)])


class Migration(migrations.Migration):

    dependencies = [
        ('pooja_vidhis', '0008_poojavidhi_source_vidhi_and_unique_constraint'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoojaVidhiTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(choices=LANGUAGE_CHOICES, default='en', max_length=10)),
                ('mainTopic', models.CharField(max_length=255)),
                ('subTopic', models.CharField(max_length=255)),
                ('article', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pooja_vidhi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='pooja_vidhis.poojavidhi')),
            ],
            options={
                'verbose_name': 'Pooja Vidhi Translation',
                'verbose_name_plural': 'Pooja Vidhi Translations',
                'ordering': ['language_code'],
                'unique_together': {('pooja_vidhi', 'language_code')},
            },
        ),
        migrations.RemoveConstraint(
            model_name='poojavidhiquestion',
            name='uq_pooja_vidhi_question_order',
        ),
        migrations.AddField(
            model_name='poojavidhiquestion',
            name='language_code',
            field=models.CharField(choices=LANGUAGE_CHOICES, default='en', max_length=10),
        ),
        migrations.RunPython(
            migrate_pooja_vidhi_data,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
