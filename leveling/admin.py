from django.contrib import admin
from .models import Attribute, Skill, SkillLevel

@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'attribute')
    search_fields = ('name', 'description')

@admin.register(SkillLevel)
class SkillLevelAdmin(admin.ModelAdmin):
    list_display = ('persona', 'skill', 'level', 'experience_points')
    search_fields = ('persona__name', 'skill__name')
