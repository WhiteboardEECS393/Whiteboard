# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wb_calendar', '0003_auto_20151109_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='recurring_days',
            new_name='dow',
        ),
        migrations.AlterField(
            model_name='event',
            name='allDay',
            field=models.BooleanField(default=False),
        ),
    ]
