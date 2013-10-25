from django.conf.urls import patterns, url
from .views import overall


urlpatterns = patterns('',
    url(r'^$', overall, name='overall_stats'),
)
