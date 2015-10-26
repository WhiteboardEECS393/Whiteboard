# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0002_basicuser_email_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicuser',
            name='email_id',
            field=models.EmailField(max_length=254),
        ),
    ]
