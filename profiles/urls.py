from django.conf.urls import patterns, url
from profiles import views

urlpatterns = patterns(
    '',
    url(r'^(?P<user_id>\d+)/$', views.profile, name='profile'),
)
