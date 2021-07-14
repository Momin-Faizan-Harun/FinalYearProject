from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_generator    =   models.BooleanField(default=False)
    is_handler      =   models.BooleanField(default=False)

    first_name      =   models.CharField(max_length=50)
    last_name       =   models.CharField(max_length=50)


class Generator(models.Model):
    user    =   models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone   =   models.CharField(max_length=12)





class Handler(models.Model):
    user    =   models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone   =   models.CharField(max_length=12)