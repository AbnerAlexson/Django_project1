from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin): # register model into admin
    pass

admin.site.register(Post, PostAdmin) # connects Post model with PostAdmin