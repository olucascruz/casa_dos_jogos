from django.db import models

# Create your models here.
class User():
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField()