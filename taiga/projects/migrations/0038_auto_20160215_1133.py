# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0037_auto_20160208_1751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='is_owner',
            new_name='is_admin',
        ),
    ]
