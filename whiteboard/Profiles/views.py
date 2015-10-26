from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from .models import BasicUser, StudentUser, ProfessorUser


def index(request):
    student_profile_list = StudentUser.objects.all()
    professor_profile_list = ProfessorUser.objects.all()

    # template = loader.get_template('Profiles/index.html')
    template = 'Profiles/index.html'
    context = RequestContext(request, {
        'student_profile_list': student_profile_list,
        'professor_profile_list': professor_profile_list,
    })
    return render_to_response(template, locals(), context)
