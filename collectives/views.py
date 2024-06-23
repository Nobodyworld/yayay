# File: collectives\views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Collective
from .forms import CollectiveForm

def collectives_list(request):
    collectives = Collective.objects.all()
    context = {
        'collectives': collectives,
        'mode': 'list'
    }
    return render(request, 'app/collectives.html', context)

def collective_detail(request, collective_id):
    collective = get_object_or_404(Collective, id=collective_id)
    context = {
        'collective': collective,
        'mode': 'detail'
    }
    return render(request, 'app/collectives.html', context)

@login_required
def create_collective(request):
    if request.method == 'POST':
        form = CollectiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('collectives:collectives_list')
    else:
        form = CollectiveForm()
    context = {
        'form': form,
        'mode': 'create'
    }
    return render(request, 'app/collectives.html', context)

@login_required
def join_collective(request):
    collectives = Collective.objects.all()
    if request.method == 'POST':
        collective_id = request.POST.get('collective_id')
        collective = get_object_or_404(Collective, id=collective_id)
        collective.members.add(request.user)
        return redirect('dashboard')  # Ensure 'dashboard' URL exists
    context = {
        'collectives': collectives,
        'mode': 'join'
    }
    return render(request, 'app/collectives.html', context)
