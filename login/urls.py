from django.conf.urls import patterns, url
from django.template import RequestContext, loader

from login import views

urlpatterns = patterns('',

	url(r'^$', views.index, name = 'index'),

)