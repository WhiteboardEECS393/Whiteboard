from django.test import TestCase
from .models import DiscussionBoard
from .models import Thread
from .models import Post
from class_overviews.tests import createCourse
from Profiles.tests import createStudentUser
from django.db import models

#Needed for testing DicsussionBoard
global testname
testname = 'Board name'
global testdescription
testdescription = 'The board can be described as...'
#Needed for testing Thread
global testsubject
testsubject = 'Thread subject'
global testcreator
testcreator = 'Daniel'
global testmessage
testmessage = 'We come in peace'
global testtime_of_creation
testtime_of_creation = models.timezone.now()
#Needed for testing Post
global testcontent
testcontent = 'Some content'

def createDiscussionBoard(self):
    return DiscussionBoard(name = testname, description = testdescription, course = createcourse)

def createThread(self):
    return Thread(subject = testsubject, creator = createStudentUser(self), message = testmessage, time_of_creation = testtime_of_creation, board = createDiscussionBoard())

def createPost(self):
    return Post(creator = createStudentUser(self), time_of_creation = testtime_of_creation, content = testcontent, thread = createThread(self))

class wbMessageBoard(TestCase):

    def test_Discussion_Board(self):
        testdiscussionboard = createDiscussionBoard(self)
        self.assertEquals(testdiscussionboard.name,testname)
        self.assertEquals(testdiscussionboard.description, testdescription)
        self.assertEquals(testdiscussionboard.course, createCourse(self))

    def test_Thread(self):
        testThread = createThread(self)
        self.assertEquals(testThread.subject,testsubject)
        self.assertEquals(testThread.creator, createStudentUser(self))
        self.assertEquals(testThread.message, testmessage)
        self.assertEquals(testThread.time_of_creation,testtime_of_creation)
        self.assertEquals(testThread.board,createDiscussionBoard(self))