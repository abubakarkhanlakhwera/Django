from django.shortcuts import render, redirect, get_object_or_404
from .models import Candidate
from Hr.models import Job
from .form import JobApplicationForm

def candidate_dashboard(req):
    jobs = Job.objects.all()
    return render(req, 'candidate_dashboard.html', {'jobs': jobs})

def apply_for_job(req, job_id):
    job = get_object_or_404(Job, id=job_id)  # Using get_object_or_404 for better error handling

    if req.method == 'POST':
        form = JobApplicationForm(req.POST, req.FILES)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.save()
            candidate.applied_jobs.add(job)  # Add the job to the applied_jobs field
            return redirect('candidate_dashboard')
    else:
        form = JobApplicationForm()  # Initialize an empty form for GET requests

    return render(req, 'apply_for_job.html', {'form': form, 'job': job})
