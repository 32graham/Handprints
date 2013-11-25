from django.conf.urls import patterns, url
from tickets import views
from .views import TicketList, IndexView

urlpatterns = patterns('',
    url(r'^$',                                   IndexView.as_view()),
    url(r'^status/(?P<status_id>\w+)/$',         TicketList.as_view(), name='status'),
    url(r'^tier/(?P<tier_id>\w+)/$',             TicketList.as_view(), name='tier'),
    url(r'^department/(?P<department_id>\w+)/$', TicketList.as_view(), name='department'),
    url(r'^(?P<ticket_id>\d+)/$',                views.ticket,         name='ticket'),
    url(r'^newticket/$',                         views.new_ticket,     name='new_ticket'),
)
