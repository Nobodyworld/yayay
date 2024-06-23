from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import PersonaMetrics, Attribute, Skill, Tier, Upvote, Rating
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from personas.models import Persona
from django.shortcuts import render

def persona_metrics(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)

    try:
        metrics = PersonaMetrics.objects.get(persona=persona)
    except ObjectDoesNotExist:
        raise Http404("Persona metrics do not exist for the specified persona.")

    data = {
        'persona': persona.name,
        'metrics': {
            'social_count': metrics.social_count,
            'achievement_points': metrics.achievement_points,
            'total_points': metrics.total_points,
            'total_attempts': metrics.total_attempts,
            'highest_score': metrics.highest_score,
            'last_updated': metrics.last_updated.strftime('%Y-%m-%d %H:%M:%S'),
            'average_rating': metrics.average_rating,
            'total_upvotes': metrics.total_upvotes,
            'total_downvotes': metrics.total_downvotes,
        }
    }

    return JsonResponse(data)

class PersonaMetricsDetailView(LoginRequiredMixin, DetailView):
    model = PersonaMetrics
    template_name = 'app/metrics.html'
    context_object_name = 'metrics'

    def get_object(self):
        persona_id = self.kwargs.get('persona_id')
        return get_object_or_404(PersonaMetrics, persona__id=persona_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'detail_metrics'
        return context

class MetricsListView(ListView):
    model = Skill
    template_name = 'app/metrics.html'
    context_object_name = 'skill_scores'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'list_metrics'
        return context

class MetricsDetailView(DetailView):
    model = Skill
    template_name = 'app/metrics.html'
    context_object_name = 'skill_score'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'tiers': Tier.objects.filter(persona=self.object.persona),
            'upvotes': Upvote.objects.filter(persona=self.object.persona),
            'ratings': Rating.objects.filter(persona=self.object.persona)
        })
        context['mode'] = 'detail_metric'
        return context

def analytics_dashboard(request):
    metrics = PersonaMetrics.objects.all()
    context = {
        'metrics': metrics,
        'mode': 'analytics_dashboard'
    }
    return render(request, 'app/metrics.html', context)

class AttributeListView(ListView):
    model = Attribute
    template_name = 'app/metrics.html'
    context_object_name = 'attributes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'list_attributes'
        return context
    
class AttributeDetailView(DetailView):
    model = Attribute
    template_name = 'app/metrics.html'
    context_object_name = 'attribute'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'skills': Skill.objects.filter(attribute=self.object),
        })
        context['mode'] = 'detail_attribute'
        return context
    
class SkillListView(ListView):
    model = Skill
    template_name = 'app/metrics.html'
    context_object_name = 'skills'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'list_skills'
        return context
    
class SkillDetailView(DetailView):
    model = Skill
    template_name = 'app/metrics.html'
    context_object_name = 'skill'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'tiers': Tier.objects.filter(skill=self.object),
            'upvotes': Upvote.objects.filter(skill=self.object),
            'ratings': Rating.objects.filter(skill=self.object)
        })
        context['mode'] = 'detail_skill'
        return context
