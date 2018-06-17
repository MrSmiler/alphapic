
from django.urls import path
from . import views


app_name = 'home'


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_image, name='upload'),
    path('search/', views.search_user, name='search'),
    path('image/like/', views.like_image, name='like'),

        ]
