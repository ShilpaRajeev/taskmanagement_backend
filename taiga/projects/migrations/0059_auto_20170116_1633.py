# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0058_auto_20161215_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='looking_for_people_note',
            field=models.TextField(blank=True, default='', verbose_name='looking for people note'),
        ),
        migrations.AlterField(
            model_name='projecttemplate',
            name='looking_for_people_note',
            field=models.TextField(blank=True, default='', verbose_name='looking for people note'),
        ),
    ]
