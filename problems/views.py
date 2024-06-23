# File: problems/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProblemsForm
from goals.models import Goal

@login_required
def identify_problems(request):
    if request.method == 'POST':
        form = ProblemsForm(request.POST)
        if form.is_valid():
            try:
                goal = Goal.objects.filter(user=request.user).first()
                if not goal:
                    form.add_error(None, "You must have at least one goal to create a problem.")
                else:
                    problem = form.save(commit=False)
                    problem.goal = goal
                    problem.save()
                    return redirect('collectives:explore_collective_problems')
            except Goal.DoesNotExist:
                form.add_error(None, "You must have at least one goal to create a problem.")
    else:
        form = ProblemsForm()
    context = {
        'form': form,
        'mode': 'identify'
    }
    return render(request, 'app/problems.html', context)
