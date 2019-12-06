from django.shortcuts import render
from . forms import newUser, newPost
from . models import listing
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

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
	query = request.GET.get("q")
	if query:
		queryset = listing.objects.filter(Q(title__icontains=query) | Q(desc__icontains=query))
	else:
		queryset = listing.objects.all()
	context ={
		'object_list':queryset
	}
	return render(request, 'sko/home.html', context)

def account(request):
	queryset = listing.objects.filter(author = request.user)
	context = {
		'object_list':queryset
	}
	return render(request, 'sko/account.html', context)

def search(request):
	search_bar = 'book'
	queryset = listing.objects.filter(Q(desc__icontains=search_bar) | Q(title__icontains=search_bar))
	context ={
		'object_list':queryset
		}
	return render(request, 'sko/home.html', context)
