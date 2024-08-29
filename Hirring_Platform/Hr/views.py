# views.py

from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm

def hr(request):
    show_form = request.GET.get('show_form', False)
    form = None
    
    # Fetch all jobs from the database
    jobs = Job.objects.all()

    if show_form:
        if request.method == 'POST':
            form = JobForm(request.POST)
            if form.is_valid():
                form.save()  # Save the job posting
                return redirect('hr')  # Redirect to the HR page after saving
        else:
            form = JobForm()
    
    return render(request, 'hr.html', {'form': form, 'show_form': show_form, 'jobs': jobs})

def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()  # Save the job posting
            return redirect('hr')  # Redirect to the HR page after saving
    else:
        form = JobForm()
    return render(request, 'hr.html', {'form': form, 'show_form': True})
