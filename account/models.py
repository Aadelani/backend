from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# CUSTOM USER TABLE
class User(AbstractUser):

    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255, null=True)

    USERNAME_FIELD = 'username'


    def __str__(self) -> str:
        return self.username


# CUSTOMER PROFILE MODELS
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="consumer_profile")
    wallet_balance = models.FloatField(null=False, default=0.0)

    def __str__(self) -> str:
        return f"{self.user} Profile"
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_payment")
    amount = models.FloatField(null=False, default=0.0)

    def __str__(self) -> str:
        return self.user.name + self.amount
