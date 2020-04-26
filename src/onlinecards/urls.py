from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name = "home"),
    path('register/', views.register, name = "register"),
    path('loginnext/', views.loginnext, name = "loginnext"),
    path('logout/', views.logoutUser, name = "logout"),
   

    
    
]
