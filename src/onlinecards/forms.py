from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserDash

PRO_CHOICES = (
    ('E' , 'Enable'),
    ('D' , 'Disable')
)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DashboardUserForm(forms.ModelForm):
    class Meta:
        model = UserDash
        fields = [
            'firstname',
            'lastname',
            'designation',
            'email',
            'aboutme',
        ]


# class DashboardUserForm(forms.UserCreationForm):
#     class Meta:
#         model = User
#         fields = [
#             'firstname',
#             'lastname',
#             'designation',
#             'email',
#             'aboutme'
#         ]


