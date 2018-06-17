
from django.forms import ModelForm
from .models import Picture



class UploadImageForm(ModelForm):

    class Meta:
        model = Picture
        fields = ['image']
