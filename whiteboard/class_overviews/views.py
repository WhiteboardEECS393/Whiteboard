from django.shortcuts import render
from django.http import HttpResponse


def course(request):
    return HttpResponse("Hello, world. You're at the course homepage.")

def courseDetail(request, department, course_number):
    return HttpResponse("You're looking at the course %s%s." % (department, course_number))

def courseSectionDetail(request, department, course_number, section_number):
    return HttpResponse("You're looking at the course %s%s %s." % (department, course_number, section_number))

def courseSemesterDetail(request, department, course_number, season, year):
    return HttpResponse("You're looking at the course %s%s %s%s." % (department, course_number, season, year))

def courseSemesterSectionDetail(request, department, course_number, season, year, section_number):
    return HttpResponse("You're looking at the course %s%s %s%s %s." % (department, course_number, season, year, section_number))