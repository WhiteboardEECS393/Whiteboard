from django.db import models


class Course(models.Model):
    department = models.CharField(max_length=4)
    course_number = models.IntegerField(default=999)
    course_name = models.CharField(max_length=200)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.department + str(self.course_number) + ": " + self.course_name


class Section(models.Model):
    professor_name = models.CharField(max_length=40) # change to foreign key to Professor class
    season = models.CharField(max_length=10, default="Fall")
    year = models.IntegerField(default=2015)
    location = models.CharField(max_length=50)
    time_of_day = models.CharField(max_length=20)
    days_of_week = models.CharField(max_length=7)
    section_number = models.IntegerField(default=0)
    course = models.ForeignKey(Course)

    class Meta:
        ordering = ['-year', 'season']

    def __str__(self):
        return str(self.course) + " (" + str(self.section_number) + ") " + self.season + str(self.year)


class Document(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)
    course_section = models.ForeignKey(Section)

    def __str__(self):
        return self.name
