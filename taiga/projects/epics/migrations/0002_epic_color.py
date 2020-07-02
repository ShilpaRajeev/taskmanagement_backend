# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import taiga.base.utils.colors


class Migration(migrations.Migration):

    dependencies = [
        ('epics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='epic',
            name='color',
            field=models.CharField(blank=True, default=taiga.base.utils.colors.generate_random_predefined_hex_color, max_length=32, verbose_name='color'),
        ),
    ]
