from django import forms
from .models import UserJobInformation


class UserJobInformationForm(forms.ModelForm):
    """
    this form allows user to create job information and detail about their city and country
    """

    class Meta:
        model = UserJobInformation
        exclude = ['user']
        widgets = {
            'job_title': forms.TextInput(
                attrs={'class': 'input is-primary', 'placeholder': 'Username', 'style': 'margin:20px'}),
            'job_description': forms.Textarea(
                attrs={'class': 'textarea', 'placeholder': 'Description', 'style': 'margin:20px'}),
            'city': forms.Select(choices=UserJobInformation.CITY_CHOICES,
                                 attrs={'class': 'dropdown-menu', 'style': 'margin:20px'}),
            'country': forms.Select(choices=UserJobInformation.COUNTRY_CHOICES,
                                    attrs={'class': 'dropdown-menu', 'style': 'margin:20px'}),

        }
