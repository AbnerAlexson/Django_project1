from django.db import models

class Post(models.Model):
    text = models.CharField(max_length=240)

    def __str__(self):
        return self.text[0:100] # this function is so that the character shows in the admin view
