

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0008_add_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='is_blocked',
            field=models.BooleanField(blank=True, default=False, verbose_name='is blocked'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='severity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issues', to='projects.Severity', verbose_name='severity'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issues', to='projects.IssueStatus', verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issues', to='projects.IssueType', verbose_name='type'),
        ),
    ]
