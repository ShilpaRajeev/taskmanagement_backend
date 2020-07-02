# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0060_auto_20180614_1338'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='issuestatus',
            unique_together=set([('project', 'name'), ('project', 'slug')]),
        ),
    ]
