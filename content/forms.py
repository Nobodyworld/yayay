from django import forms
from .models import PersonaChat, PersonaImage

class PersonaChatForm(forms.ModelForm):
    class Meta:
        model = PersonaChat
        fields = ['content', 'is_public']

class PersonaImageForm(forms.ModelForm):
    class Meta:
        model = PersonaImage
        fields = ['image', 'caption', 'is_public']
