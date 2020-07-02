# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epics', '0002_epic_color'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='relateduserstory',
            unique_together=set([('user_story', 'epic')]),
        ),
    ]
