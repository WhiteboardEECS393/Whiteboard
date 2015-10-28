from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/$', views.course, name='course'),
    url(r'^(?P<depart>[A-Z]+)(?P<course_num>[0-9]+)/$', views.courseDetail, name='courseDetail'),
    url(r'^(?P<depart>[A-Z]+)(?P<course_num>[0-9]+)/(?P<section_num>[0-9]+)$', views.courseSectionDetail, name='courseSectionDetail'),
    url(r'^(?P<depart>[A-Z]+)(?P<course_num>[0-9]+)/(?P<sea>[a-zA-Z]+)(?P<yr>[0-9]+)$', views.courseSemesterDetail, name='courseSemesterDetail'),
    url(r'^(?P<depart>[A-Z]+)(?P<course_num>[0-9]+)/(?P<sea>[a-zA-Z]+)(?P<yr>[0-9]+)/(?P<section_num>[0-9]+)$', views.courseSemesterSectionDetail, name='courseSemesterSectionDetail'),
]
