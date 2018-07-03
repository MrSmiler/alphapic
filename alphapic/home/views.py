from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
from .models import User, Picture, ImageLike, Relation
from .forms import UploadImageForm
from django.utils import translation

# Create your views here

@login_required(redirect_field_name='')
def index(request):
    return redirect(reverse('home:real_search', args=(request.user.username,)))

def search_user(request):
    username = request.GET['username']
    return redirect(reverse('home:real_search', args=(username,)))
    

# this invokes when user search for registerd users of the site
def search(request, username):

    another_user = get_object_or_404(User, username=username)
    context = {'another_user':another_user}
    followers_number = another_user.user_followers.count()
    context['follower_number'] = followers_number
    following_number = another_user.user_following.count()
    context['following_number'] = following_number
    if request.user.is_authenticated:
        all_liked_images = request.user.imagelike_set.all()
        liked_images = [ imagelike.picture.id for imagelike in all_liked_images]
        context['liked_images'] = liked_images
        context['is_followed_by_user'] = False
        try:
            relation = Relation.objects.get(following=another_user,
                    follower=request.user)
            context['is_followed_by_user'] = True
        except Relation.DoesNotExist:
            context['is_followed_by_user'] = False


        
    return render(request, 'home/user_navigate.html', context)



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


# this is ajax request handler for liking a image
def like_image(request, image_id):
    if request.user.is_authenticated:
        image = get_object_or_404(Picture, id=image_id)
        try:
            imagelike = ImageLike.objects.get(picture = image, user =
                    request.user)
            data = { 'is_ok':False, 'msg':'you have already liked it'}
        except ImageLike.DoesNotExist:
            imagelike = ImageLike(user = request.user, picture = image)
            imagelike.save()
            image.likes += 1
            image.save()

            data = { 'is_ok':True, 'likes':image.likes }
    else:
        data = { 'is_ok':False}

    return JsonResponse(data) 


# this is ajax request handler for unliking a image
def unlike_image(request, image_id):
    if request.user.is_authenticated:
        image = get_object_or_404(Picture, id=image_id)
        try:
            imagelike = ImageLike.objects.get(picture=image, user = request.user)
        except ImageLike.DoesNotExist:
            data = { 'is_ok':False}
        else :
            imagelike.delete()
            image.likes -= 1
            image.save()

            data = { 'is_ok':True, 'likes':image.likes }
    else:
        data = { 'is_ok':False}

    return JsonResponse(data) 


def follow(request, user_id):
    if request.user.is_authenticated:
        following = get_object_or_404(User, id=user_id)
        try:
            relation = Relation.objects.get(following = following, follower =
                    request.user)
            data = { 'is_ok':False}
        except Relation.DoesNotExist:
            relation = Relation(following=following, follower= request.user)
            relation.save()
            data = { 'is_ok':True }

    else :
        data = {'is_ok':False}

    return JsonResponse(data) 


def unfollow(request, user_id):
    data = {}
    if request.user.is_authenticated:
        following = get_object_or_404(User, id=user_id)
        relation = get_object_or_404(Relation, following=following,
                follower=request.user)
        relation.delete()
        data['is_ok'] = True 
    else:
        data['is_ok'] = False

    return JsonResponse(data)


def change_language(request, language_code):
    translation.activate(language_code)
    request.session[translation.LANGUAGE_SESSION_KEY] = language_code

    if request.user.is_authenticated:
        return redirect(reverse('home:real_search', args=(request.user.username,)))

    return redirect(reverse('home:index'))











