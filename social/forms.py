# File: social\forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Tag, Category, Post
from personas.models import Persona

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter tag name'}),
        }
        help_texts = {
            'name': 'The name of the tag. Must be unique.',
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Tag.objects.filter(name__iexact=name).exists():
            raise ValidationError("A tag with this name already exists.")
        return name

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter category name'}),
        }
        help_texts = {
            'name': 'The name of the category. Must be unique.',
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Category.objects.filter(name__iexact=name).exists():
            raise ValidationError("A category with this name already exists.")
        return name

class PostForm(forms.ModelForm):
    persona = forms.ModelChoiceField(queryset=Persona.objects.all(), required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'persona', 'tags', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter post content'}),
        }
        help_texts = {
            'title': 'The title of the post.',
            'content': 'The content of the post.',
            'persona': 'Optional: Associate this post with a persona.',
            'tags': 'Optional: Add tags to categorize this post.',
            'is_active': 'Indicates whether the post is currently active.',
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()
        if not self.cleaned_data.get('persona') and not self.user:
            raise ValidationError("A post must be associated with either a persona or a user.")
        return self.cleaned_data

    def save(self, commit=True):
        post = super().save(commit=False)
        post.author = self.user
        if commit:
            post.save()
        self.save_m2m()
        return post