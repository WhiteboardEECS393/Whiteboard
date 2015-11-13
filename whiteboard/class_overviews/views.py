from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Course, Section, Document
from wbMessageBoard.models import DiscussionBoard, Thread
from Profiles.models import StudentUser, Professor
from django.contrib.auth.decorators import login_required


@login_required
def courseDetail(request, depart, course_num, sea="", yr=2015, section_num=0):

    template = 'class_overviews/course.html'
    c = Course.objects.filter(department = depart, course_number=course_num)
    if len(c) == 0:
        template = 'class_overviews/classnotfoundpage.html'
        context = RequestContext(request,)
        return render_to_response(template, locals(), context)
    else:
        c = c[0]

    if section_num == 0 and sea == "":
        s = Section.objects.filter(course = c)
    elif section_num != 0:
        s = Section.objects.filter(course = c, section_number = section_num)
    elif sea != "":
        s = Section.objects.filter(course = c, season = sea, year = yr)
    else:
        s = Section.objects.filter(course = c, season = sea, year = yr, section_number = section_num)

    if len(s) == 0:
        template = 'class_overviews/classnotfoundpage.html'
        context = RequestContext(request,)
        return render_to_response(template, locals(), context)
    else:
        s = s[0]

    sections = Section.objects.filter(course = c)

    documents = Document.objects.filter(course_section = s)

    b = DiscussionBoard.objects.filter(course = s)
    if len(b):
        threads = Thread.objects.filter(board = b)
    else:
        threads =   []

    students = s.studentuser_student.all()
    tas = s.studentuser_ta.all()

    user = StudentUser.objects.filter(user=request.user)[0]
    curr_classes = StudentUser.getCurrentClasses(user)

    professor = s.professor_set.all()[0]

    context = RequestContext(request, {
        'course': c,
        'section' : s,
        'sections' : sections,
        'documents' : documents,
        'threads' : threads,
        'board_id': b[0].id,
        'students' : students,
        'teaching_assistants' : tas,
        'curr_user' : user,
        'curr_user_classes' : curr_classes,
        'professor' : professor,
    })
    return render_to_response(template, locals(), context)


@login_required
def getThreads(s):
    b = DiscussionBoard.objects.filter(course = s)

    threads = Thread.objects.filter(board = b)
    return threads

