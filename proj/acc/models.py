from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomerProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE
    )
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user.username} profile"
