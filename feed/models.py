from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    text = models.CharField(max_length=240)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey( # this is the author of the post 
        User,
        on_delete=models.CASCADE, # deletes author when post is the delete
    )


    def __str__(self):
        return self.text[0:100] # this function is so that the character shows in the admin view