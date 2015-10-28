from django.shortcuts import render_to_response, render
from django.template import RequestContext
from Profiles.models import StudentUser, Professor, TeachingAssistantUser
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from .forms import LoginForm, CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


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
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/MyProfile/')
            else:
                return HttpResponse('Your User is not active.')
    return render(request, 'Profiles/userloginpage.html', {'login_form': form})


def create_new_user(request,):
    form = CreateUserForm(request.POST or None)
    if request.POST and form.is_valid():
            user = form.create_new_user(request)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    '''
                    if tabool:
                        return HttpResponseRedirect('../create_ta/')
                    else:
                        return HttpResponseRedirect('../create_student/')
                    '''
                    return HttpResponseRedirect('../MyProfile/')
                else:
                    return HttpResponse('Your User is not active.')
    return render(request, 'Profiles/createuser.html', {'create_user_form': form})


def create_student(request, ):
    return HttpResponse('created student')
