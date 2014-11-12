from django.conf.urls import patterns, url
from django.template import RequestContext, loader

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from teams import views
from django.views.generic import TemplateView
from django.forms.formsets import formset_factory

from teams import views
from teams.views import *

urlpatterns = patterns('',
	
	(r'^add/', manage_members),

)