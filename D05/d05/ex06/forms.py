from django import forms

class MovieForm(forms.Form):
	opening_crawl = forms.CharField(required=True)
