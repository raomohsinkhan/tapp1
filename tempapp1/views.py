from django.shortcuts import render
from django.http import HttpResponse
import csv
from .models import Customers,Products
# Create your views here.


def home(request):
	return render(request,'abc.html',{"title":"Home"})

def ci(request):
	return render(request,'ci.html',{"title":"Customers"})

def pi(request):
	return render(request,'pi.html',{"title":"Products"})

def t1(request):
	dests = Customers.objects.all()
	return render(request,'news.html',{"title":"Customers", "dests":dests})

def products(request):
	dests = Products.objects.all()
	return render(request,'products.html',{"title":"Products", "dests":dests})


def t2(request):
	return render(request,'contact.html',{"title":"Contact"})

def t3(request):
	return render(request,'about.html',{"title":"About"})

def savepi(request):
	pname = request.GET['pname']
	unitprice = request.GET['unitprice']
	p1 = Products()
	p1.pname = pname
	p1.unitprice = unitprice
	p1.save()
	dests = Products.objects.all()
	return render(request,'products.html',{"title":"Products", "dests":dests})



def saveci(request):
	fname = request.GET['fname']
	lname = request.GET['lname']
	address = request.GET['address']
	city = request.GET['city']
	country = request.GET['country']
	age = request.GET['age']
	gender = request.GET['gender']
	c1 = Customers()
	c1.fname = fname
	c1.lname = lname
	c1.address = address
	c1.city = city
	c1.country = country
	c1.age = age
	c1.gender = gender
	c1.save()
	dests = Customers.objects.all()
	return render(request,'news.html',{"title":"Customers", "dests":dests})

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

#Exporting Customers Information into CSV File Format
def export2csv(request):
	a = 'i am rao mohsin'
	c = Customers.objects.all()
	response = HttpResponse('')
	response['Content-Disposition'] = 'attachment; filename=abc.csv'
	writer = csv.writer(response)
	writer.writerow(['fname','lname','address','city','country','age','gender'])
	customer_fields = c.values_list('fname','lname','address','city','country','age','gender')
	for profile in customer_fields:
		writer.writerow(profile)
	return response

#Exporting Product Information into CSV File Format
def exproducts(request):
	p = Products.objects.all()
	response = HttpResponse('')
	response['Content-Disposition'] = 'attachment; filename=products.csv'
	writer = csv.writer(response)
	writer.writerow(['pname','unitprice','added'])
	product_fields = p.values_list('pname','unitprice','added')
	for profile in product_fields:
		writer.writerow(profile)
	return response


