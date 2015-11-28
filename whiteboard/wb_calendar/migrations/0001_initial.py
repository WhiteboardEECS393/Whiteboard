# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(to='Profiles.StudentUser')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('allDay', models.BooleanField(default=False)),
                ('recurring', models.BooleanField(default=False)),
                ('dow', models.CharField(null=True, max_length=7, blank=True)),
                ('calendar', models.ForeignKey(to='wb_calendar.Calendar')),
            ],
        ),
    ]
