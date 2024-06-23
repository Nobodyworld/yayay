# File: artifacts\forms.py
from django import forms
from .models import PersonaArtifact

class ArtifactForm(forms.ModelForm):
    class Meta:
        model = PersonaArtifact
        fields = ['title', 'description', 'solution']