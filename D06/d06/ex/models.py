from django.db import models

class Tip(models.Model):
	content = models.TextField()
	author = models.CharField()
	date = models.DateField()