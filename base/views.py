# from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm, ContactForm
from django.shortcuts import redirect, render


def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def dashboard(request):
    return render(request,'dashboard.html')

def loginpage(request):
    page = 'login'
    if request.method == 'POST':
        email= request.POST.get('email').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')
            
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'username or password does not exist')
    context = {'page':page}
    return render(request,'login_register.html', context)

def logoutuser(request):
    logout(request)
    return redirect('index')

def registerpage(request):
    form = MyUserCreationForm()
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'an error occured during registration')
    return render(request, 'login_register.html',{'form':form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'website enquiry'
            body = {
                'name' :form.cleaned_data['name'],
                'email' :form.cleaned_data['email'],
                'message' :form.cleaned_data['message'],
            }
            message = body.message
            try:
                send_mail(subject,message,'admin@example.com',['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact')
    form = ContactForm()
    return render(request, 'contact.html', {'form':form})