from django.contrib import admin
from .models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'public', 'created_at')
    search_fields = ('name', 'description')
