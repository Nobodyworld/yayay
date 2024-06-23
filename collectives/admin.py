from django.contrib import admin
from .models import Collective

@admin.register(Collective)
class CollectiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
