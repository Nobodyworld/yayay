# File: transactions/urls.py
from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path('earn/', views.earn_tokens, name='earn_tokens'),
    path('purchase/', views.purchase_tokens, name='purchase_tokens'),
    path('create/', views.create_transaction, name='create_transaction'),
]
