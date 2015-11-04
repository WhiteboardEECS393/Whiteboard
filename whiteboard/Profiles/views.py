from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import StudentUser, Professor
from django.contrib.auth.decorators import login_required


def profile(request, first, last, student_id):
    template = 'Profiles/userprofile.html'
    student_list = StudentUser.objects.filter(pk=student_id)

    if len(student_list) != 1:
        template = 'Profiles/usernotfound.html'
        context = RequestContext(request,)
    else:
        student = student_list[0]
        current_user = StudentUser.objects.filter(user=request.user.id)[0]
        context = RequestContext(request, {
            'current_user': current_user,
            'student': student,
        })
    return render_to_response(template, locals(), context)
