# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='minors',
            field=models.ManyToManyField(blank=True, to='Profiles.Minor'),
        ),
    ]
