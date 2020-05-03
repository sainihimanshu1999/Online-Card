from django.db import models
from django.conf import settings
from django.shortcuts import reverse

class UserDash(models.Model):
    user_id = models.IntegerField(primary_key = True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    aboutme = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='profile_image', blank= True)
    created = models.DateTimeField(auto_now= True)
    font_size = models.IntegerField(null=True)
    github = models.CharField(max_length=100, blank= True, null= True)
    facebook = models.CharField(max_length=100, blank= True, null= True )
    linkedin = models.CharField(max_length=100, blank= True, null= True )
    instagram = models.CharField(max_length=100, blank= True, null= True )

    def __str__(self):
        return self.firstname



# class Profile(models.Model):
#     fname = models.ForeignKey(UserDash, on_delete=models.CASCADE )


