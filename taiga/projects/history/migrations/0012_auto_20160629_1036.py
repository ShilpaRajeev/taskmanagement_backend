# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0011_auto_20160629_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyentry',
            name='project',
            field=models.ForeignKey(on_delete=models.deletion.CASCADE, to='projects.Project'),
        ),
    ]
