# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wb_calendar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='recurring_days',
        ),
        migrations.AddField(
            model_name='event',
            name='recurring_days',
            field=models.CharField(null=True, blank=True, max_length=7),
        ),
        migrations.DeleteModel(
            name='DaysOfWeek',
        ),
    ]
