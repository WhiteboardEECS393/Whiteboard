# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('class_overviews', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('bio', models.CharField(max_length=500)),
                ('office_location', models.CharField(max_length=100)),
                ('photo', models.FileField(upload_to='Profiles/static/img')),
                ('classes', models.ManyToManyField(blank=True, to='class_overviews.Section')),
                ('current_department', models.ForeignKey(to='Profiles.Department', blank=True, null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('first_name', models.CharField(default='First', max_length=100)),
                ('last_name', models.CharField(default='Last', max_length=100)),
                ('email_id', models.EmailField(default='abc123@case.edu', max_length=254)),
                ('bio', models.CharField(default='none', max_length=500)),
                ('photo', models.FileField(upload_to='Profiles/static/img')),
                ('grad_year', models.IntegerField(default=2016)),
                ('majors', models.ManyToManyField(blank=True, to='Profiles.Major')),
                ('minors', models.ManyToManyField(blank=True, to='Profiles.Minor')),
                ('student_classes', models.ManyToManyField(blank=True, to='class_overviews.Section', related_name='studentuser_student')),
                ('ta_classes', models.ManyToManyField(blank=True, to='class_overviews.Section', related_name='studentuser_ta')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.AddField(
            model_name='department',
            name='department_head',
            field=models.ForeignKey(to='Profiles.Professor', blank=True, null=True),
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
