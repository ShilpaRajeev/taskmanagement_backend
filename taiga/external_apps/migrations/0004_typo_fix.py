# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('external_apps', '0003_auto_20170607_2320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicationtoken',
            options={'ordering': ['application', 'user'], 'verbose_name': 'application token', 'verbose_name_plural': 'application tokens'},
        ),
    ]
