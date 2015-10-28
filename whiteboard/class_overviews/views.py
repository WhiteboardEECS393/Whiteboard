from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Course, Section, Document
from django.db.models.query import QuerySet


def course(request):
    return HttpResponse("Hello, world. You're at the course homepage.")

def courseDetail(request, depart, course_num):
    #return course with the most recent year and season. if there are multiple in that semester. return first

    template = 'class_overviews/course.html'
    c = Course.objects.filter(department = depart, course_number=course_num)
    if len(c) == 0:
        template = '' #later add template for error 404
        context = RequestContext(request,)
        #return render_to_response(template, locals(), context)
        return HttpResponse("We could not find the course %s%s." % (depart, course_num))
    else:
        c = c[0]

    section = Section.objects.filter(course = c)
    if len(section) == 0:
        template = '' #later add template for error 404
        context = RequestContext(request,)
        #return render_to_response(template, locals(), context)
        return HttpResponse("We could not find the course %s%s." % (depart, course_num))
    else:
        section = section[0]
        #later add the check for most recent class

    context = RequestContext(request, {
        'course': c,
        'section' : section,
    })
    return render_to_response(template, locals(), context)


def courseSectionDetail(request, depart, course_num, section_num):
    #return course that matches this data with the most recent semester

    template = 'class_overviews/course.html'
    c = Course.objects.filter(department = depart, course_number=course_num)
    if len(c) == 0:
        template = '' #later add template for error 404
        context = RequestContext(request,)
        #return render_to_response(template, locals(), context)
        return HttpResponse("We could not find the course %s%s." % (depart, course_num))
    else:
        c = c[0]

    section = Section.objects.filter(course = c, section_number = section_num)
    if len(section) == 0:
        template = '' #later add template for error 404
        context = RequestContext(request,)
        #return render_to_response(template, locals(), context)
        return HttpResponse("We could not find the course %s%s." % (depart, course_num))
    else:
        section = section[0]
        #later add the check for most recent class

    context = RequestContext(request, {
        'course': c,
        'section' : section,
    })
    return render_to_response(template, locals(), context)


def courseSemesterDetail(request, depart, course_num, sea, yr):
    #return course that matches this data, if there is more than one, return first

    template = 'class_overviews/course.html'
    c = Course.objects.filter(department = depart, course_number=course_num)
    if len(c) == 0:
        template = '' #later add template for error 404
        context = RequestContext(request,)
        #return render_to_response(template, locals(), context)
        return HttpResponse("We could not find the course %s%s." % (depart, course_num))
    else:
        c = c[0]

    section = Section.objects.filter(course = c, season = sea, year = yr)
    if len(section) == 0:
        template = '' #later add template for error 404
        context = RequestContext(request,)
        #return render_to_response(template, locals(), context)
        return HttpResponse("We could not find the course %s%s." % (depart, course_num))
    else:
        section = section[0]
        #later add the check for most recent class

    context = RequestContext(request, {
        'course': c,
        'section' : section,
    })
    return render_to_response(template, locals(), context)


def courseSemesterSectionDetail(request, depart, course_num, sea, yr, section_num):
    #return course that matches this data

    template = 'class_overviews/course.html'
    c = Course.objects.filter(department = depart, course_number=course_num)
    if len(c) == 0:
        template = '' #later add template for error 404
        context = RequestContext(request,)
        #return render_to_response(template, locals(), context)
        return HttpResponse("We could not find the course %s%s." % (depart, course_num))
    else:
        c = c[0]

    section = Section.objects.filter(course = c, season = sea, year = yr)
    if len(section) == 0:
        template = '' #later add template for error 404
        context = RequestContext(request,)
        #return render_to_response(template, locals(), context)
        return HttpResponse("We could not find the course %s%s." % (depart, course_num))
    else:
        section = section[0]
        #later add the check for most recent class

    context = RequestContext(request, {
        'course': c,
        'section' : section,
    })
    return render_to_response(template, locals(), context)

