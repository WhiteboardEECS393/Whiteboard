from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import StudentUser, Professor, TeachingAssistantUser


def profile(request):
    template = 'Profiles/Profile.html'
    current_user = StudentUser.objects.filter(user=request.user.id)[0]
    context = RequestContext(request, {
        'current_user': current_user,
    })
    return render_to_response(template, locals(), context)


def classes(request):
    template = 'Profiles/EECS393.html'
    context = RequestContext(request,)
    return render_to_response(template, locals(), context)


def classestwo(request):

    template = 'Profiles/EECS325.html'
    context = RequestContext(request, )
    return render_to_response(template, locals(), context)
