from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from haystack.views import basic_search
from tickets.views import IndexView
from django.conf import settings
from django.views.static import serve


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
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='auth_logout'),
    url(r'^media/(?P<path>.*)$', login_required(serve), {'document_root': settings.MEDIA_ROOT}),
    url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'profiles.views.reset_confirm', name='password_reset_confirm'),
    url(r'^reset/$', 'profiles.views.reset', name='password_reset'),
)
