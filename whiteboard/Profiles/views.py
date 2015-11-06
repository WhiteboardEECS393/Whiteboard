from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from .models import StudentUser, Professor
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


@login_required
def profile(request, first, last, student_id):
    template = 'Profiles/userprofile.html'
    student_list = StudentUser.objects.filter(pk=student_id)
    if len(student_list) != 1:
        template = 'Profiles/usernotfound.html'
        context = RequestContext(request,)
    else:
        student = student_list[0]
        current_user = StudentUser.objects.filter(user=request.user.id)[0]
        threads = current_user.thread_set.all()
        context = RequestContext(request, {
            'current_user': current_user,
            'student': student,
            'threads': threads,
        })
    return render_to_response(template, locals(), context)

@login_required
def edit_profile(request, first, last, student_id):
    template = 'Profiles/editprofile.html'
    student_list = StudentUser.objects.filter(pk=student_id)
    current_user = StudentUser.objects.filter(user=request.user.id)[0]
    if len(student_list) != 1:
        template = 'Profiles/usernotfound.html'
        context = RequestContext(request,)
    elif student_list[0] != current_user:
        return HttpResponseRedirect(reverse('profile', kwargs={'first':first, 'last': last, 'student_id': student_id}))
    else:
        threads = current_user.thread_set.all()
        context = RequestContext(request, {
            'student': current_user,
            'threads': threads,
        })
    return render_to_response(template, locals(), context)