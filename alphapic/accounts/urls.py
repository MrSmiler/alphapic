
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/settings/', views.profile, name='profile_settings'),
    path('profile/change/password', views.change_password, name='ch_password'),

        ]
