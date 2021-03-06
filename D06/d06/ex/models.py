from django.db import models
from django.utils import timezone

class Register(models.Model):
	username = models.CharField(max_length=32)
	password = models.CharField(max_length=64)
	password_confirm = models.CharField(max_length=64)

class Tip(models.Model):
	content = models.TextField()
	author = models.CharField(max_length=128)
	date = models.DateField(auto_now_add=True)