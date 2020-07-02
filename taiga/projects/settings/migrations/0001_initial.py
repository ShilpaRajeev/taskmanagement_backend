# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taiga.projects.settings.choices


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0061_auto_20180918_1355'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProjectSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homepage', models.SmallIntegerField(choices=[(taiga.projects.settings.choices.Section(1), 'Timeline'), (taiga.projects.settings.choices.Section(2), 'Epics'), (taiga.projects.settings.choices.Section(3), 'Backlog'), (taiga.projects.settings.choices.Section(4), 'Kanban'), (taiga.projects.settings.choices.Section(5), 'Issues'), (taiga.projects.settings.choices.Section(6), 'TeamWiki')], default=taiga.projects.settings.choices.Section(1))),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_project_settings', to='projects.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_project_settings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='userprojectsettings',
            unique_together=set([('project', 'user')]),
        ),
    ]
