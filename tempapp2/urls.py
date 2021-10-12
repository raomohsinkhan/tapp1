from django.urls import path


from . import views 

urlpatterns = [
    path('', views.home,name='home'),
    path('t1', views.t1,name='t1'),
    path('t2', views.t2,name='t2'),
    path('t3', views.t3,name='t3'),
    #path('register',views.register,name='register')
]
