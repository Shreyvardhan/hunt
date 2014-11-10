from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.views.generic.edit import FormView
from forms import TeamRegistrationForm
from django.contrib.auth import authenticate, login

class RegisterView(FormView):
    template_name = 'index.html'
    form_class = TeamRegistrationForm
    success_url = 'thanks.html'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/')

# class LoginView(FormView):

#     template_name = 'myapp/login.html'
#     form_class = AuthenticationForm
#     success_url = 'myapp/home.html'

#     def form_valid(self, form):
#         user = authenticate(username=self.request.POST['username'],
#                                       password=self.request.POST['password'])
#         if user is not None:
#             login(self.request, user)
#             return HttpResponseRedirect('/myapp/')
#         return HttpResponseRedirect('/myapp/login')