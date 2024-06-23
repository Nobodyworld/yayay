# File: problems/forms.py
from django import forms
from .models import Problem

class ProblemsForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['title', 'description']
        labels = {
            'title': 'Problem Title',
            'description': 'Problem Description',
        }
        help_texts = {
            'title': 'Enter a concise title for the problem.',
            'description': 'Provide a detailed description of the problem.',
        }
