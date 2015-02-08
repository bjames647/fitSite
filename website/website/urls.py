from django.conf.urls import patterns, include, url

from website.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^compete/compete/$', UserPageView.as_view(), name='compete'),
    #url(r'^accounts/profile/$', user_view, name='userview'),
    url(r'^accounts/profile/$', UserPageView.as_view(), name='profile'),
    url(r'^accounts/logout/$', LogOutView.as_view(), name='logout'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/register/$', SignUpView.as_view(), name='signup'),
    url('^$', HomePageView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
