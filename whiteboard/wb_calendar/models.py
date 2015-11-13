from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    calendar = models.ForeignKey('Calendar')
    course_section = models.ForeignKey('class_overviews.Section')
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField()
    recurring = models.BooleanField(default=False)
    recurring_days = models.CharField(max_length=7, null=True, blank=True)


class Calendar(models.Model):
    owner = models.ForeignKey('Profiles.StudentUser')
    name = models.CharField(max_length=50)
