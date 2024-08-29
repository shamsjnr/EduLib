from django.db import models

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  publish_date = models.DateField(verbose_name = "Publish date")
  availability = models.BooleanField(default=True)