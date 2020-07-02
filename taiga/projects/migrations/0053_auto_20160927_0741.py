# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0052_epic_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='creation_template',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='projects.ProjectTemplate', verbose_name='creation template'),
        ),
    ]
