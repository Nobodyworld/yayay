from django.db import models
from users.models import User
from collectives.models import Collective

class Possession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='possessions')
    collective = models.ForeignKey(Collective, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Possession'
        verbose_name_plural = 'Possessions'
