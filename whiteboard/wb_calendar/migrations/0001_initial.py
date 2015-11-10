# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0001_initial'),
        ('class_overviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(to='Profiles.StudentUser')),
            ],
        ),
        migrations.CreateModel(
            name='DaysOfWeek',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('day', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('recurring', models.BooleanField(default=False)),
                ('calendar', models.ForeignKey(to='wb_calendar.Calendar')),
                ('course_section', models.ForeignKey(to='class_overviews.Section')),
                ('recurring_days', models.ManyToManyField(to='wb_calendar.DaysOfWeek')),
            ],
        ),
    ]
