# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_remove_wikipage_watchers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wikilink',
            options={'ordering': ['project', 'order', 'id'], 'verbose_name': 'wiki link', 'verbose_name_plural': 'wiki links'},
        ),
        migrations.AlterField(
            model_name='wikilink',
            name='order',
            field=models.PositiveSmallIntegerField(default='10000', verbose_name='order'),
        ),
    ]
