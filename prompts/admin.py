from django.contrib import admin
from .models import Prompts

@admin.register(Prompts)
class PromptsAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'rating', 'created_at', 'is_active']
    list_filter = ['created_at', 'rating', 'author']
    search_fields = ['text', 'author__username', 'category']
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_public=True)
    make_active.short_description = "Mark selected prompts as active"

    def make_inactive(self, request, queryset):
        queryset.update(is_public=False)
    make_inactive.short_description = "Mark selected prompts as inactive"


