

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0008_auto_20181010_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifypolicy',
            name='web_notify_level',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
