# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0046_triggers_to_update_tags_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='anon_permissions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(choices=[('view_project', 'View project'), ('view_milestones', 'View milestones'), ('view_us', 'View user stories'), ('view_tasks', 'View tasks'), ('view_issues', 'View issues'), ('view_wiki_pages', 'View wiki pages'), ('view_wiki_links', 'View wiki links')]), blank=True, default=list, null=True, size=None, verbose_name='anonymous permissions'),
        ),
        migrations.AlterField(
            model_name='project',
            name='public_permissions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(choices=[('view_project', 'View project'), ('view_milestones', 'View milestones'), ('add_milestone', 'Add milestone'), ('modify_milestone', 'Modify milestone'), ('delete_milestone', 'Delete milestone'), ('view_us', 'View user story'), ('add_us', 'Add user story'), ('modify_us', 'Modify user story'), ('comment_us', 'Comment user story'), ('delete_us', 'Delete user story'), ('view_tasks', 'View tasks'), ('add_task', 'Add task'), ('modify_task', 'Modify task'), ('comment_task', 'Comment task'), ('delete_task', 'Delete task'), ('view_issues', 'View issues'), ('add_issue', 'Add issue'), ('modify_issue', 'Modify issue'), ('comment_issue', 'Comment issue'), ('delete_issue', 'Delete issue'), ('view_wiki_pages', 'View wiki pages'), ('add_wiki_page', 'Add wiki page'), ('modify_wiki_page', 'Modify wiki page'), ('comment_wiki_page', 'Comment wiki page'), ('delete_wiki_page', 'Delete wiki page'), ('view_wiki_links', 'View wiki links'), ('add_wiki_link', 'Add wiki link'), ('modify_wiki_link', 'Modify wiki link'), ('delete_wiki_link', 'Delete wiki link')]), blank=True, default=list, null=True, size=None, verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, null=True, size=None, verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags_colors',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), size=2), blank=True, default=list, null=True, size=None, verbose_name='tags colors'),
        ),
    ]