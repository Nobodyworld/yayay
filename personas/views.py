# File: personas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Persona
from .forms import PersonaForm

def personas_list(request):
    personas = Persona.objects.filter(public=True)
    context = {
        'personas': personas,
        'mode': 'list',
    }
    return render(request, 'app/personas.html', context)

def persona_detail(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    context = {
        'persona': persona,
        'mode': 'detail',
    }
    return render(request, 'app/personas.html', context)

@login_required
def create_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.user = request.user
            persona.save()
            return redirect('personas:index')
    else:
        form = PersonaForm()
    context = {
        'form': form,
        'mode': 'create',
    }
    return render(request, 'app/personas.html', context)

@login_required
def update_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    if request.user != persona.user:
        return redirect('personas:index')
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('personas:index')
    else:
        form = PersonaForm(instance=persona)
    context = {
        'form': form,
        'mode': 'update',
    }
    return render(request, 'app/personas.html', context)

@login_required
def delete_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    if request.user != persona.user:
        return redirect('personas:index')
    if request.method == 'POST':
        persona.delete()
        return redirect('personas:index')
    context = {
        'persona': persona,
        'mode': 'delete',
    }
    return render(request, 'app/personas.html', context)
