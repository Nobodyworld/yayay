# File: transactions/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TokenTransaction
from .forms import TokenPurchaseForm, TokenTransactionForm  # Correct the import here

@login_required
def earn_tokens(request):
    transactions = TokenTransaction.objects.filter(user=request.user)
    return render(request, 'earn_tokens.html', {'transactions': transactions})

@login_required
def purchase_tokens(request):
    if request.method == 'POST':
        form = TokenPurchaseForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            transaction = TokenTransaction(user=request.user, amount=amount)
            transaction.save()
            return redirect('transactions:earn_tokens')
    else:
        form = TokenPurchaseForm()
    return render(request, 'purchase_tokens.html', {'form': form})

@login_required
def create_transaction(request):
    if request.method == 'POST':
        form = TokenTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transactions:earn_tokens')
    else:
        form = TokenTransactionForm()
    context = {
        'form': form,
        'mode': 'create_transaction'
    }
    return render(request, 'create_transaction.html', context)
