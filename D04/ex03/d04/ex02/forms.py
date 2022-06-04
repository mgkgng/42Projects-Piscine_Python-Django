from django import forms

class Info(forms.Form):
	firstName = forms.CharField(required=True)
