from django.db import models
from django.contrib.auth.models import AbstractUser
import os

# Create your models here.

class User(AbstractUser):
    # birth date of the user
    birth_date = models.DateField(null=True)

    # biography of the user
    bio = models.TextField(null=True)

    # profile picture of the user
    profile_pic = models.ImageField(upload_to='uploaded/', null=True)




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

    following = models.ForeignKey('User', on_delete=models.CASCADE, related_name='who_follows')

    follower = models.ForeignKey('User', on_delete=models.CASCADE, related_name='who_is_followed')


