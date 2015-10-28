from django.shortcuts import render_to_response
from django.template import RequestContext
from Profiles.models import StudentUser, Professor, TeachingAssistantUser
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login


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


def main_redirect(request,):
    context = RequestContext(request,)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/MyProfile/')
            else:
                return HttpResponse('Your User is not active.')
        else:
            return HttpResponseRedirect('/login_retry/')
    else:
        return render_to_response('Profiles/userloginpage.html', {}, context)


def failed_login_redirect(request,):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/MyProfile/')
            else:
                return HttpResponse('Your User is not active.')
        else:
            return HttpResponseRedirect('/login_retry/')
    else:
        return render_to_response('Profiles/userloginfailedpage.html', {}, context)


def create_new_user(request,):
    context = RequestContext(request,)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirmpass']

        if password == confirm_password and authenticate(username=username, password=password) is None:
            User.objects.create_user(username=username, password=password)
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/MyProfile/')
            else:
                return HttpResponse('Your User is not active.')
        else:
            return HttpResponse('passwords do not match')
            # return HttpResponseRedirect('/login_retry/')
    else:
        return render_to_response('Profiles/createuser.html/', {}, context)
