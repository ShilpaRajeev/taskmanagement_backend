# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0005_attachment_sha1'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='attachment',
            index_together=set([('content_type', 'object_id')]),
        ),
    ]
