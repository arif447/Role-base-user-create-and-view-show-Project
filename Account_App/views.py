from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html', context={})


def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are successfully register')
            return HttpResponseRedirect(reverse('Account_App:login_view'))
    return render(request, 'register.html', context={'form': form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and user.is_admin:
                login(request, user)
                messages.success(request, 'You are successfully logein')
                return HttpResponseRedirect(reverse('Account_App:adminpage'))

            elif user is not None and user.is_customer:
                login(request, user)
                messages.success(request, 'You are successfully logein')
                return HttpResponseRedirect(reverse('Account_App:customer'))

            elif user is not None and user.is_employee:
                login(request, user)
                messages.success(request, 'You are successfully logein')
                return HttpResponseRedirect(reverse('Account_App:employee'))

    return render(request, 'login.html', context={'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.warning(request, "You are logged out")
    return HttpResponseRedirect(reverse('Account_App:login_view'))


def admin_page(request):
    return render(request, 'admin.html', context={})

def customer(request):
    return render(request,'customer.html', context={})


def employee(request):
    return render(request,'employ.html', context={})

def createpost(request):
    return render(request, 'post.html', context={})

def edit(request):
    return render(request, 'edit.html', context={})
def payment(request):
    return render(request, 'payment.html', context={})

def profile(request):
    return render(request, 'profile.html', context={})