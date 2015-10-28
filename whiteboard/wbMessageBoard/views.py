from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from .models import DiscussionBoard, Thread, Post
from .forms import BoardForm

# Create your views here.


def index(request):
    board_list = DiscussionBoard.objects.all()

    template = loader.get_template('wbMessageBoard/index.html')
    context = RequestContext(request, {
        'board_list': board_list,
    })
    return HttpResponse(template.render(context))


def boards(request, board_id):
    thread_list = Thread.objects.filter(board=board_id).order_by('-time_of_creation')

    template = loader.get_template('wbMessageBoard/board.html')
    context = RequestContext(request, {
        'thread_list': thread_list,
        'board': board_id,
    })
    return HttpResponse(template.render(context))


def create_board(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            new_board = DiscussionBoard(name=form.cleaned_data['thread_name'],
                                        description=form.cleaned_data['thread_description'])
            new_board.save()
            return HttpResponseRedirect('/boards/')
    else:
        form = BoardForm()
    return render(request, 'wbMessageBoard/create_board.html', {'form': form})


def thread(request, thread_id, start_post=None):
    if start_post is None:
        start_post = 0
    post_list = Post.objects.filter(thread=thread_id).order_by('time_of_creation')[start_post:start_post+10]
    current_thread = Thread.objects.filter(id=thread_id)
    context = {
        'post_list': post_list,
        'thread': current_thread,
    }
    return render(request, 'wbMessageBoard/thread.html', context)

