from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from tickets import views
from .views import TicketList

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^status/(?P<status_id>\w+)/$', login_required(TicketList.as_view()), name='status'),
    url(r'^tier/(?P<tier_id>\w+)/$', login_required(TicketList.as_view()), name='tier'),
    url(r'^company/(?P<company_id>\w+)/$', login_required(TicketList.as_view()), name='company'),
    url(r'^(?P<ticket_id>\d+)/$', views.ticket, name='ticket'),
    url(r'^(?P<ticket_id>\d+)/postcomment/$', views.comment, name='comment'),
    url(r'^newticket/$', views.new_ticket, name='new_ticket'),
)
