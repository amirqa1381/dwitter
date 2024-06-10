from django import forms

from room.models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'input is-primary', 'placeholder': 'Username', 'style': 'margin:20px'})
        }
