from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/', views.create_board, name='create broad'),
    url(r'^(?P<board_id>[0-9]+)/$', views.boards, name='board'),
    url(r'^(?P<board_id>[0-9]+)/create/$', views.create_thread, name='create thread'),
    url(r'^thread/(?P<thread_id>[0-9]+)/$', views.thread, name='view thread'),
    url(r'^thread/(?P<thread_id>[0-9]+)/create/$', views.create_post, name='Reply to thread'),
    url(r'^thread/(?P<thread_id>[0-9]+)\?start=(?P<start_post>[0-9]+)/$', views.thread),
]


