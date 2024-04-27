from django import forms
from .models import Dweet


class DweetForm(forms.ModelForm):
    class Meta:
        model = Dweet
        exclude = ("user", "is_active")
        widgets = {
            'content': forms.Textarea(
                attrs={'class': 'textarea is-success is-medium', "placeholder": "Dweet something..."}),
        }
        labels = {
            'content': '',
        }

    def formfield_callback(self, model_field):
        field = super().formfield_callback(model_field)
        if model_field.name == 'content':
            field.required = True
        return field
