from django.shortcuts import render, redirect
from .forms import SinUpForm, TodoForm
from .models import Todo

def index(request):
	user = request.user
	todo = Todo.objects.all().filter(username = user)
	
	params = {
		'todo': todo
	}
	return render(request, 'accounts/index.html', params)



def user_accounts(request):
	if (request.method == 'POST'):
		sinup = SinUpForm(request.POST)
		if sinup.is_valid():
			sinup.save()
			return redirect(to = '/')

	params = {
		'title': 'NewAccount',
		'form': SinUpForm()
	}
	return render(request, 'accounts/new_accounts.html', params)



def create(request):
	if (request.method == 'POST'):
		form = TodoForm(request.POST)
		if form.is_valid():
			todo = form.save(commit = False)
			todo.username = request.user
			todo.save()
			
		return redirect(to = '/')

	name = request.user

	context = {
		'title': 'TODO',
		'form': TodoForm()
	}
	return render(request, 'accounts/create.html', context)
