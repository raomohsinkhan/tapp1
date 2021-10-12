from django.shortcuts import render
from django.http import HttpResponse

from .models import Customers,Products
# Create your views here.


def home(request):
	return render(request,'abc.html',{"title":"Home"})

def ci(request):
	return render(request,'ci.html',{"title":"News"})

def t1(request):
	dests = Customers.objects.all()
	return render(request,'news.html',{"title":"News", "dests":dests})


def products(request):
	dests = Products.objects.all()
	return render(request,'products.html',{"title":"Products", "dests":dests})


def t2(request):
	return render(request,'contact.html',{"title":"Contact"})

def t3(request):
	return render(request,'about.html',{"title":"About"})


def saveci(request):
	fname = request.GET['fname']
	lname = request.GET['lname']
	address = request.GET['address']
	city = request.GET['city']
	country = request.GET['country']
	gender = request.GET['gender']
	c1 = Customers()
	c1.fname = fname
	c1.lname = lname
	c1.address = address
	c1.city = city
	c1.country = country
	c1.gender = gender
	c1.save()
	dests = Customers.objects.all()
	return render(request,'news.html',{"title":"News", "dests":dests})

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



