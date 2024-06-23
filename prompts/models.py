from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from metrics.models import Skill
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils import timezone
from django.core.cache import cache
from django.db.utils import OperationalError
import logging
from django.core.exceptions import ValidationError
from social.models import Category
from content.models import PersonaChat  # Adjust the import

User = get_user_model()

def get_category_choices():
    try:
        cached_choices = cache.get('category_choices')
        if not cached_choices:
            cached_choices = [(cat.id, cat.name) for cat in Category.objects.all()]
            cache.set('category_choices', cached_choices, timeout=86400)
        return cached_choices
    except OperationalError:
        return []

class Prompts(models.Model):
    personas = models.ManyToManyField(
        'personas.Persona',
        related_name='prompts',
        help_text=_("Personas that have engaged with this prompts.")
    )

    PROMPTS_TYPES = [
        ('user_achievement', 'User Achievement'),
        ('general', 'General'),
        ('bonus', 'Bonus'),
        ('cognition', 'Cognition'),
        ('mastery', 'Mastery'),
        ('communication', 'Communication'),
        ('versatility', 'Versatility'),
        ('discipline', 'Discipline'),
        ('research', 'Research'),
    ]

    type = models.CharField(max_length=20, choices=PROMPTS_TYPES, default='general', help_text=_("Defines the social type of the prompts."))
    related_skills = models.ManyToManyField(Skill, blank=True, related_name='prompts', help_text=_("Skills related to the prompts."))
    is_forkable = models.BooleanField(default=True, help_text=_("Indicates if the prompts can be forked or copied."))
    is_leveling = models.BooleanField(default=False, help_text=_("Indicates if the prompts is associated with leveling."))
    engagement_type = models.CharField(max_length=20, help_text=_("Describes the nature of engagement the prompts entails."))
    content_link = models.ForeignKey(PersonaChat, on_delete=models.SET_NULL, null=True, blank=True, help_text=_("Links the prompts to specific persona content."))  # Update reference
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prompts', help_text=_("The user who authored the prompts."))
    category = models.CharField(max_length=3, choices=get_category_choices, default='GEN', help_text=_("Categorizes the prompts for structured social."))
    text = models.TextField(help_text=_("The textual content of the prompts."))
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)], help_text=_("Rates the prompts from 1 (lowest) to 5 (highest)."))
    created_at = models.DateTimeField(auto_now_add=True, help_text=_("Records the creation time of the prompts."))
    is_public = models.BooleanField(default=True, help_text=_("Indicates if the prompts is publicly accessible."))

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.text[:50]}..."

    def save(self, *args, **kwargs):
        creating = not self.pk
        super().save(*args, **kwargs)
        if creating:
            logging.info(f"New prompts created with ID: {self.pk}")
        else:
            logging.info(f"Prompts updated with ID: {self.pk}")

    def get_absolute_url(self):
        return reverse('prompts:prompts_detail', args=[str(self.id)])

    def clean(self):
        if not (1 <= self.rating <= 5):
            raise ValidationError(_('Rating must be between 1 and 5.'))

    @property
    def is_active(self):
        return self.is_public and self.created_at <= timezone.now()
