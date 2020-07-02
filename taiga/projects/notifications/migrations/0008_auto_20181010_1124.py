# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taiga.base.db.models.fields.json


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0007_notifypolicy_live_notify_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('read', models.DateTimeField(default=None, null=True)),
                ('event_type', models.PositiveIntegerField()),
                ('data', taiga.base.db.models.fields.json.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='web_notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='notifypolicy',
            name='web_notify_level',
            field=models.BooleanField(default=True),
        ),
    ]
