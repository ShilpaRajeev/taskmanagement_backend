# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.core.serializers.json
from django.db import migrations, models
import taiga.base.db.models.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0057_auto_20161129_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttemplate',
            name='epic_custom_attributes',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='epic custom attributes'),
        ),
        migrations.AddField(
            model_name='projecttemplate',
            name='is_looking_for_people',
            field=models.BooleanField(default=False, verbose_name='is looking for people'),
        ),
        migrations.AddField(
            model_name='projecttemplate',
            name='issue_custom_attributes',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='issue custom attributes'),
        ),
        migrations.AddField(
            model_name='projecttemplate',
            name='looking_for_people_note',
            field=models.TextField(blank=True, default='', verbose_name='loking for people note'),
        ),
        migrations.AddField(
            model_name='projecttemplate',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, null=True, size=None, verbose_name='tags'),
        ),
        migrations.AddField(
            model_name='projecttemplate',
            name='tags_colors',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), size=2), blank=True, default=list, null=True, size=None, verbose_name='tags colors'),
        ),
        migrations.AddField(
            model_name='projecttemplate',
            name='task_custom_attributes',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='task custom attributes'),
        ),
        migrations.AddField(
            model_name='projecttemplate',
            name='us_custom_attributes',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='us custom attributes'),
        ),
    ]
