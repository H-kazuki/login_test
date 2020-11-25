from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class User(models.Model):
	username = models.CharField('Username', max_length = 20)
	email = models.EmailField('Email', max_length = 100)
	password = models.CharField('Pass', max_length = 20, validators = [MinLengthValidator(6)])


class Todo(models.Model):
	username = models.CharField('Username', max_length = 150)
	title = models.CharField('Title', max_length = 50)
	contents = models.TextField('Contents', max_length = 200)
	created_at = models.DateTimeField('Date', auto_now_add = True)
	