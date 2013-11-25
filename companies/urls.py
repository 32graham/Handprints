from django.conf.urls import patterns, url
from companies import views

urlpatterns = patterns('',
    url(r'^(?P<company_id>\w+)/$', views.company_detail, name='company'),
)
