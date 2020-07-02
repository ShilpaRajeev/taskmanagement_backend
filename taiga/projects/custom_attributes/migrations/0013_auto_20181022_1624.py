# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django.core.serializers.json
from django.db import migrations, models
import taiga.base.db.models.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('custom_attributes', '0012_auto_20161201_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='epiccustomattribute',
            name='extra',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, default=None, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
        migrations.AddField(
            model_name='issuecustomattribute',
            name='extra',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, default=None, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
        migrations.AddField(
            model_name='taskcustomattribute',
            name='extra',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, default=None, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
        migrations.AddField(
            model_name='userstorycustomattribute',
            name='extra',
            field=taiga.base.db.models.fields.json.JSONField(blank=True, default=None, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
        migrations.AlterField(
            model_name='epiccustomattribute',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('multiline', 'Multi-Line Text'), ('richtext', 'Rich text'), ('date', 'Date'), ('url', 'Url'), ('dropdown', 'Dropdown')], default='text', max_length=16, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='issuecustomattribute',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('multiline', 'Multi-Line Text'), ('richtext', 'Rich text'), ('date', 'Date'), ('url', 'Url'), ('dropdown', 'Dropdown')], default='text', max_length=16, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='taskcustomattribute',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('multiline', 'Multi-Line Text'), ('richtext', 'Rich text'), ('date', 'Date'), ('url', 'Url'), ('dropdown', 'Dropdown')], default='text', max_length=16, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='userstorycustomattribute',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('multiline', 'Multi-Line Text'), ('richtext', 'Rich text'), ('date', 'Date'), ('url', 'Url'), ('dropdown', 'Dropdown')], default='text', max_length=16, verbose_name='type'),
        ),
    ]
