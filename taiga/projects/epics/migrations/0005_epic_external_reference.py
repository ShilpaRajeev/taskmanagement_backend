# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epics', '0004_auto_20160928_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='epic',
            name='external_reference',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=None, null=True, size=None, verbose_name='external reference'),
        ),
    ]
