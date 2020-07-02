
import django.core.serializers.json
from django.db import migrations
import taiga.base.db.models.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('custom_attributes', '0014_auto_20181025_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epiccustomattributesvalues',
            name='attributes_values',
            field=taiga.base.db.models.fields.json.JSONField(default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder, verbose_name='values'),
        ),
    ]
