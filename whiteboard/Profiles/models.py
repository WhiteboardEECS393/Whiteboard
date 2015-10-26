from django.db import models


class BasicUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=254)
    bio = models.CharField(max_length=500)
    photo = models.CharField(max_length=200)  # stores a string that holds the photo file path

    def __str__(self):
        return self.first_name + " " + self.last_name


class Major(models.Model):
    major = models.CharField(max_length=50)
    required_classes = models.CharField(max_length=100)  # to change to be many to one field from class profile

    def __str__(self):
        return self.major


class Minor(models.Model):
    minor = models.CharField(max_length=50)
    required_classes = models.CharField(max_length=100)  # to change to be many to one field from class profile

    def __str__(self):
        return self.minor


class StudentUser(BasicUser):
    grad_year = models.IntegerField(default=2016)
    majors = models.ManyToManyField('Major')
    minors = models.ManyToManyField('Minor')
    classes = models.CharField(max_length=100)  # to change to be many to one field from class profile


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_head = models.ForeignKey('ProfessorUser')
    department_info = models.CharField(max_length=500)
    majors = models.ForeignKey('Major')
    minors = models.ForeignKey('Minor')


class TeachingAssistantUser(StudentUser):
    teaching_classes = models.CharField(max_length=100)  # to change to be many to one field from class profile
    department = models.ForeignKey('Department')


class ProfessorUser(BasicUser):
    current_department = models.ForeignKey('Department', blank=True, null=True)
    classes = models.CharField(max_length=100)  # to change to be many to one field from class profile
    office_location = models.CharField(max_length=100)
