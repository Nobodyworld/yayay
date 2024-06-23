# File: core\forms.py
from django import forms
from .models import Will, Meaning, Knowledge, Wisdom

class WillForm(forms.ModelForm):
    class Meta:
        model = Will
        fields = ['description']

class MeaningForm(forms.ModelForm):
    class Meta:
        model = Meaning
        fields = ['description']

class KnowledgeForm(forms.ModelForm):
    class Meta:
        model = Knowledge
        fields = ['description']

class WisdomForm(forms.ModelForm):
    class Meta:
        model = Wisdom
        fields = ['description']