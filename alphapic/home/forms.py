
from django.forms import ModelForm
from .models import Picture, User



class UploadImageForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['image']




