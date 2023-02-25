from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("name","email","std","sec")

	def save(self,commit = True):
		user = super(UserForm,self).save()
		

		return user