# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscussionBoard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('creator', models.CharField(max_length=60)),
                ('time_of_creation', models.DateTimeField(verbose_name='Created on')),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('subject', models.CharField(max_length=200)),
                ('creator', models.CharField(max_length=60)),
                ('message', models.CharField(max_length=1000)),
                ('time_of_creation', models.DateTimeField(verbose_name='Created on')),
                ('board', models.ForeignKey(to='wbMessageBoard.DiscussionBoard')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(to='wbMessageBoard.Thread'),
        ),
    ]
