from django import forms
from .models import Tip, Register
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class RegisterForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())
	password_confirm = forms.CharField(required=True, widget=forms.PasswordInput())

	class Meta:
		model=Register
		fields=("username", "password")
	
	#def clean_password(self):
	#	return make_password(self.cleaned_data["password"])

	def clean_password_confirm(self):
		p = self.data["password"]
		p_confirm = self.data["password_confirm"]
		if p != p_confirm:
			raise ValidationError("Password confirmation not corresponding to the password")
		return p
	
	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError(f'Username "{username}" is already in use.')
		return username

class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())
	
class TipForm(forms.ModelForm):
	content = forms.CharField(required=True)

	class Meta:
		model = Tip
		fields = ("content", "author")