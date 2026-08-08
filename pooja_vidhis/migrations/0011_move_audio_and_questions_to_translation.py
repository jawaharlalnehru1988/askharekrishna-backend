from django.db import migrations, models
import django.db.models.deletion


def migrate_audio_and_questions(apps, schema_editor):
    PoojaVidhiTranslation = apps.get_model('pooja_vidhis', 'PoojaVidhiTranslation')

    with schema_editor.connection.cursor() as cursor:
        cursor.execute('SELECT id, "audioPath" FROM pooja_vidhis_poojavidhi WHERE "audioPath" IS NOT NULL AND "audioPath" != \'\'')
        rows = cursor.fetchall()

    for pv_id, audio_path in rows:
        trans = PoojaVidhiTranslation.objects.filter(pooja_vidhi_id=pv_id, language_code='en').first() or PoojaVidhiTranslation.objects.filter(pooja_vidhi_id=pv_id).first()
        if trans:
            trans.audioPath = audio_path
            trans.save()

    with schema_editor.connection.cursor() as cursor:
        cursor.execute('SELECT id, pooja_vidhi_id, language_code FROM pooja_vidhis_poojavidhiquestion')
        q_rows = cursor.fetchall()

        for q_id, pv_id, lang_code in q_rows:
            trans = PoojaVidhiTranslation.objects.filter(pooja_vidhi_id=pv_id, language_code=lang_code).first()
            if not trans:
                trans = PoojaVidhiTranslation.objects.filter(pooja_vidhi_id=pv_id).first()
            if trans:
                cursor.execute('UPDATE pooja_vidhis_poojavidhiquestion SET translation_id = %s WHERE id = %s', [trans.id, q_id])


class Migration(migrations.Migration):

    dependencies = [
        ('pooja_vidhis', '0010_remove_poojavidhi_legacy_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='poojavidhitranslation',
            name='audioPath',
            field=models.FileField(blank=True, max_length=500, null=True, upload_to='pooja_vidhis/audio/'),
        ),
        migrations.AddField(
            model_name='poojavidhiquestion',
            name='translation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='pooja_vidhis.poojavidhitranslation'),
        ),
        migrations.RunPython(
            migrate_audio_and_questions,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunSQL('ALTER TABLE pooja_vidhis_poojavidhiquestion DROP CONSTRAINT IF EXISTS uq_pooja_vidhi_question_lang_order;'),
                migrations.RunSQL('ALTER TABLE pooja_vidhis_poojavidhiquestion DROP COLUMN IF EXISTS pooja_vidhi_id;'),
                migrations.RunSQL('ALTER TABLE pooja_vidhis_poojavidhiquestion DROP COLUMN IF EXISTS language_code;'),
                migrations.RunSQL('ALTER TABLE pooja_vidhis_poojavidhi DROP COLUMN IF EXISTS "audioPath";'),
                migrations.RunSQL('ALTER TABLE pooja_vidhis_poojavidhiquestion ALTER COLUMN translation_id SET NOT NULL;'),
                migrations.RunSQL('ALTER TABLE pooja_vidhis_poojavidhiquestion ADD CONSTRAINT uq_pooja_vidhi_translation_question_order UNIQUE (translation_id, "order");'),
            ],
            state_operations=[
                migrations.RemoveConstraint(
                    model_name='poojavidhiquestion',
                    name='uq_pooja_vidhi_question_lang_order',
                ),
                migrations.RemoveField(
                    model_name='poojavidhiquestion',
                    name='pooja_vidhi',
                ),
                migrations.RemoveField(
                    model_name='poojavidhiquestion',
                    name='language_code',
                ),
                migrations.RemoveField(
                    model_name='poojavidhi',
                    name='audioPath',
                ),
                migrations.AlterField(
                    model_name='poojavidhiquestion',
                    name='translation',
                    field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='pooja_vidhis.poojavidhitranslation'),
                ),
                migrations.AddConstraint(
                    model_name='poojavidhiquestion',
                    constraint=models.UniqueConstraint(fields=('translation', 'order'), name='uq_pooja_vidhi_translation_question_order'),
                ),
            ]
        )
    ]
