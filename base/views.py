# from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import User, Payment
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm, ContactForm, ProfileForm, PaymentForm
from django.shortcuts import redirect, render, get_object_or_404


def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        customer = request.user
        records = Payment.objects.filter(teacher=customer)
        total_amount = Payment.objects.filter(teacher=customer, verified=True)
        number = Payment.objects.filter(teacher=customer, verified=True).count()
        total = 0
        # values = total_amount.get('')
        for value in total_amount:
            total += value.amount

    context = {'customer':customer, 'records':records, 'total':total, 'number':number}
    return render(request,'dashboard.html', context)

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
        form = MyUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # login(request, user)
            return redirect('login')
        else:
            messages.error(request, 'an error occured during registration')
            return redirect('register')
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


def profiles(request, pk):
    profile = User.objects.get(id=pk)
    form = ProfileForm(instance=profile)
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    context ={'form':form,'user':current_user}
    return render(request,'profile.html',context)

def initiate_payment(request):
    if request.method == 'POST':
        teacher = request.user
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save(commit=False)
            payment.teacher = teacher
            payment.save()
            pub_key = 'pk_test_3634710fe504afb2cc6de2ef27f378c5c39f16dc'
            return render(request, 'make_payment.html', {'payment': payment, 'paystack_public_key':pub_key})
    else:
        payment_form = PaymentForm()
    return render(request, 'initiate_payment.html', {'payment_form':payment_form})

def verify_payment(request,ref):
    payment = get_object_or_404(Payment,ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request,'verification successfull')
    else:
        messages.error(request, 'verification failed')
    return redirect('dashboard')