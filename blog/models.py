from django.db import models

# Create your models here.
#En este archivo definimos todos los objetos llamados Models - este es un lugar en el cual definiremos nuestro modelo post.

from django.utils import timezone

class Post(models.Model):
	author =models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text  = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
		