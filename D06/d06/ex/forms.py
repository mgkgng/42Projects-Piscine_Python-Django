from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True)
	password_confirm = forms.CharField(required=True)

	class Meta:
		model=User
		fields=("username", "password")
	
	def clean(self):
		form_data = self.cleaned_data
		if not "username" in form_data.keys():
			return form_data
		# to check if username already exist
		if User.objects.filter(username=form_data["username"]).exists():
			raise ValidationError("The username is already taken.")