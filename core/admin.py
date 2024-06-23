from django.contrib import admin
from .models import Will, Meaning, Knowledge, Wisdom

@admin.register(Will)
class WillAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at')
    search_fields = ('description',)

@admin.register(Meaning)
class MeaningAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at')
    search_fields = ('description',)

@admin.register(Knowledge)
class KnowledgeAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at')
    search_fields = ('description',)

@admin.register(Wisdom)
class WisdomAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at')
    search_fields = ('description',)
