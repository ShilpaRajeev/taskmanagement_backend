# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0007_attachment_from_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='from_comment',
            field=models.BooleanField(default=False, verbose_name='from comment'),
        ),
    ]
