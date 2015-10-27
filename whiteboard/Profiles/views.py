from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import StudentUser, Professor, TeachingAssistantUser


def index(request):
    student_profile_list = StudentUser.objects.all()
    professor_profile_list = Professor.objects.all()
    teaching_assistant_profile_list = TeachingAssistantUser.objects.all()

    template = 'Profiles/index.html'
    context = RequestContext(request, {
        'student_profile_list': student_profile_list,
        'professor_profile_list': professor_profile_list,
        'teaching_assistant_profile_list': teaching_assistant_profile_list,
    })
    return render_to_response(template, locals(), context)


def profile(request):
    template = 'Profiles/Profile.html'
    context = RequestContext(request, )
    return render_to_response(template, locals(), context)


def classes(request):

    template = 'Profiles/EECS393.html'
    context = RequestContext(request, )
    return render_to_response(template, locals(), context)


def classestwo(request):

    template = 'Profiles/EECS325.html'
    context = RequestContext(request, )
    return render_to_response(template, locals(), context)