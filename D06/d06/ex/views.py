from django.shortcuts import render, redirect
import requests
from .forms import RegisterForm, LoginForm
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
	context = {}
	if request.user.is_authenticated:
		return redirect("/ex/home")
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			u = User.objects.create_user(form.cleaned_data["username"], form.cleaned_data["password"])
			u.save()
			auth.login(request, u)
			print("boubou")
			return redirect("/ex/home")
		else:
			context["form"]	= form
	else:
		context["form"] = RegisterForm()
	return render(request, "main/register.html", context)

def login(request):
	context = {}
	if request.user.is_authenticated:
		return redirect("/ex/home")
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			user = auth.authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
			if user is not None:
				auth.login(request, user)
				return redirect('/ex/home')
			else:
				context["form"] = form
		else:
			context["form"] = form
	else:
		context["form"] = LoginForm()
	return render(request, 'main/login.html', context)

def logout(request):
	auth.logout(request)
	return redirect('/ex/home')
