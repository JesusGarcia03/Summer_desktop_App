from django.shortcuts import render
from .models import Record



def home(request):
	records = Record.objects.all() 
	return render(request, 'home.html',{})
