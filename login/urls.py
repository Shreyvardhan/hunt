from django.conf.urls import patterns, url
from django.template import RequestContext, loader

from django.http import HttpResponse, HttpResponseRedirect

from login import views

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

def members(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/members/add')
    else:
        return HttpResponseRedirect('/team/login/')

urlpatterns = patterns('',
	
	# (r'^accounts/', include('registration.backends.default.urls')),

	url(r'^login/', views.LoginView.as_view()),
	# url(r'^register/', views.RegisterView.as_view()),
	url(r'^$', members),

)