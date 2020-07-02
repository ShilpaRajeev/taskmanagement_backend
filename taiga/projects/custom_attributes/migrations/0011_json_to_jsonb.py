# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations
from django.contrib.postgres.fields import JSONField

class Migration(migrations.Migration):

    dependencies = [
        ('custom_attributes', '0010_auto_20160928_0540'),
    ]

    operations = [
        migrations.RunSQL(
            """
                ALTER TABLE "{table_name}"
                   ALTER COLUMN "{column_name}"
                           TYPE jsonb
                          USING regexp_replace("{column_name}"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb;
            """.format(
                table_name="custom_attributes_epiccustomattributesvalues",
                column_name="attributes_values",
            ),
            reverse_sql=migrations.RunSQL.noop
        ),
        migrations.RunSQL(
            """
                ALTER TABLE "{table_name}"
                   ALTER COLUMN "{column_name}"
                           TYPE jsonb
                          USING regexp_replace("{column_name}"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb;
            """.format(
                table_name="custom_attributes_userstorycustomattributesvalues",
                column_name="attributes_values",
            ),
            reverse_sql=migrations.RunSQL.noop
        ),
        migrations.RunSQL(
            """
                ALTER TABLE "{table_name}"
                   ALTER COLUMN "{column_name}"
                           TYPE jsonb
                          USING regexp_replace("{column_name}"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb;
            """.format(
                table_name="custom_attributes_taskcustomattributesvalues",
                column_name="attributes_values",
            ),
            reverse_sql=migrations.RunSQL.noop
        ),
        migrations.RunSQL(
            """
                ALTER TABLE "{table_name}"
                   ALTER COLUMN "{column_name}"
                           TYPE jsonb
                          USING regexp_replace("{column_name}"::text, '[\\\\]+u0000', '\\\\\\\\u0000', 'g')::jsonb;
            """.format(
                table_name="custom_attributes_issuecustomattributesvalues",
                column_name="attributes_values",
            ),
            reverse_sql=migrations.RunSQL.noop
        ),

        # Function: Remove a key in a json field
        migrations.RunSQL(
            """
        CREATE OR REPLACE FUNCTION "json_object_delete_keys"("json" jsonb, VARIADIC "keys_to_delete" text[])
                           RETURNS jsonb
                          LANGUAGE sql
                         IMMUTABLE
                            STRICT
                                AS $function$
                   SELECT COALESCE ((SELECT ('{' || string_agg(to_json("key") || ':' || "value", ',') || '}')
                                       FROM jsonb_each("json")
                                      WHERE "key" <> ALL ("keys_to_delete")),
                                    '{}')::text::jsonb $function$;
            """,
            reverse_sql="""
        CREATE OR REPLACE FUNCTION "json_object_delete_keys"("json" json, VARIADIC "keys_to_delete" text[])
                           RETURNS json
                          LANGUAGE sql
                         IMMUTABLE
                            STRICT
                                AS $function$
                   SELECT COALESCE ((SELECT ('{' || string_agg(to_json("key") || ':' || "value", ',') || '}')
                                       FROM json_each("json")
                                      WHERE "key" <> ALL ("keys_to_delete")),
                                    '{}')::json $function$;"""
        ),
    ]
