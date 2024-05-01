from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input is-info', 'placeholder': 'Password', 'style': 'margin: 20px;'}),
        label='')
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'input is-info', 'placeholder': 'Password confirm', 'style': 'margin:20px;'}), label='')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'input is-primary', 'placeholder': 'Username', 'style': 'margin:20px'}),
            'email': forms.EmailInput(
                attrs={'class': 'input is-primary', 'placeholder': 'Email', 'style': 'margin:20px'}),
            'first_name': forms.TextInput(
                attrs={'class': 'input is-info', 'placeholder': 'Optional(First Name)', 'style': 'margin:20px'}),
            'last_name': forms.TextInput(
                attrs={'class': 'input is-info', 'placeholder': 'Optional(Last Name)', 'style': 'margin:20px'}),
        }
        labels = {
            'username': '',
            'email': '',
            'first_name': '',
            'last_name': '',
        }
        required = ('username', 'email', 'password1', 'password2')
        error_messages = {
            'required': {"This field is required."},
        }


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widget = {
            'username': forms.TextInput(
                attrs={'class': 'input is-primary', 'placeholder': 'Username', 'style': 'margin:20px'}),
            'password': forms.PasswordInput(
                attrs={'class': 'input is-primary', 'placeholder': 'Password', 'style': 'margin: 20px;'})
        }
