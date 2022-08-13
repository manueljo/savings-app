from  django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'permanent_address', 'residential_address', 'lga', 'nin_number', 'first_kin_name', 'first_kin_relation', 'first_kin_number', 'first_kin_address','second_kin_name', 'second_kin_relation', 'second_kin_number', 'second_kin_address']
        

class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=20)
    message = forms.CharField(widget=forms.Textarea,max_length=2000)
    