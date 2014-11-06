from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from teams.models import Team
from teams.models import Member

class TeamCreationForm(forms.ModelForm):

	password = forms.CharField(label = 'Passcode', widget = forms.PasswordInput)

	class Meta:
		model = Team
		fields = ('name','date_joined')

	def save(self, commit = True):
		user = super(TeamCreationForm, self).save(commit = False)
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
		return user

class TeamChangeForm(forms.ModelForm):

	password = ReadOnlyPasswordHashField()

	class Meta:
		model = Team
		fields = ('name', 'password', 'is_active', 'is_admin')

	def clean_password(self):
		return self.initial["password"]

class TeamAdmin(UserAdmin):

	form = TeamChangeForm
	add_form = TeamCreationForm

	list_display = ('name', 'rank')
	list_filter = ('rank',)

	fieldsets = [

		("General", {

			'classes': ('wide',),
			'fields': ('name', 'date_joined',)

		}),
		
		('Rank', {

			'fields': ('rank',)

		}),

		('Meta', {

			'classes': ('collapse',),
			'fields': ('is_admin',)

		})
	
	]
	
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('name', 'password')}
		),
	)
	search_fields = ('name',)
	ordering = ('rank',)
	filter_horizontal = ()

admin.site.register(Team, TeamAdmin)
admin.site.unregister(Group)
