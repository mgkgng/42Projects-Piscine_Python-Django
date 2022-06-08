from django.shortcuts import render, redirect, HttpResponseRedirect
import requests
from .forms import LoginForm
from django.contrib import auth
from django.conf import settings

def home(request):
	namelist = settings.NAMELIST
	if request.method == "POST":
		cookie = request.POST.get("username", None)
		request.COOKIES["username"] = cookie
		response = render(request, "main/home.html", {"namelist": namelist})
		response.set_cookie("username", cookie, max_age=settings.SESSION_COOKIE_AGE)
		return response
	return render(request, "main/home.html", {"namelist": namelist})
