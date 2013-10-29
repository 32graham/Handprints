from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tickets/', include('tickets.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^stats/', include('stats.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='auth_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/tickets/'}, name='auth_logout'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/jgraham32/media/'}),
)
