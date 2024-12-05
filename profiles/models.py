from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField( # connects django user to profile 
        User,
        on_delete=models.CASCADE, # deletes profiles 
        related_name="profile"
    )

    def __str__(self):
        return self.user.username #give profile name same as username

@receiver(post_save, sender=User) # received when user is made
def create_user_profile(sender, instance, created, **kwargs): #this function creates Profiles
    """Create a new Profile() object when a Django User is created."""
    if created:
        Profile.objects.create(user=instance) # if user is created, new profile is also created