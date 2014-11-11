from django import forms            
from teams.models import Team, Member 

class TeamRegistrationForm(forms.ModelForm):
	"""
	Registration form
	"""
	error_messages = {
		'duplicate_team_name': "A user for that email already exists.",
		'password_mismatch': "The two password fields didn't match.",
	}

	name = forms.CharField(label = "Team Name", max_length=255)
	
	password1 = forms.CharField(widget = forms.PasswordInput, label = "Team Password")
	password2 = forms.CharField(widget = forms.PasswordInput, label = "Confirm Team Password")
	
	class Meta:
		# If you are customizing the User class, always make sure to use 'get_user_model()' instead of 'User'
		model = Team
		fields = ['name', 'password1', 'password2']
	
	def clean_username(self):
		name = self.cleaned_data["name"]
		try:
			get_user_model().objects.get(name = name)
		except get_user_model().DoesNotExist:
			return name
		raise forms.ValidationError(
			self.error_messages['duplicate_team_name'],
			code = 'duplicate_team_name',
		)

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code = 'password_mismatch',
			)
		return password2

	def save(self, commit=True):
		team = super(TeamRegistrationForm, self).save(commit = False)
		team.set_password(self.cleaned_data["password1"])
		if commit:
			team.save()
		return team

