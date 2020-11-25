from django import forms
from django.contrib.auth.models import User
from .models import Todo
from django.contrib.auth.forms import UserCreationForm

class SinUpForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

class TodoForm(forms.ModelForm):
	class Meta():
		model = Todo
		fields = ['title', 'contents']