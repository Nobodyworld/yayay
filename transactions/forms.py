# File: transactions/forms.py
from django import forms
from .models import TokenTransaction, BadgeTransaction

class TokenTransactionForm(forms.ModelForm):
    class Meta:
        model = TokenTransaction
        fields = ['amount']

class BadgeTransactionForm(forms.ModelForm):
    class Meta:
        model = BadgeTransaction
        fields = ['badge']

class TokenPurchaseForm(forms.ModelForm):
    class Meta:
        model = TokenTransaction
        fields = ['amount']
