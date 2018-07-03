from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import os

# Create your models here.

class User(AbstractUser):
    # birth date of the user
    birth_date = models.DateField(null=True)

    # biography of the user
    bio = models.TextField(null=True)

    # profile picture of the user
    profile_pic = models.ImageField(upload_to='uploaded/', null=True)

    def how_old(self):
        now = timezone.now()
        age = now.year -  self.birth_date.year  
        if now.month > self.birth_date.month:
            age -= 1
        return age


class Picture(models.Model):

    # a refrence to the image
    image = models.ImageField(upload_to='images/')

    # the user who uploaded this image
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    # number of likes that a image has
    likes = models.IntegerField(default=0)


    def __str__(self):
        
        return os.path.basename(self.image.name)



class Relation(models.Model):

    follower = models.ForeignKey('User', on_delete=models.CASCADE,
            related_name='user_following')
    following = models.ForeignKey('User', on_delete=models.CASCADE,
            related_name='user_followers')


    def __str__(self):
        return str(self.follower) +' follows '+ str(self.following)


class ImageLike(models.Model):
    # this table shows that some user liked some picture

    picture = models.ForeignKey('Picture', on_delete=models.CASCADE)

    user = models.ForeignKey('User', on_delete=models.CASCADE)


