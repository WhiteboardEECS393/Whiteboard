# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class_overviews', '0001_initial'),
        ('Profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscussionBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('course', models.ForeignKey(to='class_overviews.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('time_of_creation', models.DateTimeField(verbose_name='Created on')),
                ('content', models.CharField(max_length=1000)),
                ('creator', models.ForeignKey(to='Profiles.StudentUser')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=1000)),
                ('time_of_creation', models.DateTimeField(verbose_name='Created on')),
                ('board', models.ForeignKey(to='wbMessageBoard.DiscussionBoard')),
                ('creator', models.ForeignKey(to='Profiles.StudentUser')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(to='wbMessageBoard.Thread'),
        ),
    ]
