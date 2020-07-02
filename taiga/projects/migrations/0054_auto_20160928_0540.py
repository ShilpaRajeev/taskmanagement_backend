# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import taiga.base.utils.time


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0053_auto_20160927_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='user_order',
            field=models.BigIntegerField(default=taiga.base.utils.time.timestamp_ms, verbose_name='user order'),
        ),
        migrations.AlterField(
            model_name='projecttemplate',
            name='order',
            field=models.BigIntegerField(default=taiga.base.utils.time.timestamp_ms, verbose_name='user order'),
        ),
    ]
