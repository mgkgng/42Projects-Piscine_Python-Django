from django.db import models

class File(models.Model):
	name = models.CharField(max_length=40)
	imagefile = models.FileField(upload_to="files")

	def __str__(self):
		return self.name