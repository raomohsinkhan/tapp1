from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
# Create your views here.


def home(request):
	return HttpResponse("Tempapp2: Hello World.")


def t1(request):
	if request.method == 'POST':
		# INSER DATA INTO DATABASE
		fname = request.POST['fname']
		lname = request.POST['lname']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']
		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'username has been booked')
				return redirect('t1')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email has been booked soemone else, do not know')
				return redirect('t1')
			else:
				user = User.objects.create_user(email=email,password=password1,first_name=fname,last_name=lname,username=username)
				user.save()
				messages.info(request,'user created successfully')
				return redirect('/')
			return redirect('/')
		else:
			messages.info(request,'Password not matched...')
			return redirect('t1')
		return redirect('/')
	else:
		return render(request,'register.html',{"title":"Register", "dests":"dests"})

def t2(request):
	return HttpResponse("Tempapp2: This is a t2 page.")

def t3(request):
	return HttpResponse("Tempapp2: This is a t3 page.")



