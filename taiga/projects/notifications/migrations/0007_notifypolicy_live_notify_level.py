# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import taiga.projects.notifications.choices


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0006_auto_20151103_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifypolicy',
            name='live_notify_level',
            field=models.SmallIntegerField(choices=[(taiga.projects.notifications.choices.NotifyLevel(1), 'Involved'), (taiga.projects.notifications.choices.NotifyLevel(2), 'All'), (taiga.projects.notifications.choices.NotifyLevel(3), 'None')], default=taiga.projects.notifications.choices.NotifyLevel(1)),
        ),
    ]
