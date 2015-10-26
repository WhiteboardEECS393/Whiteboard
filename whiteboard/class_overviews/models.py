from django.db import models


class Course(models.Model):
    course_number = models.CharField(max_length=8)
    course_name = models.CharField(max_length=200)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.course_number + ": " + self.course_name


class Section(models.Model):
    professor_name = models.CharField(max_length=50)    #will later be foreign key
    semester = models.CharField(max_length=50)
    '''teaching_assistants = models.CharField(max_length=200, blank=True) #foreign key
    location = models.CharField(max_length=50)
    time_of_day = models.CharField(max_length=20)
    days_of_week = models.CharField(max_length=7)
    section_number = models.IntegerField(default=0)
    students = models.CharField(max_length=1000, blank=True) #foreign key
    syllabus_path = models.CharField(max_length=100, blank=True)'''
    course = models.ForeignKey(Course)

    def __str__(self):
        return self.course.course_number + " " + self.semester


class Document(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)
    #course_section = models.ForeignKey(Section)

    def __str__(self):
        return self.name
