from django.contrib import admin
from .models import Follower

# Register your models here.

class FollowerAdmin(admin.ModelAdmin): # register model into admin
    pass

admin.site.register(Follower, FollowerAdmin) # connects Follower model with FollowerAdmin
