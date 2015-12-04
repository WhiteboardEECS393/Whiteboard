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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('major', models.CharField(max_length=50)),
                ('required_classes', models.ManyToManyField(to='class_overviews.Course', blank=True)),
            ],
            options={
                'ordering': ['major'],
            },
        ),
        migrations.CreateModel(
            name='Minor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('minor', models.CharField(max_length=50)),
                ('required_classes', models.ManyToManyField(to='class_overviews.Course', blank=True)),
            ],
            options={
                'ordering': ['minor'],
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('full_name', models.CharField(default='albert einstein', max_length=200)),
                ('email_id', models.EmailField(max_length=254)),
                ('bio', models.CharField(max_length=500)),
                ('office_location', models.CharField(max_length=100)),
                ('photo', models.FileField(upload_to='Profiles/static/img')),
                ('classes', models.ManyToManyField(to='class_overviews.Section', blank=True)),
                ('current_department', models.ForeignKey(null=True, blank=True, to='Profiles.Department')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(default='First', max_length=100)),
                ('last_name', models.CharField(default='Last', max_length=100)),
                ('full_name', models.CharField(default='First Last', max_length=200)),
                ('email_id', models.EmailField(default='abc123@case.edu', max_length=254)),
                ('bio', models.CharField(default='none', max_length=500)),
                ('photo', models.FileField(upload_to='Profiles/static/img')),
                ('grad_year', models.IntegerField(default=2016)),
                ('majors', models.ManyToManyField(to='Profiles.Major', blank=True)),
                ('minors', models.ManyToManyField(to='Profiles.Minor', blank=True)),
                ('student_classes', models.ManyToManyField(related_name='studentuser_student', to='class_overviews.Section', blank=True)),
                ('ta_classes', models.ManyToManyField(related_name='studentuser_ta', to='class_overviews.Section', blank=True)),
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
            field=models.ManyToManyField(to='Profiles.Major', blank=True),
        ),
        migrations.AddField(
            model_name='department',
            name='minors',
            field=models.ManyToManyField(to='Profiles.Minor', blank=True),
        ),
    ]
