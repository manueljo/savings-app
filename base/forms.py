from  django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Payment

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'permanent_address', 'residential_address', 'lga', 'nin_number', 'passport']
        # exclude = ['username']
        
class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=20)
    message = forms.CharField(widget=forms.Textarea,max_length=2000)
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'permanent_address',
                  'residential_address', 'lga', 'nin_number', 'passport']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'email']