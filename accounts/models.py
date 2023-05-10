from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=255,unique=True)
    phone = models.CharField(max_length=12,unique=True)
    password = models.TextField()

    first_name = None
    last_name =None
    username= None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []