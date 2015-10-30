from django.test import TestCase
from .models import Course
from .models import Section
from .models import Document

#Needed for testing course
global testdepartment
testdepartment = 'EECS'
global testcourse_number
testcourse_Number =393
global testcourse_name
testcourse_Name ='EECS 393 Software Engineering'
global testdescription
#Needed for testing Section
testdescription = 'A class about software engineering'
global testprofessor
testprofessor = 'Andy Podgurski'
global testseason
testseason = 'Fall'
global testyear
testyear = 2015
global testteachingassitants
testteachingassitants = 'Mutliple'
global testlocation
testlocation = 'Nord 400'
global testtime_of_day
testtime_of_day = '11:30-12:20'
global testdays_of_week
testdays_of_week = 'MWF'
global testsection_number
testsection_number = 1234
#Needed for testing Document
global testdocument_name
testdocument_name = 'SRS Example'
global testpath
testpath = 'C://MyComputer/Somewhere'
global testdocument_description
testdocument_description = 'An example of an SRS document'


def createCourse(self):
        return Course(department=testdepartment,course_number=testcourse_number, course_name=testcourse_name,description=testdescription)

def createSection(self):
    return Section(professor_name = testprofessor, season = testseason, year = testyear, teaching_assistants = testteachingassitants, location = testlocation, time_of_day = testtime_of_day, days_of_week = testdays_of_week, section_number = testsection_number, course = createCourse(self))

def createDocument(self):
    return Document(name = testdocument_name, path = testpath, description = testdocument_description, course_section = createSection(self))

class ClassOverViewsMethodTests(TestCase):

    def test_Course_Constructor(self):
        testcourse = createCourse(self)
        self.assertEquals(testcourse.department,testdepartment)
        self.assertEquals(testcourse.course_number, testcourse_number)
        self.assertEquals(testcourse.course_name, testcourse_name)
        self.assertEquals(testcourse.description,testdescription)

    def test_Section_Constructor(self):
        testcourse = createCourse(self)
        testsection = createSection(self)
        self.assertEquals(testsection.professor_name,testprofessor)
        self.assertEquals(testsection.season, testseason)
        self.assertEquals(testsection.year, testyear)
        self.assertEquals(testsection.teaching_assistants,testteachingassitants)
        self.assertEquals(testsection.location,testlocation)
        self.assertEquals(testsection.time_of_day, testtime_of_day)
        self.assertEquals(testsection.days_of_week, testdays_of_week)
        self.assertEquals(testsection.section_number,testsection_number)
        self.assertEquals(testsection.course,testcourse)

    def test_Document_Constructor(self):
        testsection = createSection(self)
        testDocument = createDocument(self)
        self.assertEquals(testDocument.name, testdocument_name)
        self.assertEquals(testDocument.path, testpath)
        self.assertEquals(testDocument.description,testdocument_description)
        self.assertEquals(testDocument.course_section,testsection)