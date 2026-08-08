from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pooja_vidhis', '0009_refactor_poojavidhi_translations'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunSQL('ALTER TABLE pooja_vidhis_poojavidhi DROP CONSTRAINT IF EXISTS uq_pooja_vidhi_source_language;'),
                migrations.RunSQL('ALTER TABLE pooja_vidhis_poojavidhi DROP COLUMN IF EXISTS "mainTopic";'),
                migrations.RunSQL('ALTER TABLE pooja_vidhis_poojavidhi DROP COLUMN IF EXISTS "subTopic";'),
                migrations.RunSQL('ALTER TABLE pooja_vidhis_poojavidhi DROP COLUMN IF EXISTS "article";'),
                migrations.RunSQL('ALTER TABLE pooja_vidhis_poojavidhi DROP COLUMN IF EXISTS "language_id";'),
                migrations.RunSQL('ALTER TABLE pooja_vidhis_poojavidhi DROP COLUMN IF EXISTS "source_vidhi_id";'),
                migrations.RunSQL('ALTER TABLE pooja_vidhis_poojavidhi DROP COLUMN IF EXISTS "translated_from_id";'),
                migrations.RunSQL('ALTER TABLE pooja_vidhis_poojavidhiquestion DROP CONSTRAINT IF EXISTS uq_pooja_vidhi_question_order;'),
                migrations.RunSQL('ALTER TABLE pooja_vidhis_poojavidhiquestion ADD CONSTRAINT uq_pooja_vidhi_question_lang_order UNIQUE (pooja_vidhi_id, language_code, "order");'),
            ],
            state_operations=[
                migrations.RemoveConstraint(
                    model_name='poojavidhi',
                    name='uq_pooja_vidhi_source_language',
                ),
                migrations.RemoveField(
                    model_name='poojavidhi',
                    name='article',
                ),
                migrations.RemoveField(
                    model_name='poojavidhi',
                    name='language',
                ),
                migrations.RemoveField(
                    model_name='poojavidhi',
                    name='mainTopic',
                ),
                migrations.RemoveField(
                    model_name='poojavidhi',
                    name='source_vidhi',
                ),
                migrations.RemoveField(
                    model_name='poojavidhi',
                    name='subTopic',
                ),
                migrations.AddConstraint(
                    model_name='poojavidhiquestion',
                    constraint=models.UniqueConstraint(fields=('pooja_vidhi', 'language_code', 'order'), name='uq_pooja_vidhi_question_lang_order'),
                ),
            ]
        )
    ]
