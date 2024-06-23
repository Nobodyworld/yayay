# File: core\views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.forms import WillForm, MeaningForm, KnowledgeForm, WisdomForm
from core.models import Will, Meaning, Knowledge, Wisdom
from users.forms import UserRegistrationForm, ProfileCompletionForm
from core.utils import calculate_will, calculate_meaning, calculate_knowledge, calculate_wisdom

def landing_page(request):
    context = {'mode': 'landing'}
    return render(request, 'app/core.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('core:complete_profile')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        'mode': 'register'
    }
    return render(request, 'app/core.html', context)

@login_required
def complete_profile(request):
    if request.method == 'POST':
        form = ProfileCompletionForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('core:dashboard')
    else:
        form = ProfileCompletionForm()
    context = {
        'form': form,
        'mode': 'complete_profile'
    }
    return render(request, 'app/core.html', context)

@login_required
def create_will(request):
    if request.method == 'POST':
        form = WillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:dashboard')
    else:
        form = WillForm()
    context = {
        'form': form,
        'mode': 'create_will'
    }
    return render(request, 'app/core.html', context)

@login_required
def create_meaning(request, will_id):
    will = get_object_or_404(Will, id=will_id)
    if request.method == 'POST':
        form = MeaningForm(request.POST)
        if form.is_valid():
            meaning = form.save(commit=False)
            meaning.will = will
            meaning.save()
            return redirect('core:dashboard')
    else:
        form = MeaningForm()
    context = {
        'form': form,
        'will': will,
        'mode': 'create_meaning'
    }
    return render(request, 'app/core.html', context)

@login_required
def create_knowledge(request, meaning_id):
    meaning = get_object_or_404(Meaning, id=meaning_id)
    if request.method == 'POST':
        form = KnowledgeForm(request.POST)
        if form.is_valid():
            knowledge = form.save(commit=False)
            knowledge.meaning = meaning
            knowledge.save()
            return redirect('core:dashboard')
    else:
        form = KnowledgeForm()
    context = {
        'form': form,
        'meaning': meaning,
        'mode': 'create_knowledge'
    }
    return render(request, 'app/core.html', context)

@login_required
def create_wisdom(request, knowledge_id):
    knowledge = get_object_or_404(Knowledge, id=knowledge_id)
    if request.method == 'POST':
        form = WisdomForm(request.POST)
        if form.is_valid():
            wisdom = form.save(commit=False)
            wisdom.knowledge = knowledge
            wisdom.save()
            return redirect('core:dashboard')
    else:
        form = WisdomForm()
    context = {
        'form': form,
        'knowledge': knowledge,
        'mode': 'create_wisdom'
    }
    return render(request, 'app/core.html', context)

@login_required
def dashboard(request):
    user = request.user
    # Calculate attributes (will, meaning, knowledge, wisdom)
    will = calculate_will(user)
    meaning = calculate_meaning(user)
    knowledge = calculate_knowledge(user)
    wisdom = calculate_wisdom(user)

    context = {
        'will': will,
        'meaning': meaning,
        'knowledge': knowledge,
        'wisdom': wisdom,
        'mode': 'dashboard'
    }
    return render(request, 'app/core.html', context)
