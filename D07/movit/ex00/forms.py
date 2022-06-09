from django import forms
from .models import Article

class LoginForm():
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())

class ArticleForm(forms.ModelForm):
	title = forms.CharField(max_length=64, required=True)
	content = forms.CharField(widget=forms.Textarea, required=True)

	class Meta:
		model=Article
		fields=("title", "content")