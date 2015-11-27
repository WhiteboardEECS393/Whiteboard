from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    calendar = models.ForeignKey('Calendar')
    start = models.TimeField()
    end = models.TimeField()
    allDay = models.BooleanField(default=False)
    recurring = models.BooleanField(default=False)
    dow = models.CharField(max_length=7, null=True, blank=True)


class Calendar(models.Model):
    owner = models.ForeignKey('Profiles.StudentUser')
    name = models.CharField(max_length=50)
