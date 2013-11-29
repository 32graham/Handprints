from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from haystack.views import basic_search
from tickets.views import IndexView
from django.conf import settings

admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(),  name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tickets/', include('tickets.urls')),
    url(r'^companies/', include('companies.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^stats/', include('stats.urls')),
    url(r'^search/', login_required(basic_search)),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='auth_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/tickets/'}, name='auth_logout'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
