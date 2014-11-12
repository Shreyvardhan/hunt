from django.shortcuts import render
from teams.models import Team, Member
from rest_framework import viewsets
from teams.serializers import TeamSerializer, MemberSerializer
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from forms import MemberForm
from rest_framework import generics
from django.shortcuts import render_to_response
from django.forms.models import modelformset_factory
from django.template import RequestContext
from django.shortcuts import redirect

def hello(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def manage_members(request):

	return redirect('/level')
	
	# if Member.objects.filter(team = request.user):
	# else:	
	# 	MemberFormSet = modelformset_factory(Member, MemberForm, extra = 3)
		
	# 	if request.method == "POST":
			
	# 		formset = MemberFormSet(request.POST)

	# 	# if(formset.is_valid()):
	# 		instances = formset.save(commit = False)
	# 		for instance in instances:
	# 			instance.team = request.user
	# 			if instance.name is None:
	# 				message = "Damn you."
	# 			else:
	# 				message = "Thank you."
	# 				instance.save()
				
	# 		# else:
	# 			# message = formset.errors

	# 		return redirect('/level')
	
	# 	else:
	# 		return render_to_response('teams/members.html', {'formset': MemberFormSet()}, context_instance = RequestContext(request))