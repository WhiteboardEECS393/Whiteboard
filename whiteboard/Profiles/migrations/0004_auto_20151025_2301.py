# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0003_auto_20151025_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professoruser',
            name='current_department',
            field=models.ForeignKey(null=True, blank=True, to='Profiles.Department'),
        ),
    ]
