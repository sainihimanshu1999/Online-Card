from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import views
from .views import DashboarduserView

urlpatterns = [

    path('', views.home, name = "home"),
    path('register/', views.register, name = "register"),
    path('loginnext/', views.loginnext, name = "loginnext"),
    # path('forms/', views.forms, name = "forms"),
    path('logout/', views.logoutUser, name = "logout"),
    path('dashboardu/', login_required(DashboarduserView.as_view(), login_url='loginnext') , name = "dashboardu"),
    # path('profile/',  views.profile,  name="profile"),
   

    
    
]
