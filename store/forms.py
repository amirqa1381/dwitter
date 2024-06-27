from django import forms
from .models import UserJobInformation, Product, ProductComment


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
                attrs={'class': 'input is-primary', 'placeholder': 'Title', 'style': 'margin:20px'}),
            'job_description': forms.Textarea(
                attrs={'class': 'textarea', 'placeholder': 'Description', 'style': 'margin:20px', 'rows': 10}),

        }


class ProductForm(forms.ModelForm):
    """
    this class is for product model for handling the form for submitting the form
    """

    class Meta:
        model = Product
        fields = ['name', 'description', 'serial_number', 'category', 'image']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'input is-info', 'placeholder': 'Product Name', 'style': 'margin:20px'}),
            'serial_number': forms.NumberInput(
                attrs={'class': 'input is-info', 'type': 'number', 'placeholder': 'Serial Number',
                       'style': 'margin:20px'}),
            'image': forms.FileInput(attrs={'class': 'file has-name', 'style': 'margin:30px'}),
            'description': forms.Textarea(
                attrs={'class': 'textarea is-info', 'placeholder': 'Description', 'style': 'margin:20px'}),
            'category': forms.Select(
                attrs={'class': 'dropdown', 'style': 'background-color:#00202E;padding:10px;border-radius:10px'})

        }
        error_messages = {
            'name': {
                'required': ""
            },
            'serial_number': {
                'required': ""
            },
            'image': {
                'required': ""
            },
            'category': {
                'required': ""
            },
            'description': {
                'required': ""
            }
        }


class ProductCommentForm(forms.ModelForm):
    """
    this form is for handling the form part
    """

    class Meta:
        model = ProductComment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(
                attrs={'class': 'textarea', 'placeholder': 'Add a comment...', 'style': 'margin:20px'}),
        }
