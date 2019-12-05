from django.db import models

class user(models.Model):
	firstName = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100)
	userName =models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=12)
	password = models.CharField(max_length=100)


	