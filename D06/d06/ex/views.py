from django.shortcuts import render, redirect
import random, datetime
from .forms import RegisterForm, LoginForm, TipForm
from .models import Tip
from django.contrib import auth
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def home(request):
	context = {}
	if request.method == "POST":
		form = TipForm(request.POST)
		if form.data["content"]:
			tip = Tip(
				content=form.data["content"],
				author=request.user.username,
				#date = datetime.date.today()
			)
			tip.save()
			return redirect("/ex/home")

	if request.user.is_authenticated:
		context["tipform"] = TipForm()
		context["glace"] = Tip.objects.all()
		return render(request, "main/home.html", context)
	elif "username" in request.COOKIES.keys():
		return render(request, "main/home.html")
	else:
		cookie = random.choice(settings.NAMELIST) 
		request.COOKIES["username"] = cookie
		response = render(request, "main/home.html")
		response.set_cookie("username", cookie, max_age=settings.SESSION_COOKIE_AGE)
		return response

def register(request):
	context = {}
	if request.user.is_authenticated:
		return redirect("/ex/home")
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			u = User.objects.create_user(username, None, password)
			u.save()
			auth.login(request, u)
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
			u = auth.authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
			if u and u.is_active:
				auth.login(request, u)
				return redirect('/ex/home')
			else:
				context["msg"] = "Wrong username or password."
				context["form"] = LoginForm()
				return render(request, 'main/login.html', context)
		else:
			context["form"] = form
	else:
		context["form"] = LoginForm()
	return render(request, 'main/login.html', context)

def logout(request):
	auth.logout(request)
	return redirect('/ex/home')
