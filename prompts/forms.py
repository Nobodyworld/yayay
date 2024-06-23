# File: prompts\forms.py
from django import forms
from .models import Prompts
from personas.models import Persona

class PromptsForm(forms.ModelForm):
    persona = forms.ModelChoiceField(
        queryset=Persona.objects.all(),
        required=False,
        help_text="Select a persona this prompts is associated with, if any."
    )

    class Meta:
        model = Prompts
        fields = ['text', 'author', 'category', 'rating', 'persona']

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 10:
            raise forms.ValidationError("The prompts text must be at least 10 characters long.")
        return text