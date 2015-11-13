from django.test import TestCase
from django.contrib.auth.models import User
from .models import Major
from .models import Minor
from .models import StudentUser
from .models import Department
from .models import Professor

def createMajor(self):
    newMajor = Major(major = "Computer Science")
    return newMajor
def createMinor(self):
    newMinor = Minor(minor = "Game Design")
    return newMinor
def createStudentUser(self):
    newStudent = StudentUser(user = User.objects.create_user(username='Daniel',
                                                         email='abc@case.edu',
                                                         password='password'))
    return  newStudent
def createDepartment(self):
    newdepartment = Department(department_code = "EECS",
                               department_name = "Electrical Engineering and Computer Science",
                               department_info = "Stuff about the department")
    return newdepartment
def createProfessor(self):
    newProfessor = Professor(first_name = "Tekin",
                             last_name = "Osoy....glu",
                             email_id = "abc@case.edu",
                             bio = "Something or the other",
                             office_location = "Where the sun don't shine")
    return newProfessor

class ProfilesMethodTests(TestCase):
    def test_Major_str(self):
        testMajor = createMajor(self)
        self.assertEquals(testMajor.major, testMajor.__str__())

    def test_Minor_str(self):
        test_Minor = createMinor(self)
        self.assertEquals(test_Minor.minor, test_Minor.__str__())

    def test_Student_str(self):
        testStudentUser = createStudentUser(self)
        self.assertEquals(testStudentUser.first_name + " " + testStudentUser.last_name, testStudentUser.__str__())

    def test_Department_str(self):
        testDepartment = createDepartment(self)
        self.assertEquals(testDepartment.department_name, testDepartment.__str__())

    def test_Professor_str(self):
        testProfessor = createProfessor(self)
        self.assertEquals(testProfessor.first_name + " " + testProfessor.last_name, testProfessor.__str__())