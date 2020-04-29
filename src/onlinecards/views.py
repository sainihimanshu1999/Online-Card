import requests
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from .forms import DashboardUserForm
from .models import UserDash

# home view
def home(request):
    return render(request, "index.html")

# SignUp page
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user )
            return redirect('loginnext')
    context = {'form': form}
    return render(request, "register.html", context)

# Login Page
def loginnext(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboardu')
        else:
            messages.info(request, 'Username or Password is incorrect')
    
    context = {}
    return render(request, 'login.html', context)

# Logout Page
def logoutUser(request):
    logout(request)
    return redirect('home')

#profile Registration
@login_required(login_url='loginnext')
def dashboard_user_view(request):
    if request.method == 'POST':
        form = DashboardUserForm(request.POST)
        if form.is_valid():
            form.save()
            form = DashboardUserForm()
            

    else:
        form = DashboardUserForm(request.GET)
    return render(request, "dashboarduser.html", {'form': form})


def card(request, firstname):
    firstname = UserDash
    




# def forms(request):
#     if request.method == "POST":
#         if request.POST.get('submit') == 'sign_in':
#             if request.method == 'POST':
#                 username = request.POST.get('username')
#                 password = request.POST.get('password')

#                 user = authenticate(request, username=username, password=password)
#                 if user is not None:
#                     login(request, user)
#                     return redirect('home')
#                 else:
#                     messages.info(request, 'Username or Password is incorrect')
        
#             context = {}
#             return render(request, 'login.html', context)

#         elif request.POST.get('submit') == 'sign_up':
#             form = CreateUserForm()
#             if request.method == 'POST':
#                 form = CreateUserForm(request.POST)
#                 if form.is_valid():
#                     form.save()
#                     user = form.cleaned_data.get('username')
#                     messages.success(request, 'Account was created for ' + user )
#                     return redirect('loginnext')
#             context = {'form': form}
#             return render(request, "register.html", context)





    