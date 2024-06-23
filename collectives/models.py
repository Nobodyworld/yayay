# File: collectives/models.py
from django.db import models
from users.models import User

class Collective(models.Model):
    name = models.CharField(max_length=255, verbose_name="Collective Name")
    description = models.TextField(verbose_name="Description")
    members = models.ManyToManyField(User, related_name='collectives', verbose_name="Members")

    class Meta:
        verbose_name = "Collective"
        verbose_name_plural = "Collectives"
        ordering = ['name']

    def __str__(self):
        return self.name
