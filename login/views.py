from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.views.generic.edit import FormView
from forms import TeamRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

class RegisterView(FormView):
    template_name = 'login/index.html'
    form_class = TeamRegistrationForm
    success_url = 'login/thanks.html'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/thanks')

class LoginView(FormView):
    template_name = 'login/index.html'
    form_class = AuthenticationForm
    success_url = 'index.html'

    def form_valid(self, form):
        user = authenticate(name = self.request.POST['username'],
                                      password = self.request.POST['password'])
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect('/members/')
        return HttpResponseRedirect('/')
    # else:
        # return HttpResponseRedirect('/members')

def check_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/members')