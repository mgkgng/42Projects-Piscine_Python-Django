from django.shortcuts import render, redirect
import requests
from .forms import LoginForm
from django.contrib import auth

def home(request):
	if request.method == "POST":
		

		redirect("/getUsername")

def getUsername(request):
	