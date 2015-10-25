# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=500)),
                ('photo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('department_info', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('major', models.CharField(max_length=50)),
                ('required_classes', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Minor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('minor', models.CharField(max_length=50)),
                ('required_classes', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessorUser',
            fields=[
                ('basicuser_ptr', models.OneToOneField(to='Profiles.BasicUser', parent_link=True, serialize=False, primary_key=True, auto_created=True)),
                ('classes', models.CharField(max_length=100)),
                ('office_location', models.CharField(max_length=100)),
            ],
            bases=('Profiles.basicuser',),
        ),
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('basicuser_ptr', models.OneToOneField(to='Profiles.BasicUser', parent_link=True, serialize=False, primary_key=True, auto_created=True)),
                ('grad_year', models.IntegerField(default=2016)),
                ('classes', models.CharField(max_length=100)),
            ],
            bases=('Profiles.basicuser',),
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
        migrations.CreateModel(
            name='TeachingAssistantUser',
            fields=[
                ('studentuser_ptr', models.OneToOneField(to='Profiles.StudentUser', parent_link=True, serialize=False, primary_key=True, auto_created=True)),
                ('teaching_classes', models.CharField(max_length=100)),
            ],
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
            model_name='professoruser',
            name='current_department',
            field=models.ForeignKey(to='Profiles.Department'),
        ),
        migrations.AddField(
            model_name='department',
            name='department_head',
            field=models.ForeignKey(to='Profiles.ProfessorUser'),
        ),
        migrations.AddField(
            model_name='teachingassistantuser',
            name='department',
            field=models.ForeignKey(to='Profiles.Department'),
        ),
    ]
