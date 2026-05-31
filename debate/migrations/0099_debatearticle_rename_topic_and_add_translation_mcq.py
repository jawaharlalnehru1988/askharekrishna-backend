from django.db import migrations, models
import django.db.models.deletion
from django.db.models import Q


class Migration(migrations.Migration):

    dependencies = [
        ('debate', '0098_alter_debatearticle_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='debatearticle',
            old_name='topic',
            new_name='mainTopic',
        ),
        migrations.AddField(
            model_name='debatearticle',
            name='source_article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='translations', to='debate.debatearticle'),
        ),
        migrations.AlterField(
            model_name='debatearticle',
            name='slug',
            field=models.SlugField(blank=True, max_length=280, unique=True, allow_unicode=True),
        ),
        migrations.AlterModelOptions(
            name='debatearticle',
            options={'ordering': ['order', 'mainTopic', 'subTopic'], 'verbose_name': 'Debate Article', 'verbose_name_plural': 'Debate Articles'},
        ),
        migrations.AddConstraint(
            model_name='debatearticle',
            constraint=models.UniqueConstraint(condition=Q(source_article__isnull=False), fields=('source_article', 'language'), name='uq_debate_source_language'),
        ),
        migrations.CreateModel(
            name='DebateQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('order', models.PositiveSmallIntegerField(default=1)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('debate_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='debate.debatearticle')),
            ],
            options={
                'verbose_name': 'Debate MCQ Question',
                'verbose_name_plural': 'Debate MCQ Questions',
                'ordering': ['debate_article_id', 'order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='DebateQuestionOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_text', models.CharField(max_length=500)),
                ('order', models.PositiveSmallIntegerField(default=1)),
                ('is_correct', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='debate.debatequestion')),
            ],
            options={
                'verbose_name': 'Debate MCQ Option',
                'verbose_name_plural': 'Debate MCQ Options',
                'ordering': ['question_id', 'order', 'id'],
            },
        ),
        migrations.AddConstraint(
            model_name='debatequestion',
            constraint=models.UniqueConstraint(fields=('debate_article', 'order'), name='uq_debate_question_order'),
        ),
        migrations.AddConstraint(
            model_name='debatequestionoption',
            constraint=models.UniqueConstraint(fields=('question', 'order'), name='uq_debate_option_order'),
        ),
    ]
