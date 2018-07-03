
from django.urls import path
from . import views


app_name = 'home'


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_image, name='upload'),
    path('search_user/', views.search_user, name='search'),
    path('search/<str:username>/', views.search, name='real_search'),
    path('image/like/<int:image_id>/', views.like_image, name='like'),
    path('image/unlike/<int:image_id>/', views.unlike_image, name='unlike'),
    path('follow/<int:user_id>/', views.follow, name='follow'),
    path('unfollow/<int:user_id>/', views.unfollow, name='unfollow'),
    path('change/language/<str:language_code>', views.change_language,
        name='ch_language'),

        ]
