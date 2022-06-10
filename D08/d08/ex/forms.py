from django import forms
from .models import File

class UploadFileForm(forms.ModelForm):
	name = forms.CharField(required=True)
	imagefile = forms.FileField(required=True)
	class Meta:
		model=File
		fields=("name", "imagefile")