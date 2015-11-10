# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wb_calendar', '0002_auto_20151109_0129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end_time',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='start_time',
            new_name='start',
        ),
        migrations.AddField(
            model_name='event',
            name='allDay',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
