from django.conf.urls import patterns, url
from tickets import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<ticket_id>\d+)/$', views.ticket, name='ticket'),
    url(r'^(?P<ticket_id>\d+)/postcomment/$', views.comment, name='comment'),
    url(r'^tier/(?P<tier_id>\d+)/$', views.tier, name='tier'),
    url(r'^company/(?P<company_id>\d+)/$', views.company, name='company'),
)
