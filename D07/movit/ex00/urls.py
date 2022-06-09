from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.Home, name='index'),
	path(r'new',views.MainView.as_view(), name="test"),

	#path(r'home',views.MainView.Home, name="home"),
	#path(r'article',views.MainView.Article, name="article"),
	#path(r'login',views.MainView.Login, name="login"),
]