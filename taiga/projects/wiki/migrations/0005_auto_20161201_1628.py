# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_auto_20160928_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikipage',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=500, verbose_name='slug'),
        ),
    ]
