from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy

User = get_user_model()


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address_1 = models.CharField(max_length=250)
    address_2 = models.CharField(max_length=250, default='Address 2')
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    phone = models.CharField(verbose_name="Telephone", max_length=16)

    def __str__(self):
        return f"{self.user.username} profile"

    def get_absolute_url(self):
        return reverse_lazy('accounts:profile-detail', kwargs={"pk": self.pk})