from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from home.models import User
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User 
        fields = ['username', 'password']
    


class SignupForm(UserCreationForm):
    
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']
