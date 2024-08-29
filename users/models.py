from django.db import models

# Create your models here.
class User(models.Model):
  names = models.CharField(max_length=100)
  email = models.EmailField()
  phone = models.CharField(max_length=15)
  username = models.CharField(max_length=20)