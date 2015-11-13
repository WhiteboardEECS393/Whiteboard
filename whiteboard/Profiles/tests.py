from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
from .models import Major
from .models import Minor
from .models import StudentUser
from .models import Department
from .models import Professor
from class_overviews.models import Section
from class_overviews.models import Course

def createMajor(self):
    newMajor = Major(major = "Computer Science")
    return newMajor
def createMinor(self):
    newMinor = Minor(minor = "Game Design")
    return newMinor
def createStudentUser(self):
    user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
def createDepartment(self):
    departement_code = "EECS"
    departement_name = "Electrical Engineering and Computer Science"
    departement_info = "Stuff about the department"
def createProfessor(self):
    first_name = "Tekin"
    last_name = "Osoy....glu"
    email_id = "abc@case.edu"
    bio = "Something or the other"
    office_Location = "Where the sun don't shine"

class ProfilesMethodTests(TestCase):
    def test_Major_str(self):
        testMajor = createMajor(self)
        self.assertEquals(testMajor.major, testMajor.__str__(self))

    def test_Minor_str(self):
        test_Minor = createMinor(self)
        self.assertEquals(test_Minor.minor, test_Minor.__str__(self))

    def test_Student_str(self):
        testStudentUser = createStudentUser(self)
        self.assertEquals(testStudentUser.first_name + " " + testStudentUser.last_name, testStudentUser.__str__(self))

    def test_Department_str(self):
        testDepartment = createDepartment(self)
        self.assertEquals(testDepartment.department_name, testDepartment.__str__(self))

    def test_Professor_str(self):
        testProfessor = createProfessor(self)
        self.assertEquals(testProfessor.first_name + " " + testProfessor.last_name, testProfessor.__str__(self))
'''
#Needed for testing BasicUser
#How do you make a user?
global testfirst_name
testfirst_name = 'Daniel'
global testlast_name
testlast_name = 'McKinnon'
global testemail_id
testemail_id = 'dnm30@case.edu'
global testbio
testbio = 'This is the story of my life'
global testphoto
testphoto = 'Filepath'
#Needed to test Major
global testmajor
testmajor = 'Computer Science'
#Needed to test minor
global testminor
testminor = 'Sociology'
#Needed to test StudentUser
global testgrad_year
testgrad_year = 2016
global teststudent_majors
teststudent_majors = 'Computer Science and Cog Scie'
global teststudent_minors
teststudent_minors = 'Sociology and Theater'
global testsection_OS
testsection_OS= Section(location = "DeGrace",
                                         start_time = models.TimeField(auto_now=True, auto_now_add=True),
                                         end_time = models.TimeField(auto_now=True, auto_now_add=True),
                                         days_of_week = "MWF",
                                         course = Course(department = createDepartment(self),
                                                         course_number = 338,
                                                         course_name = "Operating Systems")))
#Needed to test Department
global testdepartment_name
testdepartment_name = 'EECS'
global testdepartment_head
testdepartment_head = 'Not sure'
global testdepartment_info
testdepartment_info = 'Some info'
global testdepartment_majors
testdepartment_majors = 'Comp. Sci, Comp E, Systems, EE'
global testdepartment_minors
testdepartment_minors = 'Game design and other minors'
#Needed for teaching assistant
global testteaching_classes
testteaching_classes = 'Java 132'
#Needed to test Professor
global testprofessor_first_name
testprofessor_first_name = 'Andy'
global testprofessor_last_name
testprofessor_last_name = 'Podgurski'
global testprofessor_email_id
testprofessor_email_id = 'hap@case.edu'
global testprofessor_bio
testprofessor_bio = 'This is the story of Podgurski\'s life'
global testprofessor_department
testprofessor_department = 'EECS'
global testprofessor_classes
testprofessor_classes = 'ECCS 444 and EECS 393'
global testoffice_location
testoffice_location = 'Somewhere on the quad'

def createMajor(self):
    return Major(major = testmajor, required_classes = testrequired_classes)

def createMinor(self):
    return Minor(minor = testminor, required_classes = testrequired_classes)

def createStudentUser(self):
    new_User = StudentUser(grad_year = testgrad_year,
                           majors = teststudent_majors,
                           minors = teststudent_minors)
    new_User.student_classes.add(Section(location = "Nord 410",
                                         start_time = models.TimeField(auto_now=True, auto_now_add=True),
                                         end_time = models.TimeField(auto_now=True, auto_now_add=True),
                                         days_of_week = "MWF",
                                         course = Course(department = createDepartment(self),
                                                         course_number = 345,
                                                         course_name = "PLC")))


def createDepartment(self):
    return Department(department_Name = testdepartment_name, department_head = createProfessor(self), department_info = testdepartment_info, majors = testdepartment_majors, minors = testdepartment_minors)

def createProfessor(self):
    return Professor(first_name = testprofessor_first_name, last_name = testprofessor_last_name, email_id = testprofessor_email_id, bio = testprofessor_bio, current_department = createDepartment(self), classes=testprofessor_classes, office_Location = testoffice_location)

class ProfilesMethodTests(TestCase):
    def test_Major_str(self):
        testMajor = createMajor(self)
        self.assertEquals(testMajor.major, testMajor.__str__(self))

    def test_Minor_srt(self):
        test_Minor = createMinor(self)
        self.assertEquals(test_Minor.minor, test_Minor.__str__(self))

    def test_Student_str(self):
        testStudentUser = createStudentUser(self)
        self.assertEquals(testStudentUser.first_name + " " + testStudentUser.last_name, testStudentUser.__str__(self))


    def test_Department_str(self):
        testDepartment = createDepartment(self)
        self.assertEquals(testDepartment.department_name, testDepartment.__str__(self))

    def test_Professor_Constructor(self):
        testProfessor = createProfessor(self)
        self.assertEquals(testProfessor.first_name,testprofessor_first_name)
        self.assertEquals(testProfessor.last_name, testprofessor_last_name)
        self.assertEquals(testProfessor.email_id, testemail_id)
        self.assertEquals(testProfessor.bio,testbio)
        self.assertEquals(testProfessor.current_department,testprofessor_department)
        self.assertEquals(testProfessor.classes,testprofessor_classes)
        self.assertEquals(testProfessor.office_location, testoffice_location)
'''