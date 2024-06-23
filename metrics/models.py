from django.conf import settings
from django.db import models
from django.db.models import F
from django.db import transaction
from personas.models import Persona
from leveling.models import Skill
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Attribute(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class PersonaMetrics(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, related_name='metrics')
    social_count = models.PositiveIntegerField(default=0)
    achievement_points = models.PositiveIntegerField(default=0)
    total_points = models.IntegerField(default=0)
    total_attempts = models.IntegerField(default=0)
    highest_score = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    average_rating = models.FloatField(default=0.0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    total_upvotes = models.PositiveIntegerField(default=0)
    total_downvotes = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Persona Statistics"

    def __str__(self):
        return f"Metrics for {self.persona.name}"

    def update_metrics(self, points, upvote=False, downvote=False):
        if points < 0:
            raise ValueError("Points cannot be negative.")
        with transaction.atomic():
            self.total_attempts = F('total_attempts') + 1
            self.total_points = F('total_points') + points
            self.highest_score = max(points, self.highest_score)
            if upvote:
                self.total_upvotes = F('total_upvotes') + 1
            if downvote:
                self.total_downvotes = F('total_downvotes') + 1
            self.save()
            self.refresh_from_db()

    def update_rating(self, new_rating):
        with transaction.atomic():
            total_votes = self.total_upvotes + self.total_downvotes
            self.average_rating = ((self.average_rating * total_votes) + new_rating) / (total_votes + 1)
            self.save()

    def increment_socials(self, count=1):
        self.social_count = F('social_count') + count
        self.save()
        self.refresh_from_db()

class Tier(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='tiers')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='tiers')
    level = models.PositiveSmallIntegerField(verbose_name=_("Tier Level"))

    def __str__(self):
        return f"{self.persona.name} - {self.skill.name} - Tier {self.level}"

class Upvote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='upvotes')
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='upvotes')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='upvotes')

    def __str__(self):
        return f"{self.user.username} upvoted {self.persona.name}'s {self.skill.name}"

class Rating(models.Model): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='ratings')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='ratings')
    value = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name=_("Rating Value"))

    def __str__(self):
        return f"{self.user.username} rated {self.persona.name}'s {self.skill.name} as {self.value} stars"
