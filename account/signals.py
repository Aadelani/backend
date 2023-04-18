from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile
from random import randint

# PROFILES SIGNALS (Profile && TechnicianProfile)
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # randomly choosing color from the COLOR_SCHEME

    if created:
        Profile.objects.create(user=instance, wallet_balance=0.00)
        
post_save.connect(create_profile, sender=User)