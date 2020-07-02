# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0038_auto_20160215_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='blocked_code',
            field=models.CharField(blank=True, choices=[('blocked-by-nonpayment', 'This project is blocked due to payment failure'), ('blocked-by-staff', 'This project is blocked by admin staff'), ('blocked-by-owner-leaving', 'This project is blocked because the owner left')], default=None, max_length=255, null=True, verbose_name='blocked code'),
        ),
    ]