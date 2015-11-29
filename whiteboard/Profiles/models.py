from django.db import models
from django.contrib.auth.models import User
from class_overviews.models import Semester, Section, Course



class Major(models.Model):
    major = models.CharField(max_length=50)
    required_classes = models.ManyToManyField('class_overviews.Course', blank=True)

    def __str__(self):
        return self.major

    class Meta:
        ordering = ['major']


class Minor(models.Model):
    minor = models.CharField(max_length=50)
    required_classes = models.ManyToManyField('class_overviews.Course', blank=True)

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
    photo = models.FileField(upload_to='Profiles/static/img')
    grad_year = models.IntegerField(default=2016)
    majors = models.ManyToManyField('Major', blank=True)
    minors = models.ManyToManyField('Minor', blank=True)
    student_classes = models.ManyToManyField('class_overviews.Section', related_name='%(class)s_student', blank=True)
    ta_classes = models.ManyToManyField('class_overviews.Section', related_name='%(class)s_ta', blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def getCurrentClasses(self):
        semester = Semester.objects.filter(season = "Fall", year = 2015)[0]
        classes = self.student_classes.filter(semester = semester)
        return classes

    def getOlderClasses(self):
        semester = Semester.objects.filter(season = "Fall", year = 2015)[0]
        classes = self.student_classes.exclude(semester = semester)
        return classes

    class Meta:
        ordering = ['last_name', 'first_name']

class Department(models.Model):
    department_code = models.CharField(max_length = 4)
    department_name = models.CharField(max_length=100)
    department_head = models.ForeignKey('Professor', blank=True, null=True)
    department_info = models.CharField(max_length=500)
    majors = models.ManyToManyField('Major', blank=True)
    minors = models.ManyToManyField('Minor', blank=True)

    def __str__(self):
        return self.department_name

    def getCurrentClasses(self):
        semester = Semester.objects.filter(season = "Fall", year = 2015)[0]
        courses = Course.objects.filter(department = self.department_code)
        classes = []
        for course in courses:
            sections = Section.objects.filter(semester = semester, course = course)
            if len(sections) > 0:
                classes.extend(sections)
        return classes

    def getOlderClasses(self):
        semester = Semester.objects.filter(season = "Fall", year = 2015)[0]
        courses = Course.objects.filter(department = self.department_code)
        classes = []
        for course in courses:
            sections = Section.objects.filter(course = course).exclude(semester = semester)
            if len(sections) > 0:
                classes.extend(sections)
        return classes

    class Meta:
        ordering = ['department_name']


class Professor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=254)
    bio = models.CharField(max_length=500)
    current_department = models.ForeignKey('Department', blank=True, null=True)
    office_location = models.CharField(max_length=100)
    photo = models.FileField(upload_to='Profiles/static/img')  # stores a string that holds the photo file path
    classes = models.ManyToManyField('class_overviews.Section', blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def getCurrentClasses(self):
        semester = Semester.objects.filter(season = "Fall", year = 2015)[0]
        classes = self.classes.filter(semester = semester)
        return classes

    def getOlderClasses(self):
        semester = Semester.objects.filter(season = "Fall", year = 2015)[0]
        classes = self.classes.exclude(semester = semester)
        return classes

    class Meta:
            ordering = ['last_name', 'first_name']
