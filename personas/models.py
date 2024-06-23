from django.db import models
from users.models import User

class Persona(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='personas')
    name = models.CharField(max_length=50)
    description = models.TextField()
    public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
