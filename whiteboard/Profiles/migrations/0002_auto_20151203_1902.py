# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='full_name',
            field=models.CharField(max_length=200, default='albert einstein'),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='full_name',
            field=models.CharField(max_length=200, default='First Last'),
        ),
    ]
