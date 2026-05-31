from django.db import migrations, models
import django.db.models.deletion
from django.db.models import Q


class Migration(migrations.Migration):

    dependencies = [
        ('pooja_vidhis', '0007_poojavidhiquestion_poojavidhiquestionoption_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='poojavidhi',
            name='source_vidhi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='translations', to='pooja_vidhis.poojavidhi'),
        ),
        migrations.AddConstraint(
            model_name='poojavidhi',
            constraint=models.UniqueConstraint(condition=Q(('source_vidhi__isnull', False)), fields=('source_vidhi', 'language'), name='uq_pooja_vidhi_source_language'),
        ),
    ]
