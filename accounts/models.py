from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=255,unique=True)
    phone = models.CharField(max_length=12,unique=True)
    password = models.TextField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    first_name = None
    last_name =None
    username= None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile')
    email           = models.EmailField(max_length=100,default=1,unique=True)
    phone_number    = models.CharField(max_length=50,default=1 ,unique=True)

    def __str__(self):
        return self.user.first_name

   

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=15,default=0)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    phone2 = models.CharField(max_length=15,default=0)
    
    def __str__(self):
        return self.user.first_name


