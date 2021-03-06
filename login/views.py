from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.views.generic.edit import FormView
from forms import TeamRegistrationForm
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm

from teams.models import Team, Member

class RegisterView(FormView):
    template_name = 'login/registration.html'
    form_class = TeamRegistrationForm
    success_url = '/level'

    def form_valid(self, form):
        form.save()
        # messages.info(request, "Thanks for registering. You are now logged in.")
        user = authenticate(name = self.request.POST['name'],
                                      password = self.request.POST['password2'])
        login(self.request, user)

        Team.objects.filter(name = self.request.POST['name']).update(level = 1)
    
        return HttpResponseRedirect('/level')

class LoginView(FormView):
    template_name = 'login/index.html'
    form_class = AuthenticationForm
    success_url = '/members/add'

    def form_valid(self, form):
        user = authenticate(name = self.request.POST['username'],
                                      password = self.request.POST['password'])
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect('/level')
        return HttpResponseRedirect('/')
    # else:
        # return HttpResponseRedirect('/members')

def check_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/level')