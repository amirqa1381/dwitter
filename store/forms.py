from django import forms
from .models import UserJobInformation


class UserJobInformationForm(forms.ModelForm):
    """
    this form allows user to create job information and detail about their city and country
    """
    city = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'dropdown',
                   'style': 'margin:20px;background-color:#002E27;padding:10px;border-radius:10px'}),
        choices=UserJobInformation.CITY_CHOICES)
    country = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'dropdown',
                   'style': 'margin:20px;background-color:#002E27;padding:10px;border-radius:10px'}),
        choices=UserJobInformation.COUNTRY_CHOICES)

    class Meta:
        model = UserJobInformation
        exclude = ['user', 'is_submitted']
        widgets = {
            'job_title': forms.TextInput(
                attrs={'class': 'input is-primary', 'placeholder': 'Username', 'style': 'margin:20px'}),
            'job_description': forms.Textarea(
                attrs={'class': 'textarea', 'placeholder': 'Description', 'style': 'margin:20px', 'rows': 10}),

        }
