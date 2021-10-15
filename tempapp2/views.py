from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def home(request):
	return HttpResponse("Tempapp2: Hello World.")

def welcome(request):
	return render(request,'ac_welcome.html')
def register(request):
	return render(request,'ac_register.html')
def helpme(request):
	return render(request,'ac_helpme.html')
def contactus(request):
	return render(request,'ac_contactus.html')
def forgotpassword(request):
	return render(request,'ac_forgotpassword.html')
def backtohome(request):
	return redirect('/')

def se4forgotpassword(request):
	if request.method == 'POST':
		a = request.POST['email']
		subject = 'Reset Password Request'
		message = 'Password Forgot, send password reset link. Thank you.'
		send_mail(subject, message, settings.EMAIL_HOST_USER,[a], fail_silently=False)
		return render(request,'ac_forgotpassword.html',{"message":"Thank you, we have recived your message"})
	else:
		return render(request,'ac_forgotpassword.html')
		


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
				return redirect('login')
		else:
			messages.info(request,'Password not matched...')
			return redirect('t1')
	else:
		return render(request,'ac_register.html',{"title":"Register", "dests":"dests"})

def t2(request):
	return HttpResponse("Tempapp2: This is a t2 page.")

def t3(request):
	return HttpResponse("Tempapp2: This is a t3 page.")

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			#successfully login
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request,'invalid credentials')
			return redirect('login')
	else:
		return render(request,'ac_login.html')


def logout(request):
	auth.logout(request)
	return redirect('/')

