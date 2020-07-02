# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0061_auto_20180918_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='videoconferences',
            field=models.CharField(blank=True, choices=[('whereby-com', 'Whereby.com'), ('jitsi', 'Jitsi'), ('custom', 'Custom'), ('talky', 'Talky')], max_length=250, null=True, verbose_name='videoconference system'),
        ),
        migrations.AlterField(
            model_name='projecttemplate',
            name='videoconferences',
            field=models.CharField(blank=True, choices=[('whereby-com', 'Whereby.com'), ('jitsi', 'Jitsi'), ('custom', 'Custom'), ('talky', 'Talky')], max_length=250, null=True, verbose_name='videoconference system'),
        ),
    ]
