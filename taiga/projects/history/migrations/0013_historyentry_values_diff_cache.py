# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations
import taiga.base.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0012_auto_20160629_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyentry',
            name='values_diff_cache',
            field=taiga.base.db.models.fields.JSONField(blank=True, default=None, null=True),
        ),
    ]
