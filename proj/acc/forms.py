from django import forms
from django.core.exceptions import ValidationError

from . import models


class ProfileCreateForm(forms.ModelForm):
    delivery_address = forms.CharField(
        required=True,
        label="Delivery address",
        widget=forms.Textarea
    )

    class Meta:
        model = models.CustomerProfile
        fields = [
            "delivery_address",
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

    #def clean(self, *args, **kwargs):
        #cleaned_data = super().clean(*args, **kwargs)
       # name = cleaned_data["name"]
       # message = cleaned_data["message"]
       # return cleaned_data