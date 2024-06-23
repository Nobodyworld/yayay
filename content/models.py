from django.db import models
from personas.models import Persona

class PersonaChat(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='chats')
    content = models.TextField(help_text="The text content of the chat.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time the chat was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="The date and time the chat was last updated.")
    is_public = models.BooleanField(default=False, help_text="Indicates if the chat is publicly accessible.")

    def __str__(self):
        return f"Chat for {self.persona.name} at {self.created_at}"

class PersonaImage(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='persona_images/', help_text="The image file associated with the persona.")
    caption = models.TextField(blank=True, help_text="Optional caption for the image.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time the image was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="The date and time the image was last updated.")
    is_public = models.BooleanField(default=False, help_text="Indicates if the image is publicly accessible.")

    def __str__(self):
        return f"Image for {self.persona.name} at {self.created_at}"

    class Meta:
        ordering = ['-created_at']
