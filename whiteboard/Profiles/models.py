from django.db import models
from django.contrib.auth.models import User

class Major(models.Model):
    major = models.CharField(max_length=50)
    #required_classes = models.ManyToManyField('class_overviews.Course', blank=True)

    def __str__(self):
        return self.major

    class Meta:
        ordering = ['major']


class Minor(models.Model):
    minor = models.CharField(max_length=50)
    #required_classes = models.ManyToManyField('class_overviews.Course', blank=True)

    def __str__(self):
        return self.minor

    class Meta:
        ordering = ['minor']

class StudentUser(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=100, default='First')
    last_name = models.CharField(max_length=100, default="Last")
    email_id = models.EmailField(max_length=254, default='abc123@case.edu')
    bio = models.CharField(max_length=500, default='none')
    photo = models.CharField(max_length=200, default='none')  # stores a string that holds the photo file path
    grad_year = models.IntegerField(default=2016)
    majors = models.ForeignKey('Major', blank=True, null=True)
    minors = models.ForeignKey('Minor', blank=True, null=True)
    student_classes = models.ManyToManyField('class_overviews.Section', related_name='%(class)s_student', blank=True)
    ta_classes = models.ManyToManyField('class_overviews.Section', related_name='%(class)s_ta', blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['last_name', 'first_name']


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_head = models.ForeignKey('Professor', blank=True)
    department_info = models.CharField(max_length=500)
    majors = models.ManyToManyField('Major', blank=True)
    minors = models.ManyToManyField('Minor', blank=True)

    class Meta:
        ordering = ['department_name']


class Professor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=254)
    bio = models.CharField(max_length=500)
    current_department = models.ForeignKey('Department', blank=True, null=True)
    office_location = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + self.last_name

    class Meta:
            ordering = ['last_name', 'first_name']
