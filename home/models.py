from django.db import models
from django.conf import settings
from core.models import Post
from django.utils.text import slugify
from personas.models import Persona  # Ensure you import the Persona model

class HomePageContent(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published')
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Home Page Content"
        verbose_name_plural = "Home Page Contents"

    def __str__(self):
        return self.title

class LandingPage(models.Model):
    title = models.CharField(max_length=200, help_text="Title for the landing page")
    slug = models.SlugField(unique=True, blank=True, help_text="Slug for URL")
    content = models.TextField(help_text="Main content for the landing page")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time the page was created")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Landing Page'
        verbose_name_plural = 'Landing Pages'

class Feed(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_feeds')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='%(class)s_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.post.title} by {self.user.username}'

class PersonaFeed(Feed):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='persona_feeds')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class ChatFeed(Feed):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='chat_feeds')
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.post.title

class ImageFeed(Feed):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='image_feeds')
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.post.title

class PromptsFeed(Feed):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.post.title
