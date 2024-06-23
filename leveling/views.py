# File: leveling\views.py
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Skill, Attribute

class AttributeListView(LoginRequiredMixin, ListView):
    model = Attribute
    template_name = 'leveling.html'
    context_object_name = 'attributes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'list_attributes'
        return context

class AttributeDetailView(LoginRequiredMixin, DetailView):
    model = Attribute
    template_name = 'leveling.html'
    context_object_name = 'attribute'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'skills': Skill.objects.filter(attribute=self.object),
        })
        context['mode'] = 'detail_attribute'
        return context

class SkillListView(LoginRequiredMixin, ListView):
    model = Skill
    template_name = 'leveling.html'
    context_object_name = 'skills'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'list_skills'
        return context

class SkillDetailView(LoginRequiredMixin, DetailView):
    model = Skill
    template_name = 'leveling.html'
    context_object_name = 'skill'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'detail_skill'
        return context
