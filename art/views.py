from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from userauth.models import *
from .forms import ArtForm

def artwork(request):
	form = ArtForm()
	if request.method == 'POST':
		if request.user.is_authenticated:

			form = ArtForm(request.POST,request.FILES)	
			if form.is_valid():
				form = form.save(commit=False)
				form.user = request.user
				form.save() 
				return redirect('/')
		else:
			
			return redirect('/signup')

	context = {"form":form}
	return render(request,"html/artwork.html",context)