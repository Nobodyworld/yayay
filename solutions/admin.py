from django.contrib import admin
from .models import Solution

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('title', 'problem', 'cost', 'created_at')
    search_fields = ('title', 'description')
