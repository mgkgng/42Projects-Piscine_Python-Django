from django.shortcuts import render, HttpResponse,redirect
from django.views.generic import View
from .models import Article
from .forms import LoginForm, ArticleForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse

def init(request):
	return HttpResponse("Hello world")

class MainView(View):
	lform = LoginForm

	def Home(self, request):
		return redirect(reverse('test'))

	def Article(self, request):
		context = {}
		context["article"] = Article
		return render(request, "movit/article.html", context)

	def Login(self, request):
		if request.method == "POST":
			f = self.lform(request.POST)
			if f.is_valid():
				u = User.objects.create_user(f.cleaned_data["username"], f.cleaned_data["password"])
				u.save()
				auth.login(request, u)
				return redirect("/ex/home")
		f = self.lform()
		return render(request, "main/login.html", {"form": f})