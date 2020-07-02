# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('external_apps', '0002_remove_application_key'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ['name', 'id'], 'verbose_name': 'application', 'verbose_name_plural': 'applications'},
        ),
        migrations.AlterModelOptions(
            name='applicationtoken',
            options={'ordering': ['application', 'user'], 'verbose_name': 'application token', 'verbose_name_plural': 'application tolens'},
        ),
    ]
