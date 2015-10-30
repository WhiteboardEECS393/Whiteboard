from django.test import TestCase
from .models import BasicUser
from .models import Major
from .models import Minor
from .models import StudentUser
from .models import Department
from .models import TeachingAssistantUser
from .models import Professor

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
global testrequired_classes
testrequired_classes = 'Required classes'
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
global teststudent_classes
teststudent_classes = 'Networks, Stats, Software Engineering, Sociology'
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


def createBasicUuser(self):
    return BasicUser(first_name = testfirst_name, last_name = testlast_name, email_id = testemail_id, bio = testbio, photo = testphoto)

def createMajor(self):
    return Major(major = testmajor, required_classes = testrequired_classes)

def createMinor(self):
    return Minor(minor = testminor, required_classes = testrequired_classes)

def createStudentUser(self):
    return StudentUser(grad_year = testgrad_year, majors = teststudent_majors, minors = teststudent_minors, classes = teststudent_classes)

def createDepartment(self):
    return Department(department_Name = testdepartment_name, department_head = createProfessor(self), department_info = testdepartment_info, majors = testdepartment_majors, minors = testdepartment_minors)

def createTeachingAssisstant(self):
    return TeachingAssistantUser(teaching_classes = testteaching_classes, department = createDepartment(self))

def createProfessor(self):
    return Professor(first_name = testprofessor_first_name, last_name = testprofessor_last_name, email_id = testprofessor_email_id, bio = testprofessor_bio, current_department = createDepartment(self), classes=testprofessor_classes, office_Location = testoffice_location)

class ProfilesMethodTest(TestCase):

    def test_Basic_User_Constructor(self):
        testBasicUser = createBasicUuser(self)
        self.assertEquals(testBasicUser.first_name,testfirst_name)
        self.assertEquals(testBasicUser.last_name, testlast_name)
        self.assertEquals(testBasicUser.email_id, testemail_id)
        self.assertEquals(testBasicUser.bio,testbio)
        self.assertEquals(testBasicUser.photo,testphoto)

    def test_Major_Constructor(self):
        testMajor = createMajor(self)
        self.assertEquals(testMajor.required_classes,testrequired_classes)
        self.assertEquals(testMajor.major, testmajor)

    def test_Minor_Constructor(self):
        testMinor = createMinor(self)
        self.assertEquals(testMinor.required_classes,testrequired_classes)
        self.assertEquals(testMinor.minor, testminor)

    def test_Student_User_Constructor(self):
        testStudentUser = createStudentUser(self)
        self.assertEquals(testStudentUser.grad_year,testgrad_year)
        self.assertEquals(testStudentUser.majors, teststudent_majors)
        self.assertEquals(testStudentUser.minors, teststudent_minors)
        self.assertEquals(testStudentUser.classes,teststudent_classes)

    def test_Department_Constructor(self):
        testDepartment = createDepartment(self)
        self.assertEquals(testDepartment.department_name,testdepartment_name)
        self.assertEquals(testDepartment.department_head, testdepartment_head)
        self.assertEquals(testDepartment.department_info, testdepartment_info)
        self.assertEquals(testDepartment.majors,testdepartment_majors)
        self.assertEquals(testDepartment.minors,testdepartment_minors)

    def test_Teaching_Assisstant_User_Constructor(self):
        testTeachingAssisstant = createTeachingAssisstant(self)
        self.assertEquals(testTeachingAssisstant.teaching_classes,testteaching_classes)
        self.assertEquals(testTeachingAssisstant.department, testassistant_department)

    def test_Professor_Constructor(self):
        testProfessor = createProfessor(self)
        self.assertEquals(testProfessor.first_name,testprofessor_first_name)
        self.assertEquals(testProfessor.last_name, testprofessor_last_name)
        self.assertEquals(testProfessor.email_id, testemail_id)
        self.assertEquals(testProfessor.bio,testbio)
        self.assertEquals(testProfessor.current_department,testprofessor_department)
        self.assertEquals(testProfessor.classes,testprofessor_classes)
        self.assertEquals(testProfessor.office_location, testoffice_location)
