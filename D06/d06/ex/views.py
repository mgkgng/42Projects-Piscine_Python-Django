from django.shortcuts import render, redirect, HttpResponseRedirect
import requests
from .forms import LoginForm
from django.contrib import auth
from django.conf import settings
from django.contrib.auth.models import User

def home(request):
	namelist = settings.NAMELIST
	if request.method == "POST":
		cookie = request.POST.get("username", None)
		request.COOKIES["username"] = cookie
		response = render(request, "main/home.html", {"namelist": namelist})
		response.set_cookie("username", cookie, max_age=settings.SESSION_COOKIE_AGE)
		return response
	return render(request, "main/home.html", {"namelist": namelist})

def register(request):
	if request.user.is_authenticated():
		return redirect("/home")
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			password_confirm = form.cleaned_data["password_confirm"]
			if password != password_confirm:
				return HttpResponseRedirect("Password confirmation not corresponding to the password")
			u = User.objects.create_user
	form = LoginForm()
	return render(request, "main/register.html", {"form": form})

def login(request):
	if request.user.is_authenticated():
		return redirect("/home")
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = auth.authenticate(username=username, password=password)
			if user and user.is_active:
				auth.login(request, user)
				return redirect('/home')
			else:
				form._error["username"] = ["This user does not exist."]
	else:
		form = LoginForm()
	return render(request, 'main/home.html', {"form", form})

def logout(request):
	auth.logout(request)
	return redirect('/home')
