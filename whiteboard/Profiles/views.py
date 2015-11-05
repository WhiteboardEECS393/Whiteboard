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
        classes = student.student_classes.all()

        user = StudentUser.objects.filter(user=request.user)[0]
        curr_user_classes = StudentUser.getCurrentClasses(student)
        majors = student.majors.all()
        minors = student.minors.all()

        context = RequestContext(request, {
            'student': student,
            'classes' : classes,
            'curr_user' : user,
            'curr_user_classes' : curr_user_classes,
            'majors' : majors,
            'minors' : minors,
        })
    return render_to_response(template, locals(), context)
