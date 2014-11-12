from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'deadlines.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'$', level),
    url(r'$/*', 'levels.views.level'),

)