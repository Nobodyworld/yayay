from django.db import models
from solutions.models import Solution

class PersonaArtifact(models.Model):
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE, related_name='artifacts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
