from django.conf.urls import patterns, url
from .views import ProfileDetailView, ProfileSettingsView, me

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', ProfileDetailView.as_view(), name='profile'),
    url(r'^me/$', me, name='profile_me'),
    url(r'^me/settings/$', ProfileSettingsView.as_view(), name='profile_settings'),
)
