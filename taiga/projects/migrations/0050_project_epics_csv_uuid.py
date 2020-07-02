# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0049_auto_20160629_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='epics_csv_uuid',
            field=models.CharField(blank=True, db_index=True, default=None, editable=False, max_length=32, null=True),
        ),
    ]
