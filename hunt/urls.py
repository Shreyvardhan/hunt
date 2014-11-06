from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hunt.views.home', name='home'),

    url(r'^level/', include('levels.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
