from django.shortcuts import render, HttpResponse,redirect
from django.views.generic import View
from .models import Article
from .forms import LoginForm, ArticleForm
from django.contrib import auth
from django.contrib.auth.models import User

def init(request):
	return HttpResponse("Hello world")

class MainView(View):

	def Home(self, request):
		return redirect('/movit_app/Article')

	def Article(self, request):
		context = {}
		context["article"] = Article
		return render(request, "movit/article.html", context)

	def Login(self, request):
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				u = User.objects.create_user(form.cleaned_data["username"], form.cleaned_data["password"])
				u.save()
				auth.login(request, u)
				return redirect("/ex/home")
		form = LoginForm()
		return render(request, "main/login.html", {"form": form})