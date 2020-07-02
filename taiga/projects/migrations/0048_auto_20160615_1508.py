# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0047_auto_20160614_1201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projecttemplate',
            options={'ordering': ['order', 'name'], 'verbose_name': 'project template', 'verbose_name_plural': 'project templates'},
        ),
        migrations.AddField(
            model_name='projecttemplate',
            name='order',
            field=models.IntegerField(default=10000, verbose_name='user order'),
        ),
    ]
