# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import taiga.base.utils.time


class Migration(migrations.Migration):

    dependencies = [
        ('epics', '0003_auto_20160901_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epic',
            name='epics_order',
            field=models.BigIntegerField(default=taiga.base.utils.time.timestamp_ms, verbose_name='epics order'),
        ),
        migrations.AlterField(
            model_name='relateduserstory',
            name='order',
            field=models.BigIntegerField(default=taiga.base.utils.time.timestamp_ms, verbose_name='order'),
        ),
    ]
