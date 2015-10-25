from django.http import HttpResponse


def index(request):
    return HttpResponse("This test is kinda strange.")
