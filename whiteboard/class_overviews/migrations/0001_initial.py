# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('department', models.CharField(max_length=4)),
                ('course_number', models.IntegerField(default=999)),
                ('course_name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('professor_name', models.CharField(max_length=40)),
                ('season', models.CharField(max_length=10, default='Fall')),
                ('year', models.IntegerField(default=2015)),
                ('teaching_assistants', models.CharField(blank=True, max_length=200)),
                ('location', models.CharField(max_length=50)),
                ('time_of_day', models.CharField(max_length=20)),
                ('days_of_week', models.CharField(max_length=7)),
                ('section_number', models.IntegerField(default=0)),
                ('course', models.ForeignKey(to='class_overviews.Course')),
                ('students', models.ManyToManyField(to='Profiles.StudentUser')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='course_section',
            field=models.ForeignKey(to='class_overviews.Section'),
        ),
    ]
