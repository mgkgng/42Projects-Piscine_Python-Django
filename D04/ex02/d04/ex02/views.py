from django.shortcuts import render, HttpResponse
from django.utils import timezone
from forms import Info
import logging

logger = logging.getLogger(__name__)

def index(request):
	if request.method == "POST":
		form = Info(request.POST)

		if form.is_valid():
			logger.

		else:
			form = Info()
	return render(request, "base.html", {"log", list(i.split(' ') for i in logfile.split('\n'))})

