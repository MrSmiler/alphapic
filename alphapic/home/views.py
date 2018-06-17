from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import User, Picture
from .forms import UploadImageForm

# Create your views here.


def index(request):
    
    return render(request, 'home/index.html', {})

def search_user(request):
    username = request.GET['username']
    another_user = get_object_or_404(User, username=username)
    if request.user.is_authenticated:
        if another_user == request.user:
            return render(request, 'home/index.html', {})

    return render(request, 'home/user_navigate.html', {'another_user':another_user})

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            image = user.picture_set.create(image=form.cleaned_data['image'])
            image.save()
            return redirect('home:index')
            

    else:
        form = UploadImageForm()
   
    return render(request, 'home/upload.html', {'form':form})


def like_image(request):
    image_id = request.GET['image_id']
    image = get_object_or_404(Picture, id=image_id)
    image.likes += 1
    image.save()

    data = { 'is_ok':True, 'likes':image.likes }
        
    return JsonResponse(data) 

