from django.shortcuts import render
#from django.core.files import File
from .forms import UploadFileForm
from .models import File

def index(request):
	context = {}
	context["files"] = File.objects.all()
	if request.method == "POST":
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			context["form"] = form
	context["form"] = UploadFileForm()
	return render(request, "main/home.html", context)