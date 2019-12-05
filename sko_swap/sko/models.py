from django.db import models
from django.contrib.auth.models import User

class user(models.Model):
	firstName = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100)
	userName =models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=12)
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.userName

class listing(models.Model):
	title =  models.CharField(max_length=100)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	price = models.CharField(max_length=100)
	desc = models.TextField()

	def __str__(self):
		return self.title
		


	