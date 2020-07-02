# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taiga.base.utils.time


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_auto_20160615_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikilink',
            name='order',
            field=models.BigIntegerField(default=taiga.base.utils.time.timestamp_ms, verbose_name='order'),
        ),
    ]
