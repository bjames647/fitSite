from django.conf.urls import patterns, include, url

from website.views import HomePageView
from website.views import SignUpView
from website.views import LoginView
from website.views import LogOutView
from website.views import UserPageView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/profile/$', UserPageView.as_view(), name='profile'),
    url(r'^accounts/logout/$', LogOutView.as_view(), name='logout'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/register/$', SignUpView.as_view(), name='signup'),
    url('^$', HomePageView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
