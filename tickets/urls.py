from django.conf.urls import patterns, url
from tickets import views
#from .views import TicketFilterView

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)

urlpatterns = patterns('',
    url(r'^(?P<ticket_id>\d+)/$', views.ticket,      name='ticket'),
    url(r'^newticket/$',          views.new_ticket,  name='new_ticket'),
    url(r'^$',                    views.ticket_list, name='tickets'),
)
