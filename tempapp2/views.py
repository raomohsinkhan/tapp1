from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
	return HttpResponse("Tempapp2: Hello World.")


def t1(request):
	return HttpResponse("Tempapp2: This is a t1 page.")


def t2(request):
	return HttpResponse("Tempapp2: This is a t2 page.")

def t3(request):
	return HttpResponse("Tempapp2: This is a t3 page.")