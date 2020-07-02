# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations


UPDATE_PROJECTS_ANON_PERMISSIONS_SQL = """
    UPDATE projects_project
    SET
        ANON_PERMISSIONS = array_append(ANON_PERMISSIONS, '{comment_permission}')
    WHERE
        '{base_permission}' = ANY(ANON_PERMISSIONS)
        AND
        NOT '{comment_permission}' = ANY(ANON_PERMISSIONS)
"""

UPDATE_PROJECTS_PUBLIC_PERMISSIONS_SQL = """
    UPDATE projects_project
    SET
        PUBLIC_PERMISSIONS = array_append(PUBLIC_PERMISSIONS, '{comment_permission}')
    WHERE
        '{base_permission}' = ANY(PUBLIC_PERMISSIONS)
        AND
        NOT '{comment_permission}' = ANY(PUBLIC_PERMISSIONS)
"""

class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0041_auto_20160519_1058'),
    ]

    operations = [
        # user stories
        migrations.RunSQL(UPDATE_PROJECTS_ANON_PERMISSIONS_SQL.format(
            base_permission="modify_us",
            comment_permission="comment_us")
        ),

        migrations.RunSQL(UPDATE_PROJECTS_PUBLIC_PERMISSIONS_SQL.format(
            base_permission="modify_us",
            comment_permission="comment_us")
        ),

        # tasks
        migrations.RunSQL(UPDATE_PROJECTS_ANON_PERMISSIONS_SQL.format(
            base_permission="modify_task",
            comment_permission="comment_task")
        ),

        migrations.RunSQL(UPDATE_PROJECTS_PUBLIC_PERMISSIONS_SQL.format(
            base_permission="modify_task",
            comment_permission="comment_task")
        ),

        # issues
        migrations.RunSQL(UPDATE_PROJECTS_ANON_PERMISSIONS_SQL.format(
            base_permission="modify_issue",
            comment_permission="comment_issue")
        ),

        migrations.RunSQL(UPDATE_PROJECTS_PUBLIC_PERMISSIONS_SQL.format(
            base_permission="modify_issue",
            comment_permission="comment_issue")
        )
    ]