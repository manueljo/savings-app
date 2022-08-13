from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.timezone import now

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    username = models.CharField(max_length=100,null=True)
    email = models.EmailField(unique=True, null=True)
    permanent_address = models.CharField(max_length=100,null=True)
    residential_address = models.CharField(max_length=100,null=True)
    lga = models.CharField(max_length=20, null=True)
    nin_number = models.PositiveBigIntegerField(null=True)
    first_kin_name = models.CharField(max_length=50, null=True)
    first_kin_relation = models.CharField(max_length=10, null=True)
    first_kin_number = models.PositiveBigIntegerField(null=True)
    first_kin_address = models.CharField(max_length=100, default='osun')
    second_kin_name = models.CharField(max_length=50, null=True)
    second_kin_relation = models.CharField(max_length=10, null=True)
    second_kin_number = models.PositiveBigIntegerField(null=True)
    second_kin_address = models.CharField(max_length=100, null=True)
    #passport
    date_created = models.DateField(default=now,editable=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['lga']
    

class School(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=50)
    # code = models.CharField(max_length=20, null=True)
    
    