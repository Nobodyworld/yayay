from django.views.generic import CreateView, DetailView, ListView
from .models import PersonaChat, PersonaImage
from .forms import PersonaChatForm, PersonaImageForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from personas.models import Persona
from django.shortcuts import get_object_or_404, redirect, render
import logging

logger = logging.getLogger(__name__)
User = get_user_model()

def select_persona(request):
    if request.method == 'POST':
        persona_id = request.POST.get('persona_id')
        request.session['active_persona_id'] = persona_id
        return redirect('content:chat_list')
    personas = Persona.objects.filter(user=request.user)
    context = {
        'personas': personas,
        'mode': 'select'
    }
    return render(request, 'app/content.html', context)

class PersonaChatCreateView(CreateView):
    model = PersonaChat
    form_class = PersonaChatForm
    template_name = 'app/content.html'
    success_url = reverse_lazy('content:chat_list')

    def form_valid(self, form):
        persona_id = self.request.session.get('active_persona_id')
        if not persona_id:
            return redirect('content:select_persona')
        form.instance.persona = get_object_or_404(Persona, pk=persona_id)
        form.instance.user = self.request.user  # Ensure the user is set
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'create_chat'
        context['action_url'] = reverse_lazy('content:chat_create')
        return context

class PersonaChatDetailView(DetailView):
    model = PersonaChat
    template_name = 'app/content.html'
    context_object_name = 'chat'

    def get_queryset(self):
        persona_id = self.request.session.get('active_persona_id')
        if not persona_id:
            return PersonaChat.objects.none()
        return PersonaChat.objects.filter(persona_id=persona_id).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        persona_id = self.request.session.get('active_persona_id')
        if persona_id:
            context['persona'] = get_object_or_404(Persona, pk=persona_id)
        else:
            context['persona'] = None
            context['warning'] = "No active persona selected."
        context['mode'] = 'detail_chat'
        return context

class PersonaChatListView(ListView):
    model = PersonaChat
    template_name = 'app/content.html'
    context_object_name = 'chats'
    paginate_by = 10

    def get_queryset(self):
        persona_id = self.request.session.get('active_persona_id')
        if not persona_id:
            return PersonaChat.objects.none()
        return PersonaChat.objects.filter(persona_id=persona_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        persona_id = self.request.session.get('active_persona_id')
        if persona_id:
            context['persona'] = get_object_or_404(Persona, pk=persona_id)
        else:
            context['persona'] = None
            context['warning'] = "No active persona selected."
        context['mode'] = 'list_chats'
        return context

class PersonaImageCreateView(CreateView):
    model = PersonaImage
    form_class = PersonaImageForm
    template_name = 'app/content.html'
    success_url = reverse_lazy('content:image_list')

    def form_valid(self, form):
        persona_id = self.request.session.get('active_persona_id')
        if not persona_id:
            return redirect('content:select_persona')
        form.instance.persona = get_object_or_404(Persona, pk=persona_id)
        form.instance.user = self.request.user  # Ensure the user is set
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'create_image'
        context['action_url'] = reverse_lazy('content:image_create')
        return context

class PersonaImageDetailView(DetailView):
    model = PersonaImage
    template_name = 'app/content.html'
    context_object_name = 'image'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        persona_id = self.request.session.get('active_persona_id')
        if persona_id:
            context['persona'] = get_object_or_404(Persona, pk=persona_id)
        else:
            context['persona'] = None
            context['warning'] = "No active persona selected."
        context['mode'] = 'detail_image'
        return context

class PersonaImageListView(ListView):
    model = PersonaImage
    template_name = 'app/content.html'
    context_object_name = 'images'
    paginate_by = 10

    def get_queryset(self):
        persona_id = self.request.session.get('active_persona_id')
        logger.debug(f"Active persona ID: {persona_id}")
        if not persona_id:
            return PersonaImage.objects.none()
        return PersonaImage.objects.filter(persona_id=persona_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        persona_id = self.request.session.get('active_persona_id')
        if persona_id:
            context['persona'] = get_object_or_404(Persona, pk=persona_id)
        else:
            context['persona'] = None
            context['warning'] = "No active persona selected."
        context['mode'] = 'list_images'
        return context
