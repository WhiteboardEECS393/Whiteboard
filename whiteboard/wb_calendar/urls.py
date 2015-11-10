from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'$', views.calendar),
    url(r'\?start=(?P<start_date>\d{4}-\d{2}-\d{2})\&end=(?P<end_date>\d{4}-\d{2}-\d{2})$', views.calendar),

]