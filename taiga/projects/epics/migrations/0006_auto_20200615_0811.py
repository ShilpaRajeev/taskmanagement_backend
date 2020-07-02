

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epics', '0005_epic_external_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epic',
            name='assigned_to',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='epics_assigned_to_me', to=settings.AUTH_USER_MODEL, verbose_name='assigned to'),
        ),
        migrations.AlterField(
            model_name='epic',
            name='client_requirement',
            field=models.BooleanField(blank=True, default=False, verbose_name='is client requirement'),
        ),
        migrations.AlterField(
            model_name='epic',
            name='is_blocked',
            field=models.BooleanField(blank=True, default=False, verbose_name='is blocked'),
        ),
        migrations.AlterField(
            model_name='epic',
            name='team_requirement',
            field=models.BooleanField(blank=True, default=False, verbose_name='is team requirement'),
        ),
    ]
