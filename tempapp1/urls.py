from django.urls import path


from . import views 

urlpatterns = [
    path('', views.home,name='home'),
    path('t1', views.t1,name='t1'),
    path('t2', views.t2,name='t2'),
    path('t3', views.t3,name='t3'),
    path('add', views.add,name='add'),
    path('subtract', views.subtract,name='subtract'),
    path('divide', views.divide,name='divide'),
    path('multiplay', views.multiplay,name='multiplay'),
    path('ci', views.ci,name='ci'),
    path('pi', views.pi,name='pi'),
    path('savepi', views.savepi,name='savepi'),
    path('saveci', views.saveci,name='saveci'),
    path('products', views.products,name='products'),
]
