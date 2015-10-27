# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('major', models.CharField(max_length=50)),
                ('required_classes', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['major'],
            },
        ),
        migrations.CreateModel(
            name='Minor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('minor', models.CharField(max_length=50)),
                ('required_classes', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['minor'],
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('bio', models.CharField(max_length=500)),
                ('classes', models.CharField(max_length=100)),
                ('office_location', models.CharField(max_length=100)),
                ('current_department', models.ForeignKey(blank=True, to='Profiles.Department', null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=100, default='First')),
                ('last_name', models.CharField(max_length=100, default='Last')),
                ('email_id', models.EmailField(max_length=254, default='abc123@case.edu')),
                ('bio', models.CharField(max_length=500, default='none')),
                ('photo', models.CharField(max_length=200, default='none')),
                ('grad_year', models.IntegerField(default=2016)),
                ('classes', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='TeachingAssistantUser',
            fields=[
                ('studentuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='Profiles.StudentUser', primary_key=True, serialize=False)),
                ('teaching_classes', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
            bases=('Profiles.studentuser',),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='majors',
            field=models.ManyToManyField(to='Profiles.Major'),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='minors',
            field=models.ManyToManyField(to='Profiles.Minor'),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='department',
            name='department_head',
            field=models.ForeignKey(to='Profiles.Professor'),
        ),
        migrations.AddField(
            model_name='department',
            name='majors',
            field=models.ForeignKey(to='Profiles.Major'),
        ),
        migrations.AddField(
            model_name='department',
            name='minors',
            field=models.ForeignKey(to='Profiles.Minor'),
        ),
        migrations.AddField(
            model_name='teachingassistantuser',
            name='department',
            field=models.ForeignKey(to='Profiles.Department'),
        ),
    ]
