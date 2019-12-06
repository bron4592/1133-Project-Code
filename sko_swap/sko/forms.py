from django import forms
from . import models

cond1 = (
(0, "Brand New"),
(1, "Like New"),
(2, "Very Good"),
(3, "Good"),
(4, "Acceptable"),
)

course1 = (
(0, "CSCI-1300"),
(1, "CSCI-2270"),
(2, "CSCI-2400"),
(3, "CSCI-2824"),
(4, "CSCI-3002"),
(5, "CSCI-3308"),
)

class newUser(forms.ModelForm):
	class Meta:
		model = models.user
		fields = ['firstName', 'lastName', 'userName', 'email', 'phone', 'password']
		labels = {'firstName':'First Name', 'lastName':'Last Name', 'userName':'Username', 'email':'Email (Must be @colorado.edu)', 'phone':'Phone Number', 'password':'Password'}

class newPost(forms.ModelForm):
	class Meta:
		model = models.listing
		fields = ['title', 'price', 'desc', 'phone', 'photo','cond', 'course']
		labels = {'title':'Listing Title',
				  'price':'Listing Price',
				  'desc':'Product Description',
				  'phone': 'Enter a Contact Number',
				  'cond':'Item Condition',
				  'course':'Applicable Course',
				}
		widgets = {
		'cond': forms.Select(choices=cond1),
		'course': forms.Select(choices=course1),
		}