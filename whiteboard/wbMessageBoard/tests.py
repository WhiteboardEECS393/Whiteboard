from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
from .models import DiscussionBoard
from .models import Thread
from .models import Post
from class_overviews.tests import createSection
from Profiles.models import StudentUser

def createDiscussionBoard(self):
    newBoard = DiscussionBoard(name="testBored",
                               description = "What this bored is all about",
                               course = createSection(self))
    return newBoard
def createThread(self):
    newThread = Thread(subject = "Dijkstra",
                       creator = StudentUser(user = User.objects.create_user(username='Daniel',
                                                         email='abc@case.edu',
                                                         password='password')),
                       message = "He is the supreme being",
                       time_of_creation = models.DateTimeField(auto_now=True,
                                                               auto_now_add=True),
                       board = createDiscussionBoard(self))
    return newThread
def createPost(self):
    newPost = Post(creator = StudentUser(user = User.objects.create_user(username='Danny',
                                                         email='abc@case.edu',
                                                         password='password')),
                   time_of_creation = models.DateTimeField(auto_now=True,
                                                           auto_now_add=True),
                   content = "Some type of content",
                   thread = createThread(self))
    return newPost

class wbMessageBoard(TestCase):
    def test_Discussion_Board_str(self):
        testBoard = createDiscussionBoard(self)
        self.assertEquals(testBoard.name, testBoard.__str__())

    def test_Thread_str(self):
        testThread = createThread(self)
        self.assertEquals(testThread.subject, testThread.__str__())

    def test_Post_str(self):
        testPost = createPost(self)
        self.assertEquals(testPost.thread.subject + ' ' + str(testPost.creator), testPost.__str__())
