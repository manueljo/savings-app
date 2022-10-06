from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.registerpage, name='register'),
    path('profile/<int:pk>/', views.profiles, name='profile'),
    path('initiate_pay/', views.initiate_payment, name='initiate-payment'),
    path('<str:ref>/', views.verify_payment, name='verify-payment'),
]
