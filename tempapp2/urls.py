from django.urls import path


from . import views 

urlpatterns = [
    path('', views.home,name='home'),
    path('t1', views.t1,name='t1'),
    path('t2', views.t2,name='t2'),
    path('t3', views.t3,name='t3'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('register', views.register,name='register'),
    path('helpme', views.helpme,name='helpme'),
    path('welcome', views.welcome,name='welcome'),
    path('contactus', views.contactus,name='contactus'),
    path('backtohome', views.backtohome,name='backtohome'),
    path('forgotpassword', views.forgotpassword,name='forgotpassword'),
    path('se4forgotpassword',views.se4forgotpassword,name='se4forgotpassword')
    #path('register',views.register,name='register')
]
