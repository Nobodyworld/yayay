from django.contrib import admin
from .models import PersonaChat, PersonaImage

@admin.register(PersonaChat)
class PersonaChatAdmin(admin.ModelAdmin):
    list_display = ('persona', 'created_at', 'is_public')
    search_fields = ('content',)

@admin.register(PersonaImage)
class PersonaImageAdmin(admin.ModelAdmin):
    list_display = ('persona', 'created_at', 'is_public')
    search_fields = ('caption',)
