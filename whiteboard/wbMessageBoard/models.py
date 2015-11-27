from django.db import models


# Create your models here.
class DiscussionBoard(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    course = models.ForeignKey('class_overviews.Section')

    def __str__(self):
        return self.name


class Thread(models.Model):
    subject = models.CharField(max_length=200)
    creator = models.ForeignKey('Profiles.StudentUser')
    message = models.CharField(max_length=1000)
    time_of_creation = models.DateTimeField('Created on')
    board = models.ForeignKey(DiscussionBoard)

    def __str__(self):
        return self.subject


class Post(models.Model):
    creator = models.ForeignKey('Profiles.StudentUser')
    time_of_creation = models.DateTimeField('Created on')
    content = models.CharField(max_length=1000)
    thread = models.ForeignKey(Thread)

    def __str__(self):
        return self.thread.subject + ' ' + str(self.creator)
    #        return self.thread.subject + ' ' + self.creator.first_name + " " + self.creator.last_name


