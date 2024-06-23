from django.contrib import admin
from .models import PersonaMetrics, Tier, Upvote, Rating

@admin.register(PersonaMetrics)
class PersonaMetricsAdmin(admin.ModelAdmin):
    list_display = ('persona', 'social_count', 'achievement_points', 'total_points', 'total_attempts', 'highest_score', 'average_rating', 'total_upvotes', 'total_downvotes', 'last_updated')
    search_fields = ('persona__name',)

@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    list_display = ('persona', 'skill', 'level')
    search_fields = ('persona__name', 'skill__name')

@admin.register(Upvote)
class UpvoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'persona', 'skill')
    search_fields = ('user__username', 'persona__name', 'skill__name')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'persona', 'skill', 'value')
    search_fields = ('user__username', 'persona__name', 'skill__name')
