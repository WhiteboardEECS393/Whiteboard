from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<depart>[A-Z]+)(?P<course_num>[0-9]+)/(?P<section_num>[0-9]+)/upload_document$', views.upload_document, name='upload_document'),
    url(r'^(?P<depart>[A-Z]+)(?P<course_num>[0-9]+)/$', views.courseDetail, name='courseDetail'),
    url(r'^(?P<depart>[A-Z]+)(?P<course_num>[0-9]+)/(?P<section_num>[0-9]+)$', views.courseDetail, name='courseDetail'),
    url(r'^(?P<depart>[A-Z]+)(?P<course_num>[0-9]+)/(?P<section_num>[0-9]+)/$', views.courseDetail, name='courseDetail'),
    url(r'^(?P<depart>[A-Z]+)(?P<course_num>[0-9]+)/(?P<sea>[a-zA-Z]+)(?P<yr>[0-9]+)$', views.courseDetail, name='courseDetail'),
    url(r'^(?P<depart>[A-Z]+)(?P<course_num>[0-9]+)/(?P<sea>[a-zA-Z]+)(?P<yr>[0-9]+)/(?P<section_num>[0-9]+)$', views.courseDetail, name='courseDetail'),
]
