from django.conf.urls import patterns, include, url
from . views import user_login

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookmarks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', user_login, name = "Login")
)
