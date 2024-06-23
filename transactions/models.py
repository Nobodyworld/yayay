from django.db import models
from users.models import User
from core.models import Badge

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction: {self.amount} by {self.user.username}"

class TokenTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='token_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"TokenTransaction: {self.amount} by {self.user.username}"

class BadgeTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='badge_transactions')
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"BadgeTransaction: {self.badge.name} to {self.user.username}"
