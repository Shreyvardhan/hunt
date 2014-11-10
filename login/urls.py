from django.conf.urls import patterns, url
from django.template import RequestContext, loader

from login import views

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = patterns('',
	
	# (r'^accounts/', include('registration.backends.default.urls')),

	url(r'^$', views.RegisterView.as_view()),

)