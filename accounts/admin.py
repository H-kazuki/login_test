from django.contrib import admin
from .models import User
from .models import Todo

class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'email', 'password']

admin.site.register(User, UserAdmin)
admin.site.register(Todo)