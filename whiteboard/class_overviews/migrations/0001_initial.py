# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('department', models.CharField(max_length=4)),
                ('course_number', models.IntegerField(default=999)),
                ('course_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('start_time', models.TimeField(blank=True)),
                ('end_time', models.TimeField(blank=True)),
                ('days_of_week', models.CharField(max_length=7)),
                ('section_number', models.IntegerField(default=0)),
                ('course', models.ForeignKey(to='class_overviews.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('season', models.CharField(default='Fall', max_length=10)),
                ('year', models.IntegerField(default=2015)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='semester',
            field=models.ForeignKey(to='class_overviews.Semester'),
        ),
        migrations.AddField(
            model_name='document',
            name='course_section',
            field=models.ForeignKey(to='class_overviews.Section'),
        ),
    ]
