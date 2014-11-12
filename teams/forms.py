from django import forms            
from teams.models import Team, Member 
from django.forms.formsets import formset_factory

class MemberForm(forms.ModelForm):

	name = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'Name'}), required = False, max_length=255)
	grade = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'Grade'}), required = False,max_length=255)
	section = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'Section'}), required = False,max_length=255)
	team = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'Team'}), max_length=255, required = False)
	email = forms.CharField(widget=forms.EmailInput(attrs = {'placeholder':'Email'}), max_length=255, required = False)

	class Meta:
		model = Member
		fields = ['name', 'grade', 'section', 'team']
		exclude = ('team',)