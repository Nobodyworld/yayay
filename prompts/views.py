from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Prompts
from .forms import PromptsForm

class PromptsListView(ListView):
    model = Prompts
    template_name = 'app/prompts.html'
    context_object_name = 'prompts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'list'
        return context

class PromptsDetailView(DetailView):
    model = Prompts
    template_name = 'app/prompts.html'
    context_object_name = 'prompt'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'detail'
        context['prompts_list_url'] = reverse_lazy('prompts:prompts_list')
        return context

class PromptsCreateView(CreateView):
    model = Prompts
    form_class = PromptsForm
    template_name = 'app/prompts.html'
    success_url = reverse_lazy('prompts:prompts_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'create'
        return context

class PromptsUpdateView(UpdateView):
    model = Prompts
    form_class = PromptsForm
    template_name = 'app/prompts.html'
    success_url = reverse_lazy('prompts:prompts_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'update'
        return context

class PromptsDeleteView(DeleteView):
    model = Prompts
    template_name = 'app/prompts.html'
    success_url = reverse_lazy('prompts:prompts_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'delete'
        context['prompts_list_url'] = reverse_lazy('prompts:prompts_list')
        return context
