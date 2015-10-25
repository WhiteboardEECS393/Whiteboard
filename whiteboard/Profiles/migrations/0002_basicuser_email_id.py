# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicuser',
            name='email_id',
            field=models.EmailField(max_length=254, default='adc123@case.edu'),
        ),
    ]
