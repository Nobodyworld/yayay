# transactions/admin.py

from django.contrib import admin
from .models import TokenTransaction, BadgeTransaction

@admin.register(TokenTransaction)
class TokenTransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'created_at')
    search_fields = ('user__username',)

@admin.register(BadgeTransaction)
class BadgeTransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'badge', 'created_at')
    search_fields = ('user__username', 'badge__name')
