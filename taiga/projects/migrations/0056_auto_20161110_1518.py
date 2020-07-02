# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0055_json_to_jsonb'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_contact_activated',
            field=models.BooleanField(default=True, verbose_name='active contact'),
        ),
        migrations.AddField(
            model_name='projecttemplate',
            name='is_contact_activated',
            field=models.BooleanField(default=True, verbose_name='active contact'),
        ),
    ]
