from django.db import models

class Movies(models.Model):
	title = models.CharField(max_length=64, unique=True)
	episode_nb = models.BigAutoField(primary_key=True)
	opening_crawl = models.TextField(null=True) ## should check max size one more time before pushing
	director = models.CharField(max_length=32)
	producer = models.CharField(max_length=128)
	release_date = models.DateField()

	def __str__(self):
		return self.title
