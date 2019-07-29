from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Add(models.Model):
    name = models.CharField(max_length=20)
    body = models.TextField()
    Phone_number = models.CharField(max_length=10)
    city = models.CharField(max_length=10)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

def __srt__(self):
    return self.name