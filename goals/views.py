# File: goals\views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import GoalForm
from .models import Goal

@login_required
def goal_list(request):
    goals = Goal.objects.filter(user=request.user)
    context = {
        'goals': goals,
        'mode': 'list'
    }
    return render(request, 'app/goals.html', context)

@login_required
def goal_detail(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    context = {
        'goal': goal,
        'mode': 'detail'
    }
    return render(request, 'app/goals.html', context)

@login_required
def goal_create(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('goals:goal_list')
    else:
        form = GoalForm()
    context = {
        'form': form,
        'mode': 'create'
    }
    return render(request, 'app/goals.html', context)

@login_required
def goal_update(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goals:goal_list')
    else:
        form = GoalForm(instance=goal)
    context = {
        'form': form,
        'mode': 'update'
    }
    return render(request, 'app/goals.html', context)

@login_required
def goal_delete(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == 'POST':
        goal.delete()
        return redirect('goals:goal_list')
    context = {
        'goal': goal,
        'mode': 'delete'
    }
    return render(request, 'app/goals.html', context)
