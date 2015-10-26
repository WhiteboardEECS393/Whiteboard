from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import BasicUser, StudentUser, ProfessorUser


def index(request):
    student_profile_list = StudentUser.objects.all()
    professor_profile_list = ProfessorUser.objects.all()

    # template = loader.get_template('Profiles/index.html')
    template = loader.get_template('Profiles/classpage.html')
    context = RequestContext(request, {
        'student_profile_list': student_profile_list,
        'professor_profile_list': professor_profile_list,
    })
    return HttpResponse(template.render(context))
