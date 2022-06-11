from tkinter import Widget
from django.db import models

class Login(models.Model):
	username = models.CharField(max_length=32)
	password = models.CharField(max_length=64)

	def __str__(self):
		return self.username