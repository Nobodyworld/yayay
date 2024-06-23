# File: problems/models.py
from django.db import models
from goals.models import Goal

class Problem(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='problems')
    title = models.CharField(max_length=255, verbose_name="Problem Title")
    description = models.TextField(verbose_name="Problem Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Problem"
        verbose_name_plural = "Problems"
        ordering = ['-created_at']
