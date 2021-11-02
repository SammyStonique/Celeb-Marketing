from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from .models import *



def home(request):
    return render(request,'online_market/index.html')

def cart(request):
    return render(request,'online_market/cart.html')

def checkout(request):
    return render(request,'online_market/checkout.html')

def contact(request):
    return render(request,'online_market/contact.html')

def product(request):
    return render(request,'online_market/product-list.html')

def product_details(request):
    return render(request,'online_market/product-details.html')

def account(request):
    return render(request,'online_market/my-account.html')

def customer_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('main-homepage')
    else:
        form = UserRegisterForm()

    return render(request,'online_market/customer-register.html',{'form':form})

def login(request):
    return render(request, 'online_market/login.html')