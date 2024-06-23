# File: collectives\forms.py
from django import forms
from .models import Collective

class CollectiveForm(forms.ModelForm):
    class Meta:
        model = Collective
        fields = ['name', 'description']