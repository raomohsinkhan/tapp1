from django.db import models

# Create your models here.


# I will create a model here
# which will showo on news page
# model attributes are as follow

class Customers(models.Model):
	fname =models.CharField(max_length=100)
	lname =models.CharField(max_length=100)
	address = models.TextField()
	city =models.CharField(max_length=100)
	country =models.CharField(max_length=100)
	age = models.IntegerField(default=0)
	gender = models.BooleanField(default=False) #0 = Female, 1=Male