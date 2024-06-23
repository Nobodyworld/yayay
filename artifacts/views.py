# File: artifacts\views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import PersonaArtifact
from .forms import ArtifactForm

def artifacts_list(request):
    artifacts = PersonaArtifact.objects.all()
    context = {
        'artifacts': artifacts,
        'mode': 'list'
    }
    return render(request, 'app/artifacts.html', context)

def artifact_detail(request, artifact_id):
    artifact = get_object_or_404(PersonaArtifact, id=artifact_id)
    context = {
        'artifact': artifact,
        'mode': 'detail'
    }
    return render(request, 'app/artifacts.html', context)

def artifact_upload(request):
    if request.method == 'POST':
        form = ArtifactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artifacts:artifacts_list')
    else:
        form = ArtifactForm()
    context = {
        'form': form,
        'mode': 'create'
    }
    return render(request, 'app/artifacts.html', context)

def artifact_delete(request, artifact_id):
    artifact = get_object_or_404(PersonaArtifact, id=artifact_id)
    if request.method == 'POST':
        artifact.delete()
        return redirect('artifacts:artifacts_list')
    context = {
        'artifact': artifact,
        'mode': 'delete'
    }
    return render(request, 'app/artifacts.html', context)

def artifact_download(request, artifact_id):
    artifact = get_object_or_404(PersonaArtifact, id=artifact_id)
    # Implement file download logic here
    context = {
        'artifact': artifact,
        'mode': 'download'
    }
    return render(request, 'app/artifacts.html', context)
