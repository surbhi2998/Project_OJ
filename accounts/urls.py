from django.contrib import admin
from django.urls import path,include
from accounts import views

urlpatterns = [
    
    path('register',views.register,name='register'),
    path('login',views.signin,name='signin'),
    path('logout',views.signout,name='signout'),
   
    
]