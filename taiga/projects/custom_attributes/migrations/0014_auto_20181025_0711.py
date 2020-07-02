# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_attributes', '0013_auto_20181022_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epiccustomattribute',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('multiline', 'Multi-Line Text'), ('richtext', 'Rich text'), ('date', 'Date'), ('url', 'Url'), ('dropdown', 'Dropdown'), ('checkbox', 'Checkbox'), ('number', 'Number')], default='text', max_length=16, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='issuecustomattribute',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('multiline', 'Multi-Line Text'), ('richtext', 'Rich text'), ('date', 'Date'), ('url', 'Url'), ('dropdown', 'Dropdown'), ('checkbox', 'Checkbox'), ('number', 'Number')], default='text', max_length=16, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='taskcustomattribute',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('multiline', 'Multi-Line Text'), ('richtext', 'Rich text'), ('date', 'Date'), ('url', 'Url'), ('dropdown', 'Dropdown'), ('checkbox', 'Checkbox'), ('number', 'Number')], default='text', max_length=16, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='userstorycustomattribute',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('multiline', 'Multi-Line Text'), ('richtext', 'Rich text'), ('date', 'Date'), ('url', 'Url'), ('dropdown', 'Dropdown'), ('checkbox', 'Checkbox'), ('number', 'Number')], default='text', max_length=16, verbose_name='type'),
        ),
    ]
