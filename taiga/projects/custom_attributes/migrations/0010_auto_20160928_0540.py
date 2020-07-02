# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import taiga.base.utils.time


class Migration(migrations.Migration):

    dependencies = [
        ('custom_attributes', '0009_auto_20160728_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epiccustomattribute',
            name='order',
            field=models.BigIntegerField(default=taiga.base.utils.time.timestamp_ms, verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='issuecustomattribute',
            name='order',
            field=models.BigIntegerField(default=taiga.base.utils.time.timestamp_ms, verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='taskcustomattribute',
            name='order',
            field=models.BigIntegerField(default=taiga.base.utils.time.timestamp_ms, verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='userstorycustomattribute',
            name='order',
            field=models.BigIntegerField(default=taiga.base.utils.time.timestamp_ms, verbose_name='order'),
        ),
    ]
