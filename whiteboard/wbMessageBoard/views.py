from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from Profiles.models import StudentUser
from .models import DiscussionBoard, Thread, Post
from .forms import BoardForm, ThreadForm, ReplyForm


# Create your views here.


@login_required
def index(request):
    board_list = DiscussionBoard.objects.all()

    template = loader.get_template('wbMessageBoard/index.html')
    context = RequestContext(request, {
        'board_list': board_list,
    })
    return HttpResponse(template.render(context))


@login_required
def boards(request, board_id):
    thread_list = Thread.objects.filter(board=board_id).order_by('-time_of_creation')

    template = loader.get_template('wbMessageBoard/board.html')
    context = RequestContext(request, {
        'thread_list': thread_list,
        'board': board_id,
    })
    return HttpResponse(template.render(context))


@login_required
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


@login_required
def thread(request, thread_id, start_post=None):
    user = StudentUser.objects.get(user=request.user.id)
    if not user:
        return HttpResponseRedirect('/')
    if start_post is None:
        start_post = 0
    post_list = Post.objects.filter(thread=thread_id).order_by('time_of_creation')
    current_thread = Thread.objects.filter(id=thread_id)[0]
    context = {
        'post_list': post_list,
        'thread': current_thread,
        'curr_user': user,
    }
    return render(request, 'wbMessageBoard/postedthread.html', context)


@login_required
def create_thread(request, board_id):
    user = StudentUser.objects.get(user=request.user.id)
    curr_user_classes = StudentUser.getCurrentClasses(user)
    if not user:
        return HttpResponseRedirect('/')
    board = DiscussionBoard.objects.get(id=board_id)
    if request.method == 'POST':

        form = ThreadForm(request.POST)
        if form.is_valid():
            new_thread = Thread(subject=form.cleaned_data['thread_subject'],
                                message=form.cleaned_data['thread_message'],
                                time_of_creation=timezone.localtime(timezone.now()),
                                creator=user,
                                board=DiscussionBoard.objects.filter(id=board_id)[0], )
            new_thread.save()
            return HttpResponseRedirect('/course/' + board.course.course.department
                                        + str(board.course.course.course_number) + '/'
                                        + str(board.course.section_number))
    else:
        form = ThreadForm()
    return render(request, 'wbMessageBoard/createpost.html', {'form': form,
                                                              'board': board,
                                                              'curr_user': user,
                                                              'curr_user_classes': curr_user_classes,
                                                              })


@login_required
def create_post(request, thread_id):
    user = StudentUser.objects.get(user=request.user.id)
    curr_user_classes = StudentUser.getCurrentClasses(user)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            new_post = Post(content=form.cleaned_data['reply_message'],
                            time_of_creation=timezone.localtime(timezone.now()),
                            creator=user,
                            thread=Thread.objects.filter(id=thread_id)[0], )
            new_post.save()
            return HttpResponseRedirect('/boards/thread/' + thread_id)
    else:
        form = ReplyForm()
    return render(request, 'wbMessageBoard/create_reply.html', {'form': form, 'thread_id': thread_id, 'user': user,
                                                                'curr_user': user,
                                                                'curr_user_classes': curr_user_classes,
                                                                })
