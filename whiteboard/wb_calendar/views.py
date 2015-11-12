from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
import json
from .models import Calendar, Event
from Profiles.models import StudentUser
from class_overviews.models import Course, Section


# Create your views here.

@login_required
def calendar(request, start_date=None, end_date=None):
    user = StudentUser.objects.get(user=request.user.id)
    if not user:
        return HttpResponseRedirect('/')
    calendar = Calendar.objects.get(owner=user)
    #if not calendar:
        #do something
    data = serializers.serialize('python', Event.objects.filter(calendar=calendar), fields=('title',
                                                                                            'start',
                                                                                            'end',
                                                                                            'allDay',
                                                                                            'recurring',
                                                                                            'dow'))
    fields = [d['fields'] for d in data]
    for f in fields:
        f['start'] = f['start'].isoformat()
        f['end'] = f['end'].isoformat()
        f['dow'] = getDOW(f['dow'])

    return HttpResponse(json.dumps(fields))


# Not sure if we'll need this, but it'll be for custom events
# def createEvent(request):
#     if request.method == 'POST':
#         user = StudentUser.objects.get(user=request.user.id)
#         if not user:
#             return HttpResponseRedirect('/')
#         calendar = Calendar.objects.get(owner=user)

@login_required
def importClasses(request):
    user = StudentUser.objects.get(user=request.user.id)
    if not user:
        return HttpResponseRedirect('/')
    calendar = Calendar.objects.get(owner=user)
    classes = user.student_classes.all()
    for c in classes:
        #course = Course.objects.get(pk=c.course)
        saveEvent(title=c.course.course_name + ' ' +str(c.course.course_number), description=c.section_number,
                  calendar=calendar, start=c.start_time, end=c.end_time, allDay=False, recurring=True,
                  dow=c.days_of_week)
    return HttpResponseRedirect('/')



def saveEvent(title, description, calendar, start, end, allDay, recurring, dow):
    event = Event(title=title, description=description, calendar=calendar, start=start,
                  end=end, allDay=allDay, recurring=recurring,
                  dow=dow)
    event.save()


def getDOW(dowString):
    dow = []
    if 'M' in dowString:
        dow.append(1)
    if 'T' in dowString:
        dow.append(2)
    if 'W' in dowString:
        dow.append(3)
    if 'R' in dowString:
        dow.append(4)
    if 'F' in dowString:
        dow.append(5)
    if 'S' in dowString:
        dow.append(6)
    if 'U' in dowString:
        dow.append(7)
    return dow
