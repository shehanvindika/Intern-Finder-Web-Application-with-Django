from django.db import models


class Register(models.Model):
    companyName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    password1 = models.CharField(max_length=255)  # character to astric
    password2 = models.CharField(max_length=255)  # character to astric

class Posts(models.Model):
    companyName=models.CharField(max_length=255)
    position=models.CharField(max_length=255)
    requirments = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    deadline = models.CharField(max_length=255) #character to date