# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import taiga.base.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0008_auto_20150508_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyentry',
            name='comment_versions',
            field=taiga.base.db.models.fields.JSONField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='historyentry',
            name='edit_comment_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]