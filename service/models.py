from django.db import models
from account.models import User

# Create your models here.


class Job(models.Model):
    STATUS_CHOICES = (
        ("FAILED", "FAILED"),
        ("COMPLETED", "COMPLETED"),
        ("IN PROGRESS", "IN PROGRESS"),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_jobs")
    status = models.CharField(
        max_length=255, choices=STATUS_CHOICES, default=STATUS_CHOICES[0]
    )

    def __str__(self) -> str:
        return self.owner.username