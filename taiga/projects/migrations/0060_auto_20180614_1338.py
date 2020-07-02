# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taiga.base.db.models.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0059_auto_20170116_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueDueDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('order', models.IntegerField(default=10, verbose_name='order')),
                ('by_default', models.BooleanField(default=False, verbose_name='by default')),
                ('color', models.CharField(default='#999999', max_length=20, verbose_name='color')),
                ('days_to_due', models.IntegerField(blank=True, default=None, null=True, verbose_name='days to due')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_duedates', to='projects.Project', verbose_name='project')),
            ],
            options={
                'verbose_name': 'issue due date',
                'verbose_name_plural': 'issue due dates',
                'ordering': ['project', 'order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='TaskDueDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('order', models.IntegerField(default=10, verbose_name='order')),
                ('by_default', models.BooleanField(default=False, verbose_name='by default')),
                ('color', models.CharField(default='#999999', max_length=20, verbose_name='color')),
                ('days_to_due', models.IntegerField(blank=True, default=None, null=True, verbose_name='days to due')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_duedates', to='projects.Project', verbose_name='project')),
            ],
            options={
                'verbose_name': 'task due date',
                'verbose_name_plural': 'task due dates',
                'ordering': ['project', 'order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='UserStoryDueDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('order', models.IntegerField(default=10, verbose_name='order')),
                ('by_default', models.BooleanField(default=False, verbose_name='by default')),
                ('color', models.CharField(default='#999999', max_length=20, verbose_name='color')),
                ('days_to_due', models.IntegerField(blank=True, default=None, null=True, verbose_name='days to due')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='us_duedates', to='projects.Project', verbose_name='project')),
            ],
            options={
                'verbose_name': 'user story due date',
                'verbose_name_plural': 'user story due dates',
                'ordering': ['project', 'order', 'name'],
            },
        ),
        migrations.AddField(
            model_name='projecttemplate',
            name='issue_duedates',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='issue duedates'),
        ),
        migrations.AddField(
            model_name='projecttemplate',
            name='task_duedates',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='task duedates'),
        ),
        migrations.AddField(
            model_name='projecttemplate',
            name='us_duedates',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='us duedates'),
        ),
        migrations.AlterUniqueTogether(
            name='issuestatus',
            unique_together=set([('project', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='userstoryduedate',
            unique_together=set([('project', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='taskduedate',
            unique_together=set([('project', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='issueduedate',
            unique_together=set([('project', 'name')]),
        ),
    ]
