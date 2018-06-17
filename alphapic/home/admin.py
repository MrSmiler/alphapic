from django.contrib import admin
from .models import User, Picture, Relation

# Register your models here.

admin.site.register(User)
admin.site.register(Picture)
admin.site.register(Relation)


