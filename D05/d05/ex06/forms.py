from django import forms

class MovieForm(forms.Form):
	opening_crawl = forms.TextField(required=True)
