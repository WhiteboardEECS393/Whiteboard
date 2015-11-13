from django.test import TestCase
from .models import Course
from .models import Section
from .models import Document

def createCourse(self):
    newCourse = Course(department = "EECS",
                       course_number = 338,
                       course_name = "Operating Systems")
    return newCourse
def createSection(self):
    newSection = Section(location = "Degrace",
                         days_of_week = "MW",
                         course = createCourse(self))
    return newSection


class ClassOverViewTests(TestCase):
    def test_Course_str(self):
        testCourse = createCourse(self)
        self.assertEquals(testCourse.department + str(testCourse.course_number) + ": " + testCourse.course_name,
                          testCourse.__str__())

    def test_Section_str(self):
        testSection = createSection(self)
        self.assertEquals(str(testSection.course) + " (" + str(testSection.section_number)+") " + testSection.season + str(testSection.year),
                          testSection.__str__())

    def test_Document_str(self):
        testDocument = Document(name = "Syllabus",
                                path = "Through the woods",
                                course_section = createSection(self))
        self.assertEquals(testDocument.name, testDocument.__str__())