# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0006_remove_issue_watchers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='external_reference',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=False, null=False), blank=True, default=None, null=True, size=None, verbose_name='external reference'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, null=True, size=None, verbose_name='tags'),
        ),
    ]
