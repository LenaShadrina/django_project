from django import forms
from django.core.exceptions import ValidationError
from . import models


class ProfileCreateForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        label="First name",
    )
    last_name = forms.CharField(
        required=True,
        label="Last name",
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        )
    address_1 = forms.CharField(
        required=True,
        label="Delivery address 1",
    )
    address_2 = forms.CharField(
        required=True,
        label="Delivery address 2",
    )
    postal_code = forms.CharField(
        required=True,
        label="Postal code",
    )
    city = forms.CharField(
        required=True,
        label="City",
    )
    phone = forms.CharField(
        required=True,
        label="Telephone",
    )
    class Meta:
        model = models.CustomerProfile
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
        ]


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=123,
        min_length=1,
        required=True,
        label="Inter your name"
    )
    message = forms.CharField(
        required=True,
        label="Leave your message",
        widget=forms.Textarea
    )
