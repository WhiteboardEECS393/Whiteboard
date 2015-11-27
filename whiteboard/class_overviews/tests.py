from django.test import TestCase
from django.db import models
from .models import Course
from .models import Semester
from .models import Section
from .models import Document

def createSemester(self):
    testSemester = Semester(startDate = models.DateTimeField(auto_now=True,
                                                             auto_now_add=True),
                            endDate = models.DateTimeField(auto_now=True,
                                                           auto_now_add=True))
    return testSemester
def createCourse(self):
    newCourse = Course(department = "EECS",
                       course_number = 338,
                       course_name = "Operating Systems")
    return newCourse
def createSection(self):
    newSection = Section(location = "Degrace",
                         days_of_week = "MW",
                         course = createCourse(self),
                         semester = createSemester(self))
    return newSection


class ClassOverViewTests(TestCase):
    def test_Semester(self):
        testSemester = createSemester(self)
        self.assertEquals(testSemester.season + " " + str(testSemester.year),
                          testSemester.__str__())

    def test_Course_str(self):
        testCourse = createCourse(self)
        self.assertEquals(testCourse.department + str(testCourse.course_number) + ": " + testCourse.course_name,
                          testCourse.__str__())

    def test_Section_str(self):
        testSection = createSection(self)
        self.assertEquals(str(testSection.course) + " (" + str(testSection.section_number)+") " + testSection.semester.season + str(testSection.semester.year),
                          testSection.__str__())

    def test_Document_str(self):
        testDocument = Document(name = "Syllabus",
                                path = "Through the woods",
                                course_section = createSection(self))
        self.assertEquals(testDocument.name, testDocument.__str__())