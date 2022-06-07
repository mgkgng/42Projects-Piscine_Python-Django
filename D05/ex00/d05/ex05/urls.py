from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('init', views.init, name='init'),
	path('populate', views.populate, name='populate'),
	path('display', views.display, name='display'),
	path('remove', views.remove, name='remove'),
]