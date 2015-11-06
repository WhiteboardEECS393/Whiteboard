from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^(?P<first>[A-Za-z]+)(?P<last>[A-Za-z]+)/(?P<student_id>[0-9]+)/edit', views.edit_profile, name='edit_profile'),
        url(r'^(?P<first>[A-Za-z]+)(?P<last>[A-Za-z]+)/(?P<student_id>[0-9]+)', views.profile, name='profile'),
        ]
