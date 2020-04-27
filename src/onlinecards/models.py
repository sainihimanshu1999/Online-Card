from django.db import models
from django.conf import settings
from django.shortcuts import reverse

class UserDash(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    aboutme = models.TextField(max_length=1000)

    def __str__(self):
        return(self.firstname)

    

