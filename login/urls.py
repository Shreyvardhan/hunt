from django.conf.urls import patterns, url
from django.template import RequestContext, loader

from django.http import HttpResponse, HttpResponseRedirect

from login import views

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

def check_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/members')

urlpatterns = patterns('',
	
	# (r'^accounts/', include('registration.backends.default.urls')),

	url(r'^$', check_login),

)