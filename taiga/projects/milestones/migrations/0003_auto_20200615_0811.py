

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milestones', '0002_remove_milestone_watchers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='closed',
            field=models.BooleanField(blank=True, default=False, verbose_name='is closed'),
        ),
    ]
