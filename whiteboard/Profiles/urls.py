from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.profile, name='profile'),
        url(r'^EECS393/', views.classes, name='EECS 393'),
        url(r'^EECS325/', views.classestwo, name='EECS 325'),
        ]
