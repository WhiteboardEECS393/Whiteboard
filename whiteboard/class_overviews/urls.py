from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/$', views.course, name='course'),
    url(r'^(?P<department>[A-Z]+)(?P<course_number>[0-9]+)/$', views.courseDetail, name='courseDetail'),
    url(r'^(?P<department>[A-Z]+)(?P<course_number>[0-9]+)/(?P<section_number>[0-9]+)$', views.courseSectionDetail, name='courseSectionDetail'),
    url(r'^(?P<department>[A-Z]+)(?P<course_number>[0-9]+)/(?P<season>[a-zA-Z]+)(?P<year>[0-9]+)$', views.courseSemesterDetail, name='courseSemesterDetail'),
    url(r'^(?P<department>[A-Z]+)(?P<course_number>[0-9]+)/(?P<season>[a-zA-Z]+)(?P<year>[0-9]+)/(?P<section_number>[0-9]+)$', views.courseSemesterSectionDetail, name='courseSemesterSectionDetail'),
]
