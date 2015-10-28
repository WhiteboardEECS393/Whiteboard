"""whiteboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^course/', include('class_overviews.urls')),
    url(r'^$', views.main_redirect, name='main_redirect'),
    url(r'^create_student/', views.create_student, name='create_student'),
    url(r'^create_new_user/', views.create_new_user, name='create_new_user'),
    url(r'^AllProfiles/', views.index, name='index'),
    url(r'^MyProfile/', include('Profiles.urls')),
    url(r'^admin/', include(admin.site.urls)),

]
