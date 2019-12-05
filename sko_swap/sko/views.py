from django.shortcuts import render
from . forms import newUser, newPost
from . models import listing
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
	if request.method == 'POST':
		form = newUser(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			messages.success(request, f'Account Successfully Created!')
			return redirect('sko/home')
	else:
		form = newUser()
	return render(request, 'sko/register.html', {'form':form})

def createPost(request):
	if request.method == 'POST':
		form = newPost(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			messages.success(request, f'New Post Successfully Added!')
			return redirect('sko/home')
	else:
		form = newPost()
	return render(request, 'sko/newPost.html', {'form':form})
def home(request):
	queryset = listing.objects.all()
	context ={
		'object_list':queryset
	} 
	return render(request, 'sko/home.html', context)
# Create your views here.
