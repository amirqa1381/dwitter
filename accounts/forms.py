from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from main.models import Profile
from django.contrib.auth import update_session_auth_hash

class RegistrationForm(UserCreationForm):
    """
    this form is for registering the new user and we created it for handling it..
    """
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
    """
     this class is for login page and we created it for handling the logining of the user
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input is-primary', 'placeholder': 'Username', 'style': 'margin:20px'}),
        label='', max_length=150)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input is-primary', 'placeholder': 'Password', 'style': 'margin:20px'}), label='',
        max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password')


class UpdateUserInfoForm(UserChangeForm):
    """
    this class is for updating the user info
    """
    password = None
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input is-primary', 'placeholder': 'Username', 'style': 'margin:20px'}),
        label='', max_length=150)
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input is-primary', 'placeholder': 'First Name', 'style': 'margin:20px'}),
        label='', max_length=150)

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input is-primary', 'placeholder': 'Last Name', 'style': 'margin:20px'}),
        label='', max_length=150)

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'input is-primary', 'placeholder': 'Email', 'style': 'margin:20px'}),
        label='', max_length=150)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ImagesetForm(forms.ModelForm):
    """
    This class is for image set form and here we create a form class for images
    """
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'input is-primary', 'style': 'margin:20px'}))

    class Meta:
        model = Profile
        fields = ['image']


class UserPasswordChangeForm(PasswordChangeForm):
    """
    this form is for changing the user password and get the old password and add the new password
    """
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input is-primary', 'placeholder': 'Old Password', 'style': 'margin:20px'}),
        label='Old Password')
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input is-primary', 'placeholder': 'New Password 1', 'style': 'margin:20px'}),
        label='New Password')
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input is-primary', 'placeholder': 'Confirm New Password', 'style': 'margin:20px'}),
        label='Confirm New Password')

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']