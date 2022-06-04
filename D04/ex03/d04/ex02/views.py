from django.shortcuts import render, HttpResponse
from django.utils import timezone
from . import forms
from .forms import Info
import logging

logger = logging.getLogger("info")


def index(request):
	if request.method == "POST":
		form = Info(request.POST)
		if form.is_valid():
			logger.info(form.cleaned_data["firstName"])
	form = Info()
	return render(request, "ex02/base.html", {"form": form})