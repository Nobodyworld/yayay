from django.contrib import admin
from .models import PersonaArtifact

@admin.register(PersonaArtifact)
class PersonaArtifactAdmin(admin.ModelAdmin):
    list_display = ('title', 'solution', 'created_at')
    search_fields = ('title', 'description')
