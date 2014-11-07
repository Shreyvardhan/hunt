from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from teams.models import Team
from teams.models import Member

class MemberInline(admin.TabularInline):
	model = Member

class TeamCreationForm(forms.ModelForm):

	password = forms.CharField(label = 'Passcode', widget = forms.PasswordInput)

	class Meta:
		model = Team
		fields = ('name', )

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

	# def members(self):
	# 	html = ""
	# 	for obj in Member.objects.filter(team=self):
	# 		html += '<p><a href="%s">%s</a></p>' %(obj.name, obj.name)
	# 	return html
	
	# members.allow_tags = True

	list_display = ('name', 'rank',)
	list_filter = ('rank',)

	inlines = [MemberInline,]

	fieldsets = [

		("General", {

			'classes': ('wide',),
			'fields': ('name',)

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

"""
Members Admin
"""
class MemberAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'team', 'grade', 'section',)
	list_filter = ('grade',)
	search_fields = ('name','grade','team')

	fieldsets = [

		("General", {

			'fields': ('name', 'grade', 'section', 'email')

		}),
		
		('Team', {

			'fields': ('team',)

		})
	
	]

admin.site.register(Team, TeamAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.unregister(Group)