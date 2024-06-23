from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ProfileCompletionForm
from .models import User

@login_required
def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {
        'user': user,
        'mode': 'profile'
    }
    return render(request, 'app/users.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('users:complete_profile')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        'mode': 'register'
    }
    return render(request, 'app/users.html', context)

@login_required
def complete_profile(request):
    if request.method == 'POST':
        form = ProfileCompletionForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home:home')
    else:
        form = ProfileCompletionForm()
    context = {
        'form': form,
        'mode': 'complete_profile'
    }
    return render(request, 'app/users.html', context)
