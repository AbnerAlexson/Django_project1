from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin): # register model into admin
    pass

admin.site.register(Profile, ProfileAdmin) # connects Profile model with ProfileAdmin