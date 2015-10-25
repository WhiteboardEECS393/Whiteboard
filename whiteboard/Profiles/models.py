from django.db import models


class BasicUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    photo = models.ImageField()


class StudentUser(BasicUser):
    grad_year = models.IntegerField(default=2016)
    majors = models.ManyToManyField(Major)
    minors = models.ManyToManyField(Minor)
    classes = models.CharField(max_length=100)  # to change to be many to one field from class profile


class TeachingAssistantUser(StudentUser):
    teaching_classes = models.CharField(max_length=100)  # to change to be many to one field from class profile
    department = models.ForeignKey(Department)


class Major(models.Model):
    major = models.CharField(max_length=50)
    required_classes = models.CharField(max_length=100)  # to change to be many to one field from class profile


class Minor(models.Model):
    minor = models.CharField(max_length=50)
    required_classes = models.CharField(max_length=100)  # to change to be many to one field from class profile


class ProfessorUser(BasicUser):
    department = models.ForeignKey(Department)
    classes = models.CharField(max_length=100)  # to change to be many to one field from class profile
    office_location = models.CharField(max_length=100)


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_head = models.ForeignKey(ProfessorUser)
    department_info = models.CharField(max_length=500)
    majors = models.ForeignKey(Major)
    minors = models.ForeignKey(Minor)
