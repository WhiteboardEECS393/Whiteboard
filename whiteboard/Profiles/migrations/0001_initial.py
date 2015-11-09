# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('class_overviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('department_code', models.CharField(max_length=4)),
                ('department_name', models.CharField(max_length=100)),
                ('department_info', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ['department_name'],
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('major', models.CharField(max_length=50)),
                ('required_classes', models.ManyToManyField(blank=True, to='class_overviews.Course')),
            ],
            options={
                'ordering': ['major'],
            },
        ),
        migrations.CreateModel(
            name='Minor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('minor', models.CharField(max_length=50)),
                ('required_classes', models.ManyToManyField(blank=True, to='class_overviews.Course')),
            ],
            options={
                'ordering': ['minor'],
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('bio', models.CharField(max_length=500)),
                ('office_location', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=200, default='none')),
                ('classes', models.ManyToManyField(blank=True, to='class_overviews.Section')),
                ('current_department', models.ForeignKey(null=True, blank=True, to='Profiles.Department')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('first_name', models.CharField(max_length=100, default='First')),
                ('last_name', models.CharField(max_length=100, default='Last')),
                ('email_id', models.EmailField(max_length=254, default='abc123@case.edu')),
                ('bio', models.CharField(max_length=500, default='none')),
                ('photo', models.CharField(max_length=200, default='none')),
                ('grad_year', models.IntegerField(default=2016)),
                ('majors', models.ManyToManyField(blank=True, to='Profiles.Major')),
                ('minors', models.ManyToManyField(blank=True, to='Profiles.Minor')),
                ('student_classes', models.ManyToManyField(blank=True, related_name='studentuser_student', to='class_overviews.Section')),
                ('ta_classes', models.ManyToManyField(blank=True, related_name='studentuser_ta', to='class_overviews.Section')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.AddField(
            model_name='department',
            name='department_head',
            field=models.ForeignKey(null=True, blank=True, to='Profiles.Professor'),
        ),
        migrations.AddField(
            model_name='department',
            name='majors',
            field=models.ManyToManyField(blank=True, to='Profiles.Major'),
        ),
        migrations.AddField(
            model_name='department',
            name='minors',
            field=models.ManyToManyField(blank=True, to='Profiles.Minor'),
        ),
    ]
