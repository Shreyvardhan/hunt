from django.conf.urls import patterns, include, url
from views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'deadlines.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'$', 'levels.views.index'),

)