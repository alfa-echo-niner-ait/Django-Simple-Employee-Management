from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    