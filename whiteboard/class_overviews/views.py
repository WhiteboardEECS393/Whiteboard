from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Course, Section, Document
from django.db.models.query import QuerySet


def course(request):
    return HttpResponse("Hello, world. You're at the course homepage.")


def courseDetail(request, depart, course_num, sea="Fall", yr=2015, section_num=0):

    template = 'class_overviews/course.html'
    c = Course.objects.filter(department = depart, course_number=course_num)
    if len(c) == 0:
        template = 'class_overviews/classnotfoundpage.html'
        context = RequestContext(request,)
        return render_to_response(template, locals(), context)
    else:
        c = c[0]

    s = Section.objects.filter(course = c, season = sea, year = yr)
    if len(s) == 0:
        template = 'class_overviews/classnotfoundpage.html'
        context = RequestContext(request,)
        return render_to_response(template, locals(), context)
    else:
        s = s[0]
        #later add the check for most recent class

    documents = Document.objects.filter(course_section = s)

    context = RequestContext(request, {
        'course': c,
        'section' : s,
        'documents' : documents
    })
    return render_to_response(template, locals(), context)

