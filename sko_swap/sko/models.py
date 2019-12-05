from django.db import models

class user(models.Model):
	firstName = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100)
	userName =models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=12)
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.userName

class createPost(models.Model):
	author = models.ForeignKey(user, on_delete=models.CASCADE)
	itemName = models.CharField(max_length=100)
	itemPrice = models.CharField(max_length=100)
	photos = models.ImageField()
	description = models.TextField()
# Create your models here.
