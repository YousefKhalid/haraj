from django.db import models


class Add(models.Model):
    name = models.CharField(max_length=20)
    body = models.TextField()
    Phone_number = models.CharField(max_length=10)
    city = models.CharField(max_length=10)

def __srt__(self):
    return self.name