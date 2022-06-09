from multiprocessing import AuthenticationError
from tkinter import CASCADE
from django.db import models

class User(models.Model):
	username = models.CharField(max_length=64)
	password = models.CharField(max_length=128)

class Article(models.Model):
	title = models.CharField(max_length=64)
	author = models.CharField(max_length=128)
	created = models.DateField(auto_now_add=True)
	synopsis = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()

	def __str__(self):
		return self.title

class UserFavouriteArticle(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	article = models.ForeignKey(Article, on_delete=models.CASCADE)

	def __str__(self):
		return self.article
