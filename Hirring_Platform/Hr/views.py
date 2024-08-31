# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import HRProfile, Job
from candidate.models import Candidate
from .forms import HRProfileForm, JobForm, JobApplicationForm
from django.apps import apps

# HR Signup View
def hr_signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = HRProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('hr_dashboard')  # Redirect to HR dashboard after signup
    else:
        user_form = UserCreationForm()
        profile_form = HRProfileForm()

    return render(request, 'hr_signup.html', {'user_form': user_form, 'profile_form': profile_form})

# HR Dashboard View
@login_required
def hr_dashboard(request):
    hr_profile = get_object_or_404(HRProfile, user=request.user)
    jobs = Job.objects.filter(hr=hr_profile)
    return render(request, 'hr_dashboard.html', {'jobs': jobs, 'hr_profile': hr_profile})

# Post Job View
@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.hr = get_object_or_404(HRProfile, user=request.user)  # Link the job to the HR profile
            job.save()
            return redirect('hr_dashboard')
    else:
        form = JobForm()
    
    return render(request, 'post_job.html', {'form': form})

# Candidate Dashboard View
@login_required
def hr_dashboard(request):
    HRProfile = apps.get_model('Hr', 'HRProfile')
    Job = apps.get_model('Hr', 'Job')
    hr_profile = HRProfile.objects.get(user=request.user)
    jobs = Job.objects.filter(hr_profile=hr_profile)
    return render(request, 'hr_dashboard.html', {'jobs': jobs})

# Apply for Job View
@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.user = request.user
            candidate.save()
            candidate.applied_jobs.add(job)
            return redirect('candidate_dashboard')
    else:
        form = JobApplicationForm()

    return render(request, 'apply_for_job.html', {'form': form, 'job': job})

# HR Home Page (with Job Form Option)
def hr_home(request):
    show_form = request.GET.get('show_form', False)
    form = None
    
    if show_form:
        if request.method == 'POST':
            form = JobForm(request.POST)
            if form.is_valid():
                form.save()  # Save the job posting
                return redirect('hr_home')  # Redirect to the HR page after saving
        else:
            form = JobForm()
    
    jobs = Job.objects.all()
    return render(request, 'hr_home.html', {'form': form, 'show_form': show_form, 'jobs': jobs})

def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('hr_dashboard')  # Replace 'hr_dashboard' with the name of the URL pattern for HR dashboard
        else:
            return render(request, 'signin.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

    