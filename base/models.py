from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.timezone import now
import secrets
from .paystack import PayStack

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100,null=True, blank=True)
    permanent_address = models.CharField(max_length=100,null=True)
    residential_address = models.CharField(max_length=100,null=True)
    lga = models.CharField(max_length=20, null=True, blank=True)
    nin_number = models.PositiveBigIntegerField(null=True)
    passport = models.ImageField(null=True)
    date_registered = models.DateField(default=now,editable=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']
    
    def __str__(self):
        return self.first_name
    

class School(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=50)
    code = models.SmallIntegerField()
    
    def __str__(self):
        return str(self.school)

class NextOfKin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=10)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.user.first_name)

class Payment(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('date_created',)
        
    def __str__(self):
        return f'payment: {self.teacher}'
    
    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args,**kwargs)
        
    def amount_value(self):
        return self.amount * 100
    
    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount']/100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False             