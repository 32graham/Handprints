from django.conf.urls import patterns, url
from .views import ProfileDetailView, ProfileSettingsView

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', ProfileDetailView.as_view(), name='profile'),
    url(r'^(?P<pk>\d+)/settings/$', ProfileSettingsView.as_view(), name='profile_settings'),
)
