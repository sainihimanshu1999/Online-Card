from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import views
from .views import DashboarduserView
from .views import SocialbuttonView

urlpatterns = [

    path('', views.home, name = "home"),
    path('register/', views.register, name = "register"),
    path('loginnext/', views.loginnext, name = "loginnext"),
    # path('card/<int:pk>', views.card, name = "card"),
    path('logout/', views.logoutUser, name = "logout"),
    path('dashboardu/', login_required(DashboarduserView.as_view(), login_url='loginnext') , name = "dashboardu"),
    path('profile/',  views.SocialbuttonView,  name="profile"),
   

    
    
]
