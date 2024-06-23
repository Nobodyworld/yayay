# File: goals/models.py
from django.db import models
from django.utils.timezone import now
from users.models import User
from collectives.models import Collective
from django.core.exceptions import ValidationError

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    collective = models.ForeignKey(Collective, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    target_date = models.DateField(default=now)

    def __str__(self):
        return self.title

    def clean(self):
        if self.target_date < now().date():
            raise ValidationError("Target date cannot be in the past.")

    class Meta:
        verbose_name = "Goal"
        verbose_name_plural = "Goals"
        ordering = ['-created_at']
