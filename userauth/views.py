from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import *


def signup(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			messages.success(request,"OK!!")
			return redirect("/")

		messages.error(request,"Thappu da!!")
	form = UserForm()
	context = {"form":form}
	return render(request,'html/signup.html',context)

def login_user(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(request,email=email,password=password)
		if user is not None:
			login(request,user)
			return redirect("/")

	return render(request,'html/login.html')



def logout_user(request):
	logout(request)
	return redirect('/')
