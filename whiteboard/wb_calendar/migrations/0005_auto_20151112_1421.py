# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wb_calendar', '0004_auto_20151109_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='course_section',
        ),
        migrations.RemoveField(
            model_name='event',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_date',
        ),
    ]
