# home/views.py
from django.shortcuts import render
from .models import HomePageContent, PersonaFeed, ChatFeed, ImageFeed, PromptsFeed, LandingPage
import logging
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, DetailView
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)


def home_view(request):
    try:
        content = HomePageContent.objects.filter(status='published').latest('created_at')
    except HomePageContent.DoesNotExist:
        logger.warning("No published homepage content found.")
        content = None

    context = {
        'content': content,
        'mode': 'home'
    }
    return render(request, 'app/home.html', context)

def index_view(request):
    return render(request, 'app/index.html')

def content_home(request):
    return render(request, 'app/content_home.html')  # Ensure this template exists

class LandingPageView(DetailView):
    model = LandingPage
    template_name = 'app/home.html'
    context_object_name = 'landing_page'

    def get_object(self):
        return LandingPage.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'landing_page'
        return context

class AboutView(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'about'
        return context

class BlogView(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'blog'
        return context

class ContactView(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'contact'
        return context

class FAQView(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'faq'
        return context

class PricingView(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'pricing'
        return context

class PrivacyView(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'privacy'
        return context

class SupportView(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'support'
        return context

class TermsView(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'terms'
        return context

class FeedListView(ListView):
    model = PersonaFeed
    template_name = 'app/home.html'
    paginate_by = 10

    def get_queryset(self):
        feed_type = self.request.GET.get('type', 'all')
        model_map = {
            'chat': ChatFeed,
            'image': ImageFeed,
            'prompts': PromptsFeed,
            'persona': PersonaFeed,
        }
        if feed_type != 'all':
            self.model = model_map[feed_type]
        return self.model.objects.all()

    def get_template_names(self):
        feed_type = self.request.GET.get('type', 'all')
        return [f'app/{feed_type}_feed.html' if feed_type != 'all' else 'app/all_feed.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feed_type'] = self.request.GET.get('type', 'all')
        context['mode'] = 'list_feed'
        return context

def filter_feeds(request):
    feed_type = request.GET.get('type', 'all')
    page = request.GET.get('page', 1)
    items_per_page = int(request.GET.get('limit', 10))

    try:
        model_map = {
            'chat': ChatFeed,
            'image': ImageFeed,
            'prompts': PromptsFeed,
            'persona': PersonaFeed,
        }
        model = model_map.get(feed_type)
        if model:
            queryset = model.objects.all()
        else:
            queryset = list(PersonaFeed.objects.all()) + list(ChatFeed.objects.all()) + list(ImageFeed.objects.all()) + list(PromptsFeed.objects.all())
        
        paginator = Paginator(queryset, items_per_page)
        page_obj = paginator.get_page(page)

        data = {
            'feeds': list(page_obj.object_list.values('title', 'id')),
            'has_next': page_obj.has_next(),
            'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
            'has_previous': page_obj.has_previous(),
            'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
        }
        return JsonResponse(data)

    except ValidationError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': 'Unexpected error occurred.', 'details': str(e)}, status=500)
