from django.contrib import admin
from .models import Possession

@admin.register(Possession)
class PossessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'collective', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'collective')
    ordering = ('-created_at',)
