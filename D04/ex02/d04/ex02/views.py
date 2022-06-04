from django.shortcuts import render, HttpResponse
from django.utils import timezone
from forms import Info

def index(request):
	if request.method == "POST":
		form = Info(request.POST)

		if form.is_valid():
			logfile = open("logs", 'w')
			logfile.write(timezone.now() + "\t\t\t" + form.cleaned_data['firstName']) + "\t\t\t" + form.cleaned_data['lastName']

		else:
			form = Info()
	return render(request, "base.html")
