import django.db.models.deletion
from django.db import migrations, models


def migrate_cooking_articles_forward(apps, schema_editor):
    CookingArticle = apps.get_model('cooking', 'CookingArticle')
    CookingMainTopic = apps.get_model('cooking', 'CookingMainTopic')
    CookingArticleTranslation = apps.get_model('cooking', 'CookingArticleTranslation')
    db_alias = schema_editor.connection.alias

    # 1. Create CookingMainTopic entries from all distinct mainTopics
    category_names = list(
        CookingArticle.objects.using(db_alias)
        .exclude(mainTopic__isnull=True)
        .exclude(mainTopic__exact='')
        .values_list('mainTopic', flat=True)
        .distinct()
        .order_by('mainTopic')
    )

    topic_cache = {}
    for idx, name in enumerate(category_names, start=1):
        topic, _ = CookingMainTopic.objects.using(db_alias).get_or_create(
            name=name,
            defaults={'order': idx, 'is_active': True},
        )
        topic_cache[name] = topic

    # 2. Get all English articles (which will remain as canonical parent articles)
    en_articles = list(CookingArticle.objects.using(db_alias).filter(language='en').order_by('order', 'id'))
    ta_articles = list(CookingArticle.objects.using(db_alias).filter(language='ta'))

    # Associate each EN article with its topic
    for en in en_articles:
        if en.mainTopic in topic_cache:
            en.topic = topic_cache[en.mainTopic]
            en.save(update_fields=['topic'])

        # Create English translation record
        CookingArticleTranslation.objects.using(db_alias).get_or_create(
            article_parent=en,
            language_code='en',
            defaults={
                'mainTopic': en.mainTopic,
                'subTopic': en.subTopic,
                'article': en.article,
                'audioPath': en.audioPath,
            },
        )

    # 3. Associate and create Tamil translation records under the matching English parent
    for ta in ta_articles:
        base_slug = ta.slug[:-3] if ta.slug.endswith('-ta') else ta.slug
        parent = next((e for e in en_articles if e.slug == base_slug), None)
        if not parent:
            parent = next((e for e in en_articles if e.order == ta.order and e.mainTopic == ta.mainTopic), None)

        if parent:
            CookingArticleTranslation.objects.using(db_alias).get_or_create(
                article_parent=parent,
                language_code='ta',
                defaults={
                    'mainTopic': ta.mainTopic,
                    'subTopic': ta.subTopic,
                    'article': ta.article,
                    'audioPath': ta.audioPath,
                },
            )

    # 4. Delete the standalone non-English rows from CookingArticle so only canonical parents remain
    CookingArticle.objects.using(db_alias).exclude(language='en').delete()


def migrate_cooking_articles_backward(apps, schema_editor):
    # Backward no-op or pass
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0002_cookingarticle_audiopath'),
    ]

    operations = [
        # Step 1: Create CookingMainTopic model
        migrations.CreateModel(
            name='CookingMainTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('name_translations', models.JSONField(blank=True, default=dict, help_text="Localized names: {'ta': '...', 'hi': '...', 'kn': '...', 'te': '...', ...}")),
                ('description', models.CharField(blank=True, default='', max_length=500)),
                ('description_translations', models.JSONField(blank=True, default=dict, help_text="Localized descriptions: {'ta': '...', 'hi': '...', 'kn': '...', 'te': '...', ...}")),
                ('image', models.ImageField(blank=True, max_length=500, null=True, upload_to='cooking/category/')),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cooking Main Topic',
                'verbose_name_plural': 'Cooking Main Topics',
                'ordering': ['order', 'name'],
            },
        ),

        # Step 2: Add topic FK and imagePath to CookingArticle
        migrations.AddField(
            model_name='cookingarticle',
            name='topic',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='articles',
                to='cooking.cookingmaintopic',
            ),
        ),
        migrations.AddField(
            model_name='cookingarticle',
            name='imagePath',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='cooking/images/'),
        ),

        # Step 3: Create CookingArticleTranslation model
        migrations.CreateModel(
            name='CookingArticleTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(
                    choices=[
                        ('en', 'English'), ('ta', 'Tamil'), ('kn', 'Kannada'),
                        ('te', 'Telugu'), ('hi', 'Hindi'), ('ml', 'Malayalam'),
                        ('bn', 'Bengali'), ('mr', 'Marathi'), ('gu', 'Gujarati'),
                        ('or', 'Odia'), ('pa', 'Punjabi'), ('sa', 'Sanskrit')
                    ],
                    default='en',
                    max_length=10,
                )),
                ('mainTopic', models.CharField(max_length=255)),
                ('subTopic', models.CharField(max_length=255)),
                ('article', models.TextField()),
                ('audioPath', models.FileField(blank=True, max_length=500, null=True, upload_to='cooking/audio/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('article_parent', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='translations',
                    to='cooking.cookingarticle',
                )),
            ],
            options={
                'verbose_name': 'Cooking Article Translation',
                'verbose_name_plural': 'Cooking Article Translations',
                'ordering': ['article_parent_id', 'language_code'],
            },
        ),
        migrations.AddConstraint(
            model_name='cookingarticletranslation',
            constraint=models.UniqueConstraint(
                fields=('article_parent', 'language_code'),
                name='uq_cooking_translation_language',
            ),
        ),

        # Step 4: Run Python data migration before removing legacy columns
        migrations.RunPython(
            migrate_cooking_articles_forward,
            migrate_cooking_articles_backward,
        ),

        # Step 5: Remove legacy columns from CookingArticle
        migrations.RemoveField(
            model_name='cookingarticle',
            name='mainTopic',
        ),
        migrations.RemoveField(
            model_name='cookingarticle',
            name='subTopic',
        ),
        migrations.RemoveField(
            model_name='cookingarticle',
            name='article',
        ),
        migrations.RemoveField(
            model_name='cookingarticle',
            name='language',
        ),
        migrations.RemoveField(
            model_name='cookingarticle',
            name='audioPath',
        ),

        # Step 6: Alter options on CookingArticle
        migrations.AlterModelOptions(
            name='cookingarticle',
            options={'ordering': ['order', 'id'], 'verbose_name': 'Cooking Article', 'verbose_name_plural': 'Cooking Articles'},
        ),
        migrations.AlterField(
            model_name='cookingarticle',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=280, unique=True),
        ),
    ]
