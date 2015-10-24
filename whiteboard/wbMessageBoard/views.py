from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import DiscussionBoard, Thread

# Create your views here.

def index(request):
    board_list = DiscussionBoard.objects.all()

    template = loader.get_template('wbMessageBoard/index.html')
    context = RequestContext(request, {
        'board_list': board_list,
    })
    return HttpResponse(template.render(context))

def boards(request, board_id):
    #current_board = DiscussionBoard.objects.get(pk=board_id)
    thread_list = Thread.objects.filter(board = board_id).order_by('-time_of_creation')

    template = loader.get_template('wbMessageBoard/board.html')
    context = RequestContext(request, {
        'thread_list': thread_list,
        'board': board_id,
    })
    return HttpResponse(template.render(context))