from django.conf.urls import patterns, url
from tickets import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<ticket_id>\d+)/$', views.ticket, name='ticket')
)
