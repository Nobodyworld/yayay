from django.shortcuts import render, get_object_or_404, redirect
from .models import Possession
from .forms import PossessionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def possessions_list(request):
    possessions = Possession.objects.filter(user=request.user)
    context = {
        'possessions': possessions,
        'mode': 'list'
    }
    return render(request, 'app/possessions.html', context)

@login_required
def create_possession(request):
    if request.method == 'POST':
        form = PossessionForm(request.POST)
        if form.is_valid():
            possession = form.save(commit=False)
            possession.user = request.user
            possession.save()
            messages.success(request, 'Possession created successfully.')
            return redirect('possessions:possessions_list')
    else:
        form = PossessionForm()
    context = {
        'form': form,
        'mode': 'create'
    }
    return render(request, 'app/possessions.html', context)

@login_required
def update_possession(request, possession_id):
    possession = get_object_or_404(Possession, id=possession_id, user=request.user)
    if request.method == 'POST':
        form = PossessionForm(request.POST, instance=possession)
        if form.is_valid():
            form.save()
            messages.success(request, 'Possession updated successfully.')
            return redirect('possessions:possessions_list')
    else:
        form = PossessionForm(instance=possession)
    context = {
        'form': form,
        'mode': 'update'
    }
    return render(request, 'app/possessions.html', context)

@login_required
def delete_possession(request, possession_id):
    possession = get_object_or_404(Possession, id=possession_id, user=request.user)
    if request.method == 'POST':
        possession.delete()
        messages.success(request, 'Possession deleted successfully.')
        return redirect('possessions:possessions_list')
    context = {
        'possession': possession,
        'mode': 'delete'
    }
    return render(request, 'app/possessions.html', context)
