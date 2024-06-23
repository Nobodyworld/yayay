# File: solutions\views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SolutionForm

@login_required
def create_solution(request):
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.user = request.user
            solution.save()
            return redirect('solutions:solutions_list')  # Ensure 'solutions_list' URL exists
    else:
        form = SolutionForm()
    context = {
        'form': form,
        'mode': 'create_solution'
    }
    return render(request, 'app/solutions.html', context)
