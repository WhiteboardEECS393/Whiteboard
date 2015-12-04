from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^(?P<first>[A-Za-z]+)(?P<last>[A-Za-z]+)/(?P<student_id>[0-9]+)/edit', views.edit_profile, name='edit_profile'),
        url(r'^(?P<first>[A-Za-z]+)(?P<last>[A-Za-z]+)/(?P<student_id>[0-9]+)/image_upload', views.edit_picture, name='edit_picture'),
        url(r'^(?P<first>[A-Za-z]+)(?P<last>[A-Za-z]+)/(?P<student_id>[0-9]+)/all', views.all_classes, name='all classes'),
        url(r'^(?P<first>[A-Za-z]+)(?P<last>[A-Za-z]+)/(?P<student_id>[0-9]+)', views.profile, name='profile'),
        url(r'^Professor/(?P<first>[A-Za-z]+)/(?P<last>[A-Za-z]+)', views.professorProfile, name='professorProfile'),
        url(r'^Professor/', views.professor_index, name='Professor Index'),
        url(r'^Department/(?P<code>[A-Za-z]+)', views.departmentProfile, name='departmentProfile'),
        url(r'^Department/', views.department_index, name='Department Index'),
        url(r'^Student/', views.student_index, name='Student Index'),
        ]
