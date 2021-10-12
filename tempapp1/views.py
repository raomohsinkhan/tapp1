from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
	return render(request,'abc.html',{"title":"Home"})


def t1(request):
	return render(request,'news.html',{"title":"News"})

def t2(request):
	return render(request,'contact.html',{"title":"Contact"})

def t3(request):
	return render(request,'about.html',{"title":"About"})

def add(request):
	return render(request,'about.html',{"title":"Add"})

def subtract(request):
	return render(request,'contact.html',{"title":"Subtract"})

def divide(request):
	return render(request,'contact.html',{"title":"Divide"})

def multiplay(request):
	return render(request,'contact.html',{"title":"Multiplay"})

def tt2(request):
	return render(request,'contact.html',{"title":"Contact"})



