from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignupForm, UserProfileSettingsForm, User, UserPasswordChangeForm
from django.contrib.auth import authenticate, logout as jlogout,  login as jlogin

# Create your views here.


def login(request):
    if  request.user.is_authenticated:
        return redirect('home:index')

    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                jlogin(request, user)
                return redirect('home:index')

    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})



def signup(request):
    if  request.user.is_authenticated:
        return redirect('home:index')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            jlogin(request, user)
            return redirect('home:index')

    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form':form})



def logout(request):
    jlogout(request)
    return redirect('home:index')


def profile(request):
    if request.method == 'POST':
        form =  UserProfileSettingsForm( request.POST, request.FILES, instance
                = request.user)
        if form.is_valid():
            form.save()
            return redirect('home:index')
        
    else:
        form = UserProfileSettingsForm(instance=request.user)
        
    return render(request, 'accounts/user_profile_settings.html',
                {'form':form})


def change_password(request):
    if request.method == 'POST':
        form =  UserPasswordChangeForm(request.user ,request.POST)
        if form.is_valid():
           form.save() 
           return redirect('home:index')


    else:
        form = UserPasswordChangeForm(request.user)

    return render(request, 'accounts/change_password.html', {'form':form})


