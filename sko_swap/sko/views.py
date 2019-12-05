from django.shortcuts import render
from . forms import newUser
from django.shortcuts import render, redirect

def register(request):
	if request.method == 'POST':
		form = newUser(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			messages.success(request, f'New Search Successfully Added!')
			return redirect('sko/home')
	else:
		form = newUser()
	return render(request, 'sko/register.html', {'form':form})

def home(request):
	return render(request, 'sko/home.html')

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
	return render(request, 'sko/create_post.html', {'form':form})
# Create your views here.
