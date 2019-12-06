from django import forms
from . import models


class newUser(forms.ModelForm):
	class Meta:
		model = models.user
		fields = ['firstName', 'lastName', 'userName', 'email', 'phone', 'password']
		labels = {'firstName':'First Name', 'lastName':'Last Name', 'userName':'Username', 'email':'Email (Must be @colorado.edu)', 'phone':'Phone Number', 'password':'Password'}