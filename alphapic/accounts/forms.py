from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.forms import ModelForm
from home.models import User
from django.utils.translation import gettext_lazy as _
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, label=_('Username'), widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(required=True, label=_('Password'),widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User 
        fields = ['username', 'password']
    


class SignupForm(UserCreationForm):
    
    username = forms.CharField(required=True,label=_('Username'), widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,label=_('Email'), widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(required=True, label=_('PassWord1'),widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(required=True, label=_('PassWord2'),widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']


class UserProfileSettingsForm(ModelForm):
    birth_date = forms.DateField(required=True,label=_('Birth Date'), widget=forms.DateInput(attrs={'class':'form-control'}))
    bio = forms.CharField(required=True,label=_('bio'), widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['birth_date', 'bio', 'profile_pic']




class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(required=True,label=_('Old PassWord'), widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(required=True,label=_('PassWord1'), widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(required=True,label=_('PassWord2'), widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']




