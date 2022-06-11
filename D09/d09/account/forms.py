from django import forms
from kivy import require
from .models import Login

class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput)
	password_confirm = forms.CharField(required=True, widget=forms.PasswordInput)