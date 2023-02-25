from django.shortcuts import render
from django.http import HttpResponse 
from art.models import *

def home(request):
	art_all = ArtSave.objects.all()
	context = {'art':art_all}
	return render(request,'html/index.html',context)
