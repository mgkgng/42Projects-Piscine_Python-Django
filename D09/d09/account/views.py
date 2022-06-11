from django.shortcuts import render
import json
from .forms import LoginForm

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			
