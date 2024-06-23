from django import forms
from .models import Possession

class PossessionForm(forms.ModelForm):
    class Meta:
        model = Possession
        fields = ['name', 'description', 'collective']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'collective': forms.Select(attrs={'class': 'form-control'}),
        }
