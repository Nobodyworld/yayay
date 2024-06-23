from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from personas.models import Persona
from django.db.models import Sum

class Attribute(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Attribute Name"))
    description = models.TextField(verbose_name=_("Description of the attribute"))

    def __str__(self):
        return self.name

class Skill(models.Model):
    attribute = models.ForeignKey(
        Attribute, 
        on_delete=models.CASCADE, 
        related_name='skills', 
        verbose_name=_("Associated Attribute")
    )
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Skill Name"))
    description = models.TextField(blank=True, verbose_name=_("Description of the skill"))

    def __str__(self):
        return f"{self.name} ({self.attribute.name})"

class SkillLevel(models.Model):
    persona = models.ForeignKey(
        Persona, 
        on_delete=models.CASCADE, 
        related_name='persona_skills',
        verbose_name=_("Persona")
    )
    skill = models.ForeignKey(
        Skill, 
        on_delete=models.CASCADE, 
        related_name='persona_skills',
        verbose_name=_("Skill")
    )
    experience_points = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0)],
        verbose_name=_("Experience Points")
    )
    level = models.IntegerField(
        default=1, 
        verbose_name=_("Skill Level")
    )

    def add_experience(self, points):
        self.experience_points += points
        required_points = 100 * self.level
        while self.experience_points >= required_points:
            self.level += 1
            self.experience_points -= required_points
            required_points = 100 * self.level
        self.save()

    def __str__(self):
        return f"{self.persona.name} - {self.skill.name} - Level {self.level}"

class AttributeLevel(models.Model):
    persona = models.ForeignKey(
        Persona,
        on_delete=models.CASCADE,
        related_name='leveling_attributes',
        verbose_name=_("Persona")
    )
    attribute = models.ForeignKey(
        Attribute,
        on_delete=models.CASCADE,
        related_name='persona_attributes',
        verbose_name=_("Attribute")
    )
    total_points = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0)],
        verbose_name=_("Aggregated Total Points")
    )

    def update_total_points(self):
        total = self.persona.persona_skills.filter(skill__attribute=self.attribute).aggregate(sum=Sum('experience_points'))['sum']
        self.total_points = total or 0
        self.save()

    def __str__(self):
        return f"{self.attribute.name} - {self.persona.name}"

    class Meta:
        verbose_name = _("Attribute Level")
        verbose_name_plural = _("Attribute Levels")
